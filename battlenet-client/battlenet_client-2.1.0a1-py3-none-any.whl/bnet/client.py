"""Defines the base class "BNetClient"

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Battle.net and any data
    retrieved from this API.
"""
from time import sleep
from requests import Response, exceptions
from io import BytesIO
from decouple import config
from urllib.parse import unquote
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from typing import Optional, List

from . import exceptions, constants


class BNetClient(OAuth2Session):
    """Handles the communication using OAuth v2 client to the Battle.net REST API

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        client_id (str): the client ID from the developer portal
        client_secret (str): the client secret from the developer portal
        scope (list, optional): the scope or scopes to use during the endpoints that require the Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard

    Attributes:
        tag (str): the region tag (abbreviation) of the client
        api_host (str): the host to use for accessing the API endpoints
        auth_host (str): the host to use for authentication
        render_host (str): the host to use for images
    """

    __MAJOR__ = 2
    __MINOR__ = 1
    __PATCH__ = 0

    def __init__(
        self,
        region: str,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
    ) -> None:

        self._state = None

        if not client_id:
            client_id = config("CLIENT_ID")

        if not client_secret:
            client_secret = config("CLIENT_SECRET")

        try:
            self.tag = getattr(constants, region)
        except AttributeError:
            if region.strip().lower() in ("us", "eu", "kr", "tw", "cn"):
                self.tag = region.strip().lower()
            else:
                raise exceptions.BNetRegionNotFoundError("Region not available")

        self._client_secret = client_secret

        if self.tag == "cn":
            self.api_host = "https://gateway.battlenet.com.cn"
            self.auth_host = "https://www.battlenet.com.cn"
            self.render_host = "https://render.worldofwarcraft.com.cn"
        elif self.tag in ("kr", "tw"):
            self.api_host = f"https://{self.tag}.api.blizzard.com"
            self.auth_host = "https://apac.battle.net"
            self.render_host = f"https://render-{self.tag}.worldofwarcraft.com"
        else:
            self.api_host = f"https://{self.tag}.api.blizzard.com"
            self.auth_host = f"https://{self.tag}.battle.net"
            self.render_host = f"https://render-{self.tag}.worldofwarcraft.com"

        if redirect_uri and scope:
            self.auth_flow = True
            super().__init__(
                client_id=client_id, scope=scope, redirect_uri=redirect_uri
            )
        else:
            super().__init__(client=BackendApplicationClient(client_id=client_id))
            self.fetch_token(
                token_url=f"{self.auth_host}/oauth/token",
                client_id=self.client_id,
                client_secret=self._client_secret,
            )
            self.auth_flow = False

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.tag.upper()} {self.version} API Client"

    def __repr__(self) -> str:
        return f"{self.__str__()} ({'Auth Code Flow' if self.auth_flow else 'Credential Client Flow'})"

    @property
    def version(self):
        return f"v{self.__MAJOR__}.{self.__MINOR__}.{self.__PATCH__}"

    def validate_token(self) -> bool:
        """Checks with the API if the token is good or not.

        Returns:
            bool: True of the token is valid, false otherwise.
        """

        url = f"{self.auth_host}/oauth/check_token"
        data = self.post(
            url,
            params={"token": self.access_token},
            headers={"Battlenet-Namespace": None},
        )
        result: bool = (
            data.status_code == 200 and data.json()["client_id"] == self.client_id
        )
        return result

    def authorization_url(self, **kwargs) -> str:
        """Prepares and returns the authorization URL to the Battle.net authorization servers

        Returns:
            str: the URL to the Battle.net authorization server
        """
        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        auth_url = f"{self.auth_host}/oauth/authorize"
        authorization_url, self._state = self.authorization_url(url=auth_url, **kwargs)
        return unquote(authorization_url)

    def user_info(self, locale: str) -> Response:
        """Returns the user info

        Args:
            locale (str): localization to use

        Returns:
            dict: the json decoded information for the user (user # and battle tag ID)

        Notes:
            this function requires the BattleNet Client to be use OAuth (Authentication Workflow)
        """
        if not self.auth_flow:
            raise exceptions.BNetClientError("Requires Authorization Code Workflow")

        url = f"{self.auth_host}/oauth/userinfo"
        return self.get(url, params={"locale": locale})

    def request(self, method, url, **kwargs):

        retries = 0

        while retries < 5:
            try:
                response = super().request(method, url, **kwargs)
                response.raise_for_status()
            except exceptions.HTTPError as err:
                if err.response.status_code == 429:
                    retries += 1
                    sleep(1)
            else:
                if response.request.url.startswith(self.api_host):
                    if response.headers["content-type"].startswith("application/json"):
                        return response.json()

                    if response.headers["content-type"] in ("image/jpeg", "image/png"):
                        return BytesIO(response.content)

                return response
