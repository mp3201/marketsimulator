from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
from marketsim import context
@registry.expose(["Side function", "book"])
class book_strategysideMeanReversion(IOrderBook):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_Float as _strategy_side_MeanReversion_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    
    
    def __repr__(self):
        return "book(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        return deref_opt(_orderbook_OfTrader_IAccount())
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
from marketsim import context
@registry.expose(["Side function", "book"])
class book_strategysideFundamentalValue(IOrderBook):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_Float as _strategy_side_FundamentalValue_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    
    
    def __repr__(self):
        return "book(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        return deref_opt(_orderbook_OfTrader_IAccount())
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
from marketsim import context
@registry.expose(["Side function", "book"])
class book_strategysidePairTrading(IOrderBook):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloat as _strategy_side_PairTrading_IOrderBookFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : PairTrading
    }
    
    
    def __repr__(self):
        return "book(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
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
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        return deref_opt(_orderbook_OfTrader_IAccount())
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def book(x = None): 
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return book_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return book_strategysideFundamentalValue(x)
    if x is None or rtti.can_be_casted(x, PairTrading):
        return book_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for book('+str(x) +':'+ str(type(x))+')')
from marketsim import registry
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
@registry.expose(["-", "Book"])
class Book_strategysideTrendFollower(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower
    }
    
    
    def __repr__(self):
        return "Book(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.book
    
from marketsim import registry
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
@registry.expose(["-", "Book"])
class Book_strategysideCrossingAverages(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages
    }
    
    
    def __repr__(self):
        return "Book(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.book
    
def Book(x = None): 
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Book_strategysideTrendFollower(x)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Book_strategysideCrossingAverages(x)
    raise Exception('Cannot find suitable overload for Book('+str(x) +':'+ str(type(x))+')')
