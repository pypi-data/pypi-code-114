from pathlib import Path
from typing import Any, Dict, Iterable

import pyarrow as pa

from .type import (
    BOOLEAN,
    LOCAL_DATE,
    LOCAL_DATE_TIME,
    NULLABLE_DOUBLE,
    NULLABLE_DOUBLE_ARRAY,
    NULLABLE_FLOAT,
    NULLABLE_FLOAT_ARRAY,
    NULLABLE_INT,
    NULLABLE_INT_ARRAY,
    NULLABLE_LONG,
    NULLABLE_LONG_ARRAY,
    STRING,
    DataType,
)

_ARROW_TYPES = {
    pa.bool_(): BOOLEAN,
    pa.float64(): NULLABLE_DOUBLE,
    pa.float32(): NULLABLE_FLOAT,
    pa.int64(): NULLABLE_LONG,
    pa.int32(): NULLABLE_INT,
    pa.list_(pa.float64()): NULLABLE_DOUBLE_ARRAY,
    pa.list_(pa.float32()): NULLABLE_FLOAT_ARRAY,
    pa.list_(pa.int64()): NULLABLE_LONG_ARRAY,
    pa.list_(pa.int32()): NULLABLE_INT_ARRAY,
    pa.string(): STRING,
    pa.date32(): LOCAL_DATE,
    pa.timestamp("s"): LOCAL_DATE_TIME,
    pa.timestamp("ns"): LOCAL_DATE_TIME,
}

DEFAULT_MAX_CHUNKSIZE = 1_000


def write_arrow_to_file(
    table: pa.Table,  # type: ignore
    *,
    max_chunksize: int = DEFAULT_MAX_CHUNKSIZE,
    filepath: Path,
) -> None:
    with pa.ipc.new_file(filepath, table.schema) as writer:
        for batch in table.to_batches(max_chunksize=max_chunksize):
            writer.write(batch)


def get_data_types_from_arrow(
    table: pa.Table,  # type: ignore
    *,
    keys: Iterable[str],
) -> Dict[str, DataType]:
    arrow_types = table.schema.types
    return {
        table.column_names[i]: DataType(
            java_type=_ARROW_TYPES[arrow_type].java_type,
            nullable=_ARROW_TYPES[arrow_type].nullable
            and (table.column_names[i] not in keys),
        )
        for i, arrow_type in enumerate(arrow_types)
    }


def get_corresponding_arrow_type(data_type: DataType) -> Any:
    return next(
        arrow_type
        for arrow_type, arrow_data_type in _ARROW_TYPES.items()
        if arrow_data_type.java_type == data_type.java_type
    )
