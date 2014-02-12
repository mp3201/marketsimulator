from marketsim import IFunction
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import listOf
from marketsim import registry
from marketsim.gen._intrinsic.strategy.choose_the_best import _ChooseTheBest_Impl
from marketsim import float
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountIFunctionFloat(_ChooseTheBest_Impl):
    """  In some moments of time the most effective strategy
     is chosen and made running; other strategies are suspended.
     It can be considered as a particular case for MultiArmedBandit strategy with
     *corrector* parameter set to *chooseTheBest*
    """ 
    def __init__(self, strategies = None, account = None, performance = None):
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIOrderGenerator as _strategy_Noise_IEventSideIOrderGenerator
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim.gen._out.strategy.weight.trader._trader_efficiencytrend import trader_EfficiencyTrend_Float as _strategy_weight_trader_trader_EfficiencyTrend_Float
        from marketsim import rtti
        self.strategies = strategies if strategies is not None else [_strategy_Noise_IEventSideIOrderGenerator()]
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket_()
        self.performance = performance if performance is not None else _strategy_weight_trader_trader_EfficiencyTrend_Float()
        rtti.check_fields(self)
        _ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy),
        'account' : IFunction[IAccount,ISingleAssetStrategy],
        'performance' : IFunction[IFunction[float],IAccount]
    }
    def __repr__(self):
        return "ChooseTheBest(%(strategies)s, %(account)s, %(performance)s)" % self.__dict__
    
def ChooseTheBest(strategies = None,account = None,performance = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import listOf
    from marketsim import ISingleAssetStrategy
    from marketsim import IAccount
    if strategies is None or rtti.can_be_casted(strategies, listOf(ISingleAssetStrategy)):
        if account is None or rtti.can_be_casted(account, IFunction[IAccount,ISingleAssetStrategy]):
            if performance is None or rtti.can_be_casted(performance, IFunction[IFunction[float],IAccount]):
                return ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountIFunctionFloat(strategies,account,performance)
    raise Exception('Cannot find suitable overload for ChooseTheBest('+str(strategies)+','+str(account)+','+str(performance)+')')
