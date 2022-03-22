# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register("A093069")
def kynea() -> Iterable[int]:
    """Kynea numbers."""
    for n in count(start=1):
        yield pow(pow(2, n) + 1, 2) - 2
