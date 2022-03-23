import sys

from pyvisa import ResourceManager


class TunicsLaser:
    device_adr = None
    adr = None
    static_adr = "GPIB0::10::INSTR"

    def __init__(self, adr=None, DEBUG_LOGGING=True):
        self.adr = adr if adr is not None else self.static_adr  # use given address or static
        self.DEBUG_LOGGING = DEBUG_LOGGING
        self.__setup_visa_rm()
        self.__take_instr_from_rm()
        self.__set_instrument()

    def __setup_visa_rm(self):
        try:
            self.rm = ResourceManager()
        except sys.exc_info() as e:
            raise e

    def __take_instr_from_rm(self):
        if self.adr in self.rm.list_resources():
            self.device_adr = self.adr
        else:
            raise Exception("No instrument found")

    def __set_instrument(self):
        try:
            self.instr = self.rm.open_resource(self.device_adr)
        except sys.exc_info() as e:
            raise e

    def send_command(self,
                     command: str) -> str:
        """
        send command manually to the device
        :param command: String command (look manual)
        :return: response from device
        """
        return self.instr.query(command)

    def set_wavelength(self,
                       wl: float,
                       internal_logging=False) -> None:
        wl_f = f"{wl:8.3f}".replace(" ", "0")
        cmd = f"L={wl_f}\n"
        response = self.send_command(cmd)
        if self.DEBUG_LOGGING:
            print(f"Wavelength set to {wl_f} [nm]")
        if internal_logging:
            print(f"response: '{response}'")

    def get_wavelength(self) -> str:
        """
        Request the present wavelength value.
        :return: -> "L=nnnn.nnn" (in nm)
        """
        return self.send_command("L?\n")

    def set_power(self,
                  power: float,
                  internal_logging=False) -> None:
        pow_f = f"{power:5.2f}".replace(" ", "0")
        cmd = f"P={pow_f}\n"
        response = self.send_command(cmd)
        if self.DEBUG_LOGGING:
            print(f"Power set to {pow_f} [mW] or [dBm]")
        if internal_logging:
            print(f"response: '{response}'")

    def get_power(self) -> str:
        """
        Request the present power output level.
        :return: -> "P=nn.nn" (in mW) or "±nn.nn" (in dBm) or "disabled" if Enable mod is not active
        """
        return self.send_command("P?\n")

    def set_current(self,
                    current: float,
                    internal_logging=False) -> None:
        cur_f = f"{current:4.1f}".replace(" ", "0")
        cmd = f"I={cur_f}\n"
        response = self.send_command(cmd)
        if self.DEBUG_LOGGING:
            print(f"Power set to {cur_f} [mA]")
        if internal_logging:
            print(f"response: '{response}'")

    def get_current(self) -> str:
        """
        Request the present laser diode current level.
        :return: -> "I=nn.n" (in mA) or "disabled" if the Enable mode is not active.
        """
        return self.send_command("I?\n")

    def set_opt_freq(self,
                     freq: float,
                     internal_logging=False) -> None:
        freq_f = f"{freq:8.1f}".replace(" ", "0")
        cmd = f"I={freq_f}\n"
        response = self.send_command(cmd)
        if self.DEBUG_LOGGING:
            print(f"Power set to {freq_f} [GHz]")
        if internal_logging:
            print(f"response: '{response}'")

    def get_opt_freq(self) -> str:
        """
        Request the present optical frequency value.
        :return: -> "f=nnnnnn.n" (in GHz)
        """
        return self.send_command("f?\n")

    def enable(self,
               internal_logging=False) -> str:
        """
        Enable laser.
        :return: -> "0"
        """
        cmd = "ENABLE\n"
        response = self.send_command(cmd)
        if self.DEBUG_LOGGING:
            print(f"Laser ENABLED")
        if internal_logging:
            print(f"response: '{response}'")
        return response

    def disable(self,
                internal_logging=False) -> str:
        """
        Disable laser.
        :return: -> "0"
        """
        cmd = "DISABLE\n"
        response = self.send_command(cmd)
        if self.DEBUG_LOGGING:
            print(f"Laser DISABLED")
        if internal_logging:
            print(f"response: '{response}'")
        return response


if __name__ == "__main__":
    pass
