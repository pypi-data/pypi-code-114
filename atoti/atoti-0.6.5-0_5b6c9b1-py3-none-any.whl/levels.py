from typing import Optional

from atoti_core import BaseLevels, LevelKey, raise_multiple_levels_with_same_name_error

from .hierarchies import Hierarchies
from .level import Level


class Levels(BaseLevels[Hierarchies, Level]):
    """Flat representation of all the levels in the cube."""

    def __delitem__(self, key: LevelKey) -> None:
        """Delete a level.

        Args:
            key: The name of the level to delete, or a ``(hierarchy_name, level_name)`` tuple.
        """
        if key not in self:
            raise KeyError(f"{key} is not an existing level.")
        level = self[key]
        level._java_api.drop_level(level._coordinates, cube_name=level._cube_name)
        level._java_api.refresh()

    def _find_level(
        self,
        level_name: str,
        *,
        dimension_name: Optional[str] = None,
        hierarchy_name: Optional[str] = None,
    ) -> Level:
        """Get a level from the hierarchy name and level name."""
        hierarchies = self._hierarchies._java_api.retrieve_hierarchy_for_level(
            level_name,
            cube_name=self._hierarchies._cube_name,
            dimension_name=dimension_name,
            hierarchy_name=hierarchy_name,
        )
        if len(hierarchies) > 1:
            raise_multiple_levels_with_same_name_error(
                level_name,
                hierarchies=[hierarchy.get_coordinates() for hierarchy in hierarchies],
            )

        if len(hierarchies) == 0:
            raise KeyError(f"No level with name {level_name} found in cube.")

        hierarchy = self._hierarchies._create_hierarchy_from_arguments(hierarchies[0])

        # https://github.com/python/mypy/issues/12183
        return hierarchy.levels[level_name]  # type: ignore[return-value]
