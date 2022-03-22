# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_quasiperfect


@registry.register("A088831")
def quasiperfect() -> Iterable[int]:
    """Quasiperfect numbers."""
    for n in count(start=1):
        if is_quasiperfect(n):
            yield n
