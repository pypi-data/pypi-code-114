"""Defines exceptions related to the Diablo III API wrappers

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""


class D3Error(Exception):
    """Base Error class for Diablo III Client"""

    pass


class D3ClientError(D3Error):
    """Error raised if there is a mismatch with the client and API endpoints"""

    pass
