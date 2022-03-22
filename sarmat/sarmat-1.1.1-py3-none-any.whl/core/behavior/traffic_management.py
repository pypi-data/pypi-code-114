"""
Sarmat.

Описание поведения объектов.

Объекты управления перевозками.
"""
from datetime import date, datetime, timedelta
from typing import Generator

from sarmat.core.containers import PeriodItemStructure, StationStructure, DestinationPointStructure, RouteItemStructure
from sarmat.core.exceptions import IncomparableTypesError, WrongValueError

from .bases import CompareBehavior, ScheduleItem, SCHEDULE_ROW


class BhStation(CompareBehavior):
    """Базовое поведение объекта Станция"""
    compare_error_message = "Сравнение станций не предусмотрено"

    def _compare_classes(self, other):
        return isinstance(other, BhStation)

    def __eq__(self, other):
        """Сравнение на равенство станций"""
        super().__eq__(other)

        if self.id and other.id:
            return self.id == other.id

        if not(self.id or other.id):
            return self.station_type == other.station_type and self.point == other.point and self.name == other.name

        return False

    def __ne__(self, other):
        """Проверка на неравенство станций"""
        super().__ne__(other)

        if self.id and other.id:
            return self.id != other.id

        if not(self.id or other.id):
            return self.station_type != other.station_type or self.point != other.point or self.name != other.name

        return True

    def __lt__(self, item):
        """Проверка на превосходство объекта перед станцией не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, item):
        """Проверка на превосходство станции над объектом не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Проверка на непревосходство станции над объектом не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед станцией не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на принадлежность станции к населенному пункту"""
        raise IncomparableTypesError("Станции проверке на вхождение не подлежат")


class BhRoad(CompareBehavior):
    """Базовое поведение объекта 'Дорога'"""
    compare_error_message = "Сравнение дорог не предусмотрено"

    def _compare_classes(self, other):
        return isinstance(other, BhRoad)

    def __eq__(self, other):
        """Сравнение на равенство дорог"""
        super().__eq__(other)

        if self.id and other.id:
            return self.id == other.id

        if not(self.id or other.id):
            return all([
                self.direct_travel_time_min == other.direct_travel_time_min,
                self.reverse_travel_time_min == other.reverse_travel_time_min,
                self.direct_len_km == other.direct_len_km,
                self.reverse_len_km == other.reverse_len_km,
                self.road_type == other.road_type,
            ])

        return False

    def __ne__(self, other):
        """Проверка на неравенство дорог"""
        super().__ne__(other)

        if self.id and other.id:
            return self.id != other.id

        if not(self.id or other.id):
            return any([
                self.direct_travel_time_min != other.direct_travel_time_min,
                self.reverse_travel_time_min != other.reverse_travel_time_min,
                self.direct_len_km != other.direct_len_km,
                self.reverse_len_km != other.reverse_len_km,
                self.road_type != other.road_type,
                ])

        return True

    def __lt__(self, item):
        """Проверка на превосходство объекта перед дорогой"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, item):
        """Проверка на превосходство над объектом дорога"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Проверка на непревосходство над объектом дорога"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед дорогой"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на принадлежность дороги"""
        raise IncomparableTypesError("Проверка н авхождение для дорог не предусмотрена")


class BhRouteItem(CompareBehavior):
    """Базовое поведение объекта 'Пункт маршрута'"""
    compare_error_message = "Для пунктов маршрута не предусмотрены операции сравнения"

    def _compare_classes(self, other):
        return isinstance(other, BhRouteItem)

    def __eq__(self, other):
        """Сравнение на равенство пунктов маршрута"""
        super().__eq__(other)

        if self.id and other.id:
            return self.id == other.id

        if not(self.id and other.id):
            return self.station == other.station and self.point == other.point

        return False

    def __ne__(self, other):
        """Проверка на неравенство пунктов маршрута"""
        super().__ne__(other)

        if self.id and other.id:
            return self.id != other.id

        if not(self.id or other.od):
            return self.station != other.station or self.point != other.point

        return True

    def __lt__(self, item):
        """Проверка на превосходство объекта перед пунктом маршрута"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, item):
        """Проверка на превосходство над объектом пункт маршрута"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Проверка на непревосходство над объектом пункт маршрута"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед пунктом маршрута"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на принадлежность объекта к пункту маршрута"""
        if isinstance(item, StationStructure):
            return self.station == item

        if isinstance(item, DestinationPointStructure):
            return self.point == item

        raise IncomparableTypesError(f"Для объекта {item} проверка на вхождение в пункт маршрута не предусмотрена")


class BhPeriodItem(CompareBehavior):
    """Базовое поведение объекта 'Элемент периода'"""

    def _compare_classes(self, other):
        return isinstance(other, BhPeriodItem)

    def __eq__(self, other):
        """Сравнение на равенство периодов"""
        super().__eq__(other)

        return self.period_type == other.period_type and self.value == other.value

    def __ne__(self, other):
        """Проверка на неравенство периодов"""
        super().__ne__(other)

        return self.period_type != other.period_type or self.value != other.value

    def __lt__(self, item):
        """Проверка на превосходство объекта перед периодом"""
        super().__lt__(item)
        if self.period_type != item.period_type:
            raise IncomparableTypesError("Периоды разных типов сравнивать нельзя")

        return self.value < item.value

    def __gt__(self, item):
        """Проверка на превосходство периода над объектом"""
        super().__gt__(item)
        if self.period_type != item.period_type:
            raise IncomparableTypesError("Периоды разных типов сравнивать нельзя")

        return self.value > item.value

    def __le__(self, other):
        """Проверка на непревосходство над объектом периода"""
        super().__le__(other)
        if self.period_type != other.period_type:
            raise IncomparableTypesError("Периоды разных типов сравнивать нельзя")

        return self.value <= other.value

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед периодом"""
        super().__ge__(other)
        if self.period_type != other.period_type:
            raise IncomparableTypesError("Периоды разных типов сравнивать нельзя")

        return self.value >= other.value

    def __contains__(self, item):
        """Проверка на принадлежность объекта к периоду не имеет смысла"""
        raise IncomparableTypesError("Проверка на вхождение для периода не предусмотрена")


class BhPeriod(CompareBehavior):
    """Базовое поведение объекта 'Период'"""

    compare_error_message = "Сравнение периодов не предусматривается"

    def _compare_classes(self, other):
        return isinstance(other, BhPeriod)

    def __eq__(self, other):
        """Сравнение на равенство периодов"""
        super().__eq__(other)

        if self.period and other.period:
            return self.period == other.period

        if self.periods and other.periods:
            if len(self.periods) == len(other.periods):
                pairs = zip(self.periods, other.periods)
                return all([i == j for i, j in pairs])

        return False

    def __ne__(self, other):
        """Проверка на неравенство периодов"""
        super().__eq__(other)

        if self.period and other.period:
            return self.period != other.period

        if self.periods and other.periods:
            if len(self.periods) != len(other.periods):
                return True

            pairs = zip(self.periods, other.periods)
            return not all([i == j for i, j in pairs])

        return True

    def __lt__(self, other):
        """Проверка на превосходство объекта перед периодом"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, item):
        """Проверка на превосходство над объектом периода"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Проверка на непревосходство над объектом периода"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед периодом"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на принадлежность объекта к периоду"""
        if isinstance(item, PeriodItemStructure):
            return item in self.periods

        raise IncomparableTypesError(f"Объект {item} неподходящего типа")

    def __len__(self):
        """Длина составной части периода"""
        return len(self.periods) if self.periods else 0

    def __getitem__(self, item):
        """Получение элемента из сложного периода"""
        try:
            int(item)
        except (ValueError, TypeError):
            raise WrongValueError("Индекс элемента должен быть числом")

        if abs(item) >= len(self.periods):
            raise WrongValueError("Индекс превышает размер составного периода")

        return self.preiods[item]


class BhRoute(CompareBehavior):
    """Базовые методы маршрутов"""

    def _compare_classes(self, other):
        return isinstance(other, BhRoute)

    def __eq__(self, other):
        """Сравнение на равенство маршрутов"""
        super().__eq__(other)
        return self.first_station == other.first_station and self.structure == other.structure

    def __ne__(self, other):
        """Проверка на неравенство маршрутов"""
        super().__ne__(other)
        return self.first_station != other.first_station or self.structure != other.structure

    def __lt__(self, item):
        """Проверка на превосходство объекта перед маршрутом"""
        super().__lt__(item)
        return len(self.structure) < len(item.structure)

    def __gt__(self, item):
        """Проверка на превосходство над объектом маршрут"""
        super().__gt__(item)
        return len(self.structure) > len(item.structure)

    def __le__(self, other):
        """Проверка на непревосходство над объектом маршрут"""
        super().__le__(other)
        return len(self.structure) <= len(other.structure)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед маршрутом"""
        super().__ge__(other)
        return len(self.structure) >= len(other.structure)

    def __contains__(self, item):
        """Проверка на принадлежность объекта к маршруту"""
        if isinstance(item, StationStructure):
            stations = [self.first_station] + [i.station for i in self.structure]
            return item in stations

        if isinstance(item, DestinationPointStructure):
            return item in [i.point for i in self.structure]

        if isinstance(item, RouteItemStructure):
            return item in self.structure

        raise IncomparableTypesError(f"Для объекта {item} проверка на принадлежность к маршруту не выполняется")

    def __getitem__(self, item: int) -> ScheduleItem:
        if isinstance(item, slice):
            return self._get_slice(item)

        try:
            int(item)
        except (TypeError, ValueError):
            raise WrongValueError("Индекс элемента должен быть числом")

        if len(self.structure) < abs(item):
            raise WrongValueError(f"Длина маршрута меньше {item}")

        schedule = list(self.get_schedule())
        return schedule[item]

    def __len__(self) -> int:
        return len(self.structure) + 1

    def _get_slice(self, item: slice) -> ScheduleItem:
        route = list(self.get_schedule())[item]

        if not route:
            raise WrongValueError("Неверно указаны пункты отправления и назначения")

        if len(route) == 1:
            return route[0]

        start_point, end_point = route[0], route[-1]

        length, travel_time, stop_time = 0, 0, 0
        for i in route[1:]:
            length += i.len_from_last
            travel_time += i.time_from_last
            stop_time += i.stop_time

        if stop_time:
            stop_time -= end_point.stop_time

        return ScheduleItem(
            f"{start_point.station or ''}-{end_point.station or ''}",
            f"{start_point.point or ''}-{end_point.point or ''}",
            end_point.len_from_start - start_point.len_from_start,
            length,
            None,
            None,
            end_point.time_from_start - start_point.time_from_start,
            travel_time,
            stop_time
        )

    def get_schedule(self) -> Generator[SCHEDULE_ROW, None, None]:
        """
        Расчет расписания по маршруту
        Returns: генератор списка пунктов прохождения по маршруту
        """
        length_from_start: int = 0
        travel_min_from_start: int = 0

        yield ScheduleItem(self.first_station,
                           self.first_station.point,
                           length_from_start,
                           0,
                           None,
                           None,
                           travel_min_from_start,
                           0,
                           0)

        for item in sorted(self.structure, key=lambda x: x.order):
            length_from_start += item.length_from_last_km or 0
            travel_min_from_start += item.travel_time_min or 0
            yield ScheduleItem(item.station,
                               item.point,
                               length_from_start,
                               item.length_from_last_km,
                               None,
                               None,
                               travel_min_from_start,
                               item.travel_time_min,
                               item.stop_time_min or 0)


class BhJourney(BhRoute):
    """Базовые методы рейсов"""

    def _compare_classes(self, other):
        return isinstance(other, BhJourney)

    def __eq__(self, other):
        """Сравнение на равенство рейсов"""
        return super().__eq__(other) and (self.departure_time == other.departure_time)

    def __ne__(self, other):
        """Проверка на неравенство рейсов"""
        return super().__ne__(other) or (self.departure_time != other.departure_time)

    def get_journey_schedule(self, start_date: date) -> Generator[SCHEDULE_ROW, None, None]:
        """
        Расчет расписания по рейсу
        Returns: генератор списка пунктов прохождения по рейсу
        """
        stop_time = 0
        hour, minute = self.departure_time.hour, self.departure_time.minute
        departure_date_time = datetime(*start_date.timetuple()[:3], hour, minute)

        for item in super().get_schedule():
            yield ScheduleItem(
                item.station,
                item.point,
                item.len_from_start,
                item.len_from_last,
                departure_date_time + timedelta(minutes=item.time_from_start + stop_time),
                departure_date_time + timedelta(minutes=(item.time_from_start + stop_time + item.stop_time)),
                item.time_from_start,
                item.time_from_last,
                item.stop_time,
            )

            stop_time += item.stop_time


class BhJourneyBunchItem(CompareBehavior):
    """Базовое поведение объекта 'Элемент связки рейсов'"""
    compare_error_message = "Операция сравнения для элементов связок не предусмотрена"

    def _compare_classes(self, other):
        return isinstance(other, BhJourneyBunchItem)

    def __eq__(self, other):
        """Сравнение на равенство элементов связки"""
        super().__eq__(other)
        return self.journey == other.journey and self.stop_interval == other.stop_interval

    def __ne__(self, other):
        """Проверка на неравенство элементов связки"""
        super().__ne__(other)
        return self.journey != other.journey or self.stop_interval != other.stop_interval

    def __lt__(self, item):
        """Проверка на превосходство объекта перед элементом связки"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, item):
        """Проверка на превосходство над объектом элемент связки"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Проверка на непревосходство над объектом элемент связки"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед элементом связки"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на принадлежность объекта к элементу связки"""
        raise IncomparableTypesError("Проверка на вхождение для элементов связки не предусмотрена")


class BhJourneyBunch(CompareBehavior):
    """Базовое поведение объекта Связка рейсов"""
    compare_message_error = "Сравнение связок не предусматривается"

    def _compare_classes(self, other):
        return isinstance(other, BhJourneyBunch)

    def __eq__(self, other):
        """Сравнение на равенство связок рейсов"""
        super().__eq__(other)
        return self.journeys == other.journeys

    def __ne__(self, other):
        """Проверка на неравенство связок рейсов"""
        super().__ne__(other)
        return self.journeys != other.journeys

    def __lt__(self, item):
        """Проверка на превосходство объекта перед связкой рейса"""
        raise IncomparableTypesError(self.compare_message_error)

    def __gt__(self, item):
        """Проверка на превосходство над объектом связка рейсов"""
        raise IncomparableTypesError(self.compare_message_error)

    def __le__(self, other):
        """Проверка на непревосходство над объектом связка рейсов"""
        raise IncomparableTypesError(self.compare_message_error)

    def __ge__(self, other):
        """Проверка на непревосходство объекта перед связкой рейсов"""
        raise IncomparableTypesError(self.compare_message_error)

    def __contains__(self, item):
        """Проверка на принадлежность объекта к связке рейсов"""
        if isinstance(item, BhJourneyBunchItem):
            return item in self.journeys
        elif isinstance(item, BhJourney):
            journeys = [i.journey for i in self.journeys]
            return item in journeys

        raise IncomparableTypesError(
            f"Для объекта {item} недопустима проверка на вхождение в связку рейсов"
        )
