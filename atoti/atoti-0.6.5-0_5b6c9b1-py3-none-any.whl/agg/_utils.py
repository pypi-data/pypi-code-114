from __future__ import annotations

from typing import Union

from .._operation import Operation
from ..column import Column
from ..measure_description import MeasureConvertible, MeasureDescription

MeasureOrMeasureConvertible = Union[MeasureDescription, MeasureConvertible]
ColumnOrOperation = Union[Column, Operation]


BASIC_DOC = """Return a measure equal to the {value} of the passed measure across the specified scope.

    {args}

    Example:

        >>> df = pd.DataFrame(
        ...     columns=["id", "Quantity", "Price", "Other"],
        ...     data=[
        ...         ("a1", 100, 12.5, 1),
        ...         ("a2", 10, 43, 2),
        ...         ("a3", 1000, 25.9, 2),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df,
        ...     table_name="Product",
        ...     keys=["id"],
        ... )
        >>> table.head()
            Quantity  Price  Other
        id
        a1       100   12.5      1
        a2        10   43.0      2
        a3      1000   25.9      2
        >>> cube = session.create_cube(table)
        >>> m = cube.measures
{example}

    .. doctest::
        :hide:

        >>> session._clear()
"""

SCOPE_DOC = """
        scope: The scope of the aggregation.
               When ``None`` is specified, the natural aggregation scope is used: it contains all the data in the cube which coordinates match the ones of the currently evaluated member.
    """

BASIC_ARGS_DOC = (
    """
    Args:
        operand: The measure or table column to aggregate.
"""
    + SCOPE_DOC
)

EXTREMUM_MEMBER_DOC = """Return a measure equal to the member {op}imizing the passed measure on the given level.

    When multiple members {op}imize the passed measure, the first one
    (according to the order of the given level) is returned.

    Args:
        measure: The measure to {op}imize.
        level: The level on which the {op}imizing member is searched for.

    Example:

        >>> df = pd.DataFrame(
        ...     columns=["Continent", "City", "Price"],
        ...     data=[
        ...         ("Europe", "Paris", 200.0),
        ...         ("Europe", "Berlin", 150.0),
        ...         ("Europe", "London", 240.0),
        ...         ("North America", "New York", 270.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df,
        ...     table_name="City price table",
        ... )
        >>> table.head()
               Continent      City  Price
        0         Europe     Paris  200.0
        1         Europe    Berlin  150.0
        2         Europe    London  240.0
        3  North America  New York  270.0
        >>> cube = session.create_cube(table, mode="manual")
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> h["Geography"] = [table["Continent"], table["City"]]
        >>> m["Price"] = tt.value(table["Price"])
{example}


        .. doctest::
            :hide:

            >>> session._clear()
"""

QUANTILE_STD_AND_VAR_DOC_KWARGS = {
    "what": "of the passed measure across the specified scope",
}
