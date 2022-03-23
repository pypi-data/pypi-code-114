"""
Type annotations for iot-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_data.type_defs import DeleteThingShadowRequestRequestTypeDef

    data: DeleteThingShadowRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteThingShadowRequestRequestTypeDef",
    "DeleteThingShadowResponseTypeDef",
    "GetRetainedMessageRequestRequestTypeDef",
    "GetRetainedMessageResponseTypeDef",
    "GetThingShadowRequestRequestTypeDef",
    "GetThingShadowResponseTypeDef",
    "ListNamedShadowsForThingRequestRequestTypeDef",
    "ListNamedShadowsForThingResponseTypeDef",
    "ListRetainedMessagesRequestRequestTypeDef",
    "ListRetainedMessagesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublishRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetainedMessageSummaryTypeDef",
    "UpdateThingShadowRequestRequestTypeDef",
    "UpdateThingShadowResponseTypeDef",
)

DeleteThingShadowRequestRequestTypeDef = TypedDict(
    "DeleteThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "shadowName": NotRequired[str],
    },
)

DeleteThingShadowResponseTypeDef = TypedDict(
    "DeleteThingShadowResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRetainedMessageRequestRequestTypeDef = TypedDict(
    "GetRetainedMessageRequestRequestTypeDef",
    {
        "topic": str,
    },
)

GetRetainedMessageResponseTypeDef = TypedDict(
    "GetRetainedMessageResponseTypeDef",
    {
        "topic": str,
        "payload": bytes,
        "qos": int,
        "lastModifiedTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThingShadowRequestRequestTypeDef = TypedDict(
    "GetThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "shadowName": NotRequired[str],
    },
)

GetThingShadowResponseTypeDef = TypedDict(
    "GetThingShadowResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamedShadowsForThingRequestRequestTypeDef = TypedDict(
    "ListNamedShadowsForThingRequestRequestTypeDef",
    {
        "thingName": str,
        "nextToken": NotRequired[str],
        "pageSize": NotRequired[int],
    },
)

ListNamedShadowsForThingResponseTypeDef = TypedDict(
    "ListNamedShadowsForThingResponseTypeDef",
    {
        "results": List[str],
        "nextToken": str,
        "timestamp": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRetainedMessagesRequestRequestTypeDef = TypedDict(
    "ListRetainedMessagesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListRetainedMessagesResponseTypeDef = TypedDict(
    "ListRetainedMessagesResponseTypeDef",
    {
        "retainedTopics": List["RetainedMessageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PublishRequestRequestTypeDef = TypedDict(
    "PublishRequestRequestTypeDef",
    {
        "topic": str,
        "qos": NotRequired[int],
        "retain": NotRequired[bool],
        "payload": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
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

RetainedMessageSummaryTypeDef = TypedDict(
    "RetainedMessageSummaryTypeDef",
    {
        "topic": NotRequired[str],
        "payloadSize": NotRequired[int],
        "qos": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
    },
)

UpdateThingShadowRequestRequestTypeDef = TypedDict(
    "UpdateThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
        "shadowName": NotRequired[str],
    },
)

UpdateThingShadowResponseTypeDef = TypedDict(
    "UpdateThingShadowResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
