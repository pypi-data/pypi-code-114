from . import divisionlike
from . import efficiencylike
from . import efficiency
from typing import Sequence, Type
import datetime

class Division(divisionlike.Divisionlike):
    
    controller : divisionlike.Controlleralog
    efficiency : efficiencylike.Efficiencylike

    def __init__(self, 
        controller : divisionlike.Controlleralog,
        efficiency : Type[efficiencylike.Efficiencylike] = efficiency.Efficiency
    ):
        self.controller = controller
        self.efficiency = efficiency(self)

    def get_games_on_date(self, date: datetime.datetime) -> Sequence[divisionlike.Gamealog]:
        return self.controller.get_games_on_date(date)
