from __future__ import annotations

from typing import Optional, Union

from atoti_core import coordinates_to_java_description

from .._measures.calculated_measure import AggregatedMeasure
from .._measures.generic_measure import GenericMeasure
from .._measures.table_measure import TableMeasure
from .._operation import Operation
from ..column import Column
from ..measure_description import MeasureDescription
from ..scope import Scope
from ..scope._utils import LeafLevels, Window
from ._utils import ColumnOrOperation, MeasureOrMeasureConvertible


def agg(
    agg_fun: str,
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return a measure aggregating the passed one.

    A scope can only be specified when passing an instance of MeasureDescription.
    """
    from .._udaf import UserDefinedAggregateFunction

    if isinstance(operand, Operation):
        udaf = UserDefinedAggregateFunction(operand, agg_fun)
        udaf.register_aggregation_function()
        return GenericMeasure(
            "ATOTI_UDAF_MEASURE",
            udaf.column_names,
            udaf.plugin_key,
            [
                coordinates_to_java_description(level_coordinates)
                for level_coordinates in (
                    scope._levels_coordinates if isinstance(scope, LeafLevels) else []
                )
            ],
            agg_fun,
        )
    if not isinstance(operand, MeasureDescription):
        if scope is not None:
            raise ValueError(
                (
                    """Illegal argument "scope" if you are not passing a measure object """
                    """as "measure" argument."""
                )
            )
        if isinstance(operand, Column):
            return TableMeasure(
                _column_name=operand.name,
                _agg_fun=agg_fun,
                _table_name=operand._table_name,
            )
        return operand._to_measure_description(agg_fun)

    if isinstance(scope, Window):
        return scope._create_aggregated_measure(operand, agg_fun)
    if isinstance(scope, LeafLevels) or scope is None:
        return AggregatedMeasure(
            _underlying_measure=operand, _agg_fun=agg_fun, _on_levels=scope
        )
    raise TypeError(f"Scope {scope} of invalid type {type(scope).__name__} passed")
