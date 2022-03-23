"""Defines exceptions related to the Diablo III API wrappers"""


class D3Error(Exception):
    """Base Error class for Diablo III Client"""

    pass


class D3ClientError(D3Error):
    """Error raised if there is a mismatch with the client and API endpoints"""

    pass
