"""
Sarmat.

Описание сущностей.

Управление перевозками.
"""
from datetime import time, date
from typing import List

from .geo_locations import DirectionStructure, DestinationPointStructure, RoadNameStructure
from .sarmat import SarmatStructure, nested_dataclass
from ..constants import PeriodType, RoadType, StationType, JourneyType


@nested_dataclass
class StationStructure(SarmatStructure):
    """Станции (пункты посадки-высадки пассажиров)"""

    station_type: StationType               # тип станции
    name: str                               # наименование
    point: DestinationPointStructure        # ближайший населенный пункт
    address: str = ""                       # почтовый адрес


@nested_dataclass
class RoadStructure(SarmatStructure):
    """Дороги"""

    start_point: DestinationPointStructure      # начало дороги
    end_point: DestinationPointStructure        # конец дороги
    direct_travel_time_min: int                 # время прохождения в прямом направлении
    reverse_travel_time_min: int                # время прохождения в обратном направлении
    direct_len_km: float                        # расстояние в прямом направлении
    reverse_len_km: float                       # расстояние в обратном направлении
    road_type: RoadType                         # тип дорожного покрытия
    road: RoadNameStructure = None              # классификация дороги


@nested_dataclass
class RouteItemStructure(SarmatStructure):
    """Состав маршрута"""

    length_from_last_km: float                  # расстояние от предыдущего пункта
    travel_time_min: int                        # время движения от предыдущего пункта в минутах
    road: RoadStructure = None                  # дорога
    order: int = 1                              # порядок следования
    station: StationStructure = None            # станция
    point: DestinationPointStructure = None     # ближайший населенный пункт
    stop_time_min: int = None                   # время стоянки в минутах


@nested_dataclass
class RouteStructure(SarmatStructure):
    """Описание маршрута"""

    name: str                                       # наименование
    first_station: StationStructure                 # станция отправления
    structure: List[RouteItemStructure]             # состав маршрута
    direction: List[DirectionStructure] = None      # направления
    comments: str = None                            # комментарий к маршруту
    number: int = None                              # номер маршрута
    literal: str = ""                               # литера


@nested_dataclass
class JourneyStructure(SarmatStructure):
    """Атрибуты рейса"""

    number: float                                   # номер рейса
    name: str                                       # наименование
    first_station: StationStructure                 # пункт отправления
    structure: List[RouteItemStructure]             # состав рейса
    journey_type: JourneyType                       # тип рейса
    departure_time: time                            # время отправления
    bunch: int = None                               # принадлежность к связке
    literal: str = None                             # литера
    is_chartered: bool = False                      # признак заказного рейса
    need_control: bool = False                      # признак именной продажи и мониторинга
    season_begin: date = None                       # начало сезона
    season_end: date = None                         # окончание сезона
    direction: List[DirectionStructure] = None      # направления
    comments: str = None                            # комментарии по рейсу


@nested_dataclass
class JourneyBunchItemStructure(SarmatStructure):
    """Атрибуты элемента из связки рейсов"""

    journey: JourneyStructure     # рейс
    stop_interval: int      # время простоя в часах


@nested_dataclass
class JourneyBunchStructure(SarmatStructure):
    """Атрибуты связки рейсов"""

    journeys: List[JourneyBunchItemStructure]     # элементы связки
    name: str = None                           # наименование связки


@nested_dataclass
class PeriodItemStructure(SarmatStructure):
    """Элементы сложного периода"""

    period_type: PeriodType     # тип периода
    cypher: str                 # шифр (константа)
    name: str                   # название
    value: List[int]            # список значений
    is_active: bool             # период активности


@nested_dataclass
class PeriodStructure(SarmatStructure):
    """Период"""

    cypher: str                                 # системное имя
    name: str                                   # константа
    periods: List[PeriodItemStructure] = None   # описание сложного периода
    period: PeriodItemStructure = None          # описание простого периода
