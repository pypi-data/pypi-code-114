"""This module defines access to the API endpoints from Battle.net, not a game

.. moduleauthor: David Couples <gahdania@gahd.io>
"""
from battlenet_client.exceptions import BNetClientError


class BattleNetAPI:

    def __init__(self, client):
        self.client = client

    def user_info(self, locale):
        """Accesses the user's information

        Args:
            locale (str): localization to use,

        Returns:
            dict: the json decoded information for the user (user # and battle tag ID)

        Notes:
            this function requires the BattleNet Client to be use OAuth (Authentication Workflow)
        """
        if not self.client.auth_flow:
            raise BNetClientError("Requires Authorization Code Workflow")

        url = f"{self.client.auth_host}/oauth/userinfo"
        return self.client.api_get(url, locale, None)
