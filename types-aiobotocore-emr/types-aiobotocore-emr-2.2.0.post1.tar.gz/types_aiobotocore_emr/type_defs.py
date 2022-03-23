"""
Type annotations for emr service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_emr/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_emr.type_defs import AddInstanceFleetInputRequestTypeDef

    data: AddInstanceFleetInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActionOnFailureType,
    AdjustmentTypeType,
    AuthModeType,
    AutoScalingPolicyStateChangeReasonCodeType,
    AutoScalingPolicyStateType,
    CancelStepsRequestStatusType,
    ClusterStateChangeReasonCodeType,
    ClusterStateType,
    ComparisonOperatorType,
    ComputeLimitsUnitTypeType,
    IdentityTypeType,
    InstanceCollectionTypeType,
    InstanceFleetStateChangeReasonCodeType,
    InstanceFleetStateType,
    InstanceFleetTypeType,
    InstanceGroupStateChangeReasonCodeType,
    InstanceGroupStateType,
    InstanceGroupTypeType,
    InstanceRoleTypeType,
    InstanceStateChangeReasonCodeType,
    InstanceStateType,
    JobFlowExecutionStateType,
    MarketTypeType,
    NotebookExecutionStatusType,
    OnDemandCapacityReservationPreferenceType,
    PlacementGroupStrategyType,
    RepoUpgradeOnBootType,
    ScaleDownBehaviorType,
    SpotProvisioningTimeoutActionType,
    StatisticType,
    StepCancellationOptionType,
    StepExecutionStateType,
    StepStateType,
    UnitType,
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
    "AddInstanceFleetInputRequestTypeDef",
    "AddInstanceFleetOutputTypeDef",
    "AddInstanceGroupsInputRequestTypeDef",
    "AddInstanceGroupsOutputTypeDef",
    "AddJobFlowStepsInputRequestTypeDef",
    "AddJobFlowStepsOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "ApplicationTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "AutoScalingPolicyTypeDef",
    "AutoTerminationPolicyTypeDef",
    "BlockPublicAccessConfigurationMetadataTypeDef",
    "BlockPublicAccessConfigurationTypeDef",
    "BootstrapActionConfigTypeDef",
    "BootstrapActionDetailTypeDef",
    "CancelStepsInfoTypeDef",
    "CancelStepsInputRequestTypeDef",
    "CancelStepsOutputTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "ConfigurationTypeDef",
    "CreateSecurityConfigurationInputRequestTypeDef",
    "CreateSecurityConfigurationOutputTypeDef",
    "CreateStudioInputRequestTypeDef",
    "CreateStudioOutputTypeDef",
    "CreateStudioSessionMappingInputRequestTypeDef",
    "DeleteSecurityConfigurationInputRequestTypeDef",
    "DeleteStudioInputRequestTypeDef",
    "DeleteStudioSessionMappingInputRequestTypeDef",
    "DescribeClusterInputRequestTypeDef",
    "DescribeClusterOutputTypeDef",
    "DescribeJobFlowsInputRequestTypeDef",
    "DescribeJobFlowsOutputTypeDef",
    "DescribeNotebookExecutionInputRequestTypeDef",
    "DescribeNotebookExecutionOutputTypeDef",
    "DescribeReleaseLabelInputRequestTypeDef",
    "DescribeReleaseLabelOutputTypeDef",
    "DescribeSecurityConfigurationInputRequestTypeDef",
    "DescribeSecurityConfigurationOutputTypeDef",
    "DescribeStepInputRequestTypeDef",
    "DescribeStepOutputTypeDef",
    "DescribeStudioInputRequestTypeDef",
    "DescribeStudioOutputTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "ExecutionEngineConfigTypeDef",
    "FailureDetailsTypeDef",
    "GetAutoTerminationPolicyInputRequestTypeDef",
    "GetAutoTerminationPolicyOutputTypeDef",
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    "GetManagedScalingPolicyInputRequestTypeDef",
    "GetManagedScalingPolicyOutputTypeDef",
    "GetStudioSessionMappingInputRequestTypeDef",
    "GetStudioSessionMappingOutputTypeDef",
    "HadoopJarStepConfigTypeDef",
    "HadoopStepConfigTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetTypeDef",
    "InstanceGroupConfigTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupModifyConfigTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupStatusTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceGroupTypeDef",
    "InstanceResizePolicyTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceStatusTypeDef",
    "InstanceTimelineTypeDef",
    "InstanceTypeConfigTypeDef",
    "InstanceTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "JobFlowDetailTypeDef",
    "JobFlowExecutionStatusDetailTypeDef",
    "JobFlowInstancesConfigTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "KerberosAttributesTypeDef",
    "KeyValueTypeDef",
    "ListBootstrapActionsInputRequestTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ListClustersInputRequestTypeDef",
    "ListClustersOutputTypeDef",
    "ListInstanceFleetsInputRequestTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "ListInstanceGroupsInputRequestTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "ListInstancesInputRequestTypeDef",
    "ListInstancesOutputTypeDef",
    "ListNotebookExecutionsInputRequestTypeDef",
    "ListNotebookExecutionsOutputTypeDef",
    "ListReleaseLabelsInputRequestTypeDef",
    "ListReleaseLabelsOutputTypeDef",
    "ListSecurityConfigurationsInputRequestTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "ListStepsInputRequestTypeDef",
    "ListStepsOutputTypeDef",
    "ListStudioSessionMappingsInputRequestTypeDef",
    "ListStudioSessionMappingsOutputTypeDef",
    "ListStudiosInputRequestTypeDef",
    "ListStudiosOutputTypeDef",
    "ManagedScalingPolicyTypeDef",
    "MetricDimensionTypeDef",
    "ModifyClusterInputRequestTypeDef",
    "ModifyClusterOutputTypeDef",
    "ModifyInstanceFleetInputRequestTypeDef",
    "ModifyInstanceGroupsInputRequestTypeDef",
    "NotebookExecutionSummaryTypeDef",
    "NotebookExecutionTypeDef",
    "OnDemandCapacityReservationOptionsTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementGroupConfigTypeDef",
    "PlacementTypeTypeDef",
    "PortRangeTypeDef",
    "PutAutoScalingPolicyInputRequestTypeDef",
    "PutAutoScalingPolicyOutputTypeDef",
    "PutAutoTerminationPolicyInputRequestTypeDef",
    "PutBlockPublicAccessConfigurationInputRequestTypeDef",
    "PutManagedScalingPolicyInputRequestTypeDef",
    "ReleaseLabelFilterTypeDef",
    "RemoveAutoScalingPolicyInputRequestTypeDef",
    "RemoveAutoTerminationPolicyInputRequestTypeDef",
    "RemoveManagedScalingPolicyInputRequestTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RunJobFlowInputRequestTypeDef",
    "RunJobFlowOutputTypeDef",
    "ScalingActionTypeDef",
    "ScalingConstraintsTypeDef",
    "ScalingRuleTypeDef",
    "ScalingTriggerTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "SessionMappingDetailTypeDef",
    "SessionMappingSummaryTypeDef",
    "SetTerminationProtectionInputRequestTypeDef",
    "SetVisibleToAllUsersInputRequestTypeDef",
    "ShrinkPolicyTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "SimplifiedApplicationTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "StartNotebookExecutionInputRequestTypeDef",
    "StartNotebookExecutionOutputTypeDef",
    "StepConfigTypeDef",
    "StepDetailTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "StepTimelineTypeDef",
    "StepTypeDef",
    "StopNotebookExecutionInputRequestTypeDef",
    "StudioSummaryTypeDef",
    "StudioTypeDef",
    "SupportedProductConfigTypeDef",
    "TagTypeDef",
    "TerminateJobFlowsInputRequestTypeDef",
    "UpdateStudioInputRequestTypeDef",
    "UpdateStudioSessionMappingInputRequestTypeDef",
    "VolumeSpecificationTypeDef",
    "WaiterConfigTypeDef",
)

AddInstanceFleetInputRequestTypeDef = TypedDict(
    "AddInstanceFleetInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": "InstanceFleetConfigTypeDef",
    },
)

AddInstanceFleetOutputTypeDef = TypedDict(
    "AddInstanceFleetOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceFleetId": str,
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddInstanceGroupsInputRequestTypeDef = TypedDict(
    "AddInstanceGroupsInputRequestTypeDef",
    {
        "InstanceGroups": Sequence["InstanceGroupConfigTypeDef"],
        "JobFlowId": str,
    },
)

AddInstanceGroupsOutputTypeDef = TypedDict(
    "AddInstanceGroupsOutputTypeDef",
    {
        "JobFlowId": str,
        "InstanceGroupIds": List[str],
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddJobFlowStepsInputRequestTypeDef = TypedDict(
    "AddJobFlowStepsInputRequestTypeDef",
    {
        "JobFlowId": str,
        "Steps": Sequence["StepConfigTypeDef"],
    },
)

AddJobFlowStepsOutputTypeDef = TypedDict(
    "AddJobFlowStepsOutputTypeDef",
    {
        "StepIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Args": NotRequired[List[str]],
        "AdditionalInfo": NotRequired[Dict[str, str]],
    },
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "Status": NotRequired["AutoScalingPolicyStatusTypeDef"],
        "Constraints": NotRequired["ScalingConstraintsTypeDef"],
        "Rules": NotRequired[List["ScalingRuleTypeDef"]],
    },
)

AutoScalingPolicyStateChangeReasonTypeDef = TypedDict(
    "AutoScalingPolicyStateChangeReasonTypeDef",
    {
        "Code": NotRequired[AutoScalingPolicyStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

AutoScalingPolicyStatusTypeDef = TypedDict(
    "AutoScalingPolicyStatusTypeDef",
    {
        "State": NotRequired[AutoScalingPolicyStateType],
        "StateChangeReason": NotRequired["AutoScalingPolicyStateChangeReasonTypeDef"],
    },
)

AutoScalingPolicyTypeDef = TypedDict(
    "AutoScalingPolicyTypeDef",
    {
        "Constraints": "ScalingConstraintsTypeDef",
        "Rules": Sequence["ScalingRuleTypeDef"],
    },
)

AutoTerminationPolicyTypeDef = TypedDict(
    "AutoTerminationPolicyTypeDef",
    {
        "IdleTimeout": NotRequired[int],
    },
)

BlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "BlockPublicAccessConfigurationMetadataTypeDef",
    {
        "CreationDateTime": datetime,
        "CreatedByArn": str,
    },
)

BlockPublicAccessConfigurationTypeDef = TypedDict(
    "BlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
        "PermittedPublicSecurityGroupRuleRanges": NotRequired[List["PortRangeTypeDef"]],
    },
)

BootstrapActionConfigTypeDef = TypedDict(
    "BootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": "ScriptBootstrapActionConfigTypeDef",
    },
)

BootstrapActionDetailTypeDef = TypedDict(
    "BootstrapActionDetailTypeDef",
    {
        "BootstrapActionConfig": NotRequired["BootstrapActionConfigTypeDef"],
    },
)

CancelStepsInfoTypeDef = TypedDict(
    "CancelStepsInfoTypeDef",
    {
        "StepId": NotRequired[str],
        "Status": NotRequired[CancelStepsRequestStatusType],
        "Reason": NotRequired[str],
    },
)

CancelStepsInputRequestTypeDef = TypedDict(
    "CancelStepsInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepIds": Sequence[str],
        "StepCancellationOption": NotRequired[StepCancellationOptionType],
    },
)

CancelStepsOutputTypeDef = TypedDict(
    "CancelStepsOutputTypeDef",
    {
        "CancelStepsInfoList": List["CancelStepsInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchAlarmDefinitionTypeDef = TypedDict(
    "CloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "MetricName": str,
        "Period": int,
        "Threshold": float,
        "EvaluationPeriods": NotRequired[int],
        "Namespace": NotRequired[str],
        "Statistic": NotRequired[StatisticType],
        "Unit": NotRequired[UnitType],
        "Dimensions": NotRequired[Sequence["MetricDimensionTypeDef"]],
    },
)

ClusterStateChangeReasonTypeDef = TypedDict(
    "ClusterStateChangeReasonTypeDef",
    {
        "Code": NotRequired[ClusterStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

ClusterStatusTypeDef = TypedDict(
    "ClusterStatusTypeDef",
    {
        "State": NotRequired[ClusterStateType],
        "StateChangeReason": NotRequired["ClusterStateChangeReasonTypeDef"],
        "Timeline": NotRequired["ClusterTimelineTypeDef"],
    },
)

ClusterSummaryTypeDef = TypedDict(
    "ClusterSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired["ClusterStatusTypeDef"],
        "NormalizedInstanceHours": NotRequired[int],
        "ClusterArn": NotRequired[str],
        "OutpostArn": NotRequired[str],
    },
)

ClusterTimelineTypeDef = TypedDict(
    "ClusterTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired["ClusterStatusTypeDef"],
        "Ec2InstanceAttributes": NotRequired["Ec2InstanceAttributesTypeDef"],
        "InstanceCollectionType": NotRequired[InstanceCollectionTypeType],
        "LogUri": NotRequired[str],
        "LogEncryptionKmsKeyId": NotRequired[str],
        "RequestedAmiVersion": NotRequired[str],
        "RunningAmiVersion": NotRequired[str],
        "ReleaseLabel": NotRequired[str],
        "AutoTerminate": NotRequired[bool],
        "TerminationProtected": NotRequired[bool],
        "VisibleToAllUsers": NotRequired[bool],
        "Applications": NotRequired[List["ApplicationTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "ServiceRole": NotRequired[str],
        "NormalizedInstanceHours": NotRequired[int],
        "MasterPublicDnsName": NotRequired[str],
        "Configurations": NotRequired[List["ConfigurationTypeDef"]],
        "SecurityConfiguration": NotRequired[str],
        "AutoScalingRole": NotRequired[str],
        "ScaleDownBehavior": NotRequired[ScaleDownBehaviorType],
        "CustomAmiId": NotRequired[str],
        "EbsRootVolumeSize": NotRequired[int],
        "RepoUpgradeOnBoot": NotRequired[RepoUpgradeOnBootType],
        "KerberosAttributes": NotRequired["KerberosAttributesTypeDef"],
        "ClusterArn": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "StepConcurrencyLevel": NotRequired[int],
        "PlacementGroups": NotRequired[List["PlacementGroupConfigTypeDef"]],
    },
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "Name": NotRequired[str],
        "ScriptPath": NotRequired[str],
        "Args": NotRequired[List[str]],
    },
)

ComputeLimitsTypeDef = TypedDict(
    "ComputeLimitsTypeDef",
    {
        "UnitType": ComputeLimitsUnitTypeType,
        "MinimumCapacityUnits": int,
        "MaximumCapacityUnits": int,
        "MaximumOnDemandCapacityUnits": NotRequired[int],
        "MaximumCoreCapacityUnits": NotRequired[int],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Classification": NotRequired[str],
        "Configurations": NotRequired[Sequence[Dict[str, Any]]],
        "Properties": NotRequired[Mapping[str, str]],
    },
)

CreateSecurityConfigurationInputRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
    },
)

CreateSecurityConfigurationOutputTypeDef = TypedDict(
    "CreateSecurityConfigurationOutputTypeDef",
    {
        "Name": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStudioInputRequestTypeDef = TypedDict(
    "CreateStudioInputRequestTypeDef",
    {
        "Name": str,
        "AuthMode": AuthModeType,
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "ServiceRole": str,
        "WorkspaceSecurityGroupId": str,
        "EngineSecurityGroupId": str,
        "DefaultS3Location": str,
        "Description": NotRequired[str],
        "UserRole": NotRequired[str],
        "IdpAuthUrl": NotRequired[str],
        "IdpRelayStateParameterName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateStudioOutputTypeDef = TypedDict(
    "CreateStudioOutputTypeDef",
    {
        "StudioId": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "CreateStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)

DeleteSecurityConfigurationInputRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteStudioInputRequestTypeDef = TypedDict(
    "DeleteStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)

DeleteStudioSessionMappingInputRequestTypeDef = TypedDict(
    "DeleteStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)

DescribeClusterInputRequestTypeDef = TypedDict(
    "DescribeClusterInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeClusterOutputTypeDef = TypedDict(
    "DescribeClusterOutputTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobFlowsInputRequestTypeDef = TypedDict(
    "DescribeJobFlowsInputRequestTypeDef",
    {
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "JobFlowIds": NotRequired[Sequence[str]],
        "JobFlowStates": NotRequired[Sequence[JobFlowExecutionStateType]],
    },
)

DescribeJobFlowsOutputTypeDef = TypedDict(
    "DescribeJobFlowsOutputTypeDef",
    {
        "JobFlows": List["JobFlowDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookExecutionInputRequestTypeDef = TypedDict(
    "DescribeNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionId": str,
    },
)

DescribeNotebookExecutionOutputTypeDef = TypedDict(
    "DescribeNotebookExecutionOutputTypeDef",
    {
        "NotebookExecution": "NotebookExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReleaseLabelInputRequestTypeDef = TypedDict(
    "DescribeReleaseLabelInputRequestTypeDef",
    {
        "ReleaseLabel": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeReleaseLabelOutputTypeDef = TypedDict(
    "DescribeReleaseLabelOutputTypeDef",
    {
        "ReleaseLabel": str,
        "Applications": List["SimplifiedApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityConfigurationInputRequestTypeDef = TypedDict(
    "DescribeSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeSecurityConfigurationOutputTypeDef = TypedDict(
    "DescribeSecurityConfigurationOutputTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStepInputRequestTypeDef = TypedDict(
    "DescribeStepInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
    },
)

DescribeStepOutputTypeDef = TypedDict(
    "DescribeStepOutputTypeDef",
    {
        "Step": "StepTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStudioInputRequestTypeDef = TypedDict(
    "DescribeStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)

DescribeStudioOutputTypeDef = TypedDict(
    "DescribeStudioOutputTypeDef",
    {
        "Studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EbsBlockDeviceConfigTypeDef = TypedDict(
    "EbsBlockDeviceConfigTypeDef",
    {
        "VolumeSpecification": "VolumeSpecificationTypeDef",
        "VolumesPerInstance": NotRequired[int],
    },
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "VolumeSpecification": NotRequired["VolumeSpecificationTypeDef"],
        "Device": NotRequired[str],
    },
)

EbsConfigurationTypeDef = TypedDict(
    "EbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": NotRequired[Sequence["EbsBlockDeviceConfigTypeDef"]],
        "EbsOptimized": NotRequired[bool],
    },
)

EbsVolumeTypeDef = TypedDict(
    "EbsVolumeTypeDef",
    {
        "Device": NotRequired[str],
        "VolumeId": NotRequired[str],
    },
)

Ec2InstanceAttributesTypeDef = TypedDict(
    "Ec2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": NotRequired[str],
        "Ec2SubnetId": NotRequired[str],
        "RequestedEc2SubnetIds": NotRequired[List[str]],
        "Ec2AvailabilityZone": NotRequired[str],
        "RequestedEc2AvailabilityZones": NotRequired[List[str]],
        "IamInstanceProfile": NotRequired[str],
        "EmrManagedMasterSecurityGroup": NotRequired[str],
        "EmrManagedSlaveSecurityGroup": NotRequired[str],
        "ServiceAccessSecurityGroup": NotRequired[str],
        "AdditionalMasterSecurityGroups": NotRequired[List[str]],
        "AdditionalSlaveSecurityGroups": NotRequired[List[str]],
    },
)

ExecutionEngineConfigTypeDef = TypedDict(
    "ExecutionEngineConfigTypeDef",
    {
        "Id": str,
        "Type": NotRequired[Literal["EMR"]],
        "MasterInstanceSecurityGroupId": NotRequired[str],
    },
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Reason": NotRequired[str],
        "Message": NotRequired[str],
        "LogFile": NotRequired[str],
    },
)

GetAutoTerminationPolicyInputRequestTypeDef = TypedDict(
    "GetAutoTerminationPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

GetAutoTerminationPolicyOutputTypeDef = TypedDict(
    "GetAutoTerminationPolicyOutputTypeDef",
    {
        "AutoTerminationPolicy": "AutoTerminationPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlockPublicAccessConfigurationOutputTypeDef = TypedDict(
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
        "BlockPublicAccessConfigurationMetadata": "BlockPublicAccessConfigurationMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "GetManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

GetManagedScalingPolicyOutputTypeDef = TypedDict(
    "GetManagedScalingPolicyOutputTypeDef",
    {
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioSessionMappingInputRequestTypeDef = TypedDict(
    "GetStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)

GetStudioSessionMappingOutputTypeDef = TypedDict(
    "GetStudioSessionMappingOutputTypeDef",
    {
        "SessionMapping": "SessionMappingDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HadoopJarStepConfigTypeDef = TypedDict(
    "HadoopJarStepConfigTypeDef",
    {
        "Jar": str,
        "Properties": NotRequired[Sequence["KeyValueTypeDef"]],
        "MainClass": NotRequired[str],
        "Args": NotRequired[Sequence[str]],
    },
)

HadoopStepConfigTypeDef = TypedDict(
    "HadoopStepConfigTypeDef",
    {
        "Jar": NotRequired[str],
        "Properties": NotRequired[Dict[str, str]],
        "MainClass": NotRequired[str],
        "Args": NotRequired[List[str]],
    },
)

InstanceFleetConfigTypeDef = TypedDict(
    "InstanceFleetConfigTypeDef",
    {
        "InstanceFleetType": InstanceFleetTypeType,
        "Name": NotRequired[str],
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
        "InstanceTypeConfigs": NotRequired[Sequence["InstanceTypeConfigTypeDef"]],
        "LaunchSpecifications": NotRequired["InstanceFleetProvisioningSpecificationsTypeDef"],
    },
)

InstanceFleetModifyConfigTypeDef = TypedDict(
    "InstanceFleetModifyConfigTypeDef",
    {
        "InstanceFleetId": str,
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
    },
)

InstanceFleetProvisioningSpecificationsTypeDef = TypedDict(
    "InstanceFleetProvisioningSpecificationsTypeDef",
    {
        "SpotSpecification": NotRequired["SpotProvisioningSpecificationTypeDef"],
        "OnDemandSpecification": NotRequired["OnDemandProvisioningSpecificationTypeDef"],
    },
)

InstanceFleetStateChangeReasonTypeDef = TypedDict(
    "InstanceFleetStateChangeReasonTypeDef",
    {
        "Code": NotRequired[InstanceFleetStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

InstanceFleetStatusTypeDef = TypedDict(
    "InstanceFleetStatusTypeDef",
    {
        "State": NotRequired[InstanceFleetStateType],
        "StateChangeReason": NotRequired["InstanceFleetStateChangeReasonTypeDef"],
        "Timeline": NotRequired["InstanceFleetTimelineTypeDef"],
    },
)

InstanceFleetTimelineTypeDef = TypedDict(
    "InstanceFleetTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)

InstanceFleetTypeDef = TypedDict(
    "InstanceFleetTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired["InstanceFleetStatusTypeDef"],
        "InstanceFleetType": NotRequired[InstanceFleetTypeType],
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
        "ProvisionedOnDemandCapacity": NotRequired[int],
        "ProvisionedSpotCapacity": NotRequired[int],
        "InstanceTypeSpecifications": NotRequired[List["InstanceTypeSpecificationTypeDef"]],
        "LaunchSpecifications": NotRequired["InstanceFleetProvisioningSpecificationsTypeDef"],
    },
)

InstanceGroupConfigTypeDef = TypedDict(
    "InstanceGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceCount": int,
        "Name": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "BidPrice": NotRequired[str],
        "Configurations": NotRequired[Sequence["ConfigurationTypeDef"]],
        "EbsConfiguration": NotRequired["EbsConfigurationTypeDef"],
        "AutoScalingPolicy": NotRequired["AutoScalingPolicyTypeDef"],
        "CustomAmiId": NotRequired[str],
    },
)

InstanceGroupDetailTypeDef = TypedDict(
    "InstanceGroupDetailTypeDef",
    {
        "Market": MarketTypeType,
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": InstanceGroupStateType,
        "CreationDateTime": datetime,
        "InstanceGroupId": NotRequired[str],
        "Name": NotRequired[str],
        "BidPrice": NotRequired[str],
        "LastStateChangeReason": NotRequired[str],
        "StartDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "CustomAmiId": NotRequired[str],
    },
)

InstanceGroupModifyConfigTypeDef = TypedDict(
    "InstanceGroupModifyConfigTypeDef",
    {
        "InstanceGroupId": str,
        "InstanceCount": NotRequired[int],
        "EC2InstanceIdsToTerminate": NotRequired[Sequence[str]],
        "ShrinkPolicy": NotRequired["ShrinkPolicyTypeDef"],
        "Configurations": NotRequired[Sequence["ConfigurationTypeDef"]],
    },
)

InstanceGroupStateChangeReasonTypeDef = TypedDict(
    "InstanceGroupStateChangeReasonTypeDef",
    {
        "Code": NotRequired[InstanceGroupStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

InstanceGroupStatusTypeDef = TypedDict(
    "InstanceGroupStatusTypeDef",
    {
        "State": NotRequired[InstanceGroupStateType],
        "StateChangeReason": NotRequired["InstanceGroupStateChangeReasonTypeDef"],
        "Timeline": NotRequired["InstanceGroupTimelineTypeDef"],
    },
)

InstanceGroupTimelineTypeDef = TypedDict(
    "InstanceGroupTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "InstanceGroupType": NotRequired[InstanceGroupTypeType],
        "BidPrice": NotRequired[str],
        "InstanceType": NotRequired[str],
        "RequestedInstanceCount": NotRequired[int],
        "RunningInstanceCount": NotRequired[int],
        "Status": NotRequired["InstanceGroupStatusTypeDef"],
        "Configurations": NotRequired[List["ConfigurationTypeDef"]],
        "ConfigurationsVersion": NotRequired[int],
        "LastSuccessfullyAppliedConfigurations": NotRequired[List["ConfigurationTypeDef"]],
        "LastSuccessfullyAppliedConfigurationsVersion": NotRequired[int],
        "EbsBlockDevices": NotRequired[List["EbsBlockDeviceTypeDef"]],
        "EbsOptimized": NotRequired[bool],
        "ShrinkPolicy": NotRequired["ShrinkPolicyTypeDef"],
        "AutoScalingPolicy": NotRequired["AutoScalingPolicyDescriptionTypeDef"],
        "CustomAmiId": NotRequired[str],
    },
)

InstanceResizePolicyTypeDef = TypedDict(
    "InstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": NotRequired[List[str]],
        "InstancesToProtect": NotRequired[List[str]],
        "InstanceTerminationTimeout": NotRequired[int],
    },
)

InstanceStateChangeReasonTypeDef = TypedDict(
    "InstanceStateChangeReasonTypeDef",
    {
        "Code": NotRequired[InstanceStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "State": NotRequired[InstanceStateType],
        "StateChangeReason": NotRequired["InstanceStateChangeReasonTypeDef"],
        "Timeline": NotRequired["InstanceTimelineTypeDef"],
    },
)

InstanceTimelineTypeDef = TypedDict(
    "InstanceTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)

InstanceTypeConfigTypeDef = TypedDict(
    "InstanceTypeConfigTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": NotRequired[int],
        "BidPrice": NotRequired[str],
        "BidPriceAsPercentageOfOnDemandPrice": NotRequired[float],
        "EbsConfiguration": NotRequired["EbsConfigurationTypeDef"],
        "Configurations": NotRequired[Sequence["ConfigurationTypeDef"]],
        "CustomAmiId": NotRequired[str],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": NotRequired[str],
        "Ec2InstanceId": NotRequired[str],
        "PublicDnsName": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "Status": NotRequired["InstanceStatusTypeDef"],
        "InstanceGroupId": NotRequired[str],
        "InstanceFleetId": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "InstanceType": NotRequired[str],
        "EbsVolumes": NotRequired[List["EbsVolumeTypeDef"]],
    },
)

InstanceTypeSpecificationTypeDef = TypedDict(
    "InstanceTypeSpecificationTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[int],
        "BidPrice": NotRequired[str],
        "BidPriceAsPercentageOfOnDemandPrice": NotRequired[float],
        "Configurations": NotRequired[List["ConfigurationTypeDef"]],
        "EbsBlockDevices": NotRequired[List["EbsBlockDeviceTypeDef"]],
        "EbsOptimized": NotRequired[bool],
        "CustomAmiId": NotRequired[str],
    },
)

JobFlowDetailTypeDef = TypedDict(
    "JobFlowDetailTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "ExecutionStatusDetail": "JobFlowExecutionStatusDetailTypeDef",
        "Instances": "JobFlowInstancesDetailTypeDef",
        "LogUri": NotRequired[str],
        "LogEncryptionKmsKeyId": NotRequired[str],
        "AmiVersion": NotRequired[str],
        "Steps": NotRequired[List["StepDetailTypeDef"]],
        "BootstrapActions": NotRequired[List["BootstrapActionDetailTypeDef"]],
        "SupportedProducts": NotRequired[List[str]],
        "VisibleToAllUsers": NotRequired[bool],
        "JobFlowRole": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "AutoScalingRole": NotRequired[str],
        "ScaleDownBehavior": NotRequired[ScaleDownBehaviorType],
    },
)

JobFlowExecutionStatusDetailTypeDef = TypedDict(
    "JobFlowExecutionStatusDetailTypeDef",
    {
        "State": JobFlowExecutionStateType,
        "CreationDateTime": datetime,
        "StartDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "LastStateChangeReason": NotRequired[str],
    },
)

JobFlowInstancesConfigTypeDef = TypedDict(
    "JobFlowInstancesConfigTypeDef",
    {
        "MasterInstanceType": NotRequired[str],
        "SlaveInstanceType": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceGroups": NotRequired[Sequence["InstanceGroupConfigTypeDef"]],
        "InstanceFleets": NotRequired[Sequence["InstanceFleetConfigTypeDef"]],
        "Ec2KeyName": NotRequired[str],
        "Placement": NotRequired["PlacementTypeTypeDef"],
        "KeepJobFlowAliveWhenNoSteps": NotRequired[bool],
        "TerminationProtected": NotRequired[bool],
        "HadoopVersion": NotRequired[str],
        "Ec2SubnetId": NotRequired[str],
        "Ec2SubnetIds": NotRequired[Sequence[str]],
        "EmrManagedMasterSecurityGroup": NotRequired[str],
        "EmrManagedSlaveSecurityGroup": NotRequired[str],
        "ServiceAccessSecurityGroup": NotRequired[str],
        "AdditionalMasterSecurityGroups": NotRequired[Sequence[str]],
        "AdditionalSlaveSecurityGroups": NotRequired[Sequence[str]],
    },
)

JobFlowInstancesDetailTypeDef = TypedDict(
    "JobFlowInstancesDetailTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "MasterPublicDnsName": NotRequired[str],
        "MasterInstanceId": NotRequired[str],
        "InstanceGroups": NotRequired[List["InstanceGroupDetailTypeDef"]],
        "NormalizedInstanceHours": NotRequired[int],
        "Ec2KeyName": NotRequired[str],
        "Ec2SubnetId": NotRequired[str],
        "Placement": NotRequired["PlacementTypeTypeDef"],
        "KeepJobFlowAliveWhenNoSteps": NotRequired[bool],
        "TerminationProtected": NotRequired[bool],
        "HadoopVersion": NotRequired[str],
    },
)

KerberosAttributesTypeDef = TypedDict(
    "KerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": NotRequired[str],
        "ADDomainJoinUser": NotRequired[str],
        "ADDomainJoinPassword": NotRequired[str],
    },
)

KeyValueTypeDef = TypedDict(
    "KeyValueTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

ListBootstrapActionsInputRequestTypeDef = TypedDict(
    "ListBootstrapActionsInputRequestTypeDef",
    {
        "ClusterId": str,
        "Marker": NotRequired[str],
    },
)

ListBootstrapActionsOutputTypeDef = TypedDict(
    "ListBootstrapActionsOutputTypeDef",
    {
        "BootstrapActions": List["CommandTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersInputRequestTypeDef = TypedDict(
    "ListClustersInputRequestTypeDef",
    {
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "ClusterStates": NotRequired[Sequence[ClusterStateType]],
        "Marker": NotRequired[str],
    },
)

ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {
        "Clusters": List["ClusterSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceFleetsInputRequestTypeDef = TypedDict(
    "ListInstanceFleetsInputRequestTypeDef",
    {
        "ClusterId": str,
        "Marker": NotRequired[str],
    },
)

ListInstanceFleetsOutputTypeDef = TypedDict(
    "ListInstanceFleetsOutputTypeDef",
    {
        "InstanceFleets": List["InstanceFleetTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceGroupsInputRequestTypeDef = TypedDict(
    "ListInstanceGroupsInputRequestTypeDef",
    {
        "ClusterId": str,
        "Marker": NotRequired[str],
    },
)

ListInstanceGroupsOutputTypeDef = TypedDict(
    "ListInstanceGroupsOutputTypeDef",
    {
        "InstanceGroups": List["InstanceGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesInputRequestTypeDef = TypedDict(
    "ListInstancesInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": NotRequired[str],
        "InstanceGroupTypes": NotRequired[Sequence[InstanceGroupTypeType]],
        "InstanceFleetId": NotRequired[str],
        "InstanceFleetType": NotRequired[InstanceFleetTypeType],
        "InstanceStates": NotRequired[Sequence[InstanceStateType]],
        "Marker": NotRequired[str],
    },
)

ListInstancesOutputTypeDef = TypedDict(
    "ListInstancesOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookExecutionsInputRequestTypeDef = TypedDict(
    "ListNotebookExecutionsInputRequestTypeDef",
    {
        "EditorId": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "From": NotRequired[Union[datetime, str]],
        "To": NotRequired[Union[datetime, str]],
        "Marker": NotRequired[str],
    },
)

ListNotebookExecutionsOutputTypeDef = TypedDict(
    "ListNotebookExecutionsOutputTypeDef",
    {
        "NotebookExecutions": List["NotebookExecutionSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReleaseLabelsInputRequestTypeDef = TypedDict(
    "ListReleaseLabelsInputRequestTypeDef",
    {
        "Filters": NotRequired["ReleaseLabelFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListReleaseLabelsOutputTypeDef = TypedDict(
    "ListReleaseLabelsOutputTypeDef",
    {
        "ReleaseLabels": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityConfigurationsInputRequestTypeDef = TypedDict(
    "ListSecurityConfigurationsInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
    },
)

ListSecurityConfigurationsOutputTypeDef = TypedDict(
    "ListSecurityConfigurationsOutputTypeDef",
    {
        "SecurityConfigurations": List["SecurityConfigurationSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStepsInputRequestTypeDef = TypedDict(
    "ListStepsInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepStates": NotRequired[Sequence[StepStateType]],
        "StepIds": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
    },
)

ListStepsOutputTypeDef = TypedDict(
    "ListStepsOutputTypeDef",
    {
        "Steps": List["StepSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioSessionMappingsInputRequestTypeDef = TypedDict(
    "ListStudioSessionMappingsInputRequestTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "Marker": NotRequired[str],
    },
)

ListStudioSessionMappingsOutputTypeDef = TypedDict(
    "ListStudioSessionMappingsOutputTypeDef",
    {
        "SessionMappings": List["SessionMappingSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudiosInputRequestTypeDef = TypedDict(
    "ListStudiosInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
    },
)

ListStudiosOutputTypeDef = TypedDict(
    "ListStudiosOutputTypeDef",
    {
        "Studios": List["StudioSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedScalingPolicyTypeDef = TypedDict(
    "ManagedScalingPolicyTypeDef",
    {
        "ComputeLimits": NotRequired["ComputeLimitsTypeDef"],
    },
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

ModifyClusterInputRequestTypeDef = TypedDict(
    "ModifyClusterInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepConcurrencyLevel": NotRequired[int],
    },
)

ModifyClusterOutputTypeDef = TypedDict(
    "ModifyClusterOutputTypeDef",
    {
        "StepConcurrencyLevel": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceFleetInputRequestTypeDef = TypedDict(
    "ModifyInstanceFleetInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": "InstanceFleetModifyConfigTypeDef",
    },
)

ModifyInstanceGroupsInputRequestTypeDef = TypedDict(
    "ModifyInstanceGroupsInputRequestTypeDef",
    {
        "ClusterId": NotRequired[str],
        "InstanceGroups": NotRequired[Sequence["InstanceGroupModifyConfigTypeDef"]],
    },
)

NotebookExecutionSummaryTypeDef = TypedDict(
    "NotebookExecutionSummaryTypeDef",
    {
        "NotebookExecutionId": NotRequired[str],
        "EditorId": NotRequired[str],
        "NotebookExecutionName": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

NotebookExecutionTypeDef = TypedDict(
    "NotebookExecutionTypeDef",
    {
        "NotebookExecutionId": NotRequired[str],
        "EditorId": NotRequired[str],
        "ExecutionEngine": NotRequired["ExecutionEngineConfigTypeDef"],
        "NotebookExecutionName": NotRequired[str],
        "NotebookParams": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Arn": NotRequired[str],
        "OutputNotebookURI": NotRequired[str],
        "LastStateChangeReason": NotRequired[str],
        "NotebookInstanceSecurityGroupId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

OnDemandCapacityReservationOptionsTypeDef = TypedDict(
    "OnDemandCapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": NotRequired[Literal["use-capacity-reservations-first"]],
        "CapacityReservationPreference": NotRequired[OnDemandCapacityReservationPreferenceType],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)

OnDemandProvisioningSpecificationTypeDef = TypedDict(
    "OnDemandProvisioningSpecificationTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price"],
        "CapacityReservationOptions": NotRequired["OnDemandCapacityReservationOptionsTypeDef"],
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

PlacementGroupConfigTypeDef = TypedDict(
    "PlacementGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
        "PlacementStrategy": NotRequired[PlacementGroupStrategyType],
    },
)

PlacementTypeTypeDef = TypedDict(
    "PlacementTypeTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "MinRange": int,
        "MaxRange": NotRequired[int],
    },
)

PutAutoScalingPolicyInputRequestTypeDef = TypedDict(
    "PutAutoScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyTypeDef",
    },
)

PutAutoScalingPolicyOutputTypeDef = TypedDict(
    "PutAutoScalingPolicyOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyDescriptionTypeDef",
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAutoTerminationPolicyInputRequestTypeDef = TypedDict(
    "PutAutoTerminationPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "AutoTerminationPolicy": NotRequired["AutoTerminationPolicyTypeDef"],
    },
)

PutBlockPublicAccessConfigurationInputRequestTypeDef = TypedDict(
    "PutBlockPublicAccessConfigurationInputRequestTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
    },
)

PutManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "PutManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
    },
)

ReleaseLabelFilterTypeDef = TypedDict(
    "ReleaseLabelFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Application": NotRequired[str],
    },
)

RemoveAutoScalingPolicyInputRequestTypeDef = TypedDict(
    "RemoveAutoScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
    },
)

RemoveAutoTerminationPolicyInputRequestTypeDef = TypedDict(
    "RemoveAutoTerminationPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

RemoveManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "RemoveManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
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

RunJobFlowInputRequestTypeDef = TypedDict(
    "RunJobFlowInputRequestTypeDef",
    {
        "Name": str,
        "Instances": "JobFlowInstancesConfigTypeDef",
        "LogUri": NotRequired[str],
        "LogEncryptionKmsKeyId": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "AmiVersion": NotRequired[str],
        "ReleaseLabel": NotRequired[str],
        "Steps": NotRequired[Sequence["StepConfigTypeDef"]],
        "BootstrapActions": NotRequired[Sequence["BootstrapActionConfigTypeDef"]],
        "SupportedProducts": NotRequired[Sequence[str]],
        "NewSupportedProducts": NotRequired[Sequence["SupportedProductConfigTypeDef"]],
        "Applications": NotRequired[Sequence["ApplicationTypeDef"]],
        "Configurations": NotRequired[Sequence["ConfigurationTypeDef"]],
        "VisibleToAllUsers": NotRequired[bool],
        "JobFlowRole": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "SecurityConfiguration": NotRequired[str],
        "AutoScalingRole": NotRequired[str],
        "ScaleDownBehavior": NotRequired[ScaleDownBehaviorType],
        "CustomAmiId": NotRequired[str],
        "EbsRootVolumeSize": NotRequired[int],
        "RepoUpgradeOnBoot": NotRequired[RepoUpgradeOnBootType],
        "KerberosAttributes": NotRequired["KerberosAttributesTypeDef"],
        "StepConcurrencyLevel": NotRequired[int],
        "ManagedScalingPolicy": NotRequired["ManagedScalingPolicyTypeDef"],
        "PlacementGroupConfigs": NotRequired[Sequence["PlacementGroupConfigTypeDef"]],
        "AutoTerminationPolicy": NotRequired["AutoTerminationPolicyTypeDef"],
    },
)

RunJobFlowOutputTypeDef = TypedDict(
    "RunJobFlowOutputTypeDef",
    {
        "JobFlowId": str,
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScalingActionTypeDef = TypedDict(
    "ScalingActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": "SimpleScalingPolicyConfigurationTypeDef",
        "Market": NotRequired[MarketTypeType],
    },
)

ScalingConstraintsTypeDef = TypedDict(
    "ScalingConstraintsTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
    },
)

ScalingRuleTypeDef = TypedDict(
    "ScalingRuleTypeDef",
    {
        "Name": str,
        "Action": "ScalingActionTypeDef",
        "Trigger": "ScalingTriggerTypeDef",
        "Description": NotRequired[str],
    },
)

ScalingTriggerTypeDef = TypedDict(
    "ScalingTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": "CloudWatchAlarmDefinitionTypeDef",
    },
)

ScriptBootstrapActionConfigTypeDef = TypedDict(
    "ScriptBootstrapActionConfigTypeDef",
    {
        "Path": str,
        "Args": NotRequired[List[str]],
    },
)

SecurityConfigurationSummaryTypeDef = TypedDict(
    "SecurityConfigurationSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "CreationDateTime": NotRequired[datetime],
    },
)

SessionMappingDetailTypeDef = TypedDict(
    "SessionMappingDetailTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "SessionPolicyArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

SessionMappingSummaryTypeDef = TypedDict(
    "SessionMappingSummaryTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "SessionPolicyArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)

SetTerminationProtectionInputRequestTypeDef = TypedDict(
    "SetTerminationProtectionInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
        "TerminationProtected": bool,
    },
)

SetVisibleToAllUsersInputRequestTypeDef = TypedDict(
    "SetVisibleToAllUsersInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
        "VisibleToAllUsers": bool,
    },
)

ShrinkPolicyTypeDef = TypedDict(
    "ShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": NotRequired[int],
        "InstanceResizePolicy": NotRequired["InstanceResizePolicyTypeDef"],
    },
)

SimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "SimpleScalingPolicyConfigurationTypeDef",
    {
        "ScalingAdjustment": int,
        "AdjustmentType": NotRequired[AdjustmentTypeType],
        "CoolDown": NotRequired[int],
    },
)

SimplifiedApplicationTypeDef = TypedDict(
    "SimplifiedApplicationTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

SpotProvisioningSpecificationTypeDef = TypedDict(
    "SpotProvisioningSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": SpotProvisioningTimeoutActionType,
        "BlockDurationMinutes": NotRequired[int],
        "AllocationStrategy": NotRequired[Literal["capacity-optimized"]],
    },
)

StartNotebookExecutionInputRequestTypeDef = TypedDict(
    "StartNotebookExecutionInputRequestTypeDef",
    {
        "EditorId": str,
        "RelativePath": str,
        "ExecutionEngine": "ExecutionEngineConfigTypeDef",
        "ServiceRole": str,
        "NotebookExecutionName": NotRequired[str],
        "NotebookParams": NotRequired[str],
        "NotebookInstanceSecurityGroupId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartNotebookExecutionOutputTypeDef = TypedDict(
    "StartNotebookExecutionOutputTypeDef",
    {
        "NotebookExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StepConfigTypeDef = TypedDict(
    "StepConfigTypeDef",
    {
        "Name": str,
        "HadoopJarStep": "HadoopJarStepConfigTypeDef",
        "ActionOnFailure": NotRequired[ActionOnFailureType],
    },
)

StepDetailTypeDef = TypedDict(
    "StepDetailTypeDef",
    {
        "StepConfig": "StepConfigTypeDef",
        "ExecutionStatusDetail": "StepExecutionStatusDetailTypeDef",
    },
)

StepExecutionStatusDetailTypeDef = TypedDict(
    "StepExecutionStatusDetailTypeDef",
    {
        "State": StepExecutionStateType,
        "CreationDateTime": datetime,
        "StartDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "LastStateChangeReason": NotRequired[str],
    },
)

StepStateChangeReasonTypeDef = TypedDict(
    "StepStateChangeReasonTypeDef",
    {
        "Code": NotRequired[Literal["NONE"]],
        "Message": NotRequired[str],
    },
)

StepStatusTypeDef = TypedDict(
    "StepStatusTypeDef",
    {
        "State": NotRequired[StepStateType],
        "StateChangeReason": NotRequired["StepStateChangeReasonTypeDef"],
        "FailureDetails": NotRequired["FailureDetailsTypeDef"],
        "Timeline": NotRequired["StepTimelineTypeDef"],
    },
)

StepSummaryTypeDef = TypedDict(
    "StepSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Config": NotRequired["HadoopStepConfigTypeDef"],
        "ActionOnFailure": NotRequired[ActionOnFailureType],
        "Status": NotRequired["StepStatusTypeDef"],
    },
)

StepTimelineTypeDef = TypedDict(
    "StepTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "StartDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Config": NotRequired["HadoopStepConfigTypeDef"],
        "ActionOnFailure": NotRequired[ActionOnFailureType],
        "Status": NotRequired["StepStatusTypeDef"],
    },
)

StopNotebookExecutionInputRequestTypeDef = TypedDict(
    "StopNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionId": str,
    },
)

StudioSummaryTypeDef = TypedDict(
    "StudioSummaryTypeDef",
    {
        "StudioId": NotRequired[str],
        "Name": NotRequired[str],
        "VpcId": NotRequired[str],
        "Description": NotRequired[str],
        "Url": NotRequired[str],
        "AuthMode": NotRequired[AuthModeType],
        "CreationTime": NotRequired[datetime],
    },
)

StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "StudioId": NotRequired[str],
        "StudioArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "AuthMode": NotRequired[AuthModeType],
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "ServiceRole": NotRequired[str],
        "UserRole": NotRequired[str],
        "WorkspaceSecurityGroupId": NotRequired[str],
        "EngineSecurityGroupId": NotRequired[str],
        "Url": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "DefaultS3Location": NotRequired[str],
        "IdpAuthUrl": NotRequired[str],
        "IdpRelayStateParameterName": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

SupportedProductConfigTypeDef = TypedDict(
    "SupportedProductConfigTypeDef",
    {
        "Name": NotRequired[str],
        "Args": NotRequired[Sequence[str]],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TerminateJobFlowsInputRequestTypeDef = TypedDict(
    "TerminateJobFlowsInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
    },
)

UpdateStudioInputRequestTypeDef = TypedDict(
    "UpdateStudioInputRequestTypeDef",
    {
        "StudioId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DefaultS3Location": NotRequired[str],
    },
)

UpdateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "UpdateStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)

VolumeSpecificationTypeDef = TypedDict(
    "VolumeSpecificationTypeDef",
    {
        "VolumeType": str,
        "SizeInGB": int,
        "Iops": NotRequired[int],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
