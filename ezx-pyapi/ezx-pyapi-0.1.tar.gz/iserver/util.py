'''
Created on 11 Mar 2022

@author: shalomshachne
'''
import time

from iserver.EzxMsg import EzxMsg
from iserver.enums.msgenums import State, Side


__counter = 0

closed_states = { 
    State.REJT.value,
    State.CAND.value,
    State.FILLED.value,
    State.EXPIRE.value,
    State.OVRF.value, 
    State.DONE.value
    }


def next_id() -> str:
    '''
    Get next unique ID. Uses a combination of millis time and a counter. Not thread safe.
    '''
    global __counter
    if __counter >= 999:
        __counter = 0
    __counter = __counter + 1
    millis = round(time.time() * 1000)
    return str(millis) + '-' + str(__counter)


def is_closed(order : EzxMsg):
    try:
        return order.state in closed_states
    except: 
        # if wrong kind of object gets here and returns false
        pass

def format_order(order: EzxMsg):
    # Buy IBM 100x165.23 (ROID=1234,ssOrderID=45667)
    side = Side(order.side).name    
    return f'{side} {order.symbol} {order.orderQty}x{order.price: .2f} (ROID={order.routerOrderID}) ({order.event}) (Filled={order.cumQty})'
      



