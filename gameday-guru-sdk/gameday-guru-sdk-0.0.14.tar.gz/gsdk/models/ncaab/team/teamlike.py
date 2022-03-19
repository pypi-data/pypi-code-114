from . import efficiencylike
import abc
from typing import Protocol

class Divisionalog(Protocol):
    efficiency : efficiencylike.Divisionalog

class Controlleralog(Protocol): 
    """Abstract class for team controller.
    We just need get and set methods for the team.
    """

    efficiency_controller : efficiencylike.Controlleralog
    
    @abc.abstractmethod
    def get(self, team : 'Teamlike'):
        pass

    @abc.abstractmethod
    def serialize(self, team : 'Teamlike')->None:
        pass

class Teamlike(
    # injection targets
    efficiencylike.Teamalog, 
    Protocol
):
    """Team abstract class with injection targets.
    """
    pts : float
    pts_against : float
    name : str
    id : int