"""
Type annotations for elastic-inference service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeOfferingTypeDef

    data: AcceleratorTypeOfferingTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import LocationTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceleratorTypeOfferingTypeDef",
    "AcceleratorTypeTypeDef",
    "DescribeAcceleratorOfferingsRequestRequestTypeDef",
    "DescribeAcceleratorOfferingsResponseTypeDef",
    "DescribeAcceleratorTypesResponseTypeDef",
    "DescribeAcceleratorsRequestRequestTypeDef",
    "DescribeAcceleratorsResponseTypeDef",
    "ElasticInferenceAcceleratorHealthTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "FilterTypeDef",
    "KeyValuePairTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MemoryInfoTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AcceleratorTypeOfferingTypeDef = TypedDict(
    "AcceleratorTypeOfferingTypeDef",
    {
        "acceleratorType": NotRequired[str],
        "locationType": NotRequired[LocationTypeType],
        "location": NotRequired[str],
    },
)

AcceleratorTypeTypeDef = TypedDict(
    "AcceleratorTypeTypeDef",
    {
        "acceleratorTypeName": NotRequired[str],
        "memoryInfo": NotRequired["MemoryInfoTypeDef"],
        "throughputInfo": NotRequired[List["KeyValuePairTypeDef"]],
    },
)

DescribeAcceleratorOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorOfferingsRequestRequestTypeDef",
    {
        "locationType": LocationTypeType,
        "acceleratorTypes": NotRequired[Sequence[str]],
    },
)

DescribeAcceleratorOfferingsResponseTypeDef = TypedDict(
    "DescribeAcceleratorOfferingsResponseTypeDef",
    {
        "acceleratorTypeOfferings": List["AcceleratorTypeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorTypesResponseTypeDef = TypedDict(
    "DescribeAcceleratorTypesResponseTypeDef",
    {
        "acceleratorTypes": List["AcceleratorTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorsRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorsRequestRequestTypeDef",
    {
        "acceleratorIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeAcceleratorsResponseTypeDef = TypedDict(
    "DescribeAcceleratorsResponseTypeDef",
    {
        "acceleratorSet": List["ElasticInferenceAcceleratorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ElasticInferenceAcceleratorHealthTypeDef = TypedDict(
    "ElasticInferenceAcceleratorHealthTypeDef",
    {
        "status": NotRequired[str],
    },
)

ElasticInferenceAcceleratorTypeDef = TypedDict(
    "ElasticInferenceAcceleratorTypeDef",
    {
        "acceleratorHealth": NotRequired["ElasticInferenceAcceleratorHealthTypeDef"],
        "acceleratorType": NotRequired[str],
        "acceleratorId": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "attachedResource": NotRequired[str],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[int],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "sizeInMiB": NotRequired[int],
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
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
