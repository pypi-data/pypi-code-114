"""
Type annotations for forecastquery service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_forecastquery/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DataPointTypeDef",
    "ForecastTypeDef",
    "QueryForecastRequestRequestTypeDef",
    "QueryForecastResponseTypeDef",
    "ResponseMetadataTypeDef",
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": NotRequired[str],
        "Value": NotRequired[float],
    },
)

ForecastTypeDef = TypedDict(
    "ForecastTypeDef",
    {
        "Predictions": NotRequired[Dict[str, List["DataPointTypeDef"]]],
    },
)

QueryForecastRequestRequestTypeDef = TypedDict(
    "QueryForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
        "Filters": Mapping[str, str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

QueryForecastResponseTypeDef = TypedDict(
    "QueryForecastResponseTypeDef",
    {
        "Forecast": "ForecastTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
