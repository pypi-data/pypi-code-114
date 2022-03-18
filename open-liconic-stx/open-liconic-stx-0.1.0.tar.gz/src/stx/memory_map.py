from __future__ import annotations

from stx.serial_port import SerialPort


class MemoryMap:
    """
    Interface to the bit and data registers

    Examples
    --------
    >>> memory_map = MemoryMap(SerialPort("COM3"))

    >>> memory_map.bits[1915]  # read bit 1915 (ready)
    True
    >>> memory_map.bits[1801] = True  # set bit 1801 (initialize)

    >>> memory_map.data[982]  # read data DM982 (actual temperature in 0.1 °C)
    373
    >>> memory_map.data[890] = 400  # set data DM890 (target temperature in 0.1 °C)
    """

    bits: BitMemoryMap
    data: DataMemoryMap

    def __init__(self, serial_port: SerialPort):
        self.bits = BitMemoryMap(serial_port)
        self.data = DataMemoryMap(serial_port)


class DataMemoryMap:
    """Interface to the data memory"""

    __serial_port: SerialPort

    def __init__(self, serial_port: SerialPort):
        self.__serial_port = serial_port

    def __getitem__(self, address: int) -> int:
        return self.__serial_port.read_data(address)

    def __setitem__(self, address: int, value: int):
        self.__serial_port.send_and_expect_ok(f"WR DM{address} {value}")


class BitMemoryMap:
    """Interface to the bits"""

    __serial_port: SerialPort

    def __init__(self, serial_port: SerialPort):
        self.__serial_port = serial_port

    def __getitem__(self, address: int) -> bool:
        return self.__serial_port.read_bit(address)

    def __setitem__(self, address: int, value: bool):
        operator = "ST" if value else "RS"
        self.__serial_port.send_and_expect_ok(f"{operator} {address}")
