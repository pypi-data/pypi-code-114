from georacle.endpoints.endpoint import Endpoint
from georacle.types import Precision, Box, LocationResponse, CountResponse
from georacle.exceptions import BoundingBoxError


class BBox(Endpoint):
    def __init__(self, headers: dict[str, str]):
        """
        Construct a new :code:`BBox` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        super().__init__(headers)
        self.base_url = "https://api.georacle.io/location/bbox"
        self.count_url = f"{self.base_url}/count"

    def query(
        self, bbox: Box, key: str, val: str, limit: int, decode: bool
    ) -> LocationResponse:
        """
        Search for locations within a bounding box

        :math:`bbox = \{Lat_{min}, Lon_{min}, Lat_{max}, Lon_{max}\} \in \mathbb{R}^2`

        :param Box box: The bounding box
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param int limit: An upper bound on the search results
        :param bool decode: Decode ABI-packed payload if true
        :return: A list of matching location IDs
        :rtype: LocationResponse
        """

        (south, west, north, east) = self._validate(bbox)
        params = {
            "south": south,
            "west": west,
            "north": north,
            "east": east,
            "key": key,
            "value": val,
            "limit": limit,
        }

        resp = self._raw_query(self.base_url, params)
        return self._decode_location(resp) if decode else resp

    def count(self, bbox: Box, key: str, val: str, decode: bool) -> CountResponse:
        """
        Obtain a count of locations within a bounding box

        :math:`bbox = \{Lat_{min}, Lon_{min}, Lat_{max}, Lon_{max}\} \in \mathbb{R}^2`

        :param Box box: The bounding box
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param bool decode: Decode ABI-packed payload if true
        :return: A count of matching location IDs
        :rtype: CountResponse
        """

        (south, west, north, east) = self._validate(bbox)
        params = {
            "south": south,
            "west": west,
            "north": north,
            "east": east,
            "key": key,
            "value": val,
        }

        resp = self._raw_query(self.count_url, params)
        return self._decode_count(resp) if decode else resp

    def _validate(self, bbox: Box) -> (int, int, int, int):
        """
        Validate a bounding box

        :math:`bbox = \{Lat_{min}, Lon_{min}, Lat_{max}, Lon_{max}\} \in \mathbb{R}^2`

        :param Box box: The bounding box
        :return: A validated bounding box (scaled by :math:`10^6`)
        :rtype: tuple[int, int, int, int]
        :raises BoundingBoxError: on an invalid bounding box definition
        """

        if len(bbox) != 4:
            raise BoundingBoxError(f"Invalid size: {len(bbox)}")

        scaled_values = [int(i * Precision) for i in bbox]
        (south, west, north, east) = scaled_values

        if south >= north:
            raise BoundingBoxError(f"Invalid Y coordinates: {south} >= {north}")

        if west >= east:
            raise BoundingBoxError(f"Invalid X coordinates: {west} >= {east}")

        return (south, west, north, east)
