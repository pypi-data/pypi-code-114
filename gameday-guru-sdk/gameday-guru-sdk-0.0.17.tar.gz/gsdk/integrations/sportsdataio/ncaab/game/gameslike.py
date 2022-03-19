from typing import Protocol
from . import by_date_like
from ...sportsdataio_meta import SportsDataIOMetalike

class Gameslike(Protocol):

    by_date : by_date_like.GamesByDatelike
    meta : SportsDataIOMetalike