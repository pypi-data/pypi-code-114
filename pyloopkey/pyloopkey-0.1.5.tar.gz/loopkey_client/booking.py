"""BookingAPI class to handle bookings in corporate integration."""
from typing import Optional, Iterable

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co


class BookingAPI(LoopkeyAPI):

    base_url = co.API_BOOKING

    def __init__(self, client: Client, booking_id: Optional[int] = None):
        self._id = booking_id
        super().__init__(client)

    def create(
            self,
            site_id: int,
            door_ids: Iterable[str],
            **kwargs,
    ) -> requests.Response:
        """
        Create booking.
        :param site_id: Site id.
        :param door_ids: Door ids.
        :param kwargs: kwargs can contain roleIds, doorIds, userId, name, description, startDateTime, endDateTime,
        startTimeOfDay, endTimeOfDay, daysOfTheWeek, userName, userSurname, userPhone, userEmail, userCpf,
        userPasscode, userCard, sendPasscodeBySms, and restrictions.
        Restrictions include offlineAllowed, remoteAllowed, smartphoneAllowed, cardAllowed, and passcodeAllowed.
        :return: Response object from requests library with Booking json.
        """
        data_dict = {"siteId": site_id, "doorIds": ", ".join(door_ids), "allowedPersonalData": True}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "new", data=data_dict)

    def update(self, **kwargs) -> requests.Response:
        """
        Update booking.
        :param kwargs: kwargs can contain roleIds, doorIds, userId, name, description, startDateTime, endDateTime,
        startTimeOfDay, endTimeOfDay, daysOfTheWeek, userName, userSurname, userPhone, userEmail, userCpf,
        userPasscode, userCard, sendPasscodeBySms, and restrictions.
        Restrictions include offlineAllowed, remoteAllowed, smartphoneAllowed, cardAllowed, and passcodeAllowed.
        :return: Response object from requests library with Booking json.
        """
        data_dict = {"bookingId": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, "update", data=data_dict)

    def find(
            self,
            site_id: int,
            query: Optional[str],
    ) -> requests.Response:
        """
        Find bookings.
        :param site_id: Site id.
        :param query: Query to add; can be user name, door name or booking state (past, active, future).
        :return: Response object from requests library with Booking json.
        """
        params = {"siteId": site_id}
        if query:
            params["query"] = query
        return self._call_action(requests.get, "find", params=params)

    def delete(self) -> requests.Response:
        """
        Delete booking.
        :return: Response object from requests library with Booking json
        """
        return self._call_action(requests.post, "delete", data={"bookingId": self._id})
