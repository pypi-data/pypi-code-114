"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_iotsecuretunneling/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_iotsecuretunneling.type_defs import CloseTunnelRequestRequestTypeDef

    data: CloseTunnelRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CloseTunnelRequestRequestTypeDef",
    "ConnectionStateTypeDef",
    "DescribeTunnelRequestRequestTypeDef",
    "DescribeTunnelResponseTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsRequestRequestTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelRequestRequestTypeDef",
    "OpenTunnelResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

CloseTunnelRequestRequestTypeDef = TypedDict(
    "CloseTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
        "delete": NotRequired[bool],
    },
)

ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef",
    {
        "status": NotRequired[ConnectionStatusType],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

DescribeTunnelRequestRequestTypeDef = TypedDict(
    "DescribeTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
    },
)

DescribeTunnelResponseTypeDef = TypedDict(
    "DescribeTunnelResponseTypeDef",
    {
        "tunnel": "TunnelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConfigTypeDef = TypedDict(
    "DestinationConfigTypeDef",
    {
        "services": List[str],
        "thingName": NotRequired[str],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTunnelsRequestRequestTypeDef = TypedDict(
    "ListTunnelsRequestRequestTypeDef",
    {
        "thingName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTunnelsResponseTypeDef = TypedDict(
    "ListTunnelsResponseTypeDef",
    {
        "tunnelSummaries": List["TunnelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OpenTunnelRequestRequestTypeDef = TypedDict(
    "OpenTunnelRequestRequestTypeDef",
    {
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "destinationConfig": NotRequired["DestinationConfigTypeDef"],
        "timeoutConfig": NotRequired["TimeoutConfigTypeDef"],
    },
)

OpenTunnelResponseTypeDef = TypedDict(
    "OpenTunnelResponseTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "maxLifetimeTimeoutMinutes": NotRequired[int],
    },
)

TunnelSummaryTypeDef = TypedDict(
    "TunnelSummaryTypeDef",
    {
        "tunnelId": NotRequired[str],
        "tunnelArn": NotRequired[str],
        "status": NotRequired[TunnelStatusType],
        "description": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

TunnelTypeDef = TypedDict(
    "TunnelTypeDef",
    {
        "tunnelId": NotRequired[str],
        "tunnelArn": NotRequired[str],
        "status": NotRequired[TunnelStatusType],
        "sourceConnectionState": NotRequired["ConnectionStateTypeDef"],
        "destinationConnectionState": NotRequired["ConnectionStateTypeDef"],
        "description": NotRequired[str],
        "destinationConfig": NotRequired["DestinationConfigTypeDef"],
        "timeoutConfig": NotRequired["TimeoutConfigTypeDef"],
        "tags": NotRequired[List["TagTypeDef"]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
