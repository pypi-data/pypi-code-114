from dataclasses import dataclass
from typing import Collection

from atoti_core import LevelCoordinates, keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class PartialAggregateProvider:
    """Partial Aggregate Provider."""

    key: str
    levels_coordinates: Collection[LevelCoordinates]
    measures_names: Collection[str]
