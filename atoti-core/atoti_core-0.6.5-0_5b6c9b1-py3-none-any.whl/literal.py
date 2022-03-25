from enum import Enum
from typing import Any, Literal, Optional, Set, Tuple, Type, Union, get_args

# From https://www.python.org/dev/peps/pep-0586/#legal-parameters-for-literal-at-type-check-time
_LiteralArg = Optional[Union[bool, bytes, Enum, int, str]]
"""Type of a value that can be used as :class:`typing.Literal` args."""

LITERAL_ARG_TYPES: Tuple[Type[_LiteralArg], ...] = (
    bool,
    bytes,
    Enum,
    int,
    type(None),
    str,
)
"""Instances of these types can be used as :class:`typing.Literal` args."""


# Inspired from https://github.com/agronholm/typeguard/blob/de6ab051309ba74a0a27840f8172697c8778ae4f/src/typeguard/__init__.py#L625-L642.
def get_literal_args(any_type: Any) -> Set[_LiteralArg]:
    """Extract all the top-level :class:`typing.Literal` args from the passed type.

    *any_type* cannot be an unresolved type, use :func:`typing.get_type_hints` to handle `postponed evaluation of annotations <https://www.python.org/dev/peps/pep-0563/>`__.
    """
    if getattr(any_type, "__origin__", None) not in {
        Literal,
        Union,
    }:
        # Ignore nested types.
        return set()

    literal_args: Set[_LiteralArg] = set()

    for arg in get_args(any_type):
        if getattr(arg, "__origin__", None) is Literal:
            literal_args.update(get_literal_args(arg))
        elif isinstance(arg, LITERAL_ARG_TYPES):
            literal_args.add(arg)

    return literal_args
