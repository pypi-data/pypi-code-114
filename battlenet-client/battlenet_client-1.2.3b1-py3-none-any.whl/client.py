"""This module defines the base client class for the Battle.net API

.. moduleauthor: David Couples <gahdania@gahd.io>
"""

from io import BytesIO
from time import sleep
from urllib.parse import unquote

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from battlenet_client import exceptions, constants
from battlenet_client import bnet


class BattleNetClient(OAuth2Session):
    """Handles the communication using OAuth v2 client to the Battle.net REST API

    Args:
        region (str): region abbreviation for use with the APIs
        game (dict): the game for the request
        client_id (str): the client ID from the developer portal
        client_secret (str): the client secret from the developer portal

    Keyword Args:
        scope (list, optional): the scope or scopes to use during the endpoints that require the Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard

    Attributes:
        tag (str): the region tag (abbreviation) of the client
        api_host (str): the host to use for accessing the API endpoints
        auth_host (str): the host to use for authentication
        render_host (str): the hose to use for images
        game (dict): holds basic info about the game
    """

    def __init__(self, region, game, client_id, client_secret, *, scope=None, redirect_uri=None):

        self._state = None

        try:
            self.tag = getattr(constants, region)
        except AttributeError:
            if region.strip().lower() in ('us', 'eu', 'kr', 'tw', 'cn'):
                self.tag = region.strip().lower()
            else:
                raise exceptions.BNetRegionNotFoundError("Region not available")

        self.game = game

        self._client_secret = client_secret

        if self.tag == 'cn':
            self.api_host = 'https://gateway.battlenet.com.cn'
            self.auth_host = 'https://www.battlenet.com.cn'
            self.render_host = 'https://render.worldofwarcraft.com.cn'
        elif self.tag == 'kr' or self.tag == 'tw':
            self.api_host = f'https://{self.tag}.api.blizzard.com'
            self.auth_host = 'https://apac.battle.net'
            self.render_host = f'https://render-{self.tag}.worldofwarcraft.com'
        else:
            self.api_host = f'https://{self.tag}.api.blizzard.com'
            self.auth_host = f'https://{self.tag}.battle.net'
            self.render_host = f'https://render-{self.tag}.worldofwarcraft.com'

        # load the API endpoints programmatically
        for mod_name in bnet.__all__:
            mod = getattr(bnet, mod_name)
            for cls_name in dir(mod):
                if not cls_name.startswith('__') and isinstance(getattr(mod, cls_name), type):
                    setattr(self, mod_name, getattr(mod, cls_name)(self))

        if redirect_uri and scope:
            self.auth_flow = True
            super().__init__(client_id=client_id, scope=scope, redirect_uri=redirect_uri)
            # set the mode indicator of the client to "Web Application Flow"
        else:
            super().__init__(client=BackendApplicationClient(client_id=client_id))
            # set the mode indicator of the client to "Backend Application Flow"
            self.fetch_token()
            self.auth_flow = False

    def __str__(self):
        return f"{self.game['name']} API Client"

    def __repr__(self):
        return f"{self.__class__.__name__} Instance: {self.game['abbrev']}"

    def api_get(self, *args, **kwargs):
        """HTTP GET accessor method"""
        return self.__endpoint('get', *args, **kwargs)

    def api_post(self, *args, **kwargs):
        """HTTP POST accessor method"""
        return self.__endpoint('post', *args, **kwargs)

    def __endpoint(self, method, uri, locale, *, retries=5, params=None, headers=None, fields=None):
        """Processes the API request into the appropriate headers and parameters

        Args:
            method (str): the HTTP method to use
            uri (str): the URI for the API endpoint
            locale (str): the locale identifier to use with the API

        Keyword Args:
            retries (int, optional): the number of retries at getting to the
                API endpoint (default is 5)
            params (dict, optional): dict of the parameters to be passed via
                query string to the endpoint
            headers (dict, optional):  Additional headers to sent with the
                request
            fields (dict, optional): search parameters and values to add to
                the request
        """

        if params:
            params['locale'] = self.localize(locale)
        else:
            params = {'locale': self.localize(locale)}

        if fields:
            params.update({key: value for key, value in fields.items()})

        for _ in range(retries):
            try:
                raw_data = super().request(method, uri, params=params, headers=headers)
                raw_data.raise_for_status()
            except requests.exceptions.Timeout:
                sleep(2.5)
            except requests.exceptions.HTTPError as error:
                if error.response.status_code == 429:
                    sleep(1.0)

                if error.response.status_code == 404:
                    raise exceptions.BNetDataNotFoundError(error)

                if error.response.status_code == 403:
                    raise exceptions.BNetAccessForbiddenError(error)

                raise error
            else:
                if raw_data.headers['content-type'].startswith('application/json'):
                    return raw_data.json()
                else:
                    return BytesIO(raw_data.content)

    def validate_token(self):
        """Checks with the API if the token is good or not.

        Returns:
            bool: True of the token is valid, false otherwise.
        """
        url = f"{self.auth_host}/oauth/check_token"
        data = super().post(url, params={'token': self.access_token}, headers={'Battlenet-Namespace': None})
        return data.status_code == 200 and data.json()['client_id'] == self.client_id

    def authorization_url(self, **kwargs):
        """Prepares and returns the authorization URL to the Battle.net
        authorization servers

        Returns:
            str: the URL to the Battle.net authorization server
        """
        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        auth_url = f"{self.auth_host}/oauth/authorize"
        authorization_url, self._state = super().authorization_url(url=auth_url, **kwargs)
        return unquote(authorization_url)

    def fetch_token(self, **kwargs):

        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        token_url = f"{self.auth_host}/oauth/token"
        super().fetch_token(token_url=token_url, client_id=self.client_id, client_secret=self._client_secret,
                            **kwargs)

    @staticmethod
    def currency_convertor(value):
        """Returns the value into gold, silver and copper

        Args:
            value (int or str): the value to be converted

        Returns:
            list: gold, silver and copper values
        """
        if not isinstance(value, (str, int)):
            raise TypeError("Value needs to be a string or integer")

        value = int(value)

        if value < 0:
            raise ValueError("Value must be zero or a positive value")

        return value // 10000, (value % 10000) // 100, value % 100

    @staticmethod
    def slugify(value):
        """Returns the 'slugified' string

        Args:
            value (str): the string to be converted into a slug

        Returns:
            (str): the slug of :value:
        """

        if not isinstance(value, str):
            raise TypeError("Value must be a string")

        return value.lower().replace("\'", "").replace(' ', '-')

    @staticmethod
    def localize(locale):
        """Returns the standardized locale

        Args:
            locale (str): the locality to be standardized

        Returns:
            (str): the locale in the format of "<lang>_<COUNTRY>"

        Raise:
            TypeError: when locale is not a string
            ValueError: when the lang and country are not in the given lists
        """
        if not isinstance(locale, str):
            raise TypeError('Locale must be a string')

        if locale[:2].lower() not in ('en', 'es', 'pt', 'fr', 'ru', 'de', 'it', 'ko', 'zh'):
            raise ValueError('Invalid language code')

        if locale[-2:].lower() not in ('us', 'mx', 'br', 'gb', 'es', 'fr', 'ru', 'de', 'pt', 'it', 'kr', 'tw', 'cn'):
            raise ValueError('Invalid country code')

        return f"{locale[:2].lower()}_{locale[-2:].upper()}"
