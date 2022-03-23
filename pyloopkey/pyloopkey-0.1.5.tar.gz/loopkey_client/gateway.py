"""GatewayAPI class to handle gateway in corporate integration."""
from typing import Optional

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co


class GatewayAPI(LoopkeyAPI):

    base_url = co.API_GATEWAY

    def __init__(self, client: Client, gateway_id: Optional[int] = None):
        """
        Init for Gateway.
        :param client: Client for authentication.
        :param gateway_id: Gateway id.
        """
        self._id = gateway_id
        super().__init__(client)

    def add(self, site_id: int,) -> requests.Response:
        """
        Add a gateway in a site.
        :param site_id: Site id.
        :return: Response object from requests library with Gateway json.
        """
        return self._call_action(requests.post, "add", data={"gatewayId": self._id, "siteId": site_id})

    def send_command(self, site_id: int, command: str) -> requests.Response:
        """
        Send command to gateway.
        :param site_id: Site id.
        :param command: Command to send; it can be reboot or restartBluetooth.
        :return: Response object from requests library with Gateway command json.
        """
        return self._call_action(requests.post, "command", data={"siteId": site_id, "command": command, "gatewayId": self._id})

    def update(self, address: str) -> requests.Response:
        """
        Update a gateway.
        :param address: Address for gateway.
        :return: Response object from requests library with Gateway json.
        """
        return self._call_action(requests.post, "update", data={"gatewayId": self._id, "address": address})

    def list_doors(self) -> requests.Response:
        """
        List doors by gateway.
        :return: Response object from requests library with Gateway doors json.
        """
        return self._call_action(requests.get, "doors", params={"gatewayId": self._id})
