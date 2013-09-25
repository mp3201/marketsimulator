from templet import stringfunction
from werkzeug.utils import cached_property
from .. import types
from types import *

from base import *

class Gen(Base):
    
    def __init__(self, cls, alias, rvtype=float):
        Base.__init__(self, cls)
        self._alias = alias
        self.rvtype = rvtype.__name__
        
    @property
    def alias(self):
        return self._alias
        
    @property
    @stringfunction
    def baseclass(self):
        "ops.Function[${self.rvtype}]"
        
    @property
    def category(self):
        return "Random"
            
    @stringfunction
    def casts_to(self):
        """
        ${{}}

            def _casts_to(self, dst):
                return ${self.name}._types[0]._casts_to(dst)
        """

        
    @cached_property
    def callfields(self):
        return self.joinfields("self.%(name)s")
    
    @property
    def implmodule(self):
        return "random"
    
    def members(self):
        return Base.members(self) + """
            call
            casts_to
        """ 

defs = ["from marketsim import registry, types, ops", "import random"]

def imported(alias, t = float):
    
    def inner(cls):
        defs.append(Gen(cls, alias, t)())
        exec Meta(cls)() in globals()
        return globals()[cls.__name__]
    
    return inner
