from enum import Enum as _Enum
from typing import NamedTuple as _NamedTuple
from ._classes import Number as _Number


class _Units(_NamedTuple):
    temp: tuple[str, str] = ("K", "Kelvin")
    speed: tuple[str, str] = ("m/s", "meter/sec")

    time = ("unix", "UTC")
    pressure = "hPa"
    cloudiness = "%"
    precipitation = ("mm", "millimeters")
    degrees = ("°", "degrees (meteorological)")


class Units(_Enum):
    STANDARD = _Units()
    METRIC   = _Units(temp=("°C", "Celsius"))
    IMPERIAL = _Units(temp=("°F", "Fahrenheit"), speed=("mph", "miles/hour"))


def convert_temp(temp: _Number, __from: Units = Units.STANDARD, __to: Units = Units.IMPERIAL) -> _Number:
    """Converts temperature between different units"""
    if __from == __to:
        return temp

    match (__from, __to):
        case (Units.STANDARD, Units.METRIC):
            return temp - 273.15
        case (Units.STANDARD, Units.IMPERIAL):
            return 1.8 * (temp - 273.15) + 32
        case (Units.METRIC, Units.STANDARD):
            return temp + 273.15
        case (Units.METRIC, Units.IMPERIAL):
            return 1.8 * temp + 32
        case (Units.IMPERIAL, Units.STANDARD):
            return (temp - 32) * 1.8 + 273.15
        case (Units.IMPERIAL, Units.METRIC):
            return (temp - 32) * 1.8
        case _:
            raise NotImplementedError(
                f"Conversion between types '{__from.__class__}' and '{__to.__class__}' is not defined"
            )


_MPS_PER_MPH = 0.44704


def convert_speed(speed: _Number, __from: Units = Units.STANDARD, __to: Units = Units.IMPERIAL) -> _Number:
    if __from in {Units.STANDARD, Units.METRIC} and __to in {Units.STANDARD, Units.METRIC}:
        return speed

    match (__from, __to):
        case (Units.STANDARD | Units.METRIC, Units.IMPERIAL):
            return speed / _MPS_PER_MPH
        case (Units.IMPERIAL, Units.STANDARD | Units.METRIC):
            return _MPS_PER_MPH * speed
        case _:
            raise NotImplementedError(
                f"Conversion between types '{__from.__class__}' and '{__to.__class__}' is not defined"
            )
