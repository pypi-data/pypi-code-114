import datetime
from . import efficiencylike

class Efficiency(efficiencylike.Efficiencylike):
    
    division : efficiencylike.Divisionalog
    avg_oeff : float
    avg_deff : float
    ppp : float

    def __init__(self, division: efficiencylike.Divisionalog):
        self.division = division

    def update_by_date(self, date: datetime.datetime) -> None:
        """Updates the efficiency ratings for games on a certain date.

        Args:
            date (datetime.datetime): the date on which the games take place.
        """
        for game in self.division.get_games_on_date(date):
            game.home.biupdate_and_serialize(game.away, game.home_pts, game.away_pts, date)
