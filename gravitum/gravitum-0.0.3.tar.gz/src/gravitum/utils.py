from .types import Int8, Int16, Int32, Int64, \
    UInt8, UInt16, UInt32, UInt64, IntType
from .virtualpointer import VirtualPointer


def get_type(size: int, signed: bool) -> IntType:
    """Get type int with specified size and signed."""
    if size == 1:
        return Int8 if signed else UInt8
    elif size == 2:
        return Int16 if signed else UInt16
    elif size == 4:
        return Int32 if signed else UInt32
    elif size == 8:
        return Int64 if signed else UInt64
    raise NotImplementedError()


def ptr(source: bytearray, data_type: IntType = UInt8) -> VirtualPointer:
    """Create virtual pointer."""
    return VirtualPointer(source=source, data_type=data_type)
