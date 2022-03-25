from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from .bitwise_operators_only import Identity
from .keyword_only_dataclass import keyword_only_dataclass


@keyword_only_dataclass
# See https://github.com/python/mypy/issues/5374.
@dataclass  # type: ignore[misc]
class BaseMeasure(ABC):
    """Measure of a base cube."""

    _name: str

    @property
    def name(self) -> str:
        """Name of the measure."""
        return self._name

    @property
    @abstractmethod
    def folder(self) -> Optional[str]:
        """Folder of the measure."""

    @property
    @abstractmethod
    def visible(self) -> bool:
        """Whether the measure is visible or not."""

    @property
    @abstractmethod
    def description(self) -> Optional[str]:
        """Description of the measure."""

    @property
    @abstractmethod
    def formatter(self) -> Optional[str]:
        """Formatter of the measure."""

    @property
    def _identity(self) -> Identity:
        return (self.name,)
