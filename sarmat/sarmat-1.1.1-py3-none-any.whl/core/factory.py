"""
Sarmat.

Ядро пакета.

Фабрика классов.
"""
from __future__ import absolute_import

from collections import defaultdict
from itertools import chain
from typing import Any, List
from uuid import uuid4

from sarmat.core.actions import (
    ADestinationPoint,
    AGeoLocation,
    AJourney,
    AJourneyBunch,
    ARoute,
    AStation,
)
from sarmat.core.behavior import (
    BhCrew,
    BhDestinationPoint,
    BhDirection,
    BhGeo,
    BhPeriod,
    BhPeriodItem,
    BhPermit,
    BhRoad,
    BhRoadName,
    BhRoute,
    BhRouteItem,
    BhStation,
    BhJourney,
    BhJourneyBunch,
    BhJourneyBunchItem,
    BhVehicle,
    NoActionBehavior,
)
from sarmat.core.containers import (
    CrewStructure,
    DestinationPointStructure,
    DirectionStructure,
    GeoStructure,
    PeriodItemStructure,
    PeriodStructure,
    PermitStructure,
    RoadStructure,
    RoadNameStructure,
    RouteStructure,
    RouteItemStructure,
    StationStructure,
    JourneyBunchStructure,
    JourneyBunchItemStructure,
    JourneyStructure,
    VehicleStructure,
)


class SarmatCreator:
    """Класс реализует паттерн "Фабричный метод", создает классы с реализованной в них логикой"""

    # хранилище тегов
    role_tags = defaultdict(list)

    @classmethod
    def register_class(cls, tag: str, cls_behavior: Any) -> None:
        """
        Регистрация поведенческого класса
        Args:
            tag: тэг
            cls_behavior: поведенческий класс
        """
        sub_tags = tag.split('.')

        for sub_tag in sub_tags:
            classes = cls.role_tags[sub_tag]

            if classes and cls_behavior in classes:
                idx = classes.index(cls_behavior)
                cls.role_tags[sub_tag][idx] = cls_behavior
            else:
                cls.role_tags[sub_tag].append(cls_behavior)

    def _get_behavior_classes(self, tag: str) -> List[Any]:
        """Получение списка поведенческих классов по тегу"""
        sub_tags = tag.split('.')

        roles = []
        for item in sub_tags:
            roles += self.role_tags.get(item) or []

        return roles or [NoActionBehavior]

    def create_direction(self, tag: str, **kwargs):
        """Создание объекта 'Направления'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhDirection], classes, [DirectionStructure])

        Direction = type('Direction', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return Direction(**kwargs)

    def create_destination_point(self, tag: str, **kwargs):
        """Создание объекта 'Пункт назначения'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([ADestinationPoint, BhDestinationPoint], classes, [DestinationPointStructure])

        DestinationPointObject = type(
            'DestinationPointObject',
            tuple(parents),
            {"permission_tag": tag, "controller": self},
        )

        if kwargs['state']:
            kwargs['state'] = self.create_geo_object(tag, **kwargs['state'])

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return DestinationPointObject(**kwargs)

    def create_geo_object(self, tag: str, **kwargs):
        """Создание объекта 'Географическая точка'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([AGeoLocation, BhGeo], classes, [GeoStructure])

        GeoObject = type('GeoObject', tuple(parents), {"permission_tag": tag, "controller": self})

        parent = kwargs.get('parent')
        if parent:
            kwargs['parent'] = self.create_geo_object(tag, **parent)

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return GeoObject(**kwargs)

    def create_road_name(self, tag: str, **kwargs):
        """Создание объекта 'Описание дороги'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhRoadName], classes, [RoadNameStructure])

        RoadName = type('RoadName', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return RoadName(**kwargs)

    # TODO: по контейнерам создать базовые поведенческие классы
    # JourneyProgressStructure, JourneyScheduleStructure, IntervalStructure

    def create_route_item(self, tag: str, **kwargs):
        """Создание объекта 'Пункт маршрута'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhRouteItem], classes, [RouteItemStructure])

        RouteItem = type('RouteItem', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0
        if kwargs.get('road'):
            kwargs['road'] = self.create_road(tag, **kwargs['road'])
        if kwargs.get('station'):
            kwargs['station'] = self.create_station(tag, **kwargs['station'])
        if kwargs.get('point'):
            kwargs['point'] = self.create_destination_point(tag, **kwargs['point'])

        return RouteItem(**kwargs)

    def create_route(self, tag: str, **kwargs):
        """Создание объекта 'Маршрут'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([ARoute, BhRoute], classes, [RouteStructure])

        Route = type('Route', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0
        if kwargs.get('first_station'):
            kwargs['first_station'] = self.create_station(tag, **kwargs['first_station'])
        if kwargs.get('structure'):
            kwargs['structure'] = [self.create_route_item(tag, **item) for item in kwargs['structure']]
        if kwargs.get('direction'):
            kwargs['direction'] = [self.create_direction(tag, **item) for item in kwargs['direction']]

        return Route(**kwargs)

    def create_station(self, tag: str, **kwargs):
        """Создание объекта 'Станция'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([AStation, BhStation], classes, [StationStructure])

        Station = type('Station', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        if kwargs.get('point'):
            kwargs['point'] = self.create_destination_point(tag, **kwargs['point'])

        return Station(**kwargs)

    def create_journey(self, tag: str, **kwargs):
        """Создание объекта 'Рейс'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([AJourney, BhJourney], classes, [JourneyStructure])

        Journey = type('journey', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0
        if kwargs.get('first_station'):
            kwargs['first_station'] = self.create_station(tag, **kwargs['first_station'])
        if kwargs.get('structure'):
            kwargs['structure'] = [self.create_route_item(tag, **item) for item in kwargs['structure']]
        if kwargs.get('direction'):
            kwargs['direction'] = [self.create_direction(tag, **item) for item in kwargs['direction']]

        return Journey(**kwargs)

    def create_road(self, tag: str, **kwargs):
        """Создание объекта 'Дорога'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhRoad], classes, [RoadStructure])

        Road = type('Road', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0
        if kwargs.get('start_point'):
            kwargs['start_point'] = self.create_destination_point(tag, **kwargs['start_point'])
        if kwargs.get('end_point'):
            kwargs['end_point'] = self.create_destination_point(tag, **kwargs['end_point'])
        if kwargs.get('road'):
            kwargs['road'] = self.create_road_name(tag, **kwargs['road'])

        return Road(**kwargs)

    def create_journey_bunch_item(self, tag: str, **kwargs):
        """Создание объекта 'Элемент связки'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhJourneyBunchItem], classes, [JourneyBunchItemStructure])

        JourneyBunchItem = type('JourneyBunchItem', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0
        if kwargs.get('journey'):
            kwargs['journey'] = self.create_journey(tag, **kwargs['journey'])

        return JourneyBunchItem(**kwargs)

    def create_journey_bunch(self, tag: str, **kwargs):
        """Создание объекта 'Связка рейсов'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([AJourneyBunch, BhJourneyBunch], classes, [JourneyBunchStructure])

        JourneyBunch = type('JourneyBunch', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0
        if kwargs.get('journeys'):
            kwargs['journeys'] = [self.create_journey_bunch_item(tag, **i) for i in kwargs['journeys']]

        return JourneyBunch(**kwargs)

    def create_period_item(self, tag: str, **kwargs):
        """Создание объекта 'Период'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhPeriodItem], classes, [PeriodItemStructure])

        PeriodItem = type('PeriodItem', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return PeriodItem(**kwargs)

    def create_period(self, tag: str, **kwargs):
        classes = self._get_behavior_classes(tag)
        parents = chain([BhPeriod], classes, [PeriodStructure])

        Period = type('Period', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        if kwargs.get('period'):
            kwargs['period'] = self.create_period_item(tag, **kwargs['period'])

        if kwargs.get('periods'):
            kwargs['periods'] = [self.create_period_item(tag, **item) for item in kwargs['periods']]

        return Period(**kwargs)

    def create_crew(self, tag: str, **kwargs):
        classes = self._get_behavior_classes(tag)
        parents = chain([BhCrew], classes, [CrewStructure])

        Crew = type('Crew', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return Crew(**kwargs)

    def create_permit(self, tag: str, **kwargs):
        """Создание объекта 'Путевой лист'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhPermit], classes, [PermitStructure])

        Permit = type('Permit', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = uuid4()

        if kwargs.get('crew'):
            kwargs['crew'] = [self.create_crew(tag, **item) for item in kwargs['crew']]

        if kwargs.get('vehicle'):
            kwargs['vehicle'] = [self.create_vehicle(tag, **item) for item in kwargs['vehicle']]

        return Permit(**kwargs)

    def create_vehicle(self, tag: str, **kwargs):
        """Создание объекта 'Транспортное средство'"""
        classes = self._get_behavior_classes(tag)
        parents = chain([BhVehicle], classes, [VehicleStructure])

        Vehicle = type('Vehicle', tuple(parents), {"permission_tag": tag, "controller": self})

        if kwargs.get('id') is None:
            kwargs['id'] = 0

        return Vehicle(**kwargs)
