"""SiteAPI class to handle site in corporate integration."""
from typing import Optional

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co


class SiteAPI(LoopkeyAPI):

    base_url = co.API_SITE

    def __init__(self, client: Client, site_id: Optional[int] = None):
        """
        Init for Site.
        :param client: Client for authentication.
        :param site_id: Site id.
        """
        self._id = site_id
        super().__init__(client)

    def create(self, corp_id: int, **kwargs) -> requests.Response:
        """
        Create a site.
        :param corp_id: Corporation id.
        :param kwargs: kwargs can contain name, address, latitude and longitude.
        :return: Response object from requests library with Site json.
        """
        data_dict = {"corpId": corp_id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "new", data=data_dict)

    def list_access_groups(self) -> requests.Response:
        """
        List of access groups.
        :return: Response object from requests library with Site access groups json.
        """
        return self._call_action(requests.get, "accessGroups", params={"siteId": self._id})

    def list_doors(self, door_name: Optional[str] = None) -> requests.Response:
        """
        List doors in a site.
        :param door_name: Name of door.
        :return: Response object from requests library with Site doors json.
        """
        params = {"siteId": self._id}
        if door_name:
            params["query"] = door_name
        return self._call_action(requests.get, "doors", params=params)

    def list_gateways(self) -> requests.Response:
        """
        List of gateways in a site.
        :return: Response object from requests library with Site gateways json.
        """
        return self._call_action(requests.get, "gateways", params={"siteId": self._id})

    def list_bookings(self, **kwargs) -> requests.Response:
        """
        List bookings in a site.
        :param kwargs: kwargs can contain skip, limit, order and bookingId.
        :return: Response object from requests library with Site bookings json.
        """
        params = {"siteId": self._id}
        params.update(kwargs)
        return self._call_action(requests.get, "bookings", params=params)

    def list_roles(self) -> requests.Response:
        """
        List roles in a site.
        :return: Response object from requests library with Site roles json.
        """
        return self._call_action(requests.get, "roles", params={"siteId": self._id})
