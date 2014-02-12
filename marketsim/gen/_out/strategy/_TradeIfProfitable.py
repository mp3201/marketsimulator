from marketsim import IFunction
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "TradeIfProfitable"])
class TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountIFunctionFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, inner = None, account = None, performance = None):
        from marketsim.gen._out.strategy.weight.trader._trader_efficiencytrend import trader_EfficiencyTrend_Float as _strategy_weight_trader_trader_EfficiencyTrend_Float
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIOrderGenerator as _strategy_Noise_IEventSideIOrderGenerator
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim import event
        self.inner = inner if inner is not None else _strategy_Noise_IEventSideIOrderGenerator()
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket_()
        self.performance = performance if performance is not None else _strategy_weight_trader_trader_EfficiencyTrend_Float()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'account' : IFunction[IAccount,ISingleAssetStrategy],
        'performance' : IFunction[IFunction[float],IAccount]
    }
    def __repr__(self):
        return "TradeIfProfitable(%(inner)s, %(account)s, %(performance)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._suspendable import Suspendable_ISingleAssetStrategyIFunctionBoolean as _strategy_Suspendable_ISingleAssetStrategyIFunctionBoolean
        from marketsim.gen._out.ops._greaterequal import GreaterEqual_IFunctionFloatIFunctionFloat as _ops_GreaterEqual_IFunctionFloatIFunctionFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        return _strategy_Suspendable_ISingleAssetStrategyIFunctionBoolean(self.inner,_ops_GreaterEqual_IFunctionFloatIFunctionFloat(self.performance(self.account(self.inner)),_constant_Int(0)))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def TradeIfProfitable(inner = None,account = None,performance = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import ISingleAssetStrategy
    from marketsim import IAccount
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        if account is None or rtti.can_be_casted(account, IFunction[IAccount,ISingleAssetStrategy]):
            if performance is None or rtti.can_be_casted(performance, IFunction[IFunction[float],IAccount]):
                return TradeIfProfitable_ISingleAssetStrategyISingleAssetStrategyIAccountIAccountIFunctionFloat(inner,account,performance)
    raise Exception('Cannot find suitable overload for TradeIfProfitable('+str(inner)+','+str(account)+','+str(performance)+')')
