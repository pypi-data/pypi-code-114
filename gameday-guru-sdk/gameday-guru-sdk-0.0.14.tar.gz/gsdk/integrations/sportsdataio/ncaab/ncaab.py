from dotenv import dotenv_values
from . import ncaablike
from . import game
from . import team
from .. import sportsdataio_meta



class Ncaab(ncaablike.NCAABlike):

    games : game.gameslike.Gameslike
    teams : team.teamlike.TeamsByIdlike
    
    def __init__(self) -> None:

        meta = sportsdataio_meta.SportsDataIOMetalike=sportsdataio_meta.SportsDataIOmeta(
            "SPORTS_DATA_KEY",
            "SPORTS_DATA_DOMAIN"
        )
        self.games = game.games.Games(meta)
        self.teams = team.team.TeamsById(meta)

