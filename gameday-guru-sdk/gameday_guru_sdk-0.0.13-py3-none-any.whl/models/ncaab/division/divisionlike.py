import abc
import datetime
from typing import Protocol, Sequence
from . import efficiencylike

class Teamalog(
    # dependency targets
    efficiencylike.Teamalog,
    Protocol
):
    pass

class Gamealog(
    # dependency targets
    efficiencylike.Gamealog,
    Protocol
):
    pass

class Controlleralog(Protocol):
    @abc.abstractmethod
    def get_games_on_date(self, date : datetime.datetime)->Sequence[Gamealog]:   
        pass

class Divisionlike(
    Protocol
):

    efficiency : efficiencylike.Efficiencylike
    controller : Controlleralog
    
    @abc.abstractmethod
    def get_games_on_date(self, date : datetime.datetime)->Sequence[Gamealog]:   
        # todo fix type linting here
        pass