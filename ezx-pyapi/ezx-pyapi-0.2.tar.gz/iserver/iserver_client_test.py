'''
Created on Sep 27, 2021

@author: Sgoldberg
'''

import socket

HOST = "192.168.1.218"
PORT = 15000


def connect() -> socket.socket :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((HOST, PORT))
        print('connected...')
        return s
    except Exception as e:
        print(f'connection failed: {e}')

