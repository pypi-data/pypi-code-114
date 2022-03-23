"""
Type annotations for storagegateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import ActivateGatewayInputRequestTypeDef

    data: ActivateGatewayInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ActiveDirectoryStatusType,
    AvailabilityMonitorTestStatusType,
    CaseSensitivityType,
    FileShareTypeType,
    GatewayCapacityType,
    HostEnvironmentType,
    ObjectACLType,
    PoolStatusType,
    RetentionLockTypeType,
    SMBSecurityStrategyType,
    TapeStorageClassType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivateGatewayInputRequestTypeDef",
    "ActivateGatewayOutputTypeDef",
    "AddCacheInputRequestTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceInputRequestTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferInputRequestTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageInputRequestTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolInputRequestTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AssociateFileSystemInputRequestTypeDef",
    "AssociateFileSystemOutputTypeDef",
    "AttachVolumeInputRequestTypeDef",
    "AttachVolumeOutputTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "CacheAttributesTypeDef",
    "CachediSCSIVolumeTypeDef",
    "CancelArchivalInputRequestTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelRetrievalInputRequestTypeDef",
    "CancelRetrievalOutputTypeDef",
    "ChapInfoTypeDef",
    "CreateCachediSCSIVolumeInputRequestTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareInputRequestTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareInputRequestTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotInputRequestTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeInputRequestTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolInputRequestTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeInputRequestTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesInputRequestTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyInputRequestTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitInputRequestTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteChapCredentialsInputRequestTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareInputRequestTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayInputRequestTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleInputRequestTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveInputRequestTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeInputRequestTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolInputRequestTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeInputRequestTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestInputRequestTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitInputRequestTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeBandwidthRateLimitScheduleInputRequestTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    "DescribeCacheInputRequestTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeCachediSCSIVolumesInputRequestTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeChapCredentialsInputRequestTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "DescribeFileSystemAssociationsInputRequestTypeDef",
    "DescribeFileSystemAssociationsOutputTypeDef",
    "DescribeGatewayInformationInputRequestTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeInputRequestTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "DescribeNFSFileSharesInputRequestTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeSMBFileSharesInputRequestTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "DescribeSMBSettingsInputRequestTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeSnapshotScheduleInputRequestTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeStorediSCSIVolumesInputRequestTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeTapeArchivesInputRequestTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsInputRequestTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesInputRequestTypeDef",
    "DescribeTapesOutputTypeDef",
    "DescribeUploadBufferInputRequestTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeVTLDevicesInputRequestTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeWorkingStorageInputRequestTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeInputRequestTypeDef",
    "DetachVolumeOutputTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayInputRequestTypeDef",
    "DisableGatewayOutputTypeDef",
    "DisassociateFileSystemInputRequestTypeDef",
    "DisassociateFileSystemOutputTypeDef",
    "DiskTypeDef",
    "EndpointNetworkConfigurationTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "FileSystemAssociationStatusDetailTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainInputRequestTypeDef",
    "JoinDomainOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesInputRequestTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "ListFileSharesInputRequestTypeDef",
    "ListFileSharesOutputTypeDef",
    "ListFileSystemAssociationsInputRequestTypeDef",
    "ListFileSystemAssociationsOutputTypeDef",
    "ListGatewaysInputRequestTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListLocalDisksInputRequestTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTapePoolsInputRequestTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesInputRequestTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeInitiatorsInputRequestTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "ListVolumeRecoveryPointsInputRequestTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesInputRequestTypeDef",
    "ListVolumesOutputTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "NotifyWhenUploadedInputRequestTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoolInfoTypeDef",
    "RefreshCacheInputRequestTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceInputRequestTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheInputRequestTypeDef",
    "ResetCacheOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveTapeArchiveInputRequestTypeDef",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointInputRequestTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SMBFileShareInfoTypeDef",
    "SMBLocalGroupsTypeDef",
    "SetLocalConsolePasswordInputRequestTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordInputRequestTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayInputRequestTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "StartAvailabilityMonitorTestInputRequestTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartGatewayInputRequestTypeDef",
    "StartGatewayOutputTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "UpdateAutomaticTapeCreationPolicyInputRequestTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitInputRequestTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleInputRequestTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsInputRequestTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateFileSystemAssociationInputRequestTypeDef",
    "UpdateFileSystemAssociationOutputTypeDef",
    "UpdateGatewayInformationInputRequestTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeInputRequestTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareInputRequestTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareInputRequestTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityInputRequestTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    "UpdateSMBLocalGroupsInputRequestTypeDef",
    "UpdateSMBLocalGroupsOutputTypeDef",
    "UpdateSMBSecurityStrategyInputRequestTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleInputRequestTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeInputRequestTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
)

ActivateGatewayInputRequestTypeDef = TypedDict(
    "ActivateGatewayInputRequestTypeDef",
    {
        "ActivationKey": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayRegion": str,
        "GatewayType": NotRequired[str],
        "TapeDriveType": NotRequired[str],
        "MediumChangerType": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

ActivateGatewayOutputTypeDef = TypedDict(
    "ActivateGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddCacheInputRequestTypeDef = TypedDict(
    "AddCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": Sequence[str],
    },
)

AddCacheOutputTypeDef = TypedDict(
    "AddCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceInputRequestTypeDef = TypedDict(
    "AddTagsToResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

AddTagsToResourceOutputTypeDef = TypedDict(
    "AddTagsToResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddUploadBufferInputRequestTypeDef = TypedDict(
    "AddUploadBufferInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": Sequence[str],
    },
)

AddUploadBufferOutputTypeDef = TypedDict(
    "AddUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddWorkingStorageInputRequestTypeDef = TypedDict(
    "AddWorkingStorageInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": Sequence[str],
    },
)

AddWorkingStorageOutputTypeDef = TypedDict(
    "AddWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignTapePoolInputRequestTypeDef = TypedDict(
    "AssignTapePoolInputRequestTypeDef",
    {
        "TapeARN": str,
        "PoolId": str,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)

AssignTapePoolOutputTypeDef = TypedDict(
    "AssignTapePoolOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateFileSystemInputRequestTypeDef = TypedDict(
    "AssociateFileSystemInputRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
        "ClientToken": str,
        "GatewayARN": str,
        "LocationARN": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "AuditDestinationARN": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "EndpointNetworkConfiguration": NotRequired["EndpointNetworkConfigurationTypeDef"],
    },
)

AssociateFileSystemOutputTypeDef = TypedDict(
    "AssociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachVolumeInputRequestTypeDef = TypedDict(
    "AttachVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VolumeARN": str,
        "NetworkInterfaceId": str,
        "TargetName": NotRequired[str],
        "DiskId": NotRequired[str],
    },
)

AttachVolumeOutputTypeDef = TypedDict(
    "AttachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomaticTapeCreationPolicyInfoTypeDef = TypedDict(
    "AutomaticTapeCreationPolicyInfoTypeDef",
    {
        "AutomaticTapeCreationRules": NotRequired[List["AutomaticTapeCreationRuleTypeDef"]],
        "GatewayARN": NotRequired[str],
    },
)

AutomaticTapeCreationRuleTypeDef = TypedDict(
    "AutomaticTapeCreationRuleTypeDef",
    {
        "TapeBarcodePrefix": str,
        "PoolId": str,
        "TapeSizeInBytes": int,
        "MinimumNumTapes": int,
        "Worm": NotRequired[bool],
    },
)

BandwidthRateLimitIntervalTypeDef = TypedDict(
    "BandwidthRateLimitIntervalTypeDef",
    {
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "DaysOfWeek": List[int],
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
        "AverageDownloadRateLimitInBitsPerSec": NotRequired[int],
    },
)

CacheAttributesTypeDef = TypedDict(
    "CacheAttributesTypeDef",
    {
        "CacheStaleTimeoutInSeconds": NotRequired[int],
    },
)

CachediSCSIVolumeTypeDef = TypedDict(
    "CachediSCSIVolumeTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeStatus": NotRequired[str],
        "VolumeAttachmentStatus": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeProgress": NotRequired[float],
        "SourceSnapshotId": NotRequired[str],
        "VolumeiSCSIAttributes": NotRequired["VolumeiSCSIAttributesTypeDef"],
        "CreatedDate": NotRequired[datetime],
        "VolumeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "TargetName": NotRequired[str],
    },
)

CancelArchivalInputRequestTypeDef = TypedDict(
    "CancelArchivalInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)

CancelArchivalOutputTypeDef = TypedDict(
    "CancelArchivalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelRetrievalInputRequestTypeDef = TypedDict(
    "CancelRetrievalInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)

CancelRetrievalOutputTypeDef = TypedDict(
    "CancelRetrievalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChapInfoTypeDef = TypedDict(
    "ChapInfoTypeDef",
    {
        "TargetARN": NotRequired[str],
        "SecretToAuthenticateInitiator": NotRequired[str],
        "InitiatorName": NotRequired[str],
        "SecretToAuthenticateTarget": NotRequired[str],
    },
)

CreateCachediSCSIVolumeInputRequestTypeDef = TypedDict(
    "CreateCachediSCSIVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VolumeSizeInBytes": int,
        "TargetName": str,
        "NetworkInterfaceId": str,
        "ClientToken": str,
        "SnapshotId": NotRequired[str],
        "SourceVolumeARN": NotRequired[str],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCachediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNFSFileShareInputRequestTypeDef = TypedDict(
    "CreateNFSFileShareInputRequestTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
        "NFSFileShareDefaults": NotRequired["NFSFileShareDefaultsTypeDef"],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[Sequence[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)

CreateNFSFileShareOutputTypeDef = TypedDict(
    "CreateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSMBFileShareInputRequestTypeDef = TypedDict(
    "CreateSMBFileShareInputRequestTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[Sequence[str]],
        "ValidUserList": NotRequired[Sequence[str]],
        "InvalidUserList": NotRequired[Sequence[str]],
        "AuditDestinationARN": NotRequired[str],
        "Authentication": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)

CreateSMBFileShareOutputTypeDef = TypedDict(
    "CreateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSnapshotFromVolumeRecoveryPointOutputTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    {
        "SnapshotId": str,
        "VolumeARN": str,
        "VolumeRecoveryPointTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotInputRequestTypeDef = TypedDict(
    "CreateSnapshotInputRequestTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSnapshotOutputTypeDef = TypedDict(
    "CreateSnapshotOutputTypeDef",
    {
        "VolumeARN": str,
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStorediSCSIVolumeInputRequestTypeDef = TypedDict(
    "CreateStorediSCSIVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskId": str,
        "PreserveExistingData": bool,
        "TargetName": str,
        "NetworkInterfaceId": str,
        "SnapshotId": NotRequired[str],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateStorediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTapePoolInputRequestTypeDef = TypedDict(
    "CreateTapePoolInputRequestTypeDef",
    {
        "PoolName": str,
        "StorageClass": TapeStorageClassType,
        "RetentionLockType": NotRequired[RetentionLockTypeType],
        "RetentionLockTimeInDays": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTapePoolOutputTypeDef = TypedDict(
    "CreateTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTapeWithBarcodeInputRequestTypeDef = TypedDict(
    "CreateTapeWithBarcodeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "TapeBarcode": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTapeWithBarcodeOutputTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTapesInputRequestTypeDef = TypedDict(
    "CreateTapesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "ClientToken": str,
        "NumTapesToCreate": int,
        "TapeBarcodePrefix": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTapesOutputTypeDef = TypedDict(
    "CreateTapesOutputTypeDef",
    {
        "TapeARNs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutomaticTapeCreationPolicyInputRequestTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DeleteAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "DeleteBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
        "BandwidthType": str,
    },
)

DeleteBandwidthRateLimitOutputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChapCredentialsInputRequestTypeDef = TypedDict(
    "DeleteChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
    },
)

DeleteChapCredentialsOutputTypeDef = TypedDict(
    "DeleteChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileShareInputRequestTypeDef = TypedDict(
    "DeleteFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
        "ForceDelete": NotRequired[bool],
    },
)

DeleteFileShareOutputTypeDef = TypedDict(
    "DeleteFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayInputRequestTypeDef = TypedDict(
    "DeleteGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotScheduleInputRequestTypeDef = TypedDict(
    "DeleteSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

DeleteSnapshotScheduleOutputTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapeArchiveInputRequestTypeDef = TypedDict(
    "DeleteTapeArchiveInputRequestTypeDef",
    {
        "TapeARN": str,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)

DeleteTapeArchiveOutputTypeDef = TypedDict(
    "DeleteTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapeInputRequestTypeDef = TypedDict(
    "DeleteTapeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)

DeleteTapeOutputTypeDef = TypedDict(
    "DeleteTapeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapePoolInputRequestTypeDef = TypedDict(
    "DeleteTapePoolInputRequestTypeDef",
    {
        "PoolARN": str,
    },
)

DeleteTapePoolOutputTypeDef = TypedDict(
    "DeleteTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeInputRequestTypeDef = TypedDict(
    "DeleteVolumeInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

DeleteVolumeOutputTypeDef = TypedDict(
    "DeleteVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityMonitorTestInputRequestTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "Status": AvailabilityMonitorTestStatusType,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "DescribeBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeBandwidthRateLimitOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCacheInputRequestTypeDef = TypedDict(
    "DescribeCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeCacheOutputTypeDef = TypedDict(
    "DescribeCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCachediSCSIVolumesInputRequestTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesInputRequestTypeDef",
    {
        "VolumeARNs": Sequence[str],
    },
)

DescribeCachediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputTypeDef",
    {
        "CachediSCSIVolumes": List["CachediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChapCredentialsInputRequestTypeDef = TypedDict(
    "DescribeChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
    },
)

DescribeChapCredentialsOutputTypeDef = TypedDict(
    "DescribeChapCredentialsOutputTypeDef",
    {
        "ChapCredentials": List["ChapInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemAssociationsInputRequestTypeDef = TypedDict(
    "DescribeFileSystemAssociationsInputRequestTypeDef",
    {
        "FileSystemAssociationARNList": Sequence[str],
    },
)

DescribeFileSystemAssociationsOutputTypeDef = TypedDict(
    "DescribeFileSystemAssociationsOutputTypeDef",
    {
        "FileSystemAssociationInfoList": List["FileSystemAssociationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayInformationInputRequestTypeDef = TypedDict(
    "DescribeGatewayInformationInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeGatewayInformationOutputTypeDef = TypedDict(
    "DescribeGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List["TagTypeDef"],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": HostEnvironmentType,
        "EndpointType": str,
        "SoftwareUpdatesEndDate": str,
        "DeprecationDate": str,
        "GatewayCapacity": GatewayCapacityType,
        "SupportedGatewayCapacities": List[GatewayCapacityType],
        "HostEnvironmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeMaintenanceStartTimeOutputTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNFSFileSharesInputRequestTypeDef = TypedDict(
    "DescribeNFSFileSharesInputRequestTypeDef",
    {
        "FileShareARNList": Sequence[str],
    },
)

DescribeNFSFileSharesOutputTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputTypeDef",
    {
        "NFSFileShareInfoList": List["NFSFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBFileSharesInputRequestTypeDef = TypedDict(
    "DescribeSMBFileSharesInputRequestTypeDef",
    {
        "FileShareARNList": Sequence[str],
    },
)

DescribeSMBFileSharesOutputTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputTypeDef",
    {
        "SMBFileShareInfoList": List["SMBFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBSettingsInputRequestTypeDef = TypedDict(
    "DescribeSMBSettingsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeSMBSettingsOutputTypeDef = TypedDict(
    "DescribeSMBSettingsOutputTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
        "FileSharesVisible": bool,
        "SMBLocalGroups": "SMBLocalGroupsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotScheduleInputRequestTypeDef = TypedDict(
    "DescribeSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

DescribeSnapshotScheduleOutputTypeDef = TypedDict(
    "DescribeSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorediSCSIVolumesInputRequestTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesInputRequestTypeDef",
    {
        "VolumeARNs": Sequence[str],
    },
)

DescribeStorediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputTypeDef",
    {
        "StorediSCSIVolumes": List["StorediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapeArchivesInputRequestTypeDef = TypedDict(
    "DescribeTapeArchivesInputRequestTypeDef",
    {
        "TapeARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {
        "TapeArchives": List["TapeArchiveTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapeRecoveryPointsInputRequestTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List["TapeRecoveryPointInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapesInputRequestTypeDef = TypedDict(
    "DescribeTapesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef",
    {
        "Tapes": List["TapeTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUploadBufferInputRequestTypeDef = TypedDict(
    "DescribeUploadBufferInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeUploadBufferOutputTypeDef = TypedDict(
    "DescribeUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVTLDevicesInputRequestTypeDef = TypedDict(
    "DescribeVTLDevicesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VTLDeviceARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List["VTLDeviceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkingStorageInputRequestTypeDef = TypedDict(
    "DescribeWorkingStorageInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeWorkingStorageOutputTypeDef = TypedDict(
    "DescribeWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachVolumeInputRequestTypeDef = TypedDict(
    "DetachVolumeInputRequestTypeDef",
    {
        "VolumeARN": str,
        "ForceDetach": NotRequired[bool],
    },
)

DetachVolumeOutputTypeDef = TypedDict(
    "DetachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceiSCSIAttributesTypeDef = TypedDict(
    "DeviceiSCSIAttributesTypeDef",
    {
        "TargetARN": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfacePort": NotRequired[int],
        "ChapEnabled": NotRequired[bool],
    },
)

DisableGatewayInputRequestTypeDef = TypedDict(
    "DisableGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DisableGatewayOutputTypeDef = TypedDict(
    "DisableGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateFileSystemInputRequestTypeDef = TypedDict(
    "DisassociateFileSystemInputRequestTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ForceDelete": NotRequired[bool],
    },
)

DisassociateFileSystemOutputTypeDef = TypedDict(
    "DisassociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "DiskId": NotRequired[str],
        "DiskPath": NotRequired[str],
        "DiskNode": NotRequired[str],
        "DiskStatus": NotRequired[str],
        "DiskSizeInBytes": NotRequired[int],
        "DiskAllocationType": NotRequired[str],
        "DiskAllocationResource": NotRequired[str],
        "DiskAttributeList": NotRequired[List[str]],
    },
)

EndpointNetworkConfigurationTypeDef = TypedDict(
    "EndpointNetworkConfigurationTypeDef",
    {
        "IpAddresses": NotRequired[Sequence[str]],
    },
)

FileShareInfoTypeDef = TypedDict(
    "FileShareInfoTypeDef",
    {
        "FileShareType": NotRequired[FileShareTypeType],
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
    },
)

FileSystemAssociationInfoTypeDef = TypedDict(
    "FileSystemAssociationInfoTypeDef",
    {
        "FileSystemAssociationARN": NotRequired[str],
        "LocationARN": NotRequired[str],
        "FileSystemAssociationStatus": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "EndpointNetworkConfiguration": NotRequired["EndpointNetworkConfigurationTypeDef"],
        "FileSystemAssociationStatusDetails": NotRequired[
            List["FileSystemAssociationStatusDetailTypeDef"]
        ],
    },
)

FileSystemAssociationStatusDetailTypeDef = TypedDict(
    "FileSystemAssociationStatusDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
    },
)

FileSystemAssociationSummaryTypeDef = TypedDict(
    "FileSystemAssociationSummaryTypeDef",
    {
        "FileSystemAssociationId": NotRequired[str],
        "FileSystemAssociationARN": NotRequired[str],
        "FileSystemAssociationStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
    },
)

GatewayInfoTypeDef = TypedDict(
    "GatewayInfoTypeDef",
    {
        "GatewayId": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "GatewayType": NotRequired[str],
        "GatewayOperationalState": NotRequired[str],
        "GatewayName": NotRequired[str],
        "Ec2InstanceId": NotRequired[str],
        "Ec2InstanceRegion": NotRequired[str],
        "HostEnvironment": NotRequired[HostEnvironmentType],
        "HostEnvironmentId": NotRequired[str],
    },
)

JoinDomainInputRequestTypeDef = TypedDict(
    "JoinDomainInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "UserName": str,
        "Password": str,
        "OrganizationalUnit": NotRequired[str],
        "DomainControllers": NotRequired[Sequence[str]],
        "TimeoutInSeconds": NotRequired[int],
    },
)

JoinDomainOutputTypeDef = TypedDict(
    "JoinDomainOutputTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutomaticTapeCreationPoliciesInputRequestTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
    },
)

ListAutomaticTapeCreationPoliciesOutputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    {
        "AutomaticTapeCreationPolicyInfos": List["AutomaticTapeCreationPolicyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSharesInputRequestTypeDef = TypedDict(
    "ListFileSharesInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List["FileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSystemAssociationsInputRequestTypeDef = TypedDict(
    "ListFileSystemAssociationsInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

ListFileSystemAssociationsOutputTypeDef = TypedDict(
    "ListFileSystemAssociationsOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileSystemAssociationSummaryList": List["FileSystemAssociationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysInputRequestTypeDef = TypedDict(
    "ListGatewaysInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List["GatewayInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocalDisksInputRequestTypeDef = TypedDict(
    "ListLocalDisksInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ListLocalDisksOutputTypeDef = TypedDict(
    "ListLocalDisksOutputTypeDef",
    {
        "GatewayARN": str,
        "Disks": List["DiskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapePoolsInputRequestTypeDef = TypedDict(
    "ListTapePoolsInputRequestTypeDef",
    {
        "PoolARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTapePoolsOutputTypeDef = TypedDict(
    "ListTapePoolsOutputTypeDef",
    {
        "PoolInfos": List["PoolInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapesInputRequestTypeDef = TypedDict(
    "ListTapesInputRequestTypeDef",
    {
        "TapeARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef",
    {
        "TapeInfos": List["TapeInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeInitiatorsInputRequestTypeDef = TypedDict(
    "ListVolumeInitiatorsInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

ListVolumeInitiatorsOutputTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputTypeDef",
    {
        "Initiators": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeRecoveryPointsInputRequestTypeDef = TypedDict(
    "ListVolumeRecoveryPointsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ListVolumeRecoveryPointsOutputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List["VolumeRecoveryPointInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumesInputRequestTypeDef = TypedDict(
    "ListVolumesInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List["VolumeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NFSFileShareDefaultsTypeDef = TypedDict(
    "NFSFileShareDefaultsTypeDef",
    {
        "FileMode": NotRequired[str],
        "DirectoryMode": NotRequired[str],
        "GroupId": NotRequired[int],
        "OwnerId": NotRequired[int],
    },
)

NFSFileShareInfoTypeDef = TypedDict(
    "NFSFileShareInfoTypeDef",
    {
        "NFSFileShareDefaults": NotRequired["NFSFileShareDefaultsTypeDef"],
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Path": NotRequired[str],
        "Role": NotRequired[str],
        "LocationARN": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[List[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "Tags": NotRequired[List["TagTypeDef"]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv4Address": NotRequired[str],
        "MacAddress": NotRequired[str],
        "Ipv6Address": NotRequired[str],
    },
)

NotifyWhenUploadedInputRequestTypeDef = TypedDict(
    "NotifyWhenUploadedInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)

NotifyWhenUploadedOutputTypeDef = TypedDict(
    "NotifyWhenUploadedOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PoolInfoTypeDef = TypedDict(
    "PoolInfoTypeDef",
    {
        "PoolARN": NotRequired[str],
        "PoolName": NotRequired[str],
        "StorageClass": NotRequired[TapeStorageClassType],
        "RetentionLockType": NotRequired[RetentionLockTypeType],
        "RetentionLockTimeInDays": NotRequired[int],
        "PoolStatus": NotRequired[PoolStatusType],
    },
)

RefreshCacheInputRequestTypeDef = TypedDict(
    "RefreshCacheInputRequestTypeDef",
    {
        "FileShareARN": str,
        "FolderList": NotRequired[Sequence[str]],
        "Recursive": NotRequired[bool],
    },
)

RefreshCacheOutputTypeDef = TypedDict(
    "RefreshCacheOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceInputRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

RemoveTagsFromResourceOutputTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetCacheInputRequestTypeDef = TypedDict(
    "ResetCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ResetCacheOutputTypeDef = TypedDict(
    "ResetCacheOutputTypeDef",
    {
        "GatewayARN": str,
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

RetrieveTapeArchiveInputRequestTypeDef = TypedDict(
    "RetrieveTapeArchiveInputRequestTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)

RetrieveTapeArchiveOutputTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetrieveTapeRecoveryPointInputRequestTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointInputRequestTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)

RetrieveTapeRecoveryPointOutputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SMBFileShareInfoTypeDef = TypedDict(
    "SMBFileShareInfoTypeDef",
    {
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Path": NotRequired[str],
        "Role": NotRequired[str],
        "LocationARN": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[List[str]],
        "ValidUserList": NotRequired[List[str]],
        "InvalidUserList": NotRequired[List[str]],
        "AuditDestinationARN": NotRequired[str],
        "Authentication": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "Tags": NotRequired[List["TagTypeDef"]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)

SMBLocalGroupsTypeDef = TypedDict(
    "SMBLocalGroupsTypeDef",
    {
        "GatewayAdmins": NotRequired[List[str]],
    },
)

SetLocalConsolePasswordInputRequestTypeDef = TypedDict(
    "SetLocalConsolePasswordInputRequestTypeDef",
    {
        "GatewayARN": str,
        "LocalConsolePassword": str,
    },
)

SetLocalConsolePasswordOutputTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSMBGuestPasswordInputRequestTypeDef = TypedDict(
    "SetSMBGuestPasswordInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Password": str,
    },
)

SetSMBGuestPasswordOutputTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShutdownGatewayInputRequestTypeDef = TypedDict(
    "ShutdownGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ShutdownGatewayOutputTypeDef = TypedDict(
    "ShutdownGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAvailabilityMonitorTestInputRequestTypeDef = TypedDict(
    "StartAvailabilityMonitorTestInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

StartAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartGatewayInputRequestTypeDef = TypedDict(
    "StartGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

StartGatewayOutputTypeDef = TypedDict(
    "StartGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorediSCSIVolumeTypeDef = TypedDict(
    "StorediSCSIVolumeTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeStatus": NotRequired[str],
        "VolumeAttachmentStatus": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeProgress": NotRequired[float],
        "VolumeDiskId": NotRequired[str],
        "SourceSnapshotId": NotRequired[str],
        "PreservedExistingData": NotRequired[bool],
        "VolumeiSCSIAttributes": NotRequired["VolumeiSCSIAttributesTypeDef"],
        "CreatedDate": NotRequired[datetime],
        "VolumeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "TargetName": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TapeArchiveTypeDef = TypedDict(
    "TapeArchiveTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeBarcode": NotRequired[str],
        "TapeCreatedDate": NotRequired[datetime],
        "TapeSizeInBytes": NotRequired[int],
        "CompletionTime": NotRequired[datetime],
        "RetrievedTo": NotRequired[str],
        "TapeStatus": NotRequired[str],
        "TapeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "RetentionStartDate": NotRequired[datetime],
        "PoolEntryDate": NotRequired[datetime],
    },
)

TapeInfoTypeDef = TypedDict(
    "TapeInfoTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeBarcode": NotRequired[str],
        "TapeSizeInBytes": NotRequired[int],
        "TapeStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "PoolId": NotRequired[str],
        "RetentionStartDate": NotRequired[datetime],
        "PoolEntryDate": NotRequired[datetime],
    },
)

TapeRecoveryPointInfoTypeDef = TypedDict(
    "TapeRecoveryPointInfoTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeRecoveryPointTime": NotRequired[datetime],
        "TapeSizeInBytes": NotRequired[int],
        "TapeStatus": NotRequired[str],
    },
)

TapeTypeDef = TypedDict(
    "TapeTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeBarcode": NotRequired[str],
        "TapeCreatedDate": NotRequired[datetime],
        "TapeSizeInBytes": NotRequired[int],
        "TapeStatus": NotRequired[str],
        "VTLDevice": NotRequired[str],
        "Progress": NotRequired[float],
        "TapeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "RetentionStartDate": NotRequired[datetime],
        "PoolEntryDate": NotRequired[datetime],
    },
)

UpdateAutomaticTapeCreationPolicyInputRequestTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyInputRequestTypeDef",
    {
        "AutomaticTapeCreationRules": Sequence["AutomaticTapeCreationRuleTypeDef"],
        "GatewayARN": str,
    },
)

UpdateAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "UpdateBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
        "AverageDownloadRateLimitInBitsPerSec": NotRequired[int],
    },
)

UpdateBandwidthRateLimitOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": Sequence["BandwidthRateLimitIntervalTypeDef"],
    },
)

UpdateBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChapCredentialsInputRequestTypeDef = TypedDict(
    "UpdateChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": NotRequired[str],
    },
)

UpdateChapCredentialsOutputTypeDef = TypedDict(
    "UpdateChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemAssociationInputRequestTypeDef = TypedDict(
    "UpdateFileSystemAssociationInputRequestTypeDef",
    {
        "FileSystemAssociationARN": str,
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
    },
)

UpdateFileSystemAssociationOutputTypeDef = TypedDict(
    "UpdateFileSystemAssociationOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "UpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": NotRequired[str],
        "GatewayTimezone": NotRequired[str],
        "CloudWatchLogGroupARN": NotRequired[str],
        "GatewayCapacity": NotRequired[GatewayCapacityType],
    },
)

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewaySoftwareNowInputRequestTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": NotRequired[int],
        "DayOfMonth": NotRequired[int],
    },
)

UpdateMaintenanceStartTimeOutputTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNFSFileShareInputRequestTypeDef = TypedDict(
    "UpdateNFSFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "NFSFileShareDefaults": NotRequired["NFSFileShareDefaultsTypeDef"],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[Sequence[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "NotificationPolicy": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)

UpdateNFSFileShareOutputTypeDef = TypedDict(
    "UpdateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBFileShareInputRequestTypeDef = TypedDict(
    "UpdateSMBFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[Sequence[str]],
        "ValidUserList": NotRequired[Sequence[str]],
        "InvalidUserList": NotRequired[Sequence[str]],
        "AuditDestinationARN": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired["CacheAttributesTypeDef"],
        "NotificationPolicy": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)

UpdateSMBFileShareOutputTypeDef = TypedDict(
    "UpdateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBFileShareVisibilityInputRequestTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityInputRequestTypeDef",
    {
        "GatewayARN": str,
        "FileSharesVisible": bool,
    },
)

UpdateSMBFileShareVisibilityOutputTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBLocalGroupsInputRequestTypeDef = TypedDict(
    "UpdateSMBLocalGroupsInputRequestTypeDef",
    {
        "GatewayARN": str,
        "SMBLocalGroups": "SMBLocalGroupsTypeDef",
    },
)

UpdateSMBLocalGroupsOutputTypeDef = TypedDict(
    "UpdateSMBLocalGroupsOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBSecurityStrategyInputRequestTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyInputRequestTypeDef",
    {
        "GatewayARN": str,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
    },
)

UpdateSMBSecurityStrategyOutputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSnapshotScheduleInputRequestTypeDef = TypedDict(
    "UpdateSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateSnapshotScheduleOutputTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVTLDeviceTypeInputRequestTypeDef = TypedDict(
    "UpdateVTLDeviceTypeInputRequestTypeDef",
    {
        "VTLDeviceARN": str,
        "DeviceType": str,
    },
)

UpdateVTLDeviceTypeOutputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputTypeDef",
    {
        "VTLDeviceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VTLDeviceTypeDef = TypedDict(
    "VTLDeviceTypeDef",
    {
        "VTLDeviceARN": NotRequired[str],
        "VTLDeviceType": NotRequired[str],
        "VTLDeviceVendor": NotRequired[str],
        "VTLDeviceProductIdentifier": NotRequired[str],
        "DeviceiSCSIAttributes": NotRequired["DeviceiSCSIAttributesTypeDef"],
    },
)

VolumeInfoTypeDef = TypedDict(
    "VolumeInfoTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeId": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "GatewayId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeAttachmentStatus": NotRequired[str],
    },
)

VolumeRecoveryPointInfoTypeDef = TypedDict(
    "VolumeRecoveryPointInfoTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeUsageInBytes": NotRequired[int],
        "VolumeRecoveryPointTime": NotRequired[str],
    },
)

VolumeiSCSIAttributesTypeDef = TypedDict(
    "VolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfacePort": NotRequired[int],
        "LunNumber": NotRequired[int],
        "ChapEnabled": NotRequired[bool],
    },
)
