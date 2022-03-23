'''
Created on Oct 20, 2021

@author: Sgoldberg
'''
from enum import Enum, auto
import logging
import socket

from iserver import ezx_msg
from iserver.EzxMsg import EzxMsg
from iserver.enums.msgenums import LogonType
from iserver.msgs import LogonRequest
from iserver.msgs import LogonResponse
import iserver
import threading
import time



def connect(host, port) -> socket.socket :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    logging.info(f'connected to {host}:{port}')
    return s


def _create_login(info):
    l = LogonRequest()
    l.companyName = info.company
    l.userName = info.user
    l.password = info.password
    l.logonType = info.logon_type
    # to-do handle setting seqno
    l.seqNo = 0
    return l
    
    
def empty_msg_handler(msg_subtype: int, msg: EzxMsg):
    logging.info(f"received msg={msg}")


class NotLoggedInException(Exception):
    def __init__(self, msg : str = 'Not logged into iServer'):
        super().__init__(msg)
    


class ClientState(Enum):
    INITIAL = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    LOGGED_IN = auto()
    LOGON_FAILURE = auto()
    DISCONNECTED = auto()
    STOPPED = auto()



DEFAULT_CONNECT_RETRY_SECONDS = 5
DEFAULT_HEARTBEAT_SECONDS = 15 

class ConnectionInfo(object):
    '''
    Specifies all settings related to connecting to the iServer.
    '''

    def __init__(self, host : str, port : int, company : str, user : str, password :str, 
                 logon_type : int = LogonType.ALL_FILLS_MSGS_AND_ALL_OPEN_ORDERS.value, 
                 connect_retry_seconds : float = DEFAULT_CONNECT_RETRY_SECONDS, heartbeat_seconds : int = DEFAULT_HEARTBEAT_SECONDS):
        '''
        Constructor
        '''        
        self.host = host
        self.port = port
        self.company = company
        self.user = user
        self.password = password
        self.logon_type = logon_type
        self.connect_retry_seconds = connect_retry_seconds
        heartbeat_seconds = min(DEFAULT_HEARTBEAT_SECONDS, heartbeat_seconds)
        self.heartbeat_seconds = heartbeat_seconds        
        
    def __str__(self):
        return iserver.to_bean_string(self)

class ApiClient(object):
    '''
    classdocs
    '''

    def __init__(self, connection_info : ConnectionInfo, msg_handler = empty_msg_handler, state_handler = lambda *args: None):
        '''
        Constructor
        '''
        # TODO: throw exception for None?
        self.connection_info = connection_info
        self._msg_handler = msg_handler
        self._state = ClientState.INITIAL
        self.on_state_change = state_handler
        
        self.connection_monitor = ClientMonitor(self)

        
    def start(self):        
        '''
        Start the connection with iServer
        '''
        
        if self.is_running():
            return
        
        logging.info("start(): starting client")
        
        self.connection_monitor.start()
        

    def _connect(self):
        logging.info("start(): connecting to iServer...")
        try:
            self._socket = connect(self.connection_info.host, self.connection_info.port)
            # if we get here, we're connected
            self._set_state(ClientState.CONNECTED)
            
            logging.info("start(): connected")
            self.__recv_thread = threading.Thread(target=self._recv)
            self.__recv_thread.start()
            
            self._sendLogin()
            
        except Exception as e:
            logging.error('start(): failed to connect! ex=%s', e)            
            #todo: save exception?
            
        
    def stop(self):
        '''
        Disconnect and shut down the ApiClient
        '''
        # set STOPPED state first to prevent reconnect logic
        self._set_state(ClientState.STOPPED)        
        try:
            if self._socket:
                self._socket.close()
                self._socket = None
                
                logging.info("stop(): socket closed.")
            
            if self.connection_monitor:
                self.connection_monitor.stop()
                
               
        except:
            pass
         
    def state(self) -> ClientState:
        return self._state
    
    def _set_state(self, state : ClientState):
        logging.debug("ApiClient.state=%s", state)        
        self._state = state
        self.on_state_change(state)
    
    def is_running(self):
        '''
        Indicates that client has been started and is running        
        '''
        return self.connection_monitor.is_running() # if the monitor is running, the client is alive
    
        
    def is_stopped(self):
        '''
        Returns True when Client was stopped programmatically to shut it down.
        '''
        return self._state == ClientState.STOPPED
    
    def is_connected(self):
        return self._state == ClientState.LOGGED_IN or self._state == ClientState.CONNECTED    
    
    def is_loggedin(self):
        return ClientState.LOGGED_IN == self.state()
    
    def _sendLogin(self):
        logging.info("sendLogin(): sending logon message now.")
        self.send_message(_create_login(self.connection_info))
        
    def _handle_message(self, msg_type, msg_subtype, body : bytearray):
        body = body.decode('UTF-8')
        logging.debug(f"_handle_message(): processing subtype={msg_subtype}, msg={body}")
        msg_object = ezx_msg.decode_message(msg_subtype, body)
                
        if msg_object:
            # handle the logon response first.
            if type(msg_object) is LogonResponse:  
                self.handle_logon_response(msg_object)
            # pass message to the user            
            self._msg_handler(msg_subtype, msg_object)
        else:                        
            logging.warn(f"_handle_message(): did not decode subtype={msg_subtype}")         
        
    def handle_logon_response(self, logon_response):
        if logon_response.returnCode == 0:
            self._set_state(ClientState.LOGGED_IN)
        else:
            logging.fatal(f"handle_logon(): logon failed! returnCode={logon_response.returnCode}, failure message={logon_response.returnDesc} ")            
            logging.fatal('handle_logon(): stopping client. Please contact EZX support!')
            self.logon_failure = (logon_response.returnCode, logon_response.returnDesc)
            self._set_state(ClientState.LOGON_FAILURE)
   
            self.stop()
        
    def _recv(self):
        if not self._socket:
            logging.error("_recv(): no socket to receive, exiting")
            return 
        
        # s = self._socket
        with self._socket as s:
            while s:
                try:
                    logging.debug('_recv(): waiting for message...')
                    header = s.recv(15)
                    if not header:
                        break
                    length, msg_type, msg_subtype = ezx_msg.parse_header(header)
                    
                    logging.debug('_recv(): got header. reading body of length=%d', length)                    
                    body = s.recv(length)
                    if not body:
                        break
                    
                    logging.debug('_recv(): processing msg type=%d. bytes received=%s', msg_type, body)                            
                    self._handle_message(msg_type, msg_subtype, body)
                    
                except ConnectionAbortedError:
                    #TODO: figure out whether this was user disconnect or from another source.
                    logging.info("_recv(): socket was disconnected")
                    break
                    
                except Exception as e:
                    logging.error(f"_recv(): error receiving message! ex={e}")
                    break;

        logging.debug("_recv(): no longer receiving messages.")

        self._socket = None

        if not self.is_stopped():
            self._set_state(ClientState.DISCONNECTED)
         
    def send_message(self, api_msg_object: EzxMsg):
        if not self.is_loggedin() and not type(api_msg_object) == LogonRequest: # LogonRequest is sent before being in the logged in state
            raise NotLoggedInException()
        
        try:
            msg = ezx_msg.to_api_bytes(api_msg_object)
            self._socket.sendall(msg)
            logging.debug("send_message(): sent msg=%s", msg)
            
        except Exception as e:
            logging.error('send_message(): error on send - probably a disconnect! ex=%s', e)
    
    
         
    
    def get_logon_failure(self) -> (int, str):
        '''
        Retrieve logon failure code and description if iServer indicates that the Logon failed
        @return: tuple of errcode (int) and message 
        '''
        try:
            return self.logon_failure
        
        except AttributeError: # this might not be set
            pass
            
       
        
class ClientMonitor(object):
    
    
    def __init__(self, client, wait_seconds = DEFAULT_CONNECT_RETRY_SECONDS, heartbeat_seconds = DEFAULT_HEARTBEAT_SECONDS):
        self.client = client
        self.monitor_thread = None


    def retry_seconds(self) -> float: 
        return self.client.connection_info.connect_retry_seconds
    
    def start(self):
        if self.monitor_thread:
            logging.warn('started called when ClientMonitor is already running.')
            return 

        logging.info("ClientMonitor.start(): starting monitor thread")
        self.run = True        
        self.monitor_thread = threading.Thread(target=self.monitor)
        self.monitor_thread.daemon = True                        
        self.monitor_thread.start()
    
        
    def stop(self):
        logging.info("ClientMonitor.stop(): shutting down monitor")
        self.run = False
                        
        
    def monitor(self):
        logging.info("ClientMonitor.monitor(): starting connection monitor")        
        # 1. if not connected, connect
        # 2. if logged in, send heartbeat
        while self.run:
            if self.connect_required():
                self.client._connect()
                time.sleep(self.retry_seconds())            
            
            
            #elif Logged in, send heartbeat.
        
        logging.info('ClientMonitor.monitor(): exiting')
    
    def connect_required(self):
        return self.client.state() == ClientState.INITIAL or self.client.state() == ClientState.DISCONNECTED
    
    def is_running(self):
        if self.monitor_thread:
            return self.monitor_thread.is_alive()
        