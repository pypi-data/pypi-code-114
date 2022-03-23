"""Defines the classes that handle the community APIs for Starcraft 2

Classes:
    Community
    CommunityCN

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Starcraft 2 and any data
    retrieved from this API.
"""

from typing import TYPE_CHECKING, Optional

from requests import Response

if TYPE_CHECKING:
    from .client import SC2Client

from .exceptions import SC2ClientError, SC2RegionError


class Profile:
    def __init__(self, client: "SC2Client") -> None:
        self.__client = client

    def static(self, region_id: int, locale: Optional[str] = None) -> Response:
        """Returns all static SC2 profile data (achievements, categories, criteria, and rewards).

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants

        Returns:
            dict: dict containing the static profile data
        """

        return self.__client.community(locale, "static", "profile", region_id)

    def metadata(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ) -> Response:
        """Returns metadata for an individual's profile.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: dict containing the requested metadata
        """
        return self.__client.community(
            locale, "metadata", "profile", region_id, realm_id, profile_id
        )

    def profile(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ) -> Response:
        """Returns data about an individual SC2 profile.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: dict containing the requested profile data
        """
        return self.__client.community(
            locale, "profile", region_id, realm_id, profile_id
        )

    def ladder(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        ladder_id: Optional[int] = None,
        locale: Optional[str] = None,
    ) -> Response:
        """Returns a ladder summary, or specific ladder for an individual SC2 profile.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID
            ladder_id (int, optional): the ID of a specific ladder, if desired

        Returns:
            dict: dict containing the requested profile data
        """
        if ladder_id:
            return self.__client.community(
                locale, "profile", region_id, realm_id, profile_id, "ladder", "summary"
            )

        return self.__client.community(
            locale, "profile", region_id, realm_id, profile_id, "ladder", ladder_id
        )


class Ladder:
    def __init__(self, client: "SC2Client") -> None:
        self.__client = client

    def grandmaster(self, region_id: int, locale: Optional[str] = None) -> Response:
        """Returns ladder data for the current season's grandmaster leaderboard.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants

        Returns:
            dict: dict containing info about the grandmaster leaderboard
        """
        return self.__client.community(locale, "ladder", "grandmaster", region_id)

    def season(self, region_id: int, locale: Optional[str] = None) -> Response:
        """Returns data about the current season.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants

        Returns:
            dict: dict containing info about the current season
        """
        return self.__client.community(locale, "ladder", "season", region_id)


class Account:
    def __init__(self, client: "SC2Client") -> None:
        self.__client = client

    def player(self, account_id: str, locale: Optional[str] = None) -> Response:
        """Returns the player data for the provided `account_id`.

        Args:
            locale (str): which locale to use for the request
            account_id (int): the account ID to request

        Returns:
            dict: json decoded data of the account
        """
        if not self.__client.auth_flow:
            raise SC2ClientError("Requires the authorized workflow")

        return self.__client.community(locale, "player", account_id)


class Legacy:
    def __init__(self, client: "SC2Client") -> None:
        self.__client = client

    def profile(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ) -> Response:
        """Retrieves data about an individual SC2 profile.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
             dict: json decoded data of the profile
        """
        return self.__client.community(
            locale, "legacy", "profile", region_id, realm_id, profile_id
        )

    def ladders(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ) -> Response:
        """Retrieves data about an individual SC2 profile's ladders.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: json decoded data of the profile's ladders
        """
        return self.__client.community(
            locale, "legacy", "profile", region_id, realm_id, profile_id, "ladders"
        )

    def match_history(
        self,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ) -> Response:
        """Returns data about an individual SC2 profile's match history.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: json decoded data of the profile's match history
        """
        return self.__client.community(
            locale, "legacy", "profile", region_id, realm_id, profile_id, "matches"
        )

    def ladder(
        self, region_id: int, ladder_id: int, locale: Optional[str] = None
    ) -> Response:
        """Returns data about an individual SC2 profile's match history.

        Args:
            locale (str): localization being requested of the API
            region_id (int): region for the profile, or use sc2.constants
            ladder_id (int): ladder ID for the request

        Returns:
            dict: json decoded data of the profile's data for the specified ladder
        """
        return self.__client.community(locale, "legacy", "ladder", region_id, ladder_id)

    def achievements(self, region_id: int, locale: Optional[str] = None) -> Response:
        """Returns the player data for the provided `account_id`.

        Args:
            locale (str): which locale to use for the request
            region_id (int): the account ID to request

        Returns:
            dict: json decoded data of the profile's achievements
        """
        return self.__client.community(
            locale, "legacy", "data", "achievements", region_id
        )

    def rewards(self, region_id: int, locale: Optional[str] = None) -> Response:
        """Returns the player data for the provided `account_id`.

        Args:
            locale (str): which locale to use for the request
            region_id (int): the account ID to request

        Returns:
            dict: json decoded data of the profile's rewards
        """
        return self.__client.community(locale, "legacy", "data", "rewards", region_id)


class ProfileCN:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.__client = client

    def profile(
        self, profile_id: str, region: str, name: str, locale: Optional[str] = None
    ) -> Response:
        """Retrieves data about an individual SC2 profile.

        Args:
            locale (str): localization being requested of the API
            profile_id (int): the profile ID
            region (str): region for the profile
            name (str): name of the profile

        Returns:
             dict: json decoded data of the profile
        """
        if self.__client.tag != 5:
            raise SC2RegionError("This API is not available in this region")

        return self.__client.community(locale, "profile", profile_id, region, name)

    def ladders(
        self, profile_id: str, region: str, name: str, locale: Optional[str] = None
    ) -> Response:
        """Returns data about an individual SC2 profile's ladders.

        Args:
            locale (str): localization being requested of the API
            profile_id (int): the profile ID
            region (str): region for the profile
            name (str): name of the profile

        Returns:
            dict: json decoded data of the profile's ladders
        """

        if self.__client.tag != 5:
            raise SC2RegionError("This API is not available in this region")

        return self.__client.community(
            locale, "profile", profile_id, region, name, "ladders"
        )

    def match_history(
        self, profile_id: str, region: str, name: str, locale: Optional[str] = None
    ) -> Response:
        """Returns data about an individual SC2 profile's match history.

        Args:
            locale (str): localization being requested of the API
            profile_id (int): the profile ID
            region (str): region for the profile
            name (str): name of the profile

        Returns:
            dict: json decoded data of the profile's ladders
        """
        if self.__client.tag != 5:
            raise SC2RegionError("This API is not available in this region")

        return self.__client.community(
            locale, "profile", profile_id, region, name, "matches"
        )


class LadderCN:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.__client = client

    def ladder(self, ladder_id: str, locale: Optional[str] = None) -> Response:
        """Returns data about an SC2 ladder.

        Args:
            locale (str): The locale to use in the response.
            ladder_id (str): The ID of the ladder to retrieve.

        Returns:
            dict: dict with data of the ladder
        """
        return self.__client.community(locale, "ladder", ladder_id)


class DataResourceCN:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.__client = client

    def achievements(self, locale: Optional[str] = None) -> Response:
        """Returns the achievements for Starcraft II

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        return self.__client.community(locale, "data", "achievements")

    def rewards(self, locale: Optional[str] = None) -> Response:
        """Returns the rewards of the achievements in Starcraft II

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        return self.__client.community(locale, "data", "rewards")
