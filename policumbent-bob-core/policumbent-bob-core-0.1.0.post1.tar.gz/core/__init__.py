import re

from .alert import AlertPriority
from .bikeData import BikeData
from .common_settings import CommonSettings
from .message import Message
from .mqtt import Mqtt
from .sensor import Sensor
from .weatherData import WeatherData


__all__ = [
    # module import
    'alert',
    'bikeData',
    'common_settings',
    'message',
    'mqtt',
    'sensor',
    'weatherData',

    # class import 
    'AlertPriority',
    'BikeData',
    'CommonSettings',
    'Message',
    'Mqtt',
    'Sensor',
    'WeatherData',
]


try:
    with open('pyproject.toml', 'r') as f:
        __version__ = re.search(r'^version\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
except FileNotFoundError:
    __version__ = "0.1.0"