from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from atoti_core import BaseLevelIsinCondition, keyword_only_dataclass

from ._level_condition import LevelCondition
from ._single_condition import SingleCondition
from .measure_description import MeasureDescription


@keyword_only_dataclass
@dataclass(frozen=True)
class LevelIsinCondition(SingleCondition, BaseLevelIsinCondition):
    def _to_measure_description(
        self,
        agg_fun: Optional[str] = None,  # pylint: disable=unused-argument
    ) -> MeasureDescription:
        from ._measures.boolean_measure import BooleanMeasure

        if len(self.members) == 1:
            return LevelCondition(
                level_coordinates=self.level_coordinates,
                operator="eq",
                value=self.members[0],
            )._to_measure_description()

        return BooleanMeasure(
            "or",
            [
                LevelCondition(
                    level_coordinates=self.level_coordinates,
                    operator="eq",
                    value=value,
                )._to_measure_description()
                for value in self.members
            ],
        )
