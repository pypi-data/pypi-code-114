from typing import Protocol
from . import game
from . import team

class NCAABlike(Protocol):

    games : game.gameslike.Gameslike
    teams : team.teamlike.TeamsByIdlike