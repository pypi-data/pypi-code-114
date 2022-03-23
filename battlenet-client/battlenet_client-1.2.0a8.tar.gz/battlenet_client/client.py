"""BattleNet Clients handle the processing on the requests with the Developer Portal API

.. moduleauthor: David "Gahd" Couples <gahdania@gahd.io>
"""

from io import BytesIO
from time import sleep
from urllib.parse import unquote

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class BattleNetClient(OAuth2Session):
    """Handles the communication using OAuth v2 client to Battle.net REST API

    Args:
        region (str): region abbreviation for use with the APIs
        scope (list, optional): the scope or scopes to use during the endpoints that require the Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal

    Attributes:
        tag (str): the region tag (abbreviation) of the client
        api_host (str): the host to use for accessing the API endpoints
        auth_host (str): the host to use for authentication
        render_host (str): the hose to use for images
    """

    def __init__(self, region, game, client_id, client_secret, *, scope=None, redirect_uri=None):

        self._state = None

        if region.lower() in ("us", "eu", "kr", "tw", "cn"):
            self.tag = region.strip().lower()
        else:
            raise ValueError("Invalid region")

        self.game = game

        self._client_secret = client_secret

        if self.tag == 'cn':
            self.api_host = 'https://gateway.battlenet.com.cn'
            self.auth_host = 'https://www.battlenet.com.cn'
            self.render_host = None  # may need someone playing on the chinese client to help me
        elif self.tag == 'kr' or self.tag == 'tw':
            self.api_host = f'https://{self.tag}.api.blizzard.com'
            self.auth_host = f'https://apac.battle.net'
            self.render_host = f'https://render-{self.tag}.worldofwarcraft.com'
        else:
            self.api_host = f'https://{self.tag}.api.blizzard.com'
            self.auth_host = f'https://{self.tag}.battle.net'
            self.render_host = f'https://render-{self.tag}.worldofwarcraft.com'

        if redirect_uri and scope and 'openid' not in scope:
            self.__auth_flow = 'oauth'
            super().__init__(client_id=client_id, scope=scope, redirect_uri=redirect_uri)
            # set the mode indicator of the client to "Web Application Flow"

        else:
            super().__init__(client=BackendApplicationClient(client_id=client_id))
            # set the mode indicator of the client to "Backend Application Flow"
            self.fetch_token()
            self.__auth_flow = None

    def __str__(self):
        return f"Battle.net Client ({self.tag.upper()})"

    @property
    def auth_flow(self):
        return self.__auth_flow

    @auth_flow.setter
    def auth_flow(self, value=None):
        self.__auth_flow = value

    def validate_token(self, locale=None):
        """Checks with the API if the token is good or not.

        Args:
            locale (str): localization desired.

        Returns:
            bool: True of the token is valid, false otherwise.
        """
        url = f"{self.auth_host}/oauth/check_token"
        return self.get(url, locale=locale)

    def authorization_url(self, **kwargs):
        """Prepares and returns the authorization URL to the Battle.net authorization servers

        Returns:
            str: the URL to the Battle.net authorization server
        """
        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        auth_url = f"{self.auth_host}/oauth/authorize"
        authorization_url, self._state = super().authorization_url(url=auth_url, **kwargs)
        return unquote(authorization_url)

    def fetch_token(self, **kwargs):
        token_url = f"{self.auth_host}/oauth/token"
        super().fetch_token(token_url=token_url, client_id=self.client_id, client_secret=self._client_secret,
                            **kwargs)

    def _request(self, method, uri, *, retries=5, headers=None, params=None):
        """Sends the request to given `uri`

        Args:
            method (str): HTTP request method: get or post
            uri (str): URI of the endpoint

        Keyword Args:
            retries (int, optional): the number of retries until the attempt is cancelled.  Default is 5 retries
            headers (dict, optional): additional headers to add to the request

        Returns:
            dict or :obj:`BytesIO`: json decoded dict from the API or the data from a media source,
                or binary data (ie: an emblem image)

        Raises:
            HTTPError: on all errors from the Battle.net REST API
        """
        raw_data = None
        retry = 0

        if not uri.startswith('http'):
            url = f'{self.api_host}/{uri.lower()}'
        else:
            url = uri

        while retry < retries and not raw_data:
            try:
                raw_data = super().request(method, url, headers=headers, params=params, stream=None)
                raw_data.raise_for_status()
            except requests.Timeout:
                retry += 1
                sleep(2.5)
            except requests.exceptions.HTTPError as error:
                retry += 1
                if error.response.status_code == 429:
                    sleep(1.0)
                else:
                    raise error
            else:
                if raw_data.headers['content-type'].startswith('application/json'):
                    return raw_data.json()
                else:
                    return BytesIO(raw_data.content)

    def get_user_info(self, locale):
        """Returns the user info

        Args:
            locale (str): localization to use

        Returns:
            dict: the json decoded information for the user (user # and battle tag ID)
        """
        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        url = f"{self.auth_host}/oauth/userinfo"
        return self.post(url, params={'locale': locale})

    def get(self, *args, **kwargs):
        return self._request("get", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._request("post", *args, **kwargs)
