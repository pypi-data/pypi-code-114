"""
Type annotations for drs service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_drs/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_drs.type_defs import CPUTypeDef

    data: CPUTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    DataReplicationErrorStringType,
    DataReplicationInitiationStepNameType,
    DataReplicationInitiationStepStatusType,
    DataReplicationStateType,
    EC2InstanceStateType,
    FailbackReplicationErrorType,
    FailbackStateType,
    InitiatedByType,
    JobLogEventType,
    JobStatusType,
    JobTypeType,
    LastLaunchResultType,
    LastLaunchTypeType,
    LaunchDispositionType,
    LaunchStatusType,
    PITPolicyRuleUnitsType,
    RecoveryInstanceDataReplicationInitiationStepNameType,
    RecoveryInstanceDataReplicationInitiationStepStatusType,
    RecoveryInstanceDataReplicationStateType,
    RecoverySnapshotsOrderType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
    TargetInstanceTypeRightSizingMethodType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CPUTypeDef",
    "CreateReplicationConfigurationTemplateRequestRequestTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteRecoveryInstanceRequestRequestTypeDef",
    "DeleteReplicationConfigurationTemplateRequestRequestTypeDef",
    "DeleteSourceServerRequestRequestTypeDef",
    "DescribeJobLogItemsRequestRequestTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsRequestRequestTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeRecoveryInstancesRequestFiltersTypeDef",
    "DescribeRecoveryInstancesRequestRequestTypeDef",
    "DescribeRecoveryInstancesResponseTypeDef",
    "DescribeRecoverySnapshotsRequestFiltersTypeDef",
    "DescribeRecoverySnapshotsRequestRequestTypeDef",
    "DescribeRecoverySnapshotsResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestRequestTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersRequestRequestTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "DisconnectRecoveryInstanceRequestRequestTypeDef",
    "DisconnectSourceServerRequestRequestTypeDef",
    "DiskTypeDef",
    "GetFailbackReplicationConfigurationRequestRequestTypeDef",
    "GetFailbackReplicationConfigurationResponseTypeDef",
    "GetLaunchConfigurationRequestRequestTypeDef",
    "GetReplicationConfigurationRequestRequestTypeDef",
    "IdentificationHintsTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobTypeDef",
    "LaunchConfigurationTypeDef",
    "LicensingTypeDef",
    "LifeCycleLastLaunchInitiatedTypeDef",
    "LifeCycleLastLaunchTypeDef",
    "LifeCycleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PITPolicyRuleTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingServerTypeDef",
    "RecoveryInstanceDataReplicationErrorTypeDef",
    "RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef",
    "RecoveryInstanceDataReplicationInfoTypeDef",
    "RecoveryInstanceDataReplicationInitiationStepTypeDef",
    "RecoveryInstanceDataReplicationInitiationTypeDef",
    "RecoveryInstanceDiskTypeDef",
    "RecoveryInstanceFailbackTypeDef",
    "RecoveryInstancePropertiesTypeDef",
    "RecoveryInstanceTypeDef",
    "RecoverySnapshotTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationTemplateResponseMetadataTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "ReplicationConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDataReplicationRequestRequestTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerResponseMetadataTypeDef",
    "SourceServerTypeDef",
    "StartFailbackLaunchRequestRequestTypeDef",
    "StartFailbackLaunchResponseTypeDef",
    "StartRecoveryRequestRequestTypeDef",
    "StartRecoveryRequestSourceServerTypeDef",
    "StartRecoveryResponseTypeDef",
    "StopFailbackRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TerminateRecoveryInstancesRequestRequestTypeDef",
    "TerminateRecoveryInstancesResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFailbackReplicationConfigurationRequestRequestTypeDef",
    "UpdateLaunchConfigurationRequestRequestTypeDef",
    "UpdateReplicationConfigurationRequestRequestTypeDef",
    "UpdateReplicationConfigurationTemplateRequestRequestTypeDef",
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "cores": NotRequired[int],
        "modelName": NotRequired[str],
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
        "pitPolicy": Sequence["PITPolicyRuleTypeDef"],
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

DeleteRecoveryInstanceRequestRequestTypeDef = TypedDict(
    "DeleteRecoveryInstanceRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
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

DescribeRecoveryInstancesRequestFiltersTypeDef = TypedDict(
    "DescribeRecoveryInstancesRequestFiltersTypeDef",
    {
        "recoveryInstanceIDs": NotRequired[Sequence[str]],
        "sourceServerIDs": NotRequired[Sequence[str]],
    },
)

DescribeRecoveryInstancesRequestRequestTypeDef = TypedDict(
    "DescribeRecoveryInstancesRequestRequestTypeDef",
    {
        "filters": "DescribeRecoveryInstancesRequestFiltersTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeRecoveryInstancesResponseTypeDef = TypedDict(
    "DescribeRecoveryInstancesResponseTypeDef",
    {
        "items": List["RecoveryInstanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecoverySnapshotsRequestFiltersTypeDef = TypedDict(
    "DescribeRecoverySnapshotsRequestFiltersTypeDef",
    {
        "fromDateTime": NotRequired[str],
        "toDateTime": NotRequired[str],
    },
)

DescribeRecoverySnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeRecoverySnapshotsRequestRequestTypeDef",
    {
        "sourceServerID": str,
        "filters": NotRequired["DescribeRecoverySnapshotsRequestFiltersTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "order": NotRequired[RecoverySnapshotsOrderType],
    },
)

DescribeRecoverySnapshotsResponseTypeDef = TypedDict(
    "DescribeRecoverySnapshotsResponseTypeDef",
    {
        "items": List["RecoverySnapshotTypeDef"],
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
        "hardwareId": NotRequired[str],
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

DisconnectRecoveryInstanceRequestRequestTypeDef = TypedDict(
    "DisconnectRecoveryInstanceRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

DisconnectSourceServerRequestRequestTypeDef = TypedDict(
    "DisconnectSourceServerRequestRequestTypeDef",
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

GetFailbackReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetFailbackReplicationConfigurationRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

GetFailbackReplicationConfigurationResponseTypeDef = TypedDict(
    "GetFailbackReplicationConfigurationResponseTypeDef",
    {
        "bandwidthThrottling": int,
        "name": str,
        "recoveryInstanceID": str,
        "usePrivateIP": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

LicensingTypeDef = TypedDict(
    "LicensingTypeDef",
    {
        "osByol": NotRequired[bool],
    },
)

LifeCycleLastLaunchInitiatedTypeDef = TypedDict(
    "LifeCycleLastLaunchInitiatedTypeDef",
    {
        "apiCallDateTime": NotRequired[str],
        "jobID": NotRequired[str],
        "type": NotRequired[LastLaunchTypeType],
    },
)

LifeCycleLastLaunchTypeDef = TypedDict(
    "LifeCycleLastLaunchTypeDef",
    {
        "initiated": NotRequired["LifeCycleLastLaunchInitiatedTypeDef"],
    },
)

LifeCycleTypeDef = TypedDict(
    "LifeCycleTypeDef",
    {
        "addedToServiceDateTime": NotRequired[str],
        "elapsedReplicationDuration": NotRequired[str],
        "firstByteDateTime": NotRequired[str],
        "lastLaunch": NotRequired["LifeCycleLastLaunchTypeDef"],
        "lastSeenByServiceDateTime": NotRequired[str],
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

PITPolicyRuleTypeDef = TypedDict(
    "PITPolicyRuleTypeDef",
    {
        "interval": int,
        "retentionDuration": int,
        "units": PITPolicyRuleUnitsType,
        "enabled": NotRequired[bool],
        "ruleID": NotRequired[int],
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
        "recoveryInstanceID": NotRequired[str],
        "sourceServerID": NotRequired[str],
    },
)

RecoveryInstanceDataReplicationErrorTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationErrorTypeDef",
    {
        "error": NotRequired[FailbackReplicationErrorType],
        "rawError": NotRequired[str],
    },
)

RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef",
    {
        "backloggedStorageBytes": NotRequired[int],
        "deviceName": NotRequired[str],
        "replicatedStorageBytes": NotRequired[int],
        "rescannedStorageBytes": NotRequired[int],
        "totalStorageBytes": NotRequired[int],
    },
)

RecoveryInstanceDataReplicationInfoTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInfoTypeDef",
    {
        "dataReplicationError": NotRequired["RecoveryInstanceDataReplicationErrorTypeDef"],
        "dataReplicationInitiation": NotRequired[
            "RecoveryInstanceDataReplicationInitiationTypeDef"
        ],
        "dataReplicationState": NotRequired[RecoveryInstanceDataReplicationStateType],
        "etaDateTime": NotRequired[str],
        "lagDuration": NotRequired[str],
        "replicatedDisks": NotRequired[
            List["RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef"]
        ],
    },
)

RecoveryInstanceDataReplicationInitiationStepTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInitiationStepTypeDef",
    {
        "name": NotRequired[RecoveryInstanceDataReplicationInitiationStepNameType],
        "status": NotRequired[RecoveryInstanceDataReplicationInitiationStepStatusType],
    },
)

RecoveryInstanceDataReplicationInitiationTypeDef = TypedDict(
    "RecoveryInstanceDataReplicationInitiationTypeDef",
    {
        "startDateTime": NotRequired[str],
        "steps": NotRequired[List["RecoveryInstanceDataReplicationInitiationStepTypeDef"]],
    },
)

RecoveryInstanceDiskTypeDef = TypedDict(
    "RecoveryInstanceDiskTypeDef",
    {
        "bytes": NotRequired[int],
        "ebsVolumeID": NotRequired[str],
        "internalDeviceName": NotRequired[str],
    },
)

RecoveryInstanceFailbackTypeDef = TypedDict(
    "RecoveryInstanceFailbackTypeDef",
    {
        "agentLastSeenByServiceDateTime": NotRequired[str],
        "elapsedReplicationDuration": NotRequired[str],
        "failbackClientID": NotRequired[str],
        "failbackClientLastSeenByServiceDateTime": NotRequired[str],
        "failbackInitiationTime": NotRequired[str],
        "failbackJobID": NotRequired[str],
        "failbackToOriginalServer": NotRequired[bool],
        "firstByteDateTime": NotRequired[str],
        "state": NotRequired[FailbackStateType],
    },
)

RecoveryInstancePropertiesTypeDef = TypedDict(
    "RecoveryInstancePropertiesTypeDef",
    {
        "cpus": NotRequired[List["CPUTypeDef"]],
        "disks": NotRequired[List["RecoveryInstanceDiskTypeDef"]],
        "identificationHints": NotRequired["IdentificationHintsTypeDef"],
        "lastUpdatedDateTime": NotRequired[str],
        "networkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
        "os": NotRequired["OSTypeDef"],
        "ramBytes": NotRequired[int],
    },
)

RecoveryInstanceTypeDef = TypedDict(
    "RecoveryInstanceTypeDef",
    {
        "arn": NotRequired[str],
        "dataReplicationInfo": NotRequired["RecoveryInstanceDataReplicationInfoTypeDef"],
        "ec2InstanceID": NotRequired[str],
        "ec2InstanceState": NotRequired[EC2InstanceStateType],
        "failback": NotRequired["RecoveryInstanceFailbackTypeDef"],
        "isDrill": NotRequired[bool],
        "jobID": NotRequired[str],
        "pointInTimeSnapshotDateTime": NotRequired[str],
        "recoveryInstanceID": NotRequired[str],
        "recoveryInstanceProperties": NotRequired["RecoveryInstancePropertiesTypeDef"],
        "sourceServerID": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

RecoverySnapshotTypeDef = TypedDict(
    "RecoverySnapshotTypeDef",
    {
        "expectedTimestamp": str,
        "snapshotID": str,
        "sourceServerID": str,
        "ebsSnapshots": NotRequired[List[str]],
        "timestamp": NotRequired[str],
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
        "pitPolicy": List["PITPolicyRuleTypeDef"],
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
        "pitPolicy": NotRequired[List["PITPolicyRuleTypeDef"]],
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
        "pitPolicy": List["PITPolicyRuleTypeDef"],
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
        "lastLaunchResult": LastLaunchResultType,
        "lifeCycle": "LifeCycleTypeDef",
        "recoveryInstanceId": str,
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceServerTypeDef = TypedDict(
    "SourceServerTypeDef",
    {
        "arn": NotRequired[str],
        "dataReplicationInfo": NotRequired["DataReplicationInfoTypeDef"],
        "lastLaunchResult": NotRequired[LastLaunchResultType],
        "lifeCycle": NotRequired["LifeCycleTypeDef"],
        "recoveryInstanceId": NotRequired[str],
        "sourceProperties": NotRequired["SourcePropertiesTypeDef"],
        "sourceServerID": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

StartFailbackLaunchRequestRequestTypeDef = TypedDict(
    "StartFailbackLaunchRequestRequestTypeDef",
    {
        "recoveryInstanceIDs": Sequence[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartFailbackLaunchResponseTypeDef = TypedDict(
    "StartFailbackLaunchResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRecoveryRequestRequestTypeDef = TypedDict(
    "StartRecoveryRequestRequestTypeDef",
    {
        "sourceServers": Sequence["StartRecoveryRequestSourceServerTypeDef"],
        "isDrill": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartRecoveryRequestSourceServerTypeDef = TypedDict(
    "StartRecoveryRequestSourceServerTypeDef",
    {
        "sourceServerID": str,
        "recoverySnapshotID": NotRequired[str],
    },
)

StartRecoveryResponseTypeDef = TypedDict(
    "StartRecoveryResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFailbackRequestRequestTypeDef = TypedDict(
    "StopFailbackRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TerminateRecoveryInstancesRequestRequestTypeDef = TypedDict(
    "TerminateRecoveryInstancesRequestRequestTypeDef",
    {
        "recoveryInstanceIDs": Sequence[str],
    },
)

TerminateRecoveryInstancesResponseTypeDef = TypedDict(
    "TerminateRecoveryInstancesResponseTypeDef",
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

UpdateFailbackReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateFailbackReplicationConfigurationRequestRequestTypeDef",
    {
        "recoveryInstanceID": str,
        "bandwidthThrottling": NotRequired[int],
        "name": NotRequired[str],
        "usePrivateIP": NotRequired[bool],
    },
)

UpdateLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLaunchConfigurationRequestRequestTypeDef",
    {
        "sourceServerID": str,
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
        "pitPolicy": NotRequired[Sequence["PITPolicyRuleTypeDef"]],
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
        "pitPolicy": NotRequired[Sequence["PITPolicyRuleTypeDef"]],
        "replicationServerInstanceType": NotRequired[str],
        "replicationServersSecurityGroupsIDs": NotRequired[Sequence[str]],
        "stagingAreaSubnetId": NotRequired[str],
        "stagingAreaTags": NotRequired[Mapping[str, str]],
        "useDedicatedReplicationServer": NotRequired[bool],
    },
)
