from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.orderbook.props import TickSize_Impl
from marketsim.gen._out._iorderbook import IOrderBook
@registry.expose(["Asset", "TickSize"])
class TickSize_IOrderBook(IFunctionfloat,TickSize_Impl):
    """ **Returns tick size for the order *book***
    
    
    Parameters are:
    
    **book**
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim import rtti
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
        TickSize_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    
    
    def __repr__(self):
        return "TickSize(%(book)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.book.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def TickSize(book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return TickSize_IOrderBook(book)
    raise Exception('Cannot find suitable overload for TickSize('+str(book) +':'+ str(type(book))+')')
