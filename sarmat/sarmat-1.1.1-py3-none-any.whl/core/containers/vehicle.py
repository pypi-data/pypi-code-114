"""
Sarmat.

Описание сущностей.

Подвижной состав.
"""
from datetime import date
from typing import List
from uuid import UUID

from .sarmat import PersonStructure, SarmatStructure, nested_dataclass
from ..constants import CrewType, PermitType, VehicleType


@nested_dataclass
class VehicleStructure(SarmatStructure):
    """Подвижной состав"""

    vehicle_type: VehicleType   # тип транспортного средства
    vehicle_name: str           # марка транспортного средства
    state_number: str           # гос. номер
    seats: int                  # количество мест для посадки
    stand: int = 0              # количество мест стоя
    capacity: int = 0           # вместимость багажного отделения


@nested_dataclass
class CrewStructure(PersonStructure, SarmatStructure):
    """Экипаж"""

    crew_type: CrewType     # тип члена экипажа
    is_main: bool = True    # признак главного члена экипажа


@nested_dataclass
class PermitStructure(SarmatStructure):
    """Путевой лист"""

    id: UUID                            # идентификатор записи
    number: str                         # номер путевого листа
    permit_type: PermitType             # тип путевого листа
    depart_date: date                   # дата выезда
    crew: List[CrewStructure]           # экипаж
    vehicle: List[VehicleStructure]     # подвижной состав
