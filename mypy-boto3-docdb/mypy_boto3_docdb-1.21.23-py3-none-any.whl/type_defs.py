"""
Type annotations for docdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionMessageRequestTypeDef

    data: AddSourceIdentifierToSubscriptionMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import ApplyMethodType, SourceTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterMessageRequestTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceMessageTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterMessageRequestTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeGlobalClustersMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverDBClusterMessageRequestTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterMessageRequestTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterMessageRequestTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterMessageRequestTypeDef",
    "StopDBClusterResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "UpgradeTargetTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AddSourceIdentifierToSubscriptionMessageRequestTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)

CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "CertificateType": NotRequired[str],
        "Thumbprint": NotRequired[str],
        "ValidFrom": NotRequired[datetime],
        "ValidTill": NotRequired[datetime],
        "CertificateArn": NotRequired[str],
    },
)

CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": NotRequired[Sequence[str]],
        "DisableLogTypes": NotRequired[Sequence[str]],
    },
)

CopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "SourceDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "SourceDBClusterSnapshotIdentifier": str,
        "TargetDBClusterSnapshotIdentifier": str,
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "SourceRegion": NotRequired[str],
    },
)

CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterMessageRequestTypeDef = TypedDict(
    "CreateDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "DBSubnetGroupName": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterIdentifier": NotRequired[str],
        "SourceRegion": NotRequired[str],
    },
)

CreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBInstanceMessageRequestTypeDef = TypedDict(
    "CreateDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBClusterIdentifier": str,
        "AvailabilityZone": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "PromotionTier": NotRequired[int],
    },
)

CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "CreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "SourceIds": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalClusterMessageRequestTypeDef = TypedDict(
    "CreateGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "SourceDBClusterIdentifier": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
    },
)

CreateGlobalClusterResultTypeDef = TypedDict(
    "CreateGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "IsClusterWriter": NotRequired[bool],
        "DBClusterParameterGroupStatus": NotRequired[str],
        "PromotionTier": NotRequired[int],
    },
)

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef",
    {
        "Marker": str,
        "DBClusters": List["DBClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "DBClusterParameterGroupArn": NotRequired[str],
    },
)

DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List["DBClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)

DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)

DBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "DBClusterSnapshotAttributes": NotRequired[List["DBClusterSnapshotAttributeTypeDef"]],
    },
)

DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List["DBClusterSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[datetime],
        "Engine": NotRequired[str],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DBClusterSnapshotArn": NotRequired[str],
        "SourceDBClusterSnapshotArn": NotRequired[str],
    },
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterParameterGroup": NotRequired[str],
        "DBSubnetGroup": NotRequired[str],
        "Status": NotRequired[str],
        "PercentProgress": NotRequired[str],
        "EarliestRestorableTime": NotRequired[datetime],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LatestRestorableTime": NotRequired[datetime],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSourceIdentifier": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[List[str]],
        "DBClusterMembers": NotRequired[List["DBClusterMemberTypeDef"]],
        "VpcSecurityGroups": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "DBClusterArn": NotRequired[str],
        "AssociatedRoles": NotRequired[List["DBClusterRoleTypeDef"]],
        "ClusterCreateTime": NotRequired[datetime],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "DeletionProtection": NotRequired[bool],
    },
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List["DBEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "DBEngineDescription": NotRequired[str],
        "DBEngineVersionDescription": NotRequired[str],
        "ValidUpgradeTarget": NotRequired[List["UpgradeTargetTypeDef"]],
        "ExportableLogTypes": NotRequired[List[str]],
        "SupportsLogExportsToCloudwatchLogs": NotRequired[bool],
    },
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {
        "Marker": str,
        "DBInstances": List["DBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)

DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Engine": NotRequired[str],
        "DBInstanceStatus": NotRequired[str],
        "Endpoint": NotRequired["EndpointTypeDef"],
        "InstanceCreateTime": NotRequired[datetime],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "VpcSecurityGroups": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroup": NotRequired["DBSubnetGroupTypeDef"],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired["PendingModifiedValuesTypeDef"],
        "LatestRestorableTime": NotRequired[datetime],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "PubliclyAccessible": NotRequired[bool],
        "StatusInfos": NotRequired[List["DBInstanceStatusInfoTypeDef"]],
        "DBClusterIdentifier": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "DBInstanceArn": NotRequired[str],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
    },
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List["DBSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "DBSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List["SubnetTypeDef"]],
        "DBSubnetGroupArn": NotRequired[str],
    },
)

DeleteDBClusterMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
    },
)

DeleteDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)

DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalClusterMessageRequestTypeDef = TypedDict(
    "DeleteGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)

DeleteGlobalClusterResultTypeDef = TypedDict(
    "DeleteGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParametersMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBClusterSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
    },
)

DescribeDBClustersMessageRequestTypeDef = TypedDict(
    "DescribeDBClustersMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
        "ListSupportedCharacterSets": NotRequired[bool],
        "ListSupportedTimezones": NotRequired[bool],
    },
)

DescribeDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeDBInstancesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Duration": NotRequired[int],
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeGlobalClustersMessageRequestTypeDef = TypedDict(
    "DescribeGlobalClustersMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Vpc": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "HostedZoneId": NotRequired[str],
    },
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": NotRequired[str],
        "Marker": NotRequired[str],
        "Parameters": NotRequired[List["ParameterTypeDef"]],
    },
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
    },
)

EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": NotRequired[str],
        "CustSubscriptionId": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
        "SourceType": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "EventCategoriesList": NotRequired[List[str]],
        "Enabled": NotRequired[bool],
        "EventSubscriptionArn": NotRequired[str],
    },
)

EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
        "Date": NotRequired[datetime],
        "SourceArn": NotRequired[str],
    },
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverDBClusterMessageRequestTypeDef = TypedDict(
    "FailoverDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "TargetDBInstanceIdentifier": NotRequired[str],
    },
)

FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)

GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {
        "DBClusterArn": NotRequired[str],
        "Readers": NotRequired[List[str]],
        "IsWriter": NotRequired[bool],
    },
)

GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "GlobalClusterResourceId": NotRequired[str],
        "GlobalClusterArn": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterMembers": NotRequired[List["GlobalClusterMemberTypeDef"]],
    },
)

GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List["GlobalClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ModifyDBClusterMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "NewDBClusterIdentifier": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Port": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "CloudwatchLogsExportConfiguration": NotRequired[
            "CloudwatchLogsExportConfigurationTypeDef"
        ],
        "EngineVersion": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
    },
)

ModifyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Parameters": Sequence["ParameterTypeDef"],
    },
)

ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "AttributeName": str,
        "ValuesToAdd": NotRequired[Sequence[str]],
        "ValuesToRemove": NotRequired[Sequence[str]],
    },
)

ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "ModifyDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "NewDBInstanceIdentifier": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "PromotionTier": NotRequired[int],
    },
)

ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "DBSubnetGroupDescription": NotRequired[str],
    },
)

ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "ModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)

ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyGlobalClusterMessageRequestTypeDef = TypedDict(
    "ModifyGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "NewGlobalClusterIdentifier": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
    },
)

ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZones": NotRequired[List["AvailabilityZoneTypeDef"]],
        "Vpc": NotRequired[bool],
    },
)

OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {
        "OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"],
        "Marker": str,
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

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "ApplyType": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "ApplyMethod": NotRequired[ApplyMethodType],
    },
)

PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": NotRequired[List[str]],
        "LogTypesToDisable": NotRequired[List[str]],
    },
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": NotRequired[str],
        "AutoAppliedAfterDate": NotRequired[datetime],
        "ForcedApplyDate": NotRequired[datetime],
        "OptInStatus": NotRequired[str],
        "CurrentApplyDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)

PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DBInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "PendingCloudwatchLogsExports": NotRequired["PendingCloudwatchLogsExportsTypeDef"],
    },
)

RebootDBInstanceMessageRequestTypeDef = TypedDict(
    "RebootDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "ForceFailover": NotRequired[bool],
    },
)

RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFromGlobalClusterMessageRequestTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "DbClusterIdentifier": str,
    },
)

RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)

ResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
    },
)

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "PendingMaintenanceActionDetails": NotRequired[List["PendingMaintenanceActionTypeDef"]],
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

RestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
    },
)

RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SourceDBClusterIdentifier": str,
        "RestoreToTime": NotRequired[Union[datetime, str]],
        "UseLatestRestorableTime": NotRequired[bool],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
    },
)

RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBClusterMessageRequestTypeDef = TypedDict(
    "StartDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDBClusterMessageRequestTypeDef = TypedDict(
    "StopDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired["AvailabilityZoneTypeDef"],
        "SubnetStatus": NotRequired[str],
    },
)

TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Description": NotRequired[str],
        "AutoUpgrade": NotRequired[bool],
        "IsMajorVersionUpgrade": NotRequired[bool],
    },
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
