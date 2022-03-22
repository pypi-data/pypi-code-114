"""
Sarmat.

Описание действий с объектами.

Классы для работы с объектами маршрутной сети.
"""
from __future__ import absolute_import

from collections import namedtuple
from copy import deepcopy
from datetime import date, datetime, time, timedelta

from sarmat.core.containers import JourneyStructure, RouteStructure, JourneyBunchItemStructure
from sarmat.core.constants import JourneyType
from sarmat.core.constants.sarmat_constants import MAX_SUBURBAN_ROUTE_LENGTH
from sarmat.core.exceptions import WrongValueError
from sarmat.tools.geo_tools import get_geo_objects_projection
from sarmat.core.verification import (
    JourneyBunchItemVerifier,
    JourneyBunchVerifier,
    JourneyVerifier,
    RouteVerifier,
    StationVerifier,
)

from .bases import Action

RouteMetrics = namedtuple("RouteMetrics", "point station arrive stop depart length total_length spent_time")


class AStation(Action):
    """Действия с пунктами назначения"""

    verification_class = StationVerifier

    def copy(self):
        return self.__class__(
            id=0,
            station_type=self.station_type,
            name=f"Копия {self.name}",
            point=self.point,
            address=self.address,
        )


class RouteMixin:
    """Миксин для использования при работе с маршрутами и рейсами"""

    def get_real_journey_type(self) -> JourneyType:
        """Метод возвращает вычисленный тип рейса"""
        route_length = 0

        region_changed, country_changed = False, False
        _, base_region, base_country = get_geo_objects_projection(self.first_station.point.state)
        for route_item in self.structure:
            item_state = route_item.station.point.state if route_item.station else route_item.point.state
            _, item_region, item_country = get_geo_objects_projection(item_state)

            if base_region and item_region:
                region_changed = base_region != item_region
            if base_country and item_country:
                country_changed = base_country != item_country

            if region_changed or country_changed:
                break
            route_length += route_item.length_from_last_km

        if country_changed:
            journey_type = JourneyType.INTERNATIONAL
        elif region_changed:
            journey_type = JourneyType.INTER_REGIONAL
        elif route_length >= MAX_SUBURBAN_ROUTE_LENGTH:
            journey_type = JourneyType.LONG_DISTANCE
        else:
            journey_type = JourneyType.SUBURBAN

        return journey_type

    def get_route_metrics(self):
        """Метрика состава маршрута"""
        now = self.get_base_depart_date_time()
        route_length = 0
        spent_time_in_minutes = 0

        for item in self.structure[:-1]:
            spent_time_in_minutes += item.travel_time_min
            spent_time_in_minutes += (item.stop_time_min or 0)
            now += timedelta(minutes=item.travel_time_min)
            depart_delta = timedelta(minutes=item.stop_time_min or 0)
            route_length += item.length_from_last_km
            if item.station:
                point_name, station_name = item.station.point.name, item.station.name
            else:
                point_name, station_name = item.point.name, ""

            yield RouteMetrics(
                point_name,
                station_name,
                now.strftime("%H:%M"),
                item.stop_time_min,
                (now + depart_delta).strftime("%H:%M"),
                item.length_from_last_km,
                route_length,
                spent_time_in_minutes,
            )
            now += depart_delta

        last_item = self.structure[-1]
        route_length += last_item.length_from_last_km
        spent_time_in_minutes += last_item.travel_time_min
        now += timedelta(minutes=last_item.travel_time_min)

        if last_item.station:
            point_name, station_name = last_item.station.point.name, last_item.station.name
        else:
            point_name, station_name = last_item.point.name, ""

        yield RouteMetrics(
            point_name,
            station_name,
            now.strftime("%H:%M"),
            0,
            None,
            last_item.length_from_last_km,
            route_length,
            spent_time_in_minutes,
        )


class ARoute(RouteMixin, Action):
    """Действия с маршрутом"""

    verification_class = RouteVerifier

    def copy(self):
        return self.__class__(
            id=0,
            name=f"Копия {self.name}",
            first_station=self.first_station,
            structure=deepcopy(self.structure),
            direction=deepcopy(self.direction) if self.direction else None,
            comments=self.comments,
            number=0,
            literal="",
        )

    def create_journey_structure(self, departure_time: time) -> JourneyStructure:
        return JourneyStructure(
            id=0,
            number=self.number,
            name=self.name,
            first_station=self.first_station,
            structure=self.structure,
            journey_type=self.get_real_journey_type(),
            departure_time=departure_time,
            bunch=None,
            literal="",
            is_chartered=False,
            need_control=False,
            season_begin=None,
            season_end=None,
            direction=self.direction,
            comments=f"Создан из маршрута {self.number} ({self.id})",
        )

    def get_route_info(self) -> dict:
        """Информация о маршруте"""
        return {
            "attributes": self.as_dict(),
            "real_journey_type": self.get_real_journey_type(),
            "route_structure": [item.as_dict() for item in self.structure],
            "metrics": self.get_route_metrics(),
        }

    def get_base_depart_date_time(self) -> datetime:
        today = date.today()
        return datetime(today.year, today.month, today.day, 0, 0)


class AJourney(RouteMixin, Action):
    """Действия с рейсами"""

    verification_class = JourneyVerifier

    def copy(self):
        return self.__class__(
            id=0,
            number=0,
            name=f"Копия {self.name}",
            first_station=self.first_station,
            structure=self.structure,
            journey_type=self.journey_type,
            departure_time=self.departure_time,
            bunch=self.bunch,
            literal="",
            is_chartered=self.is_chartered,
            need_control=self.need_control,
            season_begin=self.season_begin,
            season_end=self.season_end,
            direction=self.direction,
            comments=f"Создан из рейса {self.number} ({self.id})",
        )

    def get_base_depart_date_time(self) -> datetime:
        today = date.today()
        return datetime(today.year, today.month, today.day, self.departure_time.hour, self.departure_time.minute)

    def get_journey_info(self) -> dict:
        """Информация о рейсе"""
        return {
            "attributes": self.as_dict(),
            "real_journey_type": self.get_real_journey_type(),
            "route_structure": [item.as_dict() for item in self.structure],
            "metrics": self.get_route_metrics(),
        }

    def create_route_structure(self) -> RouteStructure:
        return RouteStructure(
            id=0,
            name=self.name,
            first_station=self.first_station,
            structure=self.structure,
            direction=self.direction,
            comments=f"Создан из рейса {self.number} ({self.id})",
            number=self.number,
            literal="",
        )


class AJourneyBunch(Action):
    """Действия со связкой рейсов"""

    verification_class = JourneyBunchVerifier
    bunch_item_verifier = JourneyBunchItemVerifier()

    def add_journey_bunch_item(self, bunch_item: JourneyBunchItemStructure) -> None:
        self.bunch_item_verifier.verify(bunch_item)

        if bunch_item in self:
            raise WrongValueError("Item already in bunch")

        if bunch_item.journey in self:
            raise WrongValueError("Journey already in bunch")

        self.journeys.append(bunch_item)

    def add_journey_into_bunch(self, journey: JourneyStructure, stop_interval: int = 0) -> None:
        new_bunch_item = self.controller.create_journey_bunch_item(
            self.permission_tag,
            journey=journey.as_dict(),
            stop_interval=stop_interval,
        )
        self.add_journey_bunch_item(new_bunch_item)

    def remove_journey_bunch_item(self, bunch_item_id: int) -> None:
        if self.journeys:
            for idx, bunch_item in enumerate(self.journeys):
                if bunch_item.id == bunch_item_id:
                    self.journeys.remove(self.journeys[idx])
                    break
            else:
                raise WrongValueError(
                    f"Journey bunch item {bunch_item_id}) is not in bunch",
                )
        else:
            raise WrongValueError("Journey bunch is empty")

    def get_finish_date_time(self, date_from: datetime) -> datetime:
        for item in self.journeys:
            journey = self.controller.create_journey(self.permission_tag, **item.journey.as_dict())
            route_metrics = list(journey.get_journey_info()["metrics"])
            journey_spent_time = route_metrics[-1].spent_time
            date_from += timedelta(minutes=journey_spent_time)

            if item.stop_interval:
                date_from += timedelta(hours=item.stop_interval)

        return date_from
