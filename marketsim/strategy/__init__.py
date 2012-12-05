from _adaptive import (suspendIfNotEffective, withEstimator, chooseTheBest, 
                       tradeIfProfitable, chooseTheBestEx)

import random
from marketsim import order, mathutils, Side

from _basic import Wrapper, currentframe

import _misc, _arbitrage, _fv, _trend, _lp

def LiquidityProviderSide(\
                 side=Side.Sell,
                 orderFactoryT=order.Limit.T,
                 defaultValue=100,
                 creationIntervalDistr=(lambda: random.expovariate(1.)),
                 priceDistr=(lambda: random.lognormvariate(0., .1)),
                 volumeDistr=(lambda: random.expovariate(.1))):
    
    return Wrapper.fromFrame(_lp._LiquidityProviderSide_Impl, currentframe())
    
def LiquidityProvider(\
                 orderFactoryT=order.Limit.T,
                 defaultValue=100,
                 creationIntervalDistr=(lambda: random.expovariate(1.)),
                 priceDistr=(lambda: random.lognormvariate(0., .1)),
                 volumeDistr=(lambda: random.expovariate(.1))):
    
    return Wrapper.fromFrame(_lp._LiquidityProvider_Impl, currentframe())

def Canceller(cancellationIntervalDistr=(lambda: random.expovariate(1.)),
              choiceFunc=lambda N: random.randint(0,N-1)):
    """ Initializes canceller with 
    cancellationIntervalDistr - intervals of times between order cancellations
                                (default: exponential distribution with \lambda=1)
    choiceFunc - function N -> idx that chooses which order should be cancelled
    """
    return Wrapper.fromFrame(_lp._Canceller_Impl, currentframe())

def Noise(orderFactoryT=order.Market.T,
          sideDistr=lambda: random.randint(0,1),
          volumeDistr=lambda: random.expovariate(.1),
          creationIntervalDistr=lambda: random.expovariate(1.)):
    """ Noise(trader,\
          orderFactoryT=order.Market.T,\
          sideDistr=lambda: random.randint(0,1),\
          volumeDistr=lambda: random.expovariate(.1),\
          creationIntervalDistr=lambda: random.expovariate(1.))
    
    Creates a noise trader: a trader that randomly chooses a side and volume to trade
    
    Arguments:
    
        **trader**
            single asset single market trader
            
        **orderFactoryT**
            order factory function (default: MarketOrderT)
        
        **sideDistr**
            side of orders to create
            (default: discrete uniform distribution P(Sell)=P(Buy)=.5)
    
        **creationIntervalDistr**
            defines intervals of time between order creation 
            (default: exponential distribution with \lambda=1)
    
        **volumeDistr**
            defines volumes of orders to create
            (default: exponential distribution with \lambda=1)
    """
    
    return Wrapper.fromFrame(_misc._Noise_Impl, currentframe())


def Arbitrage(sched=None):
    return Wrapper.fromFrame(_arbitrage._Arbitrage_Impl, currentframe())

def FundamentalValue(orderFactory=order.Market.T,
                     fundamentalValue=lambda: 100,
                     volumeDistr= lambda: random.expovariate(1.),
                     creationIntervalDistr=lambda: random.expovariate(1.)):
    """ Creates a fundamental value trader
    trader - single asset single market trader
    orderFactoryT - order factory function: side -> *orderParams -> Order
    fundamentalValue - defines fundamental value 
                            (default: constant 100)
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    """
    return Wrapper.fromFrame(_fv._FundamentalValue_Impl, currentframe())

def MeanReversion(orderFactory=order.Market.T,
                  average = mathutils.ewma(alpha = 0.15),
                  volumeDistr= lambda: random.expovariate(1.),
                  creationIntervalDistr=lambda: random.expovariate(1.)):
    
    return Wrapper.fromFrame(_fv._MeanReversion_Impl, currentframe())


def Dependency(bookToDependOn,
               orderFactory=order.Market.T,
               factor=1.,
               volumeDistr=lambda: random.expovariate(.1)):
    """ Creates a strategy that believes that fair asset price 
    can be obtained as current price of another asset multiplied by some factor
    Once this relation doesn't hold it tries to buy or sell orders with better price     

    trader - single asset single market trader
    bookToDependOn - asset that is considered as reference one
    orderFactory - order factory function: side -> *orderParams -> Order
    factor - multiplier to obtain fair the asset price by reference price
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    
    return Wrapper.fromFrame(_fv._Dependency_Impl, currentframe())

def Signal(signal,
           threshold=0.7,
           orderFactory=order.Market.T,
           volumeDistr=(lambda: random.expovariate(1.))):
    """ Creates a signal trader.
    trader - single asset single market trader
    signal - signal to be listened to 
    threshold - threshold when the trader starts to act
    orderFactory - order factory function: side -> *orderParams -> Order
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
    return Wrapper.fromFrame(_trend._Signal_Impl, currentframe())

def TwoAverages(average1 = mathutils.ewma(alpha = 0.15),
                average2 = mathutils.ewma(alpha = 0.015),
                threshold = 0., 
                orderFactory=order.Market.T,
                creationIntervalDistr=(lambda: random.expovariate(1.)),
                volumeDistr=(lambda: random.expovariate(1.))):

    return Wrapper.fromFrame(_trend._TwoAverages_Impl, currentframe())

def TrendFollower(average = mathutils.ewma(alpha = 0.15),
                  threshold = 0., 
                  orderFactory=order.Market.T,
                  creationIntervalDistr=(lambda: random.expovariate(1.)),
                  volumeDistr=(lambda: random.expovariate(1.))):
    """ Creates a trend follower trader
    trader - single asset single market trader
    average - moving average object (update(time,value); derivativeAt(time))
    threshold - threshold of the moving average derivate when the trader starts to act
    orderFactory - order factory function: side -> *orderParams -> Order
    creationIntervalDistr - defines intervals of time between order creation 
                            (default: exponential distribution with \lambda=1)
    volumeDistr - function to determine volume of orders to create 
                            (default: exponential distribution with \lambda=1) 
    """
     
    return Wrapper.fromFrame(_trend._TrendFollower_Impl, currentframe())