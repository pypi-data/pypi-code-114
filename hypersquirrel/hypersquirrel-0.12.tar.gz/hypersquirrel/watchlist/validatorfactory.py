from . import PagedWatchlist
from .validator.paged import validate as validate_paged
from .validator.base import validate as validate_base


class WatchlistValidatorFactory:
    def __init__(self):
        self.registry = list()

    def register_validator(self, condition, validator):
        self.registry.append((condition, validator,))

    def get_validator(self, watchlist):
        for validator_pair in self.registry:
            condition = validator_pair[0]
            validator = validator_pair[1]
            if condition(watchlist):
                return validator
        raise ValueError(f"No validator found")


_wvf = WatchlistValidatorFactory()
_wvf.register_validator(lambda w: isinstance(w, PagedWatchlist), validate_paged)
_wvf.register_validator(lambda w: True, validate_base)


def get_watchlist_validator(watchlist):
    return _wvf.get_validator(watchlist)
