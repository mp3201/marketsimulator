def StopLoss(maxloss = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim.gen._out.order._curried._volume_price_stoploss import volume_price_StopLoss_IFunctionFloatFloatFloatIOrderGenerator as _order__curried_volume_price_StopLoss_IFunctionFloatFloatFloatIOrderGenerator
    if maxloss is None or rtti.can_be_casted(maxloss, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return _order__curried_volume_price_StopLoss_IFunctionFloatFloatFloatIOrderGenerator(maxloss,proto)
    raise Exception('Cannot find suitable overload for StopLoss('+str(maxloss)+','+str(proto)+')')
