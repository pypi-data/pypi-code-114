from commmons import is_blank


def validate(watchlist):
    assert not is_blank(watchlist.url)
