from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class price_ImmediateOrCancel_FloatIOrderGenerator(IFunction[IOrderGenerator,IFunction[float]]):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideIFunctionFloat as _order__curried_price_Limit_SideIFunctionFloat
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_price_Limit_SideIFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        price = price if price is not None else _constant_Float(100.0)
        proto = self.proto
        return ImmediateOrCancel(proto(price))
    
def price_ImmediateOrCancel(proto = None): 
    from marketsim import IOrderGenerator
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
        return price_ImmediateOrCancel_FloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for price_ImmediateOrCancel('+str(proto)+')')
