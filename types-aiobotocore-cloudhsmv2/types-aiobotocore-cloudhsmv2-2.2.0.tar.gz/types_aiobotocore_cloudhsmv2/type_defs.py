"""
Type annotations for cloudhsmv2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_cloudhsmv2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import BackupStateType, ClusterStateType, HsmStateType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackupRetentionPolicyTypeDef",
    "BackupTypeDef",
    "CertificatesTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionRequestRequestTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "DeleteHsmResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DestinationBackupTypeDef",
    "HsmTypeDef",
    "InitializeClusterRequestRequestTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ModifyBackupAttributesRequestRequestTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "ModifyClusterRequestRequestTypeDef",
    "ModifyClusterResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreBackupRequestRequestTypeDef",
    "RestoreBackupResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef",
    {
        "Type": NotRequired[Literal["DAYS"]],
        "Value": NotRequired[str],
    },
)

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupId": str,
        "BackupState": NotRequired[BackupStateType],
        "ClusterId": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "CopyTimestamp": NotRequired[datetime],
        "NeverExpires": NotRequired[bool],
        "SourceRegion": NotRequired[str],
        "SourceBackup": NotRequired[str],
        "SourceCluster": NotRequired[str],
        "DeleteTimestamp": NotRequired[datetime],
        "TagList": NotRequired[List["TagTypeDef"]],
    },
)

CertificatesTypeDef = TypedDict(
    "CertificatesTypeDef",
    {
        "ClusterCsr": NotRequired[str],
        "HsmCertificate": NotRequired[str],
        "AwsHardwareCertificate": NotRequired[str],
        "ManufacturerHardwareCertificate": NotRequired[str],
        "ClusterCertificate": NotRequired[str],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "BackupPolicy": NotRequired[Literal["DEFAULT"]],
        "BackupRetentionPolicy": NotRequired["BackupRetentionPolicyTypeDef"],
        "ClusterId": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "Hsms": NotRequired[List["HsmTypeDef"]],
        "HsmType": NotRequired[str],
        "PreCoPassword": NotRequired[str],
        "SecurityGroup": NotRequired[str],
        "SourceBackupId": NotRequired[str],
        "State": NotRequired[ClusterStateType],
        "StateMessage": NotRequired[str],
        "SubnetMapping": NotRequired[Dict[str, str]],
        "VpcId": NotRequired[str],
        "Certificates": NotRequired["CertificatesTypeDef"],
        "TagList": NotRequired[List["TagTypeDef"]],
    },
)

CopyBackupToRegionRequestRequestTypeDef = TypedDict(
    "CopyBackupToRegionRequestRequestTypeDef",
    {
        "DestinationRegion": str,
        "BackupId": str,
        "TagList": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopyBackupToRegionResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseTypeDef",
    {
        "DestinationBackup": "DestinationBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "HsmType": str,
        "SubnetIds": Sequence[str],
        "BackupRetentionPolicy": NotRequired["BackupRetentionPolicyTypeDef"],
        "SourceBackupId": NotRequired[str],
        "TagList": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHsmRequestRequestTypeDef = TypedDict(
    "CreateHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "AvailabilityZone": str,
        "IpAddress": NotRequired[str],
    },
)

CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "Hsm": "HsmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHsmRequestRequestTypeDef = TypedDict(
    "DeleteHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "HsmId": NotRequired[str],
        "EniId": NotRequired[str],
        "EniIp": NotRequired[str],
    },
)

DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "HsmId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "SortAscending": NotRequired[bool],
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

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "Clusters": List["ClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationBackupTypeDef = TypedDict(
    "DestinationBackupTypeDef",
    {
        "CreateTimestamp": NotRequired[datetime],
        "SourceRegion": NotRequired[str],
        "SourceBackup": NotRequired[str],
        "SourceCluster": NotRequired[str],
    },
)

HsmTypeDef = TypedDict(
    "HsmTypeDef",
    {
        "HsmId": str,
        "AvailabilityZone": NotRequired[str],
        "ClusterId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "EniId": NotRequired[str],
        "EniIp": NotRequired[str],
        "State": NotRequired[HsmStateType],
        "StateMessage": NotRequired[str],
    },
)

InitializeClusterRequestRequestTypeDef = TypedDict(
    "InitializeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
        "SignedCert": str,
        "TrustAnchor": str,
    },
)

InitializeClusterResponseTypeDef = TypedDict(
    "InitializeClusterResponseTypeDef",
    {
        "State": ClusterStateType,
        "StateMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyBackupAttributesRequestRequestTypeDef = TypedDict(
    "ModifyBackupAttributesRequestRequestTypeDef",
    {
        "BackupId": str,
        "NeverExpires": bool,
    },
)

ModifyBackupAttributesResponseTypeDef = TypedDict(
    "ModifyBackupAttributesResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterRequestRequestTypeDef = TypedDict(
    "ModifyClusterRequestRequestTypeDef",
    {
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "ClusterId": str,
    },
)

ModifyClusterResponseTypeDef = TypedDict(
    "ModifyClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

RestoreBackupRequestRequestTypeDef = TypedDict(
    "RestoreBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)

RestoreBackupResponseTypeDef = TypedDict(
    "RestoreBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagList": Sequence["TagTypeDef"],
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
        "TagKeyList": Sequence[str],
    },
)
