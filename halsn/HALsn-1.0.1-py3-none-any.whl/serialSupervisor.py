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

from curses import baudrate
import sys
import serial
import serial.serialutil
import time
from HALsn.sysLogger import sysLogger


class serialRoot(serial.Serial):
    '''
    Base serial object to provide methods which combine the
    required serial.Serial methods and message conversion
    methods for reading data over a serial port.
    '''
    def __init__(self, port: str, baud: int, timeout: float):

        # Generation of serial object
        try:
            super().__init__(port=port, baudrate=baud, timeout=timeout)
        except serial.serialutil.SerialException:
            self.logger.CRITICAL(
                f'Port [{self.port}] cannont be connected.')
            sys.exit()

         # System Logger - Prints to Screen and Contributes to Log File
        self.logger = sysLogger()

    def open_port(self) -> None:
        '''
        Opens the serial port to the serial device.
        '''
        if not self.isOpen():
            self.open()
            self.logger.INFO(
                f'[{self.port}] Open = {self.isOpen()}')

    def close_port(self) -> None:
        '''
        Closes the serial port to the serial device.
        '''
        if self.isOpen():
            self.close()
            self.logger.INFO(
                f'[{self.port}] Open = {self.isOpen()}')

    def _send_msg(self, msg: str) -> None:
        '''
        Writes a message to the serial slave. Reduces funtion
        call.
        '''

        try:
            self._reset_buffers()
            if self.isOpen():
                self.write(msg.encode())
            else:
                self.logger.ERROR(f'[{self.port}] is closed...')
        except serial.SerialException:
            self.logger.CRITICAL(
                f'[{self.port}]Serial Error while Writing...')
            self.close_port()
            sys.exit()

    def _read_msg(self) -> str:
        '''
        Reads a message from the serial slave. Returns False
        if nothing is read. Reduces function call.
        '''

        try:
            self._reset_buffers()
            if self.isOpen():
                msg = self.read_until(b'\r')
                return msg.decode()
            else:
                self.logger.CRITICAL(
                    f'[{self.port}]Serial Error while Reading...')
                self.close_port()
                sys.exit()
        except serial.SerialException:
            self.logger.CRITICAL(
                f'[{self.port}]Serial Error while Reading...')
            self.close_port()
            sys.exit()

    def _reset_buffers(self) -> None:
        '''
        Resets Input and Output buffers to prevent
        overflow.
        '''
        self.reset_input_buffer()
        self.reset_output_buffer()


class serialSupervisor(serialRoot):
    '''
    Further abstracted serial object to run serial commands in a
    command/query format.
    '''
    def __init__(self, port: str, baud: int, timeout: float):

        super().__init__(port, baud, timeout)

    def command(self, command_id: str, delay: float = 0.0) -> None:
        '''
        Sends command to serial slave. Argument should be a
        string.

        command_id refers to a dictionary key that will send
        the appropriate value to the appropriate slave.
        '''
        command = self.commands[command_id]
        self._send_msg(command)
        time.sleep(delay)

    def query(self, query_id: str) -> str:
        '''
        Sends request command to serial slave and waits for
        a respone. If no response is received after 3
        attempts, an error is thrown and the code will exit.
        '''
        query = self.queries[query_id][0]
        self._send_msg(query)
        return self._read_msg()

    def specific_query(self, queries: list) -> list:
        '''
        Takes a list of query IDs as an argument. Sends each query
        and collects the response. Intended for special cases where
        looking at subsets of data is required.
        '''
        row = []
        for query in queries:
            query = self.queries[query][0]
            self._send_msg(query)
            row.append(self._read_msg())
        return row

    def master_query(self) -> list:
        '''
        Queries every option in the relevant query dictionary
        and compiles it into a list. 
        '''
        row = []
        for query in self.queries.values():
            if query[1] == 1:
                self._send_msg(query[0])
                row.append(self._read_msg())
        return row

    def return_commands(self) -> list:
        '''
        Returns list of all available commands for
        device. Useful to print out when developing.
        '''
        return self.commands.keys()

    def return_queries(self) -> list:
        '''
        Returns list of all available queries for
        device. Useful to print out when developing.
        '''
        return self.queries.keys()
