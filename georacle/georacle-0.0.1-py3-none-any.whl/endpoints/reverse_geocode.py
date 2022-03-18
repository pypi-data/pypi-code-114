from georacle.types import *
from georacle.endpoints.endpoint import Endpoint
from georacle.exceptions import EmptyResponseError


class ReverseGeocode(Endpoint):
    def __init__(self, headers: str):
        """
        Construct a new :code:`ReverseGeocode` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        self.base_url = "https://api.georacle.io/geocode/reverse"
        super().__init__(headers)

    def query(self, cords: Coordinates, decode: bool = False) -> ReverseGeocodeResponse:
        """
        Map a set of coordinates to a street address

        :param Coordinates cords: A valid coordinate pair
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: The corresponding location ID and street address
        :rtype: ReverseGeocodeResponse
        """

        lat, lon = self._validate_cords(cords)
        params = {"lat": lat, "lon": lon}
        resp = self._raw_query(self.base_url, params)
        return self._decode(resp) if decode else resp

    def _decode(self, response) -> list[str]:
        """
        Decode an ABI-packed reverse geocode response

        :param dict[str, str] response: JSON response data
        :return: A decoded location ID and street address
        :rtype list[str]
        :raises EmptyResponseError: on an empty response (no matches)
        """

        from eth_abi import decode_abi

        res = response["result"]
        if len(res) <= 2:
            raise EmptyResponseError(
                "API returned an empty response. Check your query parameters."
            )

        # skip hex prefix
        payload = bytes.fromhex(res[2:])
        return list(decode_abi(["string", "string"], payload))
