"""Defines the methods for accessing user data from Battle.net

"""

from typing import Optional

from battlenet_client import utils


class OAuth:
    @staticmethod
    def user_info(client, region_tag: str, locale: Optional[str] = None):
        """Returns the user info

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: User Information (user # and battle tag ID)

        Notes:
            This function requires an OpenID, or OAuth V2 Client using the authorization code flow
        """

        url = f"{utils.auth_host(region_tag)}/oauth/userinfo"

        params = {"locale": utils.localize(locale)}

        try:
            return client.post(url, params=params)
        except AttributeError:
            return client.fetch_protected_resource(url, "POST", params=params)
