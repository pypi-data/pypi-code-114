"""Client class for authentication in LoopKey servers."""
from typing import Optional

import requests

import loopkey_client.const as co
import loopkey_client.exceptions as ex


class Client:

    def __init__(self,  auth_token: Optional[str] = "", phone: Optional[str] = "", password: Optional[str] = ""):
        """
        Inits loopkey client.
        :param auth_token: Auth token for loopkey.
        :param phone: Phone number to be used as user.
        :param password: Password of loopkey user.
        """
        self.phone = phone
        self.password = password
        self.token = auth_token or self.get_auth_token()
        self.auth_dict = {"Authorization": self.token}

    def get_auth_token(self) -> str:
        """
        Request an authentication token from loopkey servers.
        :return: Authentication token.
        """
        data_dict = {co.PHONE: self.phone, co.PASS: self.password}

        response = requests.post(
            co.API_LOGIN_URL,
            data=data_dict,
        )
        if response.status_code != 200:
            raise ex.AuthenticationError(response.json().get("errorDescription"))
        try:
            auth = response.json()
            token = auth[co.AUTHORIZATION]
            return token
        except Exception as e:
            raise ex.AuthenticationError(
                "Unexpected error while parsing authentication response."
            ) from e
