from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional

from atoti_core import (
    BaseLevelCondition,
    ComparisonOperator,
    LevelCoordinates,
    keyword_only_dataclass,
)

from ._single_condition import SingleCondition
from .measure_description import MeasureDescription, _convert_to_measure_description


@keyword_only_dataclass
@dataclass(frozen=True)
class LevelCondition(SingleCondition, BaseLevelCondition):
    def _to_measure_description(
        self,
        agg_fun: Optional[str] = None,  # pylint: disable=unused-argument
    ) -> MeasureDescription:
        lvl_measure = _level_coordinates_to_measure_description(self.level_coordinates)

        # Handle comparing to None
        if self.value is None:
            if self.operator not in ["eq", "ne"]:
                raise ValueError(f"Cannot use operation {self.operator} on None.")

            from ._measures.boolean_measure import BooleanMeasure

            return BooleanMeasure(
                _operator="isNull" if self.operator == "eq" else "notNull",
                _operands=[lvl_measure],
            )

        value_measure = _convert_to_measure_description(self.value)
        switcher: Mapping[ComparisonOperator, MeasureDescription] = {
            "eq": lvl_measure == value_measure,
            "ne": lvl_measure != value_measure,
            "lt": lvl_measure < value_measure,
            "le": lvl_measure <= value_measure,
            "gt": lvl_measure > value_measure,
            "ge": lvl_measure >= value_measure,
        }
        return switcher[self.operator]


def _level_coordinates_to_measure_description(
    level_coordinates: LevelCoordinates, agg_fun: Optional[str] = None
) -> MeasureDescription:
    """Convert this level into a measure."""
    from ._measures.level_measure import LevelMeasure

    if agg_fun is not None:
        from ._measures.calculated_measure import AggregatedMeasure
        from .scope._utils import LeafLevels

        return AggregatedMeasure(
            _underlying_measure=LevelMeasure(level_coordinates),
            _agg_fun=agg_fun,
            _on_levels=LeafLevels([level_coordinates]),
        )
    return LevelMeasure(level_coordinates)
