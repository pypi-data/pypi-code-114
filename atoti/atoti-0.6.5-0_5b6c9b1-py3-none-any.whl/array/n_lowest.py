from __future__ import annotations

from typing import Union

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription, _convert_to_measure_description
from ._utils import check_array_type, validate_n_argument


def n_lowest(
    measure: MeasureDescription, n: Union[int, MeasureDescription]
) -> MeasureDescription:
    """Return an array measure containing the *n* lowest elements of the passed array measure.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Bottom 3"] = tt.array.n_lowest(m["PnL.SUM"], n=3)
        >>> cube.query(m["PnL.SUM"], m["Bottom 3"])
                                  PnL.SUM                                  Bottom 3
        0  doubleVector[10]{-20.163, ...}  doubleVector[3]{-57.51499999999999, ...}

    """
    validate_n_argument(n)
    check_array_type(measure)
    return CalculatedMeasure(
        Operator("n_lowest", [measure, _convert_to_measure_description(n)])
    )
