#!/usr/bin/python

import time
import serial
import logging

# import numpy
import timeout_decorator


class TimeoutException(Exception):
    def __init__(self, message="Timed out"):
        super().__init__(message)

class manson(object):
    """
    Class to controll manson HCS and SDP power supplies
    """

    Vmax = None  # Maximum voltage / V
    Imax = None  # maximum current / A
    supported_modes = [232, 485] # Supported interfaces
    supported_devices = {
        # GMAX Return value: ["Device ID", "Max. supply voltage", "Max. current", "Current scale factor"]
        "605160": ["HCS-3404", 60, 16, 0.1],
        "362120": ["HCS-3202", 36, 10, 0.1],
        "402502": ["SDP-2405", 40, 5, 0.01],
    }
    device_type = ""
    current_factor = 1
    __logger = logging.getLogger(__name__)

    def __init__(self, port: str, mode: int = 232, channel: int = -1, sp=None):
        """
        Open Manson Device HCS or SDP at ``port`` or Channel and clear both input and
        output buffer. The serial interface can be accessed via ``self.sp``.

        :param port: path to port (default */dev/ttyUSB0*)
        :param serial.Serial sp: parse serial interface directly
        """
        if mode not in self.supported_modes:
            msg = f"Interface {mode} is not supported only {self.supported_modes}"
            raise ValueError(msg)
        if mode == 232 and channel != -1:
            channel = -1
            self.__logger.warning("Channel information is ignored in RS232 mode.")
        elif mode == 485 and (channel < 0 or channel > 255):
            msg = f"Incorrect channel {channel} (min. 0, max. 255)"
            raise ValueError(msg)


        self.mode = mode
        self.port = port  # Open serial port.
        self.sp = sp or self.get_serial(port)  # open serial port
        self.channel = channel
        self.sp.flushInput()  # Clears input buffer.
        self.sp.flushOutput()  # Clears output buffer.

    def test(self):
        self.init_serial()
        return True

    def get_serial(self, port: str):
        """
        Initialize serial interface

        :param str port: path to ``port``
        """
        ser = serial.Serial(
            port,
            9600,
            timeout=1,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
        )
        return ser

    def readline(self, timeout=2.0):
        """
        Read data from ``port``. Raise timeout exception if nothing is communicated.

        :param timeout: Time untile *TimeoutException* will be raised
        """
        n = 0
        while True:
            line = self.sp.readline()
            if len(line) != 0:
                break

        line = line.replace(b"\r", b"")
        line = line.replace(b"OK", b"")
        line = line.decode("utf-8")
        return line

    def txrx(self, send, arg=""):
        """
        Communication to serial device. Sends the command stored in send together with additional control parameters to the serial interface.

        :param str send: Serial command according to device manual
        :param str arg: additional arguments
        The function is but on hold until it receives OK from the serial device.
        """
        if self.mode == 232 and self.channel == -1:
            cmd = (send + arg + "\r").encode()
        else:
            cmd = send.encode() + self.channel.to_bytes(2, 'big') + arg.encode() + b"\r"

        self.sp.write(cmd)
        out = self.readline()
        return out

    @timeout_decorator.timeout(5, timeout_exception=TimeoutException)
    def cmd(self, c, c2=""):
        """Calls txrx for serial communication

        :param str c: command
        :param str c2: argument
        """
        out = self.txrx(c, c2)
        return out

    def __getattr__(self, attr):
        if attr.isupper():
            return lambda *args: self.cmd(attr, *args)
        else:
            raise AttributeError("Dunno about " + repr(attr))

    def begin_session(self):
        """
        Locks the control panel.  This is not required to control the
        supply, but is useful for long-running tests where curious fingers
        might disrupt things.
        """
        self.SESS()

    def end_session(self):
        """Unlocks device again and leaves the device in a defined state"""
        self.ENDS()

    def __str__(self):
        return f"{self.device_type}: Max. {self.Vmax}V {self.Imax}A"

    def init_serial(self):
        """Initial command sequence."""

        try:
            self.GMAX()
        except TimeoutException:
            self.channel = 0
            try:
                self.GMAX()
            except:
                raise TimeoutException("Unable to connect to device.")

        max_values = self.GMAX()
        if not max_values:
            return
        if max_values in self.supported_devices.keys():
            info = self.supported_devices[max_values]
            self.device_type = info[0]
            self.Vmax = info[1]
            self.Imax = info[2]
            if "SDP" in info[0] and self.mode == 232:
                self.channel = 0
            self.current_factor = info[3]
        else:
            raise ValueError(f"Unknown device config:\t{max_values}")

    def set_volts(self, volts):
        """Set volts

        :param float volts: 1-Vmax Volts
        """
        if volts > self.Vmax:
            self.__logger.error(
                str(volts)
                + "V too high, max. "
                + str(self.Vmax)
                + "V ->  deactivate output"
            )
            self.output_off()
        elif volts < 1:
            self.output_off()
            self.__logger.error(str(volts) + "V too low, min 1V -> deactivate output")
        else:
            self.VOLT("%03d" % int(volts * 10.0))
            time.sleep(0.01)

    def set_amps(self, amps):
        """Set current

        :param float amps: 0-Imax Ampere
        """
        if amps > self.Imax:
            self.__logger.error(
                str(amps)
                + "A too high, max. "
                + str(self.Imax)
                + "A ->  deactivate output"
            )
            self.output_off()
        else:
            self.CURR("%03d" % int(amps / self.current_factor))
            time.sleep(0.01)

    def get_volts_amps(self):
        """Set current

        :returns: voltage and current
        :rtype: list of floats
        """
        resp = self.GETD()
        volts = int(resp[:4]) * 0.01
        amps = int(resp[4:8]) * self.current_factor
        return volts, amps

    def get_volts(self):
        """get voltage. This is not faster than get_volts_amps!

        :returns: voltage
        :rtype: float
        """
        return self.get_volts_amps()[0]

    def get_amps(self):
        """get current. This is not faster than get_volts_amps!

        :returns: current
        :rtype: float
        """
        return self.get_volts_amps()[1]

    def output_on(self, on=True):
        """turn on the DC output of the power supply"""
        self.SOUT("10"[bool(on)])
        time.sleep(0.01)

    def output_off(self):
        """turn off the DC output of the power supply"""
        return self.output_on(False)
