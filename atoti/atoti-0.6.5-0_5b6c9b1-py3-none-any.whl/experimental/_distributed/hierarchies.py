from dataclasses import dataclass
from typing import Dict, Tuple, Union

from atoti_core import HierarchyKey, keyword_only_dataclass
from atoti_query import QueryHierarchy
from typeguard import typechecked, typeguard_ignore

from ..._local_hierarchies import LocalHierarchies
from ...column import Column
from ...level import Level

LevelOrColumn = Union[Level, Column]


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class DistributedHierarchies(
    LocalHierarchies[QueryHierarchy],
):
    """Manage the hierarchies."""

    _cube_name: str

    def _get_underlying(self) -> Dict[Tuple[str, str], QueryHierarchy]:
        hierarchies = {
            coordinates: self._create_hierarchy_from_arguments(description)
            for coordinates, description in self._java_api.retrieve_hierarchies(
                cube_name=self._cube_name,
            ).items()
        }
        return {
            # https://github.com/python/mypy/issues/12183
            hierarchyCoordinate: hierarchies[hierarchyCoordinate]  # type: ignore[misc]
            for hierarchyCoordinate in hierarchies
        }

    @typechecked
    def __getitem__(self, key: HierarchyKey) -> QueryHierarchy:
        (dimension_name, hierarchy_name) = self._convert_key(key)
        cube_hierarchies = self._java_api.retrieve_hierarchy(
            hierarchy_name,
            cube_name=self._cube_name,
            dimension=dimension_name,
        )
        hierarchies = [
            self._create_hierarchy_from_arguments(h) for h in cube_hierarchies
        ]
        if len(hierarchies) == 0:
            raise KeyError(f"Unknown hierarchy: {key}")
        # https://github.com/python/mypy/issues/12183
        if len(hierarchies) == 1:
            return hierarchies[0]  # type: ignore[return-value]
        raise self._multiple_hierarchies_error(key, hierarchies)  # type: ignore[arg-type]
