from dataclasses import dataclass
from typing import Iterable, Union

from typing_extensions import final

from .state import Loc


@dataclass
@final
class Skip:
    count: int


@dataclass
@final
class Insert:
    label: str


RepairOp = Union[Skip, Insert]


@dataclass
class OpItem:
    op: RepairOp
    loc: Loc
    expected: Iterable[str]
    consumed: bool
