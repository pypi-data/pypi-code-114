"""
Type annotations for elasticache service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_elasticache/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_elasticache.type_defs import AddTagsToResourceMessageRequestTypeDef

    data: AddTagsToResourceMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AuthenticationTypeType,
    AuthTokenUpdateStatusType,
    AuthTokenUpdateStrategyTypeType,
    AutomaticFailoverStatusType,
    AZModeType,
    ChangeTypeType,
    DataTieringStatusType,
    DestinationTypeType,
    LogDeliveryConfigurationStatusType,
    LogFormatType,
    LogTypeType,
    MultiAZStatusType,
    NodeUpdateInitiatedByType,
    NodeUpdateStatusType,
    OutpostModeType,
    PendingAutomaticFailoverStatusType,
    ServiceUpdateSeverityType,
    ServiceUpdateStatusType,
    SlaMetType,
    SourceTypeType,
    UpdateActionStatusType,
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
    "AddTagsToResourceMessageRequestTypeDef",
    "AllowedNodeTypeModificationsMessageTypeDef",
    "AuthenticationTypeDef",
    "AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef",
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchApplyUpdateActionMessageRequestTypeDef",
    "BatchStopUpdateActionMessageRequestTypeDef",
    "CacheClusterMessageTypeDef",
    "CacheClusterTypeDef",
    "CacheEngineVersionMessageTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheNodeTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "CacheParameterGroupDetailsTypeDef",
    "CacheParameterGroupNameMessageTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheParameterGroupTypeDef",
    "CacheParameterGroupsMessageTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "CacheSecurityGroupMessageTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheSubnetGroupMessageTypeDef",
    "CacheSubnetGroupTypeDef",
    "CloudWatchLogsDestinationDetailsTypeDef",
    "CompleteMigrationMessageRequestTypeDef",
    "CompleteMigrationResponseTypeDef",
    "ConfigureShardTypeDef",
    "CopySnapshotMessageRequestTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateCacheClusterMessageRequestTypeDef",
    "CreateCacheClusterResultTypeDef",
    "CreateCacheParameterGroupMessageRequestTypeDef",
    "CreateCacheParameterGroupResultTypeDef",
    "CreateCacheSecurityGroupMessageRequestTypeDef",
    "CreateCacheSecurityGroupResultTypeDef",
    "CreateCacheSubnetGroupMessageRequestTypeDef",
    "CreateCacheSubnetGroupResultTypeDef",
    "CreateGlobalReplicationGroupMessageRequestTypeDef",
    "CreateGlobalReplicationGroupResultTypeDef",
    "CreateReplicationGroupMessageRequestTypeDef",
    "CreateReplicationGroupResultTypeDef",
    "CreateSnapshotMessageRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateUserGroupMessageRequestTypeDef",
    "CreateUserMessageRequestTypeDef",
    "CustomerNodeEndpointTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "DecreaseReplicaCountMessageRequestTypeDef",
    "DecreaseReplicaCountResultTypeDef",
    "DeleteCacheClusterMessageRequestTypeDef",
    "DeleteCacheClusterResultTypeDef",
    "DeleteCacheParameterGroupMessageRequestTypeDef",
    "DeleteCacheSecurityGroupMessageRequestTypeDef",
    "DeleteCacheSubnetGroupMessageRequestTypeDef",
    "DeleteGlobalReplicationGroupMessageRequestTypeDef",
    "DeleteGlobalReplicationGroupResultTypeDef",
    "DeleteReplicationGroupMessageRequestTypeDef",
    "DeleteReplicationGroupResultTypeDef",
    "DeleteSnapshotMessageRequestTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteUserGroupMessageRequestTypeDef",
    "DeleteUserMessageRequestTypeDef",
    "DescribeCacheClustersMessageRequestTypeDef",
    "DescribeCacheEngineVersionsMessageRequestTypeDef",
    "DescribeCacheParameterGroupsMessageRequestTypeDef",
    "DescribeCacheParametersMessageRequestTypeDef",
    "DescribeCacheSecurityGroupsMessageRequestTypeDef",
    "DescribeCacheSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeGlobalReplicationGroupsMessageRequestTypeDef",
    "DescribeGlobalReplicationGroupsResultTypeDef",
    "DescribeReplicationGroupsMessageRequestTypeDef",
    "DescribeReservedCacheNodesMessageRequestTypeDef",
    "DescribeReservedCacheNodesOfferingsMessageRequestTypeDef",
    "DescribeServiceUpdatesMessageRequestTypeDef",
    "DescribeSnapshotsListMessageTypeDef",
    "DescribeSnapshotsMessageRequestTypeDef",
    "DescribeUpdateActionsMessageRequestTypeDef",
    "DescribeUserGroupsMessageRequestTypeDef",
    "DescribeUserGroupsResultTypeDef",
    "DescribeUsersMessageRequestTypeDef",
    "DescribeUsersResultTypeDef",
    "DestinationDetailsTypeDef",
    "DisassociateGlobalReplicationGroupMessageRequestTypeDef",
    "DisassociateGlobalReplicationGroupResultTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverGlobalReplicationGroupMessageRequestTypeDef",
    "FailoverGlobalReplicationGroupResultTypeDef",
    "FilterTypeDef",
    "GlobalNodeGroupTypeDef",
    "GlobalReplicationGroupInfoTypeDef",
    "GlobalReplicationGroupMemberTypeDef",
    "GlobalReplicationGroupTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "IncreaseReplicaCountMessageRequestTypeDef",
    "IncreaseReplicaCountResultTypeDef",
    "KinesisFirehoseDestinationDetailsTypeDef",
    "ListAllowedNodeTypeModificationsMessageRequestTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "LogDeliveryConfigurationRequestTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "ModifyCacheClusterMessageRequestTypeDef",
    "ModifyCacheClusterResultTypeDef",
    "ModifyCacheParameterGroupMessageRequestTypeDef",
    "ModifyCacheSubnetGroupMessageRequestTypeDef",
    "ModifyCacheSubnetGroupResultTypeDef",
    "ModifyGlobalReplicationGroupMessageRequestTypeDef",
    "ModifyGlobalReplicationGroupResultTypeDef",
    "ModifyReplicationGroupMessageRequestTypeDef",
    "ModifyReplicationGroupResultTypeDef",
    "ModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    "ModifyUserGroupMessageRequestTypeDef",
    "ModifyUserMessageRequestTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeGroupMemberTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "NodeGroupTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "NodeSnapshotTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingLogDeliveryConfigurationTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessedUpdateActionTypeDef",
    "PurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    "RebootCacheClusterMessageRequestTypeDef",
    "RebootCacheClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "RegionalConfigurationTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReplicationGroupMessageTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "ReplicationGroupTypeDef",
    "ReservedCacheNodeMessageTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodesOfferingMessageTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ResetCacheParameterGroupMessageRequestTypeDef",
    "ReshardingConfigurationTypeDef",
    "ReshardingStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeCacheSecurityGroupIngressMessageRequestTypeDef",
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServiceUpdateTypeDef",
    "ServiceUpdatesMessageTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "StartMigrationMessageRequestTypeDef",
    "StartMigrationResponseTypeDef",
    "SubnetOutpostTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TestFailoverMessageRequestTypeDef",
    "TestFailoverResultTypeDef",
    "TimeRangeFilterTypeDef",
    "UnprocessedUpdateActionTypeDef",
    "UpdateActionResultsMessageTypeDef",
    "UpdateActionTypeDef",
    "UpdateActionsMessageTypeDef",
    "UserGroupPendingChangesTypeDef",
    "UserGroupResponseMetadataTypeDef",
    "UserGroupTypeDef",
    "UserGroupsUpdateStatusTypeDef",
    "UserResponseMetadataTypeDef",
    "UserTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

AllowedNodeTypeModificationsMessageTypeDef = TypedDict(
    "AllowedNodeTypeModificationsMessageTypeDef",
    {
        "ScaleUpModifications": List[str],
        "ScaleDownModifications": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": NotRequired[AuthenticationTypeType],
        "PasswordCount": NotRequired[int],
    },
)

AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)

AuthorizeCacheSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)

BatchApplyUpdateActionMessageRequestTypeDef = TypedDict(
    "BatchApplyUpdateActionMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
    },
)

BatchStopUpdateActionMessageRequestTypeDef = TypedDict(
    "BatchStopUpdateActionMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
    },
)

CacheClusterMessageTypeDef = TypedDict(
    "CacheClusterMessageTypeDef",
    {
        "Marker": str,
        "CacheClusters": List["CacheClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheClusterTypeDef = TypedDict(
    "CacheClusterTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "ConfigurationEndpoint": NotRequired["EndpointTypeDef"],
        "ClientDownloadLandingPage": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "NumCacheNodes": NotRequired[int],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredOutpostArn": NotRequired[str],
        "CacheClusterCreateTime": NotRequired[datetime],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired["PendingModifiedValuesTypeDef"],
        "NotificationConfiguration": NotRequired["NotificationConfigurationTypeDef"],
        "CacheSecurityGroups": NotRequired[List["CacheSecurityGroupMembershipTypeDef"]],
        "CacheParameterGroup": NotRequired["CacheParameterGroupStatusTypeDef"],
        "CacheSubnetGroupName": NotRequired[str],
        "CacheNodes": NotRequired[List["CacheNodeTypeDef"]],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SecurityGroups": NotRequired[List["SecurityGroupMembershipTypeDef"]],
        "ReplicationGroupId": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "AuthTokenEnabled": NotRequired[bool],
        "AuthTokenLastModifiedDate": NotRequired[datetime],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "ARN": NotRequired[str],
        "ReplicationGroupLogDeliveryEnabled": NotRequired[bool],
        "LogDeliveryConfigurations": NotRequired[List["LogDeliveryConfigurationTypeDef"]],
    },
)

CacheEngineVersionMessageTypeDef = TypedDict(
    "CacheEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List["CacheEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheEngineVersionTypeDef = TypedDict(
    "CacheEngineVersionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "CacheEngineDescription": NotRequired[str],
        "CacheEngineVersionDescription": NotRequired[str],
    },
)

CacheNodeTypeDef = TypedDict(
    "CacheNodeTypeDef",
    {
        "CacheNodeId": NotRequired[str],
        "CacheNodeStatus": NotRequired[str],
        "CacheNodeCreateTime": NotRequired[datetime],
        "Endpoint": NotRequired["EndpointTypeDef"],
        "ParameterGroupStatus": NotRequired[str],
        "SourceCacheNodeId": NotRequired[str],
        "CustomerAvailabilityZone": NotRequired[str],
        "CustomerOutpostArn": NotRequired[str],
    },
)

CacheNodeTypeSpecificParameterTypeDef = TypedDict(
    "CacheNodeTypeSpecificParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "CacheNodeTypeSpecificValues": NotRequired[List["CacheNodeTypeSpecificValueTypeDef"]],
        "ChangeType": NotRequired[ChangeTypeType],
    },
)

CacheNodeTypeSpecificValueTypeDef = TypedDict(
    "CacheNodeTypeSpecificValueTypeDef",
    {
        "CacheNodeType": NotRequired[str],
        "Value": NotRequired[str],
    },
)

CacheNodeUpdateStatusTypeDef = TypedDict(
    "CacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": NotRequired[str],
        "NodeUpdateStatus": NotRequired[NodeUpdateStatusType],
        "NodeDeletionDate": NotRequired[datetime],
        "NodeUpdateStartDate": NotRequired[datetime],
        "NodeUpdateEndDate": NotRequired[datetime],
        "NodeUpdateInitiatedBy": NotRequired[NodeUpdateInitiatedByType],
        "NodeUpdateInitiatedDate": NotRequired[datetime],
        "NodeUpdateStatusModifiedDate": NotRequired[datetime],
    },
)

CacheParameterGroupDetailsTypeDef = TypedDict(
    "CacheParameterGroupDetailsTypeDef",
    {
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
        "CacheNodeTypeSpecificParameters": List["CacheNodeTypeSpecificParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheParameterGroupNameMessageTypeDef = TypedDict(
    "CacheParameterGroupNameMessageTypeDef",
    {
        "CacheParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheParameterGroupStatusTypeDef = TypedDict(
    "CacheParameterGroupStatusTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "CacheNodeIdsToReboot": NotRequired[List[str]],
    },
)

CacheParameterGroupTypeDef = TypedDict(
    "CacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "IsGlobal": NotRequired[bool],
        "ARN": NotRequired[str],
    },
)

CacheParameterGroupsMessageTypeDef = TypedDict(
    "CacheParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List["CacheParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSecurityGroupMembershipTypeDef = TypedDict(
    "CacheSecurityGroupMembershipTypeDef",
    {
        "CacheSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

CacheSecurityGroupMessageTypeDef = TypedDict(
    "CacheSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List["CacheSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSecurityGroupTypeDef = TypedDict(
    "CacheSecurityGroupTypeDef",
    {
        "OwnerId": NotRequired[str],
        "CacheSecurityGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "EC2SecurityGroups": NotRequired[List["EC2SecurityGroupTypeDef"]],
        "ARN": NotRequired[str],
    },
)

CacheSubnetGroupMessageTypeDef = TypedDict(
    "CacheSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List["CacheSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSubnetGroupTypeDef = TypedDict(
    "CacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": NotRequired[str],
        "CacheSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List["SubnetTypeDef"]],
        "ARN": NotRequired[str],
    },
)

CloudWatchLogsDestinationDetailsTypeDef = TypedDict(
    "CloudWatchLogsDestinationDetailsTypeDef",
    {
        "LogGroup": NotRequired[str],
    },
)

CompleteMigrationMessageRequestTypeDef = TypedDict(
    "CompleteMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "Force": NotRequired[bool],
    },
)

CompleteMigrationResponseTypeDef = TypedDict(
    "CompleteMigrationResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigureShardTypeDef = TypedDict(
    "ConfigureShardTypeDef",
    {
        "NodeGroupId": str,
        "NewReplicaCount": int,
        "PreferredAvailabilityZones": NotRequired[Sequence[str]],
        "PreferredOutpostArns": NotRequired[Sequence[str]],
    },
)

CopySnapshotMessageRequestTypeDef = TypedDict(
    "CopySnapshotMessageRequestTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
        "TargetBucket": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCacheClusterMessageRequestTypeDef = TypedDict(
    "CreateCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "ReplicationGroupId": NotRequired[str],
        "AZMode": NotRequired[AZModeType],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredAvailabilityZones": NotRequired[Sequence[str]],
        "NumCacheNodes": NotRequired[int],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "CacheSubnetGroupName": NotRequired[str],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "SnapshotArns": NotRequired[Sequence[str]],
        "SnapshotName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Port": NotRequired[int],
        "NotificationTopicArn": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "AuthToken": NotRequired[str],
        "OutpostMode": NotRequired[OutpostModeType],
        "PreferredOutpostArn": NotRequired[str],
        "PreferredOutpostArns": NotRequired[Sequence[str]],
        "LogDeliveryConfigurations": NotRequired[
            Sequence["LogDeliveryConfigurationRequestTypeDef"]
        ],
    },
)

CreateCacheClusterResultTypeDef = TypedDict(
    "CreateCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCacheParameterGroupResultTypeDef = TypedDict(
    "CreateCacheParameterGroupResultTypeDef",
    {
        "CacheParameterGroup": "CacheParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "CreateCacheSecurityGroupMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "Description": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCacheSecurityGroupResultTypeDef = TypedDict(
    "CreateCacheSecurityGroupResultTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCacheSubnetGroupResultTypeDef = TypedDict(
    "CreateCacheSubnetGroupResultTypeDef",
    {
        "CacheSubnetGroup": "CacheSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "CreateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupIdSuffix": str,
        "PrimaryReplicationGroupId": str,
        "GlobalReplicationGroupDescription": NotRequired[str],
    },
)

CreateGlobalReplicationGroupResultTypeDef = TypedDict(
    "CreateGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicationGroupMessageRequestTypeDef = TypedDict(
    "CreateReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "GlobalReplicationGroupId": NotRequired[str],
        "PrimaryClusterId": NotRequired[str],
        "AutomaticFailoverEnabled": NotRequired[bool],
        "MultiAZEnabled": NotRequired[bool],
        "NumCacheClusters": NotRequired[int],
        "PreferredCacheClusterAZs": NotRequired[Sequence[str]],
        "NumNodeGroups": NotRequired[int],
        "ReplicasPerNodeGroup": NotRequired[int],
        "NodeGroupConfiguration": NotRequired[Sequence["NodeGroupConfigurationTypeDef"]],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "CacheSubnetGroupName": NotRequired[str],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "SnapshotArns": NotRequired[Sequence[str]],
        "SnapshotName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Port": NotRequired[int],
        "NotificationTopicArn": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "AuthToken": NotRequired[str],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "UserGroupIds": NotRequired[Sequence[str]],
        "LogDeliveryConfigurations": NotRequired[
            Sequence["LogDeliveryConfigurationRequestTypeDef"]
        ],
        "DataTieringEnabled": NotRequired[bool],
    },
)

CreateReplicationGroupResultTypeDef = TypedDict(
    "CreateReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotMessageRequestTypeDef = TypedDict(
    "CreateSnapshotMessageRequestTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserGroupMessageRequestTypeDef = TypedDict(
    "CreateUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
        "Engine": str,
        "UserIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserMessageRequestTypeDef = TypedDict(
    "CreateUserMessageRequestTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Engine": str,
        "AccessString": str,
        "Passwords": NotRequired[Sequence[str]],
        "NoPasswordRequired": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CustomerNodeEndpointTypeDef = TypedDict(
    "CustomerNodeEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)

DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
        "GlobalNodeGroupsToRemove": NotRequired[Sequence[str]],
        "GlobalNodeGroupsToRetain": NotRequired[Sequence[str]],
    },
)

DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DecreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "DecreaseReplicaCountMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
        "NewReplicaCount": NotRequired[int],
        "ReplicaConfiguration": NotRequired[Sequence["ConfigureShardTypeDef"]],
        "ReplicasToRemove": NotRequired[Sequence[str]],
    },
)

DecreaseReplicaCountResultTypeDef = TypedDict(
    "DecreaseReplicaCountResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCacheClusterMessageRequestTypeDef = TypedDict(
    "DeleteCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "FinalSnapshotIdentifier": NotRequired[str],
    },
)

DeleteCacheClusterResultTypeDef = TypedDict(
    "DeleteCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)

DeleteCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheSecurityGroupMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
    },
)

DeleteCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
    },
)

DeleteGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "RetainPrimaryReplicationGroup": bool,
    },
)

DeleteGlobalReplicationGroupResultTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationGroupMessageRequestTypeDef = TypedDict(
    "DeleteReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "RetainPrimaryCluster": NotRequired[bool],
        "FinalSnapshotIdentifier": NotRequired[str],
    },
)

DeleteReplicationGroupResultTypeDef = TypedDict(
    "DeleteReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotMessageRequestTypeDef",
    {
        "SnapshotName": str,
    },
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserGroupMessageRequestTypeDef = TypedDict(
    "DeleteUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
    },
)

DeleteUserMessageRequestTypeDef = TypedDict(
    "DeleteUserMessageRequestTypeDef",
    {
        "UserId": str,
    },
)

DescribeCacheClustersMessageRequestTypeDef = TypedDict(
    "DescribeCacheClustersMessageRequestTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "ShowCacheNodeInfo": NotRequired[bool],
        "ShowCacheClustersNotInReplicationGroups": NotRequired[bool],
    },
)

DescribeCacheEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeCacheEngineVersionsMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
    },
)

DescribeCacheParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheParameterGroupsMessageRequestTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeCacheParametersMessageRequestTypeDef = TypedDict(
    "DescribeCacheParametersMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "Source": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeCacheSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeCacheSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "CacheParameterGroupFamily": str,
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

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Duration": NotRequired[int],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeGlobalReplicationGroupsMessageRequestTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "ShowMemberInfo": NotRequired[bool],
    },
)

DescribeGlobalReplicationGroupsResultTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsResultTypeDef",
    {
        "Marker": str,
        "GlobalReplicationGroups": List["GlobalReplicationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageRequestTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReservedCacheNodesMessageRequestTypeDef = TypedDict(
    "DescribeReservedCacheNodesMessageRequestTypeDef",
    {
        "ReservedCacheNodeId": NotRequired[str],
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReservedCacheNodesOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsMessageRequestTypeDef",
    {
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeServiceUpdatesMessageRequestTypeDef = TypedDict(
    "DescribeServiceUpdatesMessageRequestTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateStatus": NotRequired[Sequence[ServiceUpdateStatusType]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeSnapshotsListMessageTypeDef = TypedDict(
    "DescribeSnapshotsListMessageTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotsMessageRequestTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "SnapshotName": NotRequired[str],
        "SnapshotSource": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "ShowNodeGroupConfig": NotRequired[bool],
    },
)

DescribeUpdateActionsMessageRequestTypeDef = TypedDict(
    "DescribeUpdateActionsMessageRequestTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
        "Engine": NotRequired[str],
        "ServiceUpdateStatus": NotRequired[Sequence[ServiceUpdateStatusType]],
        "ServiceUpdateTimeRange": NotRequired["TimeRangeFilterTypeDef"],
        "UpdateActionStatus": NotRequired[Sequence[UpdateActionStatusType]],
        "ShowNodeLevelUpdateStatus": NotRequired[bool],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeUserGroupsMessageRequestTypeDef = TypedDict(
    "DescribeUserGroupsMessageRequestTypeDef",
    {
        "UserGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeUserGroupsResultTypeDef = TypedDict(
    "DescribeUserGroupsResultTypeDef",
    {
        "UserGroups": List["UserGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersMessageRequestTypeDef = TypedDict(
    "DescribeUsersMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "UserId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef",
    {
        "Users": List["UserTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationDetailsTypeDef = TypedDict(
    "DestinationDetailsTypeDef",
    {
        "CloudWatchLogsDetails": NotRequired["CloudWatchLogsDestinationDetailsTypeDef"],
        "KinesisFirehoseDetails": NotRequired["KinesisFirehoseDestinationDetailsTypeDef"],
    },
)

DisassociateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
    },
)

DisassociateGlobalReplicationGroupResultTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": NotRequired[str],
        "Marker": NotRequired[str],
        "Parameters": NotRequired[List["ParameterTypeDef"]],
        "CacheNodeTypeSpecificParameters": NotRequired[
            List["CacheNodeTypeSpecificParameterTypeDef"]
        ],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "Date": NotRequired[datetime],
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

FailoverGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "PrimaryRegion": str,
        "PrimaryReplicationGroupId": str,
    },
)

FailoverGlobalReplicationGroupResultTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
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

GlobalNodeGroupTypeDef = TypedDict(
    "GlobalNodeGroupTypeDef",
    {
        "GlobalNodeGroupId": NotRequired[str],
        "Slots": NotRequired[str],
    },
)

GlobalReplicationGroupInfoTypeDef = TypedDict(
    "GlobalReplicationGroupInfoTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "GlobalReplicationGroupMemberRole": NotRequired[str],
    },
)

GlobalReplicationGroupMemberTypeDef = TypedDict(
    "GlobalReplicationGroupMemberTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "ReplicationGroupRegion": NotRequired[str],
        "Role": NotRequired[str],
        "AutomaticFailover": NotRequired[AutomaticFailoverStatusType],
        "Status": NotRequired[str],
    },
)

GlobalReplicationGroupTypeDef = TypedDict(
    "GlobalReplicationGroupTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "GlobalReplicationGroupDescription": NotRequired[str],
        "Status": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Members": NotRequired[List["GlobalReplicationGroupMemberTypeDef"]],
        "ClusterEnabled": NotRequired[bool],
        "GlobalNodeGroups": NotRequired[List["GlobalNodeGroupTypeDef"]],
        "AuthTokenEnabled": NotRequired[bool],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "ARN": NotRequired[str],
    },
)

IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
        "RegionalConfigurations": NotRequired[Sequence["RegionalConfigurationTypeDef"]],
    },
)

IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "IncreaseReplicaCountMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
        "NewReplicaCount": NotRequired[int],
        "ReplicaConfiguration": NotRequired[Sequence["ConfigureShardTypeDef"]],
    },
)

IncreaseReplicaCountResultTypeDef = TypedDict(
    "IncreaseReplicaCountResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisFirehoseDestinationDetailsTypeDef = TypedDict(
    "KinesisFirehoseDestinationDetailsTypeDef",
    {
        "DeliveryStream": NotRequired[str],
    },
)

ListAllowedNodeTypeModificationsMessageRequestTypeDef = TypedDict(
    "ListAllowedNodeTypeModificationsMessageRequestTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "ReplicationGroupId": NotRequired[str],
    },
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
    },
)

LogDeliveryConfigurationRequestTypeDef = TypedDict(
    "LogDeliveryConfigurationRequestTypeDef",
    {
        "LogType": NotRequired[LogTypeType],
        "DestinationType": NotRequired[DestinationTypeType],
        "DestinationDetails": NotRequired["DestinationDetailsTypeDef"],
        "LogFormat": NotRequired[LogFormatType],
        "Enabled": NotRequired[bool],
    },
)

LogDeliveryConfigurationTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeDef",
    {
        "LogType": NotRequired[LogTypeType],
        "DestinationType": NotRequired[DestinationTypeType],
        "DestinationDetails": NotRequired["DestinationDetailsTypeDef"],
        "LogFormat": NotRequired[LogFormatType],
        "Status": NotRequired[LogDeliveryConfigurationStatusType],
        "Message": NotRequired[str],
    },
)

ModifyCacheClusterMessageRequestTypeDef = TypedDict(
    "ModifyCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "NumCacheNodes": NotRequired[int],
        "CacheNodeIdsToRemove": NotRequired[Sequence[str]],
        "AZMode": NotRequired[AZModeType],
        "NewAvailabilityZones": NotRequired[Sequence[str]],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationTopicArn": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "NotificationTopicStatus": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "AuthToken": NotRequired[str],
        "AuthTokenUpdateStrategy": NotRequired[AuthTokenUpdateStrategyTypeType],
        "LogDeliveryConfigurations": NotRequired[
            Sequence["LogDeliveryConfigurationRequestTypeDef"]
        ],
    },
)

ModifyCacheClusterResultTypeDef = TypedDict(
    "ModifyCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterNameValues": Sequence["ParameterNameValueTypeDef"],
    },
)

ModifyCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)

ModifyCacheSubnetGroupResultTypeDef = TypedDict(
    "ModifyCacheSubnetGroupResultTypeDef",
    {
        "CacheSubnetGroup": "CacheSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "ModifyGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
        "CacheNodeType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "GlobalReplicationGroupDescription": NotRequired[str],
        "AutomaticFailoverEnabled": NotRequired[bool],
    },
)

ModifyGlobalReplicationGroupResultTypeDef = TypedDict(
    "ModifyGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReplicationGroupMessageRequestTypeDef = TypedDict(
    "ModifyReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": NotRequired[str],
        "PrimaryClusterId": NotRequired[str],
        "SnapshottingClusterId": NotRequired[str],
        "AutomaticFailoverEnabled": NotRequired[bool],
        "MultiAZEnabled": NotRequired[bool],
        "NodeGroupId": NotRequired[str],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationTopicArn": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "NotificationTopicStatus": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "AuthToken": NotRequired[str],
        "AuthTokenUpdateStrategy": NotRequired[AuthTokenUpdateStrategyTypeType],
        "UserGroupIdsToAdd": NotRequired[Sequence[str]],
        "UserGroupIdsToRemove": NotRequired[Sequence[str]],
        "RemoveUserGroups": NotRequired[bool],
        "LogDeliveryConfigurations": NotRequired[
            Sequence["LogDeliveryConfigurationRequestTypeDef"]
        ],
    },
)

ModifyReplicationGroupResultTypeDef = TypedDict(
    "ModifyReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReplicationGroupShardConfigurationMessageRequestTypeDef = TypedDict(
    "ModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
        "ReshardingConfiguration": NotRequired[Sequence["ReshardingConfigurationTypeDef"]],
        "NodeGroupsToRemove": NotRequired[Sequence[str]],
        "NodeGroupsToRetain": NotRequired[Sequence[str]],
    },
)

ModifyReplicationGroupShardConfigurationResultTypeDef = TypedDict(
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyUserGroupMessageRequestTypeDef = TypedDict(
    "ModifyUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
        "UserIdsToAdd": NotRequired[Sequence[str]],
        "UserIdsToRemove": NotRequired[Sequence[str]],
    },
)

ModifyUserMessageRequestTypeDef = TypedDict(
    "ModifyUserMessageRequestTypeDef",
    {
        "UserId": str,
        "AccessString": NotRequired[str],
        "AppendAccessString": NotRequired[str],
        "Passwords": NotRequired[Sequence[str]],
        "NoPasswordRequired": NotRequired[bool],
    },
)

NodeGroupConfigurationTypeDef = TypedDict(
    "NodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "Slots": NotRequired[str],
        "ReplicaCount": NotRequired[int],
        "PrimaryAvailabilityZone": NotRequired[str],
        "ReplicaAvailabilityZones": NotRequired[List[str]],
        "PrimaryOutpostArn": NotRequired[str],
        "ReplicaOutpostArns": NotRequired[List[str]],
    },
)

NodeGroupMemberTypeDef = TypedDict(
    "NodeGroupMemberTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "CacheNodeId": NotRequired[str],
        "ReadEndpoint": NotRequired["EndpointTypeDef"],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredOutpostArn": NotRequired[str],
        "CurrentRole": NotRequired[str],
    },
)

NodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "NodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "CacheNodeId": NotRequired[str],
        "NodeUpdateStatus": NotRequired[NodeUpdateStatusType],
        "NodeDeletionDate": NotRequired[datetime],
        "NodeUpdateStartDate": NotRequired[datetime],
        "NodeUpdateEndDate": NotRequired[datetime],
        "NodeUpdateInitiatedBy": NotRequired[NodeUpdateInitiatedByType],
        "NodeUpdateInitiatedDate": NotRequired[datetime],
        "NodeUpdateStatusModifiedDate": NotRequired[datetime],
    },
)

NodeGroupTypeDef = TypedDict(
    "NodeGroupTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "Status": NotRequired[str],
        "PrimaryEndpoint": NotRequired["EndpointTypeDef"],
        "ReaderEndpoint": NotRequired["EndpointTypeDef"],
        "Slots": NotRequired[str],
        "NodeGroupMembers": NotRequired[List["NodeGroupMemberTypeDef"]],
    },
)

NodeGroupUpdateStatusTypeDef = TypedDict(
    "NodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "NodeGroupMemberUpdateStatus": NotRequired[List["NodeGroupMemberUpdateStatusTypeDef"]],
    },
)

NodeSnapshotTypeDef = TypedDict(
    "NodeSnapshotTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "NodeGroupId": NotRequired[str],
        "CacheNodeId": NotRequired[str],
        "NodeGroupConfiguration": NotRequired["NodeGroupConfigurationTypeDef"],
        "CacheSize": NotRequired[str],
        "CacheNodeCreateTime": NotRequired[datetime],
        "SnapshotCreateTime": NotRequired[datetime],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicArn": NotRequired[str],
        "TopicStatus": NotRequired[str],
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

ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
    },
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "ChangeType": NotRequired[ChangeTypeType],
    },
)

PendingLogDeliveryConfigurationTypeDef = TypedDict(
    "PendingLogDeliveryConfigurationTypeDef",
    {
        "LogType": NotRequired[LogTypeType],
        "DestinationType": NotRequired[DestinationTypeType],
        "DestinationDetails": NotRequired["DestinationDetailsTypeDef"],
        "LogFormat": NotRequired[LogFormatType],
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": NotRequired[int],
        "CacheNodeIdsToRemove": NotRequired[List[str]],
        "EngineVersion": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "AuthTokenStatus": NotRequired[AuthTokenUpdateStatusType],
        "LogDeliveryConfigurations": NotRequired[List["PendingLogDeliveryConfigurationTypeDef"]],
    },
)

ProcessedUpdateActionTypeDef = TypedDict(
    "ProcessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "UpdateActionStatus": NotRequired[UpdateActionStatusType],
    },
)

PurchaseReservedCacheNodesOfferingMessageRequestTypeDef = TypedDict(
    "PurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "ReservedCacheNodeId": NotRequired[str],
        "CacheNodeCount": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PurchaseReservedCacheNodesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    {
        "ReservedCacheNode": "ReservedCacheNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)

RebalanceSlotsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootCacheClusterMessageRequestTypeDef = TypedDict(
    "RebootCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeIdsToReboot": Sequence[str],
    },
)

RebootCacheClusterResultTypeDef = TypedDict(
    "RebootCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": NotRequired[float],
        "RecurringChargeFrequency": NotRequired[str],
    },
)

RegionalConfigurationTypeDef = TypedDict(
    "RegionalConfigurationTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
        "ReshardingConfiguration": Sequence["ReshardingConfigurationTypeDef"],
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)

ReplicationGroupMessageTypeDef = TypedDict(
    "ReplicationGroupMessageTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List["ReplicationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": NotRequired[str],
        "AutomaticFailoverStatus": NotRequired[PendingAutomaticFailoverStatusType],
        "Resharding": NotRequired["ReshardingStatusTypeDef"],
        "AuthTokenStatus": NotRequired[AuthTokenUpdateStatusType],
        "UserGroups": NotRequired["UserGroupsUpdateStatusTypeDef"],
        "LogDeliveryConfigurations": NotRequired[List["PendingLogDeliveryConfigurationTypeDef"]],
    },
)

ReplicationGroupTypeDef = TypedDict(
    "ReplicationGroupTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "Description": NotRequired[str],
        "GlobalReplicationGroupInfo": NotRequired["GlobalReplicationGroupInfoTypeDef"],
        "Status": NotRequired[str],
        "PendingModifiedValues": NotRequired["ReplicationGroupPendingModifiedValuesTypeDef"],
        "MemberClusters": NotRequired[List[str]],
        "NodeGroups": NotRequired[List["NodeGroupTypeDef"]],
        "SnapshottingClusterId": NotRequired[str],
        "AutomaticFailover": NotRequired[AutomaticFailoverStatusType],
        "MultiAZ": NotRequired[MultiAZStatusType],
        "ConfigurationEndpoint": NotRequired["EndpointTypeDef"],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "ClusterEnabled": NotRequired[bool],
        "CacheNodeType": NotRequired[str],
        "AuthTokenEnabled": NotRequired[bool],
        "AuthTokenLastModifiedDate": NotRequired[datetime],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "MemberClustersOutpostArns": NotRequired[List[str]],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "UserGroupIds": NotRequired[List[str]],
        "LogDeliveryConfigurations": NotRequired[List["LogDeliveryConfigurationTypeDef"]],
        "ReplicationGroupCreateTime": NotRequired[datetime],
        "DataTiering": NotRequired[DataTieringStatusType],
    },
)

ReservedCacheNodeMessageTypeDef = TypedDict(
    "ReservedCacheNodeMessageTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List["ReservedCacheNodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedCacheNodeTypeDef = TypedDict(
    "ReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": NotRequired[str],
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CacheNodeCount": NotRequired[int],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "State": NotRequired[str],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
        "ReservationARN": NotRequired[str],
    },
)

ReservedCacheNodesOfferingMessageTypeDef = TypedDict(
    "ReservedCacheNodesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List["ReservedCacheNodesOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedCacheNodesOfferingTypeDef = TypedDict(
    "ReservedCacheNodesOfferingTypeDef",
    {
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
    },
)

ResetCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "ParameterNameValues": NotRequired[Sequence["ParameterNameValueTypeDef"]],
    },
)

ReshardingConfigurationTypeDef = TypedDict(
    "ReshardingConfigurationTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "PreferredAvailabilityZones": NotRequired[Sequence[str]],
    },
)

ReshardingStatusTypeDef = TypedDict(
    "ReshardingStatusTypeDef",
    {
        "SlotMigration": NotRequired["SlotMigrationTypeDef"],
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

RevokeCacheSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)

RevokeCacheSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateReleaseDate": NotRequired[datetime],
        "ServiceUpdateEndDate": NotRequired[datetime],
        "ServiceUpdateSeverity": NotRequired[ServiceUpdateSeverityType],
        "ServiceUpdateRecommendedApplyByDate": NotRequired[datetime],
        "ServiceUpdateStatus": NotRequired[ServiceUpdateStatusType],
        "ServiceUpdateDescription": NotRequired[str],
        "ServiceUpdateType": NotRequired[Literal["security-update"]],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "AutoUpdateAfterRecommendedApplyByDate": NotRequired[bool],
        "EstimatedUpdateTime": NotRequired[str],
    },
)

ServiceUpdatesMessageTypeDef = TypedDict(
    "ServiceUpdatesMessageTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List["ServiceUpdateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SlotMigrationTypeDef = TypedDict(
    "SlotMigrationTypeDef",
    {
        "ProgressPercentage": NotRequired[float],
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotName": NotRequired[str],
        "ReplicationGroupId": NotRequired[str],
        "ReplicationGroupDescription": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "SnapshotStatus": NotRequired[str],
        "SnapshotSource": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "NumCacheNodes": NotRequired[int],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredOutpostArn": NotRequired[str],
        "CacheClusterCreateTime": NotRequired[datetime],
        "PreferredMaintenanceWindow": NotRequired[str],
        "TopicArn": NotRequired[str],
        "Port": NotRequired[int],
        "CacheParameterGroupName": NotRequired[str],
        "CacheSubnetGroupName": NotRequired[str],
        "VpcId": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "NumNodeGroups": NotRequired[int],
        "AutomaticFailover": NotRequired[AutomaticFailoverStatusType],
        "NodeSnapshots": NotRequired[List["NodeSnapshotTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "DataTiering": NotRequired[DataTieringStatusType],
    },
)

StartMigrationMessageRequestTypeDef = TypedDict(
    "StartMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "CustomerNodeEndpointList": Sequence["CustomerNodeEndpointTypeDef"],
    },
)

StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetOutpostTypeDef = TypedDict(
    "SubnetOutpostTypeDef",
    {
        "SubnetOutpostArn": NotRequired[str],
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired["AvailabilityZoneTypeDef"],
        "SubnetOutpost": NotRequired["SubnetOutpostTypeDef"],
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

TestFailoverMessageRequestTypeDef = TypedDict(
    "TestFailoverMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupId": str,
    },
)

TestFailoverResultTypeDef = TypedDict(
    "TestFailoverResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimeRangeFilterTypeDef = TypedDict(
    "TimeRangeFilterTypeDef",
    {
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
    },
)

UnprocessedUpdateActionTypeDef = TypedDict(
    "UnprocessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "ErrorType": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

UpdateActionResultsMessageTypeDef = TypedDict(
    "UpdateActionResultsMessageTypeDef",
    {
        "ProcessedUpdateActions": List["ProcessedUpdateActionTypeDef"],
        "UnprocessedUpdateActions": List["UnprocessedUpdateActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateActionTypeDef = TypedDict(
    "UpdateActionTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateReleaseDate": NotRequired[datetime],
        "ServiceUpdateSeverity": NotRequired[ServiceUpdateSeverityType],
        "ServiceUpdateStatus": NotRequired[ServiceUpdateStatusType],
        "ServiceUpdateRecommendedApplyByDate": NotRequired[datetime],
        "ServiceUpdateType": NotRequired[Literal["security-update"]],
        "UpdateActionAvailableDate": NotRequired[datetime],
        "UpdateActionStatus": NotRequired[UpdateActionStatusType],
        "NodesUpdated": NotRequired[str],
        "UpdateActionStatusModifiedDate": NotRequired[datetime],
        "SlaMet": NotRequired[SlaMetType],
        "NodeGroupUpdateStatus": NotRequired[List["NodeGroupUpdateStatusTypeDef"]],
        "CacheNodeUpdateStatus": NotRequired[List["CacheNodeUpdateStatusTypeDef"]],
        "EstimatedUpdateTime": NotRequired[str],
        "Engine": NotRequired[str],
    },
)

UpdateActionsMessageTypeDef = TypedDict(
    "UpdateActionsMessageTypeDef",
    {
        "Marker": str,
        "UpdateActions": List["UpdateActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserGroupPendingChangesTypeDef = TypedDict(
    "UserGroupPendingChangesTypeDef",
    {
        "UserIdsToRemove": NotRequired[List[str]],
        "UserIdsToAdd": NotRequired[List[str]],
    },
)

UserGroupResponseMetadataTypeDef = TypedDict(
    "UserGroupResponseMetadataTypeDef",
    {
        "UserGroupId": str,
        "Status": str,
        "Engine": str,
        "UserIds": List[str],
        "MinimumEngineVersion": str,
        "PendingChanges": "UserGroupPendingChangesTypeDef",
        "ReplicationGroups": List[str],
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserGroupTypeDef = TypedDict(
    "UserGroupTypeDef",
    {
        "UserGroupId": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "UserIds": NotRequired[List[str]],
        "MinimumEngineVersion": NotRequired[str],
        "PendingChanges": NotRequired["UserGroupPendingChangesTypeDef"],
        "ReplicationGroups": NotRequired[List[str]],
        "ARN": NotRequired[str],
    },
)

UserGroupsUpdateStatusTypeDef = TypedDict(
    "UserGroupsUpdateStatusTypeDef",
    {
        "UserGroupIdsToAdd": NotRequired[List[str]],
        "UserGroupIdsToRemove": NotRequired[List[str]],
    },
)

UserResponseMetadataTypeDef = TypedDict(
    "UserResponseMetadataTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Status": str,
        "Engine": str,
        "MinimumEngineVersion": str,
        "AccessString": str,
        "UserGroupIds": List[str],
        "Authentication": "AuthenticationTypeDef",
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "MinimumEngineVersion": NotRequired[str],
        "AccessString": NotRequired[str],
        "UserGroupIds": NotRequired[List[str]],
        "Authentication": NotRequired["AuthenticationTypeDef"],
        "ARN": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
