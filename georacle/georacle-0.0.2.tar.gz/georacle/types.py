from typing import Union

"""
    Georacle uses coordinates with :math:`6` degrees of decimal precision.
    Coordinates in this representation are precise within :math:`~100mm`.

    Note: Depending on the map projection used, areas within some :math:`\ep` of the poles may not be indexable
"""
Precision = 1e6

"""
    Valid latitudes are within :math:`[-\textbf{Lat}_{\textbf{max}}, \textbf{Lat}_{\textbf{max}}]`
"""
LatMax = int(90.0 * Precision)

"""
    Valid longitudes are within :math:`[-\textbf{Lon}_{\textbf{max}}, \textbf{Lon}_{\textbf{max}}]`
"""
LonMax = int(180.0 * Precision)

"""
    Radius of the Earth (in meters)
"""
RadMax = int(6378.1 * 1000 * Precision)

Box = list[float]
Coordinates = tuple[float, float]
RawResponse = dict[str, str]
LocationResponse = Union[RawResponse, list[str]]
CountResponse = Union[RawResponse, int]
GeocodeResponse = Union[RawResponse, tuple[str, float, float]]
ReverseGeocodeResponse = Union[RawResponse, list[str]]
GeometryResponse = Union[RawResponse, list[float]]
