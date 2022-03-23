'''
Created on 16 Mar 2022
Subclasses of API messages tuned to specific use cases
@author: shalomshachne
'''
from iserver.msgs.OrderRequest import OrderRequest
from iserver.enums.msgenums import MsgType

class CancelOrder(OrderRequest):
    def __init__(self, routerOrderID : int):
        super().__init__()
        self.msgType = MsgType.CANC.value
        self.routerOrderID=routerOrderID

        
