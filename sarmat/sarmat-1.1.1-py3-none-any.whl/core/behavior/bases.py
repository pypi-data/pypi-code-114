"""
Sarmat.

Описание поведения объектов.

Базовые элементы.
"""
from __future__ import absolute_import

from collections import namedtuple
from datetime import datetime
from typing import Tuple

from sarmat.core.containers import DestinationPointStructure, StationStructure
from sarmat.core.exceptions import IncomparableTypesError

SCHEDULE_ROW = Tuple[
    StationStructure,           # станция
    DestinationPointStructure,  # ближайший населенный пункт
    float,                      # расстояние от начала маршрута
    float,                      # расстояние от предыдущего пункта
    datetime,                   # плановое время прибытия в точку
    datetime,                   # плановое время отправления из точки
    int,                        # время от отправления из начальной точки (в минутах)
    int,                        # время от отправления из предыдущей точки (в минутах)
    int,                        # время стоянки в минутах
]

ScheduleItem = namedtuple(
    "ScheduleItem",
    "station point len_from_start len_from_last arrive depart time_from_start time_from_last stop_time"
)


class NoActionBehavior:
    """Класс, запрещающий всякие действия над объектом"""


class CompareBehavior(NoActionBehavior):
    """Операции сравнения объектов"""

    def _compare_classes(self, other):
        return isinstance(other, self.__class__)

    def _check_type(self, other):
        """Проверка на соответствие типов. Объекты разных типов сравнивать нельзя"""
        if not self._compare_classes(other):
            message = f"Объекты {other.__class__} и {self.__class__} не сравнимы"
            raise IncomparableTypesError(message)

    def __eq__(self, other):
        """Сравнение на равенство"""
        self._check_type(other)

    def __ne__(self, other):
        """Определение неравенства"""
        self._check_type(other)

    def __lt__(self, other):
        """Проверка на <"""
        self._check_type(other)

    def __gt__(self, other):
        """Проверка на >"""
        self._check_type(other)

    def __le__(self, other):
        """Проверка на <="""
        self._check_type(other)

    def __ge__(self, other):
        """Проверка на >="""
        self._check_type(other)

    def __contains__(self, item):
        """Проверка на вхождение во множество"""
