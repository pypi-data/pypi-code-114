"""
Type annotations for pi service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_pi/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_pi.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import DetailStatusType, FeatureStatusType, ServiceTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DataPointTypeDef",
    "DescribeDimensionKeysRequestRequestTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "DimensionDetailTypeDef",
    "DimensionGroupDetailTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "DimensionKeyDetailTypeDef",
    "FeatureMetadataTypeDef",
    "GetDimensionKeyDetailsRequestRequestTypeDef",
    "GetDimensionKeyDetailsResponseTypeDef",
    "GetResourceMetadataRequestRequestTypeDef",
    "GetResourceMetadataResponseTypeDef",
    "GetResourceMetricsRequestRequestTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "ListAvailableResourceDimensionsRequestRequestTypeDef",
    "ListAvailableResourceDimensionsResponseTypeDef",
    "ListAvailableResourceMetricsRequestRequestTypeDef",
    "ListAvailableResourceMetricsResponseTypeDef",
    "MetricDimensionGroupsTypeDef",
    "MetricKeyDataPointsTypeDef",
    "MetricQueryTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
    "ResponseResourceMetricTypeDef",
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": datetime,
        "Value": float,
    },
)

DescribeDimensionKeysRequestRequestTypeDef = TypedDict(
    "DescribeDimensionKeysRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Metric": str,
        "GroupBy": "DimensionGroupTypeDef",
        "PeriodInSeconds": NotRequired[int],
        "AdditionalMetrics": NotRequired[Sequence[str]],
        "PartitionBy": NotRequired["DimensionGroupTypeDef"],
        "Filter": NotRequired[Mapping[str, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeDimensionKeysResponseTypeDef = TypedDict(
    "DescribeDimensionKeysResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "PartitionKeys": List["ResponsePartitionKeyTypeDef"],
        "Keys": List["DimensionKeyDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionDetailTypeDef = TypedDict(
    "DimensionDetailTypeDef",
    {
        "Identifier": NotRequired[str],
    },
)

DimensionGroupDetailTypeDef = TypedDict(
    "DimensionGroupDetailTypeDef",
    {
        "Group": NotRequired[str],
        "Dimensions": NotRequired[List["DimensionDetailTypeDef"]],
    },
)

DimensionGroupTypeDef = TypedDict(
    "DimensionGroupTypeDef",
    {
        "Group": str,
        "Dimensions": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
    },
)

DimensionKeyDescriptionTypeDef = TypedDict(
    "DimensionKeyDescriptionTypeDef",
    {
        "Dimensions": NotRequired[Dict[str, str]],
        "Total": NotRequired[float],
        "AdditionalMetrics": NotRequired[Dict[str, float]],
        "Partitions": NotRequired[List[float]],
    },
)

DimensionKeyDetailTypeDef = TypedDict(
    "DimensionKeyDetailTypeDef",
    {
        "Value": NotRequired[str],
        "Dimension": NotRequired[str],
        "Status": NotRequired[DetailStatusType],
    },
)

FeatureMetadataTypeDef = TypedDict(
    "FeatureMetadataTypeDef",
    {
        "Status": NotRequired[FeatureStatusType],
    },
)

GetDimensionKeyDetailsRequestRequestTypeDef = TypedDict(
    "GetDimensionKeyDetailsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "Group": str,
        "GroupIdentifier": str,
        "RequestedDimensions": NotRequired[Sequence[str]],
    },
)

GetDimensionKeyDetailsResponseTypeDef = TypedDict(
    "GetDimensionKeyDetailsResponseTypeDef",
    {
        "Dimensions": List["DimensionKeyDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceMetadataRequestRequestTypeDef = TypedDict(
    "GetResourceMetadataRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
    },
)

GetResourceMetadataResponseTypeDef = TypedDict(
    "GetResourceMetadataResponseTypeDef",
    {
        "Identifier": str,
        "Features": Dict[str, "FeatureMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceMetricsRequestRequestTypeDef = TypedDict(
    "GetResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "MetricQueries": Sequence["MetricQueryTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "PeriodInSeconds": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetResourceMetricsResponseTypeDef = TypedDict(
    "GetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List["MetricKeyDataPointsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableResourceDimensionsRequestRequestTypeDef = TypedDict(
    "ListAvailableResourceDimensionsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "Metrics": Sequence[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAvailableResourceDimensionsResponseTypeDef = TypedDict(
    "ListAvailableResourceDimensionsResponseTypeDef",
    {
        "MetricDimensions": List["MetricDimensionGroupsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableResourceMetricsRequestRequestTypeDef = TypedDict(
    "ListAvailableResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "MetricTypes": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAvailableResourceMetricsResponseTypeDef = TypedDict(
    "ListAvailableResourceMetricsResponseTypeDef",
    {
        "Metrics": List["ResponseResourceMetricTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDimensionGroupsTypeDef = TypedDict(
    "MetricDimensionGroupsTypeDef",
    {
        "Metric": NotRequired[str],
        "Groups": NotRequired[List["DimensionGroupDetailTypeDef"]],
    },
)

MetricKeyDataPointsTypeDef = TypedDict(
    "MetricKeyDataPointsTypeDef",
    {
        "Key": NotRequired["ResponseResourceMetricKeyTypeDef"],
        "DataPoints": NotRequired[List["DataPointTypeDef"]],
    },
)

MetricQueryTypeDef = TypedDict(
    "MetricQueryTypeDef",
    {
        "Metric": str,
        "GroupBy": NotRequired["DimensionGroupTypeDef"],
        "Filter": NotRequired[Mapping[str, str]],
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

ResponsePartitionKeyTypeDef = TypedDict(
    "ResponsePartitionKeyTypeDef",
    {
        "Dimensions": Dict[str, str],
    },
)

ResponseResourceMetricKeyTypeDef = TypedDict(
    "ResponseResourceMetricKeyTypeDef",
    {
        "Metric": str,
        "Dimensions": NotRequired[Dict[str, str]],
    },
)

ResponseResourceMetricTypeDef = TypedDict(
    "ResponseResourceMetricTypeDef",
    {
        "Metric": NotRequired[str],
        "Description": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
