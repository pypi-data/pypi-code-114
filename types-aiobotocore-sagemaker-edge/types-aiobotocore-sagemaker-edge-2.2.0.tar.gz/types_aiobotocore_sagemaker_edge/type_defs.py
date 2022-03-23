"""
Type annotations for sagemaker-edge service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_edge/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sagemaker_edge.type_defs import EdgeMetricTypeDef

    data: EdgeMetricTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, Sequence, Union

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EdgeMetricTypeDef",
    "GetDeviceRegistrationRequestRequestTypeDef",
    "GetDeviceRegistrationResultTypeDef",
    "ModelTypeDef",
    "ResponseMetadataTypeDef",
    "SendHeartbeatRequestRequestTypeDef",
)

EdgeMetricTypeDef = TypedDict(
    "EdgeMetricTypeDef",
    {
        "Dimension": NotRequired[str],
        "MetricName": NotRequired[str],
        "Value": NotRequired[float],
        "Timestamp": NotRequired[Union[datetime, str]],
    },
)

GetDeviceRegistrationRequestRequestTypeDef = TypedDict(
    "GetDeviceRegistrationRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)

GetDeviceRegistrationResultTypeDef = TypedDict(
    "GetDeviceRegistrationResultTypeDef",
    {
        "DeviceRegistration": str,
        "CacheTTL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "ModelName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "LatestSampleTime": NotRequired[Union[datetime, str]],
        "LatestInference": NotRequired[Union[datetime, str]],
        "ModelMetrics": NotRequired[Sequence["EdgeMetricTypeDef"]],
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

SendHeartbeatRequestRequestTypeDef = TypedDict(
    "SendHeartbeatRequestRequestTypeDef",
    {
        "AgentVersion": str,
        "DeviceName": str,
        "DeviceFleetName": str,
        "AgentMetrics": NotRequired[Sequence["EdgeMetricTypeDef"]],
        "Models": NotRequired[Sequence["ModelTypeDef"]],
    },
)
