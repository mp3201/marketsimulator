def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out.order._curried._sideprice_immediateorcancel import sideprice_ImmediateOrCancel_SideFloatIOrderGenerator as _order__curried_sideprice_ImmediateOrCancel_SideFloatIOrderGenerator
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[Side]
    ,IFunction[float]]):
        return _order__curried_sideprice_ImmediateOrCancel_SideFloatIOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
