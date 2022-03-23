"""Helping functions. Also functions from mypythontools copies to avoid collisions."""

import sys
from typeguard import typechecked


def typechecked_compatible(function):
    """Turns off type checking for old incompatible python versions.

    Mainly for new syntax like list[str] which raise TypeError.
    """

    # def decorator(func):
    #     if sys.version_info.minor < 9:
    #         return func
    #     return typechecked(func)

    if sys.version_info.minor < 9:
        return function
    return typechecked(function)
