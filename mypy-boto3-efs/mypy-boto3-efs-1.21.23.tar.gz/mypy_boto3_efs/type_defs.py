"""
Type annotations for efs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_efs.type_defs import AccessPointDescriptionResponseMetadataTypeDef

    data: AccessPointDescriptionResponseMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    LifeCycleStateType,
    PerformanceModeType,
    ReplicationStatusType,
    ResourceIdTypeType,
    ResourceType,
    StatusType,
    ThroughputModeType,
    TransitionToIARulesType,
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
    "AccessPointDescriptionResponseMetadataTypeDef",
    "AccessPointDescriptionTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "BackupPolicyTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateMountTargetRequestRequestTypeDef",
    "CreateReplicationConfigurationRequestRequestTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreationInfoTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteFileSystemPolicyRequestRequestTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteMountTargetRequestRequestTypeDef",
    "DeleteReplicationConfigurationRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DescribeAccessPointsRequestRequestTypeDef",
    "DescribeAccessPointsResponseTypeDef",
    "DescribeAccountPreferencesRequestRequestTypeDef",
    "DescribeAccountPreferencesResponseTypeDef",
    "DescribeBackupPolicyRequestRequestTypeDef",
    "DescribeFileSystemPolicyRequestRequestTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeLifecycleConfigurationRequestRequestTypeDef",
    "DescribeMountTargetSecurityGroupsRequestRequestTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "DescribeMountTargetsRequestRequestTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "DescribeReplicationConfigurationsRequestRequestTypeDef",
    "DescribeReplicationConfigurationsResponseTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "DestinationToCreateTypeDef",
    "DestinationTypeDef",
    "FileSystemDescriptionResponseMetadataTypeDef",
    "FileSystemDescriptionTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "FileSystemSizeTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    "MountTargetDescriptionResponseMetadataTypeDef",
    "MountTargetDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "PosixUserTypeDef",
    "PutAccountPreferencesRequestRequestTypeDef",
    "PutAccountPreferencesResponseTypeDef",
    "PutBackupPolicyRequestRequestTypeDef",
    "PutFileSystemPolicyRequestRequestTypeDef",
    "PutLifecycleConfigurationRequestRequestTypeDef",
    "ReplicationConfigurationDescriptionResponseMetadataTypeDef",
    "ReplicationConfigurationDescriptionTypeDef",
    "ResourceIdPreferenceTypeDef",
    "ResponseMetadataTypeDef",
    "RootDirectoryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
)

AccessPointDescriptionResponseMetadataTypeDef = TypedDict(
    "AccessPointDescriptionResponseMetadataTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List["TagTypeDef"],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": "PosixUserTypeDef",
        "RootDirectory": "RootDirectoryTypeDef",
        "OwnerId": str,
        "LifeCycleState": LifeCycleStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessPointDescriptionTypeDef = TypedDict(
    "AccessPointDescriptionTypeDef",
    {
        "ClientToken": NotRequired[str],
        "Name": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "AccessPointId": NotRequired[str],
        "AccessPointArn": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PosixUser": NotRequired["PosixUserTypeDef"],
        "RootDirectory": NotRequired["RootDirectoryTypeDef"],
        "OwnerId": NotRequired[str],
        "LifeCycleState": NotRequired[LifeCycleStateType],
    },
)

BackupPolicyDescriptionTypeDef = TypedDict(
    "BackupPolicyDescriptionTypeDef",
    {
        "BackupPolicy": "BackupPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupPolicyTypeDef = TypedDict(
    "BackupPolicyTypeDef",
    {
        "Status": StatusType,
    },
)

CreateAccessPointRequestRequestTypeDef = TypedDict(
    "CreateAccessPointRequestRequestTypeDef",
    {
        "ClientToken": str,
        "FileSystemId": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "PosixUser": NotRequired["PosixUserTypeDef"],
        "RootDirectory": NotRequired["RootDirectoryTypeDef"],
    },
)

CreateFileSystemRequestRequestTypeDef = TypedDict(
    "CreateFileSystemRequestRequestTypeDef",
    {
        "CreationToken": str,
        "PerformanceMode": NotRequired[PerformanceModeType],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ThroughputMode": NotRequired[ThroughputModeType],
        "ProvisionedThroughputInMibps": NotRequired[float],
        "AvailabilityZoneName": NotRequired[str],
        "Backup": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMountTargetRequestRequestTypeDef = TypedDict(
    "CreateMountTargetRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "SubnetId": str,
        "IpAddress": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)

CreateReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "CreateReplicationConfigurationRequestRequestTypeDef",
    {
        "SourceFileSystemId": str,
        "Destinations": Sequence["DestinationToCreateTypeDef"],
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

CreationInfoTypeDef = TypedDict(
    "CreationInfoTypeDef",
    {
        "OwnerUid": int,
        "OwnerGid": int,
        "Permissions": str,
    },
)

DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccessPointId": str,
    },
)

DeleteFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DeleteFileSystemRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DeleteMountTargetRequestRequestTypeDef = TypedDict(
    "DeleteMountTargetRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)

DeleteReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationRequestRequestTypeDef",
    {
        "SourceFileSystemId": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "TagKeys": Sequence[str],
    },
)

DescribeAccessPointsRequestRequestTypeDef = TypedDict(
    "DescribeAccessPointsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccessPointId": NotRequired[str],
        "FileSystemId": NotRequired[str],
    },
)

DescribeAccessPointsResponseTypeDef = TypedDict(
    "DescribeAccessPointsResponseTypeDef",
    {
        "AccessPoints": List["AccessPointDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountPreferencesRequestRequestTypeDef = TypedDict(
    "DescribeAccountPreferencesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeAccountPreferencesResponseTypeDef = TypedDict(
    "DescribeAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": "ResourceIdPreferenceTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupPolicyRequestRequestTypeDef = TypedDict(
    "DescribeBackupPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeFileSystemsRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
        "CreationToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
    },
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List["FileSystemDescriptionTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLifecycleConfigurationRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)

DescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMountTargetsRequestRequestTypeDef = TypedDict(
    "DescribeMountTargetsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "MountTargetId": NotRequired[str],
        "AccessPointId": NotRequired[str],
    },
)

DescribeMountTargetsResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List["MountTargetDescriptionTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeReplicationConfigurationsRequestRequestTypeDef",
    {
        "FileSystemId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeReplicationConfigurationsResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationsResponseTypeDef",
    {
        "Replications": List["ReplicationConfigurationDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationToCreateTypeDef = TypedDict(
    "DestinationToCreateTypeDef",
    {
        "Region": NotRequired[str],
        "AvailabilityZoneName": NotRequired[str],
        "KmsKeyId": NotRequired[str],
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Status": ReplicationStatusType,
        "FileSystemId": str,
        "Region": str,
        "LastReplicatedTimestamp": NotRequired[datetime],
    },
)

FileSystemDescriptionResponseMetadataTypeDef = TypedDict(
    "FileSystemDescriptionResponseMetadataTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "FileSystemArn": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": "FileSystemSizeTypeDef",
        "PerformanceMode": PerformanceModeType,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "AvailabilityZoneId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileSystemDescriptionTypeDef = TypedDict(
    "FileSystemDescriptionTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "NumberOfMountTargets": int,
        "SizeInBytes": "FileSystemSizeTypeDef",
        "PerformanceMode": PerformanceModeType,
        "Tags": List["TagTypeDef"],
        "FileSystemArn": NotRequired[str],
        "Name": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ThroughputMode": NotRequired[ThroughputModeType],
        "ProvisionedThroughputInMibps": NotRequired[float],
        "AvailabilityZoneName": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
    },
)

FileSystemPolicyDescriptionTypeDef = TypedDict(
    "FileSystemPolicyDescriptionTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileSystemSizeTypeDef = TypedDict(
    "FileSystemSizeTypeDef",
    {
        "Value": int,
        "Timestamp": NotRequired[datetime],
        "ValueInIA": NotRequired[int],
        "ValueInStandard": NotRequired[int],
    },
)

LifecycleConfigurationDescriptionTypeDef = TypedDict(
    "LifecycleConfigurationDescriptionTypeDef",
    {
        "LifecyclePolicies": List["LifecyclePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "TransitionToIA": NotRequired[TransitionToIARulesType],
        "TransitionToPrimaryStorageClass": NotRequired[Literal["AFTER_1_ACCESS"]],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "ModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "MountTargetId": str,
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)

MountTargetDescriptionResponseMetadataTypeDef = TypedDict(
    "MountTargetDescriptionResponseMetadataTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MountTargetDescriptionTypeDef = TypedDict(
    "MountTargetDescriptionTypeDef",
    {
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
        "OwnerId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailabilityZoneName": NotRequired[str],
        "VpcId": NotRequired[str],
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

PosixUserTypeDef = TypedDict(
    "PosixUserTypeDef",
    {
        "Uid": int,
        "Gid": int,
        "SecondaryGids": NotRequired[Sequence[int]],
    },
)

PutAccountPreferencesRequestRequestTypeDef = TypedDict(
    "PutAccountPreferencesRequestRequestTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
    },
)

PutAccountPreferencesResponseTypeDef = TypedDict(
    "PutAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": "ResourceIdPreferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBackupPolicyRequestRequestTypeDef = TypedDict(
    "PutBackupPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "BackupPolicy": "BackupPolicyTypeDef",
    },
)

PutFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "PutFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
    },
)

PutLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "PutLifecycleConfigurationRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "LifecyclePolicies": Sequence["LifecyclePolicyTypeDef"],
    },
)

ReplicationConfigurationDescriptionResponseMetadataTypeDef = TypedDict(
    "ReplicationConfigurationDescriptionResponseMetadataTypeDef",
    {
        "SourceFileSystemId": str,
        "SourceFileSystemRegion": str,
        "SourceFileSystemArn": str,
        "OriginalSourceFileSystemArn": str,
        "CreationTime": datetime,
        "Destinations": List["DestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationConfigurationDescriptionTypeDef = TypedDict(
    "ReplicationConfigurationDescriptionTypeDef",
    {
        "SourceFileSystemId": str,
        "SourceFileSystemRegion": str,
        "SourceFileSystemArn": str,
        "OriginalSourceFileSystemArn": str,
        "CreationTime": datetime,
        "Destinations": List["DestinationTypeDef"],
    },
)

ResourceIdPreferenceTypeDef = TypedDict(
    "ResourceIdPreferenceTypeDef",
    {
        "ResourceIdType": NotRequired[ResourceIdTypeType],
        "Resources": NotRequired[List[ResourceType]],
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

RootDirectoryTypeDef = TypedDict(
    "RootDirectoryTypeDef",
    {
        "Path": NotRequired[str],
        "CreationInfo": NotRequired["CreationInfoTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)

UpdateFileSystemRequestRequestTypeDef = TypedDict(
    "UpdateFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ThroughputMode": NotRequired[ThroughputModeType],
        "ProvisionedThroughputInMibps": NotRequired[float],
    },
)
