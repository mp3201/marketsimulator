class String(object):
    def S1(self):
        from marketsim.gen._out._test.in1.in2._s1 import S1
        return S1(self)
    
    def Graph(self):
        from marketsim.gen._out.veusz._graph import Graph
        return Graph(self)
    
    def Quote(self, start = None,end = None):
        from marketsim.gen._out.observable._quote import Quote
        return Quote(self,start,end)
    
    def MarketData(self, start = None,end = None,delta = None,volume = None):
        from marketsim.gen._out.strategy._marketdata import MarketData
        return MarketData(self,start,end,delta,volume)
    
    def Local(self, tickSize = None,_digitsToShow = None,timeseries = None):
        from marketsim.gen._out.orderbook._local import Local
        return Local(self,tickSize,_digitsToShow,timeseries)
    
    pass