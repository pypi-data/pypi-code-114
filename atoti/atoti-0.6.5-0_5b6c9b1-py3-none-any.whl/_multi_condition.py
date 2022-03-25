from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from atoti_core import BaseMultiCondition, keyword_only_dataclass

from ._condition import Condition
from .measure_description import MeasureDescription


@keyword_only_dataclass
@dataclass(frozen=True)
class MultiCondition(Condition, BaseMultiCondition[Condition]):  # type: ignore
    def _and(self, other: Condition) -> Condition:
        if isinstance(other, MultiCondition):
            return MultiCondition(conditions=[*self.conditions, *other.conditions])

        return MultiCondition(
            conditions=[
                *self.conditions,
                other,  # type: ignore
            ]
        )

    def _to_measure_description(
        self,
        agg_fun: Optional[str] = None,  # pylint: disable=unused-argument
    ) -> MeasureDescription:
        from .function._conjunction import conjunction

        return conjunction(
            *[condition._to_measure_description() for condition in self.conditions]  # type: ignore
        )
