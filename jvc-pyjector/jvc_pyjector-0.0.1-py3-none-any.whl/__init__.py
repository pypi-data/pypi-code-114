import socket
from .constants import Commands, Power, Handshake, Values
from time import sleep

class JVCProjector:
    def __init__(self, ip, port=20554, delay=5):
        self.ip = ip
        self.port = port
        self.ready = True
        self.on = False
        self.delay = delay

    def _send_command(self, payload):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))


        s.sendall(Handshake.request.value)

        response = s.recv(5)
        if (response != Handshake.ok.value):
            return None

        response = s.recv(5)
        if (response != Handshake.ack.value):
            return None

        # generate expected ack value
        expected_ack = bytearray(Values.prefix.value)
        expected_ack.extend(payload[3:5] + Values.suffix.value)
        expected_ack = bytes(expected_ack)

        s.sendall(payload)
            
        # check if ACK matches expected
        response = s.recv(6)
        if (response != expected_ack):
            return None

        # if we are using a reference command, get the return value
        if (chr(payload[0]) == '?'):
            response = s.recv(7)
        
        s.close()
        return response

    def status(self):
        # ask projector to send power status
        result = self._send_command(Commands.power_status.value)

        # projector is ready if it isn't currently powering on or off
        self.ready = (result != Power.powering_on.value and result != Power.powering_off.value)

        # projector is considered to be on if it is powered on or powering on
        self.on = (result == Power.powered_on.value or result == Power.powering_on.value)
        return Power(result).name

    def is_on(self):
        self.status()
        return self.on

    def is_ready(self):
        self.status()
        return self.ready

    def power_on(self):
        if (not self.is_on()):
            while (not self.is_ready()):
                sleep(self.delay)
            self._send_command(Commands.power_on.value)

    def power_off(self):
        if (self.is_on()):
            self._send_command(Commands.hide_off.value)
            while (not self.is_ready()):
                sleep(self.delay)
            self._send_command(Commands.power_off.value)

    def power_state(self):
        result = self._send_command(Commands.power_status.value)
        return Power(result).name

    def command(self, command_string):
        if hasattr(Commands, command_string):
            return self._send_command(Commands[command_string].value)
        return None

    def command_list(self):
        for command in Commands:
            print(command.name)
