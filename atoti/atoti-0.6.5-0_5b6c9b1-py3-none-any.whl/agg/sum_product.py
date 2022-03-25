from __future__ import annotations

from typing import List, Optional, Union

from atoti_core import doc

from .._measures.sum_product_measure import (
    SumProductEncapsulationMeasure,
    SumProductFieldsMeasure,
)
from .._operation import Operation
from ..column import Column
from ..measure_description import MeasureDescription
from ..scope import Scope
from ._agg import agg
from ._utils import SCOPE_DOC, ColumnOrOperation, MeasureOrMeasureConvertible


def _get_factor_as_measure(
    factor: Union[ColumnOrOperation, MeasureOrMeasureConvertible]
) -> MeasureDescription:
    if isinstance(factor, MeasureDescription):
        return factor
    if isinstance(factor, (Column, Operation)):
        raise ValueError(
            "Cannot perform a sum_product aggregation on a combination of measures and table columns or operations. Convert all the factors to measures."
        )
    return factor._to_measure_description()


@doc(scope=SCOPE_DOC)
def sum_product(
    *factors: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return a measure equal to the sum product aggregation of the passed factors across the specified scope.

    Args:
        factors: Column, Measure or Level to do the sum product of.
        {scope}

    Example:

        >>> from datetime import date
        >>> df = pd.DataFrame(
        ...     columns=["Date", "Category", "Price", "Quantity", "Array"],
        ...     data=[
        ...         (date(2020, 1, 1), "TV", 300.0, 5, [10.0, 15.0]),
        ...         (date(2020, 1, 2), "TV", 200.0, 1, [5.0, 15.0]),
        ...         (date(2020, 1, 1), "Computer", 900.0, 2, [2.0, 3.0]),
        ...         (date(2020, 1, 2), "Computer", 800.0, 3, [10.0, 20.0]),
        ...         (date(2020, 1, 1), "TV", 500.0, 2, [3.0, 10.0]),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df,
        ...     table_name="Date",
        ... )
        >>> table.head()
                Date  Category  Price  Quantity         Array
        0 2020-01-01        TV  300.0         5  [10.0, 15.0]
        1 2020-01-02        TV  200.0         1   [5.0, 15.0]
        2 2020-01-01  Computer  900.0         2    [2.0, 3.0]
        3 2020-01-02  Computer  800.0         3  [10.0, 20.0]
        4 2020-01-01        TV  500.0         2   [3.0, 10.0]
        >>> cube = session.create_cube(table)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> m["turnover"] = tt.agg.sum_product(table["Price"], table["Quantity"])
        >>> cube.query(m["turnover"], levels=[l["Category"]])
                  turnover
        Category
        Computer  4,200.00
        TV        2,700.00
        >>> m["array sum product"] = tt.agg.sum_product(table["Price"], table["Array"])
        >>> cube.query(m["array sum product"])
                       array sum product
        0  doubleVector[2]{{15300.0, ...}}
    """
    if len(factors) < 1:
        raise ValueError("At least one factor is needed")
    # pyright does not know there is only columns in factors so we build a new sequence.
    factors_column: List[Column] = []
    for factor in factors:
        if isinstance(factor, Column):
            factors_column.append(factor)
    # Case with table fields
    if len(factors_column) == len(factors):
        if scope is None:
            return SumProductFieldsMeasure(factors_column)
        raise ValueError(
            "Scope is defined for table columns aggregation. "
            + "Scope must not be defined since this aggregation will be done at fact level."
        )
    # Otherwise case with two measures.
    return agg(
        "SUM_PRODUCT",
        SumProductEncapsulationMeasure(
            [_get_factor_as_measure(factor) for factor in factors]
        ),
        scope=scope,
    )
