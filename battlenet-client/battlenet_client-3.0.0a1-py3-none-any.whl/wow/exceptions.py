"""Defines exceptions related to the World of Warcraft

Classes:
    WoWError
    WoWClientError
    WoWRegionError

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of World of Warcraft and any data
    retrieved from this API.
"""


class WoWError(Exception):
    """Base Exception for the WOW API Wrappers"""

    pass


class WoWClientError(WoWError):
    """Exception used when using the wrong client, ie using Hearthstone's
    client with the WoW APIs, or when using the client credential workflow
    instead of the authorization workflow for certain APIs"""

    pass


class WoWReleaseError(WoWError):
    """Exception used when the release does not work with an API"""

    pass
