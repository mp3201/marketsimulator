from marketsim import request, event, _, Event, combine, ops, types
from marketsim.types import *

from _limit_market import LimitMarket

from _base import *

class FixedBudget(Default, HasSide, HasVolume, Cancellable):
    
    def __init__(self, side, budget):
        HasSide.__init__(self, side)
        HasVolume.__init__(self, None)
        Cancellable.__init__(self)
        self.budget = budget

    def onOrderMatched(self, order, price, volume):
        self.budget -= price*volume
        self.onMatchedWith(price, volume)
        
    def onOrderDisposed(self, order):
        self._ordersSent -= 1
        if self._ordersSent == 0:
            self.cancel()
        
    def processIn(self, orderBook):
        orderBook.process(
                    request.EvalVolumesForBudget(
                                self.side, self.budget, 
                                _(self, orderBook)._onEvaluated))
        
    def _onEvaluated(self, orderBook, pvs):
        self._ordersSent = 0
        self._volumeUnmatched = sum([v for p,v in pvs])
        for p,v in pvs:
            order = LimitMarket(self.side, p, v)
            order.owner = self
            orderBook.process(order)
            self._ordersSent += 1
            
    def __repr__(self):
        return 'FixedBudget(%s,%s)' % (self.side, self.budget)
            

class Factory(types.IOrderGenerator, combine.SideBudget):
    
    def __call__(self):
        params = combine.SideBudget.__call__(self)
        return FixedBudget(*params) if params is not None else None
