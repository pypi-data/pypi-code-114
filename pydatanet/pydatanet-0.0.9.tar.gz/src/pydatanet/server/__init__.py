import enum
import socket
import threading
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOCK_DGRAM, SOL_SOCKET

from pydatanet.server.client import Client
from pydatanet.data import encode, decode

class ServerType(enum.Enum):
    TCP = 0
    UDP = 1

class ServerStatus(enum.Enum):
    NOINIT = 0
    INIT = 1

BUFFER_SIZE = 2048

class Server:
    def __init__(self, host: str, port: int, serverType = ServerType.TCP, maxConn: int = 256):
        self.host = host
        self.port = port
        self.socket = None
        self.maxConn = maxConn
        self.status = ServerStatus.NOINIT
        self.clients = []
        self.serverType = serverType

        self.dataReceiveListeners = []

        if serverType == ServerType.TCP:
            print("* creating TCP socket")
            self.socket = socket.socket(AF_INET, SOCK_STREAM)
        elif serverType == ServerType.UDP:
            print("* creating UDP socket")
            self.socket = socket.socket(AF_INET, SOCK_DGRAM)
        else:
            raise ValueError(f"Invalid server type '{serverType}'!")

        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def on_recv(self, sender, data):
        """
        Triggered when someone sends a packet. Do not explicitly trigger as unexpected behaviour may occur.
        """
        data = decode(data)
        for listenFunc in self.dataReceiveListeners:
            listenFunc(sender, data)

    def on_recv_bind(self, func):
        """
        Bind a function to when someone sends data.
        """
        self.dataReceiveListeners.append(func)

    def connect(self):
        """
        Bind to that socket and start listening for connections.
        """
        if self.socket is not None:
            self.socket.bind((self.host, self.port))
            
            if self.serverType == ServerType.TCP:
                # TCP shenanigans that UDP does not fancy.
                self.socket.listen(self.maxConn)
                print(f"* socket is now listening at {self.host}:{self.port}")

            self.status = ServerStatus.INIT
            print("* server is now in heartbeating mode.")
            self.heartbeat()

    def _heartbeat(self):
        """
        Server heartbeat/poll method.
        """
        while self.status == ServerStatus.INIT:
            if self.serverType == ServerType.UDP:
                self.udp_poll()
            else:
                self.tcp_poll()

    def heartbeat(self):
        """
        Call this function once to start server polling. Automatically called by [Server.connect]
        """
        thr = threading.Thread(target = self._heartbeat, args=())
        thr.start()

    def getFromIp(self, ip: str):
        for client in self.clients:
            if client.getIp() == ip:
                return client

        return None

    def tcp_poll(self):
        """
        TCP socket polling method.
        """
        # Receive data from existing connections.
        for client in self.clients:
            data = client.conn.recv(BUFFER_SIZE)
            if not data:
                print(f"\t\t* [{client.ip}:{client.port}] did not send any data in return, indicating a disconnect.")
                client.close()
                self.clients.remove(client)
            
            self.on_recv(client, data)

        # Look out for new connections.
        conn, addr = self.socket.accept()
        print(f"\t* new connection has been established [{addr[0]}:{addr[1]}]")

        self.clients.append(
            Client(addr[0], addr[1], conn)
        )

    def udp_poll(self):
        pass
    
    def stop(self):
        """
        Stop the server by closing the socket.
        """
        print(f"* socket at {self.host}:{self.port} is now closing.")
        self.socket.close()

    def __del__(self):
        self.stop()