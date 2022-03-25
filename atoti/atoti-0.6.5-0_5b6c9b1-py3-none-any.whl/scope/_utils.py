from abc import abstractmethod
from dataclasses import dataclass
from typing import Collection, Optional, Tuple

from atoti_core import (
    HierarchyCoordinates,
    LevelCoordinates,
    coordinates_to_java_description,
    keyword_only_dataclass,
)

from .._measures.generic_measure import GenericMeasure
from ..measure_description import MeasureDescription
from .scope import Scope


@keyword_only_dataclass
# See https://github.com/python/mypy/issues/5374.
@dataclass(frozen=True)  # type: ignore[misc]
class Window(Scope):
    """Window-like structure used in the computation of cumulative aggregations."""

    @abstractmethod
    def _create_aggregated_measure(
        self, measure: MeasureDescription, agg_fun: str
    ) -> MeasureDescription:
        """Create the appropriate aggregated measure for this window.

        Args:
            measure: The underlying measure to aggregate
            agg_fun: The aggregation function to use.
        """


@keyword_only_dataclass
@dataclass(frozen=True)
class CumulativeWindow(Window):
    """Implementation of a Window for member-based cumulative aggregations.

    It contains a level, its range of members which is (-inf, 0) by default, and a partitioning consisting of levels in that hierarchy.
    """

    _level_coordinates: LevelCoordinates
    _dense: bool
    _window: Optional[range]
    _partitioning: Optional[LevelCoordinates] = None

    def _create_aggregated_measure(
        self, measure: MeasureDescription, agg_fun: str
    ) -> MeasureDescription:
        return GenericMeasure(
            "WINDOW_AGG",
            measure,
            coordinates_to_java_description(self._level_coordinates),
            coordinates_to_java_description(self._partitioning)
            if self._partitioning is not None
            else None,
            agg_fun,
            (self._window.start, self._window.stop) if self._window else None,
            self._dense,
        )


@keyword_only_dataclass
@dataclass(frozen=True)
class CumulativeTimeWindow(Window):
    """Implementation of a Window for time-based cumulative aggregations."""

    _level_coordinates: LevelCoordinates
    _window: Tuple[Optional[str], Optional[str]]

    def _create_aggregated_measure(
        self, measure: MeasureDescription, agg_fun: str
    ) -> MeasureDescription:
        back_offset, forward_offset = (
            CumulativeTimeWindow._parse_time_period(self._window)
            if self._window
            else (None, None)
        )

        return GenericMeasure(
            "TIME_PERIOD_AGGREGATION",
            measure,
            coordinates_to_java_description(self._level_coordinates),
            back_offset,
            forward_offset,
            agg_fun,
        )

    @staticmethod
    def _parse_time_period(
        time_period: Tuple[Optional[str], Optional[str]]
    ) -> Tuple[Optional[str], Optional[str]]:
        """Convert the time period into a backward offset and a forward offset."""
        back = time_period[0]
        forward = time_period[1]
        return (
            # Drop the `-` sign.
            back[1:] if back is not None else None,
            forward if forward is not None else None,
        )


@keyword_only_dataclass
@dataclass(frozen=True)
class SiblingsWindow(Window):
    """Implementation of a Window for sibling aggregations.

    It contains at least hierarchy, and whether to exclude the current member from the calculations (useful when computing marginal aggregations).
    """

    _hierarchy_coordinates: HierarchyCoordinates
    _exclude_self: bool = False

    def _create_aggregated_measure(
        self, measure: MeasureDescription, agg_fun: str
    ) -> MeasureDescription:
        return GenericMeasure(
            "SIBLINGS_AGG",
            measure,
            coordinates_to_java_description(self._hierarchy_coordinates),
            agg_fun,
            self._exclude_self,
        )


@dataclass(frozen=True)
class LeafLevels(Scope):  # pylint: disable=keyword-only-dataclass
    """A collection of levels coordinates, used in dynamic aggregation operations."""

    _levels_coordinates: Collection[LevelCoordinates]

    @property
    def levels_coordinates(self) -> Collection[LevelCoordinates]:
        """Dynamic aggregation levels."""
        return self._levels_coordinates
