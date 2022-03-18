from stx.memory_map import MemoryMap


class ShakerController:
    __memory_map: MemoryMap

    def __init__(self, memory_map: MemoryMap) -> None:
        self.__memory_map = memory_map

    @property
    def shaker_is_active(self) -> bool:
        """True if the shaker is active, False otherwise"""
        return self.__memory_map.bits[1913]

    def activate_shaker(self) -> None:
        """Activate the shaker"""
        self.__memory_map.bits[1913] = True

    def stop_shaker(self) -> None:
        """Stop the shaker"""
        self.__memory_map.bits[1913] = False

    @property
    def shaker_speed(self) -> int:
        """The shaker speed, between 1 and 50 (can be set)"""
        return self.__memory_map.data[39]

    @shaker_speed.setter
    def shaker_speed(self, speed: int) -> None:
        self.__memory_map.data[39] = speed
