from __future__ import annotations

from typing import Any
from typing_extensions import TypedDict

from recordclass import RecordClass


class TransmuteData(TypedDict):
    data: dict[str, Any]
    schema: dict[str, Any]


class Field(RecordClass):
    field_name: str
    value: Any
    type: str
