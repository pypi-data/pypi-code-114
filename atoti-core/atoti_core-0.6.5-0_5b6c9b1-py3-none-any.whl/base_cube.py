from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from typing import Generic, Iterable, Literal, Optional, TypeVar, Union

import pandas as pd

from .base_condition import BaseCondition
from .base_hierarchies import BaseHierarchiesBound
from .base_level import BaseLevel
from .base_levels import BaseLevelsBound, HierarchiesT
from .base_measure import BaseMeasure
from .base_measures import BaseMeasuresBound
from .bitwise_operators_only import Identity
from .context import Context
from .empty_mapping import EMPTY_MAPPING
from .keyword_only_dataclass import keyword_only_dataclass
from .repr_json import ReprJson, ReprJsonable
from .scenario import BASE_SCENARIO_NAME

LevelsT = TypeVar("LevelsT", bound=BaseLevelsBound, covariant=True)
MeasuresT = TypeVar("MeasuresT", bound=BaseMeasuresBound, covariant=True)


@keyword_only_dataclass
# See https://github.com/python/mypy/issues/5374.
@dataclass(frozen=True)  # type: ignore[misc]
class BaseCube(
    Generic[HierarchiesT, LevelsT, MeasuresT],
    ReprJsonable,
):
    """Base cube."""

    _name: str
    _hierarchies: HierarchiesT
    _measures: MeasuresT

    @property
    def name(self) -> str:
        """Name of the cube."""
        return self._name

    @property
    @abstractmethod
    def levels(self) -> LevelsT:
        """Levels of the cube."""

    @property
    def measures(self) -> MeasuresT:
        """Measures of the cube."""
        return self._measures

    @property
    def hierarchies(self) -> HierarchiesT:
        """Hierarchies of the cube."""
        return self._hierarchies

    @abstractmethod
    def query(
        self,
        *measures: BaseMeasure,
        condition: Optional[BaseCondition] = None,
        include_totals: bool = False,
        levels: Iterable[BaseLevel] = (),
        mode: Literal["pretty", "raw"] = "pretty",
        scenario: str = BASE_SCENARIO_NAME,
        timeout: Union[int, timedelta] = timedelta(seconds=30),
        context: Context = EMPTY_MAPPING,
    ) -> pd.DataFrame:
        ...

    def _repr_json_(self) -> ReprJson:
        return (
            {
                "Dimensions": self.hierarchies._repr_json_()[0],
                "Measures": self.measures._repr_json_()[0],
            },
            {"expanded": False, "root": self.name},
        )

    @property
    def _identity(self) -> Identity:
        return (self._name,)


BaseCubeBound = BaseCube[BaseHierarchiesBound, BaseLevelsBound, BaseMeasuresBound]
