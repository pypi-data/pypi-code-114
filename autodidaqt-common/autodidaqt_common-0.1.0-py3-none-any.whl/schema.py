from typing import List, Optional

import warnings
from dataclasses import dataclass, make_dataclass

import numpy as np

__all__ = (
    "ObjectType",
    "ArrayType",
    "default_value_for_schema",
)


class LogicalAxisSchema:
    @classmethod
    def for_subaxis(cls, subaxis_name: str):
        return make_dataclass(f"{cls.__name__}_Subaxis_{subaxis_name}", [])


def make_logical_axis_schema(name):
    warnings.warn(f"Generating phony logical axis schema LogicalAxis{name}")

    return make_dataclass(f"LogicalAxis_{name}", [], bases=(LogicalAxisSchema,))


@dataclass
class ObjectType:
    """
    Indicates that an axis produces objects.

    In general there's not much autodidaqt can do here since it cannot reduce objects
    unless they implement __add__.
    """

    def default_value(self):
        return None


@dataclass
class ArrayType:
    """
    Indicates that an axis produces ndarrays

    If the shape is provided, then this will be the shape of the arrays produced.
    A `None` value here indicates that we don't know ahead of time how big they
    will be.

    The `dtype` member indicates the type of the array values
    """

    shape: Optional[List[int]] = None
    dtype: type = float

    @classmethod
    def of(cls, dtype):
        return ArrayType(None, dtype)

    def default_value(self):
        if self.shape is None:
            return None

        return np.zeros(dtype=self.dtype, shape=self.shape)


DEFAULT_VALUES = {
    int: 0,
    float: 0,
    str: "",
}


def default_value_for_schema(schema):
    try:
        return schema.default_value()
    except AttributeError:
        return DEFAULT_VALUES[schema]
