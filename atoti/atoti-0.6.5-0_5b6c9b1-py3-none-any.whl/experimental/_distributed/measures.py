from dataclasses import dataclass
from typing import Dict, Mapping

from atoti_core import keyword_only_dataclass
from atoti_query import QueryMeasure

from ..._local_measures import LocalMeasures
from ...exceptions import AtotiJavaException


@keyword_only_dataclass
@dataclass
class DistributedMeasures(LocalMeasures[QueryMeasure]):
    """Manage the measures."""

    _cube_name: str

    def _get_underlying(self) -> Dict[str, QueryMeasure]:
        """Fetch the measures from the JVM each time they are needed."""
        cube_measures = self._java_api.get_full_measures(self._cube_name)
        return {
            name: QueryMeasure(
                _name=name,
                _visible=cube_measures[name].visible,
                _folder=cube_measures[name].folder,
                _formatter=cube_measures[name].formatter,
                _description=cube_measures[name].description,
            )
            for name in cube_measures
        }

    def __getitem__(self, key: str) -> QueryMeasure:
        """Return the measure with the given name."""
        try:
            cube_measure = self._java_api.get_measure(self._cube_name, key)
            return QueryMeasure(
                _name=key,
                _visible=cube_measure.visible,
                _folder=cube_measure.folder,
                _formatter=cube_measure.formatter,
                _description=cube_measure.description,
            )
        except AtotiJavaException:
            raise KeyError(f"No measure named {key}") from None

    def _update(self, other: Mapping[str, QueryMeasure]) -> None:
        raise NotImplementedError("Distributed cube measures cannot be changed")

    def __delitem__(self, key: str) -> None:
        raise NotImplementedError("Distributed cube measures cannot be changed")
