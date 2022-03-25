from typing import Iterable, Mapping, Protocol

from atoti_core import CubeName, JavaType, LevelCoordinates


class GetLevelJavaTypes(Protocol):
    def __call__(
        self, levels_coordinates: Iterable[LevelCoordinates], *, cube_name: CubeName
    ) -> Mapping[LevelCoordinates, JavaType]:
        ...
