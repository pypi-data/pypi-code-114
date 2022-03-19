from ...sportsdataio_meta import SportsDataIOMetalike
from . import by_date
from . import by_date_like
from . import gameslike
from typing import Type


class Games(gameslike.Gameslike):

    def __init__(
        self, 
        meta : SportsDataIOMetalike, 
        by_date : Type[by_date_like.GamesByDatelike] = by_date.GamesByDate
    ):
        self.meta = meta
        self.by_date = by_date(self.meta)
