from typing import Optional

from stx.memory_map import MemoryMap


class PlateHandler:
    __memory_map: MemoryMap

    def __init__(self, memory_map: MemoryMap) -> None:
        self.__memory_map = memory_map

    @property
    def transfer_station_occupied(self) -> bool:
        """True if the transfer station is occupied, False otherwise"""
        return self.__memory_map.bits[1813]

    @property
    def handler_occupied(self) -> bool:
        """True if the plate handler shovel is occupied, False otherwise"""
        return self.__memory_map.bits[1812]

    def rotate_to_stacker(self, stacker: int) -> None:
        """
        Rotate the carrousel to the given stacker

        Parameters
        ----------
        stacker
            The stacker number
        """
        self.__memory_map.data[0] = stacker

    def set_current_slot(self, slot: int) -> None:
        """
        Set the current slot

        Parameters
        ----------
        slot
            The slot number
        """
        self.__memory_map.data[5] = slot

    def move_plate_from_transfer_station_to_slot(self, stacker: int, slot: int) -> None:
        """
        Move a plate from the transfer station to the given slot

        Parameters
        ----------
        stacker
            The stacker number
        slot
            The slot number
        """
        self.__move_plate(stacker, slot, 1904)

    def move_plate_from_slot_to_transfer_station(self, stacker: int, slot: int) -> None:
        """
        Move a plate from the given slot to the transfer station

        Parameters
        ----------
        stacker
            The stacker number
        slot
            The slot number
        """
        self.__move_plate(stacker, slot, 1905)

    def move_plate_from_handler_to_transfer_station(self) -> None:
        """Move a plate from the plate handler shovel to the transfer station"""
        self.__move_plate(None, None, 1906)

    def move_plate_from_transfer_station_to_handler(self) -> None:
        """Move a plate from the transfer station to the plate handler shovel"""
        self.__move_plate(None, None, 1907)

    def move_plate_from_slot_to_handler(self, stacker: int, slot: int) -> None:
        """
        Move a plate from the given slot to the plate handler shovel

        Parameters
        ----------
        stacker
            The stacker number
        slot
            The slot number
        """
        self.__move_plate(stacker, slot, 1908)

    def move_plate_from_handler_to_slot(self, stacker: int, slot: int) -> None:
        """
        Move a plate from the plate handler shovel to the given slot

        Parameters
        ----------
        stacker
            The stacker number
        slot
            The slot number
        """
        self.__move_plate(stacker, slot, 1909)

    def __move_plate(self, stacker: Optional[int], slot: Optional[int], action_bit: int):
        """Helper method for plate movement"""
        # if not specified, use current stacker and slot. Undefined (0) after initialization -> set to 1
        if stacker is None:
            stacker = self.__memory_map.data[0]
            if stacker == 0:
                stacker = 1
        if slot is None:
            slot = self.__memory_map.data[5]
            if slot == 0:
                slot = 1

        self.rotate_to_stacker(stacker)
        self.set_current_slot(slot)
        self.__memory_map.bits[action_bit] = True
