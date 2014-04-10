from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "weibullvariate"])
class weibullvariate_FloatFloat(IFunctionfloat):
    """ **Weibull distribution**
    
    
    Parameters are:
    
    **Alpha**
    	 |alpha| is the scale parameter 
    
    **Beta**
    	 |beta| is the shape parameter  
    """ 
    def __init__(self, Alpha = None, Beta = None):
        from marketsim import rtti
        self.Alpha = Alpha if Alpha is not None else 1.0
        self.Beta = Beta if Beta is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float,
        'Beta' : float
    }
    
    
    
    
    def __repr__(self):
        return "weibullvariate(%(Alpha)s, %(Beta)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        
        delattr(self, '_processing_ex')
    
    def __call__(self, *args, **kwargs):
        import random
        return random.weibullvariate(self.Alpha, self.Beta)
    
    def _casts_to(self, dst):
        return weibullvariate_FloatFloat._types[0]._casts_to(dst)
    
def weibullvariate(Alpha = None,Beta = None): 
    from marketsim import rtti
    if Alpha is None or rtti.can_be_casted(Alpha, float):
        if Beta is None or rtti.can_be_casted(Beta, float):
            return weibullvariate_FloatFloat(Alpha,Beta)
    raise Exception('Cannot find suitable overload for weibullvariate('+str(Alpha) +':'+ str(type(Alpha))+','+str(Beta) +':'+ str(type(Beta))+')')
