"""
Type annotations for mediastore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import ContainerLevelMetricsType, ContainerStatusType, MethodNameType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContainerTypeDef",
    "CorsRuleTypeDef",
    "CreateContainerInputRequestTypeDef",
    "CreateContainerOutputTypeDef",
    "DeleteContainerInputRequestTypeDef",
    "DeleteContainerPolicyInputRequestTypeDef",
    "DeleteCorsPolicyInputRequestTypeDef",
    "DeleteLifecyclePolicyInputRequestTypeDef",
    "DeleteMetricPolicyInputRequestTypeDef",
    "DescribeContainerInputRequestTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyInputRequestTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyInputRequestTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyInputRequestTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyInputRequestTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "ListContainersInputRequestTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "PaginatorConfigTypeDef",
    "PutContainerPolicyInputRequestTypeDef",
    "PutCorsPolicyInputRequestTypeDef",
    "PutLifecyclePolicyInputRequestTypeDef",
    "PutMetricPolicyInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartAccessLoggingInputRequestTypeDef",
    "StopAccessLoggingInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ARN": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ContainerStatusType],
        "AccessLoggingEnabled": NotRequired[bool],
    },
)

CorsRuleTypeDef = TypedDict(
    "CorsRuleTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedHeaders": List[str],
        "AllowedMethods": NotRequired[List[MethodNameType]],
        "MaxAgeSeconds": NotRequired[int],
        "ExposeHeaders": NotRequired[List[str]],
    },
)

CreateContainerInputRequestTypeDef = TypedDict(
    "CreateContainerInputRequestTypeDef",
    {
        "ContainerName": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerInputRequestTypeDef = TypedDict(
    "DeleteContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteContainerPolicyInputRequestTypeDef = TypedDict(
    "DeleteContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteCorsPolicyInputRequestTypeDef = TypedDict(
    "DeleteCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteLifecyclePolicyInputRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteMetricPolicyInputRequestTypeDef = TypedDict(
    "DeleteMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

DescribeContainerInputRequestTypeDef = TypedDict(
    "DescribeContainerInputRequestTypeDef",
    {
        "ContainerName": NotRequired[str],
    },
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerPolicyInputRequestTypeDef = TypedDict(
    "GetContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetContainerPolicyOutputTypeDef = TypedDict(
    "GetContainerPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCorsPolicyInputRequestTypeDef = TypedDict(
    "GetCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef",
    {
        "CorsPolicy": List["CorsRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyInputRequestTypeDef = TypedDict(
    "GetLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef",
    {
        "LifecyclePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricPolicyInputRequestTypeDef = TypedDict(
    "GetMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

GetMetricPolicyOutputTypeDef = TypedDict(
    "GetMetricPolicyOutputTypeDef",
    {
        "MetricPolicy": "MetricPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainersInputRequestTypeDef = TypedDict(
    "ListContainersInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListContainersOutputTypeDef = TypedDict(
    "ListContainersOutputTypeDef",
    {
        "Containers": List["ContainerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricPolicyRuleTypeDef = TypedDict(
    "MetricPolicyRuleTypeDef",
    {
        "ObjectGroup": str,
        "ObjectGroupName": str,
    },
)

MetricPolicyTypeDef = TypedDict(
    "MetricPolicyTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
        "MetricPolicyRules": NotRequired[List["MetricPolicyRuleTypeDef"]],
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

PutContainerPolicyInputRequestTypeDef = TypedDict(
    "PutContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "Policy": str,
    },
)

PutCorsPolicyInputRequestTypeDef = TypedDict(
    "PutCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "CorsPolicy": Sequence["CorsRuleTypeDef"],
    },
)

PutLifecyclePolicyInputRequestTypeDef = TypedDict(
    "PutLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "LifecyclePolicy": str,
    },
)

PutMetricPolicyInputRequestTypeDef = TypedDict(
    "PutMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "MetricPolicy": "MetricPolicyTypeDef",
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

StartAccessLoggingInputRequestTypeDef = TypedDict(
    "StartAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

StopAccessLoggingInputRequestTypeDef = TypedDict(
    "StopAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": Sequence[str],
    },
)
