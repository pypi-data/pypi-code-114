"""AccessGroupAPI class to handle access groups in corporate integration."""
from typing import Optional

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co


class AccessGroupAPI(LoopkeyAPI):

    base_url = co.API_ACCESS_GROUP

    def __init__(self, client: Client, access_group_id: Optional[int] = None):
        """
        Init for AccessGroup.
        :param client: Client for authentication.
        :param access_group_id: Access Group id.
        """
        self._id = access_group_id
        super().__init__(client)

    def create(self, site_id: int, **kwargs) -> requests.Response:
        """
        Create an access group.
        :param site_id: Site id.
        :param kwargs: kwargs can contain roleIds, userList, doorList, name, description, and restrictions.
        Restrictions include startDateTime, endDateTime, startTimeOfDay, endTimeOfDay, daysOfTheWeek,
        offlineAllowed, remoteAllowed, smartphoneAllowed, cardAllowed, and passcodeAllowed.
        :return: Response object from requests library with Access Group json.
        """
        data_dict = {"siteId": site_id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "new", data=data_dict)

    def find(self, site_id: int, name: str) -> requests.Response:
        """
        Find an access group by name.
        :param site_id: Site id.
        :param name: Name of access group.
        :return: Response object from requests library with Access Group json.
        """
        return self._call_action(requests.get, "find", params={"siteId": site_id, "query": name})

    def update(self, **kwargs) -> requests.Response:
        """
        Update an access group.
        :param kwargs: kwargs can contain name, description and restrictions.
        :return: Response object from requests library with Access Group json.
        """
        data_dict = {"id": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "update", data=kwargs)

    def delete(self) -> requests.Response:
        """
        Delete an access group.
        :return: Response object from requests library with Access Group json.
        """
        return self._call_action(requests.post, "delete", data={"groupId": self._id})

    def list_doors(self) -> requests.Response:
        """
        List doors in an access group.
        :return: Response object from requests library with Access Group json.
        """
        return self._call_action(requests.get, "doors", params={"id": self._id})
