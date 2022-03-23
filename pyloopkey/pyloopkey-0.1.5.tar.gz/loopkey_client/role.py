"""RoleAPI class to handle role in corporate integration."""
from typing import Optional

import requests

from loopkey_client.loopkey_api import LoopkeyAPI
from loopkey_client.client import Client
import loopkey_client.const as co


class RoleAPI(LoopkeyAPI):

    base_url = co.API_ROLE

    def __init__(self, client: Client, role_id: Optional[int] = None):
        """
        Init for Role.
        :param client: Client for authentication.
        :param role_id: Role id.
        """
        self._id = role_id
        super().__init__(client)

    def create(
            self,
            site_id: int,
            **kwargs,
    ) -> requests.Response:
        """
        Create role.
        :param site_id: Site id.
        :param kwargs: kwargs can contain name, userList, description and isGlobal.
        :return: Response object from requests library with Role json.
        """
        data_dict = {"siteId": site_id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, data=data_dict, url=co.API_SITE.format("role/new"))

    def update(self, **kwargs,) -> requests.Response:
        """
        Update role.
        :param kwargs: kwargs can contain name and description.
        :return: Response object from requests library with Role json.
        """
        data_dict = {"id": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "update", data=data_dict)

    def delete(self, corp_id: int) -> requests.Response:
        """
        Delete role.
        :param corp_id: Corp id.
        :return: Response object from requests library with Role json.
        """
        return self._call_action(requests.post, "delete", data={"rolesIds": self._id, "corpId": corp_id})
