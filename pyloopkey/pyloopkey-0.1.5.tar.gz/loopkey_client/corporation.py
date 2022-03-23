"""CorporationAPI class to handle corporation in corporate integration."""
import requests
from typing import Optional

from loopkey_client.loopkey_api import LoopkeyAPI
from loopkey_client.client import Client
import loopkey_client.const as co


class CorporationAPI(LoopkeyAPI):

    base_url = co.API_CORP

    def __init__(self, client: Client, corp_id: Optional[int] = None):
        self._id = corp_id
        super().__init__(client)

    def list_sites(self) -> requests.Response:
        """
        List sites for corporation.
        :return: Response object from requests library with Corporation json.
        """
        return self._call_action(requests.get, "sites", params={"corpId": self._id})

    def create_corporation(self, name: str) -> requests.Response:
        """
        Create corporation.
        :param name: Corporation name.
        :return: Response object from requests library with Corporation json.
        """
        return self._call_action(requests.post, "new", data={"name": name})
