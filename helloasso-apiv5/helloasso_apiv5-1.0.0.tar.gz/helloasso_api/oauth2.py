import requests
from oauthlib.oauth2 import (
    AccessDeniedError,
    BackendApplicationClient,
    UnauthorizedClientError,
)
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

from helloasso_api.exceptions import (
    ApiV5AuthenticationError,
    ApiV5ConnectionError,
    Apiv5ExceptionError,
    ApiV5Timeout,
)
from helloasso_api.utils import get_log


class OAuth2Api(object):
    """Handle Authentication logic"""
    def __init__(
        self,
        api_base: str,
        client_id: str,
        client_secret: str,
        timeout: float,
        access_token: str = None,
        refresh_token: str = None,
        oauth2_token_getter: callable = None,
        oauth2_token_setter: callable = None,
    ):
        self.api_base = api_base
        self.client_id = client_id
        self.client_secret = client_secret
        self.timeout = timeout
        self._access_token = access_token
        self._refresh_token = refresh_token
        self.oauth2_token_getter = oauth2_token_getter
        self.oauth2_token_setter = oauth2_token_setter
        self.client = BackendApplicationClient(client_id=client_id)
        self.auth = HTTPBasicAuth(client_id, client_secret)
        self.log = get_log("apiv5.oauth2")

    def _get_path(self) -> str:
        return f"https://{self.api_base}/oauth2/token"

    @staticmethod
    def _get_headers() -> dict:
        return {
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
        }

    @property
    def access_token(self) -> str:
        """Return an access token. If a getter has been provided at instantiation it will be used,
        else the property _access_token will be used.
        """
        if self.oauth2_token_getter:
            return (
                self.oauth2_token_getter("access_token", self.client_id)
                or self._access_token
            )
        return self._access_token

    @access_token.setter
    def access_token(self, access_token: str):
        """Set the access token. If a setter has been provided at instantiation it will be used."""
        if self.oauth2_token_setter:
            self.oauth2_token_setter("access_token", self.client_id, access_token)
        self._access_token = access_token

    @property
    def refresh_token(self) -> str:
        """Return a refresh token. If a getter has been provided at instantiation it will be used,
        else the property _refresh_token will be used.
        """
        if self.oauth2_token_getter:
            return (
                self.oauth2_token_getter("refresh_token", self.client_id)
                or self._refresh_token
            )
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token: str):
        """Set the refresh token. If a setter has been provided at instantiation it will be used."""
        if self.oauth2_token_setter:
            self.oauth2_token_setter("refresh_token", self.client_id, refresh_token)
        self._refresh_token = refresh_token

    @property
    def credentials(self) -> dict:
        """Return the payload dict to authenticate to the Api."""
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
        }

    def get_token(self) -> None:
        """Authenticate to ApiV5 to get an access and a refresh token.
        HTTP errors are mapped to Python exceptions.
        """
        self.log.info("OAUTH2 : Get Token")
        try:
            oauth = OAuth2Session(client=self.client)
            result = oauth.fetch_token(
                token_url=self._get_path(), auth=self.auth, timeout=self.timeout
            )
            self.token_saver(result)
            self.log.info(f"Token : {self._access_token}")
        except requests.exceptions.ConnectionError:
            raise ApiV5ConnectionError(
                f"Failed to establish a new connection: Name or service not known : {self._get_path()}"
            )
        except requests.exceptions.Timeout:
            raise ApiV5Timeout(f"{self._get_path()} timeout : {str(self.timeout)} sec")
        except UnauthorizedClientError as e:
            raise ApiV5AuthenticationError(f"Authentication Error : {str(e)}")
        except Exception as e:
            raise Apiv5ExceptionError(f"Error : {str(e)}")

    def token_saver(self, request):
        """Parse dict response from oauth2 library and store access and refresh tokens."""
        self.access_token = request["access_token"]
        self.refresh_token = request["refresh_token"]

    def refresh_tokens(self):
        """Refresh connection tokens. If tokens are not presents a new token will be requested instead.
        HTTP errors are mapped to Python exceptions.
        """
        self.log.info("OAUTH2 : Refresh Token")
        try:
            if self.refresh_token is not None:
                oauth = OAuth2Session(client=self.client, token=self.access_token)
                result = oauth.refresh_token(
                    token_url=self._get_path(), timeout=self.timeout, **self.credentials
                )
                self.token_saver(result)
                self.log.info(f"OAUTH2 : Refresh Token : {self._access_token}")
            else:
                self.access_token, self.refresh_token = None, None
                self.log.warning(f"OAUTH2 : the Refresh Token is empty, reset tokens.")
        except requests.exceptions.ConnectionError:
            raise ApiV5ConnectionError(
                f"OAUTH2 : Failed to establish a new connection: Name or service not known : {self._get_path()}"
            )
        except requests.exceptions.Timeout:
            raise ApiV5Timeout(
                f"OAUTH2 : {self._get_path()} timeout : {str(self.timeout)} sec"
            )
        except UnauthorizedClientError as e:
            raise ApiV5AuthenticationError(f"OAUTH2 : Authentication Error : {str(e)}")
        except AccessDeniedError:
            self.access_token, self.refresh_token = None, None
            self.log.warning(
                f"OAUTH2 : (access_denied) invalid token values, reset tokens"
            )
        except Exception as e:
            raise Apiv5ExceptionError(f"OAUTH2 : Error : {str(e)}")
        finally:
            if not self.access_token or self.access_token is None:
                self.log.info(
                    f"OAUTH2 : Access Token for Refresh Token not exist, requests a new Access Token"
                )
                self.get_token()
