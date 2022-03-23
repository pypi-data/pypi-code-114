"""Generates the URI/querystring and headers for the Diablo III API endpoints"""
from typing import Optional

from battlenet_client import utils


class GameData:
    @staticmethod
    def season(
        client,
        region_tag: str,
        season_id: Optional[int] = None,
        locale: Optional[str] = None,
    ):
        """Returns an index of seasons, or a leaderboard of the specified season

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            season_id (int): the ID of the season

        Returns:
            dict: The dict containing for the index of seasons, or the index of
                the leaderboards for the given season
        """
        uri = f"{utils.api_host(region_tag)}/data/d3/season/"
        if season_id:
            uri += season_id

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def season_leaderboard(
        client,
        region_tag: str,
        season_id: int,
        leaderboard_id: str,
        locale: Optional[str] = None,
    ):
        """Returns the leaderboard for the specified season by slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            season_id (int): the ID of the season
            leaderboard_id (Str): the slug of the leaderboard

        Returns:
            dict: the dict containing for the leaderboard for the given season
        """
        uri = f"{utils.api_host(region_tag)}/data/d3/season/{season_id}/leaderboard/{leaderboard_id}"
        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def era(
        client,
        region_tag: str,
        era_id: Optional[int] = None,
        locale: Optional[str] = None,
    ):
        """Returns an index of eras, or index of leaderboards for the era

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            era_id (int): the ID of the era

        Returns:
            dict: the dict containing for the index of sea, or the leaderboard
                for the given season
        """
        uri = f"{utils.api_host(region_tag)}/data/d3/era/"
        if era_id:
            uri += era_id

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def era_leaderboard(
        client,
        region_tag: str,
        era_id: int,
        leaderboard_id: str,
        locale: Optional[str] = None,
    ):
        """Returns the leaderboard for the specified era by slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            era_id (int): the ID of the season
            leaderboard_id (str): the slug of the leaderboard

        Returns:
            dict: the dict containing for the leaderboard for the given season
        """
        uri = f"{utils.api_host(region_tag)}/data/d3/era/{era_id}/{leaderboard_id}"
        params = {"locale": utils.localize(locale)}
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)
