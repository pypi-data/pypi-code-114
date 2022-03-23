"""Defines exceptions related to the Starcraft 2 API wrappers

Classes:
    SC2Error
    SC2ClientError
    SC2RegionError

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Starcraft 2 and any data
    retrieved from this API.

"""


class SC2Error(Exception):
    """Base Exception class for Starcraft 2"""

    pass


class SC2ClientError(SC2Error):
    """Exception when the client is not the correct one"""

    pass


class SC2RegionError(SC2Error):
    """Exception for when there is a regional data conflict"""

    pass
