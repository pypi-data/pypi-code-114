import requests
import datetime
from typing import Union


class YaSchedule:

    base_url = 'https://api.rasp.yandex.net/v3.0/'

    def __init__(self, token: str) -> None:
        self._token = token

    def _get_response(self, request_url: str, payload: dict) -> dict:
        response = requests.get(request_url, payload)
        return response.json()

    def get_all_stations(self, lang: str = 'ru_RU'):
        api_method_url = "stations_list/"
        request_url = f'{self.base_url}{api_method_url}'
        payload = {'apikey': self._token, 'lang': lang}
        return self._get_response(request_url, payload)

    # TODO: KWARGS HANDLE, ADD ARGS
    def get_cities_schedule(self, from_city: str, to_city: str,
                            date: Union[datetime.date, tuple[datetime.date]], **kwargs) -> dict:
        """
        API_INFO: https://yandex.ru/dev/rasp/doc/reference/schedule-point-point.html
        intervals_segments: bool
        transfers: bool
        """
        api_method_url = "search/"
        kwargs.get('intervals_segments', False)
        kwargs.get('transfers', False)
        payload = {'apikey': self._token, 'from': from_city, 'to': to_city}
        request_url = f'{self.base_url}{api_method_url}'
        return self._get_response(request_url, payload)
