from ... import division
from ... import team
from ..... import integrations
import datetime
from typing import Sequence
from . import models
import redis

class TeamEfficiencyController(team.efficiencylike.Controlleralog):

    r : redis.Redis = redis.Redis(host='localhost', port=6379, db=0)
    key : str
    date : datetime.datetime
    efficiency_meta : models.EfficiencyRedisMeta

    def __init__(self, key : str, date : datetime.datetime = datetime.datetime.today()) -> None:
        self.key = key
        self.efficiency_meta = models.EfficiencyRedisMeta(self.key, self.r)
        self.date = date

    def get(self, efficiency : team.efficiencylike.Efficiencylike, date : datetime.datetime):
        """Populates an efficiency model.

        Args:
            efficiency (team.efficiencylike.Efficiencylike): _description_
        """
        eff = self.efficiency_meta.get_team_efficiency(str(efficiency.team.id), date)
        efficiency.possessions = eff.possessions
        efficiency.kadjoeff = eff.kadjoeff
        efficiency.kadjdeff = eff.kadjdeff
        efficiency.badjoeff = eff.badjoeff
        efficiency.badjdeff = eff.badjdeff
        efficiency.radjoeff = eff.badjdeff

    def serialize(self, efficiency: team.efficiencylike.Efficiencylike, date : datetime.datetime) -> None:
        """Serializes the efficiency model.

        Args:
            efficiency (team.efficiencylike.Efficiencylike): _description_
        """
        self.efficiency_meta.commit_efficiency(models.EfficiencyPayload(efficiency.__dict__), date)



class TeamController(team.teamlike.Controlleralog):

    key : str
    date : datetime.datetime
    efficiency_controller : team.efficiencylike.Controlleralog

    def __init__(self, key : str = "demo:internal", date : datetime.datetime = datetime.datetime.today()) -> None:
        self.key = key
        self.date = date
        self.efficiency_controller = TeamEfficiencyController(key, date)

    def get(self, team : team.teamlike.Teamlike):
        return

    def serialize(self, team: team.teamlike.Teamlike) -> None:
        return



class Team(team.team.Team):

    id : int
    key : str

    def __init__(
        self, 
        id : int,
        key : str = "demo:internal"
    ) -> None:
        division = Division()
        super().__init__(id, division, TeamController(key))
        self.key = key

    def biupdate_and_serialize(
        self, 
        opponent: division.divisionlike.Teamalog, 
        pppf: float, 
        pppa: float, 
        date : datetime.datetime,
        recency: float = 0.2
    ) -> None:

        self.eff.biupdate_and_serialize(
            Team(opponent.id, self.key).eff, 
            pppf, 
            pppa, 
            date,
            recency
        )


class Game(division.divisionlike.Gamealog):

    home : division.divisionlike.Teamalog
    home_pts : int
    away : division.divisionlike.Teamalog
    away_pts : int

    def __init__(
        self, 
        home_id : int, 
        home_pts : int, 
        away_id : int,
        away_pts : int
    ) -> None:
        self.home = Team(home_id)
        self.home_pts = home_pts
        self.away = Team(away_id)
        self.away_pts = away_pts

 

class DivisionController(division.divisionlike.Controlleralog):
    
    def get_games_on_date(self, date: datetime.datetime) -> Sequence[division.divisionlike.Gamealog]:
        sports_data_games = integrations.SportsDataIO.ncaab.games.by_date.get_games(date)
        return [Game(
            home_id=game.home_team_id,
            home_pts=game.home_team_score,
            away_id=game.away_team_id,
            away_pts=game.away_team_score
        ) for game in sports_data_games]



class Division(division.division.Division):
    """Combines the division with a controller.

    Args:
        division (_type_): _description_

    Returns:
        _type_: _description_
    """

    controller : DivisionController
    efficiency : division.efficiencylike.Efficiencylike        
        

    def __init__(self):
        super().__init__(DivisionController())

    def get_games_on_date(self, date : datetime.datetime)->Sequence[division.divisionlike.Gamealog]:   
        """Gets the games on the date using the controller.

        Args:
            date (datetime.datetime): _description_

        Returns:
            Sequence[division.divisionlike.Gamealog]: _description_
        """
        return self.controller.get_games_on_date(date)


