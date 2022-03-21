from typing import List, Type

import enum

__all__ = [
    "enum_option_names",
    "enum_mapping",
]


def _try_unwrap_value(v):
    try:
        return v.value
    except AttributeError:
        return v


def enum_option_names(enum_cls: Type[enum.Enum]) -> List[str]:
    names = [x for x in dir(enum_cls) if "__" not in x]
    values = [_try_unwrap_value(getattr(enum_cls, n)) for n in names]

    return [x[0] for x in sorted(zip(names, values), key=lambda x: x[1])]


def enum_mapping(enum_cls: Type[enum.Enum], invert=False):
    options = enum_option_names(enum_cls)
    d = dict([[o, _try_unwrap_value(getattr(enum_cls, o))] for o in options])
    if invert:
        d = {v: k for k, v in d.items()}
    return d
