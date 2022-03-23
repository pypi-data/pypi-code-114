from functools import wraps
from typing import Union, Type, SupportsBytes, Iterable

import numpy as np


class IntMeta(type):
    """Meta class of type int.

    Reprocess type conversion.
    """

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)

        operations = [
            '__neg__', '__pos__', '__invert__',
            '__add__', '__radd__', '__iadd__',
            '__sub__', '__rsub__', '__isub__',
            '__mul__', '__rmul__', '__imul__',
            '__truediv__', '__rtruediv__', '__itruediv__',
            '__floordiv__', '__rfloordiv__', '__ifloordiv__',
            '__mod__', '__rmod__', '__imod__',
            '__and__', '__rand__', '__iand__',
            '__or__', '__ror__', '__ior__',
            '__xor__', '__rxor__', '__ixor__',
            '__lshift__', '__rlshift__', '__ilshift__',
            '__rshift__', '__rrshift__', '__irshift__'
        ]

        for operation in operations:
            if not hasattr(cls, operation):
                continue

            func = getattr(cls, operation)
            setattr(cls, operation, cls.operate_wrapper(func))

    @staticmethod
    def operate_wrapper(f):
        """Wrap operation method for type conversion.

        If unary operation, the result is still the own type.
        If the operand is basic int, it will be converted to the own type.
        If the type of operand is inconsistent with the own type,
        they will be converted to large size or unsigned type.
        """

        @wraps(f)
        def decorator(self, *args):
            data_type = type(self)

            if args:
                other = args[0]

                if isinstance(other, int):
                    other = data_type(other)

                elif isinstance(self, np.integer):
                    if self.itemsize == other.itemsize:
                        data_type = type(other) \
                            if isinstance(self, np.signedinteger) \
                            else type(self)

                    else:
                        data_type = type(other) \
                            if self.itemsize < other.itemsize \
                            else type(self)

                return data_type(f(self, other))

            return data_type(f(self))

        return decorator


class IntMixin(np.integer):
    """Mixin class of type int."""

    @classmethod
    def get_size(cls) -> int:
        """Get size (bytes) of the type."""
        if issubclass(cls, np.int8) or issubclass(cls, np.uint8):
            return 1
        elif issubclass(cls, np.int16) or issubclass(cls, np.uint16):
            return 2
        elif issubclass(cls, np.int32) or issubclass(cls, np.uint32):
            return 4
        elif issubclass(cls, np.int64) or issubclass(cls, np.uint64):
            return 8
        raise NotImplementedError()

    @classmethod
    def get_signed(cls) -> bool:
        """Get signed of the type."""
        return issubclass(cls, np.signedinteger)

    @classmethod
    def from_bytes(
            cls,
            data: Union[Iterable[int], SupportsBytes],
            byteorder: str = 'little'
    ):
        """Return a value of the type from given bytes"""
        return cls(int.from_bytes(
            data,
            byteorder=byteorder,
            signed=cls.get_signed()
        ))

    def to_bytes(self, byteorder: str = 'little') -> bytes:
        """Covert this value to bytes."""
        return int(self).to_bytes(
            length=self.get_size(),
            byteorder=byteorder,
            signed=self.get_signed()
        )


class Int8(np.int8, IntMixin, metaclass=IntMeta):
    """Int8"""


class Int16(np.int16, IntMixin, metaclass=IntMeta):
    """Int16"""


class Int32(np.int32, IntMixin, metaclass=IntMeta):
    """Int32"""


class Int64(np.int64, IntMixin, metaclass=IntMeta):
    """Int64"""


class UInt8(np.uint8, IntMixin, metaclass=IntMeta):
    """UInt8"""


class UInt16(np.uint16, IntMixin, metaclass=IntMeta):
    """UInt16"""


class UInt32(np.uint32, IntMixin, metaclass=IntMeta):
    """UInt32"""


class UInt64(np.uint64, IntMixin, metaclass=IntMeta):
    """UInt64"""


IntVar = Union[
    Int8, Int16, Int32, Int64,
    UInt8, UInt16, UInt32, UInt64
]

IntType = Type[Union[
    Int8, Int16, Int32, Int64,
    UInt8, UInt16, UInt32, UInt64
]]

int8 = Int8
int16 = Int16
int32 = Int32
int64 = Int64

uint8 = UInt8
uint16 = UInt16
uint32 = UInt32
uint64 = UInt64
