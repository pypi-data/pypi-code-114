import multiprocessing

from Exchanges import BinanceExchange, BybitExchange
from Utils import DataHelpers
from Watchers.futureOrderWatchers import watchFuturesLimitTrigger
from binance_f.exception.binanceapiexception import BinanceApiException


class TradeGate:
    def __init__(self, configDict, sandbox=False):
        self.exchangeName = configDict['exchangeName']
        exchangeClass = self.getCorrectExchange(self.exchangeName)
        if sandbox:
            self.apiKey = configDict['credentials']['test']['spot']['key']
            self.apiSecret = configDict['credentials']['test']['spot']['secret']

            self.exchange = exchangeClass(configDict['credentials']['test'], sandbox=True)
        else:
            self.apiKey = configDict['credentials']['main']['spot']['key']
            self.apiSecret = configDict['credentials']['main']['spot']['secret']

            self.exchange = exchangeClass(configDict['credentials']['main'], sandbox=False)

    def getBalance(self, asset='', futures=False):
        return self.exchange.getBalance(asset, futures)

    @staticmethod
    def getCorrectExchange(exchangeName):
        if exchangeName.lower() == 'binance':
            return BinanceExchange.BinanceExchange
        if exchangeName.lower() == 'bybit':
            return BybitExchange.BybitExchange

    @staticmethod
    def setSpotOrderData(icebergQty, newClientOrderId, newOrderRespType, orderType, price, quantity, recvWindow, side,
                         stopPrice, symbol, timeInForce):
        currOrder = DataHelpers.OrderData(symbol.upper(), side.upper(), orderType.upper())
        if quantity is not None:
            currOrder.setQuantity(quantity)
        if price is not None:
            currOrder.setPrice(price)
        if timeInForce is not None:
            currOrder.setTimeInForce(timeInForce)
        if stopPrice is not None:
            currOrder.setStopPrice(stopPrice)
        if icebergQty is not None:
            currOrder.setIcebergQty(icebergQty)
        if newOrderRespType is not None:
            currOrder.setNewOrderRespType(newOrderRespType)
        if recvWindow is not None:
            currOrder.setRecvWindow(recvWindow)
        if newClientOrderId is not None:
            currOrder.setNewClientOrderId(newClientOrderId)
        return currOrder

    @staticmethod
    def setFuturesOrderData(activationPrice, callbackRate, closePosition, extraParams, newClientOrderId,
                            newOrderRespType, orderType, positionSide, price, priceProtect, quantity, recvWindow,
                            reduceOnly, side, stopPrice, symbol, timeInForce, workingType):
        if extraParams is None:
            extraParams = {}
        currOrder = DataHelpers.futuresOrderData(symbol.upper(), side.upper(), orderType.upper())
        if positionSide is not None:
            currOrder.setPositionSide(positionSide)
        if timeInForce is not None:
            currOrder.setTimeInForce(timeInForce)
        if quantity is not None:
            currOrder.setQuantity(quantity)
        if reduceOnly is not None:
            currOrder.setReduceOnly(reduceOnly)
        if price is not None:
            currOrder.setPrice(price)
        if newClientOrderId is not None:
            currOrder.setNewClientOrderId(newClientOrderId)
        if stopPrice is not None:
            currOrder.setStopPrice(stopPrice)
        if closePosition is not None:
            currOrder.setClosePosition(closePosition)
        if activationPrice is not None:
            currOrder.setActivationPrice(activationPrice)
        if callbackRate is not None:
            currOrder.setCallbackRate(callbackRate)
        if workingType is not None:
            currOrder.setWorkingType(workingType)
        if priceProtect is not None:
            currOrder.setPriceProtect(priceProtect)
        if newOrderRespType is not None:
            currOrder.setNewOrderRespType(newOrderRespType)
        if recvWindow is not None:
            currOrder.setRecvWindow(recvWindow)
        if extraParams is not None:
            currOrder.setExtraParams(extraParams)
        return currOrder

    def createAndTestSpotOrder(self, symbol, side, orderType, quantity=None, price=None, timeInForce=None,
                               stopPrice=None, icebergQty=None, newOrderRespType=None, recvWindow=None,
                               newClientOrderId=None):

        currOrder = self.setSpotOrderData(icebergQty, newClientOrderId, newOrderRespType, orderType, price, quantity,
                                          recvWindow, side, stopPrice, symbol, timeInForce)

        self.exchange.testSpotOrder(currOrder)

        return currOrder

    def makeSpotOrder(self, orderData):
        return self.exchange.makeSpotOrder(orderData)

    def getSymbolOrders(self, symbol, futures=False, orderId=None, startTime=None, endTime=None, limit=None):
        return self.exchange.getSymbolOrders(symbol=symbol, futures=futures, orderId=orderId, startTime=startTime,
                                             endTime=endTime, limit=limit)

    def getOpenOrders(self, symbol, futures=False):
        return self.exchange.getOpenOrders(symbol, futures)

    def getOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        return self.exchange.getOrder(symbol, orderId, localOrderId, futures=futures)

    def cancelAllSymbolOpenOrders(self, symbol, futures=False):
        return self.exchange.cancelAllSymbolOpenOrders(symbol, futures)

    def cancelOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        return self.exchange.cancelOrder(symbol, orderId, localOrderId, futures)

    def getTradingFees(self):
        return self.exchange.getTradingFees()

    def getSymbolTickerPrice(self, symbol, futures=False):
        return self.exchange.getSymbolTickerPrice(symbol, futures)

    def getSymbolKlines(self, symbol, interval, startTime=None, endTime=None, limit=None, futures=False, blvtnav=False,
                        convertDateTime=False, doClean=False, toCleanDataframe=False):
        return self.exchange.getSymbolKlines(symbol, interval, startTime, endTime, limit, futures, blvtnav,
                                             convertDateTime, doClean, toCleanDataframe)

    def getExchangeTime(self, futures=False):
        return self.exchange.getExchangeTime(futures)

    def createAndTestFuturesOrder(self, symbol, side, orderType, positionSide=None, timeInForce=None, quantity=None,
                                  reduceOnly=None, price=None, newClientOrderId=None,
                                  stopPrice=None, closePosition=None, activationPrice=None, callbackRate=None,
                                  workingType=None, priceProtect=None, newOrderRespType=None,
                                  recvWindow=None, extraParams=None):
        currOrder = self.setFuturesOrderData(activationPrice, callbackRate, closePosition, extraParams,
                                             newClientOrderId, newOrderRespType, orderType, positionSide, price,
                                             priceProtect, quantity, recvWindow, reduceOnly, side, stopPrice, symbol,
                                             timeInForce, workingType)

        self.exchange.testFuturesOrder(currOrder)

        return currOrder

    def makeFuturesOrder(self, futuresOrderData):
        return self.exchange.makeFuturesOrder(futuresOrderData)

    def makeBatchFuturesOrder(self, batchOrders):
        return self.exchange.makeBatchFuturesOrder(batchOrders)

    def cancelAllSymbolFuturesOrdersWithCountDown(self, symbol, countdownTime):
        return self.exchange.cancellAllSymbolFuturesOrdersWithCountDown(symbol, countdownTime)

    def changeInitialLeverage(self, symbol, leverage):
        return self.exchange.changeInitialLeverage(symbol, leverage)

    def changeMarginType(self, symbol, marginType, params=None):
        return self.exchange.changeMarginType(symbol, marginType, params)

    def changePositionMargin(self, symbol, amount, marginType):
        return self.exchange.changePositionMargin(symbol, amount, marginType)

    def getPosition(self):
        return self.exchange.getPosition()

    def spotBestBidAsks(self, symbol=None):
        return self.exchange.spotBestBidAsks(symbol)

    def getSymbolOrderBook(self, symbol, limit=None, futures=False):
        return self.exchange.getSymbolOrderBook(symbol, limit, futures)

    def getSymbolRecentTrades(self, symbol, limit=None, futures=False):
        return self.exchange.getSymbolRecentTrades(symbol, limit, futures)

    def symbolAccountTradeHistory(self, symbol, futures=False, fromId=None, limit=None):
        return self.exchange.symbolAccountTradeHistory(symbol=symbol, futures=futures, fromId=fromId, limit=limit)

    def makeSlTpLimitFuturesOrder(self, symbol, orderSide, quantity=None, quoteQuantity=None, enterPrice=None,
                                  takeProfit=None, stopLoss=None, leverage=None, marginType=None, cancelDelaySec=None):

        symbolInfo = self.getSymbolMinTrade(symbol=symbol, futures=True)
        stepQuantity = len(str(symbolInfo['precisionStep'])) - 2

        quantity = self._getQuantity(enterPrice, quantity, quoteQuantity, stepQuantity)
        self._setLeverage(leverage, symbol)
        self._setMarginType(marginType, symbol)
        cancelIfNotOpened, doPutTpSl, params = self._setTpSlParams(cancelDelaySec, orderSide, stopLoss, takeProfit)

        order = self.testAndMakeFuturesOrder(enterPrice, orderSide, quantity, symbol)

        print('Main order sent')

        watcherProc = multiprocessing.Process(target=watchFuturesLimitTrigger,
                                              args=(self, symbol, order['orderId'], doPutTpSl, cancelIfNotOpened,
                                                    params))
        watcherProc.start()
        # watchFuturesLimitTrigger(self, symbol, order['orderId'], True, False, params)
        return order

    @staticmethod
    def _getQuantity(enterPrice, quantity, quoteQuantity, stepQuantity):
        if (quantity is not None and quoteQuantity is not None) or (quantity is None and quoteQuantity is None):
            raise ValueError('Specify either quantity or quoteQuantity and not both')
        if quantity is None:
            quantity = round(quoteQuantity / enterPrice, stepQuantity)
        return quantity

    def testAndMakeFuturesOrder(self, enterPrice, orderSide, quantity, symbol):
        mainOrder = self.createAndTestFuturesOrder(symbol, orderSide.upper(), 'LIMIT', quantity=str(quantity),
                                                   price=str(enterPrice), timeInForce='GTC')
        order = self.makeFuturesOrder(mainOrder)
        return order

    @staticmethod
    def _setTpSlParams(cancelDelaySec, orderSide, stopLoss, takeProfit):
        cancelIfNotOpened = True if cancelDelaySec is not None else False
        doPutTpSl = True if takeProfit is not None or stopLoss is not None else False
        tpSlOrderSide = 'BUY' if orderSide.upper() == 'SELL' else 'SELL'
        params = {'tpSlOrderSide': tpSlOrderSide, 'takeProfit': takeProfit, 'stopLoss': stopLoss,
                  'cancelDelaySec': cancelDelaySec}
        return cancelIfNotOpened, doPutTpSl, params

    def _setMarginType(self, marginType, symbol):
        try:
            self.exchange.changeMarginType(symbol, marginType)
        except BinanceApiException:
            pass

    def _setLeverage(self, leverage, symbol):
        setLeverageResult = self.changeInitialLeverage(symbol, leverage)
        if not (setLeverageResult['leverage'] == leverage):
            raise ConnectionError('Could not change leverage.')

    def getPositionInfo(self, symbol=None):
        return self.exchange.getPositionInfo(symbol)

    def getSymbolMinTrade(self, symbol, futures=False):
        return self.exchange.getSymbolMinTrade(symbol, futures)
