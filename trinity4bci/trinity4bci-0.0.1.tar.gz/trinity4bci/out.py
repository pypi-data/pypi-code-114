import serial
import socket
import zmq
import time

class Controller:
    """
    Very very basic script that displays the output from sfpr
    """
    def __init__(self):

        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.SUB)
        self.sock.connect("tcp://127.0.0.1:1234")
        self.sock.subscribe("")  # Subscribe to all topics
        self.keep_alive = True

    def spin(self):
        '''
        Keeps the Controller listening and recieving all incoming topics, 
        in this case will constantly be listening to comands from Signal Filter and Processing Relay 
        '''
        print("Starting reciever loop . . . ")
        print("Listening for output value")

        while self.keep_alive:
            msg = self.sock.recv_string()
            print(msg)
        #
        #
        #
        #
        #
        #
        #
        self.sock.close()
        self.ctx.term()


if __name__ == "__main__":
    controller = Controller()
    controller.spin()
