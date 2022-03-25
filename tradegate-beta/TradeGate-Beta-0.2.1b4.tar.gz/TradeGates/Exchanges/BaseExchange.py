from abc import ABC, abstractmethod


class BaseExchange(ABC):
    @abstractmethod
    def __init__(self, credentials, sandbox=False, unifiedInOuts=True):
        pass

    @abstractmethod
    def getBalance(self, asset='', futures=False):
        pass

    @abstractmethod
    def symbolAccountTradeHistory(self, symbol, futures=False, fromId=None, limit=None):
        pass

    @abstractmethod
    def testSpotOrder(self, orderData):
        pass

    @abstractmethod
    def makeSpotOrder(self, orderData):
        pass

    @abstractmethod
    def getSymbolOrders(self, symbol, futures=False, orderId=None, startTime=None, endTime=None, limit=None):
        pass

    @abstractmethod
    def getOpenOrders(self, symbol, futures=False):
        pass

    @abstractmethod
    def cancelAllSymbolOpenOrders(self, symbol, futures=False):
        pass

    @abstractmethod
    def cancelOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        pass

    @abstractmethod
    def getOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        pass

    @abstractmethod
    def getTradingFees(self):
        pass

    @abstractmethod
    def getSymbolTickerPrice(self, symbol, futures=False):
        pass

    @abstractmethod
    def getSymbolKlines(self, symbol, interval, startTime=None, endTime=None, limit=None, futures=False, blvtnav=False,
                        convertDateTime=False, doClean=False, toCleanDataframe=False):
        pass

    @abstractmethod
    def getExchangeTime(self, futures=False):
        pass

    @abstractmethod
    def getSymbol24hTicker(self, symbol):
        pass

    @abstractmethod
    def testFuturesOrder(self, futuresOrderData):
        pass

    @abstractmethod
    def makeFuturesOrder(self, futuresOrderData):
        pass

    @abstractmethod
    def makeBatchFuturesOrder(self, futuresOrderDatas):
        pass

    @abstractmethod
    def changeInitialLeverage(self, symbol, leverage):
        pass

    @abstractmethod
    def changeMarginType(self, symbol, marginType, params):
        pass

    @abstractmethod
    def changePositionMargin(self, symbol, amount, marginType=None):
        pass

    @abstractmethod
    def getPosition(self):
        pass

    @abstractmethod
    def spotBestBidAsks(self, symbol=None):
        pass

    @abstractmethod
    def getSymbolOrderBook(self, symbol, limit=None, futures=False):
        pass

    @abstractmethod
    def getSymbolRecentTrades(self, symbol, limit=None, futures=False):
        pass

    @abstractmethod
    def getPositionInfo(self, symbol=None):
        pass

    @abstractmethod
    def getSymbolMinTrade(self, symbol, futures=False):
        pass
