"""This module contains the classes for accessing profile related APIs
"""
from urllib.parse import quote
from typing import Optional


from battlenet_client import utils
from .exceptions import WoWReleaseError


class Account:
    @staticmethod
    def account_profile_summary(
        client,
        region_tag: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses a summary of the account

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: JSON decoded data that contains the profile summary
        """
        uri = f"{utils.api_host(region_tag)}/profile/user/wow"
        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def protected_character_profile_summary(
        client,
        region_tag: str,
        realm_id: int,
        character_id: int,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses a summary of protected account information for the
        character identified by :realm_id: and :character_id:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_id (int): the ID for the character's realm
            character_id (int): the ID of character

        Returns:
            dict: JSON decoded data that contains the protected character
                profile summary
        """
        uri = f"{utils.api_host(region_tag)}/profile/user/wow/protected-character/{realm_id}-{character_id}"
        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def account_collections(
        client,
        region_tag: str,
        *,
        locale: Optional[str] = None,
        category: Optional[str] = "",
        release: Optional[str] = "retail",
    ):
        """Access the collection of battle pets and/or mounts of an account as
        provided by :category:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            category (str): 'pets' to retrieve the pet collections, and
                'mounts' to retrieve the mount collection of the account or
                None for both pets and mounts

        Returns:
            dict: JSON decoded data for the index/individual collections
        """
        uri = f"{utils.api_host(region_tag)}/profile/user/wow/collections/{category}"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)


class Character:
    @staticmethod
    def achievement_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the achievement summary of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested achievement summary
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += (
            f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/achievements"
        )

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def achievement_statistics(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the achievement statistics for the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains the requested achievement statistics
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/achievements/statistics"
        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def appearance_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the appearance summary for the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested appearance summary
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/appearance"
        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def collections(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        category: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the battle pet and/or mount collections for the requested
        character identified by :character_name: on realm :realm_name: of the
        given :category:.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            category (str): category to retrieve. options are pets or mounts, or None (default).  None will
                provide both

        Returns:
            dict: JSON decoded data that contains requested collection
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += (
            f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/collections"
        )

        if category:
            if category.lower() not in ("pets", "mounts"):
                raise ValueError("Category needs to pets or mounts")
            uri += f"/{utils.slugify(category)}"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def encounters(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        category: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the encounters for the requested character identified by
        :character_name: on realm :realm_name:.  The encounters can be limited
        by :category:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            category (str): category to retrieve.  options are 'dungeons',
                'raids', or None (default).  None will access both dungeons and raids

        Returns:
            dict: JSON decoded dict that contains requested encounter data or index
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/encounters"

        if category:
            if category.lower() not in ("dungeons", "raids"):
                raise ValueError("Available Categories: None, dungeons and raids")
            uri += f"/{utils.slugify(category)}"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def equipment_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the equipped items of the requested character identified by
        :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded dict that contains requested equipment summary
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/equipment"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def hunter_pets_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Access the list of hunter pets of the requested character identified
        by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the hunter's pets
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += (
            f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/hunter-pets"
        )

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def media_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the media assets, such as avatar render, of the requested
        character identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested media assets
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/character-media"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def mythic_keystone(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        season_id: Optional[int] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the mythic keystone (M+ or Mythic+) information of the
        requested character identified by :character_name: on realm
        :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            season_id (int or None): season id or None (default).  None
                accesses the list of seasons for the current expansion

        Returns:
            dict: JSON decoded data of requested mythic keystone details
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/mythic-keystone-profile"

        if season_id:
            uri += f"/season/{season_id}"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def professions_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the profession information of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's professions
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += (
            f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/professions"
        )

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def profile(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        status: bool = False,
        release: Optional[str] = "retail",
    ):
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
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            status (bool): flag to request a profile summary (False default) or status (True)

        Returns:
            dict: JSON decoded data of character profile summary
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{quote(character_name.lower())}"

        if status:
            uri += "/status"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def pvp(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        pvp_bracket: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the Player versus Player (PvP) information of the requested
        character identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            pvp_bracket (str or None): '2v2', '3v3', 'rbg', None (default).
                None returns a summary of pvp activity

        Returns:
            dict: JSON decoded data of requested pvp details
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}"

        if pvp_bracket:
            uri += f"/pvp-bracket/{utils.slugify(pvp_bracket)}"
        else:
            uri += "/pvp-summary"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def quests(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        completed: Optional[bool] = False,
        release: Optional[str] = "retail",
    ):
        """Accesses the all or just completed quest information of the
        requested character identified by :character_name: on realm
        :realm_name:.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            completed (bool):  To show all quests (False), or to show only
                completed quests (True)

        Returns:
            dict: JSON decoded data of the completed or uncompleted quests
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/quests"

        if completed:
            uri += f"/completed"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def reputations_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the reputation data of the requested character identified
        by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's reputations
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += (
            f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/reputations"
        )

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def soulbinds(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the available soulbinds of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's soulbinds
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/soulbinds"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def specializations_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Access the available specializations of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's specializations
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/specializations"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def statistics_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the statistics of the requested character identified by
        :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's statistics
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/statistics"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)

    @staticmethod
    def title_summary(
        client,
        region_tag: str,
        realm_name: str,
        character_name: str,
        *,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Accesses the list of titles earned by the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data the titles the player has earned
        """
        uri = f"{utils.api_host(region_tag)}/profile/wow/character/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(character_name)}/titles"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)


class Guild:
    @staticmethod
    def guild(
        client,
        region_tag: str,
        realm_name: str,
        guild_name: str,
        *,
        category: Optional[str] = None,
        locale: Optional[str] = None,
        release: Optional[str] = "retail",
    ):
        """Returns a single guild by its name and realm.

        Args:
            client (obj: oauth): OpenID/OAuth instance
            release (str): release of the game (ie classic1x, classic, retail)
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild
            category (str): category of guild data to retrieve

        Returns:
            dict: json decoded data of the guild
        """
        if release != "retail":
            raise WoWReleaseError(
                f"{release.title()} does not support the Guild Data API"
            )

        uri = f"{utils.api_host(region_tag)}/data/wow/guild/"
        uri += f"{utils.slugify(realm_name)}/{utils.slugify(guild_name)}"

        if category and category in ("activity", "achievements", "roster"):
            uri += f"/{category}"

        params = {
            "locale": utils.localize(locale),
            "namespace": utils.namespace("profile", release, region_tag),
        }
        return client.get(uri, params=params)
