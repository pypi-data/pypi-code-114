"""This module contains the classes for accessing game data related APIs

Class:
    Achievement
    Auction
    Azerite
    ConnectedRealm
    Covenant
    Creature
    GuildCrest
    Item
    Journal
    Media
    ModifiedCrafting
    Mount
    MythicKeystoneAffix
    MythicKeystoneDungeon
    MythicKeystoneLeaderboard
    MythicRaid
    Pet
    PlayableClass
    PlayableRace
    PlayableSpec
    Power
    Profession
    PvPSeason
    PvPTier
    Quest
    Realm
    Region
    Reputation
    Spell
    Talent
    TechTalent
    Title
    WoWToken
"""
from typing import Optional, Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:

    from client import WoWClient

from requests import Response

from .exceptions import WoWReleaseError
from battlenet_client.bnet.misc import slugify, localize


class Achievement:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def achievement_category(
        self, locale: str, category_id: Optional[int] = None
    ) -> Response:
        """Accesses a list achievement categories or specific achievement
        category if :category_id: is provided

        Args:
            locale (str): which locale to use for the request
            category_id (int, optional): the achievement's category ID or
                None(default).  None will retrieve the entire list of achievement categories

        Returns:

            dict: json decoded data for the index/individual achievement categories
        """
        if category_id:
            return self.__client.game_data(
                localize(locale), "static", "achievement-category", category_id
            )

        return self.__client.game_data(
            localize(locale), "static", "achievement-category", "index"
        )

    def achievement(
        self, locale: str, achievement_id: Optional[int] = None
    ) -> Response:
        """Returns an index of achievements, or a specific achievements

        Args:
            locale (str): which locale to use for the request
            achievement_id (int, optional): the achievement ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual achievements
        """
        if achievement_id:
            return self.__client.game_data(
                localize(locale), "static", "achievement", achievement_id
            )

        return self.__client.game_data(
            localize(locale), "static", "achievement", "index"
        )

    def achievement_media(self, locale: str, achievement_id: int) -> Response:
        """Returns media for an achievement's icon.

        Args:
            locale (str): which locale to use for the request
            achievement_id (int): the achievement ID or the word 'index'

        Returns:
            dict: json decoded media data for the achievement
        """
        return self.__client.media_data(
            localize(locale), "static", "achievement", achievement_id
        )


class Auction:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def auction(
        self,
        locale: str,
        connected_realm_id: int,
        auction_house_id: Optional[int] = None,
    ) -> Response:
        """Returns auction data.  With retail client, it returns all the auctions for the given connected realm.
        For classic titles, the results can be either the entire list, or the individual auctions

        See the Connected Realm API for information about retrieving a list of
            connected realm IDs.

        Auction house data updates at a set interval. The value was initially set
            at 1 hour; however, it might change over time without notice.

        Depending on the number of active auctions on the specified connected realm,
            the response from this game_data may be rather large, sometimes exceeding
            10 MB.

        Args:
            locale (str): which locale to use for the request
            connected_realm_id (int): the id of the connected realm
            auction_house_id (int, optional): the ID of the auction house

        Returns:
            dict: json decoded data for the index/individual auction(s)

        Raises:
            ClientError: when a client other than Client is used.
            WoWReleaseError: when an AH ID is used for the retail client
        Notes:
            Auction house functionality is not available for WoW 1.x (Vanilla Classic)
        """
        if self.__client.release == "retail" and auction_house_id is None:
            return self.__client.game_data(
                localize(locale),
                "dynamic",
                "connected-realm",
                connected_realm_id,
                "auctions",
            )

        if self.__client.release != "retail" and auction_house_id is None:
            return self.__client.game_data(
                localize(locale),
                "dynamic",
                "connected-realm",
                connected_realm_id,
                "auctions",
                "index",
            )

        if self.__client.release != "retail" and auction_house_id is not None:

            return self.__client.game_data(
                localize(locale),
                "dynamic",
                "connected-realm",
                connected_realm_id,
                "auctions",
                auction_house_id,
            )

        if self.__client.release == "retail" and auction_house_id is not None:
            raise WoWReleaseError("Auction House ID provided for retail")


class Azerite:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def azerite_essence(
        self, locale: str, essence_id: Optional[int] = None
    ) -> Response:
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            locale (str): which locale to use for the request
            essence_id (int, optional): the Azerite essence ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)
        """
        if essence_id:
            return self.__client.game_data(
                localize(locale), "static", "azerite-essence", essence_id
            )

        return self.__client.game_data(
            localize(locale), "static", "azerite-essence", "index"
        )

    def azerite_essence_search(
        self, locale: str, **field_values: Dict[str, Any]
    ) -> Response:
        """Searches for azerite essences that match `field_values`

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "azerite-essence", fields=field_values
        )

    def azerite_essence_media(self, locale: str, essence_id: int) -> Response:
        """Returns media data for an azerite essence.

        Args:
            locale (str): which locale to use for the request
            essence_id (int): the azerite essence ID

        Returns:
            dict: json decoded media data for the azerite essence
        """
        return self.__client.media_data(
            localize(locale), "static", "azerite-essence", essence_id
        )


class ConnectedRealm:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def connected_realm(
        self, locale: str, connected_realm_id: Optional[int] = None
    ) -> Response:
        """Returns an index of connected realms, or a specific connected realm. Connected realm is a group of standard
        realms that act as one large realm

        Args:
            locale (str): which locale to use for the request
            connected_realm_id (int, optional): the ID of the connected realm

        Returns:
            dict: json decoded data for the index/individual connected realms
        """
        if connected_realm_id:
            return self.__client.game_data(
                localize(locale), "dynamic", "connected-realm", connected_realm_id
            )

        return self.__client.game_data(
            localize(locale), "dynamic", "connected-realm", "index"
        )

    def connected_realm_search(
        self, locale: str, field_values: Dict[str, Any]
    ) -> Response:
        """Searches the connected realm API for connected realm(s) that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): field/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "dynamic", "connected-realm", fields=field_values
        )


class Covenant:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def covenant(self, locale: str, covenant_id: Optional[int] = None) -> Response:
        """Returns an index of covenants, or a specific covenant

        Args:
            locale (str): which locale to use for the request
            covenant_id (int, optional): the ID of the covenant or the default 'index'

        Returns:
            dict: json decoded data for the index/individual covenant
        """
        if covenant_id:
            self.__client.game_data(localize(locale), "static", "covenant", covenant_id)
        return self.__client.game_data(localize(locale), "static", "covenant", "index")

    def covenant_media(self, locale: str, covenant_id: int) -> Response:
        """Returns media for a covenant.

        Args:
            locale (str): which locale to use for the request
            covenant_id (int, optional): the covenant ID

        Returns:
            dict: json decoded media data for the covenant
        """
        return self.__client.media_data(
            localize(locale), "static", "covenant", covenant_id
        )

    def soulbind(self, locale: str, soulbind_id: Optional[int] = None) -> Response:
        """Returns an index of soulbinds, or a specific soulbind

        Args:
            locale (str): which locale to use for the request
            soulbind_id (int, optional): the ID of the soulbind or the word of 'index'

        Returns:
            dict: json decoded data for the index/individual soulbind
        """
        if soulbind_id:
            return self.__client.game_data(
                localize(locale), "static", "covenant", "soulbind", soulbind_id
            )

        return self.__client.game_data(
            localize(locale), "static", "covenant", "soulbind", "index"
        )

    def conduit(self, locale: str, conduit_id: Optional[int] = None) -> Response:
        """Returns an index of conduits, or a specific conduit

        Args:
            locale (str): which locale to use for the request
            conduit_id (int, optional): the ID of the conduit or the word of 'index'

        Returns:
            dict: json decoded data for the index/individual conduit
        """
        if conduit_id:
            return self.__client.game_data(
                localize(locale), "static", "covenant", "conduit", conduit_id
            )

        return self.__client.game_data(
            localize(locale), "static", "covenant", "conduit", "index"
        )


class Creature:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def creature_family(self, locale: str, family_id: Optional[int] = None) -> Response:
        """Returns an index of creature families, or a specific creature family

        Args:
            locale (str): which locale to use for the request
            family_id (int, optional): the creature family ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual creature family/families
        """
        if family_id:
            return self.__client.game_data(
                localize(locale), "static", "creature-family", family_id
            )

        return self.__client.game_data(
            localize(locale), "static", "creature-family", "index"
        )

    def creature_type(self, locale: str, type_id: Optional[int] = None) -> Response:
        """Returns an index of creature types, or a specific creature type

        Args:
            locale (str): which locale to use for the request
            type_id (int, optional): the creature type ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual creature type(s)
        """
        if type_id:
            return self.__client.game_data(
                localize(locale), "static", "creature-type", type_id
            )

        return self.__client.game_data(
            localize(locale), "static", "creature-type", "index"
        )

    def creature(self, locale: str, creature_id: int) -> Response:
        """Returns an index of creatures, or a specific creature

        Args:
            locale (str): which locale to use for the request
            creature_id (int, optional): the creature ID

        Returns:
            dict: json decoded data for the index/individual creature(s)
        """
        return self.__client.game_data(
            localize(locale), "static", "creature", creature_id
        )

    def creature_search(self, locale: str, field_values: Dict[str, Any]) -> Response:
        """Searches the creature API for creatures that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): matching criteria in key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "creature", fields=field_values
        )

    def creature_display_media(self, locale: str, display_id: int) -> Response:
        """Returns media for a creature display.

        Args:
            locale (str): which locale to use for the request
            display_id (int, optional): the creature display ID

        Returns:
            dict: json decoded media data for the creature display
        """
        return self.__client.media_data(
            localize(locale), "static", "creature-display", display_id
        )

    def creature_family_media(self, locale: str, family_id: int) -> Response:
        """Returns media for a creature family.

        Args:
            locale (str): which locale to use for the request
            family_id (int, optional): the creature family ID

        Returns:
            dict: json decoded media data for the creature family
        """
        return self.__client.media_data(
            localize(locale), "static", "creature-family", family_id
        )


class GuildCrest:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def guild_crest_components_index(self, locale: str) -> Response:
        """Returns an index of guild crest components.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of guild crest components
        """
        return self.__client.game_data(
            localize(locale), "static", "guild-crest", "index"
        )

    def guild_crest_border_media(self, locale: str, border_id: int) -> Response:
        """Returns media for a specific guild crest border.

        Args:
            locale (str): which locale to use for the request
            border_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild border
        """
        return self.__client.media_data(
            localize(locale), "static", "guild-crest", "border", border_id
        )

    def guild_crest_emblem_media(self, locale: str, crest_id: int) -> Response:
        """Returns media for a specific guild crest emblem.

        Args:
            locale (str): which locale to use for the request
            crest_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild crest
        """
        return self.__client.media_data(
            localize(locale), "static", "guild-crest", "emblem", crest_id
        )


class Item:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def item_class(self, locale: str, class_id: Optional[int] = None) -> Response:
        """Returns an index of item classes, or a specific item class

        Args:
            locale (str): which locale to use for the request
            class_id (int, optional): item class ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual item class(es)
        """
        if class_id:
            return self.__client.game_data(
                localize(locale), "static", "item-class", class_id
            )

        return self.__client.game_data(
            localize(locale), "static", "item-class", "index"
        )

    def item_set(self, locale: str, set_id: Optional[int] = None) -> Response:
        """Returns an index of item sets, or a specific item set

        Args:
            locale (str): which locale to use for the request
            set_id (int, optional): the item class ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual item set(s)
        """
        if set_id:
            return self.__client.game_data(
                localize(locale), "static", "item-set", set_id
            )

        return self.__client.game_data(localize(locale), "static", "item-set", "index")

    def item_subclass(self, locale: str, class_id: int, subclass_id: int) -> Response:
        """Returns an index of item subclasses, or a specific item subclass

        Args:
            locale (str): which locale to use for the request
            class_id (int): the item class ID
            subclass_id (int, optional): the item's subclass ID

        Returns:
            dict: json decoded data for the item's subclass
        """
        return self.__client.game_data(
            localize(locale),
            "static",
            "item-class",
            class_id,
            "item-subclass",
            subclass_id,
        )

    def item(self, locale: str, item_id: int) -> Response:
        """Returns an index of items, or a specific item

        Args:
            locale (str): which locale to use for the request
            item_id (int, optional): the item class ID

        Returns:
            dict: json decoded data for the individual item
        """
        return self.__client.game_data(localize(locale), "static", "item", item_id)

    def item_media(self, locale: str, item_id: int) -> Response:
        """Returns media for an item.

        Args:
            locale (str): which locale to use for the request
            item_id (int): the creature family ID

        Returns:
            dict: json decoded media data for the item
        """
        return self.__client.media_data(localize(locale), "static", "item", item_id)

    def item_search(self, locale: str, field_values: Dict[str, Any]) -> Response:
        """Searches the item API for items that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): search criteria as key/value pairs

        Returns:
             dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "item", fields=field_values
        )


class Journal:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def journal_expansion(
        self, locale: str, expansion_id: Optional[int] = None
    ) -> Response:
        """Returns an index of journal expansions, or a specific journal expansion

        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            expansion_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual journal expansion(s)
        """
        if expansion_id:
            return self.__client.game_data(
                localize(locale), "static", "journal-expansion", expansion_id
            )

        return self.__client.game_data(
            localize(locale), "static", "journal-expansion", "index"
        )

    def journal_encounter(
        self, locale: str, encounter_id: Optional[int] = None
    ) -> Response:
        """Returns an index of journal (boss) encounters, or a specific journal (boss) encounters

        Notes:
            This replaced the Boss endpoint of the community REST API
            locale (str): which locale to use for the request, default is None, using the client's locale

        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            encounter_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual journal encounter(s)
        """
        if encounter_id:
            return self.__client.game_data(
                localize(locale), "static", "journal-encounter", encounter_id
            )

        return self.__client.game_data(
            localize(locale), "static", "journal-encounter", "index"
        )

    def journal_encounter_search(
        self, locale: str, field_values: Dict[str, Any]
    ) -> Response:
        """Searches for azerite essences that match `field_values`

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "journal-encounter", fields=field_values
        )

    def journal_instance(
        self, locale: str, instance_id: Optional[int] = None
    ) -> Response:
        """Returns an index of journal instances (dungeons), or a specific journal instance (dungeon)

        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            instance_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual journal instance(s)
        """
        if instance_id:
            return self.__client.game_data(
                localize(locale), "static", "journal-instance", instance_id
            )
        return self.__client.game_data(
            localize(locale), "static", "journal-instance", "index"
        )

    def journal_instance_media(self, locale: str, instance_id: int) -> Response:
        """Returns media for an instance.

        Args:
            locale (str): which locale to use for the request
            instance_id (int): the creature family ID

        Returns:
            dict: json decoded media data for the instance
        """
        return self.__client.media_data(
            localize(locale), "static", "journal-instance", instance_id
        )


class Media:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def media_search(self, locale: str, field_values: Dict[str, Any]) -> Response:
        """Searches the media API match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): fields and values for the search criteria

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "media", fields=field_values
        )


class ModifiedCrafting:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def modified_crafting(self, locale: str) -> Response:
        """Returns an index of modified crafting recipes

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of modified crafting
        """
        return self.__client.game_data(
            localize(locale), "static", "modified-crafting", "index"
        )

    def modified_crafting_category(
        self, locale: str, category_id: Optional[int] = None
    ) -> Response:
        """Returns an index of modified crafting category index, or a specific modified crafting category

        Args:
            locale (str): which locale to use for the request
            category_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual modified crafting category/categories
        """
        if category_id:
            return self.__client.game_data(
                localize(locale), "static", "modified-crafting", "category", category_id
            )

        return self.__client.game_data(
            localize(locale), "static", "modified-crafting", "category", "index"
        )

    def modified_crafting_reagent_slot_type(
        self, locale: str, slot_type_id: Optional[int] = None
    ) -> Response:
        """Returns an index of modified crafting reagent slot type, or a specific reagent slot type

        Args:
            locale (str): which locale to use for the request
            slot_type_id (int, optional): the encounter ID or 'index'

        Returns:
            dict: json decoded data for the index/individual modified crafting reagent slot type(s)
        """
        if slot_type_id:
            return self.__client.game_data(
                localize(locale),
                "static",
                "modified-crafting",
                "reagent-slot-type",
                slot_type_id,
            )

        return self.__client.game_data(
            localize(locale),
            "static",
            "modified-crafting",
            "reagent-slot-type",
            "index",
        )


class Mount:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def mount(self, locale: str, mount_id: Optional[int] = None) -> Response:
        """Returns an index of mounts, or a specific mount

        Args:
            locale (str): which locale to use for the request
            mount_id (int, optional): the mount ID or 'index'

        Returns:
            dict: json decoded data for the index/individual mount(s)
        """
        if mount_id:
            return self.__client.game_data(
                localize(locale), "static", "mount", mount_id
            )

        return self.__client.game_data(localize(locale), "static", "mount", "index")

    def mount_search(self, locale: str, field_values: Dict[str, Any]) -> Response:
        """Searches the mount API that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): fields and values for the search criteria

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "mount", fields=field_values
        )


class MythicKeystoneAffix:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def mythic_keystone_affix(
        self, locale: str, affix_id: Optional[int] = None
    ) -> Response:
        """Returns an index of mythic keystone affixes, or a specific mythic keystone affix

        Args:
            locale (str): which locale to use for the request
            affix_id (int, optional): the affix's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone affix(es)
        """
        if affix_id:
            return self.__client.game_data(
                localize(locale), "static", "keystone-affix", affix_id
            )
        return self.__client.game_data(
            localize(locale), "static", "keystone-affix", "index"
        )

    def mythic_keystone_affix_media(self, locale: str, affix_id: int) -> Response:
        """Returns media for a mythic keystone affix.

        Args:
            locale (str): which locale to use for the request
            affix_id (int): the affix's ID

        Returns:
            dict: json decoded media data for the mythic keystone affix(es)
        """
        return self.__client.media_data(
            localize(locale), "static", "keystone-affix", affix_id
        )


class MythicKeystoneDungeon:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def mythic_keystone_dungeon(
        self, locale: str, dungeon_id: Optional[int] = None
    ) -> Response:
        """Returns an index of mythic keystone dungeons, or a specific mythic keystone dungeon

        Args:
            locale (str): which locale to use for the request
            dungeon_id (int, optional): the dungeon's ID or 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone dungeon(s)
        """
        if dungeon_id:
            return self.__client.game_data(
                localize(locale), "dynamic", "mythic-keystone", "dungeon", dungeon_id
            )
        return self.__client.game_data(
            localize(locale), "dynamic", "mythic-keystone", "dungeon", "index"
        )

    def mythic_keystone_index(self, locale: str) -> Response:
        """Returns an index of links to other documents related to Mythic Keystone dungeons.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of the mythic keystone dungeon documents
        """
        return self.__client.game_data(
            localize(locale), "dynamic", "mythic-keystone", "index"
        )

    def mythic_keystone_period(
        self, locale: str, period_id: Optional[int] = None
    ) -> Response:
        """Returns an index of mythic keystone periods, or a specific mythic keystone period

        Args:
            locale (str): which locale to use for the request
            period_id (int, optional): the keystone's period ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual for mythic keystone period(s)
        """
        if period_id:
            return self.__client.game_data(
                localize(locale), "dynamic", "mythic-keystone", "period", period_id
            )
        return self.__client.game_data(
            localize(locale), "dynamic", "mythic-keystone", "period", "index"
        )

    def mythic_keystone_season(
        self, locale: str, season_id: Optional[int] = None
    ) -> Response:
        """Returns an index of mythic keystone seasons, or a specific mythic keystone seasons

        Args:
            locale (str): which locale to use for the request
            season_id (int, optional): the keystone's season ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone season(s)
        """
        if season_id:
            return self.__client.game_data(
                localize(locale), "dynamic", "mythic-keystone", "season", season_id
            )

        return self.__client.game_data(
            localize(locale), "dynamic", "mythic-keystone", "season", "index"
        )


class MythicKeystoneLeaderboard:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def mythic_keystone_leader_board(
        self,
        locale: str,
        connected_realm_id: int,
        dungeon_id: Optional[int] = None,
        period_id: Optional[int] = None,
    ) -> Response:
        """Returns an index of mythic keystone leader boards, or a specific mythic keystone leader board

        Args:
            connected_realm_id (int): the connected realm's id
            locale (str): which locale to use for the request, default is None, using the client's locale
            dungeon_id (int, optional): the particular dungeon's ID or the word 'index'
            period_id (int, optional): the particular period to search or None when looking for the index

        Returns:
            dict: json decoded data for the index/individual mythic keystone leaderboard(s)
        """
        if dungeon_id and period_id:
            return self.__client.game_data(
                localize(locale),
                "dynamic",
                "connected-realm",
                connected_realm_id,
                "mythic-leaderboard",
                dungeon_id,
                "period",
                period_id,
            )

        return self.__client.game_data(
            localize(locale),
            "dynamic",
            "connected-realm",
            connected_realm_id,
            "mythic-leaderboard",
            "index",
        )


class MythicRaid:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def mythic_raid_leaderboard(
        self, locale: str, raid_name: str, faction: str
    ) -> Response:
        """Returns an index of mythic keystone affixes, or a specific mythic keystone affix

        Args:
            locale (str, optional): which locale to use for the request, default is None, using the client's locale
            raid_name (str): name of the raid
            faction (str): horde or alliance, defaults to alliance

        Returns:
            dict: json decoded data for the index/individual mythic raid
        """
        return self.__client.game_data(
            localize(locale),
            "dynamic",
            "leaderboard",
            "hall-of-fame",
            slugify(raid_name),
            faction,
        )


class Pet:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def pet(self, locale: str, pet_id: Optional[int] = None) -> Response:
        """Returns an index of pets, or the data about the specified pet

        Args:
            locale (str): which locale to use for the request
            pet_id (int, optional): the pet ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual pet(s)
        """
        if pet_id:
            return self.__client.game_data(localize(locale), "static", "pet", pet_id)
        return self.__client.game_data(localize(locale), "static", "pet", "index")

    def pet_media(self, locale: str, pet_id: int) -> Response:
        """Returns media for a pet

        Args:
            locale (str): which locale to use for the request
            pet_id (int): the azerite pet ID

        Returns:
            dict: json decoded media data for the for pet
        """
        return self.__client.media_data(localize(locale), "static", "pet", pet_id)

    def pet_ability(self, locale: str, pet_id: Optional[int] = None) -> Response:
        """Returns an index of pets, or the data about the specified pet

        Args:
            locale (str): which locale to use for the request
            pet_id (int, optional): the pet ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual pet ability/abilities
        """
        if pet_id:
            return self.__client.game_data(
                localize(locale), "static", "pet-ability", pet_id
            )
        return self.__client.game_data(
            localize(locale), "static", "pet-ability", "index"
        )

    def pet_ability_media(self, locale: str, ability_id: int) -> Response:
        """Returns media for an azerite ability.

        Args:
            locale (str): which locale to use for the request
            ability_id (int): the azerite ability ID

        Returns:
            dict: json decoded media data for the pet ability
        """
        return self.__client.media_data(
            localize(locale), "static", "pet-ability", ability_id
        )


class PlayableClass:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def playable_class(self, locale: str, class_id: Optional[int] = None) -> Response:
        """Returns an index of playable classes, or a specific playable class

        Args:
            locale (str): which locale to use for the request
            class_id (int, optional): the class ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable class(es)
        """
        if class_id:
            return self.__client.game_data(
                localize(locale), "static", "playable-class", class_id
            )

        return self.__client.game_data(
            localize(locale), "static", "playable-class", "index"
        )

    def playable_class_media(self, locale: str, class_id: int) -> Response:
        """Returns media for a playable class by ID.

        Args:
            locale (str): which locale to use for the request
            class_id (int ): class id

        Returns:
            dict: json decoded media data for the playable class(es)
        """
        return self.__client.media_data(
            localize(locale), "static", "playable-class", class_id
        )

    def pvp_talent_slots(self, locale: str, class_id: int) -> Response:
        """Returns the PvP talent slots for a playable class by ID.

        Args:
            locale (str): which locale to use for the request
            class_id (int): class id

        Returns:
            dict: json decoded data for the index of PvP Talent slots
        """
        return self.__client.game_data(
            localize(locale), "static", "playable-class", class_id, "pvp-talent-slots"
        )


class PlayableRace:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def playable_race(self, locale: str, race_id: Optional[int] = None) -> Response:
        """Returns an index of playable races, or a specific playable race

        Args:
            locale (str): which locale to use for the request
            race_id (int, optional): the playable race's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable race(s)
        """
        if race_id:
            return self.__client.game_data(
                localize(locale), "static", "playable-race", race_id
            )
        return self.__client.game_data(
            localize(locale), "static", "playable-race", "index"
        )


class PlayableSpec:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def playable_spec(self, locale: str, spec_id: Optional[int] = None) -> Response:
        """Returns an index of playable specialization, or a specific playable specialization

        Args:
            locale (str): which locale to use for the request
            spec_id (int, optional): the playable specialization's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable specialization(s)
        """
        if spec_id:
            return self.__client.game_data(
                localize(locale), "static", "playable-specialization", spec_id
            )
        return self.__client.game_data(
            localize(locale), "static", "playable-specialization", "index"
        )

    def playable_spec_media(self, locale: str, spec_id: int) -> Response:
        """Returns media for a playable specialization by ID.

        Args:
            locale (str): which locale to use for the request
            spec_id (int): specialization id

        Returns:
            dict: json decoded media data for the playable specialization
        """
        return self.__client.media_data(
            localize(locale), "static", "playable-specialization", spec_id
        )


class Power:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def power_type(self, locale: str, power_id: Optional[int] = None) -> Response:
        """Returns an index of power types, or a specific power type

        Args:
            locale (str): which locale to use for the request
            power_id (int, optional): the power type's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual power types
        """
        if power_id:
            return self.__client.game_data(
                localize(locale), "static", "power-type", power_id
            )
        return self.__client.game_data(
            localize(locale), "static", "power-type", "index"
        )


class Profession:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def profession(self, locale: str, profession_id: Optional[int] = None) -> Response:
        """Returns an index of achievements, or a specific achievements

        Args:
            locale (str): which locale to use for the request
            profession_id (int, optional): the profession ID or the word 'index'

        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        if profession_id:
            return self.__client.game_data(
                localize(locale), "static", "profession", profession_id
            )
        return self.__client.game_data(
            localize(locale), "static", "profession", "index"
        )

    def profession_media(self, locale: str, profession_id: int) -> Response:
        """Returns media for a creature display.

        Args:
            profession_id (int): the profession ID
            locale (str): which locale to use for the request

        Returns:
            dict: the media assets for the given creature display ID
        """
        return self.__client.media_data(
            localize(locale), "static", "profession", profession_id
        )

    def profession_skill_tier(
        self, locale: str, profession_id: int, skill_tier_id: int
    ) -> Response:
        """Returns an index of achievements, or a specific achievements

        Args:
            profession_id (int): the profession ID
            skill_tier_id (int): the skill tier ID
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        return self.__client.game_data(
            localize(locale),
            "static",
            "profession",
            profession_id,
            "skill-tier",
            skill_tier_id,
        )

    def recipe(self, locale: str, recipe_id: int):
        """Returns an index of achievements, or a specific achievements

        Args:
            recipe_id (int, optional): the recipe ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        return self.__client.game_data(localize(locale), "static", "recipe", recipe_id)

    def recipe_media(self, locale: str, recipe_id: int) -> Response:
        """Returns media for a creature display.

        Args:
            recipe_id (int): the profession ID
            locale (str): which locale to use for the request

        Returns:
            dict: the media assets for the given creature display ID
        """
        return self.__client.media_data(localize(locale), "static", "recipe", recipe_id)


class PvPSeason:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def pvp_season(self, locale: str, season_id: Optional[int] = None) -> Response:
        """Returns an index of pvp seasons, or a specific pvp season

        Args:
            locale (str): which locale to use for the request
            season_id (int, optional): the power type's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual PvP season(s)
        """
        if season_id:
            return self.__client.game_data(
                localize(locale), "dynamic", "pvp-season", season_id
            )
        return self.__client.game_data(
            localize(locale), "dynamic", "pvp-season", "index"
        )

    def pvp_leader_board(
        self, locale: str, season_id: int, pvp_bracket: Optional[str] = None
    ) -> Response:
        """Returns an index of pvp leader boards, or a specific pvp leader board

        Args:
            locale (str): which locale to use for the request
            season_id (int): pvp season's ID
            pvp_bracket (int, optional): the PvP bracket to view ('2v2', '3v3', '5v5', 'rbg') or the word 'index'

        Returns:
            dict: json decoded data for the index of the PvP leader board
        """
        if pvp_bracket:
            return self.__client.game_data(
                localize(locale),
                "dynamic",
                "pvp-season",
                season_id,
                "pvp-leaderboard",
                pvp_bracket,
            )
        return self.__client.game_data(
            localize(locale),
            "dynamic",
            "pvp-season",
            season_id,
            "pvp-leaderboard",
            "index",
        )

    def pvp_rewards_index(self, locale: str, season_id: int) -> Response:
        """Returns an index of pvp rewards, or a specific pvp reward

        Args:
            locale (str): which locale to use for the request
            season_id (int): the season ID for the rewards or the word 'index'

        Returns:
            dict: json decoded data for the index of PvP rewards
        """
        return self.__client.game_data(
            localize(locale), "dynamic", "pvp-season", season_id, "pvp-reward", "index"
        )


class PvPTier:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def pvp_tier(self, locale: str, tier_id: Optional[int] = None) -> Response:
        """Returns an index of pvp tier, or a specific pvp tier

        Args:
            locale (str): which locale to use for the request
            tier_id (int, optional): the pvp tier ID or the default 'index'

        Returns:
            dict: the index or data for the pvp tier
        """
        if tier_id:
            return self.__client.game_data(
                localize(locale), "static", "pvp-tier", tier_id
            )
        return self.__client.game_data(localize(locale), "static", "pvp-tier", "index")

    def pvp_tier_media(self, locale: str, tier_id: int) -> Response:
        """Returns media for a PvP tier by ID.

        Args:
            locale (str): which locale to use for the request
            tier_id (int): pvp tier id

        Returns:
            dict: json decoded media data for the PvP tier
        """
        return self.__client.media_data(localize(locale), "static", "pvp-tier", tier_id)


class Quest:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def quest(self, locale: str, quest_id: Optional[int] = None) -> Response:
        """Returns an index of quests, or a specific quest

        Args:
            locale (str): which locale to use for the request
            quest_id (int, optional): the quest ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual quest(s)
        """
        if quest_id:
            return self.__client.game_data(
                localize(locale), "static", "quest", quest_id
            )
        return self.__client.game_data(localize(locale), "static", "quest", "index")

    def quest_area(self, locale: str, quest_area_id: Optional[int] = None) -> Response:
        """Returns an index of quest areas, or a specific quest area

        Args:
            quest_area_id (int, optional): the quest area ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual quest area(s)
        """
        if quest_area_id:
            return self.__client.game_data(
                localize(locale), "static", "quest", "area", quest_area_id
            )
        return self.__client.game_data(
            localize(locale), "static", "quest", "area", "index"
        )

    def quest_category(
        self, locale: str, quest_category_id: Optional[int] = None
    ) -> Response:
        """Returns an index of quest categories, or a specific quest category

        Args:
            quest_category_id (int, optional): the quest category ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual quest category/categories
        """
        if quest_category_id:
            return self.__client.game_data(
                localize(locale), "static", "quest", "category", quest_category_id
            )
        return self.__client.game_data(
            localize(locale), "static", "quest", "category", "index"
        )

    def quest_type(self, locale: str, quest_type_id: Optional[int] = None) -> Response:
        """Returns an index of quest types, or a specific quest type

        Args:
            quest_type_id (int, optional): the quest type ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual quest type(s)
        """
        if quest_type_id:
            return self.__client.game_data(
                localize(locale), "static", "quest", "type", quest_type_id
            )
        return self.__client.game_data(
            localize(locale), "static", "quest", "type", "index"
        )


class Realm:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def realm(self, locale: str, realm_name: Optional[str] = None) -> Response:
        """Returns an index of realms, or a specific realm

        Args:
            locale (str): which locale to use for the request
            realm_name (str, optional): the pvp tier ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual realm(s)
        """
        if realm_name:
            return self.__client.game_data(
                localize(locale), "dynamic", "realm", slugify(realm_name)
            )
        return self.__client.game_data(localize(locale), "dynamic", "realm", "index")

    def realm_search(self, locale: str, field_values: Dict[str, Any]) -> Response:
        """Searches the creature API for connected realm(s) that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "dynamic", "realm", fields=field_values
        )


class Region:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def region(self, locale: str, region_id: Optional[int] = None) -> Response:
        """Returns an index of regions, or a specific region

        Args:
            locale (str): which locale to use for the request
            region_id (int, optional): the region ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual region(s)
        """
        if region_id:
            return self.__client.game_data(
                localize(locale), "dynamic", "region", region_id
            )
        return self.__client.game_data(localize(locale), "dynamic", "region", "index")


class Reputation:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def reputation_faction(
        self, locale: str, faction_id: Optional[int] = None
    ) -> Response:
        """Returns an index of reputation factions, or a specific reputation fa

        Args:
            locale (str): which locale to use for the request
            faction_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual reputation faction(s)
        """
        if faction_id:
            return self.__client.game_data(
                localize(locale), "static", "reputation-faction", faction_id
            )
        return self.__client.game_data(
            localize(locale), "static", "reputation-faction", "index"
        )

    def reputation_tier(self, locale: str, tier_id: Optional[int] = None) -> Response:
        """Returns an index of reputation factions, or a specific reputation fa

        Args:
            locale (str): which locale to use for the request
            tier_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual reputation tier(s)
        """
        if tier_id:
            return self.__client.game_data(
                localize(locale), "static", "reputation-tiers", tier_id
            )
        return self.__client.game_data(
            localize(locale), "static", "reputation-tiers", "index"
        )


class Spell:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def spell(self, locale: str, spell_id: int) -> Response:
        """Returns an index of spells, or a specific spell

        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            spell_id (int): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual spell(s)
        """
        return self.__client.game_data(localize(locale), "static", "spell", spell_id)

    def spell_media(self, locale: str, spell_id: int) -> Response:
        """Returns media for a spell by ID.

        Args:
            spell_id (int): pvp tier id
            locale (str): which locale to use for the request, default is None, using the client's locale

        Returns:
            dict: json decoded media data for the spell
        """
        return self.__client.media_data(localize(locale), "static", "spell", spell_id)

    def spell_search(
        self, locale: str, field_values: Dict[str, Any] = None
    ) -> Response:
        """Searches the creature API for items that match the criteria

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        return self.__client.search(
            localize(locale), "static", "spell", fields=field_values
        )


class Talent:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def talent(self, locale: str, talent_id: Optional[int] = None) -> Response:
        """Returns an index of spells, or a specific spell

        Args:
            locale (str): which locale to use for the request
            talent_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual talent(s)
        """
        if talent_id:
            return self.__client.game_data(
                localize(locale), "static", "talent", talent_id
            )
        return self.__client.game_data(localize(locale), "static", "talent", "index")

    def pvp_talent(self, locale: str, pvp_talent_id: Optional[int] = None) -> Response:
        """Returns an index of spells, or a specific spell

        Args:
            locale (str): which locale to use for the request
            pvp_talent_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the talent index or individual talent
        """
        if pvp_talent_id:
            return self.__client.game_data(
                localize(locale), "static", "pvp-talent", pvp_talent_id
            )
        return self.__client.game_data(
            localize(locale), "static", "pvp-talent", "index"
        )


class TechTalent:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def tech_talent_tree(self, locale: str, tree_id: Optional[int] = None) -> Response:
        """Returns an index of tech talent trees or a tech talent tree by ID

        Args:
            locale (str): which locale to use for the request
            tree_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual tech talent tree(s)
        """
        if tree_id:
            return self.__client.game_data(
                localize(locale), "static", "tech-talent-tree", tree_id
            )
        return self.__client.game_data(
            localize(locale), "static", "tech-talent-tree", "index"
        )

    def tech_talent(self, locale: str, talent_id: Optional[int] = None) -> Response:
        """Returns an index of tech talents or a tech talent by ID

        Args:
            locale (str): which locale to use for the request
            talent_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual tech talent(s)
        """
        if talent_id:
            return self.__client.game_data(
                localize(locale), "static", "tech-talent", talent_id
            )
        return self.__client.game_data(
            localize(locale), "static", "tech-talent", "index"
        )

    def tech_talent_media(self, locale: str, talent_id: int) -> Response:
        """Returns media for a spell by ID.

        Args:
            locale (str): which locale to use for the request
            talent_id (int): pvp tier id

        Returns:
            dict: json decoded media data for the tech talent
        """
        return self.__client.media_data(
            localize(locale), "static", "tech-talent", talent_id
        )


class Title:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def title(self, locale: str, title_id: Optional[int] = None) -> Response:
        """Returns an index of spells, or a specific spell

        Args:
            locale (str): which locale to use for the request
            title_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual title(s)
        """
        if title_id:
            return self.__client.game_data(
                localize(locale), "static", "title", title_id
            )
        return self.__client.game_data(localize(locale), "static", "title", "index")


class WoWToken:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def wow_token_index(self, locale: str) -> Response:
        """Returns the WoW Token index.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual wow token
        """
        if (
            self.__client.release in ("classic1x", "classic")
            and self.__client.tag != "cn"
        ):
            raise WoWReleaseError(
                "WoW Token API only available on retail, and CN classic markets"
            )

        return self.__client.game_data(localize(locale), "dynamic", "token", "index")
