from dataclasses import dataclass
from typing import Protocol

from atoti_core import keyword_only_dataclass
from typeguard import typeguard_ignore


class _GetCapacity(Protocol):
    def __call__(self, *, cube_name: str) -> int:
        ...


class _SetCapacity(Protocol):
    def __call__(self, capacity: int, *, cube_name: str) -> None:
        ...


@keyword_only_dataclass
@typeguard_ignore
@dataclass
class AggregatesCache:
    """The aggregates cache associated with a cube."""

    _cube_name: str
    _set_capacity: _SetCapacity
    _get_capacity: _GetCapacity

    @property
    def capacity(self) -> int:
        """Capacity of the cache.

        It is the number of ``{location: measure}`` pairs of all the aggregates that can be stored.

        A strictly negative value will disable caching.

        A zero value will enable sharing but no caching.
        This means that queries will share their computations if they are executed at the same time, but the aggregated values will not be stored to be retrieved later.
        """
        return self._get_capacity(cube_name=self._cube_name)

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        """Capacity setter."""
        self._set_capacity(cube_name=self._cube_name, capacity=capacity)
