from base64 import urlsafe_b64encode
from hashlib import sha256
from random import choices, randint
from urllib.parse import urlencode

from helloasso_api.exceptions import Apiv5ValueError


class AuthorizationApi(object):
    def __init__(self, client):
        self._client = client

    def generate_authorize_request(self, redirect_url: str, state: str = "") -> dict:
        """Generate the needed payload to call the /authorize api endpoint
        :param redirect_url: Helloasso api will redirect to this url after being called.
            This must be the same domain configured in your account for safety reasons.
        :param state: this string will be send back to you in the redirection (max len 500)

        :return dict: {
            "url" : str, ## base url to call to make an authorize call
            "code_verifier": str, ## Will be needed when calling the exchange_authorization_token method
            "params": dict, ## parameters to pass in the authorize call
            "full_url": str, ## A functional GET url to call the /authorize endpoint
        }

        See full documentation at https://api.helloasso-dev.com/v5/swagger/ui/index
        """

        if type(state) is not str or len(state) > 500:
            raise Apiv5ValueError(
                f"state is not valid. Must be a string below 500 characters, "
                f"provided state is {state}"
            )

        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
        code_verifier = "".join(choices(chars, k=(randint(44, 127))))

        hashed = sha256(code_verifier.encode("ascii")).digest()
        encoded = urlsafe_b64encode(hashed)

        code_challenge = encoded.decode("ascii")[:-1]

        url = self._client.api_base.replace("api", "auth")
        params = {
            "client_id": self._client.client_id,
            "redirect_uri": redirect_url,
            "code_challenge": code_challenge,
            "code_challenge_method": "S256",
            "state": state,
        }

        return {
            "url": f"https://{url}/authorize",
            "code_verifier": code_verifier,
            "params": params,
            "full_url": f"https://{url}/authorize?{urlencode(params)}",
        }

    def exchange_authorization_token(
        self,
        code: str,
        redirect_url: str,
        code_verifier: str,
    ) -> dict:
        """
        Exchange an authorization code with an access_token and a refresh_token
        :param code: The code return by the api callback when calling /authorize endpoint.
        :param redirect_url: The same redirect_url passed to /authorize endpoint.
        :param code_verifier: The string used to generate the code_challenge

        :return dict: {
            "access_token": "token_abc",
            "refresh_token": "token_cba",
            "token_type": "bearer",
            "expires_in": 1800, # seconds
            "organization_slug": "slug_organization"
        }
        """
        headers = {"content-type": "application/x-www-form-urlencoded"}
        body = {
            "client_id": self._client.client_id.replace("-", ""),
            "client_secret": self._client.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_url,
            "code_verifier": code_verifier,
        }
        response = self._client.call(
            "/oauth2/token",
            method="POST",
            data=body,
            headers=headers,
            include_auth=False,
        ).json()

        return {
            "access_token": response["access_token"],
            "refresh_token": response["refresh_token"],
            "token_type": response["token_type"],
            "expires_in": response["expires_in"],  # seconds
            "organization_slug": response["organization_slug"],
        }
