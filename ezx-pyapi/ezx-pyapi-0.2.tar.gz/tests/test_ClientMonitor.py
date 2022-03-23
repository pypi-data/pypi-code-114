'''
Created on 21 Mar 2022

@author: shalomshachne
'''
import logging
from time import sleep
import time
import unittest

from iserver.net import ClientMonitor, ApiClient, ClientState
from tests.data import test_data_factory
from tests import wait_for_condition


waitTime = .050
def wait_for_connection(client):
    start = time.time()
    maxwait = waitTime * 10 
    while not ClientState.CONNECTED == client.state() and time.time() - start <= maxwait:
        sleep(waitTime)

class ClientMonitorTest(unittest.TestCase):


    def setUp(self):
        self.client = MonitorTestClient()
        self.client.set_retry_seconds(waitTime)        
        self.monitor = ClientMonitor(self.client)
        

    def tearDown(self):
        self.monitor.stop()

    def test_initial_state(self):
        self.assertFalse(self.monitor.is_running(), 'not running')

    def testStart(self):
        logging.debug('testStart: starting monitor')        
        self.monitor.start()
        logging.debug('testStart: waiting for connection')        
        wait_for_connection(self.client)
        self.assertEqual(ClientState.CONNECTED, self.client.state(), 'called connect')
        self.assertTrue(self.monitor.is_running(), 'monitor is running')
        
    def test_stop(self):
        self.testStart()
        self.monitor.stop()
        wait_for_condition(lambda : not self.monitor.is_running())
        self.assertFalse(self.monitor.is_running(), 'correct running state')
        
        
    def testReconnects(self):
        logging.debug('testReconnects: started')
        self.testStart()
        self.assertEqual(1, self.client.connect_counter, 'valid initial state, 1 connection attempt')
        
        self.client._set_state(ClientState.DISCONNECTED)
        sleep(waitTime * 5)
        self.assertEqual(2, self.client.connect_counter, 'attempted reconnect')
        self.assertEqual(ClientState.CONNECTED, self.client.state(), 'called connect')

    def testNoReconnectWhenLoggedIn(self):
        self.testStart()
        self.client._set_state(ClientState.LOGGED_IN)
        sleep(waitTime * 2)
        self.assertEqual(1, self.client.connect_counter, 'no attempted reconnect')
    
    def testNoReconnectWhenStoped(self):
        self.testStart()
        self.client._set_state(ClientState.STOPPED)
        sleep(waitTime * 2)
        self.assertEqual(1, self.client.connect_counter, 'no attempted reconnect')

class MonitorTestClient(ApiClient):
    def __init__(self):
        super().__init__(test_data_factory.create_connection_info())
        self.started = False
        self.connect_counter = 0
        
    def start(self):
        self.started = True
        
    def _connect(self):
        self.connect_counter = self.connect_counter + 1
        self._set_state(ClientState.CONNECTED)
        
    def set_retry_seconds(self, seconds : float):
        self.connection_info.connect_retry_seconds = seconds    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()