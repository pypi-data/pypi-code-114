from pyvisa import ResourceManager
import sys


class TunicsLaser:
    device_adr = None
    adr = None
    static_adr = "GPIB0::10::INSTR"

    def __init__(self, adr=None):
        self.adr = adr if adr is not None else self.static_adr  # use given address or static
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

    def send_command(self, command: str) -> str:
        """
        send command manually to the device
        :param command: String command (look manual)
        :return:
        """
        return self.instr.query(command)

    def set_wavelength(self, wl: float):
        cmd = f"L={wl:8.3f}\n".replace(" ", "0")
        print(self.send_command(cmd))

    def get_wavelength(self) -> str:
        """
        Request the present wavelength value.
        :return: -> "L=nnnn.nnn" (in nm)
        """
        return self.send_command("L?\n")

    def set_power(self, power: float):
        cmd = f"P={power:5.2f}\n".replace(" ", "0")
        print(self.send_command(cmd))

    def get_power(self) -> str:
        """
        Request the present power output level.
        :return: -> "P=nn.nn" (in mW) or "±nn.nn" (in dBm) or "disabled" if Enable mod is not active
        """
        return self.send_command("P?\n")

    def set_current(self, current: float):
        cmd = f"I={current:4.1f}\n".replace(" ", "0")
        print(self.send_command(cmd))

    def get_current(self) -> str:
        """
        Request the present laser diode current level.
        :return: -> "I=nn.n" (in mA) or "disabled" if the Enable mode is not active.
        """
        return self.send_command("I?\n")

    def set_opt_freq(self, freq: float):
        cmd = f"I={freq:8.1f}\n".replace(" ", "0")
        print(self.send_command(cmd))

    def get_opt_freq(self) -> str:
        """
        Request the present optical frequency value.
        :return: -> "f=nnnnnn.n" (in GHz)
        """
        return self.send_command("f?\n")

    def enable(self):
        """
        Enable laser.
        :return: -> "0"
        """
        return self.send_command("ENABLE\n")

    def disable(self):
        """
        Disable laser.
        :return: -> "0"
        """
        return self.send_command("DISABLE\n")


if __name__ == "__main__":
    pass
