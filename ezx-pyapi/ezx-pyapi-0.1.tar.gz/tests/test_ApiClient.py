'''
Created on 10 Mar 2022

@author: shalomshachne
'''

import socket
from socketserver import BaseRequestHandler, TCPServer

from threading import Condition
import threading
import unittest

from iserver import ezx_msg
from iserver.net import ConnectionInfo, ApiClient, ClientState,\
    NotLoggedInException
from tests import check_logging, wait_for_condition
import logging
from tests.data import test_data_factory
from iserver.msgs.LogonResponse import LogonResponse
from iserver.enums.msgenums import ReturnCode
from iserver.util import next_id
from iserver.enums.api import IserverMsgSubType
from time import sleep
from unittest.mock import Mock
from iserver.msgs.LogonRequest import LogonRequest

logger=logging.getLogger(__name__)

class TestApiClient(unittest.TestCase):


    DEFAULT_PORT = 15002
    
        
    @classmethod
    def setUpClass(cls):
        # super(TestApiClient, cls).setUpClass()
        # sh = logging.StreamHandler(sys.stdout)
        # logging.root.addHandler(sh)
        check_logging()


    def start_server(self):
        self.server = MockIserver(TestApiClient.DEFAULT_PORT, self.handle)
        self.server.start()

    def setUp(self):
        self.connectInfo = ConnectionInfo(host='localhost', port=TestApiClient.DEFAULT_PORT, company='EZX', user='gnadan', password='gnadan', connect_retry_seconds=.1)        
        self.client = ApiClient(self.connectInfo)
        self.start_server()
        
        self.clientTest = lambda *args : None
        self.last_message = None  # message received by server from the ApiClient
        self.wait_condition = Condition()
        
        self.connect_wait_secs = 3
        
        
    def tearDown(self):
        self.client.stop()
        self.server.stop()        
        
    
    def on_state_change(self, state):
        self.last_state_change = state
        
        
    def handle(self, header, body):
        logger.info(f'got a message. header={header}, body={body}')
        self.wait_condition.acquire()
        self.last_message = (header, body)
        self.wait_condition.notify_all()
        self.wait_condition.release()

    def testNotifiesStateChange(self):
        received = 'untouched'
        
        def printState(state): 
            nonlocal received        
            received = state
            logger.debug('got state change=%s', received)
        
        handler = printState
                   
        self.client.on_state_change = handler
         
        self.client._set_state(ClientState.CONNECTED)
        
        self.assertEqual(ClientState.CONNECTED, received, "called back on state change")
        
    
    def test_state_functions(self):
        self.assertFalse(self.client.is_connected(), 'valid initial state')
        
        self.client._set_state(ClientState.CONNECTED)
        self.assertTrue(self.client.is_connected())
        
        self.client._set_state(ClientState.LOGGED_IN)
        self.assertTrue(self.client.is_connected())
        
    

    def assert_logon_received(self):
        message = self.last_message
        self.assertIsNotNone(message, 'got a message')
        header, _ = message
        sub_type = int(header[8:11].decode('UTF-8'))
        self.assertEqual(IserverMsgSubType.LOGON.value, sub_type, 'received logonRequest')

    def test_start_sends_logon(self):
        self.wait_condition.acquire()
        self.client.start()
        self.wait_condition.wait(self.connect_wait_secs)  # 3 seconds max wait.

        self.assert_logon_received()
 
        
    def test_notifies_logon_response(self):
        self.client.on_state_change = self.on_state_change
        
                
        response = LogonResponse(returnCode=ReturnCode.OK.value)
        api_bytes = ezx_msg.to_api_bytes(response, test_data_factory.random_quantity())
        self.client._handle_message(response.msg_type, response.msg_subtype, api_bytes[15:])
        
        self.assertEqual(ClientState.LOGGED_IN, self.client.state(), 'handled logonresponse correctly = ok')
        self.assertEqual(ClientState.LOGGED_IN, self.last_state_change, 'got notified on logon')
        
        
    def test_logon_failure_shuts_down_client(self):
        counter = 0
        def check_logon_failure_notification(state):
            nonlocal counter
            counter = counter + 1
            if counter == 1:
                self.assertEqual(ClientState.LOGON_FAILURE, state, 'notified of logon failure')
                self.got_state_change = True

        self.client.on_state_change = check_logon_failure_notification
        failure = 'wrong user name!'
        response = LogonResponse(returnCode=ReturnCode.INVALID_USER.value, returnDesc=failure)
        api_bytes = ezx_msg.to_api_bytes(response, test_data_factory.random_quantity())

        self.client._handle_message(response.msg_type, response.msg_subtype, api_bytes[15:])
        
        self.assertEqual(ClientState.STOPPED, self.client.state(), 'handled logonresponse correctly = failure')
        self.assertTrue(self.client.is_stopped(), 'shut down on logon failure')
        self.assertTrue(self.got_state_change)
        
        errcode, desc = self.client.get_logon_failure()
        self.assertEqual(ReturnCode.INVALID_USER.value, errcode)
        self.assertEqual(failure, desc)
                        
    def test_client_retries_connection(self):
        self.test_start_sends_logon()
        logger.info('stopping server to cause ApiClient disconnect')
        self.server.stop()
        self.last_message = None
        self.connect_wait_secs = 10 # not sure how long to wait.
        self.wait_condition.acquire()
        logger.info('restarting server...')        
        self.start_server()
        logger.info('waiting for login...')        
        self.wait_condition.wait(self.connect_wait_secs) 
        
        # should reconnect shortly
        # message = self.last_message
        # self.assertIsNotNone(message, 'reconnected and logged in')
        self.assert_logon_received()          
    
    def test_client_can_start_before_server(self):
        self.server.stop()
        
        wait_for_condition(lambda : not self.server.is_running())
        self.assertFalse(self.server.is_running(), 'valid test state, server is shut down')                
        self.client.start()

        self.wait_condition.acquire()        
        self.start_server()
        self.wait_condition.wait(self.connect_wait_secs)         
        self.assert_logon_received()
 
    def test_write_not_connected(self):
        response = test_data_factory.create_order_response()
        with self.assertRaises(NotLoggedInException):
            self.client.send_message(response)
            
    def test_write_connected_can_send_logon(self):
        self.client._set_state(ClientState.CONNECTED)
        mock_socket = Mock()
        mock_socket.sendall(bytearray())
        self.client._socket = mock_socket
        
        mock_socket.sendall.assert_called_once()
        logon = LogonRequest()
        self.client.send_message(logon)
        
        
    
    def test_calling_start_twice_does_nothing(self):
        mock_monitor = Mock()
        self.client.connection_monitor = mock_monitor
        mock_monitor.start()
        
        self.client.start()
        mock_monitor.start.assert_called_once()
 
            
        
    
 
        
    
class MockIserver(object):
    def __init__(self, port, handler):
        
        class ApiClientTestHandler(BaseRequestHandler):
            def __init__(self, *args):
                self.handler = handler  #function(header,body)
                super().__init__(*args)
                logger.debug('ApiClientTestHandler..__init__(): initialized handler')
                
            def handle(self):
                # parse header
                header = self.request.recv(15)
                if not header:
                    logger.error('error: did not receive enough bytes for an API header!')
                    return 
                length, msg_type, msg_subtype = ezx_msg.parse_header(header)
                logger.info(f'msg length={length}, msg_subtype={msg_subtype}')
                body = self.request.recv(length)
                self.handler(header, body)
                 
        self.port = port
        self.server =  TCPServer(('localhost', port), ApiClientTestHandler, False)
        # enable immediate reuse
        self.server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.server_bind()
        self.server.server_activate()
        logger.info(f'Server listening on: {self.server.server_address}')
        
    def start(self):
        logger.info(f'starting server on port={self.port}')
        t = threading.Thread(target=self.server.serve_forever)
        t.daemon = True
        t.start()
        self.server_thread = t
        logger.info(f'Server started.')
        # self.server.serve_forever()
        
    def is_running(self):
        try:
            return self.server_thread.is_alive()
        except AttributeError:
            pass
        
        
        
    def stop(self):
        logger.info('stopping server')
        self.server.shutdown()
        self.server.server_close()
        logger.info('server stopped')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()