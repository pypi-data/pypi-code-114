from typing import Any, Iterable

import pandas as pd

from .java_type import JavaType, is_date_type, is_numeric_type, is_time_type


def convert_to_pandas(values: Iterable[Any], *, java_type: JavaType) -> Any:
    """Convert the passed *values* to a container that can be used as a column of type *java_type* in a pandas DataFrame."""
    values_container = values if isinstance(values, list) else list(values)
    if "N/A" in values_container:
        # To avoid breaking changes values containing N/A are left untouched.
        # An alternative leading to better types than `object` would be to replace `"N/A"` with `None`.
        return values

    if is_numeric_type(java_type):
        return pd.to_numeric(values)

    if is_date_type(java_type):
        if java_type == "ZonedDateTime":
            values = [
                None
                if zoned_date_time is None
                else str(zoned_date_time).split("[", maxsplit=1)[0]
                for zoned_date_time in values
            ]

        return pd.to_datetime(values)

    if is_time_type(java_type):
        return pd.to_timedelta(values)

    return values
