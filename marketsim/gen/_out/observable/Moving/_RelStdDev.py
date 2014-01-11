from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev(Observable[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const as _const
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.source = source if source is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 100.0
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "RSD_{n=%(timeframe)s}_{%(source)s}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable.Moving._Avg import Avg as _observable_Moving_Avg
        from marketsim.gen._out.observable.Moving._StdDev import StdDev as _observable_Moving_StdDev
        return (self.source-_observable_Moving_Avg(self.source,self.timeframe))/_observable_Moving_StdDev(self.source,self.timeframe)
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
