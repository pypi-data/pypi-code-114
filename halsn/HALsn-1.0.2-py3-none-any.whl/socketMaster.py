#!/usr/bin/env python3

'''
MIT License

Copyright (c) 2021 Mikhail Hyde & Cole Crescas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import socket
import threading
import pickle
from HALsn.serialSupervisor import serialRoot
from HALsn.dataSupervisor import dataSupervisor, errorHandler


class socketRoot:
    '''
    Fundamental socket object. Contains all information requied to make a
    Server or Client and provides a base class that further implementations
    can inherit from.

    Contains essential methods to send and receive messages and is designed
    to send pickled python objects in order to maximize versatility.
    '''

    def __init__(self, server_ip: str, port: int, is_server: bool = False):

        # NUMBER OF BYTES FOR HEADER
        self.HEADER = 128
        # CONNECTION PORT
        self.PORT = port
        # IP ADDRESS OF RELEVANT SERVER
        self.SERVER = server_ip
        # ADDRESS VARIABLE FOR SERVER
        self.ADDR = (self.SERVER, self.PORT)

        # DISCONNECT MESSAGE
        self.DC_MSG = '!DC'

        # Socket Object of each Client or Server
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # If object is inteded as server, Bind to Address
        if is_server:
            self.node.bind(self.ADDR)
        # Else, connect to address of server
        else:
            self.node.connect(self.ADDR)

    def _build_header(self, en_msg: str) -> str:
        '''
        Identifies message length and returns
        and encoded string that is sent prior
        to the message to inform the recipient
        how long the incoming message is
        '''
        msg_len = str(len(en_msg))
        header = pickle.dumps(msg_len)
        return header + (b' ' * (self.HEADER - len(header)))

    def send_msg(self, conn: socket.socket, msg: str) -> None:
        '''
        Handles the socket sending protocol.
        Builds the header and sends it and the
        message in one function call
        '''
        en_msg = pickle.dumps(msg)
        header = self._build_header(en_msg)
        conn.send(header)
        conn.send(en_msg)

    def recv_msg(self, conn: socket.socket) -> str:
        '''
        Recieves length of incoming message and
        then returns the actual message.
        '''
        msg_len = conn.recv(self.HEADER)
        if msg_len:
            msg_len = int(pickle.loads(msg_len))
            print(f'Message Length: {msg_len}')
            return pickle.loads(conn.recv(msg_len))
        return None


##############################################################################

##########                      SERVERS                             ##########

##############################################################################


class server(socketRoot):
    '''
    Base server implementation. All functional servers should inherit from
    this object and redefine the 'HANDLE' Method. The process for all servers
    works by accepting a connection and handling that connection on a thread.
    What is done by the handle method depends on the implementation of the
    server.
    '''

    def __init__(self, server_ip: str, port: int, is_server: bool = True):
        super().__init__(server_ip=server_ip, port=port, is_server=is_server)

    def handle(self, conn: socket.socket, addr: str,
               connLock: threading.Lock) -> None:
        '''
        Function to run as a thread for each connected
        client. Handles the incoming messages and runs
        a predefined routine for scalability and
        repurposing.
        '''

        print(f'[NEW CONNECTION] {addr} connected.')

        while True:

            msg = self.recv_msg(conn)
            msg_type = type(msg)

            if msg is not None:

                if msg_type == str:
                    if msg == self.DC_MSG:
                        break

                connLock.acquire(timeout=1)

                connLock.release()

        conn.close()

    def start(self) -> None:
        '''
        Initializes a server. Generates a thread for
        each client that connects to the system.
        '''
        self.node.listen()
        print(f"[LISTENING] Server is listening on {self.node}")
        connLock = threading.Lock()
        while True:
            conn, addr = self.node.accept()
            thread = threading.Thread(
                target=self.handle, args=(conn, addr, connLock))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


class dataServer(server):
    '''
    Server Object. Called once on a machine to serve
    as an access point for LAN communication. Clients
    will make requests to this point for system status
    and data transmission.  This server object is used to 
    transfer data frames into the s3 bucket from the incoming
    raspberry pi nodes.
    '''

    def __init__(self, server_ip: str, port: int, is_server: bool = True):

        super().__init__(server_ip=server_ip, port=port, is_server=is_server)

    def handle(self, conn: socket.socket, addr: str,
               connLock: threading.Lock) -> None:
        '''
        Function to run as a thread for each connected
        client. Handles the incoming messages and runs
        a predefined routine for scalability and
        repurposing. 
        '''
        print(f'[NEW CONNECTION] {addr} connected.')
        while True:
            msg = self.recv_msg(conn)
            msg_type = type(msg)
            if msg is not None:
                if msg_type == str:
                    if msg == self.DC_MSG:
                        break
                connLock.acquire(timeout=1)
                handler = errorHandler(msg)

                super = dataSupervisor(
                    map=None, headers=False, s3_enable=False)
                super.parser.df = handler.master
                super.filename = 'test.csv'
                super.localfile = '/home/hal/Desktop/test.csv'
                super.export_csv()
                connLock.release()
        conn.close()


class cltHardwareServer(server):
    '''
    Hardware server for Coffee Life Test Fixture. Intended to operate on
    a Raspberry Pi/Arduino Mega pair and accept hardware requests from
    clients (nodes or bays) on the rig. Clients send messages as requests
    for hardware status and hardware enabling. The server handles these
    requests and responds accordingly.
    '''
    def __init__(self, server_ip: str, port: int, is_server: bool = True):

        super().__init__(server_ip=server_ip, port=port, is_server=is_server)

        # Arduino Serial Object to be controlled by incoming messages
        self.ard = serialRoot('/dev/Arduino', 115200, 0.25)

    def handle(self, conn: socket.socket, addr: str,
               connLock: threading.Lock) -> None:
        '''
        Function to run as a thread for each connected
        client. Handles the incoming messages and runs
        a predefined routine for scalability and
        repurposing.
        '''
        print(f'[NEW CONNECTION] {addr} connected.')
        while True:
            msg = self.recv_msg(conn)
            if msg is not None:
                print(f'[{addr}] {msg}')
                if msg == self.DC_MSG:
                    break
                connLock.acquire(timeout=1)
                tag = msg[0]
                msg = msg[1:]
                self.ard._send_msg(msg)
                if tag == '?':
                    self.send_msg(self.ard._read_msg())
                connLock.release()
        conn.close()


##############################################################################

##########                      CLIENTS                             ##########

##############################################################################


class client(socketRoot):
    '''
    Base client implementation. Mostly based on the socketRoot
    object. Should handle most implementations of socket
    communication.
    '''

    def __init__(self, server_ip: str, port: int):

        super().__init__(server_ip=server_ip, port=port)

    def disconnect(self) -> None:
        '''
        Sends disconnect message to the server. This
        closes the connection over the port and exits
        the thread on the server end
        '''
        msg = self.DC_MSG
        self.send_msg(self.node, msg)


class cltHardwareClient(client):
    '''
    CLTF Client. Adds the command/query map to the client
    and provides message type differentiating. A request
    to enable a piece of hardware is preceeded with an
    '*' and a request for system state is preceeded with
    a '?'.
    '''
    def __init__(self, server_ip: str, port: int):

        super().__init__(server_ip=server_ip, port=port)

        self.commands = {
            # Enable Input Pump for Bay N
            'en_input_pump':       '*0x01!',
            # Disable Input Pump for Bay N
            'dis_input_pump':      '*0x00!',
            # Enable Output Pump for Bay N
            'en_output_pump':      '*1x01!',
            # Disable Output Pump for Bay N
            'dis_output_pump':     '*1x00!',
            # Set Output Pump Timer - 10 Seconds
            'output_time_10':      '*3x10!',
            # Set Output Pump Timer - 20 Seconds
            'output_time_20':      '*3x20!',
            # Set Output Pump Timer - 30 Seconds
            'output_time_30':      '*3x30!',
            # Set Output Pump Timer - 40 Seconds
            'output_time_40':      '*3x40!',
            # Set Output Pump Timer - 50 Seconds
            'output_time_50':      '*3x50!',
            # Set Output Pump Timer - 60 Seconds
            'output_time_60':      '*3x60!',
        }

        self.queries = {
            # Request Bay N Input Pump State
            'input_pump_status':   '*0x02!',
            # Request Bay N Output Pump State
            'output_pump_status':  '*1x02!',
            # Request Bay N Res Float State
            'res_float_status':    '*2x00!'
        }

    def cmd_hw_state(self, cmd_id: str) -> None:
        '''
        Controls hardware state (pumps, fans, etc..).
        Does not expect a response.
        '''
        msg = '*' + self.node_id + self.commands[cmd_id]
        self.send_msg(self.node, msg)

    def req_hw_status(self, qry_id: str) -> str:
        '''
        Requests system state. Expects a response.
        '''
        msg = '?' + self.node_id + self.queries[qry_id]
        self.send_msg(self.node, msg)
        return self.recv_msg(self.node)
