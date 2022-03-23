"""
Type annotations for application-autoscaling service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_application_autoscaling/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AdjustmentTypeType,
    MetricAggregationTypeType,
    MetricStatisticType,
    MetricTypeType,
    PolicyTypeType,
    ScalableDimensionType,
    ScalingActivityStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteScalingPolicyRequestRequestTypeDef",
    "DeleteScheduledActionRequestRequestTypeDef",
    "DeregisterScalableTargetRequestRequestTypeDef",
    "DescribeScalableTargetsRequestRequestTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "DescribeScalingActivitiesRequestRequestTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScalingPoliciesRequestRequestTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "DescribeScheduledActionsRequestRequestTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PutScalingPolicyRequestRequestTypeDef",
    "PutScalingPolicyResponseTypeDef",
    "PutScheduledActionRequestRequestTypeDef",
    "RegisterScalableTargetRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScalableTargetActionTypeDef",
    "ScalableTargetTypeDef",
    "ScalingActivityTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "SuspendedStateTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmARN": str,
    },
)

CustomizedMetricSpecificationTypeDef = TypedDict(
    "CustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[List["MetricDimensionTypeDef"]],
        "Unit": NotRequired[str],
    },
)

DeleteScalingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteScalingPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DeleteScheduledActionRequestRequestTypeDef = TypedDict(
    "DeleteScheduledActionRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DeregisterScalableTargetRequestRequestTypeDef = TypedDict(
    "DeregisterScalableTargetRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)

DescribeScalableTargetsRequestRequestTypeDef = TypedDict(
    "DescribeScalableTargetsRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceIds": NotRequired[Sequence[str]],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScalableTargetsResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List["ScalableTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingActivitiesRequestRequestTypeDef = TypedDict(
    "DescribeScalingActivitiesRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScalingActivitiesResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List["ScalingActivityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeScalingPoliciesRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "PolicyNames": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScalingPoliciesResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledActionsRequestRequestTypeDef = TypedDict(
    "DescribeScheduledActionsRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionNames": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScheduledActionsResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "NextToken": str,
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

PredefinedMetricSpecificationTypeDef = TypedDict(
    "PredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": MetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)

PutScalingPolicyRequestRequestTypeDef = TypedDict(
    "PutScalingPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "PolicyType": NotRequired[PolicyTypeType],
        "StepScalingPolicyConfiguration": NotRequired["StepScalingPolicyConfigurationTypeDef"],
        "TargetTrackingScalingPolicyConfiguration": NotRequired[
            "TargetTrackingScalingPolicyConfigurationTypeDef"
        ],
    },
)

PutScalingPolicyResponseTypeDef = TypedDict(
    "PutScalingPolicyResponseTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List["AlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutScheduledActionRequestRequestTypeDef = TypedDict(
    "PutScheduledActionRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "Schedule": NotRequired[str],
        "Timezone": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "ScalableTargetAction": NotRequired["ScalableTargetActionTypeDef"],
    },
)

RegisterScalableTargetRequestRequestTypeDef = TypedDict(
    "RegisterScalableTargetRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
        "RoleARN": NotRequired[str],
        "SuspendedState": NotRequired["SuspendedStateTypeDef"],
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

ScalableTargetActionTypeDef = TypedDict(
    "ScalableTargetActionTypeDef",
    {
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
    },
)

ScalableTargetTypeDef = TypedDict(
    "ScalableTargetTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": NotRequired["SuspendedStateTypeDef"],
    },
)

ScalingActivityTypeDef = TypedDict(
    "ScalingActivityTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
        "EndTime": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
        "Details": NotRequired[str],
    },
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "PolicyType": PolicyTypeType,
        "CreationTime": datetime,
        "StepScalingPolicyConfiguration": NotRequired["StepScalingPolicyConfigurationTypeDef"],
        "TargetTrackingScalingPolicyConfiguration": NotRequired[
            "TargetTrackingScalingPolicyConfigurationTypeDef"
        ],
        "Alarms": NotRequired[List["AlarmTypeDef"]],
    },
)

ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": ServiceNamespaceType,
        "Schedule": str,
        "ResourceId": str,
        "CreationTime": datetime,
        "Timezone": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ScalableTargetAction": NotRequired["ScalableTargetActionTypeDef"],
    },
)

StepAdjustmentTypeDef = TypedDict(
    "StepAdjustmentTypeDef",
    {
        "ScalingAdjustment": int,
        "MetricIntervalLowerBound": NotRequired[float],
        "MetricIntervalUpperBound": NotRequired[float],
    },
)

StepScalingPolicyConfigurationTypeDef = TypedDict(
    "StepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": NotRequired[AdjustmentTypeType],
        "StepAdjustments": NotRequired[List["StepAdjustmentTypeDef"]],
        "MinAdjustmentMagnitude": NotRequired[int],
        "Cooldown": NotRequired[int],
        "MetricAggregationType": NotRequired[MetricAggregationTypeType],
    },
)

SuspendedStateTypeDef = TypedDict(
    "SuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": NotRequired[bool],
        "DynamicScalingOutSuspended": NotRequired[bool],
        "ScheduledScalingSuspended": NotRequired[bool],
    },
)

TargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": NotRequired["PredefinedMetricSpecificationTypeDef"],
        "CustomizedMetricSpecification": NotRequired["CustomizedMetricSpecificationTypeDef"],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "DisableScaleIn": NotRequired[bool],
    },
)
