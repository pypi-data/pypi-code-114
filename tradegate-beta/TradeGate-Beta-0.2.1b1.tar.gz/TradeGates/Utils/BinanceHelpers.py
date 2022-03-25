import json
from datetime import datetime

import pandas as pd

from Exchanges.BinanceExchange import BinanceExchange
from Utils import DataHelpers


def isOrderDataValid(order: DataHelpers.OrderData):
    if order.orderType not in BinanceExchange.spotOrderTypes:
        return False

    if order.side not in ['BUY', 'SELL']:
        return False

    if order.newOrderRespType not in [None, 'ACK', 'RESULT', 'FULL']:
        return False

    if order.timeInForce not in [None, 'GTC', 'IOC', 'FOK']:
        return False

    if order.orderType == 'LIMIT':
        if not (order.timeInForce is None or order.quantity is None or order.price is None):
            return True

    elif order.orderType == 'MARKET':
        if not (order.quantity is None and order.quoteOrderQty is None):
            return True

    elif order.orderType in ['STOP_LOSS', 'TAKE_PROFIT']:
        if not (order.quantity is None or order.stopPrice is None):
            return True

    elif order.orderType in ['STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT']:
        if not (
                order.timeInForce is None or order.quantity is None or order.price is None or order.stopPrice is None):
            return True

    elif order.orderType == 'LIMIT_MAKER':
        if not (order.quantity is None or order.price is None):
            return True

    return False


def isFuturesOrderDataValid(order: DataHelpers.futuresOrderData):
    if order.side not in ['BUY', 'SELL']:
        return False

    if order.orderType not in BinanceExchange.futuresOrderTypes:
        return False

    if order.positionSide not in [None, 'BOTH', 'LONG', 'SHORT']:
        return False

    if order.timeInForce not in [None, 'GTC', 'IOC', 'FOK', 'GTX']:
        return False

    if order.workingType not in [None, 'MARK_PRICE', 'CONTRACT_PRICE']:
        return False

    if order.newOrderRespType not in [None, 'ACK', 'RESULT']:
        return False

    if order.closePosition not in [None, True, False]:
        return False

    if order.callbackRate is not None and not (0.1 <= order.callbackRate <= 5):
        return False

    if order.priceProtect not in [None, True, False]:
        return False

    if order.closePosition is True and order.quantity is not None:
        return False

    if order.reduceOnly not in [None, True, False]:
        return False

    if order.closePosition is True and order.reduceOnly is True:
        return False

    if order.orderType == 'LIMIT':
        if not (order.timeInForce is None or order.quantity is None or order.price is None):
            return True

    elif order.orderType == 'MARKET':
        if order.quantity is not None:
            return True

    elif order.orderType in ['STOP', 'TAKE_PROFIT']:
        if not (order.quantity is None or order.price is None or order.stopPrice is None):
            return True

    elif order.orderType in ['STOP_MARKET', 'TAKE_PROFIT_MARKET']:
        if order.stopPrice is not None:
            return True

    elif order.orderType == 'TRAILING_STOP_MARKET':
        if order.callbackRate is not None:
            return True


def getSpotOrderAsDict(order: DataHelpers.OrderData):
    if order.timestamp is None:
        raise ValueError('Timestamp must be set')

    params = {'symbol': order.symbol, 'side': order.side, 'type': order.orderType, 'timestamp': order.timestamp}

    if order.timeInForce is not None:
        params['timeInForce'] = order.timeInForce

    if order.quantity is not None:
        params['quantity'] = order.quantity

    if order.quoteOrderQty is not None:
        params['quoteOrderQty'] = order.quoteOrderQty

    if order.price is not None:
        params['price'] = order.price

    if order.newOrderRespType is not None:
        params['newOrderRespType'] = order.newOrderRespType

    if order.stopPrice is not None:
        params['stopPrice'] = order.stopPrice

    if order.icebergQty is not None:
        params['icebergQty'] = order.icebergQty

    if order.newClientOrderId is not None:
        params['newClientOrderId'] = order.newClientOrderId

    if order.recvWindow is not None:
        params['recvWindow'] = order.recvWindow

    return params


def getFuturesOrderAsDict(order: DataHelpers.futuresOrderData, allStr=False):
    params = {'symbol': order.symbol, 'side': order.side, 'ordertype': order.orderType}

    if order.positionSide is not None:
        params['positionSide'] = order.positionSide

    if order.timeInForce is not None:
        params['timeInForce'] = order.timeInForce

    if order.quantity is not None:
        params['quantity'] = order.quantity

    if order.reduceOnly is not None:
        params['reduceOnly'] = order.reduceOnly

    if order.price is not None:
        params['price'] = order.price

    if order.newClientOrderId is not None:
        params['newClientOrderId'] = order.newClientOrderId

    if order.stopPrice is not None:
        params['stopPrice'] = order.stopPrice

    if order.closePosition is not None:
        params['closePosition'] = order.closePosition

    if order.activationPrice is not None:
        params['activationPrice'] = order.activationPrice

    if order.callbackRate is not None:
        params['callbackRate'] = order.callbackRate

    if order.workingType is not None:
        params['workingType'] = order.workingType

    if order.priceProtect is not None:
        params['priceProtect'] = order.priceProtect

    if order.newOrderRespType is not None:
        params['newOrderRespType'] = order.newOrderRespType

    if order.recvWindow is not None:
        params['recvWindow'] = order.recvWindow

    if allStr:
        for key, value in params.items():
            params[key] = str(value)

    return params


def getKlinesDesiredOnlyCols(data):
    finalDataArray = []
    for datum in data:
        finalDataArray.append([datum[index] for index in BinanceExchange.desiredCandleDataIndexes])
    return finalDataArray


def klinesConvertToPandas(outArray):
    df = pd.DataFrame(outArray,
                      columns=['date', 'open', 'high', 'low', 'close', 'volume', 'closeDate', 'tradesNum'])
    df.set_index('date', inplace=True)
    return df


def klinesConvertDate(data):
    for datum in data:
        for idx in BinanceExchange.timeIndexesInCandleData:
            datum[idx] = datetime.fromtimestamp(float(datum[idx]) / 1000)


def extractSymbolInfoFromFilters(symbolFilters, tickerPrice):
    params = {}
    for symbolFilter in symbolFilters:
        if symbolFilter['filterType'] == 'LOT_SIZE':
            params['minQuantity'] = float(symbolFilter['minQty'])
            params['stepQuantity'] = float(symbolFilter['stepSize'])
            params['minQuoteQuantity'] = tickerPrice * params['minQuantity']

        if symbolFilter['filterType'] == 'PRICE_FILTER':
            params['stepPrice'] = symbolFilter['tickSize']
    return params


def makeBatchOrderData(self, futuresOrderDatas):
    batchOrders = []
    for order in futuresOrderDatas:
        orderAsDict = getFuturesOrderAsDict(order, allStr=True)
        orderAsDict['type'] = orderAsDict.pop('ordertype')

        orderJSON = json.dumps(orderAsDict)

        batchOrders.append(orderJSON)
    return batchOrders
