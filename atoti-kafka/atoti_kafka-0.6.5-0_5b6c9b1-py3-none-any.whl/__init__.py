"""Plugin to load real time Kafka streams into atoti tables.

This package is required to use :meth:`atoti.Table.load_kafka`.
"""


from ._custom import create_deserializer as create_deserializer
from .deserializer import *
