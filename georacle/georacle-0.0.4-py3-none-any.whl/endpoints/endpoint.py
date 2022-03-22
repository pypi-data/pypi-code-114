import requests
from eth_abi import decode_single, decode_abi

from georacle.types import *
from georacle.exceptions import *


class Endpoint:
    def __init__(self, headers: dict[str, str]):
        """
        Construct a generic endpoint

        This class takes care of making requests and parsing the response
        """

        self.headers = headers

    def _raw_query(self, url: str, params: dict[str, str]) -> RawResponse:
        """
        Make a GET request to a specified endpoint

        :param str url: The url of the endpoint
        :param dict[str, str] params: The request parameters (query specific)
        :return: JSON encoded response object
        :rtype: RawResponse
        :raises APIError: on a bad request
        :raises APIKeyError: on an invalid API key
        :raises RateLimitError: on a rate limited client
        :raises EmptyResponseError: on an empty response
        """

        resp = requests.get(url, headers=self.headers, params=params)
        status = resp.status_code

        if status == 200 and resp.content:
            return resp.json()
        if status == 400:
            raise APIError("Bad Request. Check your query parameters.")
        if status == 401:
            raise APIKeyError("Authentication Error. Check your API Key.")
        if status == 429:
            raise RateLimitError("Client rate limited. Wait and try again.")

        raise EmptyResponseError(
            "API returned an empty response. Check your query parameters."
        )

    def _validate_cords(self, cords: Coordinates) -> tuple[float, float]:
        """
        Validate a set of coordinates

        :param Coordinates cords: The coordinate pair
        :return: A validated coordinate pair (scaled by :math:`10^6`)
        :rtype: tuple[float, float]
        :raises ValueError: on an invalid coordinate pair
        """

        if len(cords) != 2:
            raise ValueError(f"Invalid coordinates: {cords}")

        (lat, lon) = [int(i * Precision) for i in cords]

        if lat < -LatMax or lat > LatMax:
            raise ValueError(f"Invalid latitude: {lat}")
        if lon < -LonMax or lon > LonMax:
            raise ValueError(f"Invalid longitude: {lon}")

        return (lat, lon)

    def _decode_location(self, response: dict[str, str]) -> list[str]:
        """
        Decode an ABI-packed list of location IDs

        :param dict[str, str] response: JSON response data
        :return: A decoded list of location IDs
        :rtype: list[str]
        :raises EmptyResponseError: on an empty response (no matches)
        """

        res = response["result"]
        if len(res) <= 2:
            raise EmptyResponseError(
                "API returned an empty response. Check your query parameters."
            )

        # skip hex prefix
        payload = bytes.fromhex(res[2:])
        return list(decode_abi(["string[]"], payload)[0])

    def _decode_count(self, response: dict[str, str]) -> int:
        """
        Decode an ABI-packed location count

        :param dict[str, str] response: JSON response data
        :return: A decoded count of matching location IDs
        :rtype: int
        :raises EmptyResponseError: on an empty response (no matches)
        """

        res = response["result"]
        if len(res) <= 2:
            raise EmptyResponseError(
                "API returned an empty response. Check your query parameters."
            )

        # skip hex prefix
        payload = bytes.fromhex(res[2:])
        return decode_single("int256", payload)
