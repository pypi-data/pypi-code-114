import abc
from typing import Any, Dict, Protocol, Optional, Sequence
from ...sportsdataio_meta import SportsDataIOMetalike

class Stadiumlike(Protocol):
    stadium_id: int
    active: bool
    name: str
    address: None
    city: str
    state: str
    zip: None
    country: None
    capacity: int
    geo_lat: float
    geo_long: float

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, obj: Dict[str, Any]) -> 'Stadiumlike':
        pass

    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass


class Teamlike:
    team_id: int
    key: str
    active: bool
    school: str
    name: str
    ap_rank: None
    wins: int
    losses: int
    conference_wins: int
    conference_losses: int
    global_team_id: int
    conference_id: int
    conference: str
    team_logo_url: str
    short_display_name: str
    stadium: Stadiumlike

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, obj: Dict[str, Any]) -> 'Teamlike':
        pass

    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass


class TeamsByIdlike(Protocol):

    meta : SportsDataIOMetalike

    @abc.abstractmethod
    def get_team(self, id : str) -> Optional[Teamlike]:
        pass

    @abc.abstractmethod
    def get_teams(self) -> Sequence[Teamlike]:
        pass
