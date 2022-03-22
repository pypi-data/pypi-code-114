"""
Sarmat.

Описание сущностей.

Географические объекты.
"""
from .sarmat import SarmatStructure, nested_dataclass
from ..constants import LocationType, SettlementType


@nested_dataclass
class GeoStructure(SarmatStructure):
    """Структура географического справочника"""

    name: str                       # наименование
    location_type: LocationType     # тип образования
    latin_name: str = ""            # латинское название
    mapping_data: dict = None       # данные геолокации
    tags: dict = None               # тэги
    parent: 'GeoStructure' = None   # родительский объект


@nested_dataclass
class DestinationPointStructure(SarmatStructure):
    """Стрктура для описания пунктов назначения"""

    name: str               # наименование
    state: GeoStructure     # территориальное образование
    point_type: SettlementType  # тип поселения


@nested_dataclass
class DirectionStructure(SarmatStructure):
    """Описание направления"""

    name: str           # наименование
    cypher: str = ""    # шифр (системное имя)


@nested_dataclass
class RoadNameStructure(SarmatStructure):
    """Описание дороги"""

    cypher: str
    name: str = None
