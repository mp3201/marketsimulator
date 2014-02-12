from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "MeanReversion"])
class MeanReversion_IEventSideIOrderGeneratorFloat(ISingleAssetStrategy):
    """  It estimates this average using some functional and
     if the current asset price is lower than the average
     it buys the asset and if the price is higher it sells the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_IFunctionFloat as _order__curried_side_Market_IFunctionFloat
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float(_math_random_expovariate_Float(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market_IFunctionFloat()
        self.ewma_alpha = ewma_alpha if ewma_alpha is not None else 0.15
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]],
        'ewma_alpha' : float
    }
    def __repr__(self):
        return "MeanReversion(%(eventGen)s, %(orderFactory)s, %(ewma_alpha)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IOrderGeneratorIEvent as _strategy_Generic_IOrderGeneratorIEvent
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_FloatIOrderBook as _strategy_side_MeanReversion_FloatIOrderBook
        return _strategy_Generic_IOrderGeneratorIEvent(self.orderFactory(_strategy_side_MeanReversion_FloatIOrderBook(self.ewma_alpha)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MeanReversion(eventGen = None,orderFactory = None,ewma_alpha = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]]):
            if ewma_alpha is None or rtti.can_be_casted(ewma_alpha, float):
                return MeanReversion_IEventSideIOrderGeneratorFloat(eventGen,orderFactory,ewma_alpha)
    raise Exception('Cannot find suitable overload for MeanReversion('+str(eventGen)+','+str(orderFactory)+','+str(ewma_alpha)+')')
