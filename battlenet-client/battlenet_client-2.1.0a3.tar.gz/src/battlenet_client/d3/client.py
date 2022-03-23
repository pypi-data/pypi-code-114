"""Defines the client for connected to the Diablo III API

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""
import importlib
from typing import List, Optional

from requests import Response

from ..bnet.misc import localize
from ..bnet.client import BNetClient


class D3Client(BNetClient):
    """Defines the client workflow class for Diablo III

    Args:
        region (str): region abbreviation for use with the s

    Keyword Args:
        scope (list of str, optional): the scope or scopes to use during the data that require the
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
    ) -> None:

        super().__init__(
            region,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )

        mod = importlib.import_module("battlenet_client.d3.community")
        if self.tag == "cn":
            self.community_api = getattr(mod, "CommunityCN")(self)
        else:
            self.community_api = getattr(mod, "Community")(self)

        mod = importlib.import_module("battlenet_client.d3.game_data")
        self.game_data_api = getattr(mod, "GameData")(self)

    def game_data(self, locale: str, *args, **kwargs) -> Response:
        """Generates then necessary game data API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/d3/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = localize(locale)

        return self.get(uri, **kwargs)

    def community(self, locale: str, *args, **kwargs) -> Response:
        """Generates then necessary community API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/data/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = localize(locale)

        return self.get(uri, **kwargs)

    def profile_api(self, locale: str, *args, **kwargs) -> Response:
        """Generates then necessary profile API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/profile/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = localize(locale)

        return self.get(uri, **kwargs)
