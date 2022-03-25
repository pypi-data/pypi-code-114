from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Sequence

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
# See https://github.com/python/mypy/issues/5374.
@dataclass(frozen=True)  # type: ignore[misc]
class Order(ABC):
    """Order."""

    @property
    @abstractmethod
    def _key(self) -> str:
        ...


@keyword_only_dataclass
@dataclass(frozen=True)
class NaturalOrder(Order):
    """Ascending or descending natural order.

    Example:
        >>> df = pd.DataFrame(
        ...     {
        ...         "Date": ["2021-05-19", "2021-05-20"],
        ...         "Product": ["TV", "Smartphone"],
        ...         "Quantity": [12, 18],
        ...     }
        ... )
        >>> table = session.read_pandas(df, table_name="Sales")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> l["Date"].order == tt.NaturalOrder()
        True
        >>> cube.query(m["Quantity.SUM"], levels=[l["Date"]])
                   Quantity.SUM
        Date
        2021-05-19           12
        2021-05-20           18
        >>> l["Date"].order = tt.NaturalOrder(ascending=False)
        >>> cube.query(m["Quantity.SUM"], levels=[l["Date"]])
                   Quantity.SUM
        Date
        2021-05-20           18
        2021-05-19           12

    """

    ascending: bool = True

    @property
    def _key(self) -> str:
        return "NaturalOrder" if self.ascending else "ReverseOrder"


@keyword_only_dataclass
@dataclass(frozen=True)
class CustomOrder(Order):
    """Custom order with the given first elements.

    Example:
        >>> df = pd.DataFrame(
        ...     {
        ...         "Product": ["TV", "Smartphone", "Computer", "Screen"],
        ...         "Quantity": [12, 18, 50, 68],
        ...     }
        ... )
        >>> table = session.read_pandas(df, table_name="Products")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> cube.query(m["Quantity.SUM"], levels=[l["Product"]])
                   Quantity.SUM
        Product
        Computer             50
        Screen               68
        Smartphone           18
        TV                   12
        >>> l["Product"].order = tt.CustomOrder(first_elements=["TV", "Screen"])
        >>> cube.query(m["Quantity.SUM"], levels=[l["Product"]])
                   Quantity.SUM
        Product
        TV                   12
        Screen               68
        Computer             50
        Smartphone           18

    """

    first_elements: Sequence[Any]

    @property
    def _key(self) -> str:
        return "Custom"
