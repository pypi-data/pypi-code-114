# -*- coding: utf-8 -*-
import os
import sys
import uuid
import time
import socketio
from pynput import keyboard


DEFAULT = "KamiBot"
IP_ADRESS = "127.0.0.1"
SLEEP = 0.2
PORT = "50307"


class KamiNet:

    def __init__(self, ipaddr=IP_ADRESS):
        self.__ipaddr = ipaddr
        self.__userid = None
        self.__cb = None
        sio = socketio.Client()
        self.__sio = sio
        self.__connected = False
        
        @sio.event
        def connect():
            # print("Connected to server...!")
            pass

        @sio.event
        def connect_error(data):
            print('Connect Error:', data)

        @sio.event
        def disconnect():
            print("Disconnected")

        @sio.event
        def handshake(msg):
            self.__userid = str(uuid.uuid4())
            self.__sio.emit("joinRoom", {"username": self.__userid, "room": "kaminet"})

        @sio.event
        def roomUsers(msg):
            # print('roomUser:', msg)
            if self.__cb is not None:
                self.__cb('connect', {'result': True})

        @sio.event
        def message(msg):
            # print("message", msg)
            if self.__cb is not None and msg["username"] != DEFAULT:
                self.__cb('message', msg)
            self.__sio.sleep(SLEEP)


    def __background_task(self):
        # self.__sio.sleep(SLEEP)
        with keyboard.Events() as events:
            for event in events:
                if event.key == keyboard.Key.esc or event.key == keyboard.KeyCode.from_char('q') or event.key == keyboard.KeyCode.from_char('Q'):
                    self.__sio.disconnect()
                    sys.exit()


    def formatMessage(self, username, txt):
        return {'username': username, 'text':txt, 'time': time.strftime('%I:%M:%S %p', time.localtime())}
    
    def connect(self, cb=None):
        print(f'http://{self.__ipaddr}:{PORT}')
        self.__cb = cb
        self.__sio.connect(f'http://{self.__ipaddr}:{PORT}')
        # self.__sio.start_background_task(self.__background_task)
        # wait함수는 블록킹된다.
        # self.__sio.wait()

    def disconnect(self):
        self.__sio.disconnect()

    def wait(self):
        # 멈추기위해서는 ESC키 
        self.__sio.start_background_task(self.__background_task)
        self.__sio.wait()
        
    def send(self, msg):
        if self.__sio:
            print('send')
            self.__sio.emit("chatMessage", msg)

