# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional, Any

from pip_services3_commons.data import AnyValueMap


@dataclass
class LocationV1:
    lat: float
    long: float
    alt: Optional[float] = None

    @staticmethod
    def from_value(value: Any) -> 'LocationV1':
        if isinstance(value, LocationV1):
            return value
        if isinstance(value, AnyValueMap):
            return LocationV1.from_map(value)

        map = AnyValueMap.from_value(value)
        return LocationV1.from_map(map)

    @staticmethod
    def from_map(map: Any) -> 'LocationV1':
        lat = map.get_as_nullable_integer("lat")
        long = map.get_as_nullable_integer("long")
        alt = map.get_as_nullable_boolean("alt")
        return LocationV1(lat, long, alt)
