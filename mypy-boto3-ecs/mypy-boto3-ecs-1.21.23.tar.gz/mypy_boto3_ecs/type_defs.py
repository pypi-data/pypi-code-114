"""
Type annotations for ecs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef

    data: AttachmentStateChangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AgentUpdateStatusType,
    AssignPublicIpType,
    CapacityProviderStatusType,
    CapacityProviderUpdateStatusType,
    ClusterFieldType,
    CompatibilityType,
    ConnectivityType,
    ContainerConditionType,
    ContainerInstanceFieldType,
    ContainerInstanceStatusType,
    CPUArchitectureType,
    DeploymentControllerTypeType,
    DeploymentRolloutStateType,
    DesiredStatusType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    ExecuteCommandLoggingType,
    FirelensConfigurationTypeType,
    HealthStatusType,
    InstanceHealthCheckStateType,
    IpcModeType,
    LaunchTypeType,
    LogDriverType,
    ManagedScalingStatusType,
    ManagedTerminationProtectionType,
    NetworkModeType,
    OSFamilyType,
    PidModeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    PropagateTagsType,
    ResourceTypeType,
    SchedulingStrategyType,
    ScopeType,
    SettingNameType,
    SortOrderType,
    StabilityStatusType,
    TaskDefinitionFamilyStatusType,
    TaskDefinitionStatusType,
    TaskStopCodeType,
    TransportProtocolType,
    UlimitNameType,
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
    "AttachmentStateChangeTypeDef",
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CapacityProviderTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterSettingTypeDef",
    "ClusterTypeDef",
    "ContainerDefinitionTypeDef",
    "ContainerDependencyTypeDef",
    "ContainerInstanceHealthStatusTypeDef",
    "ContainerInstanceTypeDef",
    "ContainerOverrideTypeDef",
    "ContainerStateChangeTypeDef",
    "ContainerTypeDef",
    "CreateCapacityProviderRequestRequestTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTaskSetRequestRequestTypeDef",
    "CreateTaskSetResponseTypeDef",
    "DeleteAccountSettingRequestRequestTypeDef",
    "DeleteAccountSettingResponseTypeDef",
    "DeleteAttributesRequestRequestTypeDef",
    "DeleteAttributesResponseTypeDef",
    "DeleteCapacityProviderRequestRequestTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTaskSetRequestRequestTypeDef",
    "DeleteTaskSetResponseTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentTypeDef",
    "DeregisterContainerInstanceRequestRequestTypeDef",
    "DeregisterContainerInstanceResponseTypeDef",
    "DeregisterTaskDefinitionRequestRequestTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeCapacityProvidersRequestRequestTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeContainerInstancesRequestRequestTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeTaskDefinitionRequestRequestTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "DescribeTaskSetsRequestRequestTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "DescribeTasksRequestRequestTypeDef",
    "DescribeTasksResponseTypeDef",
    "DeviceTypeDef",
    "DiscoverPollEndpointRequestRequestTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
    "ExecuteCommandRequestRequestTypeDef",
    "ExecuteCommandResponseTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "FailureTypeDef",
    "FirelensConfigurationTypeDef",
    "HealthCheckTypeDef",
    "HostEntryTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "InstanceHealthCheckResultTypeDef",
    "KernelCapabilitiesTypeDef",
    "KeyValuePairTypeDef",
    "LinuxParametersTypeDef",
    "ListAccountSettingsRequestRequestTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "ListAttributesRequestRequestTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesRequestRequestTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskDefinitionFamiliesRequestRequestTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsRequestRequestTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LoadBalancerTypeDef",
    "LogConfigurationTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "ManagedAgentTypeDef",
    "ManagedScalingTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PlatformDeviceTypeDef",
    "PortMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "PutAccountSettingDefaultRequestRequestTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingRequestRequestTypeDef",
    "PutAccountSettingResponseTypeDef",
    "PutAttributesRequestRequestTypeDef",
    "PutAttributesResponseTypeDef",
    "PutClusterCapacityProvidersRequestRequestTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "RegisterContainerInstanceRequestRequestTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "RegisterTaskDefinitionRequestRequestTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RunTaskRequestRequestTypeDef",
    "RunTaskResponseTypeDef",
    "RuntimePlatformTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceTypeDef",
    "SessionTypeDef",
    "SettingTypeDef",
    "StartTaskRequestRequestTypeDef",
    "StartTaskResponseTypeDef",
    "StopTaskRequestRequestTypeDef",
    "StopTaskResponseTypeDef",
    "SubmitAttachmentStateChangesRequestRequestTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeRequestRequestTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeRequestRequestTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "SystemControlTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskOverrideTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCapacityProviderRequestRequestTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateClusterSettingsRequestRequestTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "UpdateContainerAgentRequestRequestTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateRequestRequestTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "UpdateServicePrimaryTaskSetRequestRequestTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTaskSetRequestRequestTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
)

AttachmentStateChangeTypeDef = TypedDict(
    "AttachmentStateChangeTypeDef",
    {
        "attachmentArn": str,
        "status": str,
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[str],
        "status": NotRequired[str],
        "details": NotRequired[List["KeyValuePairTypeDef"]],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "name": str,
        "value": NotRequired[str],
        "targetType": NotRequired[Literal["container-instance"]],
        "targetId": NotRequired[str],
    },
)

AutoScalingGroupProviderTypeDef = TypedDict(
    "AutoScalingGroupProviderTypeDef",
    {
        "autoScalingGroupArn": str,
        "managedScaling": NotRequired["ManagedScalingTypeDef"],
        "managedTerminationProtection": NotRequired[ManagedTerminationProtectionType],
    },
)

AutoScalingGroupProviderUpdateTypeDef = TypedDict(
    "AutoScalingGroupProviderUpdateTypeDef",
    {
        "managedScaling": NotRequired["ManagedScalingTypeDef"],
        "managedTerminationProtection": NotRequired[ManagedTerminationProtectionType],
    },
)

AwsVpcConfigurationTypeDef = TypedDict(
    "AwsVpcConfigurationTypeDef",
    {
        "subnets": Sequence[str],
        "securityGroups": NotRequired[Sequence[str]],
        "assignPublicIp": NotRequired[AssignPublicIpType],
    },
)

CapacityProviderStrategyItemTypeDef = TypedDict(
    "CapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
        "weight": NotRequired[int],
        "base": NotRequired[int],
    },
)

CapacityProviderTypeDef = TypedDict(
    "CapacityProviderTypeDef",
    {
        "capacityProviderArn": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[CapacityProviderStatusType],
        "autoScalingGroupProvider": NotRequired["AutoScalingGroupProviderTypeDef"],
        "updateStatus": NotRequired[CapacityProviderUpdateStatusType],
        "updateStatusReason": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "executeCommandConfiguration": NotRequired["ExecuteCommandConfigurationTypeDef"],
    },
)

ClusterSettingTypeDef = TypedDict(
    "ClusterSettingTypeDef",
    {
        "name": NotRequired[Literal["containerInsights"]],
        "value": NotRequired[str],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "clusterArn": NotRequired[str],
        "clusterName": NotRequired[str],
        "configuration": NotRequired["ClusterConfigurationTypeDef"],
        "status": NotRequired[str],
        "registeredContainerInstancesCount": NotRequired[int],
        "runningTasksCount": NotRequired[int],
        "pendingTasksCount": NotRequired[int],
        "activeServicesCount": NotRequired[int],
        "statistics": NotRequired[List["KeyValuePairTypeDef"]],
        "tags": NotRequired[List["TagTypeDef"]],
        "settings": NotRequired[List["ClusterSettingTypeDef"]],
        "capacityProviders": NotRequired[List[str]],
        "defaultCapacityProviderStrategy": NotRequired[List["CapacityProviderStrategyItemTypeDef"]],
        "attachments": NotRequired[List["AttachmentTypeDef"]],
        "attachmentsStatus": NotRequired[str],
    },
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "name": NotRequired[str],
        "image": NotRequired[str],
        "repositoryCredentials": NotRequired["RepositoryCredentialsTypeDef"],
        "cpu": NotRequired[int],
        "memory": NotRequired[int],
        "memoryReservation": NotRequired[int],
        "links": NotRequired[List[str]],
        "portMappings": NotRequired[List["PortMappingTypeDef"]],
        "essential": NotRequired[bool],
        "entryPoint": NotRequired[List[str]],
        "command": NotRequired[List[str]],
        "environment": NotRequired[List["KeyValuePairTypeDef"]],
        "environmentFiles": NotRequired[List["EnvironmentFileTypeDef"]],
        "mountPoints": NotRequired[List["MountPointTypeDef"]],
        "volumesFrom": NotRequired[List["VolumeFromTypeDef"]],
        "linuxParameters": NotRequired["LinuxParametersTypeDef"],
        "secrets": NotRequired[List["SecretTypeDef"]],
        "dependsOn": NotRequired[List["ContainerDependencyTypeDef"]],
        "startTimeout": NotRequired[int],
        "stopTimeout": NotRequired[int],
        "hostname": NotRequired[str],
        "user": NotRequired[str],
        "workingDirectory": NotRequired[str],
        "disableNetworking": NotRequired[bool],
        "privileged": NotRequired[bool],
        "readonlyRootFilesystem": NotRequired[bool],
        "dnsServers": NotRequired[List[str]],
        "dnsSearchDomains": NotRequired[List[str]],
        "extraHosts": NotRequired[List["HostEntryTypeDef"]],
        "dockerSecurityOptions": NotRequired[List[str]],
        "interactive": NotRequired[bool],
        "pseudoTerminal": NotRequired[bool],
        "dockerLabels": NotRequired[Dict[str, str]],
        "ulimits": NotRequired[List["UlimitTypeDef"]],
        "logConfiguration": NotRequired["LogConfigurationTypeDef"],
        "healthCheck": NotRequired["HealthCheckTypeDef"],
        "systemControls": NotRequired[List["SystemControlTypeDef"]],
        "resourceRequirements": NotRequired[List["ResourceRequirementTypeDef"]],
        "firelensConfiguration": NotRequired["FirelensConfigurationTypeDef"],
    },
)

ContainerDependencyTypeDef = TypedDict(
    "ContainerDependencyTypeDef",
    {
        "containerName": str,
        "condition": ContainerConditionType,
    },
)

ContainerInstanceHealthStatusTypeDef = TypedDict(
    "ContainerInstanceHealthStatusTypeDef",
    {
        "overallStatus": NotRequired[InstanceHealthCheckStateType],
        "details": NotRequired[List["InstanceHealthCheckResultTypeDef"]],
    },
)

ContainerInstanceTypeDef = TypedDict(
    "ContainerInstanceTypeDef",
    {
        "containerInstanceArn": NotRequired[str],
        "ec2InstanceId": NotRequired[str],
        "capacityProviderName": NotRequired[str],
        "version": NotRequired[int],
        "versionInfo": NotRequired["VersionInfoTypeDef"],
        "remainingResources": NotRequired[List["ResourceTypeDef"]],
        "registeredResources": NotRequired[List["ResourceTypeDef"]],
        "status": NotRequired[str],
        "statusReason": NotRequired[str],
        "agentConnected": NotRequired[bool],
        "runningTasksCount": NotRequired[int],
        "pendingTasksCount": NotRequired[int],
        "agentUpdateStatus": NotRequired[AgentUpdateStatusType],
        "attributes": NotRequired[List["AttributeTypeDef"]],
        "registeredAt": NotRequired[datetime],
        "attachments": NotRequired[List["AttachmentTypeDef"]],
        "tags": NotRequired[List["TagTypeDef"]],
        "healthStatus": NotRequired["ContainerInstanceHealthStatusTypeDef"],
    },
)

ContainerOverrideTypeDef = TypedDict(
    "ContainerOverrideTypeDef",
    {
        "name": NotRequired[str],
        "command": NotRequired[List[str]],
        "environment": NotRequired[List["KeyValuePairTypeDef"]],
        "environmentFiles": NotRequired[List["EnvironmentFileTypeDef"]],
        "cpu": NotRequired[int],
        "memory": NotRequired[int],
        "memoryReservation": NotRequired[int],
        "resourceRequirements": NotRequired[List["ResourceRequirementTypeDef"]],
    },
)

ContainerStateChangeTypeDef = TypedDict(
    "ContainerStateChangeTypeDef",
    {
        "containerName": NotRequired[str],
        "imageDigest": NotRequired[str],
        "runtimeId": NotRequired[str],
        "exitCode": NotRequired[int],
        "networkBindings": NotRequired[Sequence["NetworkBindingTypeDef"]],
        "reason": NotRequired[str],
        "status": NotRequired[str],
    },
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "containerArn": NotRequired[str],
        "taskArn": NotRequired[str],
        "name": NotRequired[str],
        "image": NotRequired[str],
        "imageDigest": NotRequired[str],
        "runtimeId": NotRequired[str],
        "lastStatus": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "networkBindings": NotRequired[List["NetworkBindingTypeDef"]],
        "networkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
        "healthStatus": NotRequired[HealthStatusType],
        "managedAgents": NotRequired[List["ManagedAgentTypeDef"]],
        "cpu": NotRequired[str],
        "memory": NotRequired[str],
        "memoryReservation": NotRequired[str],
        "gpuIds": NotRequired[List[str]],
    },
)

CreateCapacityProviderRequestRequestTypeDef = TypedDict(
    "CreateCapacityProviderRequestRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": "AutoScalingGroupProviderTypeDef",
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCapacityProviderResponseTypeDef = TypedDict(
    "CreateCapacityProviderResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "clusterName": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "settings": NotRequired[Sequence["ClusterSettingTypeDef"]],
        "configuration": NotRequired["ClusterConfigurationTypeDef"],
        "capacityProviders": NotRequired[Sequence[str]],
        "defaultCapacityProviderStrategy": NotRequired[
            Sequence["CapacityProviderStrategyItemTypeDef"]
        ],
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "serviceName": str,
        "cluster": NotRequired[str],
        "taskDefinition": NotRequired[str],
        "loadBalancers": NotRequired[Sequence["LoadBalancerTypeDef"]],
        "serviceRegistries": NotRequired[Sequence["ServiceRegistryTypeDef"]],
        "desiredCount": NotRequired[int],
        "clientToken": NotRequired[str],
        "launchType": NotRequired[LaunchTypeType],
        "capacityProviderStrategy": NotRequired[Sequence["CapacityProviderStrategyItemTypeDef"]],
        "platformVersion": NotRequired[str],
        "role": NotRequired[str],
        "deploymentConfiguration": NotRequired["DeploymentConfigurationTypeDef"],
        "placementConstraints": NotRequired[Sequence["PlacementConstraintTypeDef"]],
        "placementStrategy": NotRequired[Sequence["PlacementStrategyTypeDef"]],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "healthCheckGracePeriodSeconds": NotRequired[int],
        "schedulingStrategy": NotRequired[SchedulingStrategyType],
        "deploymentController": NotRequired["DeploymentControllerTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "enableECSManagedTags": NotRequired[bool],
        "propagateTags": NotRequired[PropagateTagsType],
        "enableExecuteCommand": NotRequired[bool],
    },
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTaskSetRequestRequestTypeDef = TypedDict(
    "CreateTaskSetRequestRequestTypeDef",
    {
        "service": str,
        "cluster": str,
        "taskDefinition": str,
        "externalId": NotRequired[str],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "loadBalancers": NotRequired[Sequence["LoadBalancerTypeDef"]],
        "serviceRegistries": NotRequired[Sequence["ServiceRegistryTypeDef"]],
        "launchType": NotRequired[LaunchTypeType],
        "capacityProviderStrategy": NotRequired[Sequence["CapacityProviderStrategyItemTypeDef"]],
        "platformVersion": NotRequired[str],
        "scale": NotRequired["ScaleTypeDef"],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTaskSetResponseTypeDef = TypedDict(
    "CreateTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccountSettingRequestRequestTypeDef = TypedDict(
    "DeleteAccountSettingRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "principalArn": NotRequired[str],
    },
)

DeleteAccountSettingResponseTypeDef = TypedDict(
    "DeleteAccountSettingResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAttributesRequestRequestTypeDef = TypedDict(
    "DeleteAttributesRequestRequestTypeDef",
    {
        "attributes": Sequence["AttributeTypeDef"],
        "cluster": NotRequired[str],
    },
)

DeleteAttributesResponseTypeDef = TypedDict(
    "DeleteAttributesResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCapacityProviderRequestRequestTypeDef = TypedDict(
    "DeleteCapacityProviderRequestRequestTypeDef",
    {
        "capacityProvider": str,
    },
)

DeleteCapacityProviderResponseTypeDef = TypedDict(
    "DeleteCapacityProviderResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "cluster": str,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "service": str,
        "cluster": NotRequired[str],
        "force": NotRequired[bool],
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTaskSetRequestRequestTypeDef = TypedDict(
    "DeleteTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
        "force": NotRequired[bool],
    },
)

DeleteTaskSetResponseTypeDef = TypedDict(
    "DeleteTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentCircuitBreakerTypeDef = TypedDict(
    "DeploymentCircuitBreakerTypeDef",
    {
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentConfigurationTypeDef = TypedDict(
    "DeploymentConfigurationTypeDef",
    {
        "deploymentCircuitBreaker": NotRequired["DeploymentCircuitBreakerTypeDef"],
        "maximumPercent": NotRequired[int],
        "minimumHealthyPercent": NotRequired[int],
    },
)

DeploymentControllerTypeDef = TypedDict(
    "DeploymentControllerTypeDef",
    {
        "type": DeploymentControllerTypeType,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[str],
        "taskDefinition": NotRequired[str],
        "desiredCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "failedTasks": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "capacityProviderStrategy": NotRequired[List["CapacityProviderStrategyItemTypeDef"]],
        "launchType": NotRequired[LaunchTypeType],
        "platformVersion": NotRequired[str],
        "platformFamily": NotRequired[str],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "rolloutState": NotRequired[DeploymentRolloutStateType],
        "rolloutStateReason": NotRequired[str],
    },
)

DeregisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterContainerInstanceRequestRequestTypeDef",
    {
        "containerInstance": str,
        "cluster": NotRequired[str],
        "force": NotRequired[bool],
    },
)

DeregisterContainerInstanceResponseTypeDef = TypedDict(
    "DeregisterContainerInstanceResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DeregisterTaskDefinitionRequestRequestTypeDef",
    {
        "taskDefinition": str,
    },
)

DeregisterTaskDefinitionResponseTypeDef = TypedDict(
    "DeregisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityProvidersRequestRequestTypeDef = TypedDict(
    "DescribeCapacityProvidersRequestRequestTypeDef",
    {
        "capacityProviders": NotRequired[Sequence[str]],
        "include": NotRequired[Sequence[Literal["TAGS"]]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeCapacityProvidersResponseTypeDef = TypedDict(
    "DescribeCapacityProvidersResponseTypeDef",
    {
        "capacityProviders": List["CapacityProviderTypeDef"],
        "failures": List["FailureTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "clusters": NotRequired[Sequence[str]],
        "include": NotRequired[Sequence[ClusterFieldType]],
    },
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "clusters": List["ClusterTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContainerInstancesRequestRequestTypeDef = TypedDict(
    "DescribeContainerInstancesRequestRequestTypeDef",
    {
        "containerInstances": Sequence[str],
        "cluster": NotRequired[str],
        "include": NotRequired[Sequence[ContainerInstanceFieldType]],
    },
)

DescribeContainerInstancesResponseTypeDef = TypedDict(
    "DescribeContainerInstancesResponseTypeDef",
    {
        "containerInstances": List["ContainerInstanceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServicesRequestRequestTypeDef = TypedDict(
    "DescribeServicesRequestRequestTypeDef",
    {
        "services": Sequence[str],
        "cluster": NotRequired[str],
        "include": NotRequired[Sequence[Literal["TAGS"]]],
    },
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "services": List["ServiceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeTaskDefinitionRequestRequestTypeDef",
    {
        "taskDefinition": str,
        "include": NotRequired[Sequence[Literal["TAGS"]]],
    },
)

DescribeTaskDefinitionResponseTypeDef = TypedDict(
    "DescribeTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskSetsRequestRequestTypeDef = TypedDict(
    "DescribeTaskSetsRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSets": NotRequired[Sequence[str]],
        "include": NotRequired[Sequence[Literal["TAGS"]]],
    },
)

DescribeTaskSetsResponseTypeDef = TypedDict(
    "DescribeTaskSetsResponseTypeDef",
    {
        "taskSets": List["TaskSetTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTasksRequestRequestTypeDef = TypedDict(
    "DescribeTasksRequestRequestTypeDef",
    {
        "tasks": Sequence[str],
        "cluster": NotRequired[str],
        "include": NotRequired[Sequence[Literal["TAGS"]]],
    },
)

DescribeTasksResponseTypeDef = TypedDict(
    "DescribeTasksResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
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

DiscoverPollEndpointRequestRequestTypeDef = TypedDict(
    "DiscoverPollEndpointRequestRequestTypeDef",
    {
        "containerInstance": NotRequired[str],
        "cluster": NotRequired[str],
    },
)

DiscoverPollEndpointResponseTypeDef = TypedDict(
    "DiscoverPollEndpointResponseTypeDef",
    {
        "endpoint": str,
        "telemetryEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DockerVolumeConfigurationTypeDef = TypedDict(
    "DockerVolumeConfigurationTypeDef",
    {
        "scope": NotRequired[ScopeType],
        "autoprovision": NotRequired[bool],
        "driver": NotRequired[str],
        "driverOpts": NotRequired[Dict[str, str]],
        "labels": NotRequired[Dict[str, str]],
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

EnvironmentFileTypeDef = TypedDict(
    "EnvironmentFileTypeDef",
    {
        "value": str,
        "type": Literal["s3"],
    },
)

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

ExecuteCommandConfigurationTypeDef = TypedDict(
    "ExecuteCommandConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
        "logging": NotRequired[ExecuteCommandLoggingType],
        "logConfiguration": NotRequired["ExecuteCommandLogConfigurationTypeDef"],
    },
)

ExecuteCommandLogConfigurationTypeDef = TypedDict(
    "ExecuteCommandLogConfigurationTypeDef",
    {
        "cloudWatchLogGroupName": NotRequired[str],
        "cloudWatchEncryptionEnabled": NotRequired[bool],
        "s3BucketName": NotRequired[str],
        "s3EncryptionEnabled": NotRequired[bool],
        "s3KeyPrefix": NotRequired[str],
    },
)

ExecuteCommandRequestRequestTypeDef = TypedDict(
    "ExecuteCommandRequestRequestTypeDef",
    {
        "command": str,
        "interactive": bool,
        "task": str,
        "cluster": NotRequired[str],
        "container": NotRequired[str],
    },
)

ExecuteCommandResponseTypeDef = TypedDict(
    "ExecuteCommandResponseTypeDef",
    {
        "clusterArn": str,
        "containerArn": str,
        "containerName": str,
        "interactive": bool,
        "session": "SessionTypeDef",
        "taskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FSxWindowsFileServerAuthorizationConfigTypeDef = TypedDict(
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    {
        "credentialsParameter": str,
        "domain": str,
    },
)

FSxWindowsFileServerVolumeConfigurationTypeDef = TypedDict(
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": str,
        "authorizationConfig": "FSxWindowsFileServerAuthorizationConfigTypeDef",
    },
)

FailureTypeDef = TypedDict(
    "FailureTypeDef",
    {
        "arn": NotRequired[str],
        "reason": NotRequired[str],
        "detail": NotRequired[str],
    },
)

FirelensConfigurationTypeDef = TypedDict(
    "FirelensConfigurationTypeDef",
    {
        "type": FirelensConfigurationTypeType,
        "options": NotRequired[Dict[str, str]],
    },
)

HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "command": List[str],
        "interval": NotRequired[int],
        "timeout": NotRequired[int],
        "retries": NotRequired[int],
        "startPeriod": NotRequired[int],
    },
)

HostEntryTypeDef = TypedDict(
    "HostEntryTypeDef",
    {
        "hostname": str,
        "ipAddress": str,
    },
)

HostVolumePropertiesTypeDef = TypedDict(
    "HostVolumePropertiesTypeDef",
    {
        "sourcePath": NotRequired[str],
    },
)

InferenceAcceleratorOverrideTypeDef = TypedDict(
    "InferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": NotRequired[str],
        "deviceType": NotRequired[str],
    },
)

InferenceAcceleratorTypeDef = TypedDict(
    "InferenceAcceleratorTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
)

InstanceHealthCheckResultTypeDef = TypedDict(
    "InstanceHealthCheckResultTypeDef",
    {
        "type": NotRequired[Literal["CONTAINER_RUNTIME"]],
        "status": NotRequired[InstanceHealthCheckStateType],
        "lastUpdated": NotRequired[datetime],
        "lastStatusChange": NotRequired[datetime],
    },
)

KernelCapabilitiesTypeDef = TypedDict(
    "KernelCapabilitiesTypeDef",
    {
        "add": NotRequired[List[str]],
        "drop": NotRequired[List[str]],
    },
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "capabilities": NotRequired["KernelCapabilitiesTypeDef"],
        "devices": NotRequired[List["DeviceTypeDef"]],
        "initProcessEnabled": NotRequired[bool],
        "sharedMemorySize": NotRequired[int],
        "tmpfs": NotRequired[List["TmpfsTypeDef"]],
        "maxSwap": NotRequired[int],
        "swappiness": NotRequired[int],
    },
)

ListAccountSettingsRequestRequestTypeDef = TypedDict(
    "ListAccountSettingsRequestRequestTypeDef",
    {
        "name": NotRequired[SettingNameType],
        "value": NotRequired[str],
        "principalArn": NotRequired[str],
        "effectiveSettings": NotRequired[bool],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAccountSettingsResponseTypeDef = TypedDict(
    "ListAccountSettingsResponseTypeDef",
    {
        "settings": List["SettingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttributesRequestRequestTypeDef = TypedDict(
    "ListAttributesRequestRequestTypeDef",
    {
        "targetType": Literal["container-instance"],
        "cluster": NotRequired[str],
        "attributeName": NotRequired[str],
        "attributeValue": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAttributesResponseTypeDef = TypedDict(
    "ListAttributesResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusterArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerInstancesRequestRequestTypeDef = TypedDict(
    "ListContainerInstancesRequestRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "filter": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "status": NotRequired[ContainerInstanceStatusType],
    },
)

ListContainerInstancesResponseTypeDef = TypedDict(
    "ListContainerInstancesResponseTypeDef",
    {
        "containerInstanceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "launchType": NotRequired[LaunchTypeType],
        "schedulingStrategy": NotRequired[SchedulingStrategyType],
    },
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "serviceArns": List[str],
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionFamiliesRequestRequestTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesRequestRequestTypeDef",
    {
        "familyPrefix": NotRequired[str],
        "status": NotRequired[TaskDefinitionFamilyStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesResponseTypeDef",
    {
        "families": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "ListTaskDefinitionsRequestRequestTypeDef",
    {
        "familyPrefix": NotRequired[str],
        "status": NotRequired[TaskDefinitionStatusType],
        "sort": NotRequired[SortOrderType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTaskDefinitionsResponseTypeDef = TypedDict(
    "ListTaskDefinitionsResponseTypeDef",
    {
        "taskDefinitionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "containerInstance": NotRequired[str],
        "family": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "startedBy": NotRequired[str],
        "serviceName": NotRequired[str],
        "desiredStatus": NotRequired[DesiredStatusType],
        "launchType": NotRequired[LaunchTypeType],
    },
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "taskArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "targetGroupArn": NotRequired[str],
        "loadBalancerName": NotRequired[str],
        "containerName": NotRequired[str],
        "containerPort": NotRequired[int],
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

ManagedAgentStateChangeTypeDef = TypedDict(
    "ManagedAgentStateChangeTypeDef",
    {
        "containerName": str,
        "managedAgentName": Literal["ExecuteCommandAgent"],
        "status": str,
        "reason": NotRequired[str],
    },
)

ManagedAgentTypeDef = TypedDict(
    "ManagedAgentTypeDef",
    {
        "lastStartedAt": NotRequired[datetime],
        "name": NotRequired[Literal["ExecuteCommandAgent"]],
        "reason": NotRequired[str],
        "lastStatus": NotRequired[str],
    },
)

ManagedScalingTypeDef = TypedDict(
    "ManagedScalingTypeDef",
    {
        "status": NotRequired[ManagedScalingStatusType],
        "targetCapacity": NotRequired[int],
        "minimumScalingStepSize": NotRequired[int],
        "maximumScalingStepSize": NotRequired[int],
        "instanceWarmupPeriod": NotRequired[int],
    },
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "sourceVolume": NotRequired[str],
        "containerPath": NotRequired[str],
        "readOnly": NotRequired[bool],
    },
)

NetworkBindingTypeDef = TypedDict(
    "NetworkBindingTypeDef",
    {
        "bindIP": NotRequired[str],
        "containerPort": NotRequired[int],
        "hostPort": NotRequired[int],
        "protocol": NotRequired[TransportProtocolType],
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": NotRequired["AwsVpcConfigurationTypeDef"],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": NotRequired[str],
        "privateIpv4Address": NotRequired[str],
        "ipv6Address": NotRequired[str],
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

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": NotRequired[PlacementConstraintTypeType],
        "expression": NotRequired[str],
    },
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": NotRequired[PlacementStrategyTypeType],
        "field": NotRequired[str],
    },
)

PlatformDeviceTypeDef = TypedDict(
    "PlatformDeviceTypeDef",
    {
        "id": str,
        "type": Literal["GPU"],
    },
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "containerPort": NotRequired[int],
        "hostPort": NotRequired[int],
        "protocol": NotRequired[TransportProtocolType],
    },
)

ProxyConfigurationTypeDef = TypedDict(
    "ProxyConfigurationTypeDef",
    {
        "containerName": str,
        "type": NotRequired[Literal["APPMESH"]],
        "properties": NotRequired[List["KeyValuePairTypeDef"]],
    },
)

PutAccountSettingDefaultRequestRequestTypeDef = TypedDict(
    "PutAccountSettingDefaultRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)

PutAccountSettingDefaultResponseTypeDef = TypedDict(
    "PutAccountSettingDefaultResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAccountSettingRequestRequestTypeDef = TypedDict(
    "PutAccountSettingRequestRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": NotRequired[str],
    },
)

PutAccountSettingResponseTypeDef = TypedDict(
    "PutAccountSettingResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAttributesRequestRequestTypeDef = TypedDict(
    "PutAttributesRequestRequestTypeDef",
    {
        "attributes": Sequence["AttributeTypeDef"],
        "cluster": NotRequired[str],
    },
)

PutAttributesResponseTypeDef = TypedDict(
    "PutAttributesResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutClusterCapacityProvidersRequestRequestTypeDef = TypedDict(
    "PutClusterCapacityProvidersRequestRequestTypeDef",
    {
        "cluster": str,
        "capacityProviders": Sequence[str],
        "defaultCapacityProviderStrategy": Sequence["CapacityProviderStrategyItemTypeDef"],
    },
)

PutClusterCapacityProvidersResponseTypeDef = TypedDict(
    "PutClusterCapacityProvidersResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterContainerInstanceRequestRequestTypeDef = TypedDict(
    "RegisterContainerInstanceRequestRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "instanceIdentityDocument": NotRequired[str],
        "instanceIdentityDocumentSignature": NotRequired[str],
        "totalResources": NotRequired[Sequence["ResourceTypeDef"]],
        "versionInfo": NotRequired["VersionInfoTypeDef"],
        "containerInstanceArn": NotRequired[str],
        "attributes": NotRequired[Sequence["AttributeTypeDef"]],
        "platformDevices": NotRequired[Sequence["PlatformDeviceTypeDef"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

RegisterContainerInstanceResponseTypeDef = TypedDict(
    "RegisterContainerInstanceResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTaskDefinitionRequestRequestTypeDef = TypedDict(
    "RegisterTaskDefinitionRequestRequestTypeDef",
    {
        "family": str,
        "containerDefinitions": Sequence["ContainerDefinitionTypeDef"],
        "taskRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "networkMode": NotRequired[NetworkModeType],
        "volumes": NotRequired[Sequence["VolumeTypeDef"]],
        "placementConstraints": NotRequired[Sequence["TaskDefinitionPlacementConstraintTypeDef"]],
        "requiresCompatibilities": NotRequired[Sequence[CompatibilityType]],
        "cpu": NotRequired[str],
        "memory": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "pidMode": NotRequired[PidModeType],
        "ipcMode": NotRequired[IpcModeType],
        "proxyConfiguration": NotRequired["ProxyConfigurationTypeDef"],
        "inferenceAccelerators": NotRequired[Sequence["InferenceAcceleratorTypeDef"]],
        "ephemeralStorage": NotRequired["EphemeralStorageTypeDef"],
        "runtimePlatform": NotRequired["RuntimePlatformTypeDef"],
    },
)

RegisterTaskDefinitionResponseTypeDef = TypedDict(
    "RegisterTaskDefinitionResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryCredentialsTypeDef = TypedDict(
    "RepositoryCredentialsTypeDef",
    {
        "credentialsParameter": str,
    },
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "doubleValue": NotRequired[float],
        "longValue": NotRequired[int],
        "integerValue": NotRequired[int],
        "stringSetValue": NotRequired[List[str]],
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

RunTaskRequestRequestTypeDef = TypedDict(
    "RunTaskRequestRequestTypeDef",
    {
        "taskDefinition": str,
        "capacityProviderStrategy": NotRequired[Sequence["CapacityProviderStrategyItemTypeDef"]],
        "cluster": NotRequired[str],
        "count": NotRequired[int],
        "enableECSManagedTags": NotRequired[bool],
        "enableExecuteCommand": NotRequired[bool],
        "group": NotRequired[str],
        "launchType": NotRequired[LaunchTypeType],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "overrides": NotRequired["TaskOverrideTypeDef"],
        "placementConstraints": NotRequired[Sequence["PlacementConstraintTypeDef"]],
        "placementStrategy": NotRequired[Sequence["PlacementStrategyTypeDef"]],
        "platformVersion": NotRequired[str],
        "propagateTags": NotRequired[PropagateTagsType],
        "referenceId": NotRequired[str],
        "startedBy": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

RunTaskResponseTypeDef = TypedDict(
    "RunTaskResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RuntimePlatformTypeDef = TypedDict(
    "RuntimePlatformTypeDef",
    {
        "cpuArchitecture": NotRequired[CPUArchitectureType],
        "operatingSystemFamily": NotRequired[OSFamilyType],
    },
)

ScaleTypeDef = TypedDict(
    "ScaleTypeDef",
    {
        "value": NotRequired[float],
        "unit": NotRequired[Literal["PERCENT"]],
    },
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef",
    {
        "id": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)

ServiceRegistryTypeDef = TypedDict(
    "ServiceRegistryTypeDef",
    {
        "registryArn": NotRequired[str],
        "port": NotRequired[int],
        "containerName": NotRequired[str],
        "containerPort": NotRequired[int],
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "serviceArn": NotRequired[str],
        "serviceName": NotRequired[str],
        "clusterArn": NotRequired[str],
        "loadBalancers": NotRequired[List["LoadBalancerTypeDef"]],
        "serviceRegistries": NotRequired[List["ServiceRegistryTypeDef"]],
        "status": NotRequired[str],
        "desiredCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "launchType": NotRequired[LaunchTypeType],
        "capacityProviderStrategy": NotRequired[List["CapacityProviderStrategyItemTypeDef"]],
        "platformVersion": NotRequired[str],
        "platformFamily": NotRequired[str],
        "taskDefinition": NotRequired[str],
        "deploymentConfiguration": NotRequired["DeploymentConfigurationTypeDef"],
        "taskSets": NotRequired[List["TaskSetTypeDef"]],
        "deployments": NotRequired[List["DeploymentTypeDef"]],
        "roleArn": NotRequired[str],
        "events": NotRequired[List["ServiceEventTypeDef"]],
        "createdAt": NotRequired[datetime],
        "placementConstraints": NotRequired[List["PlacementConstraintTypeDef"]],
        "placementStrategy": NotRequired[List["PlacementStrategyTypeDef"]],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "healthCheckGracePeriodSeconds": NotRequired[int],
        "schedulingStrategy": NotRequired[SchedulingStrategyType],
        "deploymentController": NotRequired["DeploymentControllerTypeDef"],
        "tags": NotRequired[List["TagTypeDef"]],
        "createdBy": NotRequired[str],
        "enableECSManagedTags": NotRequired[bool],
        "propagateTags": NotRequired[PropagateTagsType],
        "enableExecuteCommand": NotRequired[bool],
    },
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "sessionId": NotRequired[str],
        "streamUrl": NotRequired[str],
        "tokenValue": NotRequired[str],
    },
)

SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "name": NotRequired[SettingNameType],
        "value": NotRequired[str],
        "principalArn": NotRequired[str],
    },
)

StartTaskRequestRequestTypeDef = TypedDict(
    "StartTaskRequestRequestTypeDef",
    {
        "containerInstances": Sequence[str],
        "taskDefinition": str,
        "cluster": NotRequired[str],
        "enableECSManagedTags": NotRequired[bool],
        "enableExecuteCommand": NotRequired[bool],
        "group": NotRequired[str],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "overrides": NotRequired["TaskOverrideTypeDef"],
        "propagateTags": NotRequired[PropagateTagsType],
        "referenceId": NotRequired[str],
        "startedBy": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartTaskResponseTypeDef = TypedDict(
    "StartTaskResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTaskRequestRequestTypeDef = TypedDict(
    "StopTaskRequestRequestTypeDef",
    {
        "task": str,
        "cluster": NotRequired[str],
        "reason": NotRequired[str],
    },
)

StopTaskResponseTypeDef = TypedDict(
    "StopTaskResponseTypeDef",
    {
        "task": "TaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitAttachmentStateChangesRequestRequestTypeDef = TypedDict(
    "SubmitAttachmentStateChangesRequestRequestTypeDef",
    {
        "attachments": Sequence["AttachmentStateChangeTypeDef"],
        "cluster": NotRequired[str],
    },
)

SubmitAttachmentStateChangesResponseTypeDef = TypedDict(
    "SubmitAttachmentStateChangesResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitContainerStateChangeRequestRequestTypeDef = TypedDict(
    "SubmitContainerStateChangeRequestRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "task": NotRequired[str],
        "containerName": NotRequired[str],
        "runtimeId": NotRequired[str],
        "status": NotRequired[str],
        "exitCode": NotRequired[int],
        "reason": NotRequired[str],
        "networkBindings": NotRequired[Sequence["NetworkBindingTypeDef"]],
    },
)

SubmitContainerStateChangeResponseTypeDef = TypedDict(
    "SubmitContainerStateChangeResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitTaskStateChangeRequestRequestTypeDef = TypedDict(
    "SubmitTaskStateChangeRequestRequestTypeDef",
    {
        "cluster": NotRequired[str],
        "task": NotRequired[str],
        "status": NotRequired[str],
        "reason": NotRequired[str],
        "containers": NotRequired[Sequence["ContainerStateChangeTypeDef"]],
        "attachments": NotRequired[Sequence["AttachmentStateChangeTypeDef"]],
        "managedAgents": NotRequired[Sequence["ManagedAgentStateChangeTypeDef"]],
        "pullStartedAt": NotRequired[Union[datetime, str]],
        "pullStoppedAt": NotRequired[Union[datetime, str]],
        "executionStoppedAt": NotRequired[Union[datetime, str]],
    },
)

SubmitTaskStateChangeResponseTypeDef = TypedDict(
    "SubmitTaskStateChangeResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemControlTypeDef = TypedDict(
    "SystemControlTypeDef",
    {
        "namespace": NotRequired[str],
        "value": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {
        "type": NotRequired[Literal["memberOf"]],
        "expression": NotRequired[str],
    },
)

TaskDefinitionTypeDef = TypedDict(
    "TaskDefinitionTypeDef",
    {
        "taskDefinitionArn": NotRequired[str],
        "containerDefinitions": NotRequired[List["ContainerDefinitionTypeDef"]],
        "family": NotRequired[str],
        "taskRoleArn": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "networkMode": NotRequired[NetworkModeType],
        "revision": NotRequired[int],
        "volumes": NotRequired[List["VolumeTypeDef"]],
        "status": NotRequired[TaskDefinitionStatusType],
        "requiresAttributes": NotRequired[List["AttributeTypeDef"]],
        "placementConstraints": NotRequired[List["TaskDefinitionPlacementConstraintTypeDef"]],
        "compatibilities": NotRequired[List[CompatibilityType]],
        "runtimePlatform": NotRequired["RuntimePlatformTypeDef"],
        "requiresCompatibilities": NotRequired[List[CompatibilityType]],
        "cpu": NotRequired[str],
        "memory": NotRequired[str],
        "inferenceAccelerators": NotRequired[List["InferenceAcceleratorTypeDef"]],
        "pidMode": NotRequired[PidModeType],
        "ipcMode": NotRequired[IpcModeType],
        "proxyConfiguration": NotRequired["ProxyConfigurationTypeDef"],
        "registeredAt": NotRequired[datetime],
        "deregisteredAt": NotRequired[datetime],
        "registeredBy": NotRequired[str],
        "ephemeralStorage": NotRequired["EphemeralStorageTypeDef"],
    },
)

TaskOverrideTypeDef = TypedDict(
    "TaskOverrideTypeDef",
    {
        "containerOverrides": NotRequired[List["ContainerOverrideTypeDef"]],
        "cpu": NotRequired[str],
        "inferenceAcceleratorOverrides": NotRequired[List["InferenceAcceleratorOverrideTypeDef"]],
        "executionRoleArn": NotRequired[str],
        "memory": NotRequired[str],
        "taskRoleArn": NotRequired[str],
        "ephemeralStorage": NotRequired["EphemeralStorageTypeDef"],
    },
)

TaskSetTypeDef = TypedDict(
    "TaskSetTypeDef",
    {
        "id": NotRequired[str],
        "taskSetArn": NotRequired[str],
        "serviceArn": NotRequired[str],
        "clusterArn": NotRequired[str],
        "startedBy": NotRequired[str],
        "externalId": NotRequired[str],
        "status": NotRequired[str],
        "taskDefinition": NotRequired[str],
        "computedDesiredCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "launchType": NotRequired[LaunchTypeType],
        "capacityProviderStrategy": NotRequired[List["CapacityProviderStrategyItemTypeDef"]],
        "platformVersion": NotRequired[str],
        "platformFamily": NotRequired[str],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "loadBalancers": NotRequired[List["LoadBalancerTypeDef"]],
        "serviceRegistries": NotRequired[List["ServiceRegistryTypeDef"]],
        "scale": NotRequired["ScaleTypeDef"],
        "stabilityStatus": NotRequired[StabilityStatusType],
        "stabilityStatusAt": NotRequired[datetime],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "attachments": NotRequired[List["AttachmentTypeDef"]],
        "attributes": NotRequired[List["AttributeTypeDef"]],
        "availabilityZone": NotRequired[str],
        "capacityProviderName": NotRequired[str],
        "clusterArn": NotRequired[str],
        "connectivity": NotRequired[ConnectivityType],
        "connectivityAt": NotRequired[datetime],
        "containerInstanceArn": NotRequired[str],
        "containers": NotRequired[List["ContainerTypeDef"]],
        "cpu": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "desiredStatus": NotRequired[str],
        "enableExecuteCommand": NotRequired[bool],
        "executionStoppedAt": NotRequired[datetime],
        "group": NotRequired[str],
        "healthStatus": NotRequired[HealthStatusType],
        "inferenceAccelerators": NotRequired[List["InferenceAcceleratorTypeDef"]],
        "lastStatus": NotRequired[str],
        "launchType": NotRequired[LaunchTypeType],
        "memory": NotRequired[str],
        "overrides": NotRequired["TaskOverrideTypeDef"],
        "platformVersion": NotRequired[str],
        "platformFamily": NotRequired[str],
        "pullStartedAt": NotRequired[datetime],
        "pullStoppedAt": NotRequired[datetime],
        "startedAt": NotRequired[datetime],
        "startedBy": NotRequired[str],
        "stopCode": NotRequired[TaskStopCodeType],
        "stoppedAt": NotRequired[datetime],
        "stoppedReason": NotRequired[str],
        "stoppingAt": NotRequired[datetime],
        "tags": NotRequired[List["TagTypeDef"]],
        "taskArn": NotRequired[str],
        "taskDefinitionArn": NotRequired[str],
        "version": NotRequired[int],
        "ephemeralStorage": NotRequired["EphemeralStorageTypeDef"],
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
        "name": UlimitNameType,
        "softLimit": int,
        "hardLimit": int,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateCapacityProviderRequestRequestTypeDef = TypedDict(
    "UpdateCapacityProviderRequestRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": "AutoScalingGroupProviderUpdateTypeDef",
    },
)

UpdateCapacityProviderResponseTypeDef = TypedDict(
    "UpdateCapacityProviderResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterRequestRequestTypeDef = TypedDict(
    "UpdateClusterRequestRequestTypeDef",
    {
        "cluster": str,
        "settings": NotRequired[Sequence["ClusterSettingTypeDef"]],
        "configuration": NotRequired["ClusterConfigurationTypeDef"],
    },
)

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterSettingsRequestRequestTypeDef = TypedDict(
    "UpdateClusterSettingsRequestRequestTypeDef",
    {
        "cluster": str,
        "settings": Sequence["ClusterSettingTypeDef"],
    },
)

UpdateClusterSettingsResponseTypeDef = TypedDict(
    "UpdateClusterSettingsResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContainerAgentRequestRequestTypeDef = TypedDict(
    "UpdateContainerAgentRequestRequestTypeDef",
    {
        "containerInstance": str,
        "cluster": NotRequired[str],
    },
)

UpdateContainerAgentResponseTypeDef = TypedDict(
    "UpdateContainerAgentResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContainerInstancesStateRequestRequestTypeDef = TypedDict(
    "UpdateContainerInstancesStateRequestRequestTypeDef",
    {
        "containerInstances": Sequence[str],
        "status": ContainerInstanceStatusType,
        "cluster": NotRequired[str],
    },
)

UpdateContainerInstancesStateResponseTypeDef = TypedDict(
    "UpdateContainerInstancesStateResponseTypeDef",
    {
        "containerInstances": List["ContainerInstanceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServicePrimaryTaskSetRequestRequestTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "primaryTaskSet": str,
    },
)

UpdateServicePrimaryTaskSetResponseTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "service": str,
        "cluster": NotRequired[str],
        "desiredCount": NotRequired[int],
        "taskDefinition": NotRequired[str],
        "capacityProviderStrategy": NotRequired[Sequence["CapacityProviderStrategyItemTypeDef"]],
        "deploymentConfiguration": NotRequired["DeploymentConfigurationTypeDef"],
        "networkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "placementConstraints": NotRequired[Sequence["PlacementConstraintTypeDef"]],
        "placementStrategy": NotRequired[Sequence["PlacementStrategyTypeDef"]],
        "platformVersion": NotRequired[str],
        "forceNewDeployment": NotRequired[bool],
        "healthCheckGracePeriodSeconds": NotRequired[int],
        "enableExecuteCommand": NotRequired[bool],
        "enableECSManagedTags": NotRequired[bool],
        "loadBalancers": NotRequired[Sequence["LoadBalancerTypeDef"]],
        "propagateTags": NotRequired[PropagateTagsType],
        "serviceRegistries": NotRequired[Sequence["ServiceRegistryTypeDef"]],
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTaskSetRequestRequestTypeDef = TypedDict(
    "UpdateTaskSetRequestRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
        "scale": "ScaleTypeDef",
    },
)

UpdateTaskSetResponseTypeDef = TypedDict(
    "UpdateTaskSetResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VersionInfoTypeDef = TypedDict(
    "VersionInfoTypeDef",
    {
        "agentVersion": NotRequired[str],
        "agentHash": NotRequired[str],
        "dockerVersion": NotRequired[str],
    },
)

VolumeFromTypeDef = TypedDict(
    "VolumeFromTypeDef",
    {
        "sourceContainer": NotRequired[str],
        "readOnly": NotRequired[bool],
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "name": NotRequired[str],
        "host": NotRequired["HostVolumePropertiesTypeDef"],
        "dockerVolumeConfiguration": NotRequired["DockerVolumeConfigurationTypeDef"],
        "efsVolumeConfiguration": NotRequired["EFSVolumeConfigurationTypeDef"],
        "fsxWindowsFileServerVolumeConfiguration": NotRequired[
            "FSxWindowsFileServerVolumeConfigurationTypeDef"
        ],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
