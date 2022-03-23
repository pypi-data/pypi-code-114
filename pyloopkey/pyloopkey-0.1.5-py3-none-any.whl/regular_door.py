"""DoorAPI class to handle door in regular integration."""
from typing import Optional

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co
import loopkey_client.exceptions as ex


class DoorAPI(LoopkeyAPI):

    base_url = co.API_REGULAR_DOOR

    def __init__(self, client: Client, door_id: Optional[int] = None):
        """
        Init for Site.
        :param client: Client for authentication.
        :param door_id: Door id.
        """
        self._id = door_id
        super().__init__(client)

    def get(self) -> requests.Response:
        """
        Get door.
        :return: Response object from requests library with Door json.
        """
        return self._call_action(requests.get, "get", params={"id": self._id})

    def list_online_doors(self) -> requests.Response:
        """
        Set loopkey availability.
        :return: Response object from requests library with Door state json.
        """
        return self._call_action(requests.get, "online")

    def send_command(
            self,
            command: str,
            **kwargs,
    ) -> requests.Response:
        """
        Send remote command to smartlock.
        :param command: Command can be unlock, schedule_start, schedule_stop, schedule_check,
        custom, restart, update_time and update_timezone.
        :param kwargs: kwargs can contain start, duration and customCommand.
        :return: Response object from requests library with Door command json
        """
        data_dict = {"id": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, f"send/{command}", data=data_dict)

    def check_battery(self,) -> requests.Response:
        """
        Check battery of smartlock.
        :return: Response object from requests library with Door battery json.
        """
        return self._call_action(requests.post, "send/read_battery", data={"id": self._id})

    def list_events(self, buffer: int) -> requests.Response:
        """
        List events for a door.
        :param buffer: Buffer value.
        :return: Response object from requests library with Door events json.
        """
        params = {
            co.DOOR_ID: self._id,
            "eventKind": "access,management",
            "limit": buffer,
        }
        return self._call_action(requests.get, url=co.API_GET_EVENTS, params=params)

    def set_usercode(
            self,
            passcode: str,
            name: Optional[str],
            surname: Optional[str],
    ) -> requests.Response:
        """
        Attempt to set a code based on given action.
        :param passcode: Passcode to consider.
        :param name: Name to consider.
        :param surname: Surname to consider.
        :return: Response object from requests library with Door passcode json.
        """
        data_dict = {
            co.DOOR_ID: self._id,
            co.GATEWAY: True,
            co.PASSCODE: passcode,
            co.NAME: name or "No name",
            co.SURNAME: surname or "No surname",
        }
        return self._call_action(
            requests.post,
            url=co.API_SET_PASSCODE,
            data=data_dict,
        )

    def unset_usercode(self, passcode: str) -> requests.Response:
        """
        Attempt to unset a code based on given action.
        :param passcode: Passcode to consider.
        :return: Response object from requests library with Door passcode json.
        """
        data_dict = {
            co.DOOR_ID: self._id,
            co.GATEWAY: True,
            co.PERMISSION_TYPE: "passcode",
            co.VALUE: passcode
        }
        return self._call_action(
            requests.post,
            url=co.API_REMOVE_PASSCODE,
            data=data_dict,
        )

    def get_permissions(self) -> requests.Response:
        """
        Get permissions by door.
        :return: Response object from requests library with Door permissions json.
        """
        return self._call_action(requests.get, "permissions", params={"id": self._id})
