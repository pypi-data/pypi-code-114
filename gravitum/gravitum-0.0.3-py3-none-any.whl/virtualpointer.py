from typing import List, SupportsInt, Union

from .exceptions import ExceedRangeError
from .types import IntType, IntVar


class VirtualPointer:
    """Provide virtual pointer operation on bytearray.

    :param source: The source bytearray.
    :param data_type: The type of data.
    :param byteorder: The byte order of source bytearray.
    :param offset: The offset from the start of source bytearray.
    """

    def __init__(
            self,
            source: bytearray,
            data_type: IntType,
            byteorder: str = 'little',
            offset: int = 0
    ):
        self.source = source
        self.data_type = data_type
        self.byteorder = byteorder
        self.offset = offset

    def __add__(self, other):
        """Support addition."""
        return self.add(int(other))

    def copy(self):
        """Copy object."""
        return self.__class__(
            source=self.source,
            data_type=self.data_type,
            byteorder=self.byteorder,
            offset=self.offset
        )

    def add(self, num: int):
        """Offset the pointer position."""
        obj = self.copy()
        obj.offset += num * self.data_type.get_size()
        return obj

    def cast(self, data_type: IntType):
        """Cast to the specified type."""
        obj = self.copy()
        obj.data_type = data_type
        return obj

    def read_bytes(self, size: int) -> bytes:
        """Read bytes from the source bytearray."""
        try:
            return bytes(self.source[self.offset:self.offset + size])
        except IndexError:
            raise ExceedRangeError()

    def write_bytes(self, data: Union[bytes, bytearray, List[SupportsInt]]):
        """Write bytes into the source bytearray."""
        try:
            for i, v in enumerate(data):
                self.source[self.offset + i] = v
        except IndexError:
            raise ExceedRangeError()

    def read(self) -> IntVar:
        """Read an integer from the source bytearray."""
        data = self.read_bytes(self.data_type.get_size())
        return self.data_type.from_bytes(data, byteorder=self.byteorder)

    def write(self, value: SupportsInt):
        """Write an integer into the source bytearray."""
        data = self.data_type(value).to_bytes(byteorder=self.byteorder)
        self.write_bytes(data)
