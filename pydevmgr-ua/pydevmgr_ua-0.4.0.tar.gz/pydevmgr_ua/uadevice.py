from pydevmgr_core import BaseDevice, record_class
from .uacom import UaCom, parse_com
from .config import uaconfig
from .uainterface import UaInterface
from .uanode import UaNode
from .uarpc import UaRpc
from typing import  Optional
from pydantic import AnyUrl, Field

@record_class
class UaDevice(BaseDevice):
    Node = UaNode
    Rpc = UaRpc
    Interface = UaInterface
    
    class Config(BaseDevice.Config):
        Node = UaNode.Config
        Interface = UaInterface.Config
        Rpc = UaRpc.Config

        type: str = "Ua"
        # AnyUrl  will valid the address to an url 
        # the url is first replaced on-the-fly if defined in host_mapping 
        address     : AnyUrl         = Field(default_factory=lambda : uaconfig.default_address) 
        prefix      : str            = ""
        namespace   : int            = Field(default_factory=lambda : uaconfig.namespace)
        
    @classmethod
    def new_com(cls, config: Config, com: Optional[UaCom] = None) -> UaCom:         
        if com is None:       
            return UaCom(address=config.address, namespace=config.namespace).subcom(config.prefix)
        if isinstance(com, dict):
            com = UaCom(**com)
        elif isinstance(com, UaCom.Config):
            com = UaCom(config=com)
        ## Warning config is changed to the com address and namespace 
        config.address = com.address 
        config.namespace = com.namespace           
        return com.subcom(config.prefix)
            
    def connect(self):
        """ Connect to the OPC-UA client """
        self._com.connect()
        
    def disconnect(self):
        """ Connect from the  OPC-UA client """
        self._com.disconnect()
    
    def is_connected(self):
        return self._com.is_connected()
    
    @property
    def uaprefix(self):
        return self._com.prefix
