"""DoorAPI class to handle door in corporate integration."""
from typing import Optional

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co


class DoorAPI(LoopkeyAPI):

    base_url = co.API_DOOR

    def __init__(self, client: Client, door_id: Optional[int] = None):
        """
        Init for Door.
        :param client: Client for authentication.
        :param door_id: Door id.
        """
        self._id = door_id
        super().__init__(client)

    def get(self) -> requests.Response:
        """
        Get door of corporate integration.
        :return: Response object from requests library with Door json.
        """
        return self._call_action(requests.get, "get", params={"doorId": self._id})

    def add(self, site_id: int) -> requests.Response:
        """
        Add door in a site.
        :param site_id: Site id.
        :return: Response object from requests library with Door json.
        """
        return self._call_action(requests.post, "add", data={"siteId": site_id, "doorIds": self._id})

    def remove(self) -> requests.Response:
        """
        Remove door in a site.
        :return: Response object from requests library with Door json.
        """
        return self._call_action(requests.post, "remove", data={"doorId": self._id})

    def list_online_doors(self, site_id: int) -> requests.Response:
        """
        List online doors in a site.
        :param site_id: Site id.
        :return: Response object from requests library with Door json.
        """
        return self._call_action(requests.get, "online", params={"siteId": site_id})

    def sync(self, site_id: int, **kwargs) -> requests.Response:
        """
        Forces a corporation door to sync.
        :param site_id: Site id.
        :param kwargs: kwargs can contain shouldRemoveAll and removeDoorInSyncing.
        :return: Response object from requests library with Door json.
        """
        data_dict = {"siteId": site_id, "doorId": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "sync", data=data_dict)

    def send_command(self, site_id: int, message_type: str, **kwargs) -> requests.Response:
        """
        Send command to door.
        :param site_id: Site id.
        :param message_type: Command to send; it can be unlock, schedule_start, schedule_stop, schedule_check,
        custom, restart, update_time and update_timezone.
        :param kwargs: kwargs can contain start, duration, and customCommand.
        :return: Response object from requests library with Door command json.
        """
        data_dict = {"siteId": site_id, "id": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, data=data_dict, url=co.API_CORP_DOOR_COMMANDS.format(message_type))
