"""
Type annotations for mgn service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mgn/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_mgn.type_defs import CPUTypeDef

    data: CPUTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    BootModeType,
    ChangeServerLifeCycleStateSourceServerLifecycleStateType,
    DataReplicationErrorStringType,
    DataReplicationInitiationStepNameType,
    DataReplicationInitiationStepStatusType,
    DataReplicationStateType,
    FirstBootType,
    InitiatedByType,
    JobLogEventType,
    JobStatusType,
    JobTypeType,
    LaunchDispositionType,
    LaunchStatusType,
    LifeCycleStateType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
    ReplicationTypeType,
    TargetInstanceTypeRightSizingMethodType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CPUTypeDef",
    "ChangeServerLifeCycleStateRequestRequestTypeDef",
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    "CreateReplicationConfigurationTemplateRequestRequestTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    "DeleteSourceServerRequestRequestTypeDef",
    "DeleteVcenterClientRequestRequestTypeDef",
    "DescribeJobLogItemsRequestRequestTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestRequestTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersRequestRequestTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "DescribeVcenterClientsRequestRequestTypeDef",
    "DescribeVcenterClientsResponseTypeDef",
    "DisconnectFromServiceRequestRequestTypeDef",
    "DiskTypeDef",
    "FinalizeCutoverRequestRequestTypeDef",
    "GetLaunchConfigurationRequestRequestTypeDef",
    "GetReplicationConfigurationRequestRequestTypeDef",
    "IdentificationHintsTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchedInstanceTypeDef",
    "LicensingTypeDef",
    "LifeCycleLastCutoverFinalizedTypeDef",
    "LifeCycleLastCutoverInitiatedTypeDef",
    "LifeCycleLastCutoverRevertedTypeDef",
    "LifeCycleLastCutoverTypeDef",
    "LifeCycleLastTestFinalizedTypeDef",
    "LifeCycleLastTestInitiatedTypeDef",
    "LifeCycleLastTestRevertedTypeDef",
    "LifeCycleLastTestTypeDef",
    "LifeCycleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarkAsArchivedRequestRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingServerTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationTemplateResponseMetadataTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "ReplicationConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDataReplicationRequestRequestTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerResponseMetadataTypeDef",
    "SourceServerTypeDef",
    "StartCutoverRequestRequestTypeDef",
    "StartCutoverResponseTypeDef",
    "StartReplicationRequestRequestTypeDef",
    "StartTestRequestRequestTypeDef",
    "StartTestResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TerminateTargetInstancesRequestRequestTypeDef",
    "TerminateTargetInstancesResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLaunchConfigurationRequestRequestTypeDef",
    "UpdateReplicationConfigurationRequestRequestTypeDef",
    "UpdateReplicationConfigurationTemplateRequestRequestTypeDef",
    "UpdateSourceServerReplicationTypeRequestRequestTypeDef",
    "VcenterClientTypeDef",
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "cores": NotRequired[int],
        "modelName": NotRequired[str],
    },
)

ChangeServerLifeCycleStateRequestRequestTypeDef = TypedDict(
    "ChangeServerLifeCycleStateRequestRequestTypeDef",
    {
        "lifeCycle": "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
        "sourceServerID": str,
    },
)

ChangeServerLifeCycleStateSourceServerLifecycleTypeDef = TypedDict(
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    {
        "state": ChangeServerLifeCycleStateSourceServerLifecycleStateType,
    },
)

CreateReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "CreateReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": Sequence[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Mapping[str, str],
        "useDedicatedReplicationServer": bool,
        "ebsEncryptionKeyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

DataReplicationErrorTypeDef = TypedDict(
    "DataReplicationErrorTypeDef",
    {
        "error": NotRequired[DataReplicationErrorStringType],
        "rawError": NotRequired[str],
    },
)

DataReplicationInfoReplicatedDiskTypeDef = TypedDict(
    "DataReplicationInfoReplicatedDiskTypeDef",
    {
        "backloggedStorageBytes": NotRequired[int],
        "deviceName": NotRequired[str],
        "replicatedStorageBytes": NotRequired[int],
        "rescannedStorageBytes": NotRequired[int],
        "totalStorageBytes": NotRequired[int],
    },
)

DataReplicationInfoTypeDef = TypedDict(
    "DataReplicationInfoTypeDef",
    {
        "dataReplicationError": NotRequired["DataReplicationErrorTypeDef"],
        "dataReplicationInitiation": NotRequired["DataReplicationInitiationTypeDef"],
        "dataReplicationState": NotRequired[DataReplicationStateType],
        "etaDateTime": NotRequired[str],
        "lagDuration": NotRequired[str],
        "lastSnapshotDateTime": NotRequired[str],
        "replicatedDisks": NotRequired[List["DataReplicationInfoReplicatedDiskTypeDef"]],
    },
)

DataReplicationInitiationStepTypeDef = TypedDict(
    "DataReplicationInitiationStepTypeDef",
    {
        "name": NotRequired[DataReplicationInitiationStepNameType],
        "status": NotRequired[DataReplicationInitiationStepStatusType],
    },
)

DataReplicationInitiationTypeDef = TypedDict(
    "DataReplicationInitiationTypeDef",
    {
        "nextAttemptDateTime": NotRequired[str],
        "startDateTime": NotRequired[str],
        "steps": NotRequired[List["DataReplicationInitiationStepTypeDef"]],
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "jobID": str,
    },
)

DeleteReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)

DeleteSourceServerRequestRequestTypeDef = TypedDict(
    "DeleteSourceServerRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

DeleteVcenterClientRequestRequestTypeDef = TypedDict(
    "DeleteVcenterClientRequestRequestTypeDef",
    {
        "vcenterClientID": str,
    },
)

DescribeJobLogItemsRequestRequestTypeDef = TypedDict(
    "DescribeJobLogItemsRequestRequestTypeDef",
    {
        "jobID": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeJobLogItemsResponseTypeDef = TypedDict(
    "DescribeJobLogItemsResponseTypeDef",
    {
        "items": List["JobLogTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsRequestFiltersTypeDef = TypedDict(
    "DescribeJobsRequestFiltersTypeDef",
    {
        "fromDate": NotRequired[str],
        "jobIDs": NotRequired[Sequence[str]],
        "toDate": NotRequired[str],
    },
)

DescribeJobsRequestRequestTypeDef = TypedDict(
    "DescribeJobsRequestRequestTypeDef",
    {
        "filters": "DescribeJobsRequestFiltersTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef",
    {
        "items": List["JobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationConfigurationTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeReplicationConfigurationTemplatesRequestRequestTypeDef",
    {
        "replicationConfigurationTemplateIDs": Sequence[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeReplicationConfigurationTemplatesResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    {
        "items": List["ReplicationConfigurationTemplateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSourceServersRequestFiltersTypeDef = TypedDict(
    "DescribeSourceServersRequestFiltersTypeDef",
    {
        "isArchived": NotRequired[bool],
        "lifeCycleStates": NotRequired[Sequence[LifeCycleStateType]],
        "replicationTypes": NotRequired[Sequence[ReplicationTypeType]],
        "sourceServerIDs": NotRequired[Sequence[str]],
    },
)

DescribeSourceServersRequestRequestTypeDef = TypedDict(
    "DescribeSourceServersRequestRequestTypeDef",
    {
        "filters": "DescribeSourceServersRequestFiltersTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeSourceServersResponseTypeDef = TypedDict(
    "DescribeSourceServersResponseTypeDef",
    {
        "items": List["SourceServerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVcenterClientsRequestRequestTypeDef = TypedDict(
    "DescribeVcenterClientsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeVcenterClientsResponseTypeDef = TypedDict(
    "DescribeVcenterClientsResponseTypeDef",
    {
        "items": List["VcenterClientTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisconnectFromServiceRequestRequestTypeDef = TypedDict(
    "DisconnectFromServiceRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "bytes": NotRequired[int],
        "deviceName": NotRequired[str],
    },
)

FinalizeCutoverRequestRequestTypeDef = TypedDict(
    "FinalizeCutoverRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

GetLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "GetLaunchConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

GetReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetReplicationConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

IdentificationHintsTypeDef = TypedDict(
    "IdentificationHintsTypeDef",
    {
        "awsInstanceID": NotRequired[str],
        "fqdn": NotRequired[str],
        "hostname": NotRequired[str],
        "vmPath": NotRequired[str],
        "vmWareUuid": NotRequired[str],
    },
)

JobLogEventDataTypeDef = TypedDict(
    "JobLogEventDataTypeDef",
    {
        "conversionServerID": NotRequired[str],
        "rawError": NotRequired[str],
        "sourceServerID": NotRequired[str],
        "targetInstanceID": NotRequired[str],
    },
)

JobLogTypeDef = TypedDict(
    "JobLogTypeDef",
    {
        "event": NotRequired[JobLogEventType],
        "eventData": NotRequired["JobLogEventDataTypeDef"],
        "logDateTime": NotRequired[str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "jobID": str,
        "arn": NotRequired[str],
        "creationDateTime": NotRequired[str],
        "endDateTime": NotRequired[str],
        "initiatedBy": NotRequired[InitiatedByType],
        "participatingServers": NotRequired[List["ParticipatingServerTypeDef"]],
        "status": NotRequired[JobStatusType],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[JobTypeType],
    },
)

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "bootMode": BootModeType,
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "name": str,
        "sourceServerID": str,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchedInstanceTypeDef = TypedDict(
    "LaunchedInstanceTypeDef",
    {
        "ec2InstanceID": NotRequired[str],
        "firstBoot": NotRequired[FirstBootType],
        "jobID": NotRequired[str],
    },
)

LicensingTypeDef = TypedDict(
    "LicensingTypeDef",
    {
        "osByol": NotRequired[bool],
    },
)

LifeCycleLastCutoverFinalizedTypeDef = TypedDict(
    "LifeCycleLastCutoverFinalizedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
    },
)

LifeCycleLastCutoverInitiatedTypeDef = TypedDict(
    "LifeCycleLastCutoverInitiatedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
        "jobID": NotRequired[str],
    },
)

LifeCycleLastCutoverRevertedTypeDef = TypedDict(
    "LifeCycleLastCutoverRevertedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
    },
)

LifeCycleLastCutoverTypeDef = TypedDict(
    "LifeCycleLastCutoverTypeDef",
    {
        "finalized": NotRequired["LifeCycleLastCutoverFinalizedTypeDef"],
        "initiated": NotRequired["LifeCycleLastCutoverInitiatedTypeDef"],
        "reverted": NotRequired["LifeCycleLastCutoverRevertedTypeDef"],
    },
)

LifeCycleLastTestFinalizedTypeDef = TypedDict(
    "LifeCycleLastTestFinalizedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
    },
)

LifeCycleLastTestInitiatedTypeDef = TypedDict(
    "LifeCycleLastTestInitiatedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
        "jobID": NotRequired[str],
    },
)

LifeCycleLastTestRevertedTypeDef = TypedDict(
    "LifeCycleLastTestRevertedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
    },
)

LifeCycleLastTestTypeDef = TypedDict(
    "LifeCycleLastTestTypeDef",
    {
        "finalized": NotRequired["LifeCycleLastTestFinalizedTypeDef"],
        "initiated": NotRequired["LifeCycleLastTestInitiatedTypeDef"],
        "reverted": NotRequired["LifeCycleLastTestRevertedTypeDef"],
    },
)

LifeCycleTypeDef = TypedDict(
    "LifeCycleTypeDef",
    {
        "addedToServiceDateTime": NotRequired[str],
        "elapsedReplicationDuration": NotRequired[str],
        "firstByteDateTime": NotRequired[str],
        "lastCutover": NotRequired["LifeCycleLastCutoverTypeDef"],
        "lastSeenByServiceDateTime": NotRequired[str],
        "lastTest": NotRequired["LifeCycleLastTestTypeDef"],
        "state": NotRequired[LifeCycleStateType],
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

MarkAsArchivedRequestRequestTypeDef = TypedDict(
    "MarkAsArchivedRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "ips": NotRequired[List[str]],
        "isPrimary": NotRequired[bool],
        "macAddress": NotRequired[str],
    },
)

OSTypeDef = TypedDict(
    "OSTypeDef",
    {
        "fullString": NotRequired[str],
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

ParticipatingServerTypeDef = TypedDict(
    "ParticipatingServerTypeDef",
    {
        "launchStatus": NotRequired[LaunchStatusType],
        "sourceServerID": NotRequired[str],
    },
)

ReplicationConfigurationReplicatedDiskTypeDef = TypedDict(
    "ReplicationConfigurationReplicatedDiskTypeDef",
    {
        "deviceName": NotRequired[str],
        "iops": NotRequired[int],
        "isBootDisk": NotRequired[bool],
        "stagingDiskType": NotRequired[ReplicationConfigurationReplicatedDiskStagingDiskTypeType],
        "throughput": NotRequired[int],
    },
)

ReplicationConfigurationTemplateResponseMetadataTypeDef = TypedDict(
    "ReplicationConfigurationTemplateResponseMetadataTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "replicationConfigurationTemplateID": str,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "tags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationConfigurationTemplateTypeDef = TypedDict(
    "ReplicationConfigurationTemplateTypeDef",
    {
        "replicationConfigurationTemplateID": str,
        "arn": NotRequired[str],
        "associateDefaultSecurityGroup": NotRequired[bool],
        "bandwidthThrottling": NotRequired[int],
        "createPublicIP": NotRequired[bool],
        "dataPlaneRouting": NotRequired[ReplicationConfigurationDataPlaneRoutingType],
        "defaultLargeStagingDiskType": NotRequired[
            ReplicationConfigurationDefaultLargeStagingDiskTypeType
        ],
        "ebsEncryption": NotRequired[ReplicationConfigurationEbsEncryptionType],
        "ebsEncryptionKeyArn": NotRequired[str],
        "replicationServerInstanceType": NotRequired[str],
        "replicationServersSecurityGroupsIDs": NotRequired[List[str]],
        "stagingAreaSubnetId": NotRequired[str],
        "stagingAreaTags": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "useDedicatedReplicationServer": NotRequired[bool],
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
        "replicatedDisks": List["ReplicationConfigurationReplicatedDiskTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "sourceServerID": str,
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RetryDataReplicationRequestRequestTypeDef = TypedDict(
    "RetryDataReplicationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

SourcePropertiesTypeDef = TypedDict(
    "SourcePropertiesTypeDef",
    {
        "cpus": NotRequired[List["CPUTypeDef"]],
        "disks": NotRequired[List["DiskTypeDef"]],
        "identificationHints": NotRequired["IdentificationHintsTypeDef"],
        "lastUpdatedDateTime": NotRequired[str],
        "networkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
        "os": NotRequired["OSTypeDef"],
        "ramBytes": NotRequired[int],
        "recommendedInstanceType": NotRequired[str],
    },
)

SourceServerResponseMetadataTypeDef = TypedDict(
    "SourceServerResponseMetadataTypeDef",
    {
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "isArchived": bool,
        "launchedInstance": "LaunchedInstanceTypeDef",
        "lifeCycle": "LifeCycleTypeDef",
        "replicationType": ReplicationTypeType,
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "tags": Dict[str, str],
        "vcenterClientID": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceServerTypeDef = TypedDict(
    "SourceServerTypeDef",
    {
        "arn": NotRequired[str],
        "dataReplicationInfo": NotRequired["DataReplicationInfoTypeDef"],
        "isArchived": NotRequired[bool],
        "launchedInstance": NotRequired["LaunchedInstanceTypeDef"],
        "lifeCycle": NotRequired["LifeCycleTypeDef"],
        "replicationType": NotRequired[ReplicationTypeType],
        "sourceProperties": NotRequired["SourcePropertiesTypeDef"],
        "sourceServerID": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "vcenterClientID": NotRequired[str],
    },
)

StartCutoverRequestRequestTypeDef = TypedDict(
    "StartCutoverRequestRequestTypeDef",
    {
        "sourceServerIDs": Sequence[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartCutoverResponseTypeDef = TypedDict(
    "StartCutoverResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReplicationRequestRequestTypeDef = TypedDict(
    "StartReplicationRequestRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

StartTestRequestRequestTypeDef = TypedDict(
    "StartTestRequestRequestTypeDef",
    {
        "sourceServerIDs": Sequence[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartTestResponseTypeDef = TypedDict(
    "StartTestResponseTypeDef",
    {
        "job": "JobTypeDef",
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

TerminateTargetInstancesRequestRequestTypeDef = TypedDict(
    "TerminateTargetInstancesRequestRequestTypeDef",
    {
        "sourceServerIDs": Sequence[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

TerminateTargetInstancesResponseTypeDef = TypedDict(
    "TerminateTargetInstancesResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLaunchConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
        "bootMode": NotRequired[BootModeType],
        "copyPrivateIp": NotRequired[bool],
        "copyTags": NotRequired[bool],
        "launchDisposition": NotRequired[LaunchDispositionType],
        "licensing": NotRequired["LicensingTypeDef"],
        "name": NotRequired[str],
        "targetInstanceTypeRightSizingMethod": NotRequired[TargetInstanceTypeRightSizingMethodType],
    },
)

UpdateReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateReplicationConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
        "associateDefaultSecurityGroup": NotRequired[bool],
        "bandwidthThrottling": NotRequired[int],
        "createPublicIP": NotRequired[bool],
        "dataPlaneRouting": NotRequired[ReplicationConfigurationDataPlaneRoutingType],
        "defaultLargeStagingDiskType": NotRequired[
            ReplicationConfigurationDefaultLargeStagingDiskTypeType
        ],
        "ebsEncryption": NotRequired[ReplicationConfigurationEbsEncryptionType],
        "ebsEncryptionKeyArn": NotRequired[str],
        "name": NotRequired[str],
        "replicatedDisks": NotRequired[Sequence["ReplicationConfigurationReplicatedDiskTypeDef"]],
        "replicationServerInstanceType": NotRequired[str],
        "replicationServersSecurityGroupsIDs": NotRequired[Sequence[str]],
        "stagingAreaSubnetId": NotRequired[str],
        "stagingAreaTags": NotRequired[Mapping[str, str]],
        "useDedicatedReplicationServer": NotRequired[bool],
    },
)

UpdateReplicationConfigurationTemplateRequestRequestTypeDef = TypedDict(
    "UpdateReplicationConfigurationTemplateRequestRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
        "arn": NotRequired[str],
        "associateDefaultSecurityGroup": NotRequired[bool],
        "bandwidthThrottling": NotRequired[int],
        "createPublicIP": NotRequired[bool],
        "dataPlaneRouting": NotRequired[ReplicationConfigurationDataPlaneRoutingType],
        "defaultLargeStagingDiskType": NotRequired[
            ReplicationConfigurationDefaultLargeStagingDiskTypeType
        ],
        "ebsEncryption": NotRequired[ReplicationConfigurationEbsEncryptionType],
        "ebsEncryptionKeyArn": NotRequired[str],
        "replicationServerInstanceType": NotRequired[str],
        "replicationServersSecurityGroupsIDs": NotRequired[Sequence[str]],
        "stagingAreaSubnetId": NotRequired[str],
        "stagingAreaTags": NotRequired[Mapping[str, str]],
        "useDedicatedReplicationServer": NotRequired[bool],
    },
)

UpdateSourceServerReplicationTypeRequestRequestTypeDef = TypedDict(
    "UpdateSourceServerReplicationTypeRequestRequestTypeDef",
    {
        "replicationType": ReplicationTypeType,
        "sourceServerID": str,
    },
)

VcenterClientTypeDef = TypedDict(
    "VcenterClientTypeDef",
    {
        "arn": NotRequired[str],
        "datacenterName": NotRequired[str],
        "hostname": NotRequired[str],
        "lastSeenDatetime": NotRequired[str],
        "sourceServerTags": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "vcenterClientID": NotRequired[str],
        "vcenterUUID": NotRequired[str],
    },
)
