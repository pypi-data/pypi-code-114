"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kinesisvideo.type_defs import ChannelInfoTypeDef

    data: ChannelInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    APINameType,
    ChannelProtocolType,
    ChannelRoleType,
    StatusType,
    UpdateDataRetentionOperationType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChannelInfoTypeDef",
    "ChannelNameConditionTypeDef",
    "CreateSignalingChannelInputRequestTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamInputRequestTypeDef",
    "CreateStreamOutputTypeDef",
    "DeleteSignalingChannelInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DescribeSignalingChannelInputRequestTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetDataEndpointInputRequestTypeDef",
    "GetDataEndpointOutputTypeDef",
    "GetSignalingChannelEndpointInputRequestTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ListSignalingChannelsInputRequestTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadataTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "StreamInfoTypeDef",
    "StreamNameConditionTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagStreamInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagStreamInputRequestTypeDef",
    "UpdateDataRetentionInputRequestTypeDef",
    "UpdateSignalingChannelInputRequestTypeDef",
    "UpdateStreamInputRequestTypeDef",
)

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": NotRequired[str],
        "ChannelARN": NotRequired[str],
        "ChannelType": NotRequired[Literal["SINGLE_MASTER"]],
        "ChannelStatus": NotRequired[StatusType],
        "CreationTime": NotRequired[datetime],
        "SingleMasterConfiguration": NotRequired["SingleMasterConfigurationTypeDef"],
        "Version": NotRequired[str],
    },
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {
        "ComparisonOperator": NotRequired[Literal["BEGINS_WITH"]],
        "ComparisonValue": NotRequired[str],
    },
)

CreateSignalingChannelInputRequestTypeDef = TypedDict(
    "CreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelType": NotRequired[Literal["SINGLE_MASTER"]],
        "SingleMasterConfiguration": NotRequired["SingleMasterConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamInputRequestTypeDef = TypedDict(
    "CreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "DeviceName": NotRequired[str],
        "MediaType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "DataRetentionInHours": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "DeleteSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": NotRequired[str],
    },
)

DeleteStreamInputRequestTypeDef = TypedDict(
    "DeleteStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "CurrentVersion": NotRequired[str],
    },
)

DescribeSignalingChannelInputRequestTypeDef = TypedDict(
    "DescribeSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": NotRequired[str],
        "ChannelARN": NotRequired[str],
    },
)

DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {
        "ChannelInfo": "ChannelInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamInfo": "StreamInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataEndpointInputRequestTypeDef = TypedDict(
    "GetDataEndpointInputRequestTypeDef",
    {
        "APIName": APINameType,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)

GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "GetSignalingChannelEndpointInputRequestTypeDef",
    {
        "ChannelARN": str,
        "SingleMasterChannelEndpointConfiguration": NotRequired[
            "SingleMasterChannelEndpointConfigurationTypeDef"
        ],
    },
)

GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List["ResourceEndpointListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalingChannelsInputRequestTypeDef = TypedDict(
    "ListSignalingChannelsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChannelNameCondition": NotRequired["ChannelNameConditionTypeDef"],
    },
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List["ChannelInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StreamNameCondition": NotRequired["StreamNameConditionTypeDef"],
    },
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List["StreamInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "StreamARN": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
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

ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {
        "Protocol": NotRequired[ChannelProtocolType],
        "ResourceEndpoint": NotRequired[str],
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

SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {
        "Protocols": NotRequired[Sequence[ChannelProtocolType]],
        "Role": NotRequired[ChannelRoleType],
    },
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef",
    {
        "MessageTtlSeconds": NotRequired[int],
    },
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": NotRequired[str],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "MediaType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Version": NotRequired[str],
        "Status": NotRequired[StatusType],
        "CreationTime": NotRequired[datetime],
        "DataRetentionInHours": NotRequired[int],
    },
)

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {
        "ComparisonOperator": NotRequired[Literal["BEGINS_WITH"]],
        "ComparisonValue": NotRequired[str],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagStreamInputRequestTypeDef = TypedDict(
    "TagStreamInputRequestTypeDef",
    {
        "Tags": Mapping[str, str],
        "StreamARN": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeyList": Sequence[str],
    },
)

UntagStreamInputRequestTypeDef = TypedDict(
    "UntagStreamInputRequestTypeDef",
    {
        "TagKeyList": Sequence[str],
        "StreamARN": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)

UpdateDataRetentionInputRequestTypeDef = TypedDict(
    "UpdateDataRetentionInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "Operation": UpdateDataRetentionOperationType,
        "DataRetentionChangeInHours": int,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)

UpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "UpdateSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": str,
        "SingleMasterConfiguration": NotRequired["SingleMasterConfigurationTypeDef"],
    },
)

UpdateStreamInputRequestTypeDef = TypedDict(
    "UpdateStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "DeviceName": NotRequired[str],
        "MediaType": NotRequired[str],
    },
)
