import abc
import datetime
from typing import Protocol, Sequence

class Teamalog(Protocol):

    id : int

    @abc.abstractmethod
    def biupdate_and_serialize(self, opponent : 'Teamalog', pppf : float, pppa : float, date : datetime.datetime, recency : float = .2)->None:
        pass

class Gamealog(Protocol):
    home : Teamalog
    home_pts : float
    away : Teamalog
    away_pts : float

class Divisionalog(Protocol):
    
    @abc.abstractmethod
    def get_games_on_date(self, date : datetime.datetime)->Sequence[Gamealog]:
        pass

class Efficiencylike(Protocol):

    division : Divisionalog
    avg_oeff : float
    avg_deff : float
    ppp : float
    
    @abc.abstractmethod
    def __init__(self, division : Divisionalog):
        pass

    @abc.abstractmethod
    def update_by_date(self, date : datetime.datetime)->None:
        pass