# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register("A006564")
def icosahedral() -> Iterable[int]:
    """Icoseahedral numbers."""
    for n in count(start=1):
        yield (n * (5 * (n**2) - (5 * n) + 2)) // 2
