from __future__ import annotations

import time
from threading import Lock

from serial import PARITY_EVEN, Serial

from stx.errors import SerialError
from stx.utils import lock_threading_lock


class SerialPort:
    __serial_port: Serial
    __port_lock: Lock
    __timeout: float

    def __init__(self, port: str, *, timeout: float) -> None:
        """
        Wraps a plain serial connection to simplify communication with LiCONiC STX devices

        Parameters
        ----------
        port : str
            The address of the port (e.g. "COM3" on Windows or "/dev/ttyACM0" on Unix)
        timeout: float, seconds
            A :class:`TimeoutError` will be raised of read or write operations took longer than this duration
        """
        self.__serial_port = Serial(port, parity=PARITY_EVEN, timeout=timeout, write_timeout=timeout)
        self.__port_lock = Lock()
        self.__timeout = timeout

    def __communicate(self, command: str) -> str:
        """
        Send a command to the port and return the response

        Raises
        ------
        TimeoutError
            If a read or write operation took too long
        SerialError
            If the response was E0 to E5, or there were unread bytes in the input buffer before sending the command
        """
        with lock_threading_lock(self.__port_lock, timeout=self.__timeout):
            if self.__serial_port.in_waiting:
                raise SerialError("There were unread bytes in the input buffer")

            raw_response = b""
            self.__serial_port.write(command.encode("ascii") + b"\r")

            time.sleep(0.1)
            while not raw_response.endswith(b"\r\n"):
                char = self.__serial_port.read()
                if not char:
                    raise TimeoutError(rf"Did not receive a '\r\n'-terminated response after {self.__timeout} seconds")
                raw_response += char

            response = raw_response[:-2].decode("ascii")

            if response in ("E0", "E1", "E2", "E3", "E4", "E5"):
                raise SerialError.from_response(response)

            return response

    def open(self) -> None:
        """Open the connection by sending 'CR'"""
        self.send_and_expect_response("CR", "CC")

    def close(self) -> None:
        """Close the connection by sending 'CQ'"""
        self.send_and_expect_response("CQ", "CF")

    def send_and_expect_response(self, command: str, expected_response: str) -> None:
        """
        Send the command and raise a SerialError if the response was different than expected

        Parameters
        ----------
        command
            The command to send to the device
        expected_response
            The expected response

        Raises
        ------
        SerialError
            If the response was different than expected
        """
        response = self.__communicate(command)
        if response != expected_response:
            raise SerialError.from_response(response)

    def send_and_expect_ok(self, command: str) -> None:
        """
        Send the command and raise a SerialError if the response was not 'OK'

        Parameters
        ----------
        command
            The command to send to the device

        Raises
        ------
        SerialError
            If the response was different than expected
        """
        self.send_and_expect_response(command, "OK")

    def read_bit(self, address: int) -> bool:
        """
        Read the bit value at the given address

        Parameters
        ----------
        address
            The address to read
        """
        return self.__communicate(f"RD {address}") == "1"

    def read_data(self, address: int) -> int:
        """
        Read the data memory value at the given address

        Parameters
        ----------
        address
            The address to read
        """
        return int(self.__communicate(f"RD DM{address}"))
