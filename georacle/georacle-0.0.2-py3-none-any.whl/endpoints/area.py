from georacle.endpoints import Endpoint
from georacle.types import LocationResponse, CountResponse


class Area(Endpoint):
    def __init__(self, headers: dict[str, str]):
        """
        Construct a new :code:`Area` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        super().__init__(headers)
        self.base_url = "https://api.georacle.io/location/area"
        self.count_url = f"{self.base_url}/count"

    def query(
        self, name: str, key: str, val: str, limit: int, decode: bool
    ) -> LocationResponse:
        """
        Search for locations within a named area

        :param str name: The name of the search area
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param int limit: An upper bound on the search results (optional)
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A list of matching location IDs
        :rtype: LocationResponse
        """

        params = {"name": name, "key": key, "value": val, "limit": limit}
        resp = self._raw_query(self.base_url, params)
        return self._decode_location(resp) if decode else resp

    def count(self, name: str, key: str, val: str, decode: bool) -> CountResponse:
        """
        Obtain a count of locations within a named area

        :param str name: The name of the search area
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: The number of matching locations
        :rtype: CountResponse
        """

        params = {"name": name, "key": key, "value": val}
        resp = self._raw_query(self.count_url, params)
        return self._decode_count(resp) if decode else resp
