class BattleNetError(Exception):
    pass


class BattleNetDataNotFoundError(BattleNetError):
    pass


class BattleNetRegionNotFoundError(BattleNetError):
    pass


class BattleNetNegativeIndexError(BattleNetError):
    pass