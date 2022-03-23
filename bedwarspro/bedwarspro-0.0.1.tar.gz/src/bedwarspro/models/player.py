from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from .. import utils

RankType = Literal[
    'DEFAULT',
    'PRO',
    'YOUTUBE',
    'ADMIN',
    'OWNER',
]


@dataclass
class Player:
    """Player model object. """
    raw: dict = field(repr=False)

    name: str = None
    uuid: str = None

    rank: RankType = None

    first_login: datetime = None

    def __post_init__(self):
        self.rank = utils.get_rank(self.raw)
        self.first_login = utils.convert_to_datetime(self.raw.get('firstLogin'))
        self.name = self.raw.get('name')
        self.uuid = self.raw.get('uuid')
