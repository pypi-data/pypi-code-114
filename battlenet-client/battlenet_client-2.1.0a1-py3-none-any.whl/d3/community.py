"""Defines the classes that handle the community APIs for Diablo III

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""

from typing import Optional, TYPE_CHECKING

from requests import Response

if TYPE_CHECKING:

    from client import D3Client

from urllib.parse import quote

from battlenet_client.bnet.misc import slugify


class Community:
    def __init__(self, client: "D3Client") -> None:
        self.__client = client

    def __repr__(self):
        return self.__name__

    def act(self, locale: str, act_id: Optional[int] = None) -> Response:
        """Returns an index of acts, or the act by ID

        Args:
            locale (str): localization to use with API
            act_id (int, optional): the act's ID to retrieve its data

        Returns:
            dict: the dict containing the list of acts or the details of the specified :act_id:
        """
        if act_id:
            return self.__client.community(locale, "act", act_id)

        return self.__client.community(locale, "act")

    def artisan(self, locale: str, artisan_slug: str) -> Response:
        """Returns the artisan by the slug

        Args:
            locale (str): localization to use with API
            artisan_slug (str): the slug of the artisan

        Returns:
            dict: the dict containing data of the artisan
        """
        return self.__client.community(locale, "artisan", slugify(artisan_slug))

    def recipe(self, locale: str, artisan_slug: str, recipe_slug: str) -> Response:
        """Returns a single recipe by the by slug for the specified artisan

        Args:
            locale (str): localization to use with API
            artisan_slug (str): the slug of the artisan
            recipe_slug (str): the slug of the recipe

        Returns:
            dict: the dict containing for the recipe
        """
        return self.__client.community(
            locale, "artisan", slugify(artisan_slug), "recipe", slugify(recipe_slug)
        )

    def follower(self, locale: str, follower_slug: str) -> Response:
        """Returns the follower by slug

        Args:
            locale (str): localization to use with API
            follower_slug (str): the slug of a follower

        Returns:
            dict: the dict containing for the follower
        """
        return self.__client.community(locale, "follower", slugify(follower_slug))

    def character_class(self, locale: str, class_slug: str) -> Response:
        """Returns a single character class by slug

        Args:
            locale (str): localization to use with API
            class_slug (str): the slug of a character class

        Returns:
            dict: the dict containing for the character class
        """
        return self.__client.community(locale, "hero", slugify(class_slug))

    def api_skill(self, locale: str, class_slug: str, skill_slug: str) -> Response:
        """Returns a single skill by the by slug for the specified character class

        Args:
            locale (str): localization to use with API
            class_slug (str): the slug of a character class
            skill_slug (str):

        Returns:
            dict: the dict containing for the skill
        """

        return self.__client.community(
            locale,
            "hero",
            slugify(class_slug),
            "skill",
            slugify(skill_slug),
        )

    def item_type(self, locale: str, item_slug: Optional[str] = None) -> Response:
        """Returns the index of item types, or a specific item type

        Args:
            locale (str): localization to use with API
            item_slug (str, optional): the slug of an item type

        Returns:
            dict: the dict containing for the item type
        """

        if item_slug:
            return self.__client.community(locale, "item-type", slugify(item_slug))

        return self.__client.community(locale, "item-type")

    def item(self, locale: str, item_slug: str) -> Response:
        """Returns the item by slug

        Args:
            locale (str): localization to use with API
            item_slug (str): the slug of the item

        Returns:
            dict: the dict containing for the item
        """
        return self.__client.community(locale, "item", item_slug)

    def api_account(self, locale: str, bnet_tag: str) -> Response:
        """Returns the specified account profile

        Args:
            locale (str): localization to use with API
            bnet_tag (str): bnet tag of the user

        Returns:
            dict: the dict containing for the account
        """
        return self.__client.profile_api(locale, f"{quote(bnet_tag)}/")

    def api_hero(
        self, locale: str, bnet_tag: str, hero_id: str, category: Optional[str] = None
    ) -> Response:
        """Returns the follower by slug

        Args:
            locale (str): localization to use with API
            bnet_tag (str): BNet tag for the account
            hero_id (str):  Hero's ID
            category (str): category to retrieve if specified ('items', 'follower-items')

        Returns:
            dict: the dict containing for the hero, items, or follower's items
        """
        if category:
            if category in ("items", "follower-items"):
                return self.__client.profile_api(
                    locale, quote(bnet_tag), "hero", hero_id, category
                )
            else:
                raise ValueError(
                    "Invalid category;  Valid categories are 'items' and 'follower-items'"
                )
        else:
            return self.__client.profile_api(locale, quote(bnet_tag), "hero", hero_id)


class CommunityCN:
    def __init__(self, client: "D3Client") -> None:
        self.__client = client

    def act(self, locale: str, act_id: Optional[int] = None) -> Response:
        """Returns an index of acts, or the act by ID

        Args:
            locale (str): localization to use with API
            act_id (int, optional): the act's ID to retrieve its data

        Returns:
            dict: the dict containing the list of acts or the details of the specified :act_id:
        """

        if act_id:
            return self.__client.community(locale, "act", act_id)

        return self.__client.community(locale, "act")

    def artisan(self, locale: str, artisan_slug: str) -> Response:
        """Returns the artisan by the slug

        Args:
            locale (str): localization to use with API
            artisan_slug (str): the slug of the artisan

        Returns:
            dict: the dict containing data of the artisan
        """
        return self.__client.community(locale, "artisan", artisan_slug)

    def recipe(self, locale: str, artisan_slug: str, recipe_slug: str) -> Response:
        """Returns a single recipe by the by slug for the specified artisan

        Args:
            locale (str): localization to use with API
            artisan_slug (str): the slug of the artisan
            recipe_slug (str): the slug of the recipe

        Returns:
            dict: the dict containing for the recipe
        """
        return self.__client.community(
            locale, "artisan", artisan_slug, "recipe", slugify(recipe_slug)
        )

    def follower(self, locale: str, follower_slug: str) -> Response:
        """Returns the follower by slug

        Args:
            locale (str): localization to use with API
            follower_slug (str): the slug of a follower

        Returns:
            dict: the dict containing for the follower
        """
        return self.__client.community(locale, "follower", slugify(follower_slug))

    def character_class(self, locale: str, class_slug: str) -> Response:
        """Returns a single character class by slug

        Args:
            locale (str): localization to use with API
            class_slug (str): the slug of a character class

        Returns:
            dict: the dict containing for the character class
        """
        return self.__client.community(locale, "hero", slugify(class_slug))

    def api_skill(self, locale: str, class_slug: str, skill_slug: str) -> Response:
        """Returns a single skill by the by slug for the specified character class

        Args:
            locale (str): localization to use with API
            class_slug (str): the slug of a character class
            skill_slug (str):

        Returns:
            dict: the dict containing for the skill
        """
        return self.__client.community(
            locale,
            "hero",
            slugify(class_slug),
            "skill",
            slugify(skill_slug),
        )

    def item_type(self, locale: str, item_slug: Optional[str] = None) -> Response:
        """Returns the index of item types, or a specific item type

        Args:
            locale (str): localization to use with API
            item_slug (str, optional): the slug of an item type

        Returns:
            dict: the dict containing for the item type
        """
        if item_slug:
            return self.__client.community(locale, "item-type", slugify(item_slug))

        return self.__client.community(locale, "item-type")

    def item(self, locale: str, item_slug: str) -> Response:
        """Returns the item by slug

        Args:
            locale (str): localization to use with API
            item_slug (str): the slug of the item

        Returns:
            dict: the dict containing for the item
        """
        return self.__client.community(locale, "item", item_slug)

    def api_account(self, locale: str, bnet_tag: str) -> Response:
        """Returns the specified account profile

        Args:
            locale (str): localization to use with API
            bnet_tag (str): bnet tag of the user

        Returns:
            dict: the dict containing for the account
        """
        return self.__client.profile_api(locale, f"{quote(bnet_tag)}/")

    def api_hero(
        self, locale: str, bnet_tag: str, hero_id: str, category: Optional[str] = None
    ) -> Response:
        """Returns the follower by slug

        Args:
            locale (str): localization to use with API
            bnet_tag (str): BNet tag for the account
            hero_id (str):  Hero's ID
            category (str): category to retrieve if specified ('items', 'follower-items')

        Returns:
            dict: the dict containing for the hero, items, or follower's items
        """
        if category:
            if category in ("items", "follower-items"):
                return self.__client.profile_api(
                    locale, quote(bnet_tag), "hero", hero_id, category
                )
            else:
                raise ValueError(
                    "Invalid category;  Valid categories are 'items' and 'follower-items'"
                )
        else:
            return self.__client.profile_api(locale, quote(bnet_tag), "hero", hero_id)
