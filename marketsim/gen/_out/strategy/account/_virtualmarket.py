from marketsim import registry
from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._intrinsic.strategy.account import VirtualMarket_Impl
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Strategy", "VirtualMarket"])
class VirtualMarket_ISingleAssetStrategy(IAccount,VirtualMarket_Impl):
    """ **Associated with a strategy account that evaluates for every order sent by the strategy**
    
      how it would be traded by sending request.evalMarketOrder
      (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
      but we want evaluate in any case would it be profitable or not)
    
    Parameters are:
    
    **inner**
    	 strategy to track 
    """ 
    def __init__(self, inner = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_Empty_())
        rtti.check_fields(self)
        VirtualMarket_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy
    }
    
    
    def __repr__(self):
        return "VirtualMarket(%(inner)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.inner.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def VirtualMarket(inner = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        return VirtualMarket_ISingleAssetStrategy(inner)
    raise Exception('Cannot find suitable overload for VirtualMarket('+str(inner) +':'+ str(type(inner))+')')
def virtualMarket(): 
    from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
    from marketsim import rtti
    return _strategy_account_inner_inner_VirtualMarket_()
    raise Exception('Cannot find suitable overload for virtualMarket('++')')
