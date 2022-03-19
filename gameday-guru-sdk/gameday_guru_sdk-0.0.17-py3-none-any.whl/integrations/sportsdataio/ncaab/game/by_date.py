
from typing import Any, List, TypeVar, Callable, cast, Dict
from datetime import datetime
import dateutil.parser
from ...sportsdataio_meta import SportsDataIOMetalike
import requests
from . import by_date_like


T = TypeVar("T")


def from_int(x: Any) -> int:
    return x


def from_str(x: Any) -> str:
    return x


def from_datetime(x: Any) -> datetime:
    if not x:
        return datetime.today()
    return dateutil.parser.parse(x)


def from_none(x: Any) -> Any:
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in cast(List[Any], x)]


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Any, x: Any) -> Dict[Any, Any]:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()

class Period(by_date_like.Periodlike):

    def __init__(self, period_id: int, game_id: int, number: int, name: str, type: str, away_score: int, home_score: int) -> None:
        self.period_id = period_id
        self.game_id = game_id
        self.number = number
        self.name = name
        self.type = type
        self.away_score = away_score
        self.home_score = home_score

    @classmethod
    def from_dict(cls, obj: object) -> 'Period':
        assert isinstance(obj, dict)
        period_id = from_int(obj["PeriodID"])
        game_id = from_int(obj["GameID"])
        number = from_int(obj["Number"])
        name : str = obj["Name"]
        type = from_str(obj["Type"])
        away_score = from_int(obj["AwayScore"])
        home_score = from_int(obj["HomeScore"])
        return Period(period_id, game_id, number, name, type, away_score, home_score)

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        result["PeriodID"] = from_int(self.period_id)
        result["GameID"] = from_int(self.game_id)
        result["Number"] = from_int(self.number)
        result["Name"] = from_str(self.name)
        result["Type"] = from_str(self.type)
        result["AwayScore"] = from_int(self.away_score)
        result["HomeScore"] = from_int(self.home_score)
        return result


class GameByDate(by_date_like.GameByDatelike):

    def __init__(self, game_id: int, season: int, season_type: int, status: str, day: datetime, date_time: datetime, away_team: str, home_team: str, away_team_id: int, home_team_id: int, away_team_score: int, home_team_score: int, updated: datetime, period: str, time_remaining_minutes: None, time_remaining_seconds: None, point_spread: float, over_under: float, away_team_money_line: int, home_team_money_line: int, global_game_id: int, global_away_team_id: int, global_home_team_id: int, tournament_id: None, bracket: None, round: None, away_team_seed: None, home_team_seed: None, away_team_previous_game_id: None, home_team_previous_game_id: None, away_team_previous_global_game_id: None, home_team_previous_global_game_id: None, tournament_display_order: None, tournament_display_order_for_home_team: str, is_closed: bool, game_end_date_time: datetime, home_rotation_number: None, away_rotation_number: None, top_team_previous_game_id: None, bottom_team_previous_game_id: None, channel: None, neutral_venue: None, away_point_spread_payout: None, home_point_spread_payout: None, over_payout: None, under_payout: None, date_time_utc: datetime, stadium: None, periods: List[by_date_like.Periodlike]) -> None:
        self.game_id = game_id
        self.season = season
        self.season_type = season_type
        self.status = status
        self.day = day
        self.date_time = date_time
        self.away_team = away_team
        self.home_team = home_team
        self.away_team_id = away_team_id
        self.home_team_id = home_team_id
        self.away_team_score = away_team_score
        self.home_team_score = home_team_score
        self.updated = updated
        self.period = period
        self.time_remaining_minutes = time_remaining_minutes
        self.time_remaining_seconds = time_remaining_seconds
        self.point_spread = point_spread
        self.over_under = over_under
        self.away_team_money_line = away_team_money_line
        self.home_team_money_line = home_team_money_line
        self.global_game_id = global_game_id
        self.global_away_team_id = global_away_team_id
        self.global_home_team_id = global_home_team_id
        self.tournament_id = tournament_id
        self.bracket = bracket
        self.round = round
        self.away_team_seed = away_team_seed
        self.home_team_seed = home_team_seed
        self.away_team_previous_game_id = away_team_previous_game_id
        self.home_team_previous_game_id = home_team_previous_game_id
        self.away_team_previous_global_game_id = away_team_previous_global_game_id
        self.home_team_previous_global_game_id = home_team_previous_global_game_id
        self.tournament_display_order = tournament_display_order
        self.tournament_display_order_for_home_team = tournament_display_order_for_home_team
        self.is_closed = is_closed
        self.game_end_date_time = game_end_date_time
        self.home_rotation_number = home_rotation_number
        self.away_rotation_number = away_rotation_number
        self.top_team_previous_game_id = top_team_previous_game_id
        self.bottom_team_previous_game_id = bottom_team_previous_game_id
        self.channel = channel
        self.neutral_venue = neutral_venue
        self.away_point_spread_payout = away_point_spread_payout
        self.home_point_spread_payout = home_point_spread_payout
        self.over_payout = over_payout
        self.under_payout = under_payout
        self.date_time_utc = date_time_utc
        self.stadium = stadium
        self.periods = periods

    @classmethod
    def from_dict(cls, obj: Any) -> 'GameByDate':
        assert isinstance(obj, dict)
        game_id = from_int(obj["GameID"])
        season = from_int(obj["Season"])
        season_type = from_int(obj["SeasonType"])
        status = from_str(obj["Status"])
        day = from_datetime(obj["Day"])
        date_time = from_datetime(obj["DateTime"])
        away_team = from_str(obj["AwayTeam"])
        home_team = from_str(obj["HomeTeam"])
        away_team_id = from_int(obj["AwayTeamID"])
        home_team_id = from_int(obj["HomeTeamID"])
        away_team_score = from_int(obj["AwayTeamScore"])
        home_team_score = from_int(obj["HomeTeamScore"])
        updated = from_datetime(obj["Updated"])
        period = from_str(obj["Period"])
        time_remaining_minutes = from_none(obj["TimeRemainingMinutes"])
        time_remaining_seconds = from_none(obj["TimeRemainingSeconds"])
        point_spread = from_float(obj["PointSpread"])
        over_under = from_float(obj["OverUnder"])
        away_team_money_line = from_int(obj["AwayTeamMoneyLine"])
        home_team_money_line = from_int(obj["HomeTeamMoneyLine"])
        global_game_id = from_int(obj["GlobalGameID"])
        global_away_team_id = from_int(obj["GlobalAwayTeamID"])
        global_home_team_id = from_int(obj["GlobalHomeTeamID"])
        tournament_id = from_none(obj["TournamentID"])
        bracket = from_none(obj["Bracket"])
        round = from_none(obj["Round"])
        away_team_seed = from_none(obj["AwayTeamSeed"])
        home_team_seed = from_none(obj["HomeTeamSeed"])
        away_team_previous_game_id = from_none(obj["AwayTeamPreviousGameID"])
        home_team_previous_game_id = from_none(obj["HomeTeamPreviousGameID"])
        away_team_previous_global_game_id = from_none(obj["AwayTeamPreviousGlobalGameID"])
        home_team_previous_global_game_id = from_none(obj["HomeTeamPreviousGlobalGameID"])
        tournament_display_order = from_none(obj["TournamentDisplayOrder"])
        tournament_display_order_for_home_team = from_str(obj["TournamentDisplayOrderForHomeTeam"])
        is_closed = from_bool(obj["IsClosed"])
        game_end_date_time = from_datetime(obj["GameEndDateTime"])
        home_rotation_number = from_none(obj["HomeRotationNumber"])
        away_rotation_number = from_none(obj["AwayRotationNumber"])
        top_team_previous_game_id = from_none(obj["TopTeamPreviousGameId"])
        bottom_team_previous_game_id = from_none(obj["BottomTeamPreviousGameId"])
        channel = from_none(obj["Channel"])
        neutral_venue = from_none(obj["NeutralVenue"])
        away_point_spread_payout = from_none(obj["AwayPointSpreadPayout"])
        home_point_spread_payout = from_none(obj["HomePointSpreadPayout"])
        over_payout = from_none(obj["OverPayout"])
        under_payout = from_none(obj["UnderPayout"])
        date_time_utc = from_datetime(obj["DateTimeUTC"])
        stadium = from_none(obj["Stadium"])
        periods = from_list(Period.from_dict, obj["Periods"])
        return GameByDate(game_id, season, season_type, status, day, date_time, away_team, home_team, away_team_id, home_team_id, away_team_score, home_team_score, updated, period, time_remaining_minutes, time_remaining_seconds, point_spread, over_under, away_team_money_line, home_team_money_line, global_game_id, global_away_team_id, global_home_team_id, tournament_id, bracket, round, away_team_seed, home_team_seed, away_team_previous_game_id, home_team_previous_game_id, away_team_previous_global_game_id, home_team_previous_global_game_id, tournament_display_order, tournament_display_order_for_home_team, is_closed, game_end_date_time, home_rotation_number, away_rotation_number, top_team_previous_game_id, bottom_team_previous_game_id, channel, neutral_venue, away_point_spread_payout, home_point_spread_payout, over_payout, under_payout, date_time_utc, stadium, cast(List[by_date_like.Periodlike], periods))

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        result["GameID"] = from_int(self.game_id)
        result["Season"] = from_int(self.season)
        result["SeasonType"] = from_int(self.season_type)
        result["Status"] = from_str(self.status)
        result["Day"] = self.day.isoformat()
        result["DateTime"] = self.date_time.isoformat()
        result["AwayTeam"] = from_str(self.away_team)
        result["HomeTeam"] = from_str(self.home_team)
        result["AwayTeamID"] = from_int(self.away_team_id)
        result["HomeTeamID"] = from_int(self.home_team_id)
        result["AwayTeamScore"] = from_int(self.away_team_score)
        result["HomeTeamScore"] = from_int(self.home_team_score)
        result["Updated"] = self.updated.isoformat()
        result["Period"] = from_str(self.period)
        result["TimeRemainingMinutes"] = from_none(self.time_remaining_minutes)
        result["TimeRemainingSeconds"] = from_none(self.time_remaining_seconds)
        result["PointSpread"] = to_float(self.point_spread)
        result["OverUnder"] = to_float(self.over_under)
        result["AwayTeamMoneyLine"] = from_int(self.away_team_money_line)
        result["HomeTeamMoneyLine"] = from_int(self.home_team_money_line)
        result["GlobalGameID"] = from_int(self.global_game_id)
        result["GlobalAwayTeamID"] = from_int(self.global_away_team_id)
        result["GlobalHomeTeamID"] = from_int(self.global_home_team_id)
        result["TournamentID"] = from_none(self.tournament_id)
        result["Bracket"] = from_none(self.bracket)
        result["Round"] = from_none(self.round)
        result["AwayTeamSeed"] = from_none(self.away_team_seed)
        result["HomeTeamSeed"] = from_none(self.home_team_seed)
        result["AwayTeamPreviousGameID"] = from_none(self.away_team_previous_game_id)
        result["HomeTeamPreviousGameID"] = from_none(self.home_team_previous_game_id)
        result["AwayTeamPreviousGlobalGameID"] = from_none(self.away_team_previous_global_game_id)
        result["HomeTeamPreviousGlobalGameID"] = from_none(self.home_team_previous_global_game_id)
        result["TournamentDisplayOrder"] = from_none(self.tournament_display_order)
        result["TournamentDisplayOrderForHomeTeam"] = from_str(self.tournament_display_order_for_home_team)
        result["IsClosed"] = from_bool(self.is_closed)
        result["GameEndDateTime"] = self.game_end_date_time.isoformat()
        result["HomeRotationNumber"] = from_none(self.home_rotation_number)
        result["AwayRotationNumber"] = from_none(self.away_rotation_number)
        result["TopTeamPreviousGameId"] = from_none(self.top_team_previous_game_id)
        result["BottomTeamPreviousGameId"] = from_none(self.bottom_team_previous_game_id)
        result["Channel"] = from_none(self.channel)
        result["NeutralVenue"] = from_none(self.neutral_venue)
        result["AwayPointSpreadPayout"] = from_none(self.away_point_spread_payout)
        result["HomePointSpreadPayout"] = from_none(self.home_point_spread_payout)
        result["OverPayout"] = from_none(self.over_payout)
        result["UnderPayout"] = from_none(self.under_payout)
        result["DateTimeUTC"] = self.date_time_utc.isoformat()
        result["Stadium"] = from_none(self.stadium)
        result["Periods"] = from_list(lambda x: to_class(Period, x), self.periods)
        return result



class GamesByDate(by_date_like.GamesByDatelike):

    def __init__(self, meta : SportsDataIOMetalike):
        self.meta=meta

    def get_games(self, date : datetime) -> List[by_date_like.GameByDatelike]:
        json = requests.get(
            f"{self.meta.domain}/v3/cbb/scores/json/GamesByDate/{date.year}-{date.month}-{date.day}",
            params={
                "key" : self.meta.key
            }
        ).json()
        return [GameByDate.from_dict(g) for g in json]