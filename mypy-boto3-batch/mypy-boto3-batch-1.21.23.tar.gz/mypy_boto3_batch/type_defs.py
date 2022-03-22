"""
Type annotations for batch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ArrayJobDependencyType,
    AssignPublicIpType,
    CEStateType,
    CEStatusType,
    CETypeType,
    CRAllocationStrategyType,
    CRTypeType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    JobDefinitionTypeType,
    JobStatusType,
    JQStateType,
    JQStatusType,
    LogDriverType,
    PlatformCapabilityType,
    ResourceTypeType,
    RetryActionType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "AttemptContainerDetailTypeDef",
    "AttemptDetailTypeDef",
    "CancelJobRequestRequestTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUpdateTypeDef",
    "ContainerDetailTypeDef",
    "ContainerOverridesTypeDef",
    "ContainerPropertiesTypeDef",
    "ContainerSummaryTypeDef",
    "CreateComputeEnvironmentRequestRequestTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateJobQueueRequestRequestTypeDef",
    "CreateJobQueueResponseTypeDef",
    "CreateSchedulingPolicyRequestRequestTypeDef",
    "CreateSchedulingPolicyResponseTypeDef",
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    "DeleteJobQueueRequestRequestTypeDef",
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    "DeregisterJobDefinitionRequestRequestTypeDef",
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "DescribeJobDefinitionsRequestRequestTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobQueuesRequestRequestTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    "DescribeSchedulingPoliciesResponseTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "Ec2ConfigurationTypeDef",
    "EvaluateOnExitTypeDef",
    "FairsharePolicyTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "HostTypeDef",
    "JobDefinitionTypeDef",
    "JobDependencyTypeDef",
    "JobDetailTypeDef",
    "JobQueueDetailTypeDef",
    "JobSummaryTypeDef",
    "JobTimeoutTypeDef",
    "KeyValuePairTypeDef",
    "KeyValuesPairTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LinuxParametersTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListSchedulingPoliciesRequestRequestTypeDef",
    "ListSchedulingPoliciesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeDetailsTypeDef",
    "NodeOverridesTypeDef",
    "NodePropertiesSummaryTypeDef",
    "NodePropertiesTypeDef",
    "NodePropertyOverrideTypeDef",
    "NodeRangePropertyTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionRequestRequestTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "ResourceRequirementTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStrategyTypeDef",
    "SchedulingPolicyDetailTypeDef",
    "SchedulingPolicyListingDetailTypeDef",
    "SecretTypeDef",
    "ShareAttributesTypeDef",
    "SubmitJobRequestRequestTypeDef",
    "SubmitJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TerminateJobRequestRequestTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateComputeEnvironmentRequestRequestTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateJobQueueRequestRequestTypeDef",
    "UpdateJobQueueResponseTypeDef",
    "UpdateSchedulingPolicyRequestRequestTypeDef",
    "VolumeTypeDef",
)

ArrayPropertiesDetailTypeDef = TypedDict(
    "ArrayPropertiesDetailTypeDef",
    {
        "statusSummary": NotRequired[Dict[str, int]],
        "size": NotRequired[int],
        "index": NotRequired[int],
    },
)

ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef",
    {
        "size": NotRequired[int],
        "index": NotRequired[int],
    },
)

ArrayPropertiesTypeDef = TypedDict(
    "ArrayPropertiesTypeDef",
    {
        "size": NotRequired[int],
    },
)

AttemptContainerDetailTypeDef = TypedDict(
    "AttemptContainerDetailTypeDef",
    {
        "containerInstanceArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "logStreamName": NotRequired[str],
        "networkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
    },
)

AttemptDetailTypeDef = TypedDict(
    "AttemptDetailTypeDef",
    {
        "container": NotRequired["AttemptContainerDetailTypeDef"],
        "startedAt": NotRequired[int],
        "stoppedAt": NotRequired[int],
        "statusReason": NotRequired[str],
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)

ComputeEnvironmentDetailTypeDef = TypedDict(
    "ComputeEnvironmentDetailTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
        "unmanagedvCpus": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[CETypeType],
        "state": NotRequired[CEStateType],
        "status": NotRequired[CEStatusType],
        "statusReason": NotRequired[str],
        "computeResources": NotRequired["ComputeResourceTypeDef"],
        "serviceRole": NotRequired[str],
    },
)

ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef",
    {
        "order": int,
        "computeEnvironment": str,
    },
)

ComputeResourceTypeDef = TypedDict(
    "ComputeResourceTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": Sequence[str],
        "allocationStrategy": NotRequired[CRAllocationStrategyType],
        "minvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "instanceTypes": NotRequired[Sequence[str]],
        "imageId": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "ec2KeyPair": NotRequired[str],
        "instanceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "placementGroup": NotRequired[str],
        "bidPercentage": NotRequired[int],
        "spotIamFleetRole": NotRequired[str],
        "launchTemplate": NotRequired["LaunchTemplateSpecificationTypeDef"],
        "ec2Configuration": NotRequired[Sequence["Ec2ConfigurationTypeDef"]],
    },
)

ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": NotRequired[int],
        "maxvCpus": NotRequired[int],
        "desiredvCpus": NotRequired[int],
        "subnets": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
    },
)

ContainerDetailTypeDef = TypedDict(
    "ContainerDetailTypeDef",
    {
        "image": NotRequired[str],
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[List[str]],
        "jobRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "volumes": NotRequired[List["VolumeTypeDef"]],
        "environment": NotRequired[List["KeyValuePairTypeDef"]],
        "mountPoints": NotRequired[List["MountPointTypeDef"]],
        "readonlyRootFilesystem": NotRequired[bool],
        "ulimits": NotRequired[List["UlimitTypeDef"]],
        "privileged": NotRequired[bool],
        "user": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "containerInstanceArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "logStreamName": NotRequired[str],
        "instanceType": NotRequired[str],
        "networkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
        "resourceRequirements": NotRequired[List["ResourceRequirementTypeDef"]],
        "linuxParameters": NotRequired["LinuxParametersTypeDef"],
        "logConfiguration": NotRequired["LogConfigurationTypeDef"],
        "secrets": NotRequired[List["SecretTypeDef"]],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "fargatePlatformConfiguration": NotRequired["FargatePlatformConfigurationTypeDef"],
    },
)

ContainerOverridesTypeDef = TypedDict(
    "ContainerOverridesTypeDef",
    {
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[Sequence[str]],
        "instanceType": NotRequired[str],
        "environment": NotRequired[Sequence["KeyValuePairTypeDef"]],
        "resourceRequirements": NotRequired[Sequence["ResourceRequirementTypeDef"]],
    },
)

ContainerPropertiesTypeDef = TypedDict(
    "ContainerPropertiesTypeDef",
    {
        "image": NotRequired[str],
        "vcpus": NotRequired[int],
        "memory": NotRequired[int],
        "command": NotRequired[List[str]],
        "jobRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "volumes": NotRequired[List["VolumeTypeDef"]],
        "environment": NotRequired[List["KeyValuePairTypeDef"]],
        "mountPoints": NotRequired[List["MountPointTypeDef"]],
        "readonlyRootFilesystem": NotRequired[bool],
        "privileged": NotRequired[bool],
        "ulimits": NotRequired[List["UlimitTypeDef"]],
        "user": NotRequired[str],
        "instanceType": NotRequired[str],
        "resourceRequirements": NotRequired[List["ResourceRequirementTypeDef"]],
        "linuxParameters": NotRequired["LinuxParametersTypeDef"],
        "logConfiguration": NotRequired["LogConfigurationTypeDef"],
        "secrets": NotRequired[List["SecretTypeDef"]],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "fargatePlatformConfiguration": NotRequired["FargatePlatformConfigurationTypeDef"],
    },
)

ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef",
    {
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
    },
)

CreateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironmentName": str,
        "type": CETypeType,
        "state": NotRequired[CEStateType],
        "unmanagedvCpus": NotRequired[int],
        "computeResources": NotRequired["ComputeResourceTypeDef"],
        "serviceRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateComputeEnvironmentResponseTypeDef = TypedDict(
    "CreateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobQueueRequestRequestTypeDef = TypedDict(
    "CreateJobQueueRequestRequestTypeDef",
    {
        "jobQueueName": str,
        "priority": int,
        "computeEnvironmentOrder": Sequence["ComputeEnvironmentOrderTypeDef"],
        "state": NotRequired[JQStateType],
        "schedulingPolicyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateJobQueueResponseTypeDef = TypedDict(
    "CreateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "CreateSchedulingPolicyRequestRequestTypeDef",
    {
        "name": str,
        "fairsharePolicy": NotRequired["FairsharePolicyTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateSchedulingPolicyResponseTypeDef = TypedDict(
    "CreateSchedulingPolicyResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)

DeleteJobQueueRequestRequestTypeDef = TypedDict(
    "DeleteJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
    },
)

DeleteSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeregisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinition": str,
    },
)

DescribeComputeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestRequestTypeDef",
    {
        "computeEnvironments": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeComputeEnvironmentsResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseTypeDef",
    {
        "computeEnvironments": List["ComputeEnvironmentDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestRequestTypeDef",
    {
        "jobDefinitions": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "jobDefinitionName": NotRequired[str],
        "status": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

DescribeJobDefinitionsResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseTypeDef",
    {
        "jobDefinitions": List["JobDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobQueuesRequestRequestTypeDef = TypedDict(
    "DescribeJobQueuesRequestRequestTypeDef",
    {
        "jobQueues": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeJobQueuesResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseTypeDef",
    {
        "jobQueues": List["JobQueueDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsRequestRequestTypeDef = TypedDict(
    "DescribeJobsRequestRequestTypeDef",
    {
        "jobs": Sequence[str],
    },
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef",
    {
        "jobs": List["JobDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeSchedulingPoliciesRequestRequestTypeDef",
    {
        "arns": Sequence[str],
    },
)

DescribeSchedulingPoliciesResponseTypeDef = TypedDict(
    "DescribeSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List["SchedulingPolicyDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "hostPath": str,
        "containerPath": NotRequired[str],
        "permissions": NotRequired[List[DeviceCgroupPermissionType]],
    },
)

EFSAuthorizationConfigTypeDef = TypedDict(
    "EFSAuthorizationConfigTypeDef",
    {
        "accessPointId": NotRequired[str],
        "iam": NotRequired[EFSAuthorizationConfigIAMType],
    },
)

EFSVolumeConfigurationTypeDef = TypedDict(
    "EFSVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": NotRequired[str],
        "transitEncryption": NotRequired[EFSTransitEncryptionType],
        "transitEncryptionPort": NotRequired[int],
        "authorizationConfig": NotRequired["EFSAuthorizationConfigTypeDef"],
    },
)

Ec2ConfigurationTypeDef = TypedDict(
    "Ec2ConfigurationTypeDef",
    {
        "imageType": str,
        "imageIdOverride": NotRequired[str],
    },
)

EvaluateOnExitTypeDef = TypedDict(
    "EvaluateOnExitTypeDef",
    {
        "action": RetryActionType,
        "onStatusReason": NotRequired[str],
        "onReason": NotRequired[str],
        "onExitCode": NotRequired[str],
    },
)

FairsharePolicyTypeDef = TypedDict(
    "FairsharePolicyTypeDef",
    {
        "shareDecaySeconds": NotRequired[int],
        "computeReservation": NotRequired[int],
        "shareDistribution": NotRequired[Sequence["ShareAttributesTypeDef"]],
    },
)

FargatePlatformConfigurationTypeDef = TypedDict(
    "FargatePlatformConfigurationTypeDef",
    {
        "platformVersion": NotRequired[str],
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "sourcePath": NotRequired[str],
    },
)

JobDefinitionTypeDef = TypedDict(
    "JobDefinitionTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "type": str,
        "status": NotRequired[str],
        "schedulingPriority": NotRequired[int],
        "parameters": NotRequired[Dict[str, str]],
        "retryStrategy": NotRequired["RetryStrategyTypeDef"],
        "containerProperties": NotRequired["ContainerPropertiesTypeDef"],
        "timeout": NotRequired["JobTimeoutTypeDef"],
        "nodeProperties": NotRequired["NodePropertiesTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "propagateTags": NotRequired[bool],
        "platformCapabilities": NotRequired[List[PlatformCapabilityType]],
    },
)

JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef",
    {
        "jobId": NotRequired[str],
        "type": NotRequired[ArrayJobDependencyType],
    },
)

JobDetailTypeDef = TypedDict(
    "JobDetailTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": JobStatusType,
        "startedAt": int,
        "jobDefinition": str,
        "jobArn": NotRequired[str],
        "shareIdentifier": NotRequired[str],
        "schedulingPriority": NotRequired[int],
        "attempts": NotRequired[List["AttemptDetailTypeDef"]],
        "statusReason": NotRequired[str],
        "createdAt": NotRequired[int],
        "retryStrategy": NotRequired["RetryStrategyTypeDef"],
        "stoppedAt": NotRequired[int],
        "dependsOn": NotRequired[List["JobDependencyTypeDef"]],
        "parameters": NotRequired[Dict[str, str]],
        "container": NotRequired["ContainerDetailTypeDef"],
        "nodeDetails": NotRequired["NodeDetailsTypeDef"],
        "nodeProperties": NotRequired["NodePropertiesTypeDef"],
        "arrayProperties": NotRequired["ArrayPropertiesDetailTypeDef"],
        "timeout": NotRequired["JobTimeoutTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "propagateTags": NotRequired[bool],
        "platformCapabilities": NotRequired[List[PlatformCapabilityType]],
    },
)

JobQueueDetailTypeDef = TypedDict(
    "JobQueueDetailTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": JQStateType,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
        "schedulingPolicyArn": NotRequired[str],
        "status": NotRequired[JQStatusType],
        "statusReason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobArn": NotRequired[str],
        "createdAt": NotRequired[int],
        "status": NotRequired[JobStatusType],
        "statusReason": NotRequired[str],
        "startedAt": NotRequired[int],
        "stoppedAt": NotRequired[int],
        "container": NotRequired["ContainerSummaryTypeDef"],
        "arrayProperties": NotRequired["ArrayPropertiesSummaryTypeDef"],
        "nodeProperties": NotRequired["NodePropertiesSummaryTypeDef"],
        "jobDefinition": NotRequired[str],
    },
)

JobTimeoutTypeDef = TypedDict(
    "JobTimeoutTypeDef",
    {
        "attemptDurationSeconds": NotRequired[int],
    },
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)

KeyValuesPairTypeDef = TypedDict(
    "KeyValuesPairTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": NotRequired[str],
        "launchTemplateName": NotRequired[str],
        "version": NotRequired[str],
    },
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "devices": NotRequired[List["DeviceTypeDef"]],
        "initProcessEnabled": NotRequired[bool],
        "sharedMemorySize": NotRequired[int],
        "tmpfs": NotRequired[List["TmpfsTypeDef"]],
        "maxSwap": NotRequired[int],
        "swappiness": NotRequired[int],
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "jobQueue": NotRequired[str],
        "arrayJobId": NotRequired[str],
        "multiNodeJobId": NotRequired[str],
        "jobStatus": NotRequired[JobStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filters": NotRequired[Sequence["KeyValuesPairTypeDef"]],
    },
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobSummaryList": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulingPoliciesRequestRequestTypeDef = TypedDict(
    "ListSchedulingPoliciesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSchedulingPoliciesResponseTypeDef = TypedDict(
    "ListSchedulingPoliciesResponseTypeDef",
    {
        "schedulingPolicies": List["SchedulingPolicyListingDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "logDriver": LogDriverType,
        "options": NotRequired[Dict[str, str]],
        "secretOptions": NotRequired[List["SecretTypeDef"]],
    },
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "containerPath": NotRequired[str],
        "readOnly": NotRequired[bool],
        "sourceVolume": NotRequired[str],
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "assignPublicIp": NotRequired[AssignPublicIpType],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": NotRequired[str],
        "ipv6Address": NotRequired[str],
        "privateIpv4Address": NotRequired[str],
    },
)

NodeDetailsTypeDef = TypedDict(
    "NodeDetailsTypeDef",
    {
        "nodeIndex": NotRequired[int],
        "isMainNode": NotRequired[bool],
    },
)

NodeOverridesTypeDef = TypedDict(
    "NodeOverridesTypeDef",
    {
        "numNodes": NotRequired[int],
        "nodePropertyOverrides": NotRequired[Sequence["NodePropertyOverrideTypeDef"]],
    },
)

NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {
        "isMainNode": NotRequired[bool],
        "numNodes": NotRequired[int],
        "nodeIndex": NotRequired[int],
    },
)

NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List["NodeRangePropertyTypeDef"],
    },
)

NodePropertyOverrideTypeDef = TypedDict(
    "NodePropertyOverrideTypeDef",
    {
        "targetNodes": str,
        "containerOverrides": NotRequired["ContainerOverridesTypeDef"],
    },
)

NodeRangePropertyTypeDef = TypedDict(
    "NodeRangePropertyTypeDef",
    {
        "targetNodes": str,
        "container": NotRequired["ContainerPropertiesTypeDef"],
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

RegisterJobDefinitionRequestRequestTypeDef = TypedDict(
    "RegisterJobDefinitionRequestRequestTypeDef",
    {
        "jobDefinitionName": str,
        "type": JobDefinitionTypeType,
        "parameters": NotRequired[Mapping[str, str]],
        "schedulingPriority": NotRequired[int],
        "containerProperties": NotRequired["ContainerPropertiesTypeDef"],
        "nodeProperties": NotRequired["NodePropertiesTypeDef"],
        "retryStrategy": NotRequired["RetryStrategyTypeDef"],
        "propagateTags": NotRequired[bool],
        "timeout": NotRequired["JobTimeoutTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
        "platformCapabilities": NotRequired[Sequence[PlatformCapabilityType]],
    },
)

RegisterJobDefinitionResponseTypeDef = TypedDict(
    "RegisterJobDefinitionResponseTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
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

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "attempts": NotRequired[int],
        "evaluateOnExit": NotRequired[List["EvaluateOnExitTypeDef"]],
    },
)

SchedulingPolicyDetailTypeDef = TypedDict(
    "SchedulingPolicyDetailTypeDef",
    {
        "name": str,
        "arn": str,
        "fairsharePolicy": NotRequired["FairsharePolicyTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

SchedulingPolicyListingDetailTypeDef = TypedDict(
    "SchedulingPolicyListingDetailTypeDef",
    {
        "arn": str,
    },
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

ShareAttributesTypeDef = TypedDict(
    "ShareAttributesTypeDef",
    {
        "shareIdentifier": str,
        "weightFactor": NotRequired[float],
    },
)

SubmitJobRequestRequestTypeDef = TypedDict(
    "SubmitJobRequestRequestTypeDef",
    {
        "jobName": str,
        "jobQueue": str,
        "jobDefinition": str,
        "shareIdentifier": NotRequired[str],
        "schedulingPriorityOverride": NotRequired[int],
        "arrayProperties": NotRequired["ArrayPropertiesTypeDef"],
        "dependsOn": NotRequired[Sequence["JobDependencyTypeDef"]],
        "parameters": NotRequired[Mapping[str, str]],
        "containerOverrides": NotRequired["ContainerOverridesTypeDef"],
        "nodeOverrides": NotRequired["NodeOverridesTypeDef"],
        "retryStrategy": NotRequired["RetryStrategyTypeDef"],
        "propagateTags": NotRequired[bool],
        "timeout": NotRequired["JobTimeoutTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

SubmitJobResponseTypeDef = TypedDict(
    "SubmitJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TerminateJobRequestRequestTypeDef = TypedDict(
    "TerminateJobRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)

TmpfsTypeDef = TypedDict(
    "TmpfsTypeDef",
    {
        "containerPath": str,
        "size": int,
        "mountOptions": NotRequired[List[str]],
    },
)

UlimitTypeDef = TypedDict(
    "UlimitTypeDef",
    {
        "hardLimit": int,
        "name": str,
        "softLimit": int,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateComputeEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateComputeEnvironmentRequestRequestTypeDef",
    {
        "computeEnvironment": str,
        "state": NotRequired[CEStateType],
        "unmanagedvCpus": NotRequired[int],
        "computeResources": NotRequired["ComputeResourceUpdateTypeDef"],
        "serviceRole": NotRequired[str],
    },
)

UpdateComputeEnvironmentResponseTypeDef = TypedDict(
    "UpdateComputeEnvironmentResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJobQueueRequestRequestTypeDef = TypedDict(
    "UpdateJobQueueRequestRequestTypeDef",
    {
        "jobQueue": str,
        "state": NotRequired[JQStateType],
        "schedulingPolicyArn": NotRequired[str],
        "priority": NotRequired[int],
        "computeEnvironmentOrder": NotRequired[Sequence["ComputeEnvironmentOrderTypeDef"]],
    },
)

UpdateJobQueueResponseTypeDef = TypedDict(
    "UpdateJobQueueResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSchedulingPolicyRequestRequestTypeDef = TypedDict(
    "UpdateSchedulingPolicyRequestRequestTypeDef",
    {
        "arn": str,
        "fairsharePolicy": NotRequired["FairsharePolicyTypeDef"],
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "host": NotRequired["HostTypeDef"],
        "name": NotRequired[str],
        "efsVolumeConfiguration": NotRequired["EFSVolumeConfigurationTypeDef"],
    },
)
