from georacle.types import *
from georacle import __version__
from georacle.endpoints import (
    Area,
    BBox,
    Proximity,
    Info,
    Geocode,
    ReverseGeocode,
    Geometry,
)


class Georacle:
    def __init__(self, api_key: str):
        """
        Construct a new :code:`Georacle` client

        :param str api_key: Georacle API Key (obtained from https://georacle.io
        """

        self.api_key = api_key
        self.headers = {
            "X-API-Key": self.api_key,
            "User-Agent": f"pygeoracle/{__version__}",
        }

        self.area_endpoint = Area(self.headers)
        self.bbox_endpoint = BBox(self.headers)
        self.proximity_endpoint = Proximity(self.headers)
        self.info_endpoint = Info(self.headers)
        self.geocode_endpoint = Geocode(self.headers)
        self.reverse_geocode_endpoint = ReverseGeocode(self.headers)
        self.geometry_endpoint = Geometry(self.headers)

    def area(
        self, name: str, key: str, val: str, limit: int = 0, decode: bool = False
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

        return self.area_endpoint.query(name, key, val, limit, decode)

    def area_count(
        self, name: str, key: str, val: str, decode: bool = False
    ) -> CountResponse:
        """
        Obtain a count of locations within a named area

        :param str name: The name of the search area
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: The number of matching locations
        :rtype: CountResponse
        """

        return self.area_endpoint.count(name, key, val, decode)

    def bbox(
        self, box: Box, key: str, val: str, limit: int = 0, decode: bool = False
    ) -> LocationResponse:
        """
        Search for locations within a bounding box

        :param Box box: The bounding box: :math:`bbox = \{\textbf{Lat}_\textbf{min}, \textbf{Lon}_\textbf{min}, \textbf{Lat}_\textbf{max}, \textbf{Lon}_\textbf{max}\} \in \mathbb{R}^2`
        :param str key: An attribute key
        :param str val: The attribute value to search for :param int limit: An upper bound on the search results (optional)
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A list of matching location IDs
        :rtype: LocationResponse
        """

        return self.bbox_endpoint.query(box, key, val, limit, decode)

    def bbox_count(
        self, box: Box, key, val, limit=0, decode: bool = False
    ) -> CountResponse:
        """
        Obtain a count of locations within a bounding box

        :param Box box: The bounding box: :math:`bbox = \{\textbf{Lat}_\textbf{min}, \textbf{Lon}_\textbf{min}, \textbf{Lat}_\textbf{max}, \textbf{Lon}_\textbf{max}\} \in \mathbb{R}^2`
        :param str key: An attribute key
        :param str val: The attribute value to search for
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A count of matching location IDs
        :rtype: CountResponse
        """

        return self.bbox_endpoint.count(box, key, val, decode)

    def proximity(
        self,
        cords: Coordinates,
        rad: float,
        key: str,
        val: str,
        limit: int = 0,
        decode: bool = False,
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

        return self.proximity_endpoint.query(cords, rad, key, val, limit, decode)

    def proximity_count(
        self, cords: Coordinates, rad: float, key: str, val: str, decode: bool = False
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

        return self.proximity_endpoint.count(cords, rad, key, val, decode)

    def info(self, id: str, keys: list[str], decode: bool = False) -> dict[str, str]:
        """
        Filter the attributes of a location

        :param str id: A location ID
        :param list[str] keys: A list of attribute keys to filer
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A map of resulting key-value pairs
        :rtype: dict[str, str]
        """

        return self.info_endpoint.query(id, keys, decode)

    def geocode(self, address: str, decode: bool = False) -> GeocodeResponse:
        """
        Map a street address to coordinates

        :param str address: A street address
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: The corresponding location ID and coordinate pair
        :rtype: GeocodeResponse
        """

        return self.geocode_endpoint.query(address, decode)

    def reverse_geocode(
        self, cords: Coordinates, decode: bool = False
    ) -> ReverseGeocodeResponse:
        """
        Map a set of coordinates to a street address

        :param Coordinates cords: A valid coordinate pair
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: The corresponding location ID and street address
        :rtype: ReverseGeocodeResponse
        """

        return self.reverse_geocode_endpoint.query(cords, decode)

    def geometry(
        self, id: str, sample: int = 0, decode: bool = False
    ) -> GeometryResponse:
        """
        Sample the geometry of a region

        :param str id: A location ID
        :param int sample: A sample size for uniformly random sampling (optional)
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A list of coordinate pairs
        :rtype: GeometryResponse
        """

        return self.geometry_endpoint.query(id, sample, decode)

    def geometry_count(self, id: str, decode: bool = False) -> CountResponse:
        """
        Obtain a point count of a geometry

        :param str id: A location ID
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A count of points in a geometry
        :rtype: CountResponse
        """

        return self.geometry_endpoint.count(id, decode)
