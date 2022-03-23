"""Generates the URI/querystring and headers for the Hearthsone API endpoints

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of HearthstoneI and any data
    retrieved from this API.
"""

from typing import Optional, Any, TYPE_CHECKING, Dict

from requests import Response

if TYPE_CHECKING:
    from client import HSClient


class Hearthstone:
    def __init__(self, client: "HSClient") -> None:
        self.__client = client

    def card_search(
        self,
        field_values: Dict[str, Any],
        game_mode: Optional[str] = "constructed",
        locale: Optional[str] = None,
    ) -> Response:
        """Searches for cards that match `field_values'

        Args:
            locale (str): locale to use with the API
            game_mode (str): the game mode for the cards, default is 'constructed'
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/game-data-apis

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """

        return self.__client.search(locale, "cards", field_values, game_mode)

    def card(
        self,
        card_id: str,
        game_mode: Optional[str] = "constructed",
        locale: Optional[str] = None,
    ) -> Response:
        """Returns the card provided by `card_id'

        Args:
            locale (str): which locale to use for the request
            card_id (int, str): the ID or full slug of the card
            game_mode (str, optional): the game mode
                See for more information:
                https://develop.battle.net/documentation/hearthstone/guides/game-modes

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        if game_mode not in ("constructed", "battlegrounds", "mercenaries"):
            raise ValueError("Invalid game mode specified")

        return self.__client.game_data(
            locale, "cards", card_id, params={"gameMode": game_mode}
        )

    def card_back_search(
        self, field_values: Dict[str, Any], locale: Optional[str] = None
    ) -> Response:
        """Searches for cards that match `field_values'

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/guides/card-backs

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """

        return self.__client.search(locale, "cardbacks", field_values)

    def card_back(self, card_back_id: str, locale: Optional[str] = None) -> Response:
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            locale (str): which locale to use for the request
            card_back_id (int, str): the ID or full slug of the card

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        return self.__client.game_data(locale, "cardbacks", card_back_id)

    def card_deck(
        self, field_values: Optional[Dict[str, Any]], locale: Optional[str] = None
    ) -> Response:
        """Searches for cards that match `field_values'

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/guides/decks

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        return self.__client.search(locale, "deck", field_values)

    def metadata(
        self, meta_data: Optional[str] = None, locale: Optional[str] = None
    ) -> Response:
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            locale (str): which locale to use for the request
            meta_data (str, optional): what metadata to filter
                Please see below for more information
                https://develop.battle.net/documentation/hearthstone/guides/metadata
                valid options: 'sets', 'setGroups', 'types', 'rarities', 'classes',
                    'minionTypes', 'keywords'

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        if meta_data:
            return self.__client.game_data(locale, "metadata", meta_data)

        return self.__client.game_data(locale, "metadata")
