"""Defines exceptions related to the Diablo III API wrappers

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""


class HSError(Exception):
    """Base Exception for the HS API Wrappers"""

    pass


class HSClientError(HSError):
    """Exception used when using the wrong client, ie using Hearthstone's
    client with the HS APIs, or when using the client credential workflow
    instead of the authorization workflow for certain APIs"""

    pass


class HSReleaseError(HSError):
    """Exception used when the release does not work with an API"""

    pass
