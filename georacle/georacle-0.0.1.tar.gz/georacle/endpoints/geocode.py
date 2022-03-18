from georacle.types import GeocodeResponse, Precision
from georacle.endpoints.endpoint import Endpoint
from georacle.exceptions import EmptyResponseError


class Geocode(Endpoint):
    def __init__(self, headers: str):
        """
        Construct a new :code:`Geocode` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        self.base_url = "https://api.georacle.io/geocode"
        super().__init__(headers)

    def query(self, address: str, decode: bool = False) -> GeocodeResponse:
        """
        Map a street address to coordinates

        :param str address: A street address
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: The corresponding location ID and coordinate pair
        :rtype: GeocodeResponse
        :raises EmptyResponseError: on an empty response (e.g. invalid address)
        """

        params = {"address": address}
        resp = self._raw_query(self.base_url, params)
        return self._decode(resp) if decode else resp

    def _decode(self, response: dict[str, str]) -> tuple[str, float, float]:
        """
        Decode an ABI-packed geocode response

        :param dict[str, str] response: JSON response data
        :return: A decoded location ID and coordinate pair
        :rtype: tuple[str, float, float]
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

        decoded = decode_abi(["string", "int256", "int256"], payload)
        return [j / Precision if i > 0 else j for (i, j) in enumerate(decoded)]
