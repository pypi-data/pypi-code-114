"""
Type annotations for autoscaling-plans service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_autoscaling_plans/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_autoscaling_plans.type_defs import ApplicationSourceTypeDef

    data: ApplicationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ForecastDataTypeType,
    LoadMetricTypeType,
    MetricStatisticType,
    PredictiveScalingMaxCapacityBehaviorType,
    PredictiveScalingModeType,
    ScalableDimensionType,
    ScalingMetricTypeType,
    ScalingPlanStatusCodeType,
    ScalingPolicyUpdateBehaviorType,
    ScalingStatusCodeType,
    ServiceNamespaceType,
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
    "ApplicationSourceTypeDef",
    "CreateScalingPlanRequestRequestTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "DatapointTypeDef",
    "DeleteScalingPlanRequestRequestTypeDef",
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "DescribeScalingPlansRequestRequestTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanResourceTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPolicyTypeDef",
    "TagFilterTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "UpdateScalingPlanRequestRequestTypeDef",
)

ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": NotRequired[str],
        "TagFilters": NotRequired[Sequence["TagFilterTypeDef"]],
    },
)

CreateScalingPlanRequestRequestTypeDef = TypedDict(
    "CreateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ApplicationSource": "ApplicationSourceTypeDef",
        "ScalingInstructions": Sequence["ScalingInstructionTypeDef"],
    },
)

CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef",
    {
        "ScalingPlanVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "CustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[Sequence["MetricDimensionTypeDef"]],
        "Unit": NotRequired[str],
    },
)

CustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "CustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[Sequence["MetricDimensionTypeDef"]],
        "Unit": NotRequired[str],
    },
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "Value": NotRequired[float],
    },
)

DeleteScalingPlanRequestRequestTypeDef = TypedDict(
    "DeleteScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
    },
)

DescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List["ScalingPlanResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPlansRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlansRequestRequestTypeDef",
    {
        "ScalingPlanNames": NotRequired[Sequence[str]],
        "ScalingPlanVersion": NotRequired[int],
        "ApplicationSources": NotRequired[Sequence["ApplicationSourceTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {
        "ScalingPlans": List["ScalingPlanTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetScalingPlanResourceForecastDataRequestRequestTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ForecastDataType": ForecastDataTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    {
        "Datapoints": List["DatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
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

PredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "PredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": LoadMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)

PredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "PredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": ScalingMetricTypeType,
        "ResourceLabel": NotRequired[str],
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

ScalingInstructionTypeDef = TypedDict(
    "ScalingInstructionTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": Sequence["TargetTrackingConfigurationTypeDef"],
        "PredefinedLoadMetricSpecification": NotRequired[
            "PredefinedLoadMetricSpecificationTypeDef"
        ],
        "CustomizedLoadMetricSpecification": NotRequired[
            "CustomizedLoadMetricSpecificationTypeDef"
        ],
        "ScheduledActionBufferTime": NotRequired[int],
        "PredictiveScalingMaxCapacityBehavior": NotRequired[
            PredictiveScalingMaxCapacityBehaviorType
        ],
        "PredictiveScalingMaxCapacityBuffer": NotRequired[int],
        "PredictiveScalingMode": NotRequired[PredictiveScalingModeType],
        "ScalingPolicyUpdateBehavior": NotRequired[ScalingPolicyUpdateBehaviorType],
        "DisableDynamicScaling": NotRequired[bool],
    },
)

ScalingPlanResourceTypeDef = TypedDict(
    "ScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ScalingStatusCode": ScalingStatusCodeType,
        "ScalingPolicies": NotRequired[List["ScalingPolicyTypeDef"]],
        "ScalingStatusMessage": NotRequired[str],
    },
)

ScalingPlanTypeDef = TypedDict(
    "ScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": "ApplicationSourceTypeDef",
        "ScalingInstructions": List["ScalingInstructionTypeDef"],
        "StatusCode": ScalingPlanStatusCodeType,
        "StatusMessage": NotRequired[str],
        "StatusStartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
    },
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["TargetTrackingScaling"],
        "TargetTrackingConfiguration": NotRequired["TargetTrackingConfigurationTypeDef"],
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedScalingMetricSpecification": NotRequired[
            "PredefinedScalingMetricSpecificationTypeDef"
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            "CustomizedScalingMetricSpecificationTypeDef"
        ],
        "DisableScaleIn": NotRequired[bool],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)

UpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "UpdateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": NotRequired["ApplicationSourceTypeDef"],
        "ScalingInstructions": NotRequired[Sequence["ScalingInstructionTypeDef"]],
    },
)
