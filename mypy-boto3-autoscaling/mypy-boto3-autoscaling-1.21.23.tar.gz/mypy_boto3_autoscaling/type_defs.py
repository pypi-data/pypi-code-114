"""
Type annotations for autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import AcceleratorCountRequestTypeDef

    data: AcceleratorCountRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AcceleratorManufacturerType,
    AcceleratorNameType,
    AcceleratorTypeType,
    BareMetalType,
    BurstablePerformanceType,
    CpuManufacturerType,
    InstanceGenerationType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataHttpTokensStateType,
    InstanceRefreshStatusType,
    LifecycleStateType,
    LocalStorageType,
    LocalStorageTypeType,
    MetricStatisticType,
    MetricTypeType,
    PredefinedLoadMetricTypeType,
    PredefinedMetricPairTypeType,
    PredefinedScalingMetricTypeType,
    PredictiveScalingMaxCapacityBreachBehaviorType,
    PredictiveScalingModeType,
    ScalingActivityStatusCodeType,
    WarmPoolStateType,
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
    "AcceleratorCountRequestTypeDef",
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    "ActivitiesTypeTypeDef",
    "ActivityTypeDef",
    "ActivityTypeTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmTypeDef",
    "AttachInstancesQueryRequestTypeDef",
    "AttachLoadBalancerTargetGroupsTypeRequestTypeDef",
    "AttachLoadBalancersTypeRequestTypeDef",
    "AutoScalingGroupNamesTypeRequestTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    "BatchDeleteScheduledActionAnswerTypeDef",
    "BatchDeleteScheduledActionTypeRequestTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    "BatchPutScheduledUpdateGroupActionTypeRequestTypeDef",
    "BlockDeviceMappingTypeDef",
    "CancelInstanceRefreshAnswerTypeDef",
    "CancelInstanceRefreshTypeRequestTypeDef",
    "CapacityForecastTypeDef",
    "CompleteLifecycleActionTypeRequestTypeDef",
    "CreateAutoScalingGroupTypeRequestTypeDef",
    "CreateLaunchConfigurationTypeRequestTypeDef",
    "CreateOrUpdateTagsTypeRequestTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DeleteAutoScalingGroupTypeRequestTypeDef",
    "DeleteLifecycleHookTypeRequestTypeDef",
    "DeleteNotificationConfigurationTypeRequestTypeDef",
    "DeletePolicyTypeRequestTypeDef",
    "DeleteScheduledActionTypeRequestTypeDef",
    "DeleteTagsTypeRequestTypeDef",
    "DeleteWarmPoolTypeRequestTypeDef",
    "DescribeAccountLimitsAnswerTypeDef",
    "DescribeAdjustmentTypesAnswerTypeDef",
    "DescribeAutoScalingInstancesTypeRequestTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    "DescribeInstanceRefreshesAnswerTypeDef",
    "DescribeInstanceRefreshesTypeRequestTypeDef",
    "DescribeLifecycleHookTypesAnswerTypeDef",
    "DescribeLifecycleHooksAnswerTypeDef",
    "DescribeLifecycleHooksTypeRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "DescribeLoadBalancersRequestRequestTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "DescribeNotificationConfigurationsTypeRequestTypeDef",
    "DescribePoliciesTypeRequestTypeDef",
    "DescribeScalingActivitiesTypeRequestTypeDef",
    "DescribeScheduledActionsTypeRequestTypeDef",
    "DescribeTagsTypeRequestTypeDef",
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    "DescribeWarmPoolAnswerTypeDef",
    "DescribeWarmPoolTypeRequestTypeDef",
    "DesiredConfigurationTypeDef",
    "DetachInstancesAnswerTypeDef",
    "DetachInstancesQueryRequestTypeDef",
    "DetachLoadBalancerTargetGroupsTypeRequestTypeDef",
    "DetachLoadBalancersTypeRequestTypeDef",
    "DisableMetricsCollectionQueryRequestTypeDef",
    "EbsTypeDef",
    "EnableMetricsCollectionQueryRequestTypeDef",
    "EnabledMetricTypeDef",
    "EnterStandbyAnswerTypeDef",
    "EnterStandbyQueryRequestTypeDef",
    "ExecutePolicyTypeRequestTypeDef",
    "ExitStandbyAnswerTypeDef",
    "ExitStandbyQueryRequestTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "FilterTypeDef",
    "GetPredictiveScalingForecastAnswerTypeDef",
    "GetPredictiveScalingForecastTypeRequestTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceRefreshLivePoolProgressTypeDef",
    "InstanceRefreshProgressDetailsTypeDef",
    "InstanceRefreshTypeDef",
    "InstanceRefreshWarmPoolProgressTypeDef",
    "InstanceRequirementsTypeDef",
    "InstanceReusePolicyTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationNameTypeRequestTypeDef",
    "LaunchConfigurationNamesTypeRequestTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "LifecycleHookTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "LoadForecastTypeDef",
    "MemoryGiBPerVCpuRequestTypeDef",
    "MemoryMiBRequestTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDimensionTypeDef",
    "MetricGranularityTypeTypeDef",
    "MetricStatTypeDef",
    "MetricTypeDef",
    "MixedInstancesPolicyTypeDef",
    "NetworkInterfaceCountRequestTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeTypeDef",
    "PolicyARNTypeTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PredictiveScalingConfigurationTypeDef",
    "PredictiveScalingCustomizedCapacityMetricTypeDef",
    "PredictiveScalingCustomizedLoadMetricTypeDef",
    "PredictiveScalingCustomizedScalingMetricTypeDef",
    "PredictiveScalingMetricSpecificationTypeDef",
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    "PredictiveScalingPredefinedMetricPairTypeDef",
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    "ProcessTypeTypeDef",
    "ProcessesTypeTypeDef",
    "PutLifecycleHookTypeRequestTypeDef",
    "PutNotificationConfigurationTypeRequestTypeDef",
    "PutScalingPolicyTypeRequestTypeDef",
    "PutScheduledUpdateGroupActionTypeRequestTypeDef",
    "PutWarmPoolTypeRequestTypeDef",
    "RecordLifecycleActionHeartbeatTypeRequestTypeDef",
    "RefreshPreferencesTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingPolicyTypeDef",
    "ScalingProcessQueryRequestTypeDef",
    "ScheduledActionsTypeTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "SetDesiredCapacityTypeRequestTypeDef",
    "SetInstanceHealthQueryRequestTypeDef",
    "SetInstanceProtectionQueryRequestTypeDef",
    "StartInstanceRefreshAnswerTypeDef",
    "StartInstanceRefreshTypeRequestTypeDef",
    "StepAdjustmentTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TagsTypeTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "TerminateInstanceInAutoScalingGroupTypeRequestTypeDef",
    "TotalLocalStorageGBRequestTypeDef",
    "UpdateAutoScalingGroupTypeRequestTypeDef",
    "VCpuCountRequestTypeDef",
    "WarmPoolConfigurationTypeDef",
)

AcceleratorCountRequestTypeDef = TypedDict(
    "AcceleratorCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AcceleratorTotalMemoryMiBRequestTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

ActivitiesTypeTypeDef = TypedDict(
    "ActivitiesTypeTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
        "Description": NotRequired[str],
        "EndTime": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
        "Progress": NotRequired[int],
        "Details": NotRequired[str],
        "AutoScalingGroupState": NotRequired[str],
        "AutoScalingGroupARN": NotRequired[str],
    },
)

ActivityTypeTypeDef = TypedDict(
    "ActivityTypeTypeDef",
    {
        "Activity": "ActivityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdjustmentTypeTypeDef = TypedDict(
    "AdjustmentTypeTypeDef",
    {
        "AdjustmentType": NotRequired[str],
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": NotRequired[str],
        "AlarmARN": NotRequired[str],
    },
)

AttachInstancesQueryRequestTypeDef = TypedDict(
    "AttachInstancesQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)

AttachLoadBalancerTargetGroupsTypeRequestTypeDef = TypedDict(
    "AttachLoadBalancerTargetGroupsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": Sequence[str],
    },
)

AttachLoadBalancersTypeRequestTypeDef = TypedDict(
    "AttachLoadBalancersTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": Sequence[str],
    },
)

AutoScalingGroupNamesTypeRequestTypeDef = TypedDict(
    "AutoScalingGroupNamesTypeRequestTypeDef",
    {
        "AutoScalingGroupNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "CreatedTime": datetime,
        "AutoScalingGroupARN": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "MixedInstancesPolicy": NotRequired["MixedInstancesPolicyTypeDef"],
        "PredictedCapacity": NotRequired[int],
        "LoadBalancerNames": NotRequired[List[str]],
        "TargetGroupARNs": NotRequired[List[str]],
        "HealthCheckGracePeriod": NotRequired[int],
        "Instances": NotRequired[List["InstanceTypeDef"]],
        "SuspendedProcesses": NotRequired[List["SuspendedProcessTypeDef"]],
        "PlacementGroup": NotRequired[str],
        "VPCZoneIdentifier": NotRequired[str],
        "EnabledMetrics": NotRequired[List["EnabledMetricTypeDef"]],
        "Status": NotRequired[str],
        "Tags": NotRequired[List["TagDescriptionTypeDef"]],
        "TerminationPolicies": NotRequired[List[str]],
        "NewInstancesProtectedFromScaleIn": NotRequired[bool],
        "ServiceLinkedRoleARN": NotRequired[str],
        "MaxInstanceLifetime": NotRequired[int],
        "CapacityRebalance": NotRequired[bool],
        "WarmPoolConfiguration": NotRequired["WarmPoolConfigurationTypeDef"],
        "WarmPoolSize": NotRequired[int],
        "Context": NotRequired[str],
        "DesiredCapacityType": NotRequired[str],
    },
)

AutoScalingGroupsTypeTypeDef = TypedDict(
    "AutoScalingGroupsTypeTypeDef",
    {
        "AutoScalingGroups": List["AutoScalingGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoScalingInstanceDetailsTypeDef = TypedDict(
    "AutoScalingInstanceDetailsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
        "InstanceType": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "WeightedCapacity": NotRequired[str],
    },
)

AutoScalingInstancesTypeTypeDef = TypedDict(
    "AutoScalingInstancesTypeTypeDef",
    {
        "AutoScalingInstances": List["AutoScalingInstanceDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BaselineEbsBandwidthMbpsRequestTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

BatchDeleteScheduledActionAnswerTypeDef = TypedDict(
    "BatchDeleteScheduledActionAnswerTypeDef",
    {
        "FailedScheduledActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteScheduledActionTypeRequestTypeDef = TypedDict(
    "BatchDeleteScheduledActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionNames": Sequence[str],
    },
)

BatchPutScheduledUpdateGroupActionAnswerTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List["FailedScheduledUpdateGroupActionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledUpdateGroupActions": Sequence["ScheduledUpdateGroupActionRequestTypeDef"],
    },
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired["EbsTypeDef"],
        "NoDevice": NotRequired[bool],
    },
)

CancelInstanceRefreshAnswerTypeDef = TypedDict(
    "CancelInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelInstanceRefreshTypeRequestTypeDef = TypedDict(
    "CancelInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)

CapacityForecastTypeDef = TypedDict(
    "CapacityForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
    },
)

CompleteLifecycleActionTypeRequestTypeDef = TypedDict(
    "CompleteLifecycleActionTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleActionResult": str,
        "LifecycleActionToken": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)

CreateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "CreateAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "MixedInstancesPolicy": NotRequired["MixedInstancesPolicyTypeDef"],
        "InstanceId": NotRequired[str],
        "DesiredCapacity": NotRequired[int],
        "DefaultCooldown": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "TargetGroupARNs": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "PlacementGroup": NotRequired[str],
        "VPCZoneIdentifier": NotRequired[str],
        "TerminationPolicies": NotRequired[Sequence[str]],
        "NewInstancesProtectedFromScaleIn": NotRequired[bool],
        "CapacityRebalance": NotRequired[bool],
        "LifecycleHookSpecificationList": NotRequired[
            Sequence["LifecycleHookSpecificationTypeDef"]
        ],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ServiceLinkedRoleARN": NotRequired[str],
        "MaxInstanceLifetime": NotRequired[int],
        "Context": NotRequired[str],
        "DesiredCapacityType": NotRequired[str],
    },
)

CreateLaunchConfigurationTypeRequestTypeDef = TypedDict(
    "CreateLaunchConfigurationTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
        "ImageId": NotRequired[str],
        "KeyName": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "ClassicLinkVPCId": NotRequired[str],
        "ClassicLinkVPCSecurityGroups": NotRequired[Sequence[str]],
        "UserData": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "InstanceMonitoring": NotRequired["InstanceMonitoringTypeDef"],
        "SpotPrice": NotRequired[str],
        "IamInstanceProfile": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "PlacementTenancy": NotRequired[str],
        "MetadataOptions": NotRequired["InstanceMetadataOptionsTypeDef"],
    },
)

CreateOrUpdateTagsTypeRequestTypeDef = TypedDict(
    "CreateOrUpdateTagsTypeRequestTypeDef",
    {
        "Tags": Sequence["TagTypeDef"],
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

DeleteAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "DeleteAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ForceDelete": NotRequired[bool],
    },
)

DeleteLifecycleHookTypeRequestTypeDef = TypedDict(
    "DeleteLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)

DeleteNotificationConfigurationTypeRequestTypeDef = TypedDict(
    "DeleteNotificationConfigurationTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
    },
)

DeletePolicyTypeRequestTypeDef = TypedDict(
    "DeletePolicyTypeRequestTypeDef",
    {
        "PolicyName": str,
        "AutoScalingGroupName": NotRequired[str],
    },
)

DeleteScheduledActionTypeRequestTypeDef = TypedDict(
    "DeleteScheduledActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
    },
)

DeleteTagsTypeRequestTypeDef = TypedDict(
    "DeleteTagsTypeRequestTypeDef",
    {
        "Tags": Sequence["TagTypeDef"],
    },
)

DeleteWarmPoolTypeRequestTypeDef = TypedDict(
    "DeleteWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ForceDelete": NotRequired[bool],
    },
)

DescribeAccountLimitsAnswerTypeDef = TypedDict(
    "DescribeAccountLimitsAnswerTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAdjustmentTypesAnswerTypeDef = TypedDict(
    "DescribeAdjustmentTypesAnswerTypeDef",
    {
        "AdjustmentTypes": List["AdjustmentTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingInstancesTypeRequestTypeDef = TypedDict(
    "DescribeAutoScalingInstancesTypeRequestTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAutoScalingNotificationTypesAnswerTypeDef = TypedDict(
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    {
        "AutoScalingNotificationTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRefreshesAnswerTypeDef = TypedDict(
    "DescribeInstanceRefreshesAnswerTypeDef",
    {
        "InstanceRefreshes": List["InstanceRefreshTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRefreshesTypeRequestTypeDef = TypedDict(
    "DescribeInstanceRefreshesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "InstanceRefreshIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeLifecycleHookTypesAnswerTypeDef = TypedDict(
    "DescribeLifecycleHookTypesAnswerTypeDef",
    {
        "LifecycleHookTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLifecycleHooksAnswerTypeDef = TypedDict(
    "DescribeLifecycleHooksAnswerTypeDef",
    {
        "LifecycleHooks": List["LifecycleHookTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLifecycleHooksTypeRequestTypeDef = TypedDict(
    "DescribeLifecycleHooksTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LifecycleHookNames": NotRequired[Sequence[str]],
    },
)

DescribeLoadBalancerTargetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List["LoadBalancerTargetGroupStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersRequestRequestTypeDef = TypedDict(
    "DescribeLoadBalancersRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeLoadBalancersResponseTypeDef = TypedDict(
    "DescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List["LoadBalancerStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricCollectionTypesAnswerTypeDef = TypedDict(
    "DescribeMetricCollectionTypesAnswerTypeDef",
    {
        "Metrics": List["MetricCollectionTypeTypeDef"],
        "Granularities": List["MetricGranularityTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "DescribeNotificationConfigurationsAnswerTypeDef",
    {
        "NotificationConfigurations": List["NotificationConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationsTypeRequestTypeDef = TypedDict(
    "DescribeNotificationConfigurationsTypeRequestTypeDef",
    {
        "AutoScalingGroupNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribePoliciesTypeRequestTypeDef = TypedDict(
    "DescribePoliciesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "PolicyNames": NotRequired[Sequence[str]],
        "PolicyTypes": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeScalingActivitiesTypeRequestTypeDef = TypedDict(
    "DescribeScalingActivitiesTypeRequestTypeDef",
    {
        "ActivityIds": NotRequired[Sequence[str]],
        "AutoScalingGroupName": NotRequired[str],
        "IncludeDeletedGroups": NotRequired[bool],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeScheduledActionsTypeRequestTypeDef = TypedDict(
    "DescribeScheduledActionsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "ScheduledActionNames": NotRequired[Sequence[str]],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeTagsTypeRequestTypeDef = TypedDict(
    "DescribeTagsTypeRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeTerminationPolicyTypesAnswerTypeDef = TypedDict(
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    {
        "TerminationPolicyTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWarmPoolAnswerTypeDef = TypedDict(
    "DescribeWarmPoolAnswerTypeDef",
    {
        "WarmPoolConfiguration": "WarmPoolConfigurationTypeDef",
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWarmPoolTypeRequestTypeDef = TypedDict(
    "DescribeWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DesiredConfigurationTypeDef = TypedDict(
    "DesiredConfigurationTypeDef",
    {
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "MixedInstancesPolicy": NotRequired["MixedInstancesPolicyTypeDef"],
    },
)

DetachInstancesAnswerTypeDef = TypedDict(
    "DetachInstancesAnswerTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachInstancesQueryRequestTypeDef = TypedDict(
    "DetachInstancesQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)

DetachLoadBalancerTargetGroupsTypeRequestTypeDef = TypedDict(
    "DetachLoadBalancerTargetGroupsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": Sequence[str],
    },
)

DetachLoadBalancersTypeRequestTypeDef = TypedDict(
    "DetachLoadBalancersTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": Sequence[str],
    },
)

DisableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "DisableMetricsCollectionQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Metrics": NotRequired[Sequence[str]],
    },
)

EbsTypeDef = TypedDict(
    "EbsTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "Encrypted": NotRequired[bool],
        "Throughput": NotRequired[int],
    },
)

EnableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "EnableMetricsCollectionQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Granularity": str,
        "Metrics": NotRequired[Sequence[str]],
    },
)

EnabledMetricTypeDef = TypedDict(
    "EnabledMetricTypeDef",
    {
        "Metric": NotRequired[str],
        "Granularity": NotRequired[str],
    },
)

EnterStandbyAnswerTypeDef = TypedDict(
    "EnterStandbyAnswerTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnterStandbyQueryRequestTypeDef = TypedDict(
    "EnterStandbyQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)

ExecutePolicyTypeRequestTypeDef = TypedDict(
    "ExecutePolicyTypeRequestTypeDef",
    {
        "PolicyName": str,
        "AutoScalingGroupName": NotRequired[str],
        "HonorCooldown": NotRequired[bool],
        "MetricValue": NotRequired[float],
        "BreachThreshold": NotRequired[float],
    },
)

ExitStandbyAnswerTypeDef = TypedDict(
    "ExitStandbyAnswerTypeDef",
    {
        "Activities": List["ActivityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExitStandbyQueryRequestTypeDef = TypedDict(
    "ExitStandbyQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)

FailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

GetPredictiveScalingForecastAnswerTypeDef = TypedDict(
    "GetPredictiveScalingForecastAnswerTypeDef",
    {
        "LoadForecast": List["LoadForecastTypeDef"],
        "CapacityForecast": "CapacityForecastTypeDef",
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPredictiveScalingForecastTypeRequestTypeDef = TypedDict(
    "GetPredictiveScalingForecastTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "HttpTokens": NotRequired[InstanceMetadataHttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
    },
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

InstanceRefreshLivePoolProgressTypeDef = TypedDict(
    "InstanceRefreshLivePoolProgressTypeDef",
    {
        "PercentageComplete": NotRequired[int],
        "InstancesToUpdate": NotRequired[int],
    },
)

InstanceRefreshProgressDetailsTypeDef = TypedDict(
    "InstanceRefreshProgressDetailsTypeDef",
    {
        "LivePoolProgress": NotRequired["InstanceRefreshLivePoolProgressTypeDef"],
        "WarmPoolProgress": NotRequired["InstanceRefreshWarmPoolProgressTypeDef"],
    },
)

InstanceRefreshTypeDef = TypedDict(
    "InstanceRefreshTypeDef",
    {
        "InstanceRefreshId": NotRequired[str],
        "AutoScalingGroupName": NotRequired[str],
        "Status": NotRequired[InstanceRefreshStatusType],
        "StatusReason": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "PercentageComplete": NotRequired[int],
        "InstancesToUpdate": NotRequired[int],
        "ProgressDetails": NotRequired["InstanceRefreshProgressDetailsTypeDef"],
        "Preferences": NotRequired["RefreshPreferencesTypeDef"],
        "DesiredConfiguration": NotRequired["DesiredConfigurationTypeDef"],
    },
)

InstanceRefreshWarmPoolProgressTypeDef = TypedDict(
    "InstanceRefreshWarmPoolProgressTypeDef",
    {
        "PercentageComplete": NotRequired[int],
        "InstancesToUpdate": NotRequired[int],
    },
)

InstanceRequirementsTypeDef = TypedDict(
    "InstanceRequirementsTypeDef",
    {
        "VCpuCount": "VCpuCountRequestTypeDef",
        "MemoryMiB": "MemoryMiBRequestTypeDef",
        "CpuManufacturers": NotRequired[Sequence[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired["MemoryGiBPerVCpuRequestTypeDef"],
        "ExcludedInstanceTypes": NotRequired[Sequence[str]],
        "InstanceGenerations": NotRequired[Sequence[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired["NetworkInterfaceCountRequestTypeDef"],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[Sequence[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired["TotalLocalStorageGBRequestTypeDef"],
        "BaselineEbsBandwidthMbps": NotRequired["BaselineEbsBandwidthMbpsRequestTypeDef"],
        "AcceleratorTypes": NotRequired[Sequence[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired["AcceleratorCountRequestTypeDef"],
        "AcceleratorManufacturers": NotRequired[Sequence[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[Sequence[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired["AcceleratorTotalMemoryMiBRequestTypeDef"],
    },
)

InstanceReusePolicyTypeDef = TypedDict(
    "InstanceReusePolicyTypeDef",
    {
        "ReuseOnScaleIn": NotRequired[bool],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "InstanceId": str,
        "AvailabilityZone": str,
        "LifecycleState": LifecycleStateType,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
        "InstanceType": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "WeightedCapacity": NotRequired[str],
    },
)

InstancesDistributionTypeDef = TypedDict(
    "InstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": NotRequired[str],
        "OnDemandBaseCapacity": NotRequired[int],
        "OnDemandPercentageAboveBaseCapacity": NotRequired[int],
        "SpotAllocationStrategy": NotRequired[str],
        "SpotInstancePools": NotRequired[int],
        "SpotMaxPrice": NotRequired[str],
    },
)

LaunchConfigurationNameTypeRequestTypeDef = TypedDict(
    "LaunchConfigurationNameTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
    },
)

LaunchConfigurationNamesTypeRequestTypeDef = TypedDict(
    "LaunchConfigurationNamesTypeRequestTypeDef",
    {
        "LaunchConfigurationNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "LaunchConfigurationName": str,
        "ImageId": str,
        "InstanceType": str,
        "CreatedTime": datetime,
        "LaunchConfigurationARN": NotRequired[str],
        "KeyName": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "ClassicLinkVPCId": NotRequired[str],
        "ClassicLinkVPCSecurityGroups": NotRequired[List[str]],
        "UserData": NotRequired[str],
        "KernelId": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List["BlockDeviceMappingTypeDef"]],
        "InstanceMonitoring": NotRequired["InstanceMonitoringTypeDef"],
        "SpotPrice": NotRequired[str],
        "IamInstanceProfile": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "PlacementTenancy": NotRequired[str],
        "MetadataOptions": NotRequired["InstanceMetadataOptionsTypeDef"],
    },
)

LaunchConfigurationsTypeTypeDef = TypedDict(
    "LaunchConfigurationsTypeTypeDef",
    {
        "LaunchConfigurations": List["LaunchConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[str],
        "LaunchTemplateSpecification": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "InstanceRequirements": NotRequired["InstanceRequirementsTypeDef"],
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "Overrides": NotRequired[Sequence["LaunchTemplateOverridesTypeDef"]],
    },
)

LifecycleHookSpecificationTypeDef = TypedDict(
    "LifecycleHookSpecificationTypeDef",
    {
        "LifecycleHookName": str,
        "LifecycleTransition": str,
        "NotificationMetadata": NotRequired[str],
        "HeartbeatTimeout": NotRequired[int],
        "DefaultResult": NotRequired[str],
        "NotificationTargetARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

LifecycleHookTypeDef = TypedDict(
    "LifecycleHookTypeDef",
    {
        "LifecycleHookName": NotRequired[str],
        "AutoScalingGroupName": NotRequired[str],
        "LifecycleTransition": NotRequired[str],
        "NotificationTargetARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "NotificationMetadata": NotRequired[str],
        "HeartbeatTimeout": NotRequired[int],
        "GlobalTimeout": NotRequired[int],
        "DefaultResult": NotRequired[str],
    },
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "State": NotRequired[str],
    },
)

LoadBalancerTargetGroupStateTypeDef = TypedDict(
    "LoadBalancerTargetGroupStateTypeDef",
    {
        "LoadBalancerTargetGroupARN": NotRequired[str],
        "State": NotRequired[str],
    },
)

LoadForecastTypeDef = TypedDict(
    "LoadForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
        "MetricSpecification": "PredictiveScalingMetricSpecificationTypeDef",
    },
)

MemoryGiBPerVCpuRequestTypeDef = TypedDict(
    "MemoryGiBPerVCpuRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)

MemoryMiBRequestTypeDef = TypedDict(
    "MemoryMiBRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)

MetricCollectionTypeTypeDef = TypedDict(
    "MetricCollectionTypeTypeDef",
    {
        "Metric": NotRequired[str],
    },
)

MetricDataQueryTypeDef = TypedDict(
    "MetricDataQueryTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "MetricStat": NotRequired["MetricStatTypeDef"],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MetricGranularityTypeTypeDef = TypedDict(
    "MetricGranularityTypeTypeDef",
    {
        "Granularity": NotRequired[str],
    },
)

MetricStatTypeDef = TypedDict(
    "MetricStatTypeDef",
    {
        "Metric": "MetricTypeDef",
        "Stat": str,
        "Unit": NotRequired[str],
    },
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": NotRequired[List["MetricDimensionTypeDef"]],
    },
)

MixedInstancesPolicyTypeDef = TypedDict(
    "MixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": NotRequired["LaunchTemplateTypeDef"],
        "InstancesDistribution": NotRequired["InstancesDistributionTypeDef"],
    },
)

NetworkInterfaceCountRequestTypeDef = TypedDict(
    "NetworkInterfaceCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "TopicARN": NotRequired[str],
        "NotificationType": NotRequired[str],
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

PoliciesTypeTypeDef = TypedDict(
    "PoliciesTypeTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyARNTypeTypeDef = TypedDict(
    "PolicyARNTypeTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List["AlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredefinedMetricSpecificationTypeDef = TypedDict(
    "PredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": MetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)

PredictiveScalingConfigurationTypeDef = TypedDict(
    "PredictiveScalingConfigurationTypeDef",
    {
        "MetricSpecifications": List["PredictiveScalingMetricSpecificationTypeDef"],
        "Mode": NotRequired[PredictiveScalingModeType],
        "SchedulingBufferTime": NotRequired[int],
        "MaxCapacityBreachBehavior": NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType],
        "MaxCapacityBuffer": NotRequired[int],
    },
)

PredictiveScalingCustomizedCapacityMetricTypeDef = TypedDict(
    "PredictiveScalingCustomizedCapacityMetricTypeDef",
    {
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
    },
)

PredictiveScalingCustomizedLoadMetricTypeDef = TypedDict(
    "PredictiveScalingCustomizedLoadMetricTypeDef",
    {
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
    },
)

PredictiveScalingCustomizedScalingMetricTypeDef = TypedDict(
    "PredictiveScalingCustomizedScalingMetricTypeDef",
    {
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
    },
)

PredictiveScalingMetricSpecificationTypeDef = TypedDict(
    "PredictiveScalingMetricSpecificationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricPairSpecification": NotRequired[
            "PredictiveScalingPredefinedMetricPairTypeDef"
        ],
        "PredefinedScalingMetricSpecification": NotRequired[
            "PredictiveScalingPredefinedScalingMetricTypeDef"
        ],
        "PredefinedLoadMetricSpecification": NotRequired[
            "PredictiveScalingPredefinedLoadMetricTypeDef"
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            "PredictiveScalingCustomizedScalingMetricTypeDef"
        ],
        "CustomizedLoadMetricSpecification": NotRequired[
            "PredictiveScalingCustomizedLoadMetricTypeDef"
        ],
        "CustomizedCapacityMetricSpecification": NotRequired[
            "PredictiveScalingCustomizedCapacityMetricTypeDef"
        ],
    },
)

PredictiveScalingPredefinedLoadMetricTypeDef = TypedDict(
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedLoadMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)

PredictiveScalingPredefinedMetricPairTypeDef = TypedDict(
    "PredictiveScalingPredefinedMetricPairTypeDef",
    {
        "PredefinedMetricType": PredefinedMetricPairTypeType,
        "ResourceLabel": NotRequired[str],
    },
)

PredictiveScalingPredefinedScalingMetricTypeDef = TypedDict(
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedScalingMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)

ProcessTypeTypeDef = TypedDict(
    "ProcessTypeTypeDef",
    {
        "ProcessName": str,
    },
)

ProcessesTypeTypeDef = TypedDict(
    "ProcessesTypeTypeDef",
    {
        "Processes": List["ProcessTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLifecycleHookTypeRequestTypeDef = TypedDict(
    "PutLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": NotRequired[str],
        "RoleARN": NotRequired[str],
        "NotificationTargetARN": NotRequired[str],
        "NotificationMetadata": NotRequired[str],
        "HeartbeatTimeout": NotRequired[int],
        "DefaultResult": NotRequired[str],
    },
)

PutNotificationConfigurationTypeRequestTypeDef = TypedDict(
    "PutNotificationConfigurationTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
        "NotificationTypes": Sequence[str],
    },
)

PutScalingPolicyTypeRequestTypeDef = TypedDict(
    "PutScalingPolicyTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyType": NotRequired[str],
        "AdjustmentType": NotRequired[str],
        "MinAdjustmentStep": NotRequired[int],
        "MinAdjustmentMagnitude": NotRequired[int],
        "ScalingAdjustment": NotRequired[int],
        "Cooldown": NotRequired[int],
        "MetricAggregationType": NotRequired[str],
        "StepAdjustments": NotRequired[Sequence["StepAdjustmentTypeDef"]],
        "EstimatedInstanceWarmup": NotRequired[int],
        "TargetTrackingConfiguration": NotRequired["TargetTrackingConfigurationTypeDef"],
        "Enabled": NotRequired[bool],
        "PredictiveScalingConfiguration": NotRequired["PredictiveScalingConfigurationTypeDef"],
    },
)

PutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "PutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "Time": NotRequired[Union[datetime, str]],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Recurrence": NotRequired[str],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "TimeZone": NotRequired[str],
    },
)

PutWarmPoolTypeRequestTypeDef = TypedDict(
    "PutWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MaxGroupPreparedCapacity": NotRequired[int],
        "MinSize": NotRequired[int],
        "PoolState": NotRequired[WarmPoolStateType],
        "InstanceReusePolicy": NotRequired["InstanceReusePolicyTypeDef"],
    },
)

RecordLifecycleActionHeartbeatTypeRequestTypeDef = TypedDict(
    "RecordLifecycleActionHeartbeatTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleActionToken": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)

RefreshPreferencesTypeDef = TypedDict(
    "RefreshPreferencesTypeDef",
    {
        "MinHealthyPercentage": NotRequired[int],
        "InstanceWarmup": NotRequired[int],
        "CheckpointPercentages": NotRequired[List[int]],
        "CheckpointDelay": NotRequired[int],
        "SkipMatching": NotRequired[bool],
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

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyARN": NotRequired[str],
        "PolicyType": NotRequired[str],
        "AdjustmentType": NotRequired[str],
        "MinAdjustmentStep": NotRequired[int],
        "MinAdjustmentMagnitude": NotRequired[int],
        "ScalingAdjustment": NotRequired[int],
        "Cooldown": NotRequired[int],
        "StepAdjustments": NotRequired[List["StepAdjustmentTypeDef"]],
        "MetricAggregationType": NotRequired[str],
        "EstimatedInstanceWarmup": NotRequired[int],
        "Alarms": NotRequired[List["AlarmTypeDef"]],
        "TargetTrackingConfiguration": NotRequired["TargetTrackingConfigurationTypeDef"],
        "Enabled": NotRequired[bool],
        "PredictiveScalingConfiguration": NotRequired["PredictiveScalingConfigurationTypeDef"],
    },
)

ScalingProcessQueryRequestTypeDef = TypedDict(
    "ScalingProcessQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScalingProcesses": NotRequired[Sequence[str]],
    },
)

ScheduledActionsTypeTypeDef = TypedDict(
    "ScheduledActionsTypeTypeDef",
    {
        "ScheduledUpdateGroupActions": List["ScheduledUpdateGroupActionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "ScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Recurrence": NotRequired[str],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "TimeZone": NotRequired[str],
    },
)

ScheduledUpdateGroupActionTypeDef = TypedDict(
    "ScheduledUpdateGroupActionTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "ScheduledActionName": NotRequired[str],
        "ScheduledActionARN": NotRequired[str],
        "Time": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Recurrence": NotRequired[str],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "TimeZone": NotRequired[str],
    },
)

SetDesiredCapacityTypeRequestTypeDef = TypedDict(
    "SetDesiredCapacityTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "DesiredCapacity": int,
        "HonorCooldown": NotRequired[bool],
    },
)

SetInstanceHealthQueryRequestTypeDef = TypedDict(
    "SetInstanceHealthQueryRequestTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "ShouldRespectGracePeriod": NotRequired[bool],
    },
)

SetInstanceProtectionQueryRequestTypeDef = TypedDict(
    "SetInstanceProtectionQueryRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "AutoScalingGroupName": str,
        "ProtectedFromScaleIn": bool,
    },
)

StartInstanceRefreshAnswerTypeDef = TypedDict(
    "StartInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInstanceRefreshTypeRequestTypeDef = TypedDict(
    "StartInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Strategy": NotRequired[Literal["Rolling"]],
        "DesiredConfiguration": NotRequired["DesiredConfigurationTypeDef"],
        "Preferences": NotRequired["RefreshPreferencesTypeDef"],
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

SuspendedProcessTypeDef = TypedDict(
    "SuspendedProcessTypeDef",
    {
        "ProcessName": NotRequired[str],
        "SuspensionReason": NotRequired[str],
    },
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "PropagateAtLaunch": NotRequired[bool],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Value": NotRequired[str],
        "PropagateAtLaunch": NotRequired[bool],
    },
)

TagsTypeTypeDef = TypedDict(
    "TagsTypeTypeDef",
    {
        "Tags": List["TagDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": NotRequired["PredefinedMetricSpecificationTypeDef"],
        "CustomizedMetricSpecification": NotRequired["CustomizedMetricSpecificationTypeDef"],
        "DisableScaleIn": NotRequired[bool],
    },
)

TerminateInstanceInAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "TerminateInstanceInAutoScalingGroupTypeRequestTypeDef",
    {
        "InstanceId": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)

TotalLocalStorageGBRequestTypeDef = TypedDict(
    "TotalLocalStorageGBRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)

UpdateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "UpdateAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "MixedInstancesPolicy": NotRequired["MixedInstancesPolicyTypeDef"],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "DefaultCooldown": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "PlacementGroup": NotRequired[str],
        "VPCZoneIdentifier": NotRequired[str],
        "TerminationPolicies": NotRequired[Sequence[str]],
        "NewInstancesProtectedFromScaleIn": NotRequired[bool],
        "ServiceLinkedRoleARN": NotRequired[str],
        "MaxInstanceLifetime": NotRequired[int],
        "CapacityRebalance": NotRequired[bool],
        "Context": NotRequired[str],
        "DesiredCapacityType": NotRequired[str],
    },
)

VCpuCountRequestTypeDef = TypedDict(
    "VCpuCountRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)

WarmPoolConfigurationTypeDef = TypedDict(
    "WarmPoolConfigurationTypeDef",
    {
        "MaxGroupPreparedCapacity": NotRequired[int],
        "MinSize": NotRequired[int],
        "PoolState": NotRequired[WarmPoolStateType],
        "Status": NotRequired[Literal["PendingDelete"]],
        "InstanceReusePolicy": NotRequired["InstanceReusePolicyTypeDef"],
    },
)
