"""Defines the client for connected to Starcraft 2

Classes:
    SC2Client

Examples:
    > from battlenet_client import sc2
    > client = sc2.SC2Client(<region>, client_id='<client ID>', client_secret='<client secret>')

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of WoW and WoW Classic
    and any data pertaining thereto
"""
from requests import Response

from typing import Optional, List

from battlenet_client.bnet.client import BNetClient

from battlenet_client.bnet.misc import localize


class SC2Client(BNetClient):
    """Defines the client workflow class for the World of Warcraft API

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        scope (list, optional): the scope or scopes to use during the data that require the
            Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal
    """

    __MAJOR__ = 1
    __MINOR__ = 0
    __PATCH__ = 0

    def __init__(
        self,
        region: str,
        *,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        super().__init__(
            region,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )

    def game_data(self, locale: str, *args, **kwargs) -> Response:
        """Generates then necessary game data API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        kwargs["params"]["locale"] = localize(locale)

        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/sc2/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = localize(locale)

        return self.get(uri, **kwargs)

    def community(self, locale: str, *args, **kwargs) -> Response:
        """Generates then necessary community API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        kwargs["params"]["locale"] = localize(locale)

        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/sc2/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self.get(uri, **kwargs)
