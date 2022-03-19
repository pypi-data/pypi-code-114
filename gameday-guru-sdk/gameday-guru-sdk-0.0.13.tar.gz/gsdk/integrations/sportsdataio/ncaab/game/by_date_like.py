import abc
from typing import Dict, Any, List, Protocol
from datetime import datetime

from gsdk.integrations.sportsdataio.sportsdataio_meta import SportsDataIOMetalike

class Periodlike(Protocol):
    period_id: int
    game_id: int
    number: int
    name: int
    type: str
    away_score: int
    home_score: int

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, obj: object) -> 'Periodlike':
        """Creates a Periodlike object from a dictionary.

        Args:
            obj (object): is an object which is can be interpretted as a Periodlike

        Returns:
            Periodlike: a Periodlike object.
        """
        pass
    
    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

class GameByDatelike:
    game_id: int
    season: int
    season_type: int
    status: str
    day: datetime
    date_time: datetime
    away_team: str
    home_team: str
    away_team_id: int
    home_team_id: int
    away_team_score: int
    home_team_score: int
    updated: datetime
    period: str
    time_remaining_minutes: None
    time_remaining_seconds: None
    point_spread: float
    over_under: float
    away_team_money_line: int
    home_team_money_line: int
    global_game_id: int
    global_away_team_id: int
    global_home_team_id: int
    tournament_id: None
    bracket: None
    round: None
    away_team_seed: None
    home_team_seed: None
    away_team_previous_game_id: None
    home_team_previous_game_id: None
    away_team_previous_global_game_id: None
    home_team_previous_global_game_id: None
    tournament_display_order: None
    tournament_display_order_for_home_team: str
    is_closed: bool
    game_end_date_time: datetime
    home_rotation_number: None
    away_rotation_number: None
    top_team_previous_game_id: None
    bottom_team_previous_game_id: None
    channel: None
    neutral_venue: None
    away_point_spread_payout: None
    home_point_spread_payout: None
    over_payout: None
    under_payout: None
    date_time_utc: datetime
    stadium: None
    periods: List[Periodlike]

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, obj: Any) -> 'GameByDatelike':
        pass

    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

class GamesByDatelike(Protocol):
    """Driver class for getting games by date.
    """
    meta : SportsDataIOMetalike

    def __init__(self, meta : SportsDataIOMetalike) -> None:
        pass

    @abc.abstractmethod
    def get_games(cls, date : datetime) -> List['GameByDatelike']:
        pass