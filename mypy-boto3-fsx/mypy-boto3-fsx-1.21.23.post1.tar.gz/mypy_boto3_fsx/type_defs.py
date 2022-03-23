"""
Type annotations for fsx service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef

    data: ActiveDirectoryBackupAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdministrativeActionTypeType,
    AliasLifecycleType,
    AutoImportPolicyTypeType,
    BackupLifecycleType,
    BackupTypeType,
    DataCompressionTypeType,
    DataRepositoryLifecycleType,
    DataRepositoryTaskFilterNameType,
    DataRepositoryTaskLifecycleType,
    DataRepositoryTaskTypeType,
    DiskIopsConfigurationModeType,
    DriveCacheTypeType,
    EventTypeType,
    FileSystemLifecycleType,
    FileSystemMaintenanceOperationType,
    FileSystemTypeType,
    FilterNameType,
    FlexCacheEndpointTypeType,
    LustreAccessAuditLogLevelType,
    LustreDeploymentTypeType,
    OntapVolumeTypeType,
    OpenZFSCopyStrategyType,
    OpenZFSDataCompressionTypeType,
    OpenZFSQuotaTypeType,
    ResourceTypeType,
    RestoreOpenZFSVolumeOptionType,
    SecurityStyleType,
    SnapshotFilterNameType,
    SnapshotLifecycleType,
    StatusType,
    StorageTypeType,
    StorageVirtualMachineLifecycleType,
    StorageVirtualMachineRootVolumeSecurityStyleType,
    StorageVirtualMachineSubtypeType,
    TieringPolicyNameType,
    VolumeFilterNameType,
    VolumeLifecycleType,
    VolumeTypeType,
    WindowsAccessAuditLogLevelType,
    WindowsDeploymentTypeType,
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
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionTypeDef",
    "AliasTypeDef",
    "AssociateFileSystemAliasesRequestRequestTypeDef",
    "AssociateFileSystemAliasesResponseTypeDef",
    "AutoExportPolicyTypeDef",
    "AutoImportPolicyTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupRequestRequestTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryAssociationRequestRequestTypeDef",
    "CreateDataRepositoryAssociationResponseTypeDef",
    "CreateDataRepositoryTaskRequestRequestTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileSystemFromBackupRequestRequestTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemOntapConfigurationTypeDef",
    "CreateFileSystemOpenZFSConfigurationTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "CreateOntapVolumeConfigurationTypeDef",
    "CreateOpenZFSOriginSnapshotConfigurationTypeDef",
    "CreateOpenZFSVolumeConfigurationTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateStorageVirtualMachineRequestRequestTypeDef",
    "CreateStorageVirtualMachineResponseTypeDef",
    "CreateSvmActiveDirectoryConfigurationTypeDef",
    "CreateVolumeFromBackupRequestRequestTypeDef",
    "CreateVolumeFromBackupResponseTypeDef",
    "CreateVolumeRequestRequestTypeDef",
    "CreateVolumeResponseTypeDef",
    "DataRepositoryAssociationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteDataRepositoryAssociationRequestRequestTypeDef",
    "DeleteDataRepositoryAssociationResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemOpenZFSConfigurationTypeDef",
    "DeleteFileSystemOpenZFSResponseTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteStorageVirtualMachineRequestRequestTypeDef",
    "DeleteStorageVirtualMachineResponseTypeDef",
    "DeleteVolumeOntapConfigurationTypeDef",
    "DeleteVolumeOntapResponseTypeDef",
    "DeleteVolumeOpenZFSConfigurationTypeDef",
    "DeleteVolumeRequestRequestTypeDef",
    "DeleteVolumeResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryAssociationsRequestRequestTypeDef",
    "DescribeDataRepositoryAssociationsResponseTypeDef",
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileSystemAliasesRequestRequestTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResponseTypeDef",
    "DescribeStorageVirtualMachinesRequestRequestTypeDef",
    "DescribeStorageVirtualMachinesResponseTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVolumesResponseTypeDef",
    "DisassociateFileSystemAliasesRequestRequestTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "DiskIopsConfigurationTypeDef",
    "FileSystemEndpointTypeDef",
    "FileSystemEndpointsTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "LifecycleTransitionReasonTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "LustreLogConfigurationTypeDef",
    "LustreLogCreateConfigurationTypeDef",
    "OntapFileSystemConfigurationTypeDef",
    "OntapVolumeConfigurationTypeDef",
    "OpenZFSClientConfigurationTypeDef",
    "OpenZFSCreateRootVolumeConfigurationTypeDef",
    "OpenZFSFileSystemConfigurationTypeDef",
    "OpenZFSNfsExportTypeDef",
    "OpenZFSOriginSnapshotConfigurationTypeDef",
    "OpenZFSUserOrGroupQuotaTypeDef",
    "OpenZFSVolumeConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ReleaseFileSystemNfsV3LocksRequestRequestTypeDef",
    "ReleaseFileSystemNfsV3LocksResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreVolumeFromSnapshotRequestRequestTypeDef",
    "RestoreVolumeFromSnapshotResponseTypeDef",
    "S3DataRepositoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "SnapshotFilterTypeDef",
    "SnapshotTypeDef",
    "StorageVirtualMachineFilterTypeDef",
    "StorageVirtualMachineTypeDef",
    "SvmActiveDirectoryConfigurationTypeDef",
    "SvmEndpointTypeDef",
    "SvmEndpointsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TieringPolicyTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataRepositoryAssociationRequestRequestTypeDef",
    "UpdateDataRepositoryAssociationResponseTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemOntapConfigurationTypeDef",
    "UpdateFileSystemOpenZFSConfigurationTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
    "UpdateOntapVolumeConfigurationTypeDef",
    "UpdateOpenZFSVolumeConfigurationTypeDef",
    "UpdateSnapshotRequestRequestTypeDef",
    "UpdateSnapshotResponseTypeDef",
    "UpdateStorageVirtualMachineRequestRequestTypeDef",
    "UpdateStorageVirtualMachineResponseTypeDef",
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    "UpdateVolumeRequestRequestTypeDef",
    "UpdateVolumeResponseTypeDef",
    "VolumeFilterTypeDef",
    "VolumeTypeDef",
    "WindowsAuditLogConfigurationTypeDef",
    "WindowsAuditLogCreateConfigurationTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
)

ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {
        "DomainName": NotRequired[str],
        "ActiveDirectoryId": NotRequired[str],
        "ResourceARN": NotRequired[str],
    },
)

AdministrativeActionFailureDetailsTypeDef = TypedDict(
    "AdministrativeActionFailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
    },
)

AdministrativeActionTypeDef = TypedDict(
    "AdministrativeActionTypeDef",
    {
        "AdministrativeActionType": NotRequired[AdministrativeActionTypeType],
        "ProgressPercent": NotRequired[int],
        "RequestTime": NotRequired[datetime],
        "Status": NotRequired[StatusType],
        "TargetFileSystemValues": NotRequired[Dict[str, Any]],
        "FailureDetails": NotRequired["AdministrativeActionFailureDetailsTypeDef"],
        "TargetVolumeValues": NotRequired[Dict[str, Any]],
        "TargetSnapshotValues": NotRequired[Dict[str, Any]],
    },
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": NotRequired[str],
        "Lifecycle": NotRequired[AliasLifecycleType],
    },
)

AssociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "AssociateFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": Sequence[str],
        "ClientRequestToken": NotRequired[str],
    },
)

AssociateFileSystemAliasesResponseTypeDef = TypedDict(
    "AssociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoExportPolicyTypeDef = TypedDict(
    "AutoExportPolicyTypeDef",
    {
        "Events": NotRequired[Sequence[EventTypeType]],
    },
)

AutoImportPolicyTypeDef = TypedDict(
    "AutoImportPolicyTypeDef",
    {
        "Events": NotRequired[Sequence[EventTypeType]],
    },
)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
    },
)

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "Type": BackupTypeType,
        "CreationTime": datetime,
        "FileSystem": "FileSystemTypeDef",
        "FailureDetails": NotRequired["BackupFailureDetailsTypeDef"],
        "ProgressPercent": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "DirectoryInformation": NotRequired["ActiveDirectoryBackupAttributesTypeDef"],
        "OwnerId": NotRequired[str],
        "SourceBackupId": NotRequired[str],
        "SourceBackupRegion": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "Volume": NotRequired["VolumeTypeDef"],
    },
)

CancelDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "CancelDataRepositoryTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)

CancelDataRepositoryTaskResponseTypeDef = TypedDict(
    "CancelDataRepositoryTaskResponseTypeDef",
    {
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "TaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompletionReportTypeDef = TypedDict(
    "CompletionReportTypeDef",
    {
        "Enabled": bool,
        "Path": NotRequired[str],
        "Format": NotRequired[Literal["REPORT_CSV_20191124"]],
        "Scope": NotRequired[Literal["FAILED_FILES_ONLY"]],
    },
)

CopyBackupRequestRequestTypeDef = TypedDict(
    "CopyBackupRequestRequestTypeDef",
    {
        "SourceBackupId": str,
        "ClientRequestToken": NotRequired[str],
        "SourceRegion": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopyBackupResponseTypeDef = TypedDict(
    "CopyBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackupRequestRequestTypeDef = TypedDict(
    "CreateBackupRequestRequestTypeDef",
    {
        "FileSystemId": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "VolumeId": NotRequired[str],
    },
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "CreateDataRepositoryAssociationRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "FileSystemPath": str,
        "DataRepositoryPath": str,
        "BatchImportMetaDataOnCreate": NotRequired[bool],
        "ImportedFileChunkSize": NotRequired[int],
        "S3": NotRequired["S3DataRepositoryConfigurationTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDataRepositoryAssociationResponseTypeDef = TypedDict(
    "CreateDataRepositoryAssociationResponseTypeDef",
    {
        "Association": "DataRepositoryAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataRepositoryTaskRequestRequestTypeDef = TypedDict(
    "CreateDataRepositoryTaskRequestRequestTypeDef",
    {
        "Type": DataRepositoryTaskTypeType,
        "FileSystemId": str,
        "Report": "CompletionReportTypeDef",
        "Paths": NotRequired[Sequence[str]],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDataRepositoryTaskResponseTypeDef = TypedDict(
    "CreateDataRepositoryTaskResponseTypeDef",
    {
        "DataRepositoryTask": "DataRepositoryTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFileSystemFromBackupRequestRequestTypeDef = TypedDict(
    "CreateFileSystemFromBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "SubnetIds": Sequence[str],
        "ClientRequestToken": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "WindowsConfiguration": NotRequired["CreateFileSystemWindowsConfigurationTypeDef"],
        "LustreConfiguration": NotRequired["CreateFileSystemLustreConfigurationTypeDef"],
        "StorageType": NotRequired[StorageTypeType],
        "KmsKeyId": NotRequired[str],
        "FileSystemTypeVersion": NotRequired[str],
        "OpenZFSConfiguration": NotRequired["CreateFileSystemOpenZFSConfigurationTypeDef"],
    },
)

CreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "CreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "ImportPath": NotRequired[str],
        "ExportPath": NotRequired[str],
        "ImportedFileChunkSize": NotRequired[int],
        "DeploymentType": NotRequired[LustreDeploymentTypeType],
        "AutoImportPolicy": NotRequired[AutoImportPolicyTypeType],
        "PerUnitStorageThroughput": NotRequired[int],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "DriveCacheType": NotRequired[DriveCacheTypeType],
        "DataCompressionType": NotRequired[DataCompressionTypeType],
        "LogConfiguration": NotRequired["LustreLogCreateConfigurationTypeDef"],
    },
)

CreateFileSystemOntapConfigurationTypeDef = TypedDict(
    "CreateFileSystemOntapConfigurationTypeDef",
    {
        "DeploymentType": Literal["MULTI_AZ_1"],
        "ThroughputCapacity": int,
        "AutomaticBackupRetentionDays": NotRequired[int],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "EndpointIpAddressRange": NotRequired[str],
        "FsxAdminPassword": NotRequired[str],
        "DiskIopsConfiguration": NotRequired["DiskIopsConfigurationTypeDef"],
        "PreferredSubnetId": NotRequired[str],
        "RouteTableIds": NotRequired[Sequence[str]],
        "WeeklyMaintenanceStartTime": NotRequired[str],
    },
)

CreateFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "CreateFileSystemOpenZFSConfigurationTypeDef",
    {
        "DeploymentType": Literal["SINGLE_AZ_1"],
        "ThroughputCapacity": int,
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "CopyTagsToVolumes": NotRequired[bool],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DiskIopsConfiguration": NotRequired["DiskIopsConfigurationTypeDef"],
        "RootVolumeConfiguration": NotRequired["OpenZFSCreateRootVolumeConfigurationTypeDef"],
    },
)

CreateFileSystemRequestRequestTypeDef = TypedDict(
    "CreateFileSystemRequestRequestTypeDef",
    {
        "FileSystemType": FileSystemTypeType,
        "StorageCapacity": int,
        "SubnetIds": Sequence[str],
        "ClientRequestToken": NotRequired[str],
        "StorageType": NotRequired[StorageTypeType],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "WindowsConfiguration": NotRequired["CreateFileSystemWindowsConfigurationTypeDef"],
        "LustreConfiguration": NotRequired["CreateFileSystemLustreConfigurationTypeDef"],
        "OntapConfiguration": NotRequired["CreateFileSystemOntapConfigurationTypeDef"],
        "FileSystemTypeVersion": NotRequired[str],
        "OpenZFSConfiguration": NotRequired["CreateFileSystemOpenZFSConfigurationTypeDef"],
    },
)

CreateFileSystemResponseTypeDef = TypedDict(
    "CreateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "CreateFileSystemWindowsConfigurationTypeDef",
    {
        "ThroughputCapacity": int,
        "ActiveDirectoryId": NotRequired[str],
        "SelfManagedActiveDirectoryConfiguration": NotRequired[
            "SelfManagedActiveDirectoryConfigurationTypeDef"
        ],
        "DeploymentType": NotRequired[WindowsDeploymentTypeType],
        "PreferredSubnetId": NotRequired[str],
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "Aliases": NotRequired[Sequence[str]],
        "AuditLogConfiguration": NotRequired["WindowsAuditLogCreateConfigurationTypeDef"],
    },
)

CreateOntapVolumeConfigurationTypeDef = TypedDict(
    "CreateOntapVolumeConfigurationTypeDef",
    {
        "JunctionPath": str,
        "SizeInMegabytes": int,
        "StorageEfficiencyEnabled": bool,
        "StorageVirtualMachineId": str,
        "SecurityStyle": NotRequired[SecurityStyleType],
        "TieringPolicy": NotRequired["TieringPolicyTypeDef"],
    },
)

CreateOpenZFSOriginSnapshotConfigurationTypeDef = TypedDict(
    "CreateOpenZFSOriginSnapshotConfigurationTypeDef",
    {
        "SnapshotARN": str,
        "CopyStrategy": OpenZFSCopyStrategyType,
    },
)

CreateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "CreateOpenZFSVolumeConfigurationTypeDef",
    {
        "ParentVolumeId": str,
        "StorageCapacityReservationGiB": NotRequired[int],
        "StorageCapacityQuotaGiB": NotRequired[int],
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "CopyTagsToSnapshots": NotRequired[bool],
        "OriginSnapshot": NotRequired["CreateOpenZFSOriginSnapshotConfigurationTypeDef"],
        "ReadOnly": NotRequired[bool],
        "NfsExports": NotRequired[Sequence["OpenZFSNfsExportTypeDef"]],
        "UserAndGroupQuotas": NotRequired[Sequence["OpenZFSUserOrGroupQuotaTypeDef"]],
    },
)

CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "Name": str,
        "VolumeId": str,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSnapshotResponseTypeDef = TypedDict(
    "CreateSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "CreateStorageVirtualMachineRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Name": str,
        "ActiveDirectoryConfiguration": NotRequired["CreateSvmActiveDirectoryConfigurationTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "SvmAdminPassword": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "RootVolumeSecurityStyle": NotRequired[StorageVirtualMachineRootVolumeSecurityStyleType],
    },
)

CreateStorageVirtualMachineResponseTypeDef = TypedDict(
    "CreateStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachine": "StorageVirtualMachineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "CreateSvmActiveDirectoryConfigurationTypeDef",
    {
        "NetBiosName": str,
        "SelfManagedActiveDirectoryConfiguration": NotRequired[
            "SelfManagedActiveDirectoryConfigurationTypeDef"
        ],
    },
)

CreateVolumeFromBackupRequestRequestTypeDef = TypedDict(
    "CreateVolumeFromBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "Name": str,
        "ClientRequestToken": NotRequired[str],
        "OntapConfiguration": NotRequired["CreateOntapVolumeConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateVolumeFromBackupResponseTypeDef = TypedDict(
    "CreateVolumeFromBackupResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVolumeRequestRequestTypeDef = TypedDict(
    "CreateVolumeRequestRequestTypeDef",
    {
        "VolumeType": VolumeTypeType,
        "Name": str,
        "ClientRequestToken": NotRequired[str],
        "OntapConfiguration": NotRequired["CreateOntapVolumeConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "OpenZFSConfiguration": NotRequired["CreateOpenZFSVolumeConfigurationTypeDef"],
    },
)

CreateVolumeResponseTypeDef = TypedDict(
    "CreateVolumeResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataRepositoryAssociationTypeDef = TypedDict(
    "DataRepositoryAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "Lifecycle": NotRequired[DataRepositoryLifecycleType],
        "FailureDetails": NotRequired["DataRepositoryFailureDetailsTypeDef"],
        "FileSystemPath": NotRequired[str],
        "DataRepositoryPath": NotRequired[str],
        "BatchImportMetaDataOnCreate": NotRequired[bool],
        "ImportedFileChunkSize": NotRequired[int],
        "S3": NotRequired["S3DataRepositoryConfigurationTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "CreationTime": NotRequired[datetime],
    },
)

DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {
        "Lifecycle": NotRequired[DataRepositoryLifecycleType],
        "ImportPath": NotRequired[str],
        "ExportPath": NotRequired[str],
        "ImportedFileChunkSize": NotRequired[int],
        "AutoImportPolicy": NotRequired[AutoImportPolicyTypeType],
        "FailureDetails": NotRequired["DataRepositoryFailureDetailsTypeDef"],
    },
)

DataRepositoryFailureDetailsTypeDef = TypedDict(
    "DataRepositoryFailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
    },
)

DataRepositoryTaskFailureDetailsTypeDef = TypedDict(
    "DataRepositoryTaskFailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
    },
)

DataRepositoryTaskFilterTypeDef = TypedDict(
    "DataRepositoryTaskFilterTypeDef",
    {
        "Name": NotRequired[DataRepositoryTaskFilterNameType],
        "Values": NotRequired[Sequence[str]],
    },
)

DataRepositoryTaskStatusTypeDef = TypedDict(
    "DataRepositoryTaskStatusTypeDef",
    {
        "TotalCount": NotRequired[int],
        "SucceededCount": NotRequired[int],
        "FailedCount": NotRequired[int],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

DataRepositoryTaskTypeDef = TypedDict(
    "DataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "Type": DataRepositoryTaskTypeType,
        "CreationTime": datetime,
        "FileSystemId": str,
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Paths": NotRequired[List[str]],
        "FailureDetails": NotRequired["DataRepositoryTaskFailureDetailsTypeDef"],
        "Status": NotRequired["DataRepositoryTaskStatusTypeDef"],
        "Report": NotRequired["CompletionReportTypeDef"],
    },
)

DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
        "ClientRequestToken": NotRequired[str],
    },
)

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "DeleteDataRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "DeleteDataInFileSystem": bool,
        "ClientRequestToken": NotRequired[str],
    },
)

DeleteDataRepositoryAssociationResponseTypeDef = TypedDict(
    "DeleteDataRepositoryAssociationResponseTypeDef",
    {
        "AssociationId": str,
        "Lifecycle": DataRepositoryLifecycleType,
        "DeleteDataInFileSystem": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemLustreConfigurationTypeDef = TypedDict(
    "DeleteFileSystemLustreConfigurationTypeDef",
    {
        "SkipFinalBackup": NotRequired[bool],
        "FinalBackupTags": NotRequired[Sequence["TagTypeDef"]],
    },
)

DeleteFileSystemLustreResponseTypeDef = TypedDict(
    "DeleteFileSystemLustreResponseTypeDef",
    {
        "FinalBackupId": NotRequired[str],
        "FinalBackupTags": NotRequired[List["TagTypeDef"]],
    },
)

DeleteFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "DeleteFileSystemOpenZFSConfigurationTypeDef",
    {
        "SkipFinalBackup": NotRequired[bool],
        "FinalBackupTags": NotRequired[Sequence["TagTypeDef"]],
        "Options": NotRequired[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]],
    },
)

DeleteFileSystemOpenZFSResponseTypeDef = TypedDict(
    "DeleteFileSystemOpenZFSResponseTypeDef",
    {
        "FinalBackupId": NotRequired[str],
        "FinalBackupTags": NotRequired[List["TagTypeDef"]],
    },
)

DeleteFileSystemRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ClientRequestToken": NotRequired[str],
        "WindowsConfiguration": NotRequired["DeleteFileSystemWindowsConfigurationTypeDef"],
        "LustreConfiguration": NotRequired["DeleteFileSystemLustreConfigurationTypeDef"],
        "OpenZFSConfiguration": NotRequired["DeleteFileSystemOpenZFSConfigurationTypeDef"],
    },
)

DeleteFileSystemResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": FileSystemLifecycleType,
        "WindowsResponse": "DeleteFileSystemWindowsResponseTypeDef",
        "LustreResponse": "DeleteFileSystemLustreResponseTypeDef",
        "OpenZFSResponse": "DeleteFileSystemOpenZFSResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": NotRequired[bool],
        "FinalBackupTags": NotRequired[Sequence["TagTypeDef"]],
    },
)

DeleteFileSystemWindowsResponseTypeDef = TypedDict(
    "DeleteFileSystemWindowsResponseTypeDef",
    {
        "FinalBackupId": NotRequired[str],
        "FinalBackupTags": NotRequired[List["TagTypeDef"]],
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "ClientRequestToken": NotRequired[str],
    },
)

DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "SnapshotId": str,
        "Lifecycle": SnapshotLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "DeleteStorageVirtualMachineRequestRequestTypeDef",
    {
        "StorageVirtualMachineId": str,
        "ClientRequestToken": NotRequired[str],
    },
)

DeleteStorageVirtualMachineResponseTypeDef = TypedDict(
    "DeleteStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachineId": str,
        "Lifecycle": StorageVirtualMachineLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeOntapConfigurationTypeDef = TypedDict(
    "DeleteVolumeOntapConfigurationTypeDef",
    {
        "SkipFinalBackup": NotRequired[bool],
        "FinalBackupTags": NotRequired[Sequence["TagTypeDef"]],
    },
)

DeleteVolumeOntapResponseTypeDef = TypedDict(
    "DeleteVolumeOntapResponseTypeDef",
    {
        "FinalBackupId": NotRequired[str],
        "FinalBackupTags": NotRequired[List["TagTypeDef"]],
    },
)

DeleteVolumeOpenZFSConfigurationTypeDef = TypedDict(
    "DeleteVolumeOpenZFSConfigurationTypeDef",
    {
        "Options": NotRequired[Sequence[Literal["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS"]]],
    },
)

DeleteVolumeRequestRequestTypeDef = TypedDict(
    "DeleteVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "ClientRequestToken": NotRequired[str],
        "OntapConfiguration": NotRequired["DeleteVolumeOntapConfigurationTypeDef"],
        "OpenZFSConfiguration": NotRequired["DeleteVolumeOpenZFSConfigurationTypeDef"],
    },
)

DeleteVolumeResponseTypeDef = TypedDict(
    "DeleteVolumeResponseTypeDef",
    {
        "VolumeId": str,
        "Lifecycle": VolumeLifecycleType,
        "OntapResponse": "DeleteVolumeOntapResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "BackupIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataRepositoryAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeDataRepositoryAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeDataRepositoryAssociationsResponseTypeDef = TypedDict(
    "DescribeDataRepositoryAssociationsResponseTypeDef",
    {
        "Associations": List["DataRepositoryAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataRepositoryTasksRequestRequestTypeDef = TypedDict(
    "DescribeDataRepositoryTasksRequestRequestTypeDef",
    {
        "TaskIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["DataRepositoryTaskFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeDataRepositoryTasksResponseTypeDef = TypedDict(
    "DescribeDataRepositoryTasksResponseTypeDef",
    {
        "DataRepositoryTasks": List["DataRepositoryTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ClientRequestToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFileSystemAliasesResponseTypeDef = TypedDict(
    "DescribeFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemsRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestRequestTypeDef",
    {
        "FileSystemIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "FileSystems": List["FileSystemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "SnapshotIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["SnapshotFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeSnapshotsResponseTypeDef = TypedDict(
    "DescribeSnapshotsResponseTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorageVirtualMachinesRequestRequestTypeDef = TypedDict(
    "DescribeStorageVirtualMachinesRequestRequestTypeDef",
    {
        "StorageVirtualMachineIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["StorageVirtualMachineFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeStorageVirtualMachinesResponseTypeDef = TypedDict(
    "DescribeStorageVirtualMachinesResponseTypeDef",
    {
        "StorageVirtualMachines": List["StorageVirtualMachineTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "VolumeIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["VolumeFilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeVolumesResponseTypeDef = TypedDict(
    "DescribeVolumesResponseTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateFileSystemAliasesRequestRequestTypeDef = TypedDict(
    "DisassociateFileSystemAliasesRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": Sequence[str],
        "ClientRequestToken": NotRequired[str],
    },
)

DisassociateFileSystemAliasesResponseTypeDef = TypedDict(
    "DisassociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskIopsConfigurationTypeDef = TypedDict(
    "DiskIopsConfigurationTypeDef",
    {
        "Mode": NotRequired[DiskIopsConfigurationModeType],
        "Iops": NotRequired[int],
    },
)

FileSystemEndpointTypeDef = TypedDict(
    "FileSystemEndpointTypeDef",
    {
        "DNSName": NotRequired[str],
        "IpAddresses": NotRequired[List[str]],
    },
)

FileSystemEndpointsTypeDef = TypedDict(
    "FileSystemEndpointsTypeDef",
    {
        "Intercluster": NotRequired["FileSystemEndpointTypeDef"],
        "Management": NotRequired["FileSystemEndpointTypeDef"],
    },
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
    },
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "FileSystemId": NotRequired[str],
        "FileSystemType": NotRequired[FileSystemTypeType],
        "Lifecycle": NotRequired[FileSystemLifecycleType],
        "FailureDetails": NotRequired["FileSystemFailureDetailsTypeDef"],
        "StorageCapacity": NotRequired[int],
        "StorageType": NotRequired[StorageTypeType],
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "NetworkInterfaceIds": NotRequired[List[str]],
        "DNSName": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "WindowsConfiguration": NotRequired["WindowsFileSystemConfigurationTypeDef"],
        "LustreConfiguration": NotRequired["LustreFileSystemConfigurationTypeDef"],
        "AdministrativeActions": NotRequired[List[Dict[str, Any]]],
        "OntapConfiguration": NotRequired["OntapFileSystemConfigurationTypeDef"],
        "FileSystemTypeVersion": NotRequired[str],
        "OpenZFSConfiguration": NotRequired["OpenZFSFileSystemConfigurationTypeDef"],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[FilterNameType],
        "Values": NotRequired[Sequence[str]],
    },
)

LifecycleTransitionReasonTypeDef = TypedDict(
    "LifecycleTransitionReasonTypeDef",
    {
        "Message": NotRequired[str],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DataRepositoryConfiguration": NotRequired["DataRepositoryConfigurationTypeDef"],
        "DeploymentType": NotRequired[LustreDeploymentTypeType],
        "PerUnitStorageThroughput": NotRequired[int],
        "MountName": NotRequired[str],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "DriveCacheType": NotRequired[DriveCacheTypeType],
        "DataCompressionType": NotRequired[DataCompressionTypeType],
        "LogConfiguration": NotRequired["LustreLogConfigurationTypeDef"],
    },
)

LustreLogConfigurationTypeDef = TypedDict(
    "LustreLogConfigurationTypeDef",
    {
        "Level": LustreAccessAuditLogLevelType,
        "Destination": NotRequired[str],
    },
)

LustreLogCreateConfigurationTypeDef = TypedDict(
    "LustreLogCreateConfigurationTypeDef",
    {
        "Level": LustreAccessAuditLogLevelType,
        "Destination": NotRequired[str],
    },
)

OntapFileSystemConfigurationTypeDef = TypedDict(
    "OntapFileSystemConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": NotRequired[int],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "DeploymentType": NotRequired[Literal["MULTI_AZ_1"]],
        "EndpointIpAddressRange": NotRequired[str],
        "Endpoints": NotRequired["FileSystemEndpointsTypeDef"],
        "DiskIopsConfiguration": NotRequired["DiskIopsConfigurationTypeDef"],
        "PreferredSubnetId": NotRequired[str],
        "RouteTableIds": NotRequired[List[str]],
        "ThroughputCapacity": NotRequired[int],
        "WeeklyMaintenanceStartTime": NotRequired[str],
    },
)

OntapVolumeConfigurationTypeDef = TypedDict(
    "OntapVolumeConfigurationTypeDef",
    {
        "FlexCacheEndpointType": NotRequired[FlexCacheEndpointTypeType],
        "JunctionPath": NotRequired[str],
        "SecurityStyle": NotRequired[SecurityStyleType],
        "SizeInMegabytes": NotRequired[int],
        "StorageEfficiencyEnabled": NotRequired[bool],
        "StorageVirtualMachineId": NotRequired[str],
        "StorageVirtualMachineRoot": NotRequired[bool],
        "TieringPolicy": NotRequired["TieringPolicyTypeDef"],
        "UUID": NotRequired[str],
        "OntapVolumeType": NotRequired[OntapVolumeTypeType],
    },
)

OpenZFSClientConfigurationTypeDef = TypedDict(
    "OpenZFSClientConfigurationTypeDef",
    {
        "Clients": str,
        "Options": List[str],
    },
)

OpenZFSCreateRootVolumeConfigurationTypeDef = TypedDict(
    "OpenZFSCreateRootVolumeConfigurationTypeDef",
    {
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "NfsExports": NotRequired[Sequence["OpenZFSNfsExportTypeDef"]],
        "UserAndGroupQuotas": NotRequired[Sequence["OpenZFSUserOrGroupQuotaTypeDef"]],
        "CopyTagsToSnapshots": NotRequired[bool],
        "ReadOnly": NotRequired[bool],
    },
)

OpenZFSFileSystemConfigurationTypeDef = TypedDict(
    "OpenZFSFileSystemConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "CopyTagsToVolumes": NotRequired[bool],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "DeploymentType": NotRequired[Literal["SINGLE_AZ_1"]],
        "ThroughputCapacity": NotRequired[int],
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DiskIopsConfiguration": NotRequired["DiskIopsConfigurationTypeDef"],
        "RootVolumeId": NotRequired[str],
    },
)

OpenZFSNfsExportTypeDef = TypedDict(
    "OpenZFSNfsExportTypeDef",
    {
        "ClientConfigurations": List["OpenZFSClientConfigurationTypeDef"],
    },
)

OpenZFSOriginSnapshotConfigurationTypeDef = TypedDict(
    "OpenZFSOriginSnapshotConfigurationTypeDef",
    {
        "SnapshotARN": NotRequired[str],
        "CopyStrategy": NotRequired[OpenZFSCopyStrategyType],
    },
)

OpenZFSUserOrGroupQuotaTypeDef = TypedDict(
    "OpenZFSUserOrGroupQuotaTypeDef",
    {
        "Type": OpenZFSQuotaTypeType,
        "Id": int,
        "StorageCapacityQuotaGiB": int,
    },
)

OpenZFSVolumeConfigurationTypeDef = TypedDict(
    "OpenZFSVolumeConfigurationTypeDef",
    {
        "ParentVolumeId": NotRequired[str],
        "VolumePath": NotRequired[str],
        "StorageCapacityReservationGiB": NotRequired[int],
        "StorageCapacityQuotaGiB": NotRequired[int],
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "CopyTagsToSnapshots": NotRequired[bool],
        "OriginSnapshot": NotRequired["OpenZFSOriginSnapshotConfigurationTypeDef"],
        "ReadOnly": NotRequired[bool],
        "NfsExports": NotRequired[List["OpenZFSNfsExportTypeDef"]],
        "UserAndGroupQuotas": NotRequired[List["OpenZFSUserOrGroupQuotaTypeDef"]],
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

ReleaseFileSystemNfsV3LocksRequestRequestTypeDef = TypedDict(
    "ReleaseFileSystemNfsV3LocksRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ClientRequestToken": NotRequired[str],
    },
)

ReleaseFileSystemNfsV3LocksResponseTypeDef = TypedDict(
    "ReleaseFileSystemNfsV3LocksResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
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

RestoreVolumeFromSnapshotRequestRequestTypeDef = TypedDict(
    "RestoreVolumeFromSnapshotRequestRequestTypeDef",
    {
        "VolumeId": str,
        "SnapshotId": str,
        "ClientRequestToken": NotRequired[str],
        "Options": NotRequired[Sequence[RestoreOpenZFSVolumeOptionType]],
    },
)

RestoreVolumeFromSnapshotResponseTypeDef = TypedDict(
    "RestoreVolumeFromSnapshotResponseTypeDef",
    {
        "VolumeId": str,
        "Lifecycle": VolumeLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3DataRepositoryConfigurationTypeDef = TypedDict(
    "S3DataRepositoryConfigurationTypeDef",
    {
        "AutoImportPolicy": NotRequired["AutoImportPolicyTypeDef"],
        "AutoExportPolicy": NotRequired["AutoExportPolicyTypeDef"],
    },
)

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": NotRequired[str],
        "OrganizationalUnitDistinguishedName": NotRequired[str],
        "FileSystemAdministratorsGroup": NotRequired[str],
        "UserName": NotRequired[str],
        "DnsIps": NotRequired[List[str]],
    },
)

SelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "UserName": str,
        "Password": str,
        "DnsIps": Sequence[str],
        "OrganizationalUnitDistinguishedName": NotRequired[str],
        "FileSystemAdministratorsGroup": NotRequired[str],
    },
)

SelfManagedActiveDirectoryConfigurationUpdatesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    {
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
        "DnsIps": NotRequired[Sequence[str]],
    },
)

SnapshotFilterTypeDef = TypedDict(
    "SnapshotFilterTypeDef",
    {
        "Name": NotRequired[SnapshotFilterNameType],
        "Values": NotRequired[Sequence[str]],
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "SnapshotId": NotRequired[str],
        "Name": NotRequired[str],
        "VolumeId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Lifecycle": NotRequired[SnapshotLifecycleType],
        "LifecycleTransitionReason": NotRequired["LifecycleTransitionReasonTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "AdministrativeActions": NotRequired[List["AdministrativeActionTypeDef"]],
    },
)

StorageVirtualMachineFilterTypeDef = TypedDict(
    "StorageVirtualMachineFilterTypeDef",
    {
        "Name": NotRequired[Literal["file-system-id"]],
        "Values": NotRequired[Sequence[str]],
    },
)

StorageVirtualMachineTypeDef = TypedDict(
    "StorageVirtualMachineTypeDef",
    {
        "ActiveDirectoryConfiguration": NotRequired["SvmActiveDirectoryConfigurationTypeDef"],
        "CreationTime": NotRequired[datetime],
        "Endpoints": NotRequired["SvmEndpointsTypeDef"],
        "FileSystemId": NotRequired[str],
        "Lifecycle": NotRequired[StorageVirtualMachineLifecycleType],
        "Name": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "StorageVirtualMachineId": NotRequired[str],
        "Subtype": NotRequired[StorageVirtualMachineSubtypeType],
        "UUID": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "LifecycleTransitionReason": NotRequired["LifecycleTransitionReasonTypeDef"],
        "RootVolumeSecurityStyle": NotRequired[StorageVirtualMachineRootVolumeSecurityStyleType],
    },
)

SvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "SvmActiveDirectoryConfigurationTypeDef",
    {
        "NetBiosName": NotRequired[str],
        "SelfManagedActiveDirectoryConfiguration": NotRequired[
            "SelfManagedActiveDirectoryAttributesTypeDef"
        ],
    },
)

SvmEndpointTypeDef = TypedDict(
    "SvmEndpointTypeDef",
    {
        "DNSName": NotRequired[str],
        "IpAddresses": NotRequired[List[str]],
    },
)

SvmEndpointsTypeDef = TypedDict(
    "SvmEndpointsTypeDef",
    {
        "Iscsi": NotRequired["SvmEndpointTypeDef"],
        "Management": NotRequired["SvmEndpointTypeDef"],
        "Nfs": NotRequired["SvmEndpointTypeDef"],
        "Smb": NotRequired["SvmEndpointTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

TieringPolicyTypeDef = TypedDict(
    "TieringPolicyTypeDef",
    {
        "CoolingPeriod": NotRequired[int],
        "Name": NotRequired[TieringPolicyNameType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDataRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "UpdateDataRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "ClientRequestToken": NotRequired[str],
        "ImportedFileChunkSize": NotRequired[int],
        "S3": NotRequired["S3DataRepositoryConfigurationTypeDef"],
    },
)

UpdateDataRepositoryAssociationResponseTypeDef = TypedDict(
    "UpdateDataRepositoryAssociationResponseTypeDef",
    {
        "Association": "DataRepositoryAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "UpdateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "AutomaticBackupRetentionDays": NotRequired[int],
        "AutoImportPolicy": NotRequired[AutoImportPolicyTypeType],
        "DataCompressionType": NotRequired[DataCompressionTypeType],
        "LogConfiguration": NotRequired["LustreLogCreateConfigurationTypeDef"],
    },
)

UpdateFileSystemOntapConfigurationTypeDef = TypedDict(
    "UpdateFileSystemOntapConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": NotRequired[int],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "FsxAdminPassword": NotRequired[str],
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DiskIopsConfiguration": NotRequired["DiskIopsConfigurationTypeDef"],
    },
)

UpdateFileSystemOpenZFSConfigurationTypeDef = TypedDict(
    "UpdateFileSystemOpenZFSConfigurationTypeDef",
    {
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "CopyTagsToVolumes": NotRequired[bool],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "ThroughputCapacity": NotRequired[int],
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DiskIopsConfiguration": NotRequired["DiskIopsConfigurationTypeDef"],
    },
)

UpdateFileSystemRequestRequestTypeDef = TypedDict(
    "UpdateFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ClientRequestToken": NotRequired[str],
        "StorageCapacity": NotRequired[int],
        "WindowsConfiguration": NotRequired["UpdateFileSystemWindowsConfigurationTypeDef"],
        "LustreConfiguration": NotRequired["UpdateFileSystemLustreConfigurationTypeDef"],
        "OntapConfiguration": NotRequired["UpdateFileSystemOntapConfigurationTypeDef"],
        "OpenZFSConfiguration": NotRequired["UpdateFileSystemOpenZFSConfigurationTypeDef"],
    },
)

UpdateFileSystemResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "UpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "AutomaticBackupRetentionDays": NotRequired[int],
        "ThroughputCapacity": NotRequired[int],
        "SelfManagedActiveDirectoryConfiguration": NotRequired[
            "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"
        ],
        "AuditLogConfiguration": NotRequired["WindowsAuditLogCreateConfigurationTypeDef"],
    },
)

UpdateOntapVolumeConfigurationTypeDef = TypedDict(
    "UpdateOntapVolumeConfigurationTypeDef",
    {
        "JunctionPath": NotRequired[str],
        "SecurityStyle": NotRequired[SecurityStyleType],
        "SizeInMegabytes": NotRequired[int],
        "StorageEfficiencyEnabled": NotRequired[bool],
        "TieringPolicy": NotRequired["TieringPolicyTypeDef"],
    },
)

UpdateOpenZFSVolumeConfigurationTypeDef = TypedDict(
    "UpdateOpenZFSVolumeConfigurationTypeDef",
    {
        "StorageCapacityReservationGiB": NotRequired[int],
        "StorageCapacityQuotaGiB": NotRequired[int],
        "RecordSizeKiB": NotRequired[int],
        "DataCompressionType": NotRequired[OpenZFSDataCompressionTypeType],
        "NfsExports": NotRequired[Sequence["OpenZFSNfsExportTypeDef"]],
        "UserAndGroupQuotas": NotRequired[Sequence["OpenZFSUserOrGroupQuotaTypeDef"]],
        "ReadOnly": NotRequired[bool],
    },
)

UpdateSnapshotRequestRequestTypeDef = TypedDict(
    "UpdateSnapshotRequestRequestTypeDef",
    {
        "Name": str,
        "SnapshotId": str,
        "ClientRequestToken": NotRequired[str],
    },
)

UpdateSnapshotResponseTypeDef = TypedDict(
    "UpdateSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStorageVirtualMachineRequestRequestTypeDef = TypedDict(
    "UpdateStorageVirtualMachineRequestRequestTypeDef",
    {
        "StorageVirtualMachineId": str,
        "ActiveDirectoryConfiguration": NotRequired["UpdateSvmActiveDirectoryConfigurationTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "SvmAdminPassword": NotRequired[str],
    },
)

UpdateStorageVirtualMachineResponseTypeDef = TypedDict(
    "UpdateStorageVirtualMachineResponseTypeDef",
    {
        "StorageVirtualMachine": "StorageVirtualMachineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSvmActiveDirectoryConfigurationTypeDef = TypedDict(
    "UpdateSvmActiveDirectoryConfigurationTypeDef",
    {
        "SelfManagedActiveDirectoryConfiguration": NotRequired[
            "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"
        ],
    },
)

UpdateVolumeRequestRequestTypeDef = TypedDict(
    "UpdateVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "ClientRequestToken": NotRequired[str],
        "OntapConfiguration": NotRequired["UpdateOntapVolumeConfigurationTypeDef"],
        "Name": NotRequired[str],
        "OpenZFSConfiguration": NotRequired["UpdateOpenZFSVolumeConfigurationTypeDef"],
    },
)

UpdateVolumeResponseTypeDef = TypedDict(
    "UpdateVolumeResponseTypeDef",
    {
        "Volume": "VolumeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeFilterTypeDef = TypedDict(
    "VolumeFilterTypeDef",
    {
        "Name": NotRequired[VolumeFilterNameType],
        "Values": NotRequired[Sequence[str]],
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "FileSystemId": NotRequired[str],
        "Lifecycle": NotRequired[VolumeLifecycleType],
        "Name": NotRequired[str],
        "OntapConfiguration": NotRequired["OntapVolumeConfigurationTypeDef"],
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[VolumeTypeType],
        "LifecycleTransitionReason": NotRequired["LifecycleTransitionReasonTypeDef"],
        "AdministrativeActions": NotRequired[List["AdministrativeActionTypeDef"]],
        "OpenZFSConfiguration": NotRequired["OpenZFSVolumeConfigurationTypeDef"],
    },
)

WindowsAuditLogConfigurationTypeDef = TypedDict(
    "WindowsAuditLogConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "AuditLogDestination": NotRequired[str],
    },
)

WindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "WindowsAuditLogCreateConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "AuditLogDestination": NotRequired[str],
    },
)

WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": NotRequired[str],
        "SelfManagedActiveDirectoryConfiguration": NotRequired[
            "SelfManagedActiveDirectoryAttributesTypeDef"
        ],
        "DeploymentType": NotRequired[WindowsDeploymentTypeType],
        "RemoteAdministrationEndpoint": NotRequired[str],
        "PreferredSubnetId": NotRequired[str],
        "PreferredFileServerIp": NotRequired[str],
        "ThroughputCapacity": NotRequired[int],
        "MaintenanceOperationsInProgress": NotRequired[List[FileSystemMaintenanceOperationType]],
        "WeeklyMaintenanceStartTime": NotRequired[str],
        "DailyAutomaticBackupStartTime": NotRequired[str],
        "AutomaticBackupRetentionDays": NotRequired[int],
        "CopyTagsToBackups": NotRequired[bool],
        "Aliases": NotRequired[List["AliasTypeDef"]],
        "AuditLogConfiguration": NotRequired["WindowsAuditLogConfigurationTypeDef"],
    },
)
