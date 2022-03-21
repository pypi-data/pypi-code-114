import socket
import struct
import threading
import time
from typing import Callable

from prontonet.protocol import ProntonetProtocol
from prontonet.structures import ProntonetCommand, StatusLineStatusChanged, StatusAlarmsStatusChanged, \
    StatusDecoderAudioModeChanged, StatusEncoderAudioModeChanged
from prontonet.enums import Command, AlarmStatus, LineStatus, IPCallType, Codec


class ProntonetDevice:
    """
    A class used to represent Prontonet Device.

    ...

    Attributes
    ----------
    ip : str
        IP address of Prontonet device.
    port : int
        Port number of command protocol.
    status_port : int
        Port number of status protocol.

    Methods
    -------
    connect()
        Connects to status protocol socket and starts listening for messages.

    disconnect()
        Disconnects from status protocol socket.

    attach_on_connected(func, *args)
        Method to attach function, which will be executed after status socket connected.

    attach_on_status_socket_disconnected(func, *args)
        Method to attach function, which will be executed after status socket disconnected.

    attach_on_line_status_changed(func, *args)
        Method to attach function, which will be executed after line status changed.

    attach_on_alarm_status_changed(func, *args)
        Method to attach function, which will be executed after alarm status changed.

    attach_on_decoder_audio_mode_changed(func, *args)
        Method to attach function, which will be executed after decoder audio mode changed.

    attach_on_encoder_audio_mode_changed(func, *args)
        Method to attach function, which will be executed after encoder audio mode changed.

    send_command(command: ProntonetCommand)
        Send command to command protocol socket.

    """

    def __init__(self, ip, port=50031, status_port=50035):
        """
        Parameters
        ----------
        ip : str
            IP address of Prontonet device.
        port : int
            Port number of command protocol. (default is 50031)
        status_port : int
            Port number of status protocol. (default is 50035)
        """

        self.__command_socket: socket.socket or None = None
        self.__status_socket: socket.socket or None = None
        self.__status_th: threading.Thread or None = None
        self.ip: str = ip
        self.port: int = port
        self.status_port: int = status_port

        self.__on_connected: Callable or None = None
        self.__on_connected_args: tuple or None = None
        self.__on_status_socket_disconnected: Callable or None = None
        self.__on_status_socket_disconnected_args: tuple or None = None
        self.__on_status_socket_reconnected: Callable or None = None
        self.__on_status_socket_reconnected_args: tuple or None = None
        self.__on_line_status_changed: Callable or None = None
        self.__on_line_status_changed_args: tuple or None = None
        self.__on_alarm_status_changed: Callable or None = None
        self.__on_alarm_status_changed_args: tuple or None = None
        self.__on_decoder_audio_mode_changed: Callable or None = None
        self.__on_decoder_audio_mode_changed_args: tuple or None = None
        self.__on_encoder_audio_mode_changed: Callable or None = None
        self.__on_encoder_audio_mode_changed_args: tuple or None = None

    def connect(self) -> None:
        """
        Connects to status protocol socket and starts listening for messages.

        Returns
        -------
        None
        """

        self.__status_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__status_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.__status_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 1)
        self.__status_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 1)
        self.__status_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 5)

        self.__status_socket.connect((self.ip, self.status_port))

        if self.__on_connected is not None:
            self.__on_connected(self.__on_connected_args)

        self.__status_th = threading.Thread(target=self.__status_loop, daemon=True)
        self.__status_th.start()

    def __status_loop(self) -> None:
        """
        Listens for status change. When socket disconnects, attempts to reconnect.

        Returns
        -------
        None
        """

        connected = True
        while True:
            if not connected:
                try:
                    self.__status_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                    self.__status_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 1)
                    self.__status_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 1)
                    self.__status_socket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 5)
                    self.__status_socket.connect((self.ip, self.status_port))
                    connected = True
                    time.sleep(2)
                    if self.__on_status_socket_reconnected is not None:
                        self.__on_status_socket_reconnected(self.__on_status_socket_reconnected_args)
                except socket.error:
                    time.sleep(5)
            else:
                try:
                    data = self.__status_socket.recv(1024)
                    self.__process_status_message(data)
                except socket.error:
                    if self.__on_status_socket_disconnected is not None:
                        self.__on_status_socket_disconnected(self.__on_status_socket_disconnected_args)
                    time.sleep(1)
                    self.__status_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connected = False

    def __process_status_message(self, message: bytes) -> None:
        """
        Processes status messages. If function is attached to event, this method executes it.

        Parameters
        ----------
        message : bytes
            Message received from status socket.
        Returns
        -------
        None
        """

        if message[0] == Command.STATUS_LINE_STATUS_CHANGED:
            if self.__on_line_status_changed is not None:
                res = struct.unpack("<ii32sii", message[8:])
                num = ''.join(list(s for s in bytes(res[2]).decode("utf-8") if s.isprintable()))
                status = StatusLineStatusChanged(res[0], LineStatus(res[1]), num, res[3], IPCallType(res[4]))
                self.__on_line_status_changed(status, self.__on_line_status_changed_args)
        elif message[0] == Command.STATUS_ALARMS_STATUS_CHANGED:
            if self.__on_alarm_status_changed is not None:
                status = struct.unpack("<i", message[8:])
                self.__on_alarm_status_changed(StatusAlarmsStatusChanged(AlarmStatus(status[0])),
                                               self.__on_alarm_status_changed_args)
        elif message[0] == Command.STATUS_DECODER_AUDIO_MODE_CHANGED:
            if self.__on_decoder_audio_mode_changed is not None:
                message_len = len(message) - 12
                status = struct.unpack("<i" + str(message_len) + "s", message[8:])
                codec_name = ''.join(list(s for s in bytes(status[1]).decode("utf-8") if s.isprintable()))[:-1]
                self.__on_decoder_audio_mode_changed(StatusDecoderAudioModeChanged(Codec(status[0]), codec_name),
                                                     self.__on_decoder_audio_mode_changed_args)
        elif message[0] == Command.STATUS_ENCODER_AUDIO_MODE_CHANGED:
            if self.__on_encoder_audio_mode_changed is not None:
                message_len = len(message) - 12
                status = struct.unpack("<i" + str(message_len) + "s", message[8:])
                codec_name = ''.join(list(s for s in bytes(status[1]).decode("utf-8") if s.isprintable()))[:-1]
                self.__on_encoder_audio_mode_changed(StatusEncoderAudioModeChanged(Codec(status[0]), codec_name),
                                                     self.__on_encoder_audio_mode_changed_args)
        else:
            print("[!] Unknown status message received.")

    def disconnect(self) -> None:
        """
        Stops listening for status messages and closes status socket.

        Returns
        -------
        None
        """

        self.__status_th.join()
        self.__status_socket.close()

    def attach_on_connected(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after status socket connected.

        Parameters
        ----------
        func
            Function to be executed when status socket is connected.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_connected = func
        self.__on_connected_args = args

    def attach_on_status_socket_disconnected(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after status socket disconnected.

        Parameters
        ----------
        func
            Function to be executed when status socket is disconnected.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_status_socket_disconnected = func
        self.__on_status_socket_disconnected_args = args

    def attach_on_status_socket_reconnected(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after status socket reconnected.

        Parameters
        ----------
        func
            Function to be executed when status socket is reconnected.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_status_socket_reconnected = func
        self.__on_status_socket_reconnected_args = args

    def attach_on_line_status_changed(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after line status changed.

        Parameters
        ----------
        func
            Function to be executed when line status changed.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_line_status_changed = func
        self.__on_line_status_changed_args = args

    def attach_on_alarm_status_changed(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after alarm status changed.

        Parameters
        ----------
        func
            Function to be executed when alarm status changed.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_alarm_status_changed = func
        self.__on_alarm_status_changed_args = args

    def attach_on_decoder_audio_mode_changed(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after decoder audio mode changed.

        Parameters
        ----------
        func
            Function to be executed when decoder audio mode changed.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_decoder_audio_mode_changed = func
        self.__on_decoder_audio_mode_changed_args = args

    def attach_on_encoder_audio_mode_changed(self, func, *args) -> None:
        """
        Method to attach function, which will be executed after encoder audio mode changed.

        Parameters
        ----------
        func
            Function to be executed when encoder audio mode changed.
        args
            Function arguments.

        Returns
        -------
        None
        """

        self.__on_encoder_audio_mode_changed = func
        self.__on_encoder_audio_mode_changed_args = args

    def send_command(self, command: ProntonetCommand):
        """
        Sends command to command protocol socket.

        Parameters
        ----------
        command : ProntonetCommand
            Dataclass which contains command for Prontonet device (bytes),
            struct.unpack() pattern for response and command response type.

        Returns
        -------
        Structure passed to function as third argument of ProntonetCommand object.
        """

        self.__command_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__command_socket.connect((self.ip, self.port))
        self.__command_socket.send(ProntonetProtocol.connect())
        self.__command_socket.recv(1024)
        self.__command_socket.send(command.command)
        data = self.__command_socket.recv(2048)
        self.__command_socket.close()
        pattern = command.unpack_pattern
        if '#' in pattern:
            return command.response_type(data[8:-1])
        else:
            val = struct.unpack(pattern, data)
            return command.response_type(*val[2:])
