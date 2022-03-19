import logging
import warnings
from datetime import datetime

import pandas as pd
from pybit import HTTP

from BaseExchange import BaseExchange
from Utils import DataHelpers, BybitHelpers


class PyBitHTTP(HTTP):
    def __init__(self, endpoint=None, api_key=None, api_secret=None, logging_level=logging.INFO, log_requests=False,
                 request_timeout=10, recv_window=5000, force_retry=False, retry_codes=None, ignore_codes=None,
                 max_retries=3, retry_delay=3, referral_id=None, spot=False):
        super().__init__(endpoint, api_key, api_secret, logging_level, log_requests, request_timeout, recv_window,
                         force_retry, retry_codes, ignore_codes, max_retries, retry_delay, referral_id, spot)

    def query_history_order(self, **kwargs):
        if self.spot is True:
            suffix = '/spot/v1/history-orders'

            return self._submit_request(
                method='GET',
                path=self.endpoint + suffix,
                query=kwargs,
                auth=True
            )
        else:
            raise NotImplementedError('Not implemented for futures market.')


class BybitExchange(BaseExchange):
    timeIndexesInCandleData = [0, 6]
    desiredCandleDataIndexes = [0, 1, 2, 3, 4, 5, 6, 8]
    spotOrderTypes = ['LIMIT', 'MARKET', 'LIMIT_MAKER']
    spotTimeInForces = ['GTC', 'FOK', 'IOC']

    timeIntervals = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d', '1w', '1M']

    def __init__(self, credentials, sandbox=False, unifiedInOuts=True):
        self.apiKey = credentials['spot']['key']
        self.secret = credentials['spot']['secret']
        self.sandbox = sandbox
        self.unifiedInOuts = unifiedInOuts

        if sandbox:
            self.spotSession = PyBitHTTP("https://api-testnet.bybit.com", api_key=self.apiKey, api_secret=self.secret,
                                         spot=True)
            self.futuresSession = PyBitHTTP("https://api-testnet.bybit.com", api_key=self.apiKey,
                                            api_secret=self.secret)
        else:
            self.spotSession = PyBitHTTP("https://api.bybit.com", api_key=self.apiKey, api_secret=self.secret,
                                         spot=True)
            self.futuresSession = PyBitHTTP("https://api.bybit.com", api_key=self.apiKey, api_secret=self.secret)

        self.futuresSymbols = []
        for symbol in self.futuresSession.query_symbol()['result']:
            if symbol['name'].endswith('USDT'):
                self.futuresSymbols.append(symbol['name'])

    @staticmethod
    def isOrderDataValid(orderData: DataHelpers.OrderData):
        if orderData.symbol is None or orderData.quantity is None or orderData.side is None \
                or orderData.orderType is None:
            raise ValueError('Missing mandatory fields.')

        if orderData.orderType not in BybitExchange.spotOrderTypes:
            raise ValueError('Order type not correctly specified. Available order types for spot market: {}'.format(
                BybitExchange.spotOrderTypes))

        if orderData.side not in ['BUY', 'SELL']:
            raise ValueError('Order side can only be \'BUY\' or \'SELL\'')

        if orderData.timeInForce not in BybitExchange.spotTimeInForces:
            raise ValueError(
                'Time-in-force not correctly specified. Available time-in-force for spot market: {}'.format(
                    BybitExchange.spotTimeInForces))

        if orderData.orderType in ['LIMIT', 'LIMIT_MAKER'] and orderData.price is None:
            raise ValueError('Price must be specified for limit orders.')

    @staticmethod
    def isFuturesOrderDataValid(order: DataHelpers.futuresOrderData):
        pass

    @staticmethod
    def getSpotOrderAsDict(order: DataHelpers.OrderData):
        params = {
            'symbol': order.symbol,
            'qty': order.quantity,
            'side': order.side,
            'type': order.orderType,
            'timeInForce': order.timeInForce,
            'price': order.price,
            'orderLinkId': order.newClientOrderId
        }

        return params

    @staticmethod
    def getFuturesOrderAsDict(order: DataHelpers.futuresOrderData):
        pass

    @staticmethod
    def convertIntervalToFuturesKlines(interval):
        if interval == '1m':
            return 1
        elif interval == '3m':
            return 3
        elif interval == '5m':
            return 5
        elif interval == '15m':
            return 15
        elif interval == '30m':
            return 30
        elif interval == '1h':
            return 60
        elif interval == '2h':
            return 120
        elif interval == '4h':
            return 240
        elif interval == '6h':
            return 360
        elif interval == '12h':
            return 720
        elif interval == '1d':
            return 'D'
        elif interval == '1w':
            return 'W'
        elif interval == '1M':
            return 'M'

    @staticmethod
    def getIntervalInSeconds(interval):
        if interval not in BybitExchange.timeIntervals:
            raise ValueError('Incorrect time interval specified')
        if interval == '1m':
            return 60
        elif interval == '3m':
            return 3 * 60
        elif interval == '5m':
            return 5 * 60
        elif interval == '15m':
            return 15 * 60
        elif interval == '30m':
            return 30 * 60
        elif interval == '1h':
            return 60 * 60
        elif interval == '2h':
            return 120 * 60
        elif interval == '4h':
            return 240 * 60
        elif interval == '6h':
            return 360 * 60
        elif interval == '12h':
            return 720 * 60
        elif interval == '1d':
            return 86400
        elif interval == '1w':
            return 7 * 86400
        elif interval == '1M':
            return 30 * 86400

    def getBalance(self, asset='', futures=False):
        if futures:
            if asset in [None, '']:
                return BybitHelpers.getBalanceOut(self.futuresSession.get_wallet_balance()['result'], futures=True)
            else:
                return BybitHelpers.getBalanceOut(self.futuresSession.get_wallet_balance(coin=asset)['result'],
                                                  single=True, futures=True)
        else:
            if asset in [None, '']:
                return BybitHelpers.getBalanceOut(self.spotSession.get_wallet_balance()['result']['balances'])
            else:
                assets = self.spotSession.get_wallet_balance()['result']['balances']
                for coin in assets:
                    if asset == coin['coin']:
                        return BybitHelpers.getBalanceOut(coin, single=True)
                return None

    def symbolAccountTradeHistory(self, symbol, futures=False, fromId=None, limit=None):
        if futures:
            tradeHistory = self.futuresSession.user_trade_records(symbol=symbol, limit=limit, fromId=fromId)
            return BybitHelpers.getMyTradeHistoryOut(tradeHistory['result']['data'], futures=True)
        else:
            tradeHistory = self.spotSession.user_trade_records(symbol=symbol, limit=limit, fromId=fromId)
            return BybitHelpers.getMyTradeHistoryOut(tradeHistory['result'])

    def testSpotOrder(self, orderData: DataHelpers.OrderData):
        self.isOrderDataValid(orderData)

        if orderData.icebergQty is not None or orderData.newOrderRespType is not None \
                or orderData.quoteOrderQty is not None or orderData.recvWindow is not None \
                or orderData.stopPrice is not None:
            warnings.warn('Some of the given parameters have no use in ByBit exchange.')

        return orderData

    def makeSpotOrder(self, orderData):
        orderParams = self.getSpotOrderAsDict(orderData)

        return self.spotSession.place_active_order(**orderParams)['result']

    def getSymbolOrders(self, symbol, futures=False, orderId=None, startTime=None, endTime=None, limit=None):
        if futures:
            historyList = []
            pageNumber = 1
            endTimeString = None
            startTimeString = None
            done = False
            while not done:
                history = self.futuresSession.get_active_order(symbol=symbol, page=pageNumber, limit=50)

                if startTime is not None:
                    startTimeString = startTime.strftime('%Y-%m-%dT%H:%M:%SZ')
                if endTime is not None:
                    endTimeString = endTime.strftime('%Y-%m-%dT%H:%M:%SZ')

                for order in history['result']['data']:
                    if endTime is not None:
                        if endTimeString < order['create_time']:
                            continue

                    if startTime is not None:
                        if order['created_time'] < startTimeString:
                            done = True
                            break

                    historyList.append(order)

                if limit is not None and limit <= len(historyList):
                    done = True

                if len(history['result']['data']) < 50:
                    done = True

                pageNumber += 1

            return historyList
        else:
            history = self.spotSession.query_history_order(symbol=symbol, orderId=orderId, startTime=startTime,
                                                           endtime=endTime, limit=limit)
            return history['result']

    def getOpenOrders(self, symbol=None, futures=False):
        if futures:
            pass
        else:
            if symbol is None:
                openOrders = self.spotSession.query_active_order()['result']
            else:
                openOrders = self.spotSession.query_active_order(symbol=symbol)['result']
            return BybitHelpers.getOpenOrdersOut(openOrders)

    def cancelAllSymbolOpenOrders(self, symbol, futures=False):
        pass

    def cancelOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        pass

    def getOrder(self, symbol, orderId=None, localOrderId=None, futures=False):
        if futures:
            pass
        else:
            if orderId is not None:
                order = self.spotSession.get_active_order(orderId=orderId)['result']
            elif localOrderId is not None:
                order = self.spotSession.get_active_order(orderLinkId=localOrderId)['result']
            else:
                raise Exception('Specify either order Id in the exchange or local Id sent with the order')

            return order

    def getTradingFees(self):
        pass

    def getSymbolTickerPrice(self, symbol, futures=False):
        if futures:
            symbolInfo = self.futuresSession.latest_information_for_symbol(symbol=symbol)['result']
            return float(symbolInfo[0]['last_price'])
        else:
            symbolInfo = self.spotSession.latest_information_for_symbol(symbol=symbol)
            return float(symbolInfo['result']['lastPrice'])

    def getSymbolKlines(self, symbol, interval, startTime=None, endTime=None, limit=None, futures=False, blvtnav=False,
                        convertDateTime=False, doClean=False, toCleanDataframe=False):
        if not interval in self.timeIntervals:
            raise Exception('Time interval is not valid.')

        if futures:
            futuresInterval = self.convertIntervalToFuturesKlines(interval)
            data = []
            if limit is not None:
                if limit > 200:
                    limit = 200
                elif limit < 1:
                    limit = 1
            else:
                limit = 200

            if startTime is None:
                startTimestamp = int(datetime.now().timestamp() - self.getIntervalInSeconds(interval) * limit)
            else:
                startTimestamp = int(startTime.timestamp)

            candles = self.futuresSession.query_kline(symbol=symbol, interval=futuresInterval, from_time=startTimestamp,
                                                      limit=limit)

            for candle in candles['result']:
                dataArray = [float(candle['open_time']), float(candle['open']), float(candle['high']),
                             float(candle['low']), float(candle['close']), float(candle['volume']),
                             int(candle['open_time']) + self.getIntervalInSeconds(interval), None, None, None, None]
                data.append(dataArray)
        else:
            if startTime is not None:
                startTimestamp = startTime.timestamp() * 1000
            else:
                startTimestamp = None

            if endTime is not None:
                endTimestamp = endTime.timestamp() * 1000
            else:
                endTimestamp = None

            if limit is not None:
                if limit > 1000:
                    limit = 1000
                elif limit < 1:
                    limit = 1

            data = self.spotSession.query_kline(symbol=symbol, interval=interval, startTime=startTimestamp,
                                                endTime=endTimestamp, limit=limit)['result']

            for datum in data:
                for idx in range(len(datum)):
                    if idx in self.timeIndexesInCandleData:
                        continue
                    datum[idx] = float(datum[idx])

        if convertDateTime or toCleanDataframe:
            for datum in data:
                for idx in self.timeIndexesInCandleData:
                    if futures:
                        datum[idx] = datetime.fromtimestamp(float(datum[idx]))
                    else:
                        datum[idx] = datetime.fromtimestamp(float(datum[idx]) / 1000)

        if doClean or toCleanDataframe:
            outArray = []
            for datum in data:
                outArray.append([datum[index] for index in self.desiredCandleDataIndexes])

            if toCleanDataframe:
                df = pd.DataFrame(outArray,
                                  columns=['date', 'open', 'high', 'low', 'close', 'volume', 'closeDate', 'tradesNum'])
                df.set_index('date', inplace=True)
                return df
            return outArray
        else:
            return data

    def getExchangeTime(self, futures=False):
        if futures:
            return self.futuresSession.server_time()['time_now']
        else:
            return int(self.spotSession.server_time()['result']['serverTime'])

    def getSymbol24hTicker(self, symbol):
        pass

    def getAllSymbolFuturesOrders(self, symbol):
        pass

    def testFuturesOrder(self, futuresOrderData):
        pass

    def makeFuturesOrder(self, futuresOrderData):
        pass

    def makeBatchFuturesOrder(self, futuresOrderDatas):
        pass

    def cancellAllSymbolFuturesOrdersWithCountDown(self, symbol, countdownTime):
        pass

    def changeInitialLeverage(self, symbol, leverage):
        pass

    def changeMarginType(self, symbol, marginType):
        pass

    def changePositionMargin(self, symbol, amount, marginType):
        pass

    def getPosition(self):
        pass

    def spotBestBidAsks(self, symbol=None):
        pass

    def getSymbolOrderBook(self, symbol, limit=None, futures=False):
        pass

    def getSymbolRecentTrades(self, symbol, limit=None, futures=False):
        if futures:
            if limit is not None and limit > 0:
                limit = 1000 if limit > 1000 else limit
            else:
                limit = 500

            recentTrades = self.futuresSession.public_trading_records(symbol=symbol, limit=limit)['result']
            return BybitHelpers.getRecentTradeHistoryOut(recentTrades, futures=True)
        else:
            if limit is not None and limit > 0:
                limit = 60 if limit > 60 else limit
            else:
                limit = 60

            recentTrades = self.spotSession.public_trading_records(symbol=symbol, limit=limit)['result']
            return BybitHelpers.getRecentTradeHistoryOut(recentTrades)

    def setMarginType(self, symbol, marginType):
        pass

    def getPositionInfo(self, symbol=None):
        pass
