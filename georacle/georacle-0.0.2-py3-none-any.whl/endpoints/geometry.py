from georacle.types import *
from georacle.endpoints.endpoint import Endpoint
from georacle.exceptions import EmptyResponseError, EncodingError


class Geometry(Endpoint):
    def __init__(self, headers: str):
        """
        Construct a new :code:`Geometry` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        self.base_url = "https://api.georacle.io/geometry/{id}"
        self.count_url = "https://api.georacle.io/geometry/count/{id}"
        super().__init__(headers)

    def query(self, id: str, sample: int = 0, decode: bool = False) -> GeometryResponse:
        """
        Sample the geometry of a region

        :param str id: A location ID
        :param int sample: A sample size for uniformly random sampling (optional)
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A list of coordinate pairs
        :rtype: GeometryResponse
        :raises: APIError on invalid sample size
        """

        if sample < 0:
            raise APIError(f"Sample size ({sample}) must be nonnegative")
        params = {"sample": sample} if sample > 0 else None
        url = self.base_url.format(id=id)
        resp = self._raw_query(url, params)
        return self._decode(resp) if decode else resp

    def count(self, id: str, decode: bool = False) -> CountResponse:
        """
        Obtain a point count of a geometry

        :param str id: A location ID
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A count of points in a geometry
        :rtype: CountResponse
        """

        url = self.count_url.format(id=id)
        resp = self._raw_query(url, None)
        return self._decode_count(resp) if decode else resp

    def _decode(self, response: RawResponse) -> list[float]:
        """
        Decode a packed geometry response

        :param dict[str, str] response: JSON response data
        :return: A decoded list of coordinate pairs
        :rtype: list[float]
        :raises EncodingError: on an invalid encoding
        """

        res = response["result"]

        # minimum encoding: 2 byte prefix + 8 byte length
        if len(res) < 10:
            raise EncodingError(
                "API returned an empty response. Check your query parameters."
            )

        # skip hex prefix
        payload = bytes.fromhex(res[2:])

        # first 8 bytes is the payload size
        pack_len = int.from_bytes(payload[0:8], byteorder="big")
        if len(payload) < ((pack_len + 1) << 3) + 8:
            raise EncodingError(
                "Invalid geometry encoding. Check your query parameters."
            )

        # followed by n 8 byte coordinates
        pts = []
        for i in range(0, pack_len - 1, 2):
            lat = int.from_bytes(payload[(i + 1) << 3 : (i + 2) << 3], byteorder="big")
            lon = int.from_bytes(payload[(i + 2) << 3 : (i + 3) << 3], byteorder="big")
            pts.append((lat / Precision, lon / Precision))

        return pts
