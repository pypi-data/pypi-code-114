def getBalanceOut(data, single=False, futures=False):
    if not single:
        outData = []
        if not futures:
            for asset in data:
                coinData = {'asset': asset['coin'], 'free': asset['free'], 'locked': asset['locked'],
                            'exchangeSpecific': asset}
                outData.append(coinData)
            return outData
        else:
            for key, value in data.items():
                coinData = {'asset': key, 'free': value['available_balance'], 'locked': value['used_margin'],
                            'exchangeSpecific': value}
                outData.append(coinData)
            return outData
    else:
        if not futures:
            outData = {'asset': data['coin'], 'free': data['free'], 'locked': data['locked'], 'exchangeSpecific': data}
            return outData
        else:
            outData = {}
            key = list(data.keys())[0]

            outData['asset'] = key
            outData['free'] = data[key]['available_balance']
            outData['locked'] = data[key]['used_margin']
            outData['exchangeSpecific'] = data[key]
            return outData


def getMyTradeHistoryOut(data, futures=False):
    outData = []
    if futures:
        for history in data:
            outData.append(
                {'symbol': history['symbol'], 'id': history['exec_id'], 'orderId': history['order_id'],
                 'orderListId': history['order_link_id'], 'price': history['price'],
                 'qty': history['order_qty'],
                 'quoteQty': str(float(history['price']) * float(history['order_qty'])),
                 'commission': None, 'commissionAsset': None, 'time': history['trade_time_ms'],
                 'isBuyer': None, 'isMaker': None, 'isBestMatch': None, 'exchangeSpecific': history}
            )
    else:
        for history in data:
            outData.append(
                {'symbol': history['symbol'], 'id': history['id'], 'orderId': history['orderId'],
                 'orderListId': -1, 'price': history['price'], 'qty': history['qty'],
                 'quoteQty': str(float(history['price']) * float(history['qty'])),
                 'commission': history['commission'], 'commissionAsset': history['commissionAsset'],
                 'time': history['time'], 'isBuyer': history['isBuyer'], 'isMaker': history['isMaker'],
                 'isBestMatch': None, 'exchangeSpecific': history}
            )
    return outData


def getRecentTradeHistoryOut(data, futures=False):
    outData = []
    if futures:
        for datum in data:
            outData.append({
                'id': datum['id'], 'price': datum['price'], 'qty': datum['qty'],
                'quoteQty': str(float(datum['qty'] * datum['price'])),
                'time': datum['trade_time_ms'], 'isBuyerMaker': None, 'isBestMatch': None, 'exchangeSpecific': datum
            })
    else:
        for datum in data:
            outData.append({
                'id': None, 'price': datum['price'], 'qty': datum['qty'],
                'quoteQty': str(float(datum['qty']) * float(datum['price'])),
                'time': datum['time'], 'isBuyerMaker': datum['isBuyerMaker'], 'isBestMatch': None,
                'exchangeSpecific': datum
            })
    return outData


def getOpenOrdersOut(data, futures=False):
    outData = []
    if futures:
        pass
    else:
        for datum in data:
            outData.append({
                'symbol': datum['symbol'],
                'orderId': datum['orderId'],
                'orderListId': None,
                'clientOrderId': datum['orderLinkId'],
                'price': datum['price'],
                'origQty': datum['origQty'],
                'executedQty': datum['executedQty'],
                'cummulativeQuoteQty': datum['cummulativeQuoteQty'],
                'status': datum['status'],
                'timeInForce': datum['timeInForce'],
                'type': datum['type'],
                'side': datum['side'],
                'stopPrice': datum['stopPrice'],
                'icebergQty': datum['icebergQty'],
                'time': datum['time'],
                'updateTime': datum['updateTime'],
                'isWorking': datum['isWorking'],
                'origQuoteOrderQty': None,
                'exchangeSpecific': datum
            })
    return outData
