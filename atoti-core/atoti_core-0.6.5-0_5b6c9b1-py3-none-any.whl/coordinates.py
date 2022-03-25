from typing import Tuple, Union

CubeName = str

DimensionName = str

HierarchyName = str
HierarchyCoordinates = Tuple[DimensionName, HierarchyName]

HierarchyKey = Union[HierarchyName, HierarchyCoordinates]

LevelName = str
LevelCoordinates = Tuple[DimensionName, HierarchyName, LevelName]

LevelKey = Union[LevelName, Tuple[HierarchyName, LevelName], LevelCoordinates]
