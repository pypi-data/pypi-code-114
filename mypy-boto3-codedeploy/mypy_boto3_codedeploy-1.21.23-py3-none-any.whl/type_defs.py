"""
Type annotations for codedeploy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import AddTagsToOnPremisesInstancesInputRequestTypeDef

    data: AddTagsToOnPremisesInstancesInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ApplicationRevisionSortByType,
    AutoRollbackEventType,
    BundleTypeType,
    ComputePlatformType,
    DeploymentCreatorType,
    DeploymentOptionType,
    DeploymentReadyActionType,
    DeploymentStatusType,
    DeploymentTargetTypeType,
    DeploymentTypeType,
    DeploymentWaitTypeType,
    EC2TagFilterTypeType,
    ErrorCodeType,
    FileExistsBehaviorType,
    GreenFleetProvisioningActionType,
    InstanceActionType,
    InstanceStatusType,
    InstanceTypeType,
    LifecycleErrorCodeType,
    LifecycleEventStatusType,
    ListStateFilterActionType,
    MinimumHealthyHostsTypeType,
    OutdatedInstancesStrategyType,
    RegistrationStatusType,
    RevisionLocationTypeType,
    SortOrderType,
    StopStatusType,
    TagFilterTypeType,
    TargetFilterNameType,
    TargetLabelType,
    TargetStatusType,
    TrafficRoutingTypeType,
    TriggerEventTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsToOnPremisesInstancesInputRequestTypeDef",
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BatchGetApplicationRevisionsInputRequestTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsInputRequestTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsInputRequestTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesInputRequestTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsInputRequestTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsInputRequestTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesInputRequestTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "ContinueDeploymentInputRequestTypeDef",
    "CreateApplicationInputRequestTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigInputRequestTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupInputRequestTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentInputRequestTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteApplicationInputRequestTypeDef",
    "DeleteDeploymentConfigInputRequestTypeDef",
    "DeleteDeploymentGroupInputRequestTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenInputRequestTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "DeleteResourcesByExternalIdInputRequestTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DeregisterOnPremisesInstanceInputRequestTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GetApplicationInputRequestTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionInputRequestTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigInputRequestTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupInputRequestTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInputRequestTypeDef",
    "GetDeploymentInstanceInputRequestTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetInputRequestTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceInputRequestTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "ListApplicationRevisionsInputRequestTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsInputRequestTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsInputRequestTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsInputRequestTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesInputRequestTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsInputRequestTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsInputRequestTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesInputRequestTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesInputRequestTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusInputRequestTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "RawStringTypeDef",
    "RegisterApplicationRevisionInputRequestTypeDef",
    "RegisterOnPremisesInstanceInputRequestTypeDef",
    "RelatedDeploymentsTypeDef",
    "RemoveTagsFromOnPremisesInstancesInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "SkipWaitTimeForInstanceTerminationInputRequestTypeDef",
    "StopDeploymentInputRequestTypeDef",
    "StopDeploymentOutputTypeDef",
    "TagFilterTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TimeRangeTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateApplicationInputRequestTypeDef",
    "UpdateDeploymentGroupInputRequestTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "AddTagsToOnPremisesInstancesInputRequestTypeDef",
    {
        "tags": Sequence["TagTypeDef"],
        "instanceNames": Sequence[str],
    },
)

AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
        "ignorePollAlarmFailure": NotRequired[bool],
        "alarms": NotRequired[List["AlarmTypeDef"]],
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": NotRequired[str],
    },
)

AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef",
    {
        "content": NotRequired[str],
        "sha256": NotRequired[str],
    },
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "applicationId": NotRequired[str],
        "applicationName": NotRequired[str],
        "createTime": NotRequired[datetime],
        "linkedToGitHub": NotRequired[bool],
        "gitHubAccountName": NotRequired[str],
        "computePlatform": NotRequired[ComputePlatformType],
    },
)

AutoRollbackConfigurationTypeDef = TypedDict(
    "AutoRollbackConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
        "events": NotRequired[List[AutoRollbackEventType]],
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": NotRequired[str],
        "hook": NotRequired[str],
    },
)

BatchGetApplicationRevisionsInputRequestTypeDef = TypedDict(
    "BatchGetApplicationRevisionsInputRequestTypeDef",
    {
        "applicationName": str,
        "revisions": Sequence["RevisionLocationTypeDef"],
    },
)

BatchGetApplicationRevisionsOutputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List["RevisionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetApplicationsInputRequestTypeDef = TypedDict(
    "BatchGetApplicationsInputRequestTypeDef",
    {
        "applicationNames": Sequence[str],
    },
)

BatchGetApplicationsOutputTypeDef = TypedDict(
    "BatchGetApplicationsOutputTypeDef",
    {
        "applicationsInfo": List["ApplicationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentGroupsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentGroupsInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupNames": Sequence[str],
    },
)

BatchGetDeploymentGroupsOutputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputTypeDef",
    {
        "deploymentGroupsInfo": List["DeploymentGroupInfoTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentInstancesInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentInstancesInputRequestTypeDef",
    {
        "deploymentId": str,
        "instanceIds": Sequence[str],
    },
)

BatchGetDeploymentInstancesOutputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputTypeDef",
    {
        "instancesSummary": List["InstanceSummaryTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentTargetsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentTargetsInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetIds": NotRequired[Sequence[str]],
    },
)

BatchGetDeploymentTargetsOutputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputTypeDef",
    {
        "deploymentTargets": List["DeploymentTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDeploymentsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentsInputRequestTypeDef",
    {
        "deploymentIds": Sequence[str],
    },
)

BatchGetDeploymentsOutputTypeDef = TypedDict(
    "BatchGetDeploymentsOutputTypeDef",
    {
        "deploymentsInfo": List["DeploymentInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesInputRequestTypeDef",
    {
        "instanceNames": Sequence[str],
    },
)

BatchGetOnPremisesInstancesOutputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputTypeDef",
    {
        "instanceInfos": List["InstanceInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "BlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": NotRequired[
            "BlueInstanceTerminationOptionTypeDef"
        ],
        "deploymentReadyOption": NotRequired["DeploymentReadyOptionTypeDef"],
        "greenFleetProvisioningOption": NotRequired["GreenFleetProvisioningOptionTypeDef"],
    },
)

BlueInstanceTerminationOptionTypeDef = TypedDict(
    "BlueInstanceTerminationOptionTypeDef",
    {
        "action": NotRequired[InstanceActionType],
        "terminationWaitTimeInMinutes": NotRequired[int],
    },
)

CloudFormationTargetTypeDef = TypedDict(
    "CloudFormationTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List["LifecycleEventTypeDef"]],
        "status": NotRequired[TargetStatusType],
        "resourceType": NotRequired[str],
        "targetVersionWeight": NotRequired[float],
    },
)

ContinueDeploymentInputRequestTypeDef = TypedDict(
    "ContinueDeploymentInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "deploymentWaitType": NotRequired[DeploymentWaitTypeType],
    },
)

CreateApplicationInputRequestTypeDef = TypedDict(
    "CreateApplicationInputRequestTypeDef",
    {
        "applicationName": str,
        "computePlatform": NotRequired[ComputePlatformType],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateApplicationOutputTypeDef = TypedDict(
    "CreateApplicationOutputTypeDef",
    {
        "applicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentConfigInputRequestTypeDef = TypedDict(
    "CreateDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
        "minimumHealthyHosts": NotRequired["MinimumHealthyHostsTypeDef"],
        "trafficRoutingConfig": NotRequired["TrafficRoutingConfigTypeDef"],
        "computePlatform": NotRequired[ComputePlatformType],
    },
)

CreateDeploymentConfigOutputTypeDef = TypedDict(
    "CreateDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentGroupInputRequestTypeDef = TypedDict(
    "CreateDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "serviceRoleArn": str,
        "deploymentConfigName": NotRequired[str],
        "ec2TagFilters": NotRequired[Sequence["EC2TagFilterTypeDef"]],
        "onPremisesInstanceTagFilters": NotRequired[Sequence["TagFilterTypeDef"]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "triggerConfigurations": NotRequired[Sequence["TriggerConfigTypeDef"]],
        "alarmConfiguration": NotRequired["AlarmConfigurationTypeDef"],
        "autoRollbackConfiguration": NotRequired["AutoRollbackConfigurationTypeDef"],
        "outdatedInstancesStrategy": NotRequired[OutdatedInstancesStrategyType],
        "deploymentStyle": NotRequired["DeploymentStyleTypeDef"],
        "blueGreenDeploymentConfiguration": NotRequired["BlueGreenDeploymentConfigurationTypeDef"],
        "loadBalancerInfo": NotRequired["LoadBalancerInfoTypeDef"],
        "ec2TagSet": NotRequired["EC2TagSetTypeDef"],
        "ecsServices": NotRequired[Sequence["ECSServiceTypeDef"]],
        "onPremisesTagSet": NotRequired["OnPremisesTagSetTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDeploymentGroupOutputTypeDef = TypedDict(
    "CreateDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentInputRequestTypeDef = TypedDict(
    "CreateDeploymentInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": NotRequired[str],
        "revision": NotRequired["RevisionLocationTypeDef"],
        "deploymentConfigName": NotRequired[str],
        "description": NotRequired[str],
        "ignoreApplicationStopFailures": NotRequired[bool],
        "targetInstances": NotRequired["TargetInstancesTypeDef"],
        "autoRollbackConfiguration": NotRequired["AutoRollbackConfigurationTypeDef"],
        "updateOutdatedInstancesOnly": NotRequired[bool],
        "fileExistsBehavior": NotRequired[FileExistsBehaviorType],
    },
)

CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationInputRequestTypeDef = TypedDict(
    "DeleteApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)

DeleteDeploymentConfigInputRequestTypeDef = TypedDict(
    "DeleteDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)

DeleteDeploymentGroupInputRequestTypeDef = TypedDict(
    "DeleteDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)

DeleteDeploymentGroupOutputTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGitHubAccountTokenInputRequestTypeDef = TypedDict(
    "DeleteGitHubAccountTokenInputRequestTypeDef",
    {
        "tokenName": NotRequired[str],
    },
)

DeleteGitHubAccountTokenOutputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputTypeDef",
    {
        "tokenName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcesByExternalIdInputRequestTypeDef = TypedDict(
    "DeleteResourcesByExternalIdInputRequestTypeDef",
    {
        "externalId": NotRequired[str],
    },
)

DeploymentConfigInfoTypeDef = TypedDict(
    "DeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "minimumHealthyHosts": NotRequired["MinimumHealthyHostsTypeDef"],
        "createTime": NotRequired[datetime],
        "computePlatform": NotRequired[ComputePlatformType],
        "trafficRoutingConfig": NotRequired["TrafficRoutingConfigTypeDef"],
    },
)

DeploymentGroupInfoTypeDef = TypedDict(
    "DeploymentGroupInfoTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupId": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "ec2TagFilters": NotRequired[List["EC2TagFilterTypeDef"]],
        "onPremisesInstanceTagFilters": NotRequired[List["TagFilterTypeDef"]],
        "autoScalingGroups": NotRequired[List["AutoScalingGroupTypeDef"]],
        "serviceRoleArn": NotRequired[str],
        "targetRevision": NotRequired["RevisionLocationTypeDef"],
        "triggerConfigurations": NotRequired[List["TriggerConfigTypeDef"]],
        "alarmConfiguration": NotRequired["AlarmConfigurationTypeDef"],
        "autoRollbackConfiguration": NotRequired["AutoRollbackConfigurationTypeDef"],
        "deploymentStyle": NotRequired["DeploymentStyleTypeDef"],
        "outdatedInstancesStrategy": NotRequired[OutdatedInstancesStrategyType],
        "blueGreenDeploymentConfiguration": NotRequired["BlueGreenDeploymentConfigurationTypeDef"],
        "loadBalancerInfo": NotRequired["LoadBalancerInfoTypeDef"],
        "lastSuccessfulDeployment": NotRequired["LastDeploymentInfoTypeDef"],
        "lastAttemptedDeployment": NotRequired["LastDeploymentInfoTypeDef"],
        "ec2TagSet": NotRequired["EC2TagSetTypeDef"],
        "onPremisesTagSet": NotRequired["OnPremisesTagSetTypeDef"],
        "computePlatform": NotRequired[ComputePlatformType],
        "ecsServices": NotRequired[List["ECSServiceTypeDef"]],
    },
)

DeploymentInfoTypeDef = TypedDict(
    "DeploymentInfoTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "deploymentId": NotRequired[str],
        "previousRevision": NotRequired["RevisionLocationTypeDef"],
        "revision": NotRequired["RevisionLocationTypeDef"],
        "status": NotRequired[DeploymentStatusType],
        "errorInformation": NotRequired["ErrorInformationTypeDef"],
        "createTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "completeTime": NotRequired[datetime],
        "deploymentOverview": NotRequired["DeploymentOverviewTypeDef"],
        "description": NotRequired[str],
        "creator": NotRequired[DeploymentCreatorType],
        "ignoreApplicationStopFailures": NotRequired[bool],
        "autoRollbackConfiguration": NotRequired["AutoRollbackConfigurationTypeDef"],
        "updateOutdatedInstancesOnly": NotRequired[bool],
        "rollbackInfo": NotRequired["RollbackInfoTypeDef"],
        "deploymentStyle": NotRequired["DeploymentStyleTypeDef"],
        "targetInstances": NotRequired["TargetInstancesTypeDef"],
        "instanceTerminationWaitTimeStarted": NotRequired[bool],
        "blueGreenDeploymentConfiguration": NotRequired["BlueGreenDeploymentConfigurationTypeDef"],
        "loadBalancerInfo": NotRequired["LoadBalancerInfoTypeDef"],
        "additionalDeploymentStatusInfo": NotRequired[str],
        "fileExistsBehavior": NotRequired[FileExistsBehaviorType],
        "deploymentStatusMessages": NotRequired[List[str]],
        "computePlatform": NotRequired[ComputePlatformType],
        "externalId": NotRequired[str],
        "relatedDeployments": NotRequired["RelatedDeploymentsTypeDef"],
    },
)

DeploymentOverviewTypeDef = TypedDict(
    "DeploymentOverviewTypeDef",
    {
        "Pending": NotRequired[int],
        "InProgress": NotRequired[int],
        "Succeeded": NotRequired[int],
        "Failed": NotRequired[int],
        "Skipped": NotRequired[int],
        "Ready": NotRequired[int],
    },
)

DeploymentReadyOptionTypeDef = TypedDict(
    "DeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": NotRequired[DeploymentReadyActionType],
        "waitTimeInMinutes": NotRequired[int],
    },
)

DeploymentStyleTypeDef = TypedDict(
    "DeploymentStyleTypeDef",
    {
        "deploymentType": NotRequired[DeploymentTypeType],
        "deploymentOption": NotRequired[DeploymentOptionType],
    },
)

DeploymentTargetTypeDef = TypedDict(
    "DeploymentTargetTypeDef",
    {
        "deploymentTargetType": NotRequired[DeploymentTargetTypeType],
        "instanceTarget": NotRequired["InstanceTargetTypeDef"],
        "lambdaTarget": NotRequired["LambdaTargetTypeDef"],
        "ecsTarget": NotRequired["ECSTargetTypeDef"],
        "cloudFormationTarget": NotRequired["CloudFormationTargetTypeDef"],
    },
)

DeregisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "DeregisterOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)

DiagnosticsTypeDef = TypedDict(
    "DiagnosticsTypeDef",
    {
        "errorCode": NotRequired[LifecycleErrorCodeType],
        "scriptName": NotRequired[str],
        "message": NotRequired[str],
        "logTail": NotRequired[str],
    },
)

EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Type": NotRequired[EC2TagFilterTypeType],
    },
)

EC2TagSetTypeDef = TypedDict(
    "EC2TagSetTypeDef",
    {
        "ec2TagSetList": NotRequired[List[List["EC2TagFilterTypeDef"]]],
    },
)

ECSServiceTypeDef = TypedDict(
    "ECSServiceTypeDef",
    {
        "serviceName": NotRequired[str],
        "clusterName": NotRequired[str],
    },
)

ECSTargetTypeDef = TypedDict(
    "ECSTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "targetArn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List["LifecycleEventTypeDef"]],
        "status": NotRequired[TargetStatusType],
        "taskSetsInfo": NotRequired[List["ECSTaskSetTypeDef"]],
    },
)

ECSTaskSetTypeDef = TypedDict(
    "ECSTaskSetTypeDef",
    {
        "identifer": NotRequired[str],
        "desiredCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "status": NotRequired[str],
        "trafficWeight": NotRequired[float],
        "targetGroup": NotRequired["TargetGroupInfoTypeDef"],
        "taskSetLabel": NotRequired[TargetLabelType],
    },
)

ELBInfoTypeDef = TypedDict(
    "ELBInfoTypeDef",
    {
        "name": NotRequired[str],
    },
)

ErrorInformationTypeDef = TypedDict(
    "ErrorInformationTypeDef",
    {
        "code": NotRequired[ErrorCodeType],
        "message": NotRequired[str],
    },
)

GenericRevisionInfoTypeDef = TypedDict(
    "GenericRevisionInfoTypeDef",
    {
        "description": NotRequired[str],
        "deploymentGroups": NotRequired[List[str]],
        "firstUsedTime": NotRequired[datetime],
        "lastUsedTime": NotRequired[datetime],
        "registerTime": NotRequired[datetime],
    },
)

GetApplicationInputRequestTypeDef = TypedDict(
    "GetApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "application": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRevisionInputRequestTypeDef = TypedDict(
    "GetApplicationRevisionInputRequestTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
    },
)

GetApplicationRevisionOutputTypeDef = TypedDict(
    "GetApplicationRevisionOutputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "revisionInfo": "GenericRevisionInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentConfigInputRequestTypeDef = TypedDict(
    "GetDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)

GetDeploymentConfigOutputTypeDef = TypedDict(
    "GetDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigInfo": "DeploymentConfigInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentGroupInputRequestTypeDef = TypedDict(
    "GetDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)

GetDeploymentGroupOutputTypeDef = TypedDict(
    "GetDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupInfo": "DeploymentGroupInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentInputRequestTypeDef = TypedDict(
    "GetDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentInstanceInputRequestTypeDef = TypedDict(
    "GetDeploymentInstanceInputRequestTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
    },
)

GetDeploymentInstanceOutputTypeDef = TypedDict(
    "GetDeploymentInstanceOutputTypeDef",
    {
        "instanceSummary": "InstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deploymentInfo": "DeploymentInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentTargetInputRequestTypeDef = TypedDict(
    "GetDeploymentTargetInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
    },
)

GetDeploymentTargetOutputTypeDef = TypedDict(
    "GetDeploymentTargetOutputTypeDef",
    {
        "deploymentTarget": "DeploymentTargetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "GetOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetOnPremisesInstanceOutputTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputTypeDef",
    {
        "instanceInfo": "InstanceInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef",
    {
        "repository": NotRequired[str],
        "commitId": NotRequired[str],
    },
)

GreenFleetProvisioningOptionTypeDef = TypedDict(
    "GreenFleetProvisioningOptionTypeDef",
    {
        "action": NotRequired[GreenFleetProvisioningActionType],
    },
)

InstanceInfoTypeDef = TypedDict(
    "InstanceInfoTypeDef",
    {
        "instanceName": NotRequired[str],
        "iamSessionArn": NotRequired[str],
        "iamUserArn": NotRequired[str],
        "instanceArn": NotRequired[str],
        "registerTime": NotRequired[datetime],
        "deregisterTime": NotRequired[datetime],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "deploymentId": NotRequired[str],
        "instanceId": NotRequired[str],
        "status": NotRequired[InstanceStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List["LifecycleEventTypeDef"]],
        "instanceType": NotRequired[InstanceTypeType],
    },
)

InstanceTargetTypeDef = TypedDict(
    "InstanceTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "targetArn": NotRequired[str],
        "status": NotRequired[TargetStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List["LifecycleEventTypeDef"]],
        "instanceLabel": NotRequired[TargetLabelType],
    },
)

LambdaFunctionInfoTypeDef = TypedDict(
    "LambdaFunctionInfoTypeDef",
    {
        "functionName": NotRequired[str],
        "functionAlias": NotRequired[str],
        "currentVersion": NotRequired[str],
        "targetVersion": NotRequired[str],
        "targetVersionWeight": NotRequired[float],
    },
)

LambdaTargetTypeDef = TypedDict(
    "LambdaTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "targetArn": NotRequired[str],
        "status": NotRequired[TargetStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List["LifecycleEventTypeDef"]],
        "lambdaFunctionInfo": NotRequired["LambdaFunctionInfoTypeDef"],
    },
)

LastDeploymentInfoTypeDef = TypedDict(
    "LastDeploymentInfoTypeDef",
    {
        "deploymentId": NotRequired[str],
        "status": NotRequired[DeploymentStatusType],
        "endTime": NotRequired[datetime],
        "createTime": NotRequired[datetime],
    },
)

LifecycleEventTypeDef = TypedDict(
    "LifecycleEventTypeDef",
    {
        "lifecycleEventName": NotRequired[str],
        "diagnostics": NotRequired["DiagnosticsTypeDef"],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "status": NotRequired[LifecycleEventStatusType],
    },
)

ListApplicationRevisionsInputRequestTypeDef = TypedDict(
    "ListApplicationRevisionsInputRequestTypeDef",
    {
        "applicationName": str,
        "sortBy": NotRequired[ApplicationRevisionSortByType],
        "sortOrder": NotRequired[SortOrderType],
        "s3Bucket": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
        "deployed": NotRequired[ListStateFilterActionType],
        "nextToken": NotRequired[str],
    },
)

ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {
        "revisions": List["RevisionLocationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsInputRequestTypeDef = TypedDict(
    "ListApplicationsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "applications": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentConfigsInputRequestTypeDef = TypedDict(
    "ListDeploymentConfigsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {
        "deploymentConfigsList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentGroupsInputRequestTypeDef = TypedDict(
    "ListDeploymentGroupsInputRequestTypeDef",
    {
        "applicationName": str,
        "nextToken": NotRequired[str],
    },
)

ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {
        "applicationName": str,
        "deploymentGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentInstancesInputRequestTypeDef = TypedDict(
    "ListDeploymentInstancesInputRequestTypeDef",
    {
        "deploymentId": str,
        "nextToken": NotRequired[str],
        "instanceStatusFilter": NotRequired[Sequence[InstanceStatusType]],
        "instanceTypeFilter": NotRequired[Sequence[InstanceTypeType]],
    },
)

ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {
        "instancesList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentTargetsInputRequestTypeDef = TypedDict(
    "ListDeploymentTargetsInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "nextToken": NotRequired[str],
        "targetFilters": NotRequired[Mapping[TargetFilterNameType, Sequence[str]]],
    },
)

ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef",
    {
        "targetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsInputRequestTypeDef = TypedDict(
    "ListDeploymentsInputRequestTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "externalId": NotRequired[str],
        "includeOnlyStatuses": NotRequired[Sequence[DeploymentStatusType]],
        "createTimeRange": NotRequired["TimeRangeTypeDef"],
        "nextToken": NotRequired[str],
    },
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGitHubAccountTokenNamesInputRequestTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {
        "tokenNameList": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "ListOnPremisesInstancesInputRequestTypeDef",
    {
        "registrationStatus": NotRequired[RegistrationStatusType],
        "tagFilters": NotRequired[Sequence["TagFilterTypeDef"]],
        "nextToken": NotRequired[str],
    },
)

ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {
        "instanceNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerInfoTypeDef = TypedDict(
    "LoadBalancerInfoTypeDef",
    {
        "elbInfoList": NotRequired[List["ELBInfoTypeDef"]],
        "targetGroupInfoList": NotRequired[List["TargetGroupInfoTypeDef"]],
        "targetGroupPairInfoList": NotRequired[List["TargetGroupPairInfoTypeDef"]],
    },
)

MinimumHealthyHostsTypeDef = TypedDict(
    "MinimumHealthyHostsTypeDef",
    {
        "type": NotRequired[MinimumHealthyHostsTypeType],
        "value": NotRequired[int],
    },
)

OnPremisesTagSetTypeDef = TypedDict(
    "OnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": NotRequired[List[List["TagFilterTypeDef"]]],
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

PutLifecycleEventHookExecutionStatusInputRequestTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "lifecycleEventHookExecutionId": NotRequired[str],
        "status": NotRequired[LifecycleEventStatusType],
    },
)

PutLifecycleEventHookExecutionStatusOutputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    {
        "lifecycleEventHookExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RawStringTypeDef = TypedDict(
    "RawStringTypeDef",
    {
        "content": NotRequired[str],
        "sha256": NotRequired[str],
    },
)

RegisterApplicationRevisionInputRequestTypeDef = TypedDict(
    "RegisterApplicationRevisionInputRequestTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "description": NotRequired[str],
    },
)

RegisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "RegisterOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": NotRequired[str],
        "iamUserArn": NotRequired[str],
    },
)

RelatedDeploymentsTypeDef = TypedDict(
    "RelatedDeploymentsTypeDef",
    {
        "autoUpdateOutdatedInstancesRootDeploymentId": NotRequired[str],
        "autoUpdateOutdatedInstancesDeploymentIds": NotRequired[List[str]],
    },
)

RemoveTagsFromOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "RemoveTagsFromOnPremisesInstancesInputRequestTypeDef",
    {
        "tags": Sequence["TagTypeDef"],
        "instanceNames": Sequence[str],
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

RevisionInfoTypeDef = TypedDict(
    "RevisionInfoTypeDef",
    {
        "revisionLocation": NotRequired["RevisionLocationTypeDef"],
        "genericRevisionInfo": NotRequired["GenericRevisionInfoTypeDef"],
    },
)

RevisionLocationTypeDef = TypedDict(
    "RevisionLocationTypeDef",
    {
        "revisionType": NotRequired[RevisionLocationTypeType],
        "s3Location": NotRequired["S3LocationTypeDef"],
        "gitHubLocation": NotRequired["GitHubLocationTypeDef"],
        "string": NotRequired["RawStringTypeDef"],
        "appSpecContent": NotRequired["AppSpecContentTypeDef"],
    },
)

RollbackInfoTypeDef = TypedDict(
    "RollbackInfoTypeDef",
    {
        "rollbackDeploymentId": NotRequired[str],
        "rollbackTriggeringDeploymentId": NotRequired[str],
        "rollbackMessage": NotRequired[str],
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "bundleType": NotRequired[BundleTypeType],
        "version": NotRequired[str],
        "eTag": NotRequired[str],
    },
)

SkipWaitTimeForInstanceTerminationInputRequestTypeDef = TypedDict(
    "SkipWaitTimeForInstanceTerminationInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
    },
)

StopDeploymentInputRequestTypeDef = TypedDict(
    "StopDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
        "autoRollbackEnabled": NotRequired[bool],
    },
)

StopDeploymentOutputTypeDef = TypedDict(
    "StopDeploymentOutputTypeDef",
    {
        "status": StopStatusType,
        "statusMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Type": NotRequired[TagFilterTypeType],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TargetGroupInfoTypeDef = TypedDict(
    "TargetGroupInfoTypeDef",
    {
        "name": NotRequired[str],
    },
)

TargetGroupPairInfoTypeDef = TypedDict(
    "TargetGroupPairInfoTypeDef",
    {
        "targetGroups": NotRequired[List["TargetGroupInfoTypeDef"]],
        "prodTrafficRoute": NotRequired["TrafficRouteTypeDef"],
        "testTrafficRoute": NotRequired["TrafficRouteTypeDef"],
    },
)

TargetInstancesTypeDef = TypedDict(
    "TargetInstancesTypeDef",
    {
        "tagFilters": NotRequired[List["EC2TagFilterTypeDef"]],
        "autoScalingGroups": NotRequired[List[str]],
        "ec2TagSet": NotRequired["EC2TagSetTypeDef"],
    },
)

TimeBasedCanaryTypeDef = TypedDict(
    "TimeBasedCanaryTypeDef",
    {
        "canaryPercentage": NotRequired[int],
        "canaryInterval": NotRequired[int],
    },
)

TimeBasedLinearTypeDef = TypedDict(
    "TimeBasedLinearTypeDef",
    {
        "linearPercentage": NotRequired[int],
        "linearInterval": NotRequired[int],
    },
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "start": NotRequired[Union[datetime, str]],
        "end": NotRequired[Union[datetime, str]],
    },
)

TrafficRouteTypeDef = TypedDict(
    "TrafficRouteTypeDef",
    {
        "listenerArns": NotRequired[List[str]],
    },
)

TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": NotRequired[TrafficRoutingTypeType],
        "timeBasedCanary": NotRequired["TimeBasedCanaryTypeDef"],
        "timeBasedLinear": NotRequired["TimeBasedLinearTypeDef"],
    },
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "triggerName": NotRequired[str],
        "triggerTargetArn": NotRequired[str],
        "triggerEvents": NotRequired[List[TriggerEventTypeType]],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApplicationInputRequestTypeDef = TypedDict(
    "UpdateApplicationInputRequestTypeDef",
    {
        "applicationName": NotRequired[str],
        "newApplicationName": NotRequired[str],
    },
)

UpdateDeploymentGroupInputRequestTypeDef = TypedDict(
    "UpdateDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "currentDeploymentGroupName": str,
        "newDeploymentGroupName": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "ec2TagFilters": NotRequired[Sequence["EC2TagFilterTypeDef"]],
        "onPremisesInstanceTagFilters": NotRequired[Sequence["TagFilterTypeDef"]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "serviceRoleArn": NotRequired[str],
        "triggerConfigurations": NotRequired[Sequence["TriggerConfigTypeDef"]],
        "alarmConfiguration": NotRequired["AlarmConfigurationTypeDef"],
        "autoRollbackConfiguration": NotRequired["AutoRollbackConfigurationTypeDef"],
        "outdatedInstancesStrategy": NotRequired[OutdatedInstancesStrategyType],
        "deploymentStyle": NotRequired["DeploymentStyleTypeDef"],
        "blueGreenDeploymentConfiguration": NotRequired["BlueGreenDeploymentConfigurationTypeDef"],
        "loadBalancerInfo": NotRequired["LoadBalancerInfoTypeDef"],
        "ec2TagSet": NotRequired["EC2TagSetTypeDef"],
        "ecsServices": NotRequired[Sequence["ECSServiceTypeDef"]],
        "onPremisesTagSet": NotRequired["OnPremisesTagSetTypeDef"],
    },
)

UpdateDeploymentGroupOutputTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List["AutoScalingGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
