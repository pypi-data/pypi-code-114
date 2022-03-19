import time


def watchFuturesLimitTrigger(gate, symbol, orderId, doPutTpSl, cancelIfNotOpened, params):
    if doPutTpSl:
        if 'tpSlOrderSide' not in params.keys() or 'stopLoss' not in params.keys() or 'takeProfit' not in params.keys():
            raise ValueError('Must specify \'tpSlOrderSide\' and \'stopLoss\' and \'takeProfit\'')

    if cancelIfNotOpened:
        if 'timeFrame' not in params.keys() or 'delayNum' not in params.keys():
            raise ValueError('Must specify \'timeFrame\' and \'delayNum\'')

    print('Watching order')
    while True:
        time.sleep(0.1)
        order = gate.getOrder(symbol=symbol, orderId=orderId, futures=True)
        if order['status'] == 'NEW':
            continue
        elif order['status'] == 'FILLED':
            if doPutTpSl:
                orderSide = params['tpSlOrderSide']
                stopLoss = params['stopLoss']
                takeProfit = params['takeProfit']

                stopLossOrder = gate.createAndTestFuturesOrder(symbol, orderSide, 'STOP_MARKET',
                                                               stopPrice=stopLoss, closePosition=True,
                                                               priceProtect=True, workingType='MARK_PRICE',
                                                               timeInForce='GTC')

                takeProfitOrder = gate.createAndTestFuturesOrder(symbol, orderSide, 'TAKE_PROFIT_MARKET',
                                                                 closePosition=True, stopPrice=takeProfit,
                                                                 priceProtect=True, workingType='MARK_PRICE',
                                                                 timeInForce='GTC')
                result = gate.makeBatchFuturesOrder([stopLossOrder, takeProfitOrder])
                print(result)
                break
        elif order['status'] == 'CANCELED':
            break

    print('Watching position')
    while True:
        time.sleep(0.1)
        position = gate.getPositionInfo(symbol)[0]

        if float(position['entryPrice']) == 0.0:
            gate.cancelAllSymbolOpenOrders(symbol, futures=True)
            break
