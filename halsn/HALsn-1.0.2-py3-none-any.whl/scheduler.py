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

import time
from HALsn.sysLogger import sysLogger


class Routine:
    '''
    Object to handle quickly and efficiently building while loops
    to run and pre-determined time intervals. Reduces the need to
    create unique while loops with time checks, which are used
    frequently in the HALsn package.
    '''
    def __init__(self, freq: int = 1):

        # Frequency in HZ of the loop
        self.freq = freq
        # Period (inverse HZ) of the loop
        self.perd = 1 / self.freq
        # Initialize start time to 0
        self.t0 = 0

        # Standard Functions to run every time
        self.fncs = []
        self.args = []

        # Break conditions to check if the loop needs
        # to terminate
        self.bfncs = []
        self.bargs = []

        # Object Flag to check if the loop is runable
        self.validated = True
        # System Logger - Prints to Screen and Contributes to Log File
        self.logger = sysLogger(file=False)

    def add_functions(self, fncs, args: tuple) -> None:
        '''
        Add all STANDARD function-argument pairs to the
        object member
        '''
        if type(fncs) == list and type(args) == list:
            if len(fncs) == len(args):
                for fnc in fncs:
                    self.fncs.append(fnc)
                for arg in args:
                    self.args.append(arg)
            else:
                self.logger.ERROR(
                    'The function and arguments are not equivalent. Pass \'None\' if the function does not require arguments.')
                self.validated = False
        else:
            self.fncs.append(fncs)
            self.args.append(args)

    def add_break_functions(self, bfncs, bargs: tuple) -> None:
        '''
        Add all BREAK function-argument pairs to the
        object member
        '''
        if type(bfncs) == list and type(bargs) == list:
            if len(bfncs) == len(bargs):
                for bfnc in bfncs:
                    self.fncs.append(bfnc)
                for barg in bargs:
                    self.args.append(barg)
            else:
                self.logger.ERROR(
                    'The function and arguments are not equivalent. Pass \'None\' if the function does not require arguments.')
                self.validated = False
        else:
            self.bfncs.append(bfncs)
            self.bargs.append(bargs)

    def run(self) -> None:
        '''
        Checks that the object is configured to run
        a loop with valid break conditions. Exectues
        all STANDARD functions, then all BREAK
        functions. Exits when the break condition is
        met.
        '''
        if self.validated:
            if len(self.bfncs) > 0:
                self.t0 = self._current_time()
                ti = self.t0

                self._run_fncs()

                while True:

                    tf = self._current_time()
                    if self._two_point_decimal(tf - ti) >= self.perd:

                        ti = tf

                        self._run_fncs()

                        event = self._run_bfncs()
                        if event:
                            break
                    time.sleep(0.01)
            else:
                self.logger.CRITICAL(
                    'Cannot run loop without a break condition')

    def ext_timer(self) -> float:
        '''
        Function to keep track of routine timer in
        the case a function wants to recieve the
        time as an arguement.
        '''
        tf = self._current_time()
        return self._two_point_decimal(tf - self.t0)

    def return_functions(self) -> list:
        '''
        Shows all STANDARD functions currently
        appended to the self.fncs member
        '''
        return self.fncs

    def return_args(self) -> list:
        '''
        Shows all STANDARD arguments currently
        appended to the self.args member
        '''
        return self.args

    def return_bfunctions(self) -> list:
        '''
        Shows all BREAK functions currently
        appended to the self.fncs member
        '''
        return self.bfncs

    def return_bargs(self) -> list:
        '''
        Shows all BREAK arguments currently
        appended to the self.args member
        '''
        return self.bargs

    def _current_time(self) -> float:
        '''
        Contained time function. Reduces function
        call
        '''
        return self._two_point_decimal(time.perf_counter())

    def _run_fncs(self) -> None:
        '''
        Executes all STANDARD function argument
        pairs in the object member
        '''
        for idx, fnc in enumerate(self.fncs):
            fnc(self.args[idx])

    def _run_bfncs(self) -> bool:
        '''
        Executes all BREAK function argument
        pairs in the object member
        '''
        for idx, bfnc in enumerate(self.bfncs):
            event = bfnc(self.bargs[idx])
            if event:
                return True
        return False

    @staticmethod
    def _two_point_decimal(num: float) -> float:
        '''
        Formatting method to return a decimal to
        two decimal places.
        '''
        return float('{:.2f}'.format(num))
