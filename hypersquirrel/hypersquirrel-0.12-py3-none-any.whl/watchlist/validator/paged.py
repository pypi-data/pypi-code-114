from .base import validate as validate_base


def validate(watchlist):
    validate_base(watchlist)
    assert "${page}" in watchlist.url
    assert watchlist.page_min and isinstance(watchlist.page_min, int)
    assert watchlist.page_max and isinstance(watchlist.page_max, int)
    assert watchlist.page_min < watchlist.page_max
