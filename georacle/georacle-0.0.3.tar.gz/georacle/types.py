from typing import Union

Precision = 1e6
"""
    Georacle uses coordinates with :math:`6` degrees of decimal precision.
    Coordinates in this representation are precise within :math:`~100mm`.

    Note: Depending on the map projection used, areas within some :math:`\epsilon` of the poles may not be indexable
"""

LatMax = int(90.0 * Precision)
"""
    Valid latitudes are within :math:`[-Lat_{max}, Lat_{max}]`
"""

LonMax = int(180.0 * Precision)
"""
    Valid longitudes are within :math:`[-Lon_{max}, Lon_{max}]`
"""

RadMax = int(6378.1 * 1000 * Precision)
"""
    Radius of the Earth (in meters)
"""

Box = list[float]
Coordinates = tuple[float, float]
RawResponse = dict[str, str]
LocationResponse = Union[RawResponse, list[str]]
CountResponse = Union[RawResponse, int]
GeocodeResponse = Union[RawResponse, tuple[str, float, float]]
ReverseGeocodeResponse = Union[RawResponse, list[str]]
GeometryResponse = Union[RawResponse, list[float]]
