"""LoopkeyAPI class."""
import requests
from typing import Callable, Optional

from loopkey_client.client import Client
import loopkey_client.const as co


class LoopkeyAPI:

    base_url = None

    def __init__(self, client: Client):
        """
        Init for LoopkeyAPI.
        :param client: Client for authentication.
        """
        self.api_client = client

    def _call_action(
            self,
            function: Callable,
            action_name: str = "",
            headers: Optional[dict] = None,
            url: str = "",
            **kwargs,
    ) -> requests.Response:
        """
        Calls an action to perform a request to Loopkey servers.
        :param function: Request to perform (get and post mostly)
        :param action_name: Action to execute on the server (new, update, delete)
        :param headers: Headers to use in request
        :param url: URL to consider if base url doesn't work for specific endpoint
        :param kwargs: params or data should be included here depending on the type of request
        :return: Response object from requests library.
        """
        if self.base_url is None and not url:
            raise NotImplementedError
        if headers is None:
            headers = dict()
        headers.update(self.api_client.auth_dict)
        response = function(
            url=url or self.base_url.format(action_name),
            headers=headers,
            **kwargs,
        )
        return response

    def list_corporations(self) -> requests.Response:
        """
        List corporations for corporate integration.
        :return: Response object from requests library with Corporations json.
        """
        return self._call_action(
            requests.get,
            url=co.API_LIST_CORPS,
        )

    def access(self) -> requests.Response:
        """
        Get doors of regular integration.
        :return: Response object from requests library with Doors json.
        """
        return self._call_action(requests.get, url=co.API_ACCESS_URL)
