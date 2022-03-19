from typing import Any, Dict, Optional, Sequence, TypeVar, cast
from . import teamlike
from ...sportsdataio_meta import SportsDataIOMetalike
import redis
import json
import datetime

import requests


T = TypeVar("T")


def from_int(x: Any) -> int:
    return x


def from_bool(x: Any) -> bool:
    return x


def from_str(x: Any) -> str:
    return x


def from_none(x: Any) -> Any:
    return x


def from_float(x: Any) -> float:
    if not x:
        return x
    return float(x)


def to_float(x: Any) -> float:
    return x


def to_class(c: Any, x: Any) -> dict[Any, Any]:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Stadium(teamlike.Stadiumlike):
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

    def __init__(self, stadium_id: int, active: bool, name: str, address: None, city: str, state: str, zip: None, country: None, capacity: int, geo_lat: float, geo_long: float) -> None:
        self.stadium_id = stadium_id
        self.active = active
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.capacity = capacity
        self.geo_lat = geo_lat
        self.geo_long = geo_long

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> 'Stadium':
        stadium_id = from_int(obj.get("StadiumID"))
        active = from_bool(obj.get("Active"))
        name = from_str(obj.get("Name"))
        address = from_none(obj.get("Address"))
        city = from_str(obj.get("City"))
        state = from_str(obj.get("State"))
        zip = from_none(obj.get("Zip"))
        country = from_none(obj.get("Country"))
        capacity = from_int(obj.get("Capacity"))
        geo_lat = from_float(obj.get("GeoLat"))
        geo_long = from_float(obj.get("GeoLong"))
        return Stadium(stadium_id, active, name, address, city, state, zip, country, capacity, geo_lat, geo_long)

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        result["StadiumID"] = from_int(self.stadium_id)
        result["Active"] = from_bool(self.active)
        result["Name"] = from_str(self.name)
        result["Address"] = from_none(self.address)
        result["City"] = from_str(self.city)
        result["State"] = from_str(self.state)
        result["Zip"] = from_none(self.zip)
        result["Country"] = from_none(self.country)
        result["Capacity"] = from_int(self.capacity)
        result["GeoLat"] = to_float(self.geo_lat)
        result["GeoLong"] = to_float(self.geo_long)
        return result


class Team(teamlike.Teamlike):
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
    stadium: Stadium

    def __init__(self, team_id: int, key: str, active: bool, school: str, name: str, ap_rank: None, wins: int, losses: int, conference_wins: int, conference_losses: int, global_team_id: int, conference_id: int, conference: str, team_logo_url: str, short_display_name: str, stadium: Stadium) -> None:
        self.team_id = team_id
        self.key = key
        self.active = active
        self.school = school
        self.name = name
        self.ap_rank = ap_rank
        self.wins = wins
        self.losses = losses
        self.conference_wins = conference_wins
        self.conference_losses = conference_losses
        self.global_team_id = global_team_id
        self.conference_id = conference_id
        self.conference = conference
        self.team_logo_url = team_logo_url
        self.short_display_name = short_display_name
        self.stadium = stadium

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> 'Team':
        team_id = from_int(obj.get("TeamID"))
        key = from_str(obj.get("Key"))
        active = from_bool(obj.get("Active"))
        school = from_str(obj.get("School"))
        name = from_str(obj.get("Name"))
        ap_rank = from_none(obj.get("ApRank"))
        wins = from_int(obj.get("Wins"))
        losses = from_int(obj.get("Losses"))
        conference_wins = from_int(obj.get("ConferenceWins"))
        conference_losses = from_int(obj.get("ConferenceLosses"))
        global_team_id = from_int(obj.get("GlobalTeamID"))
        conference_id = from_int(obj.get("ConferenceID"))
        conference = from_str(obj.get("Conference"))
        team_logo_url = from_str(obj.get("TeamLogoUrl"))
        short_display_name = from_str(obj.get("ShortDisplayName"))
        stadium = Stadium.from_dict(obj.get("Stadium") or {})
        return Team(team_id, key, active, school, name, ap_rank, wins, losses, conference_wins, conference_losses, global_team_id, conference_id, conference, team_logo_url, short_display_name, stadium)

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        result["TeamID"] = from_int(self.team_id)
        result["Key"] = from_str(self.key)
        result["Active"] = from_bool(self.active)
        result["School"] = from_str(self.school)
        result["Name"] = from_str(self.name)
        result["ApRank"] = from_none(self.ap_rank)
        result["Wins"] = from_int(self.wins)
        result["Losses"] = from_int(self.losses)
        result["ConferenceWins"] = from_int(self.conference_wins)
        result["ConferenceLosses"] = from_int(self.conference_losses)
        result["GlobalTeamID"] = from_int(self.global_team_id)
        result["ConferenceID"] = from_int(self.conference_id)
        result["Conference"] = from_str(self.conference)
        result["TeamLogoUrl"] = from_str(self.team_logo_url)
        result["ShortDisplayName"] = from_str(self.short_display_name)
        result["Stadium"] = to_class(Stadium, self.stadium)
        return result


def team_from_dict(s: Any) -> Team:
    return Team.from_dict(s)

class TeamsById(teamlike.TeamsByIdlike):

    expiration : int = 3600000

    r : redis.Redis = redis.Redis(host='localhost', port=6379, db=1)

    def __init__(self, meta : SportsDataIOMetalike):
        self.meta=meta

    def find_team(self, id : str, seq : Sequence[Dict[str, Any]])->Dict[str, Any]:
        for team in seq:
            if team["TeamID"] == id:
                return team
        return {}

    def redis_entry_expired(self, entry : Dict[str, Any])->bool:
        """Checks if the redis entry has expired.

        Args:
            entry (Dict[str, Any]): _description_

        Returns:
            bool: _description_
        """
        if not entry["updated"]:
            return True
        return (datetime.datetime.today().timestamp() - float(entry["updated"])) > self.expiration

    def get_team_from_redis(self, id : str)->Optional[teamlike.Teamlike]:
        """Gets a team from the redis cache.

        Args:
            id (str): _description_

        Returns:
            Optional[teamlike.Teamlike]: _description_
        """
        entry : str = self.r.get(id)
        if not entry:
            return None
        entry_json = json.loads(entry)
        if self.redis_entry_expired(entry_json):
            return None
        return Team.from_dict(entry_json["team"])
    

    def update_redis(self):
        """Updates the redis cache with the teams provided from sportsdata.
        """
        teams = requests.get(
            f"{self.meta.domain}/v3/cbb/scores/json/teams",
            params={
                "key" : self.meta.key
            }
        ).json()
        for team in teams:
            self.r.set(team["TeamID"], json.dumps({
                "updated" : datetime.datetime.today().timestamp(),
                "team" : team
            }))

    def get_teams(self):
        return [
            team_from_dict(team)
            for team in requests.get(
            f"{self.meta.domain}/v3/cbb/scores/json/teams",
            params={
                "key" : self.meta.key
            }
        ).json()]

    def get_team(self, id: str) -> Optional[teamlike.Teamlike]:
        """Gets a team. Returns none if one matching the provided ID does not exist.

        Args:
            id (str): the team's id.

        Returns:
            Optional[teamlike.Teamlike]: _description_
        """
        if not self.get_team_from_redis(id):
            self.update_redis()
        return self.get_team_from_redis(id)