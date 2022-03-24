#!/usr/bin/env python3

"""
Simplistic local message bus using multicast. When a message is sent, it is
distributed to all connected parties but not to the sender (no loopback).
Messages are strings (binary stuff has to be escaped) and, when encoded, can 
be up to 1020 bytes long (4 bytes are used for framing). Longer messages are 
discarded.
"""

import errno
import fcntl
import os
import select
import signal
import socket
import struct
import sys
import threading
import time

# defaults
MULTICAST_GROUP = "224.1.2.3"
MULTICAST_PORT = 54321

class Bus:
    def __init__(self, receive_callback, multicast_group=MULTICAST_GROUP, 
            multicast_port=MULTICAST_PORT, unique_identifier=None):
        self.receive_callback = receive_callback
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.group = multicast_group
        self.port = multicast_port

        # It seems that I need IP_MULTICAST_TTL 0 for the packets to stay on the host 
        # and IP_MULTICAST_LOOP 1 for the packets to be seen by another process.
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 0)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # join the multicast group
        self.socket.bind((self.group, self.port))
        mreq = struct.pack("4sl", socket.inet_aton(self.group), socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
        # start the receive thread
        self.run = True
        self.thread = threading.Thread(target=self.recv_thread)
        self.thread.start()
        if unique_identifier:
            self.uid = unique_identifier
        else:
            self.uid = self.thread.native_id

    def send(self, payload: str) -> bool:
        # some lightweight framing that holds the uuid
        encoded = payload.encode()
        if len(encoded) > (1024-4):
            return False
        data = self.uid.to_bytes(4, sys.byteorder) + encoded
        self.socket.sendto(data, (self.group, self.port))
        return True

    def stop(self):
        self.run = False

    def recv_thread(self):
        while self.run:
            readable, _, _ = select.select([self.socket],[],[], 0.5)
            if readable:
                data = self.socket.recv(1024)
                if data:
                    if self.receive_callback:
                        # care about framing
                        uid = int.from_bytes(data[0:4], sys.byteorder)
                        payload = data[4:]
                        # loopback detection
                        if uid != self.uid:
                            self.receive_callback(payload.decode())

