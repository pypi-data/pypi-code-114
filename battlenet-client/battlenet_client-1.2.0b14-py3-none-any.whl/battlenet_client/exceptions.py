from requests.exceptions import HTTPError


class BattleNetError(Exception):
    pass


class BattleNetDataNotFoundError(HTTPError):
    pass
