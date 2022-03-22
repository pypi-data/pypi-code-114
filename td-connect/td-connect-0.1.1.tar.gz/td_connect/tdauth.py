import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Union
from urllib.parse import unquote, urlencode

import dateutil.parser
import fsspec
import requests
import websockets
from ready_logger import logger


class TDAuth:
    """
    Authentication manager for TD Ameritrade APIs.
    Automatically get new access and refresh tokens upon expiring.
    Call standard APIs: https://developer.tdameritrade.com/apis
    Call streaming APIs: https://developer.tdameritrade.com/content/streaming-data
    """

    def __init__(
        self,
        auth_file: Union[str, Path] = Path(__file__).parent.joinpath(".tdauth.json"),
        **storage_options,
    ):
        """
        Args:
            auth_file (str): Any `fsspec` compatible path to a JSON file containing configuration and authentication parameters.
                             File must contain keys REDIRECT_URL and CONSUMER_KEY which can be found on your app page at https://developer.tdameritrade.com/user/me/apps.
            storage_options: keyword arguments to pass to `fsspec.open`.
        """
        self.auth_file = auth_file
        self.storage_options = storage_options

        with fsspec.open(self.auth_file, **self.storage_options) as f:
            self._cfg = json.loads(f.read().decode())

        self.client_id = f"{self._cfg['CONSUMER_KEY']}@AMER.OAUTHAP"
        self.auth_code_url = f"https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={self._cfg['REDIRECT_URL']}&client_id={self.client_id}"

        # Check for expired credentials and renew if necessary.
        self._user_principles = self._get_user_principles()
        # should only be one account.
        self._account = self._user_principles["accounts"][0]
        self._stream_info = self._user_principles["streamerInfo"]
        self._request_id = 0

    @classmethod
    def from_gcs(cls, file_url: str, project: str, token: Union[Dict[str, Any], str]):
        """Initialize from a configuration file stored in Google Cloud Storage.

        Args:
            file (str): The Google Storage URL for the file. e.i. "gs://{bucket}/{file}"
            project (str): The name of the project containing the bucket.
            token (str): A dictionary or path to JSON file with authorization token.
                         e.g. `/home/me/.config/gcloud/application_default_credentials.json`
        """
        return cls(file_url, gcs={"project": project, "token": token})

    @classmethod
    def from_gcs_env(
        cls,
        file_url_var: str = "TD_AUTH_GS_URL",
        project_var: str = "TD_AUTH_PROJECT",
        token_var: str = "TD_AUTH_TOKEN",
    ):
        token = os.environ[token_var]
        # check if token is a file path
        if (token_path := Path(token)).is_file():
            token = token_path.read_text()
        token = json.loads(token)
        print(f"USING TOKEN: {token}")
        return cls.from_gcs(
            file_url=os.environ[file_url_var],
            project=os.environ[project_var],
            token=token,
        )

    @classmethod
    def from_env(cls, file_var: str = "TD_AUTH_FILE"):
        return cls(os.environ[file_var])

    @property
    def request_id(self):
        current_id = self._request_id
        self._request_id += 1
        return current_id

    @property
    def auth_header(self):
        "Authorization header must be passed in header to all API requests."
        return {"Authorization": f"Bearer {self._cfg.get('ACCESS_TOKEN')}"}

    async def get_stream_websocket(self):
        endpoint = f"wss://{self._stream_info['streamerSocketUrl']}/ws"
        connection = await websockets.client.connect(endpoint)
        if connection.close:
            raise ConnectionError(
                f"Could not connect to websocket endpoint: {endpoint}."
            )
        # login.
        date = dateutil.parser.parse(self._stream_info["tokenTimestamp"], ignoretz=True)
        # timestamp in ms.
        timestamp = (date - datetime.utcfromtimestamp(0)).total_seconds() * 1000.0
        credential = {
            "userid": self._account["accountId"],
            "token": self._stream_info["token"],
            "company": self._account["company"],
            "segment": self._account["segment"],
            "cddomain": self._account["accountCdDomainId"],
            "usergroup": self._stream_info["userGroup"],
            "accesslevel": self._stream_info["accessLevel"],
            "appid": self._stream_info["appId"],
            "acl": self._stream_info["acl"],
            "timestamp": timestamp,
            "authorized": "Y",
        }
        request = self.authenticate_stream_requests(
            {
                "service": "ADMIN",
                "command": "LOGIN",
                "parameters": {
                    "credential": urlencode(credential),
                    "token": self._stream_info["token"],
                    "version": "1.0",
                },
            }
        )
        await connection.send(request)
        while True:
            message = await connection.recv()
            response = json.loads(message)["response"][0]
            if response["content"]["code"] == 3:
                raise ValueError(f"STREAM LOGIN ERROR: {response[0]['content']['msg']}")
            if (
                response.get("service") == "ADMIN"
                and response.get("command") == "LOGIN"
            ):
                return connection

    def authenticate_stream_requests(self, reqs: List[Dict[str, str]]):
        if not isinstance(reqs, List):
            reqs = [reqs]
        required_fields = ("service", "command", "parameters")
        for req in reqs:
            if not all(field in req for field in required_fields):
                raise ValueError(
                    f"Stream request ({req}) must contain all required fields: {','.join(required_fields)}"
                )
            req["requestid"] = str(self.request_id)
            req["account"] = self._account["accountId"]
            req["source"] = self._stream_info["appId"]
        return json.dumps({"requests": reqs})

    def _get_user_principles(self):
        resp = requests.get(
            url="https://api.tdameritrade.com/v1/userprincipals",
            params={"fields": "streamerSubscriptionKeys,streamerConnectionInfo"},
            headers=self.auth_header,
        )
        if resp.status_code == 200:
            logger.debug(f"Successfully got userprincipals")
            return resp.json()
        logger.debug(
            f"Could not get User Principles. Getting access token from refresh token."
        )
        self._set_access_token_from_refresh_token()
        # try again using new token(s)
        return self._get_user_principles()

    def _set_access_token_from_refresh_token(self):
        if "REFRESH_TOKEN" not in self._cfg:
            logger.debug(
                "REFRESH_TOKEN not found in configuration. Getting tokens from CODE."
            )
            self._set_access_and_refresh_tokens()
        resp = requests.post(
            "https://api.tdameritrade.com/v1/oauth2/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": self._cfg["REFRESH_TOKEN"],
                "client_id": self.client_id,
            },
        )
        if resp.status_code == 200:
            logger.debug(f"Successfully got new access token from refresh token.")
            data = resp.json()
            self._update_cfg(ACCESS_TOKEN=data["access_token"])
        else:
            logger.debug(
                "Could not get access token from refresh token. Getting access and refresh tokens form CODE."
            )
            self._set_access_and_refresh_tokens()

    def _set_access_and_refresh_tokens(self):
        resp = requests.post(
            r"https://api.tdameritrade.com/v1/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "authorization_code",
                "access_type": "offline",
                "code": self._cfg.get("CODE", ""),
                "redirect_uri": f'{self._cfg["REDIRECT_URL"]}',
                "client_id": self.client_id,
            },
        )
        if resp.status_code == 200:
            logger.debug(f"Successfully got new access token from Code.")
            data = resp.json()
            self._update_cfg(
                ACCESS_TOKEN=data["access_token"], REFRESH_TOKEN=data["refresh_token"]
            )
        else:
            url = input(
                f"""
                Could not get new access token from existing code.
                You must manufally get a new code from {self.auth_code_url}
                Sign in, wait to be redirected to a new page, then paste the URL of the redirect page here: """
            ).strip()
            self._update_cfg(CODE=unquote(url.split("?code=")[-1]))
            self._set_access_and_refresh_tokens()

    def _update_cfg(self, **kwargs) -> None:
        """Update configuration and save to disk."""
        self._cfg.update(kwargs)
        cfg_json = json.dumps(self._cfg)
        with fsspec.open(self.auth_file, "wt", **self.storage_options) as f:
            f.write(cfg_json)
