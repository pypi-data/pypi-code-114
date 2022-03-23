"""This module contains the classes for accessing profile related APIs

Classes:
    Account
    CharacterAchievements
    CharacterAppearance
    CharacterCollections
    CharacterEncounters
    CharacterEquipment
    CharacterHunterPets
    CharacterMedia
    CharacterMythicKeystone
    CharacterProfession
    CharacterProfile
    CharacterPvP
    CharacterQuests
    CharacterReputations
    CharacterSoulBinds
    CharacterSpecializations
    CharacterStatistics
    CharacterTitles
    Guild
"""

from typing import Optional, TYPE_CHECKING

from requests import Response

if TYPE_CHECKING:
    from .client import WoWClient

from battlenet_client.bnet.misc import slugify
from .exceptions import WoWReleaseError, WoWClientError


class Account:
    def __init__(self, client: "WoWClient") -> None:
        if client.auth_flow:
            self.__client = client
        else:
            raise WoWClientError("Requires authorization client")

    def account_profile_summary(self, locale: Optional[str] = None) -> Response:
        """Accesses a summary of the account

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: JSON decoded data that contains the profile summary
        """
        return self.__client.protected_data(locale, "profile")

    def protected_character_profile_summary(
        self, locale: str, realm_id: int, character_id: int
    ) -> Response:
        """Accesses a summary of protected account information for the
        character identified by :realm_id: and :character_id:

        Args:
            locale (str): which locale to use for the request
            realm_id (int): the ID for the character's realm
            character_id (int): the ID of character

        Returns:
            dict: JSON decoded data that contains the protected character
                profile summary
        """
        return self.__client.protected_data(
            locale, "profile", "protected-character", realm_id, character_id
        )

    def account_collections(
        self, locale: str, category: Optional[str] = None
    ) -> Response:
        """Access the collection of battle pets and/or mounts of an account as
        provided by :category:

        Args:
            locale (str): which locale to use for the request
            category (str): 'pets' to retrieve the pet collections, and
                'mounts' to retrieve the mount collection of the account or
                None for both pets and mounts

        Returns:
            dict: JSON decoded data for the index/individual collections
        """
        if category is not None:
            return self.__client.protected_data(
                locale, "profile", "collections", slugify(category)
            )
        return self.__client.protected_data(locale, "profile", "collections")


class CharacterAchievements:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def achievement_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the achievement summary of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested achievement summary
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "achievements",
        )

    def achievement_statistics(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the achievement statistics for the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains the requested achievement statistics
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "achievements",
            "statistics",
        )


class CharacterAppearance:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def appearance_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the appearance summary for the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested appearance summary
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "appearance",
        )


class CharacterCollections:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def collections(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        category: Optional[str] = None,
    ) -> Response:
        """Accesses the battle pet and/or mount collections for the requested
        character identified by :character_name: on realm :realm_name: of the
        given :category:.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            category (str): category to retrieve. options are pets or mounts, or None (default).  None will
                provide both

        Returns:
            dict: JSON decoded data that contains requested collection
        """
        if category:
            if category.lower() not in ("pets", "mounts"):
                raise ValueError("Category needs to pets or mounts")

            return self.__client.profile_data(
                locale,
                "profile",
                "character",
                slugify(realm_name),
                slugify(character_name),
                "collections",
                category.lower(),
            )
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "collections",
        )


class CharacterEncounters:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def encounters(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        category: Optional[str] = None,
    ) -> Response:
        """Accesses the encounters for the requested character identified by
        :character_name: on realm :realm_name:.  The encounters can be limited
        by :category:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            category (str): category to retrieve.  options are 'dungeons',
                'raids', or None (default).  None will access both dungeons and raids

        Returns:
            dict: JSON decoded dict that contains requested encounter data or index
        """

        if category:
            if category.lower() not in ("dungeons", "raids"):
                raise ValueError("Available Categories: None, dungeons and raids")
            return self.__client.profile_data(
                locale,
                "profile",
                "character",
                slugify(realm_name),
                slugify(character_name),
                "encounters",
                slugify(category),
            )
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "encounters",
        )


class CharacterEquipment:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def equipment_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the equipped items of the requested character identified by
        :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded dict that contains requested equipment summary
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "equipment",
        )


class CharacterHunterPets:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def hunter_pets_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Access the list of hunter pets of the requested character identified
        by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the hunter's pets
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "hunter-pets",
        )


class CharacterMedia:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def media_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the media assets, such as avatar render, of the requested
        character identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested media assets
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "character-media",
        )


class CharacterMythicKeystone:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def mythic_keystone(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        season_id: Optional[int] = None,
    ) -> Response:
        """Accesses the mythic keystone (M+ or Mythic+) information of the
        requested character identified by :character_name: on realm
        :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            season_id (int or None): season id or None (default).  None
                accesses the list of seasons for the current expansion

        Returns:
            dict: JSON decoded data of requested mythic keystone details
        """
        if season_id:
            return self.__client.profile_data(
                locale,
                "profile",
                "character",
                slugify(realm_name),
                slugify(character_name),
                "mythic-keystone-profile",
                "season",
                season_id,
            )
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "mythic-keystone-profile",
        )


class CharacterProfessions:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def professions_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the profession information of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's professions
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "professions",
        )


class CharacterProfile:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def profile(
        self, locale: str, realm_name: str, character_name: str, status: bool = False
    ) -> Response:
        """Access the profile status of the requested character identified by
        :character_name: on realm :realm_name:

        When requesting the character profile status, a note from Blizzard:

        Returns the status and a unique ID for a character. A client should
        delete information about a character from their application if
        any of the following conditions occur:

            1) an HTTP 404 Not Found error is returned
            2) the is_valid value is false
            3) the returned character ID doesn't match the previously recorded
                value for the character

        The following example illustrates how to use this endpoint:
            1) A client requests and stores information about a character, including
            its unique character ID and the timestamp of the request.
            2) After 30 days, the client makes a request to the status endpoint to
            verify if the character information is still valid.
            3) If character cannot be found, is not valid, or the characters IDs do
            not match, the client removes the information from their application.
            4) If the character is valid and the character IDs match, the client retains
            the data for another 30 days.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            status (bool): flag to request a profile summary (False default) or status (True)

        Returns:
            dict: JSON decoded data of character profile summary
        """

        if status:
            return self.__client.profile_data(
                locale,
                "profile",
                "character",
                slugify(realm_name),
                slugify(character_name),
                "status",
            )
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
        )


class CharacterPvP:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def pvp(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        pvp_bracket: Optional[str] = None,
    ) -> Response:
        """Accesses the Player versus Player (PvP) information of the requested
        character identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            pvp_bracket (str or None): '2v2', '3v3', 'rbg', None (default).
                None returns a summary of pvp activity

        Returns:
            dict: JSON decoded data of requested pvp details
        """

        if pvp_bracket:
            return self.__client.profile_data(
                locale,
                "profile",
                "character",
                slugify(realm_name),
                slugify(character_name),
                "pvp-bracket",
                pvp_bracket,
            )
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "pvp-summary",
        )


class CharacterQuests:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def quests(
        self, locale: str, realm_name: str, character_name: str, completed: bool = False
    ) -> Response:
        """Accesses the all or just completed quest information of the
        requested character identified by :character_name: on realm
        :realm_name:.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            completed (bool):  To show all quests (False), or to show only
                completed quests (True)
        Returns:
            dict: JSON decoded data of the completed or uncompleted quests
        """

        if completed:
            return self.__client.profile_data(
                locale,
                "profile",
                "character",
                slugify(realm_name),
                slugify(character_name),
                "quests",
                "completed",
            )
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "quests",
        )


class CharacterReputations:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def reputations_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the reputation data of the requested character identified
        by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's reputations
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "reputations",
        )


class CharacterSoulBinds:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def soulbinds(
        self, realm_name: str, character_name: str, locale: Optional[str] = None
    ) -> Response:
        """Accesses the available soulbinds of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's soulbinds
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "soulbinds",
        )


class CharacterSpecializations:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def specializations_summary(
        self, realm_name: str, character_name: str, locale: Optional[str] = None
    ) -> Response:
        """Access the available specializations of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's specializations
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "specializations",
        )


class CharacterStatistics:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def statistics_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the statistics of the requested character identified by
        :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's statistics
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "statistics",
        )


class CharacterTitles:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def title_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Response:
        """Accesses the list of titles earned by the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data the titles the player has earned
        """
        return self.__client.profile_data(
            locale,
            "profile",
            "character",
            slugify(realm_name),
            slugify(character_name),
            "titles",
        )


class Guild:
    def __init__(self, client: "WoWClient") -> None:
        self.__client = client

    def guild(
        self, realm_name: str, guild_name: str, locale: Optional[str] = None
    ) -> Response:
        """Returns a single guild by its name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild
        """
        if self.__client.release != "retail":
            raise WoWReleaseError(
                f"{self.__client.release} does not support the Guild Data API"
            )

        return self.__client.game_data(
            locale,
            "profile",
            "guild",
            slugify(realm_name),
            slugify(guild_name),
        )

    def guild_activities(
        self, realm_name: str, guild_name: str, locale: Optional[str] = None
    ) -> Response:
        """Returns a single guild's activity by name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild activities
        """
        if self.__client.release != "retail":
            raise WoWReleaseError(
                f"{self.__client.release} does not support the Guild Data API"
            )

        return self.__client.game_data(
            locale,
            "profile",
            "guild",
            slugify(realm_name),
            slugify(guild_name),
            "activity",
        )

    def guild_achievements(
        self, realm_name: str, guild_name: str, locale: Optional[str] = None
    ) -> Response:
        """Returns a single guild's achievements by name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild achievements
        """
        if self.__client.release != "retail":
            raise WoWReleaseError(
                f"{self.__client.release} does not support the Guild Data API"
            )

        return self.__client.game_data(
            locale,
            "profile",
            "guild",
            slugify(realm_name),
            slugify(guild_name),
            "achievements",
        )

    def guild_roster(
        self, realm_name: str, guild_name: str, locale: Optional[str] = None
    ) -> Response:
        """Returns a single guild's roster by its name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if self.__client.release != "retail":
            raise WoWReleaseError(
                f"{self.__client.release} does not support the Guild Data API"
            )

        return self.__client.game_data(
            locale,
            "profile",
            "guild",
            slugify(realm_name),
            slugify(guild_name),
            "roster",
        )

    def guild_crest_components_index(self, locale: Optional[str] = None) -> Response:
        """Returns an index of guild crest components.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of guild crest components
        """
        return self.__client.game_data(locale, "static", "guild-crest", "index")

    def guild_crest_border_media(
        self, border_id: int, locale: Optional[str] = None
    ) -> Response:
        """Returns media for a specific guild crest border.

        Args:
            locale (str): which locale to use for the request
            border_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild border
        """
        return self.__client.media_data(
            locale, "static", "guild-crest", "border", border_id
        )

    def guild_crest_emblem_media(
        self, crest_id: int, locale: Optional[str] = None
    ) -> Response:
        """Returns media for a specific guild crest emblem.

        Args:
            locale (str): which locale to use for the request
            crest_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild crest
        """
        return self.__client.media_data(
            locale, "static", "guild-crest", "emblem", crest_id
        )
