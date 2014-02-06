from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "ImmediateOrCancel"])
class sideprice_ImmediateOrCancel(IFunction[IOrderGenerator,IFunction[Side]
,IFunction[float]]):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit as _order__curried_sideprice_Limit
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sideprice_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel
        side = side if side is not None else _side_Sell()
        price = price if price is not None else _constant(100.0)
        proto = self.proto
        return ImmediateOrCancel(proto(side,price))
    
sideprice_ImmediateOrCancel = sideprice_ImmediateOrCancel
