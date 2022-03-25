from atoti_core import parse_java_type

from .type import DataType


def parse_data_type(value: str) -> DataType:
    parts = value.split("nullable ")
    return DataType(
        java_type=parse_java_type(parts[-1]),
        nullable=len(parts) > 1,
    )
