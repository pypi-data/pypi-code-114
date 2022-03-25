"""Helper functions for converting operations into Java code."""
from typing import Callable, Mapping, Optional

from atoti_core import JavaType, is_numeric_array_type, is_numeric_type

from ...column import Column

_BUFFER_WRITE_TEMPLATE = "{buffer_code}.{writer_code}(0, {value_code});"


_READERS: Mapping[JavaType, Callable[[int], str]] = {
    "boolean": lambda index: f"fact.readBoolean({index})",
    "int": lambda index: f"fact.readInt({index})",
    "long": lambda index: f"fact.readLong({index})",
    "float": lambda index: f"fact.readFloat({index})",
    "double": lambda index: f"fact.readDouble({index})",
}


def get_column_reader_code(column: Column, index: int) -> str:
    def _default(i: int) -> str:
        if is_numeric_array_type(column.data_type.java_type):
            return f"(fact.isNull({i}) ? null : fact.readVector({i}).cloneOnHeap())"
        raise TypeError("Unsupported column type: " + column.data_type.java_type)

    return _READERS.get(column.data_type.java_type, _default)(index)


def _ensure_java_numeric_scalar_output_type(output_type: JavaType) -> None:
    if not is_numeric_type(output_type):
        raise TypeError("Unsupported output type: " + output_type)


def get_buffer_read_code(*, buffer_code: str, output_type: JavaType) -> str:
    _ensure_java_numeric_scalar_output_type(output_type)

    method_name = f"read{output_type.capitalize()}"
    return f"{buffer_code}.{method_name}(0)"


def get_buffer_add_code(
    *, buffer_code: str, value_code: str, output_type: JavaType
) -> str:
    _ensure_java_numeric_scalar_output_type(output_type)
    writer_code = f"add{output_type.capitalize()}"
    return _BUFFER_WRITE_TEMPLATE.format(
        buffer_code=buffer_code, writer_code=writer_code, value_code=value_code
    )


def get_buffer_write_code(
    *, buffer_code: str, value_code: str, output_type: Optional[JavaType]
) -> str:
    if output_type is None:
        return _BUFFER_WRITE_TEMPLATE.format(
            buffer_code=buffer_code, writer_code="write", value_code=value_code
        )

    _ensure_java_numeric_scalar_output_type(output_type)

    writer_code = f"write{output_type.capitalize()}"
    return _BUFFER_WRITE_TEMPLATE.format(
        buffer_code=buffer_code, writer_code=writer_code, value_code=value_code
    )


_TERMINATE_CODE: Mapping[JavaType, Callable[[str], str]] = {
    "double": lambda value_code: f"Double.valueOf({value_code})",
    "float": lambda value_code: f"Float.valueOf({value_code})",
    "long": lambda value_code: f"Long.valueOf({value_code})",
    "int": lambda value_code: f"Integer.valueOf({value_code})",
}


def get_terminate_code(output_type: JavaType, value_code: str) -> str:
    def _raise(_: str) -> str:
        raise TypeError("Unsupported output type: " + output_type)

    return _TERMINATE_CODE.get(output_type, _raise)(value_code)
