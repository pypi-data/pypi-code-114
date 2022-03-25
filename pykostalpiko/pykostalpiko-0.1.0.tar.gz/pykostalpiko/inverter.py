import requests
from pykostalpiko.dxs.entries import Entries
from pykostalpiko.constants import API_ENDPOINT


class Inverter:
    def __init__(self, ip: str):
        self._ip = ip

    def fetch(self, *entries: Entries) -> dict:
        if (entries.count == 0):
            raise Exception('No entries specified')

        url = f'http://{self._ip}{API_ENDPOINT}?'

        for entry in entries:
            url += f'dxsEntries={entry.value}&'

        r = requests.get(url)

        json = r.json()
        return self.__format_response(json)

    def __format_response(self, jsn) -> dict:
        new = {}
        entries = jsn['dxsEntries']

        for entry in entries:
            new[Entries(entry['dxsId']).name] = entry['value']

        return new
