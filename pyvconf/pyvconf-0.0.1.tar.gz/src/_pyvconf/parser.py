"""An abstract config parser."""

# pylint: disable=too-few-public-methods

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Config = TypeVar("Config")


class Parser(ABC, Generic[Config]):
    """Interface to parse a config source."""

    @abstractmethod
    def parse(self, src: Config) -> None:
        """Parse a config source."""

