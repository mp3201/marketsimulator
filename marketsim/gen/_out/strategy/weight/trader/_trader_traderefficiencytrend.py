# generated with class generator.python.curried$after_typing$Curried
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
@registry.expose(["Strategy", "trader_TraderEfficiencyTrend"])
class trader_TraderEfficiencyTrend_Float(IFunctionIFunctionfloat_from_IAccount):
    """ **Returns first derivative of a moving average of the trader efficiency**
    
    
    Parameters are:
    
    **alpha**
    	 parameter alpha for the moving average 
    """ 
    def __init__(self, alpha = None):
        self.alpha = alpha if alpha is not None else 0.15
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float
    }
    
    
    def __repr__(self):
        return "trader_TraderEfficiencyTrend(%(alpha)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.alpha)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.weight._traderefficiencytrend import TraderEfficiencyTrend_IAccountFloat as _strategy_weight_TraderEfficiencyTrend_IAccountFloat
        trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        alpha = self.alpha
        return _strategy_weight_TraderEfficiencyTrend_IAccountFloat(trader,alpha)
    
def trader_TraderEfficiencyTrend(alpha = None): 
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        return trader_TraderEfficiencyTrend_Float(alpha)
    raise Exception('Cannot find suitable overload for trader_TraderEfficiencyTrend('+str(alpha) +':'+ str(type(alpha))+')')
