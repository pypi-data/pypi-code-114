"""
Type annotations for neptune service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_neptune/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_neptune.type_defs import AddRoleToDBClusterMessageRequestTypeDef

    data: AddRoleToDBClusterMessageRequestTypeDef = {...}
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
    "AddRoleToDBClusterMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupMessageRequestTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CreateDBClusterEndpointMessageRequestTypeDef",
    "CreateDBClusterEndpointOutputTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupMessageRequestTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
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
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    "DeleteDBClusterEndpointOutputTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBParameterGroupMessageRequestTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    "DescribeDBParametersMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
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
    "ListTagsForResourceMessageRequestTypeDef",
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    "ModifyDBClusterEndpointOutputTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBParameterGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "OptionGroupMembershipTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResetDBParameterGroupMessageRequestTypeDef",
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
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "AddRoleToDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
        "FeatureName": NotRequired[str],
    },
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

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef",
    {
        "CharacterSetName": NotRequired[str],
        "CharacterSetDescription": NotRequired[str],
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

CopyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "CopyDBParameterGroupMessageRequestTypeDef",
    {
        "SourceDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopyDBParameterGroupResultTypeDef = TypedDict(
    "CopyDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "CreateDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "EndpointType": str,
        "StaticMembers": NotRequired[Sequence[str]],
        "ExcludedMembers": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBClusterEndpointOutputTypeDef = TypedDict(
    "CreateDBClusterEndpointOutputTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
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
        "CharacterSetName": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "DBSubnetGroupName": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSourceIdentifier": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
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
        "DBName": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "DBSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "Port": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "CharacterSetName": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DBClusterIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "Domain": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "Timezone": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
    },
)

CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBParameterGroupResultTypeDef = TypedDict(
    "CreateDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
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

DBClusterEndpointMessageTypeDef = TypedDict(
    "DBClusterEndpointMessageTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List["DBClusterEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointTypeDef = TypedDict(
    "DBClusterEndpointTypeDef",
    {
        "DBClusterEndpointIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterEndpointResourceIdentifier": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Status": NotRequired[str],
        "EndpointType": NotRequired[str],
        "CustomEndpointType": NotRequired[str],
        "StaticMembers": NotRequired[List[str]],
        "ExcludedMembers": NotRequired[List[str]],
        "DBClusterEndpointArn": NotRequired[str],
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

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {
        "DBClusterOptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
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
        "FeatureName": NotRequired[str],
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
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DBClusterSnapshotArn": NotRequired[str],
        "SourceDBClusterSnapshotArn": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
    },
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[List[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "CharacterSetName": NotRequired[str],
        "DatabaseName": NotRequired[str],
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
        "DBClusterOptionGroupMemberships": NotRequired[List["DBClusterOptionGroupStatusTypeDef"]],
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
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "CloneGroupId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "CopyTagsToSnapshot": NotRequired[bool],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "DeletionProtection": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "AutomaticRestartTime": NotRequired[datetime],
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
        "DefaultCharacterSet": NotRequired["CharacterSetTypeDef"],
        "SupportedCharacterSets": NotRequired[List["CharacterSetTypeDef"]],
        "ValidUpgradeTarget": NotRequired[List["UpgradeTargetTypeDef"]],
        "SupportedTimezones": NotRequired[List["TimezoneTypeDef"]],
        "ExportableLogTypes": NotRequired[List[str]],
        "SupportsLogExportsToCloudwatchLogs": NotRequired[bool],
        "SupportsReadReplica": NotRequired[bool],
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
        "MasterUsername": NotRequired[str],
        "DBName": NotRequired[str],
        "Endpoint": NotRequired["EndpointTypeDef"],
        "AllocatedStorage": NotRequired[int],
        "InstanceCreateTime": NotRequired[datetime],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "DBSecurityGroups": NotRequired[List["DBSecurityGroupMembershipTypeDef"]],
        "VpcSecurityGroups": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
        "DBParameterGroups": NotRequired[List["DBParameterGroupStatusTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroup": NotRequired["DBSubnetGroupTypeDef"],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired["PendingModifiedValuesTypeDef"],
        "LatestRestorableTime": NotRequired[datetime],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReadReplicaSourceDBInstanceIdentifier": NotRequired[str],
        "ReadReplicaDBInstanceIdentifiers": NotRequired[List[str]],
        "ReadReplicaDBClusterIdentifiers": NotRequired[List[str]],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[List["OptionGroupMembershipTypeDef"]],
        "CharacterSetName": NotRequired[str],
        "SecondaryAvailabilityZone": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "StatusInfos": NotRequired[List["DBInstanceStatusInfoTypeDef"]],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "DbInstancePort": NotRequired[int],
        "DBClusterIdentifier": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "DomainMemberships": NotRequired[List["DomainMembershipTypeDef"]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "EnhancedMonitoringResourceArn": NotRequired[str],
        "MonitoringRoleArn": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "DBInstanceArn": NotRequired[str],
        "Timezone": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "DeletionProtection": NotRequired[bool],
    },
)

DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupNameMessageTypeDef = TypedDict(
    "DBParameterGroupNameMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
    },
)

DBParameterGroupTypeDef = TypedDict(
    "DBParameterGroupTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "DBParameterGroupArn": NotRequired[str],
    },
)

DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List["DBParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
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

DeleteDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)

DeleteDBClusterEndpointOutputTypeDef = TypedDict(
    "DeleteDBClusterEndpointOutputTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
    },
)

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
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

DescribeDBClusterEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterEndpointIdentifier": NotRequired[str],
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

DescribeDBParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    {
        "DBParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBParametersMessageRequestTypeDef = TypedDict(
    "DescribeDBParametersMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Source": NotRequired[str],
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

DescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
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

DescribeValidDBInstanceModificationsMessageRequestTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DescribeValidDBInstanceModificationsResultTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultTypeDef",
    {
        "ValidDBInstanceModificationsMessage": "ValidDBInstanceModificationsMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {
        "Domain": NotRequired[str],
        "Status": NotRequired[str],
        "FQDN": NotRequired[str],
        "IAMRoleName": NotRequired[str],
    },
)

DoubleRangeTypeDef = TypedDict(
    "DoubleRangeTypeDef",
    {
        "From": NotRequired[float],
        "To": NotRequired[float],
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

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ModifyDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "EndpointType": NotRequired[str],
        "StaticMembers": NotRequired[Sequence[str]],
        "ExcludedMembers": NotRequired[Sequence[str]],
    },
)

ModifyDBClusterEndpointOutputTypeDef = TypedDict(
    "ModifyDBClusterEndpointOutputTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "OptionGroupName": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "CloudwatchLogsExportConfiguration": NotRequired[
            "CloudwatchLogsExportConfigurationTypeDef"
        ],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "DBInstanceParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
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
        "AllocatedStorage": NotRequired[int],
        "DBInstanceClass": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "DBSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "ApplyImmediately": NotRequired[bool],
        "MasterUserPassword": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "NewDBInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "Domain": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "DBPortNumber": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "MonitoringRoleArn": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "PromotionTier": NotRequired[int],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "CloudwatchLogsExportConfiguration": NotRequired[
            "CloudwatchLogsExportConfigurationTypeDef"
        ],
        "DeletionProtection": NotRequired[bool],
    },
)

ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
        "Parameters": Sequence["ParameterTypeDef"],
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

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
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
        "MultiAZCapable": NotRequired[bool],
        "ReadReplicaCapable": NotRequired[bool],
        "Vpc": NotRequired[bool],
        "SupportsStorageEncryption": NotRequired[bool],
        "StorageType": NotRequired[str],
        "SupportsIops": NotRequired[bool],
        "SupportsEnhancedMonitoring": NotRequired[bool],
        "SupportsIAMDatabaseAuthentication": NotRequired[bool],
        "SupportsPerformanceInsights": NotRequired[bool],
        "MinStorageSize": NotRequired[int],
        "MaxStorageSize": NotRequired[int],
        "MinIopsPerDbInstance": NotRequired[int],
        "MaxIopsPerDbInstance": NotRequired[int],
        "MinIopsPerGib": NotRequired[float],
        "MaxIopsPerGib": NotRequired[float],
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

PromoteReadReplicaDBClusterMessageRequestTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

PromoteReadReplicaDBClusterResultTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "From": NotRequired[int],
        "To": NotRequired[int],
        "Step": NotRequired[int],
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

RemoveRoleFromDBClusterMessageRequestTypeDef = TypedDict(
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
        "FeatureName": NotRequired[str],
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

ResetDBParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetDBParameterGroupMessageRequestTypeDef",
    {
        "DBParameterGroupName": str,
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
        "DatabaseName": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DBClusterParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
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
        "RestoreType": NotRequired[str],
        "RestoreToTime": NotRequired[Union[datetime, str]],
        "UseLatestRestorableTime": NotRequired[bool],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DBClusterParameterGroupName": NotRequired[str],
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

TimezoneTypeDef = TypedDict(
    "TimezoneTypeDef",
    {
        "TimezoneName": NotRequired[str],
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

ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": NotRequired[List["ValidStorageOptionsTypeDef"]],
    },
)

ValidStorageOptionsTypeDef = TypedDict(
    "ValidStorageOptionsTypeDef",
    {
        "StorageType": NotRequired[str],
        "StorageSize": NotRequired[List["RangeTypeDef"]],
        "ProvisionedIops": NotRequired[List["RangeTypeDef"]],
        "IopsToStorageRatio": NotRequired[List["DoubleRangeTypeDef"]],
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
