"""
Type annotations for memorydb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_memorydb.type_defs import ACLPendingChangesTypeDef

    data: ACLPendingChangesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import AuthenticationTypeType, AZStatusType, ServiceUpdateStatusType, SourceTypeType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ACLPendingChangesTypeDef",
    "ACLTypeDef",
    "ACLsUpdateStatusTypeDef",
    "AuthenticationModeTypeDef",
    "AuthenticationTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchUpdateClusterRequestRequestTypeDef",
    "BatchUpdateClusterResponseTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterPendingUpdatesTypeDef",
    "ClusterTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotResponseTypeDef",
    "CreateACLRequestRequestTypeDef",
    "CreateACLResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateParameterGroupRequestRequestTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateSubnetGroupRequestRequestTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteACLRequestRequestTypeDef",
    "DeleteACLResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteParameterGroupRequestRequestTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteSubnetGroupRequestRequestTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeACLsRequestRequestTypeDef",
    "DescribeACLsResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeEngineVersionsRequestRequestTypeDef",
    "DescribeEngineVersionsResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParameterGroupsRequestRequestTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeServiceUpdatesRequestRequestTypeDef",
    "DescribeServiceUpdatesResponseTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResponseTypeDef",
    "DescribeSubnetGroupsRequestRequestTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "DescribeUsersResponseTypeDef",
    "EndpointTypeDef",
    "EngineVersionInfoTypeDef",
    "EventTypeDef",
    "FailoverShardRequestRequestTypeDef",
    "FailoverShardResponseTypeDef",
    "FilterTypeDef",
    "ListAllowedNodeTypeUpdatesRequestRequestTypeDef",
    "ListAllowedNodeTypeUpdatesResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "NodeTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingModifiedServiceUpdateTypeDef",
    "ReplicaConfigurationRequestTypeDef",
    "ResetParameterGroupRequestRequestTypeDef",
    "ResetParameterGroupResponseTypeDef",
    "ReshardingStatusTypeDef",
    "ResponseMetadataTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServiceUpdateRequestTypeDef",
    "ServiceUpdateTypeDef",
    "ShardConfigurationRequestTypeDef",
    "ShardConfigurationTypeDef",
    "ShardDetailTypeDef",
    "ShardTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "UnprocessedClusterTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateACLRequestRequestTypeDef",
    "UpdateACLResponseTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateParameterGroupRequestRequestTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "UpdateSubnetGroupRequestRequestTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserTypeDef",
)

ACLPendingChangesTypeDef = TypedDict(
    "ACLPendingChangesTypeDef",
    {
        "UserNamesToRemove": NotRequired[List[str]],
        "UserNamesToAdd": NotRequired[List[str]],
    },
)

ACLTypeDef = TypedDict(
    "ACLTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "UserNames": NotRequired[List[str]],
        "MinimumEngineVersion": NotRequired[str],
        "PendingChanges": NotRequired["ACLPendingChangesTypeDef"],
        "Clusters": NotRequired[List[str]],
        "ARN": NotRequired[str],
    },
)

ACLsUpdateStatusTypeDef = TypedDict(
    "ACLsUpdateStatusTypeDef",
    {
        "ACLToApply": NotRequired[str],
    },
)

AuthenticationModeTypeDef = TypedDict(
    "AuthenticationModeTypeDef",
    {
        "Type": NotRequired[Literal["password"]],
        "Passwords": NotRequired[Sequence[str]],
    },
)

AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": NotRequired[AuthenticationTypeType],
        "PasswordCount": NotRequired[int],
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)

BatchUpdateClusterRequestRequestTypeDef = TypedDict(
    "BatchUpdateClusterRequestRequestTypeDef",
    {
        "ClusterNames": Sequence[str],
        "ServiceUpdate": NotRequired["ServiceUpdateRequestTypeDef"],
    },
)

BatchUpdateClusterResponseTypeDef = TypedDict(
    "BatchUpdateClusterResponseTypeDef",
    {
        "ProcessedClusters": List["ClusterTypeDef"],
        "UnprocessedClusters": List["UnprocessedClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "NodeType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "MaintenanceWindow": NotRequired[str],
        "TopicArn": NotRequired[str],
        "Port": NotRequired[int],
        "ParameterGroupName": NotRequired[str],
        "SubnetGroupName": NotRequired[str],
        "VpcId": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "NumShards": NotRequired[int],
        "Shards": NotRequired[List["ShardDetailTypeDef"]],
    },
)

ClusterPendingUpdatesTypeDef = TypedDict(
    "ClusterPendingUpdatesTypeDef",
    {
        "Resharding": NotRequired["ReshardingStatusTypeDef"],
        "ACLs": NotRequired["ACLsUpdateStatusTypeDef"],
        "ServiceUpdates": NotRequired[List["PendingModifiedServiceUpdateTypeDef"]],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[str],
        "PendingUpdates": NotRequired["ClusterPendingUpdatesTypeDef"],
        "NumberOfShards": NotRequired[int],
        "Shards": NotRequired[List["ShardTypeDef"]],
        "AvailabilityMode": NotRequired[AZStatusType],
        "ClusterEndpoint": NotRequired["EndpointTypeDef"],
        "NodeType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EnginePatchVersion": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
        "ParameterGroupStatus": NotRequired[str],
        "SecurityGroups": NotRequired[List["SecurityGroupMembershipTypeDef"]],
        "SubnetGroupName": NotRequired[str],
        "TLSEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicStatus": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "MaintenanceWindow": NotRequired[str],
        "SnapshotWindow": NotRequired[str],
        "ACLName": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
    },
)

CopySnapshotRequestRequestTypeDef = TypedDict(
    "CopySnapshotRequestRequestTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
        "TargetBucket": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopySnapshotResponseTypeDef = TypedDict(
    "CopySnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateACLRequestRequestTypeDef = TypedDict(
    "CreateACLRequestRequestTypeDef",
    {
        "ACLName": str,
        "UserNames": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateACLResponseTypeDef = TypedDict(
    "CreateACLResponseTypeDef",
    {
        "ACL": "ACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeType": str,
        "ACLName": str,
        "ParameterGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "NumShards": NotRequired[int],
        "NumReplicasPerShard": NotRequired[int],
        "SubnetGroupName": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "MaintenanceWindow": NotRequired[str],
        "Port": NotRequired[int],
        "SnsTopicArn": NotRequired[str],
        "TLSEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "SnapshotArns": NotRequired[Sequence[str]],
        "SnapshotName": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "SnapshotWindow": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateParameterGroupRequestRequestTypeDef = TypedDict(
    "CreateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Family": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateParameterGroupResponseTypeDef = TypedDict(
    "CreateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "ClusterName": str,
        "SnapshotName": str,
        "KmsKeyId": NotRequired[str],
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

CreateSubnetGroupRequestRequestTypeDef = TypedDict(
    "CreateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSubnetGroupResponseTypeDef = TypedDict(
    "CreateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationMode": "AuthenticationModeTypeDef",
        "AccessString": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteACLRequestRequestTypeDef = TypedDict(
    "DeleteACLRequestRequestTypeDef",
    {
        "ACLName": str,
    },
)

DeleteACLResponseTypeDef = TypedDict(
    "DeleteACLResponseTypeDef",
    {
        "ACL": "ACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "FinalSnapshotName": NotRequired[str],
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteParameterGroupRequestRequestTypeDef = TypedDict(
    "DeleteParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)

DeleteParameterGroupResponseTypeDef = TypedDict(
    "DeleteParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotName": str,
    },
)

DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSubnetGroupRequestRequestTypeDef = TypedDict(
    "DeleteSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
    },
)

DeleteSubnetGroupResponseTypeDef = TypedDict(
    "DeleteSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeACLsRequestRequestTypeDef = TypedDict(
    "DescribeACLsRequestRequestTypeDef",
    {
        "ACLName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeACLsResponseTypeDef = TypedDict(
    "DescribeACLsResponseTypeDef",
    {
        "ACLs": List["ACLTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "ClusterName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ShowShardDetails": NotRequired[bool],
    },
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "NextToken": str,
        "Clusters": List["ClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEngineVersionsRequestRequestTypeDef = TypedDict(
    "DescribeEngineVersionsRequestRequestTypeDef",
    {
        "EngineVersion": NotRequired[str],
        "ParameterGroupFamily": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
    },
)

DescribeEngineVersionsResponseTypeDef = TypedDict(
    "DescribeEngineVersionsResponseTypeDef",
    {
        "NextToken": str,
        "EngineVersions": List["EngineVersionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "SourceName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Duration": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "NextToken": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParameterGroupsRequestRequestTypeDef = TypedDict(
    "DescribeParameterGroupsRequestRequestTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeParameterGroupsResponseTypeDef = TypedDict(
    "DescribeParameterGroupsResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List["ParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParametersRequestRequestTypeDef = TypedDict(
    "DescribeParametersRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeParametersResponseTypeDef = TypedDict(
    "DescribeParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceUpdatesRequestRequestTypeDef = TypedDict(
    "DescribeServiceUpdatesRequestRequestTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ClusterNames": NotRequired[Sequence[str]],
        "Status": NotRequired[Sequence[ServiceUpdateStatusType]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeServiceUpdatesResponseTypeDef = TypedDict(
    "DescribeServiceUpdatesResponseTypeDef",
    {
        "NextToken": str,
        "ServiceUpdates": List["ServiceUpdateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "ClusterName": NotRequired[str],
        "SnapshotName": NotRequired[str],
        "Source": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ShowDetail": NotRequired[bool],
    },
)

DescribeSnapshotsResponseTypeDef = TypedDict(
    "DescribeSnapshotsResponseTypeDef",
    {
        "NextToken": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubnetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestRequestTypeDef",
    {
        "SubnetGroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeSubnetGroupsResponseTypeDef",
    {
        "NextToken": str,
        "SubnetGroups": List["SubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersRequestRequestTypeDef = TypedDict(
    "DescribeUsersRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)

EngineVersionInfoTypeDef = TypedDict(
    "EngineVersionInfoTypeDef",
    {
        "EngineVersion": NotRequired[str],
        "EnginePatchVersion": NotRequired[str],
        "ParameterGroupFamily": NotRequired[str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "Date": NotRequired[datetime],
    },
)

FailoverShardRequestRequestTypeDef = TypedDict(
    "FailoverShardRequestRequestTypeDef",
    {
        "ClusterName": str,
        "ShardName": str,
    },
)

FailoverShardResponseTypeDef = TypedDict(
    "FailoverShardResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

ListAllowedNodeTypeUpdatesRequestRequestTypeDef = TypedDict(
    "ListAllowedNodeTypeUpdatesRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)

ListAllowedNodeTypeUpdatesResponseTypeDef = TypedDict(
    "ListAllowedNodeTypeUpdatesResponseTypeDef",
    {
        "ScaleUpNodeTypes": List[str],
        "ScaleDownNodeTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "Endpoint": NotRequired["EndpointTypeDef"],
    },
)

ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef",
    {
        "Name": NotRequired[str],
        "Family": NotRequired[str],
        "Description": NotRequired[str],
        "ARN": NotRequired[str],
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
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "Description": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "MinimumEngineVersion": NotRequired[str],
    },
)

PendingModifiedServiceUpdateTypeDef = TypedDict(
    "PendingModifiedServiceUpdateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "Status": NotRequired[ServiceUpdateStatusType],
    },
)

ReplicaConfigurationRequestTypeDef = TypedDict(
    "ReplicaConfigurationRequestTypeDef",
    {
        "ReplicaCount": NotRequired[int],
    },
)

ResetParameterGroupRequestRequestTypeDef = TypedDict(
    "ResetParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "AllParameters": NotRequired[bool],
        "ParameterNames": NotRequired[Sequence[str]],
    },
)

ResetParameterGroupResponseTypeDef = TypedDict(
    "ResetParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

ServiceUpdateRequestTypeDef = TypedDict(
    "ServiceUpdateRequestTypeDef",
    {
        "ServiceUpdateNameToApply": NotRequired[str],
    },
)

ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ClusterName": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "ReleaseDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "Status": NotRequired[ServiceUpdateStatusType],
        "Type": NotRequired[Literal["security-update"]],
        "NodesUpdated": NotRequired[str],
        "AutoUpdateStartDate": NotRequired[datetime],
    },
)

ShardConfigurationRequestTypeDef = TypedDict(
    "ShardConfigurationRequestTypeDef",
    {
        "ShardCount": NotRequired[int],
    },
)

ShardConfigurationTypeDef = TypedDict(
    "ShardConfigurationTypeDef",
    {
        "Slots": NotRequired[str],
        "ReplicaCount": NotRequired[int],
    },
)

ShardDetailTypeDef = TypedDict(
    "ShardDetailTypeDef",
    {
        "Name": NotRequired[str],
        "Configuration": NotRequired["ShardConfigurationTypeDef"],
        "Size": NotRequired[str],
        "SnapshotCreationTime": NotRequired[datetime],
    },
)

ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "Slots": NotRequired[str],
        "Nodes": NotRequired[List["NodeTypeDef"]],
        "NumberOfNodes": NotRequired[int],
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
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "Source": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "ClusterConfiguration": NotRequired["ClusterConfigurationTypeDef"],
    },
)

SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List["SubnetTypeDef"]],
        "ARN": NotRequired[str],
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "Identifier": NotRequired[str],
        "AvailabilityZone": NotRequired["AvailabilityZoneTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
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

UnprocessedClusterTypeDef = TypedDict(
    "UnprocessedClusterTypeDef",
    {
        "ClusterName": NotRequired[str],
        "ErrorType": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateACLRequestRequestTypeDef = TypedDict(
    "UpdateACLRequestRequestTypeDef",
    {
        "ACLName": str,
        "UserNamesToAdd": NotRequired[Sequence[str]],
        "UserNamesToRemove": NotRequired[Sequence[str]],
    },
)

UpdateACLResponseTypeDef = TypedDict(
    "UpdateACLResponseTypeDef",
    {
        "ACL": "ACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterRequestRequestTypeDef = TypedDict(
    "UpdateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "Description": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "MaintenanceWindow": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
        "SnapshotWindow": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "NodeType": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "ReplicaConfiguration": NotRequired["ReplicaConfigurationRequestTypeDef"],
        "ShardConfiguration": NotRequired["ShardConfigurationRequestTypeDef"],
        "ACLName": NotRequired[str],
    },
)

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateParameterGroupRequestRequestTypeDef = TypedDict(
    "UpdateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterNameValues": Sequence["ParameterNameValueTypeDef"],
    },
)

UpdateParameterGroupResponseTypeDef = TypedDict(
    "UpdateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSubnetGroupRequestRequestTypeDef = TypedDict(
    "UpdateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "Description": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)

UpdateSubnetGroupResponseTypeDef = TypedDict(
    "UpdateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationMode": NotRequired["AuthenticationModeTypeDef"],
        "AccessString": NotRequired[str],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "AccessString": NotRequired[str],
        "ACLNames": NotRequired[List[str]],
        "MinimumEngineVersion": NotRequired[str],
        "Authentication": NotRequired["AuthenticationTypeDef"],
        "ARN": NotRequired[str],
    },
)
