from . import teamlike
from . import efficiencylike
from typing import Type
from . import efficiency

class Team(teamlike.Teamlike):
    """An NCAAB team.
    """

    pts : float
    pts_against : float
    name : str
    id : int
    controller : teamlike.Controlleralog
    eff : efficiencylike.Efficiencylike

    def __init__(
        self, 
        id : int,
        division : teamlike.Divisionalog, 
        controller : teamlike.Controlleralog,
        efficiency_dependency : Type[efficiencylike.Efficiencylike] = efficiency.Efficiency
    ):
        """Initializes a team using a division and a controller.

        Args:
            division (TeamDivisonlike): is the division of which the team is a member.
            controller (Controlleralog):  controller is the controller for the team's operations.
        """
        self.id = id
        self.division = division
        self.controller = controller
        self.eff = efficiency_dependency(self, division.efficiency, controller.efficiency_controller)

    def __hash__(self)->int:
        return self.id