from georacle.types import *
from georacle.endpoints.endpoint import Endpoint


class Proximity(Endpoint):
    def __init__(self, headers: dict[str, str]):
        """
        Construct a new :code:`Proximity` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        super().__init__(headers)
        self.base_url = "https://api.georacle.io/location/proximity"
        self.count_url = f"{self.base_url}/count"

    def query(
        self,
        cords: Coordinates,
        radius: float,
        key: str,
        val: str,
        limit: int,
        decode: bool,
    ) -> LocationResponse:
        """
        Search for locations by proximity

        :param Coordinates cords: A reference coordinate pair
        :param float radius: A radius (in meters)
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param int limit: An upper bound on the search results (optional)
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A list of matching location IDs
        :rtype: LocationResponse
        """

        (lat, lon) = self._validate_cords(cords)
        rad = self._validate_radius(radius)
        params = {
            "lat": lat,
            "lon": lon,
            "radius": rad,
            "key": key,
            "value": val,
            "limit": limit,
        }
        resp = self._raw_query(self.base_url, params)
        return resp if not decode else self._decode_location(resp)

    def count(
        self, cords: Coordinates, radius: float, key: str, val: str, decode: bool
    ) -> CountResponse:
        """
        Obtain a count of matching locations by proximity

        :param Coordinates cords: A reference coordinate pair
        :param float radius: A radius (in meters)
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A count of matching location IDs
        :rtype: CountResponse
        """

        (lat, lon) = self._validate_cords(cords)
        rad = self._validate_radius(radius)
        params = {"lat": lat, "lon": lon, "radius": rad, "key": key, "value": val}
        resp = self._raw_query(self.count_url, params)
        return resp if not decode else self._decode_count(resp)

    def _validate_radius(self, radius: float) -> int:
        """
        Validate a search radius

        :param float radius: The search radius
        :return: a validated radius (scaled by :math:`10^6`
        :rtype: int
        :raises ValueError: on an invalid search radius
        """

        rad = int(radius * Precision)
        if rad <= 0:
            raise ValueError(f"Radius {radius} must be positive.")
        if rad >= RadMax:
            raise ValueError(f"Radius {radius} too large.")
        return rad
