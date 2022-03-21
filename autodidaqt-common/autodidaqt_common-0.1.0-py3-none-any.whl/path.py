from typing import Tuple, Union

import functools

__all__ = ["AxisPath", "AccessRecorder"]


def safely_unwrap_int(value: Union[int, str]) -> Union[int, str]:
    try:
        return int(value)
    except ValueError:
        return str(value)


class AccessRecorder:
    def __init__(self, scope=None):
        self.path = []
        self.scope = scope

    def __getattr__(self, item):
        self.path.append(item)
        return self

    def __getitem__(self, item):
        self.path.append(item)
        return self

    def name_(self):
        return ".".join(map(str, self.full_path_()))

    def full_path_(self):
        return tuple(([] if self.scope is None else [self.scope]) + self.path)


class AxisPath:
    """Represents the path to an axis in the state tree.

    We need these in a few different representations throughout.
    These representations are:

    Natural String:
        These look like source code lifted from Python, but with quotes
        for instance:

        >>> natural_string_path = "instrument.axis.subaxis[0]"
        >>> as_tuple = AxisPath.to_tuple(natural_string_path)
        >>> assert as_tuple == ("instrument", "axis", "subaxis", 0)
        >>> assert AxisPath.to_natural_string(as_tuple) == natural_string_path


    Tokenized Strings:
        These are "machine readable" strings.

        >>> tokenized_string_path = "instrument.axis.subaxis.0"
        >>> as_tuple = AxisPath.to_tuple(tokenized_string_path)
        >>> assert as_tuple == ("instrument", "axis", "subaxis", 0)
        >>> assert AxisPath.to_tokenized_string(as_tuple) == tokenized_string_path

    Tuple Paths:
        These are the most programmatically and strongly typed variant,
        as such they are very convenient.

        >>> tuple_path = ("instrument", "axis", "subaxis", 0)
        >>> assert AxisPath.to_tuple("instrument.axis.subaxis.0") == tuple_path

        Note that the final element in this path is an integer!

    This class is a utility which provides conversion functionality between
    these different formats.
    """

    @staticmethod
    def to_natural_string(axis_path) -> str:
        tuple_path = AxisPath.to_tuple(axis_path)
        return ".".join([f"[{x}]" if isinstance(x, int) else x for x in tuple_path]).replace(
            ".[", "["
        )

    @staticmethod
    def to_tokenized_string(axis_path) -> str:
        tuple_path = AxisPath.to_tuple(axis_path)
        return ".".join(str(s) for s in tuple_path)

    @staticmethod
    def to_tuple(axis_path) -> Tuple:
        if isinstance(axis_path, str):
            return AxisPath.string_to_tuple(axis_path)
        if isinstance(axis_path, AccessRecorder):
            axis_path = axis_path.full_path_()

        return tuple(safely_unwrap_int(x) for x in axis_path)

    @staticmethod
    @functools.lru_cache(maxsize=512)
    def string_to_tuple(axis_path: str) -> Tuple:
        return tuple(
            safely_unwrap_int(x)
            for x in axis_path.replace("[", ".").replace("]", "").split(".")
            if x
        )
