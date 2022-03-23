"""This module contains the classes for accessing game data related utils.apis"""
from typing import Optional, Any, Dict, Union

from .exceptions import WoWReleaseError
from battlenet_client import utils

from battlenet_client.wow.utils import namespace


class Achievement:

    @staticmethod
    def achievement_category(
        client,
        region_tag: str,
        *,
        release: Optional[str] = "retail",
        category_id: Optional[int] = "index",
        locale: Optional[str] = None,
    ):
        """Accesses a list achievement categories or specific achievement
        category if :category_id: is provided

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            category_id (int, optional): the achievement's category ID or None (default).
                None will retrieve the entire list of achievement categories

        Returns:

            dict: json decoded data for the index/individual achievement categories
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/achievement-category/{category_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace('static', release, region_tag),
        }
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def achievement(
        client,
        region_tag: str,
        *,
        achievement_id: Optional[int] = "index",
        release: Optional[str] = "retail",
        locale: Optional[str] = None,
    ):
        """Returns an index of achievements, or a specific achievements

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            achievement_id (int, optional): the achievement ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual achievements
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/achievement/{achievement_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }
        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def achievement_media(
        client,
        region_tag: str,
        achievement_id: int,
        *,
        release: Optional[str] = "retail",
        locale: Optional[str] = None,
    ):
        """Returns media for an achievement's icon.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            achievement_id (int): the achievement ID or the word 'index'

        Returns:
            dict: json decoded media data for the achievement
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/{achievement_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Auction:
    @staticmethod
    def auction(
        client,
        region_tag: str,
        connected_realm_id: int,
        *,
        release: Optional[str] = "retail",
        auction_house_id: Optional[int] = None,
        locale: Optional[str] = None,
    ):
        """Returns auction data.  With retail client, region_tag, it returns all the auctions for the given connected
        realm. For classic titles, the results can be either the entire list, or the individual auctions

        See the Connected Realm utils.api for information about retrieving a list of
        connected realm IDs.

        Auction house data updates at a set interval. The value was initially set
        at 1 hour; however, it might change over time without notice.

        Depending on the number of active auctions on the specified connected realm,
        the response from this game_data may be rather large, sometimes exceeding
        10 MB.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            connected_realm_id (int): the id of the connected realm
            auction_house_id (int, optional): the ID of the auction house

        Returns:
            dict: json decoded data for the index/individual auction(s)

        Raises:
            WoWReleaseError: when an AH ID is used for the retail client
        Notes:
            Auction house functionality is not available for WoW 1.x (Vanilla Classic)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/connected-realm/{connected_realm_id}/"
        if release == "retail" and auction_house_id is None:
            uri += "auctions"

        if release != "retail" and auction_house_id is None:
            uri += "auctions/index"

        if release != "retail" and auction_house_id is not None:
            uri += "auctions"

        if release == "retail" and auction_house_id is not None:
            raise WoWReleaseError("Auction House ID provided for retail")

        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class AzeriteEssence:
    @staticmethod
    def azerite_essence(
        client,
        region_tag: str,
        *,
        essence_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            essence_id (int, optional): the Azerite essence ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/azerite-essence/{essence_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def azerite_essence_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches for azerite essences that match `field_values`

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/azerite-essence"

        # adding locale and namespace key/values pairs for a complete parameters list for the request
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)

    @staticmethod
    def azerite_essence_media(
        client,
        region_tag: str,
        essence_id: int,
        *,
        release: Optional[str] = "retail",
        locale: Optional[str] = None,
    ):
        """Returns media data for an azerite essence.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            essence_id (int): the azerite essence ID

        Returns:
            dict: json decoded media data for the azerite essence
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/media/azerite-essence/{essence_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class ConnectedRealm:
    @staticmethod
    def connected_realm(
        client,
        region_tag: str,
        *,
        connected_realm_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of connected realms, or a specific connected realm. Connected realm is a group of standard
        realms that act as one large realm

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            connected_realm_id (int, optional): the ID of the connected realm

        Returns:
            dict: json decoded data for the index/individual connected realms
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/connected-realm/{connected_realm_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def connected_realm_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches the connected realm utils.api for connected realm(s) that match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): field/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/connected_realm"

        # adding locale and namespace key/values pairs for a complete parameters list for the request
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)


class Covenant:
    @staticmethod
    def covenant(
        client,
        region_tag: str,
        *,
        covenant_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of covenants, or a specific covenant

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            covenant_id (int, optional): the ID of the covenant or the default 'index'

        Returns:
            dict: json decoded data for the index/individual covenant
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/covenant/{covenant_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def covenant_media(
        client,
        region_tag: str,
        covenant_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a covenant.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            covenant_id (int, optional): the covenant ID

        Returns:
            dict: json decoded media data for the covenant
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/covenant{covenant_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def soulbind(
        client,
        region_tag: str,
        *,
        soulbind_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of soulbinds, or a specific soulbind

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            soulbind_id (int, optional): the ID of the soulbind or the word of 'index'

        Returns:
            dict: json decoded data for the index/individual soulbind
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/covenant/soulbind/{soulbind_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def conduit(
        client,
        region_tag: str,
        *,
        conduit_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of conduits, or a specific conduit

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            conduit_id (int, optional): the ID of the conduit or the word of 'index'

        Returns:
            dict: json decoded data for the index/individual conduit
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/covenant/conduit/{conduit_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Creature:
    @staticmethod
    def creature_family(
        client,
        region_tag: str,
        *,
        family_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of creature families, or a specific creature family

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            family_id (int, optional): the creature family ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual creature family/families
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/creature-family/{family_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def creature_type(
        client,
        region_tag: str,
        *,
        type_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of creature types, or a specific creature type

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            type_id (int, optional): the creature type ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual creature type(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/creature-type/{type_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def creature(
        client,
        region_tag: str,
        creature_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of creatures, or a specific creature

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            creature_id (int, optional): the creature ID

        Returns:
            dict: json decoded data for the index/individual creature(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/creature/{creature_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def creature_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches the creature utils.api for creatures that match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): matching criteria in key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/creature"

        #  adding locale and namespace key/values pairs for a complete parameters list for the request
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)

    @staticmethod
    def creature_display_media(
        client,
        region_tag: str,
        display_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a creature display.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            display_id (int, optional): the creature display ID

        Returns:
            dict: json decoded media data for the creature display
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/media/creature-display/{display_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def creature_family_media(
        client,
        region_tag: str,
        family_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a creature family.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            family_id (int, optional): the creature family ID

        Returns:
            dict: json decoded media data for the creature family
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/media/creature-display/{family_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class GuildCrest:
    @staticmethod
    def guild_crest_components_index(
        client,
        region_tag: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of guild crest components.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of guild crest components
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/guild-crest/index"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def guild_crest_border_media(
        client,
        region_tag: str,
        border_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a specific guild crest border.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            border_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild border
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/guild-crest/border/{border_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def guild_crest_emblem_media(
        client,
        region_tag: str,
        emblem_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a specific guild crest emblem.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            emblem_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild crest
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/guild-crest/emblem/{emblem_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Item:
    @staticmethod
    def item_class(
        client,
        region_tag: str,
        *,
        class_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of item classes, or a specific item class

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_id (int, optional): item class ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual item class(es)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/item-class/{class_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def item_set(
        client,
        region_tag: str,
        *,
        set_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of item sets, or a specific item set

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            set_id (int, optional): the item class ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual item set(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/item-set/{set_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def item_subclass(
        client,
        region_tag: str,
        class_id: int,
        subclass_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of item subclasses, or a specific item subclass

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_id (int): the item class ID
            subclass_id (int, optional): the item's subclass ID

        Returns:
            dict: json decoded data for the item's subclass
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/item-class/{class_id}/item-subclass/{subclass_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def item(
        client,
        region_tag: str,
        item_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of items, or a specific item

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            item_id (int, optional): the item class ID

        Returns:
            dict: json decoded data for the individual item
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/item/{item_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def item_media(
        client,
        region_tag: str,
        item_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for an item.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            item_id (int): the creature family ID

        Returns:
            dict: json decoded media data for the item
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/item/{item_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def item_search(
        client,
        region_tag,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches the item utils.api for items that match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria as key/value pairs

        Returns:
             dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/item"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)


class Journal:
    @staticmethod
    def journal_expansion(
        client,
        region_tag: str,
        *,
        expansion_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of journal expansions, or a specific journal expansion

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            expansion_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual journal expansion(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/journal-expansion/{expansion_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def journal_encounter(
        client,
        region_tag: str,
        *,
        encounter_id: Optional[int] = None,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of journal (boss) encounters, or a specific journal (boss) encounters

        Notes:
            This replaced the Boss endpoint of the community REST API

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            encounter_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual journal encounter(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/journal-encounter/{encounter_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def journal_encounter_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches for azerite essences that match `field_values`

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/journal-encounter"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)

    @staticmethod
    def journal_instance(
        client,
        region_tag: str,
        *,
        instance_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of journal instances (dungeons), or a specific journal instance (dungeon)

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            instance_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual journal instance(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/journal-encounter/{instance_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def journal_instance_media(
        client,
        region_tag: str,
        instance_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for an instance.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            instance_id (int): the creature family ID

        Returns:
            dict: json decoded media data for the instance
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/journal-instance/{instance_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Media:
    @staticmethod
    def media_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches the media utils.api match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): fields and values for the search criteria

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/media"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)


class ModifiedCrafting:
    @staticmethod
    def modified_crafting(
        client,
        region_tag: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of modified crafting recipes

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of modified crafting
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/modified-crafting"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def modified_crafting_category(
        client,
        region_tag: str,
        *,
        category_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of modified crafting category index, or a specific modified crafting category

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            category_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual modified crafting category/categories
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/modified-crafting/category/{category_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def modified_crafting_reagent_slot_type(
        client,
        region_tag: str,
        *,
        slot_type_id: Optional[int] = None,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of modified crafting reagent slot type, or a specific reagent slot type

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            slot_type_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual modified crafting reagent slot type(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Mount:
    @staticmethod
    def mount(
        client,
        region_tag: str,
        *,
        mount_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mounts, or a specific mount

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            mount_id (int, optional): the mount ID or 'index'

        Returns:
            dict: json decoded data for the index/individual mount(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/mount/{mount_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mount_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches the mount utils.api that match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): fields and values for the search criteria

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/mount"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)


class MythicKeystone:
    @staticmethod
    def mythic_keystone_affix(
        client,
        region_tag: str,
        *,
        affix_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mythic keystone affixes, or a specific mythic keystone affix

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            affix_id (int, optional): the affix's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone affix(es)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/keystone-affix/{affix_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mythic_keystone_affix_media(
        client,
        region_tag: str,
        affix_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a mythic keystone affix.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            affix_id (int): the affix's ID

        Returns:
            dict: json decoded media data for the mythic keystone affix(es)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/keystone-affix/{affix_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mythic_keystone_dungeon(
        client,
        region_tag: str,
        *,
        dungeon_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mythic keystone dungeons, or a specific mythic keystone dungeon

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            dungeon_id (int, optional): the dungeon's ID or 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone dungeon(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mythic_keystone_index(
        client,
        region_tag: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of links to other documents related to Mythic Keystone dungeons.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of the mythic keystone dungeon documents
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/mythic-keystone/index"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mythic_keystone_period(
        client,
        region_tag: str,
        *,
        period_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mythic keystone periods, or a specific mythic keystone period

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            period_id (int, optional): the keystone's period ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual for mythic keystone period(s)
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/mythic-keystone/period/{period_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mythic_keystone_season(
        client,
        region_tag: str,
        *,
        season_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mythic keystone seasons, or a specific mythic keystone seasons

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            season_id (int, optional): the keystone's season ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone season(s)
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/mythic-keystone/season/{season_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def mythic_keystone_leader_board(
        client,
        region_tag: str,
        connected_realm_id: int,
        *,
        dungeon_id: Optional[int] = None,
        period_id: Optional[int] = None,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mythic keystone leader boards, or a specific mythic keystone leader board

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            connected_realm_id (int): the connected realm's id
            dungeon_id (int, optional): the particular dungeon's ID or the word 'index'
            period_id (int, optional): the particular period to search or None when looking for the index

        Returns:
            dict: json decoded data for the index/individual mythic keystone leaderboard(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/"

        if dungeon_id and period_id:
            uri += "{dungeon_id}/period/{period_id}"
        else:
            uri += "index"

        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class MythicRaid:
    @staticmethod
    def mythic_raid_leaderboard(
        client,
        region_tag: str,
        raid_name: str,
        faction: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of mythic keystone affixes, or a specific mythic keystone affix

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            raid_name (str): name of the raid
            faction (str): horde or alliance, defaults to alliance

        Returns:
            dict: json decoded data for the index/individual mythic raid
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/leaderboard/hall-of-fame/"
        uri += f"{utils.slugify(raid_name)}/{utils.slugify(faction)}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Pet:
    @staticmethod
    def pet(
        client,
        region_tag: str,
        *,
        pet_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of pets, or the data about the specified pet

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            pet_id (int, optional): the pet ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual pet(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pet/{pet_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pet_media(
        client,
        region_tag: str,
        pet_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a pet

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            pet_id (int): the azerite pet ID

        Returns:
            dict: json decoded media data for the for pet
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/pet/{pet_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pet_ability(
        client,
        region_tag: str,
        *,
        pet_ability_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of pets, or the data about the specified pet

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            pet_ability_id (int, optional): the pet ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual pet ability/abilities
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pet-ability/{pet_ability_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pet_ability_media(
        client,
        region_tag: str,
        ability_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for an azerite ability.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            ability_id (int): the azerite ability ID

        Returns:
            dict: json decoded media data for the pet ability
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/pet-ability/{ability_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class PlayableClass:
    @staticmethod
    def playable_class(
        client,
        region_tag: str,
        *,
        class_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of playable classes, or a specific playable class

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_id (int, optional): the class ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable class(es)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/playable-class/{class_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def playable_class_media(
        client,
        region_tag: str,
        class_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a playable class by ID.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_id (int ): class id

        Returns:
            dict: json decoded media data for the playable class(es)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/playable-class/{class_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pvp_talent_slots(
        client,
        region_tag: str,
        class_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns the PvP talent slots for a playable class by ID.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_id (int): class id

        Returns:
            dict: json decoded data for the index of PvP Talent slots
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/playable-class/{class_id}/pvp-talent-slots"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class PlayableRace:
    @staticmethod
    def playable_race(
        client,
        region_tag: str,
        *,
        race_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of playable races, or a specific playable race

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            race_id (int, optional): the playable race's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable race(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/playable-race/{race_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class PlayableSpec:
    @staticmethod
    def playable_spec(
        client,
        region_tag: str,
        *,
        spec_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):

        """Returns an index of playable specialization, or a specific playable specialization

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            spec_id (int, optional): the playable specialization's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable specialization(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/playable-specialization/{spec_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def playable_spec_media(
        client,
        region_tag: str,
        spec_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a playable specialization by ID.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            spec_id (int): specialization id

        Returns:
            dict: json decoded media data for the playable specialization
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/playable-specialization/{spec_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class PowerType:
    @staticmethod
    def power_type(
        client,
        region_tag: str,
        *,
        power_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of power types, or a specific power type

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            power_id (int, optional): the power type's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual power types
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/power-type/{power_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Profession:
    @staticmethod
    def profession(
        client,
        region_tag: str,
        *,
        profession_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of achievements, or a specific achievements

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            profession_id (int, optional): the profession ID or the word 'index'

        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/profession/{profession_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def profession_media(
        client,
        region_tag: str,
        profession_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a creature display.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            profession_id (str):  profession ID

        Returns:
            dict: the media assets for the given creature display ID
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/profession/{profession_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def profession_skill_tier(
        client,
        region_tag: str,
        profession_id: int,
        skill_tier_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of achievements, or a specific achievements

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            profession_id (int): the profession ID
            skill_tier_id (int): the skill tier ID

        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def recipe(
        client,
        region_tag: str,
        recipe_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of achievements, or a specific achievements

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            recipe_id (str): the recipe ID

        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/recipe/{recipe_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def recipe_media(
        client,
        region_tag: str,
        recipe_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a creature display.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            recipe_id (int): the profession ID

        Returns:
            dict: the media assets for the given creature display ID
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/recipe/{recipe_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class PVP:
    @staticmethod
    def pvp_season(
        client,
        region_tag: str,
        *,
        season_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of pvp seasons, or a specific pvp season

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            season_id (int, optional): the power type's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual PvP season(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pvp-season/{season_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pvp_leader_board(
        client,
        region_tag,
        season_id: int,
        *,
        pvp_bracket: Optional[str] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of pvp leader boards, or a specific pvp leader board

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            season_id (int): pvp season's ID
            pvp_bracket (int, optional): the PvP bracket to view ('2v2', '3v3', '5v5', 'rbg') or the word 'index'

        Returns:
            dict: json decoded data for the index of the PvP leader board
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pvp-season/{season_id}/pvp-leaderboard/{pvp_bracket}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pvp_rewards_index(
        client,
        region_tag: str,
        season_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of pvp rewards, or a specific pvp reward

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            season_id (int): the season ID for the rewards or the word 'index'

        Returns:
            dict: json decoded data for the index of PvP rewards
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pvp-season/{season_id}/pvp-reward/index"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pvp_tier(
        client,
        region_tag: str,
        *,
        tier_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of pvp tier, or a specific pvp tier

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            tier_id (int, optional): the pvp tier ID or the default 'index'

        Returns:
            dict: the index or data for the pvp tier
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pvp-tier/{tier_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pvp_tier_media(
        client,
        region_tag,
        tier_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a PvP tier by ID.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            tier_id (int): pvp tier id

        Returns:
            dict: json decoded media data for the PvP tier
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/pvp-tier/{tier_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Quest:
    @staticmethod
    def quest(
        client,
        region_tag: str,
        *,
        quest_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of quests, or a specific quest

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            quest_id (int, optional): the quest ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual quest(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/quest/{quest_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def quest_category(
        client,
        region_tag: str,
        *,
        quest_category_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of quest categories, or a specific quest category

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            quest_category_id (int, optional): the quest category ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual quest category/categories
        """
        uri = (
            f"{utils.api_host(region_tag)}/data/wow/quest/category/{quest_category_id}"
        )
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def quest_area(
        client,
        region_tag: str,
        *,
        quest_area_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of quest areas, or a specific quest area

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            quest_area_id (int, optional): the quest area ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual quest area(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/quest/area/{quest_area_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def quest_type(
        client,
        region_tag: str,
        *,
        quest_type_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of quest types, or a specific quest type

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            quest_type_id (int, optional): the quest type ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual quest type(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/quest/type/{quest_type_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Realm:
    @staticmethod
    def realm(
        client,
        region_tag: str,
        *,
        realm_slug: Optional[Union[str, int]] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of realms, or a specific realm

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_slug (str/int, optional): the pvp tier ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual realm(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/realm/{realm_slug}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def realm_search(
        client,
        region_tag,
        field_values: Dict[str, Any],
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):

        """Searches the creature utils.api for connected realm(s) that match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/realm"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)


class Region:
    @staticmethod
    def region(
        client,
        region_tag: str,
        *,
        region_req: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of region_tags, or a specific region_tag

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            region_req (int, optional): the region_tag ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual region_tag(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/region/{region_req}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Reputation:
    @staticmethod
    def reputation_faction(
        client,
        region_tag: str,
        *,
        faction_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):

        """Returns an index of reputation factions, or a specific reputation fa

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            faction_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual reputation faction(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/reputation-faction/{faction_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def reputation_tier(
        client,
        region_tag: str,
        *,
        tier_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of reputation factions, or a specific reputation fa

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            tier_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual reputation tier(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/reputation-tiers/{tier_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Spell:
    @staticmethod
    def spell(
        client,
        region_tag: str,
        spell_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of spells, or a specific spell

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            spell_id (int): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual spell(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/spell/{spell_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def spell_media(
        client,
        region_tag,
        spell_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a spell by ID.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            spell_id (int): pvp tier id

        Returns:
            dict: json decoded media data for the spell
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/spell/{spell_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def spell_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any] = None,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Searches the creature utils.api for items that match the criteria

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/search/spell"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update(
            {
                "locale": utils.localize(locale),
                "namespace": namespace("static", release, region_tag),
            }
        )

        try:
            return client.get(uri, params=field_values)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=field_values)


class Talent:
    @staticmethod
    def talent(
        client,
        region_tag: str,
        *,
        talent_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of spells, or a specific spell

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            talent_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual talent(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/talent/{talent_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def pvp_talent(
        client,
        region_tag: str,
        *,
        pvp_talent_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):

        """Returns an index of spells, or a specific spell

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            pvp_talent_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the talent index or individual talent
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/pvp-talent/{pvp_talent_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class TechTalent:
    @staticmethod
    def tech_talent_tree(
        client,
        region_tag: str,
        *,
        tree_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of tech talent trees or a tech talent tree by ID

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            tree_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual tech talent tree(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/tech-talent-tree/{tree_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def tech_talent(
        client,
        region_tag: str,
        *,
        talent_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of tech talents or a tech talent by ID

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            talent_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual tech talent(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/tech-talent/{talent_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)

    @staticmethod
    def tech_talent_media(
        client,
        region_tag: str,
        talent_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns media for a spell by ID.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            talent_id (int): pvp tier id

        Returns:
            dict: json decoded media data for the tech talent
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/media/tech-talent/{talent_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class Title:
    @staticmethod
    def title(
        client,
        region_tag: str,
        *,
        title_id: Optional[int] = "index",
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns an index of spells, or a specific spell

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            title_id (int, optional): the slug or ID of the region_tag requested

        Returns:
            dict: json decoded data for the index/individual title(s)
        """
        uri = f"{utils.api_host(region_tag)}/data/wow/title/{title_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)


class WoWToken:
    @staticmethod
    def wow_token_index(
        client,
        region_tag,
        release: Optional[str] = "retail",
        locale: Optional[str] = None,
    ):
        """Returns the WoW Token index.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual wow token
        """
        if release in utils.WOW_CLASSICS and region_tag.lower() != "cn":
            raise WoWReleaseError(
                "WoW Token API only available on retail, and CN classic markets"
            )

        uri = f"{utils.api_host(region_tag)}/data/wow/token/index"
        params = {
            "locale": utils.localize(locale),
            "namespace": namespace("static", release, region_tag),
        }

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_protected_resource(uri, "GET", params=params)
