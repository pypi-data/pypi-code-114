from Exchanges.BaseExchange import BaseExchange

from kucoin.client import User, Trade, Market
from kucoin_futures.client import FuturesUser, FuturesTrade, FuturesMarket


class KuCoinExchange(BaseExchange):
    def __init__(self, credentials, sandbox=False, unifiedInOuts=True):
        self.apiKey = credentials['spot']['key']
        self.secret = credentials['spot']['secret']
        self.passphrase = credentials['spot']['passphrase']
        self.sandbox = sandbox
        self.unifiedInOuts = unifiedInOuts

        if sandbox:
            self.spotUser = User(key=self.apiKey, secret=self.secret, passphrase=self.passphrase, is_sandbox=True)
            self.spotTrade = Trade(key=self.apiKey, secret=self.secret, passphrase=self.passphrase, is_sandbox=True)
            self.spotMarket = Market(key=self.apiKey, secret=self.secret, passphrase=self.passphrase, is_sandbox=True)

            self.futuresUser = FuturesUser(key=self.apiKey, secret=self.secret, passphrase=self.passphrase,
                                           is_sandbox=True)
            self.futuresTrade = FuturesTrade(key=self.apiKey, secret=self.secret, passphrase=self.passphrase,
                                             is_sandbox=True)
            self.futuresMarket = FuturesMarket(key=self.apiKey, secret=self.secret, passphrase=self.passphrase,
                                               is_sandbox=True)
        else:
            self.spotUser = User(key=self.apiKey, secret=self.secret, passphrase=self.passphrase)
            self.spotTrade = Trade(key=self.apiKey, secret=self.secret, passphrase=self.passphrase)
            self.spotMarket = Market(key=self.apiKey, secret=self.secret, passphrase=self.passphrase)

            self.futuresUser = FuturesUser(key=self.apiKey, secret=self.secret, passphrase=self.passphrase)
            self.futuresTrade = FuturesTrade(key=self.apiKey, secret=self.secret, passphrase=self.passphrase)
            self.futuresMarket = FuturesMarket(key=self.apiKey, secret=self.secret, passphrase=self.passphrase)

    def getBalance(self, asset='', futures=False):
        if futures:
            pass

    def symbolAccountTradeHistory(self, symbol, futures=False, fromId=None, limit=None):
        pass

    def testSpotOrder(self, orderData):
        pass

    def makeSpotOrder(self, orderData):
        pass

    def getSymbolOrders(self, symbol, futures=False, orderId=None, startTime=None, endTime=None, limit=None):
        pass

    def getOpenOrders(self, symbol, futures=False):
        pass

    def cancelAllSymbolOpenOrders(self, symbol, futures=False):
        pass

    def cancelOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        pass

    def getOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        pass

    def getTradingFees(self):
        pass

    def getSymbolTickerPrice(self, symbol, futures=False):
        pass

    def getSymbolKlines(self, symbol, interval, startTime=None, endTime=None, limit=None, futures=False, blvtnav=False,
                        convertDateTime=False, doClean=False, toCleanDataframe=False):
        pass

    def getExchangeTime(self, futures=False):
        pass

    def getSymbol24hTicker(self, symbol):
        pass

    def testFuturesOrder(self, futuresOrderData):
        pass

    def makeFuturesOrder(self, futuresOrderData):
        pass

    def makeBatchFuturesOrder(self, futuresOrderDatas):
        pass

    def changeInitialLeverage(self, symbol, leverage):
        pass

    def changeMarginType(self, symbol, marginType, params):
        pass

    def changePositionMargin(self, symbol, amount, marginType=None):
        pass

    def getPosition(self):
        pass

    def spotBestBidAsks(self, symbol=None):
        pass

    def getSymbolOrderBook(self, symbol, limit=None, futures=False):
        pass

    def getSymbolRecentTrades(self, symbol, limit=None, futures=False):
        pass

    def getPositionInfo(self, symbol=None):
        pass

    def getSymbolMinTrade(self, symbol, futures=False):
        pass
