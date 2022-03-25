from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Optional, Tuple, Union, overload

from atoti_core import HierarchyKey, keyword_only_dataclass
from typeguard import typechecked, typeguard_ignore

from ._local_hierarchies import LocalHierarchies
from .column import Column
from .hierarchy import Hierarchy
from .level import Level

LevelOrColumn = Union[Level, Column]

_HierarchyDescription = Union[Iterable[LevelOrColumn], Mapping[str, LevelOrColumn]]


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class Hierarchies(LocalHierarchies[Hierarchy]):
    """Manage the hierarchies.

    Example:
        >>> prices_df = pd.DataFrame(
        ...     columns=["Nation", "City", "Color", "Price"],
        ...     data=[
        ...         ("France", "Paris", "red", 20.0),
        ...         ("France", "Lyon", "blue", 15.0),
        ...         ("France", "Toulouse", "green", 10.0),
        ...         ("UK", "London", "red", 20.0),
        ...         ("UK", "Manchester", "blue", 15.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(prices_df, table_name="Prices")
        >>> cube = session.create_cube(table, mode="manual")
        >>> h = cube.hierarchies
        >>> h["Nation"] = {"Nation": table["Nation"]}
        >>> list(h)
        [('Prices', 'Nation')]

    A hierarchy can be renamed by creating a new one with the same levels and then removing the old one.

        >>> h["Country"] = h["Nation"].levels
        >>> del h["Nation"]
        >>> list(h)
        [('Prices', 'Country')]

    The :meth:`~dict.update` method is overridden to batch hierarchy creation operations for improved performance:

        >>> h.update(
        ...     {
        ...         ("Geography", "Geography"): [table["Nation"], table["City"]],
        ...         "Color": {"Color": table["Color"]},
        ...     }
        ... )
        >>> list(h)
        [('Prices', 'Color'), ('Geography', 'Geography'), ('Prices', 'Country')]
    """

    _cube_name: str

    def _get_underlying(self) -> Dict[Tuple[str, str], Hierarchy]:
        return {
            # https://github.com/python/mypy/issues/12183
            coordinates: self._create_hierarchy_from_arguments(description)  # type: ignore[misc]
            for coordinates, description in self._java_api.retrieve_hierarchies(
                cube_name=self._cube_name,
            ).items()
        }

    @typechecked
    def __getitem__(self, key: HierarchyKey) -> Hierarchy:
        (dimension_name, hierarchy_name) = self._convert_key(key)
        hierarchies = self._java_api.retrieve_hierarchy(
            hierarchy_name,
            cube_name=self._cube_name,
            dimension=dimension_name,
        )
        if len(hierarchies) == 0:
            raise KeyError(f"Unknown hierarchy: {key}")
        if len(hierarchies) == 1:
            # https://github.com/python/mypy/issues/12183
            return self._create_hierarchy_from_arguments(hierarchies[0])  # type: ignore[return-value]
        raise self._multiple_hierarchies_error(
            key, [hierarchy.get_coordinates() for hierarchy in hierarchies]
        )

    @typechecked
    def __delitem__(self, key: HierarchyKey) -> None:
        try:
            self._java_api.drop_hierarchy(self._cube_name, self[key]._coordinates)
        except KeyError:
            raise KeyError(f"{key} is not an existing hierarchy.") from None

    # Custom override with same value type as the one used in `update()`.
    @typechecked
    def __setitem__(  # type: ignore
        self,
        key: HierarchyKey,
        value: _HierarchyDescription,
    ) -> None:
        self.update({key: value})

    # Custom override types on purpose so that hierarchies can be described either as an iterable or a mapping.
    def _update(  # type: ignore[override]
        self,
        other: Mapping[HierarchyKey, Mapping[str, LevelOrColumn]],
    ) -> None:
        structure: Dict[str, Dict[str, Mapping[str, str]]] = {}
        for hierarchy_key, levels_or_columns in other.items():
            dimension_name, hierarchy_name = self._get_dimension_and_hierarchy_name(
                hierarchy_key, levels_or_columns
            )
            if dimension_name not in structure:
                structure[dimension_name] = {}
            structure[dimension_name].update(
                {hierarchy_name: _get_hierarchy_levels(levels_or_columns)}
            )
        self._java_api.update_hierarchies_for_cube(self._cube_name, structure=structure)
        self._java_api.refresh()

    # Custom override types on purpose so that hierarchies can be described either as an iterable or a mapping.
    @overload  # type: ignore[override]
    def update(
        self,
        __m: Mapping[HierarchyKey, _HierarchyDescription],
        **kwargs: _HierarchyDescription,
    ) -> None:
        ...

    @overload
    def update(
        self,
        __m: Iterable[Tuple[HierarchyKey, _HierarchyDescription]],
        **kwargs: _HierarchyDescription,
    ) -> None:
        ...

    @overload
    def update(self, **kwargs: _HierarchyDescription) -> None:
        ...

    # Custom override types on purpose so that hierarchies can be described either as an iterable or a mapping.
    def update(  # type: ignore
        self,
        __m: Optional[
            Union[
                Mapping[HierarchyKey, _HierarchyDescription],
                Iterable[Tuple[HierarchyKey, _HierarchyDescription]],
            ]
        ] = None,
        **kwargs: _HierarchyDescription,
    ) -> None:
        """This method batches the updates for improved performance."""
        other: Dict[HierarchyKey, _HierarchyDescription] = {}
        if __m is not None:
            other.update(__m)
        other.update(**kwargs)
        final_hierarchies: Mapping[HierarchyKey, Mapping[str, LevelOrColumn]] = {
            hierarchy_key: _normalize_levels(levels_or_columns)
            for hierarchy_key, levels_or_columns in other.items()
        }
        self._update(final_hierarchies)

    def _get_dimension_and_hierarchy_name(
        self,
        hierarchy_key: HierarchyKey,
        levels_or_columns: Mapping[str, LevelOrColumn],
    ) -> Tuple[str, str]:
        dimension_name, hierarchy_name = self._convert_key(hierarchy_key)
        if dimension_name is None:
            hierarchies = self._java_api.retrieve_hierarchy(
                hierarchy_name,
                cube_name=self._cube_name,
                dimension=None,
            )
            if len(hierarchies) > 1:
                raise self._multiple_hierarchies_error(
                    hierarchy_name,
                    [hierarchy.get_coordinates() for hierarchy in hierarchies],
                )
            first_item = list(levels_or_columns.values())[0]
            if isinstance(first_item, Level):
                dimension_name = first_item.dimension
            else:
                dimension_name = first_item._table_name
        return dimension_name, hierarchy_name


def _normalize_levels(
    levels_or_columns: Union[Iterable[LevelOrColumn], Mapping[str, LevelOrColumn]]
) -> Mapping[str, LevelOrColumn]:
    return (
        levels_or_columns  # type: ignore
        if isinstance(levels_or_columns, Mapping)
        else {
            level_or_column.name: level_or_column
            for level_or_column in levels_or_columns
        }
    )


def _get_hierarchy_levels(
    levels_or_columns: Mapping[str, LevelOrColumn]
) -> Mapping[str, str]:
    return {
        level_name: level_or_column._column_name
        if isinstance(level_or_column, Level)
        else level_or_column.name
        for (level_name, level_or_column) in levels_or_columns.items()
    }
