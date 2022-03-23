"""Defines the classes that handle the community APIs for Diablo III"""

from typing import Optional

from urllib.parse import quote

from battlenet_client import utils


class Community:
    """Defines the methods to communicate with the Community API"""

    @staticmethod
    def act(
        client,
        region_tag: str,
        *,
        act_id: Optional[int] = None,
        locale: Optional[str] = None,
    ):
        """Returns the list of acts, or the act by :act_id:

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            act_id (int, optional): the act's ID to retrieve its data

        Returns:
            dict: the dict containing the list of acts or the details of the specified :act_id:
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/act"

        if act_id:
            uri += f"/{act_id}"

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def artisan(
        client, region_tag: str, artisan_slug: str, locale: Optional[str] = None
    ):
        """Returns the artisan by the slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            artisan_slug (str): the slug of the artisan

        Returns:
            dict: the dict containing data of the artisan
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/artisan/{utils.slugify(artisan_slug)}"
        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def recipe(
        client,
        region_tag: str,
        artisan_slug: str,
        recipe_slug: str,
        locale: Optional[str] = None,
    ):
        """Returns a single recipe by the by slug for the specified artisan

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            artisan_slug (str): the slug of the artisan
            recipe_slug (str): the slug of the recipe

        Returns:
            dict: the dict containing for the recipe
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/artisan/{utils.slugify(artisan_slug)}/recipe"
        uri += f"/{utils.slugify(recipe_slug)}"
        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def follower(
        client, region_tag: str, follower_slug: str, locale: Optional[str] = None
    ):
        """Returns the follower by slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            follower_slug (str): the slug of a follower

        Returns:
            dict: the dict containing for the follower
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/follower/{utils.slugify(follower_slug)}"
        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def character_class(
        client, region_tag: str, class_slug: str, locale: Optional[str] = None
    ):
        """Returns a single character class by slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_slug (str): the slug of a character class

        Returns:
            dict: the dict containing for the character class
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/hero/{utils.slugify(class_slug)}"
        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def api_skill(
        client,
        region_tag: str,
        class_slug: str,
        skill_slug: str,
        locale: Optional[str] = None,
    ):
        """Returns a single skill by the by slug for the specified character class

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            class_slug (str): the slug of a character class
            skill_slug (str):

        Returns:
            dict: the dict containing for the skill
        """

        uri = f"{utils.api_host(region_tag)}/d3/data/hero/{utils.slugify(class_slug)}"
        uri += f"/skill/{utils.slugify(skill_slug)}"
        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def item_type(
        client,
        region_tag: str,
        *,
        item_slug: Optional[str] = None,
        locale: Optional[str] = None,
    ):
        """Returns the index of item types, or a specific item type

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            item_slug (str, optional): the slug of an item type

        Returns:
            dict: the dict containing for the item type
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/item-type"

        if item_slug:
            uri += f"/{utils.slugify(item_slug)}"

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def item(client, region_tag: str, item_slug: str, locale: Optional[str] = None):
        """Returns the item by slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            item_slug (str): the slug of the item

        Returns:
            dict: the dict containing for the item
        """
        uri = f"{utils.api_host(region_tag)}/d3/data/item/{utils.slugify(item_slug)}"

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def api_account(
        client, region_tag: str, bnet_tag: str, locale: Optional[str] = None
    ):
        """Returns the specified account profile

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            bnet_tag (str): bnet tag of the user

        Returns:
            dict: the dict containing for the account
        """
        uri = f"{utils.api_host(region_tag)}/d3/profile/{bnet_tag}"

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)

    @staticmethod
    def api_hero(
        client,
        region_tag: str,
        locale: str,
        bnet_tag: str,
        hero_id: str,
        category: Optional[str] = None,
    ):
        """Returns the follower by slug

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            bnet_tag (str): BNet tag for the account
            hero_id (str):  Hero's ID
            category (str): category to retrieve if specified ('items', 'follower-items')

        Returns:
            dict: the dict containing for the hero, items, or follower's items
        """
        uri = (
            f"{utils.api_host(region_tag)}/d3/profile/{quote(bnet_tag)}/hero/{hero_id}"
        )

        if category:

            if category not in ("items", "follower-items"):
                raise ValueError(
                    "Invalid category;  Valid categories are 'items' and 'follower-items'"
                )

            uri += f"/{category.lower()}"

        params = {"locale": utils.localize(locale)}

        try:
            return client.get(uri, params=params)
        except AttributeError:
            return client.fetch_proctected_resource(uri, "GET", params=params)
