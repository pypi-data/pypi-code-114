"""Defines the classes that handle the community APIs for Starcraft 2

Classes:
    Community
    CommunityCN

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Starcraft 2 and any data
    retrieved from this API.
"""

from typing import Optional

from battlenet_client import utils
from .exceptions import SC2RegionError


class Community:
    @staticmethod
    def static(
        client,
        region_tag: str,
        *,
        region_id: Optional[str] = None,
        locale: Optional[str] = None,
    ):
        """Returns all static SC2 profile data (achievements, categories, criteria, and rewards).

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (str): region for the profile, or use sc2.constants  (used outside CN only)

        Returns:
            dict: dict containing the static profile data
        """
        uri = f"{utils.api_host(region_tag)}/sc2/static/profile/{region_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def metadata(
        client,
        region_tag: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ):
        """Returns metadata for an individual's profile.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: dict containing the requested metadata
        """
        uri = f"{utils.api_host(region_tag)}/sc2/metadata/profile/{region_id}/{realm_id}/{profile_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def profile(
        client,
        region_tag: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ):
        """Returns data about an individual SC2 profile.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: dict containing the requested profile data
        """
        uri = f"{utils.api_host(region_tag)}/sc2/profile/{region_id}/{realm_id}/{profile_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def ladder(
        client,
        region_tag: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        *,
        ladder_id: Optional[int] = "summary",
        locale: Optional[str] = None,
    ):
        """Returns a ladder summary, or specific ladder for an individual SC2 profile.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID
            ladder_id (int, optional): the ID of a specific ladder, if desired

        Returns:
            dict: dict containing the requested profile data
        """
        uri = f"{utils.api_host(region_tag)}/sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def grandmaster(
        client, region_tag: str, region_id: int, locale: Optional[str] = None
    ):
        """Returns ladder data for the current season's grandmaster leaderboard.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants

        Returns:
            dict: dict containing info about the grandmaster leaderboard
        """
        uri = f"{utils.api_host(region_tag)}/sc2/ladder/grandmaster/{region_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def season(client, region_tag: str, region_id: int, locale: Optional[str] = None):
        """Returns data about the current season.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants

        Returns:
            dict: dict containing info about the current season
        """
        uri = f"{utils.api_host(region_tag)}/sc2/ladder/season/{region_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def player(client, region_tag: str, account_id: str, locale: Optional[str] = None):
        """Returns the player data for the provided `account_id`.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            account_id (int): the account ID to request

        Returns:
            dict: json decoded data of the account
        """
        uri = f"{utils.api_host(region_tag)}/sc2/player/{account_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Legacy:
    @staticmethod
    def profile(
        client,
        region_tag: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ):
        """Retrieves data about an individual SC2 profile.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
             dict: json decoded data of the profile
        """
        uri = f"{utils.api_host(region_tag)}/sc2/legacy/profile/{region_id}/{realm_id}/{profile_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def ladders(
        client,
        region_tag: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ):
        """Retrieves data about an individual SC2 profile's ladders.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: json decoded data of the profile's ladders
        """
        uri = f"{utils.api_host(region_tag)}/sc2/legacy/profile/{region_id}/{realm_id}/{profile_id}/ladders"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def match_history(
        client,
        region_tag: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        locale: Optional[str] = None,
    ):
        """Returns data about an individual SC2 profile's match history.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            realm_id (int): the realm of the profile (1 or 2)
            profile_id (int): the profile ID

        Returns:
            dict: json decoded data of the profile's match history
        """
        uri = f"{utils.api_host(region_tag)}/sc2/legacy/profile/{region_id}/{realm_id}/{profile_id}/matches"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def ladder(
        client,
        region_tag: str,
        region_id: int,
        ladder_id: int,
        locale: Optional[str] = None,
    ):
        """Returns data about an individual SC2 profile's match history.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): region for the profile, or use sc2.constants
            ladder_id (int): ladder ID for the request

        Returns:
            dict: json decoded data of the profile's data for the specified ladder
        """
        uri = f"{utils.api_host(region_tag)}/sc2/legacy/ladder/{region_id}/{ladder_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def achievements(
        client, region_tag: str, region_id: int, locale: Optional[str] = None
    ):
        """Returns the player data for the provided `account_id`.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): the account ID to request

        Returns:
            dict: json decoded data of the profile's achievements
        """
        uri = f"{utils.api_host(region_tag)}/sc2/legacy/data/achievements/{region_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def rewards(client, region_tag: str, region_id: int, locale: Optional[str] = None):
        """Returns the player data for the provided `account_id`.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_id (int): the account ID to request

        Returns:
            dict: json decoded data of the profile's rewards
        """
        uri = f"{utils.api_host(region_tag)}/sc2/legacy/data/rewards/{region_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class CommunityCN:
    @staticmethod
    def profile(
        client,
        region_tag: str,
        profile_id: str,
        region: str,
        name: str,
        locale: Optional[str] = None,
    ):
        """Retrieves data about an individual SC2 profile.

        Notes:
            This can only be used in the CN region

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            profile_id (int): the profile ID
            region (str): region for the profile
            name (str): name of the profile

        Returns:
             dict: json decoded data of the profile
        """
        if region_tag.lower() != "cn":
            raise SC2RegionError("This API is not available in this region")

        uri = f"{utils.api_host(region_tag)}/sc2/profile/{profile_id}/{region}/{name}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def ladders(
        client,
        region_tag: str,
        profile_id: str,
        region: str,
        name: str,
        locale: Optional[str] = None,
    ):
        """Returns data about an individual SC2 profile's ladders.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            profile_id (int): the profile ID
            region (str): region for the profile
            name (str): name of the profile

        Returns:
            dict: json decoded data of the profile's ladders
        """

        if region_tag.lower() != "cn":
            raise SC2RegionError("This API is not available in this region")

        uri = f"{utils.api_host(region_tag)}/sc2/profile/{profile_id}/{region}/{name}/ladders"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def match_history(
        client,
        region_tag: str,
        profile_id: str,
        region: str,
        name: str,
        locale: Optional[str] = None,
    ):
        """Returns data about an individual SC2 profile's match history.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            profile_id (int): the profile ID
            region (str): region for the profile
            name (str): name of the profile

        Returns:
            dict: json decoded data of the profile's ladders
        """
        if region_tag.lower() != "cn":
            raise SC2RegionError("This API is not available in this region")

        uri = f"{utils.api_host(region_tag)}/sc2/profile/{profile_id}/{region}/{name}/matches"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def ladder(client, region_tag: str, ladder_id: str, locale: Optional[str] = None):
        """Returns data about an SC2 ladder.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            ladder_id (str): The ID of the ladder to retrieve.

        Returns:
            dict: dict with data of the ladder
        """
        if region_tag.lower() != "cn":
            raise SC2RegionError("This API is not available in this region")

        uri = f"{utils.api_host(region_tag)}/sc2/ladder/{ladder_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def achievements(client, region_tag: str, locale: Optional[str] = None):
        """Returns the achievements for Starcraft II

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if region_tag.lower() != "cn":
            raise SC2RegionError("This API is not available in this region")

        uri = f"{utils.api_host(region_tag)}/sc2/data/achievements"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def rewards(client, region_tag: str, locale: Optional[str] = None):
        """Returns the rewards of the achievements in Starcraft II

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if region_tag.lower() != "cn":
            raise SC2RegionError("This API is not available in this region")

        uri = f"{utils.api_host(region_tag)}/sc2/data/rewards"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)
