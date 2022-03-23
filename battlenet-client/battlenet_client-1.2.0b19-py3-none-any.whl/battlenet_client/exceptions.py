class BNetError(Exception):
    pass


class BNetDataNotFoundError(BNetError):
    pass


class BNetRegionNotFoundError(BNetError):
    pass


class BNetNegativeIndexError(BNetError):
    pass