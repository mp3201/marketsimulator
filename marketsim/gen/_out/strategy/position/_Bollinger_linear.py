from marketsim import ISingleAssetTrader
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Volume
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Volume function", "Bollinger_linear"])
class Bollinger_linear_FloatIObservableFloatISingleAssetTrader(Observable[Volume]):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import Volume
        from marketsim import event
        Observable[Volume].__init__(self)
        self.alpha = alpha if alpha is not None else 0.15
        self.k = k if k is not None else _const_Float(0.5)
        self.trader = trader if trader is not None else _trader_SingleProxy_()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'k' : IObservable[float],
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "Bollinger_linear(%(alpha)s, %(k)s, %(trader)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.position._desiredposition import DesiredPosition_IObservableFloatISingleAssetTrader as _strategy_position_DesiredPosition_IObservableFloatISingleAssetTrader
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatIFunctionFloat as _observable_OnEveryDt_FloatIFunctionFloat
        from marketsim.gen._out.math.EW._relstddev import RelStdDev_IObservableFloatFloat as _math_EW_RelStdDev_IObservableFloatFloat
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        return _strategy_position_DesiredPosition_IObservableFloatISingleAssetTrader(_observable_OnEveryDt_FloatIFunctionFloat(1.0,_ops_Mul_IObservableFloatIObservableFloat(_math_EW_RelStdDev_IObservableFloatFloat(_orderbook_MidPrice_IOrderBook(_orderbook_OfTrader_IAccount(self.trader)),self.alpha),self.k)),self.trader)
    
def Bollinger_linear(alpha = None,k = None,trader = None): 
    from marketsim import float
    from marketsim import IObservable
    from marketsim import ISingleAssetTrader
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        if k is None or rtti.can_be_casted(k, IObservable[float]):
            if trader is None or rtti.can_be_casted(trader, ISingleAssetTrader):
                return Bollinger_linear_FloatIObservableFloatISingleAssetTrader(alpha,k,trader)
    raise Exception('Cannot find suitable overload for Bollinger_linear('+str(alpha)+','+str(k)+','+str(trader)+')')
