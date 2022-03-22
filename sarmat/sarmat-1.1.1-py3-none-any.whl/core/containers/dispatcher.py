"""
Sarmat.

Описание сущностей.

Диспетчерские объекты.
"""
from datetime import date, datetime
from typing import List
from uuid import UUID

from .sarmat import BaseSarmatStructure, SarmatStructure, nested_dataclass
from .traffic_management import PeriodStructure, StationStructure, JourneyStructure
from .vehicle import PermitStructure
from ..constants import JourneyClass, JourneyState


@nested_dataclass
class IntervalStructure(SarmatStructure):
    """График выполнения рейсов"""

    journey: JourneyStructure   # рейс
    start_date: date            # дата начала
    interval: PeriodStructure   # интервал движения


@nested_dataclass
class JourneyProgressStructure(SarmatStructure):
    """Атрибуты рейсовой ведомости"""

    id: UUID                                            # идентификатор ведомости
    depart_date: date                                   # дата отправления в рейс
    journey: JourneyStructure                           # рейс
    permit: PermitStructure                             # номер путевого листа


@nested_dataclass
class JourneyScheduleStructure(BaseSarmatStructure):
    """Процесс прохождения рейса по автоматизированным точкам"""

    journey_progress: JourneyProgressStructure             # рейсовая ведомость
    journey_class: JourneyClass                            # классификация рейса в данном пункте
    station: StationStructure                              # станция
    state: JourneyState                                    # состояние рейса
    plan_arrive: datetime = None                           # плановое время прибытия
    fact_arrive: datetime = None                           # фактическое время прибытия
    plan_depart: datetime = None                           # плановое время отправления
    fact_depart: datetime = None                           # фактическое время отправления
    platform: str = ""                                     # платформа
    comment: str = ""                                      # комментарий к текущему пункту
    last_items: List["JourneyScheduleStructure"] = None    # оставшиеся активные пункты прохождения рейса
