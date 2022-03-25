from dataclasses import dataclass
from typing import Any, Optional, Sequence

from atoti_core import keyword_only_dataclass

from .order import CustomOrder, NaturalOrder, Order


@keyword_only_dataclass
@dataclass(frozen=True)
class Comparator:
    """
    Warning:

        Deprecated, use :class:`atoti.Order` instead.
    """

    _name: str
    _first_members: Optional[Sequence[Any]]


ASCENDING = Comparator(_name=NaturalOrder()._key, _first_members=None)

DESCENDING = Comparator(_name=NaturalOrder(ascending=False)._key, _first_members=None)


def first_members(*members: Any) -> Comparator:
    """
    Warning:

        Deprecated, use :class:`atoti.CustomOrder` instead.
    """

    return Comparator(
        _name=CustomOrder(first_elements=())._key, _first_members=list(members)
    )


def _comparator_to_order(comparator: Comparator) -> Order:  # type: ignore
    if comparator._name == CustomOrder(first_elements=())._key:
        if comparator._first_members is None:
            raise ValueError("Missing members in `first_members()` comparator.")
        return CustomOrder(first_elements=comparator._first_members)
    return NaturalOrder(ascending=comparator._name == NaturalOrder()._key)


def _order_to_comparator(order: Order) -> Comparator:  # type: ignore
    if isinstance(order, CustomOrder):
        return first_members(order.first_elements)

    return (
        ASCENDING if isinstance(order, NaturalOrder) and order.ascending else DESCENDING
    )
