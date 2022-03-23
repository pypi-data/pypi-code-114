"""Defines the client for connected to Hearthstone

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of WoW and WoW Classic
    and any data pertaining thereto
"""
from typing import Optional, Any, Dict

from requests import Response

from ..bnet.client import BNetClient
from ..bnet.misc import localize, slugify


class HSClient(BNetClient):
    """Defines the client workflow class for HearthStone

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
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
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ) -> None:

        super().__init__(region, client_id=client_id, client_secret=client_secret)

    def game_data(self, locale: str, *args, **kwargs) -> Response:
        """Used to retrieve data from the source data APIs

        Args:
            locale (str): the locale to use, example: en_US


        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{'/'.join([slugify(arg) for arg in args])}"

        kwargs["params"]["locale"] = localize(locale)

        return self.get(uri, **kwargs)

    def search(
        self,
        locale: str,
        document: str,
        fields: Dict[str, Any],
        game_mode: Optional[str] = "constructed",
    ) -> Response:
        """Used to perform searches where available

        Args:
            locale (str): the locale to use, example: en_US
            document (str): the document tree to be searched
            fields (dict): the criteria to search
            game_mode (str): the game mode to search through

        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{slugify(document)}"

        params = {"locale": localize(locale)}

        if document == "cards" and game_mode.lower() in (
            "constructed",
            "battlegrounds",
            "mercenaries",
        ):
            params.update({"gameMode": game_mode})
        else:
            raise ValueError("Invalid Game Mode")

        params.update(fields)

        return self.get(uri, params=params)
