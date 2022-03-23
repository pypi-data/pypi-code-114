"""
Type annotations for redshift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeInputMessageRequestTypeDef

    data: AcceptReservedNodeExchangeInputMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActionTypeType,
    AquaConfigurationStatusType,
    AquaStatusType,
    AuthorizationStatusType,
    DataShareStatusForConsumerType,
    DataShareStatusForProducerType,
    DataShareStatusType,
    ModeType,
    NodeConfigurationOptionsFilterNameType,
    OperatorTypeType,
    ParameterApplyTypeType,
    PartnerIntegrationStatusType,
    ReservedNodeExchangeActionTypeType,
    ReservedNodeExchangeStatusTypeType,
    ReservedNodeOfferingTypeType,
    ScheduledActionFilterNameType,
    ScheduledActionStateType,
    ScheduledActionTypeValuesType,
    ScheduleStateType,
    SnapshotAttributeToSortByType,
    SortByOrderType,
    SourceTypeType,
    TableRestoreStatusTypeType,
    UsageLimitBreachActionType,
    UsageLimitFeatureTypeType,
    UsageLimitLimitTypeType,
    UsageLimitPeriodType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptReservedNodeExchangeInputMessageRequestTypeDef",
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    "AccountAttributeListTypeDef",
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AquaConfigurationTypeDef",
    "AssociateDataShareConsumerMessageRequestTypeDef",
    "AttributeValueTargetTypeDef",
    "AuthenticationProfileTypeDef",
    "AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    "AuthorizeDataShareMessageRequestTypeDef",
    "AuthorizeEndpointAccessMessageRequestTypeDef",
    "AuthorizeSnapshotAccessMessageRequestTypeDef",
    "AuthorizeSnapshotAccessResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchDeleteClusterSnapshotsRequestRequestTypeDef",
    "BatchDeleteClusterSnapshotsResultTypeDef",
    "BatchModifyClusterSnapshotsMessageRequestTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    "CancelResizeMessageRequestTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterCredentialsTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterGroupDetailsTypeDef",
    "ClusterParameterGroupNameMessageTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterGroupsMessageTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSecurityGroupMessageTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "ClusterSubnetGroupMessageTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterTypeDef",
    "ClusterVersionTypeDef",
    "ClusterVersionsMessageTypeDef",
    "ClustersMessageTypeDef",
    "CopyClusterSnapshotMessageRequestTypeDef",
    "CopyClusterSnapshotResultTypeDef",
    "CreateAuthenticationProfileMessageRequestTypeDef",
    "CreateAuthenticationProfileResultTypeDef",
    "CreateClusterMessageRequestTypeDef",
    "CreateClusterParameterGroupMessageRequestTypeDef",
    "CreateClusterParameterGroupResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateClusterSecurityGroupMessageRequestTypeDef",
    "CreateClusterSecurityGroupResultTypeDef",
    "CreateClusterSnapshotMessageRequestTypeDef",
    "CreateClusterSnapshotResultTypeDef",
    "CreateClusterSubnetGroupMessageRequestTypeDef",
    "CreateClusterSubnetGroupResultTypeDef",
    "CreateEndpointAccessMessageRequestTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateHsmClientCertificateMessageRequestTypeDef",
    "CreateHsmClientCertificateResultTypeDef",
    "CreateHsmConfigurationMessageRequestTypeDef",
    "CreateHsmConfigurationResultTypeDef",
    "CreateScheduledActionMessageRequestTypeDef",
    "CreateSnapshotCopyGrantMessageRequestTypeDef",
    "CreateSnapshotCopyGrantResultTypeDef",
    "CreateSnapshotScheduleMessageRequestTypeDef",
    "CreateTagsMessageRequestTypeDef",
    "CreateUsageLimitMessageRequestTypeDef",
    "CustomerStorageMessageTypeDef",
    "DataShareAssociationTypeDef",
    "DataShareResponseMetadataTypeDef",
    "DataShareTypeDef",
    "DataTransferProgressTypeDef",
    "DeauthorizeDataShareMessageRequestTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "DeleteAuthenticationProfileMessageRequestTypeDef",
    "DeleteAuthenticationProfileResultTypeDef",
    "DeleteClusterMessageRequestTypeDef",
    "DeleteClusterParameterGroupMessageRequestTypeDef",
    "DeleteClusterResultTypeDef",
    "DeleteClusterSecurityGroupMessageRequestTypeDef",
    "DeleteClusterSnapshotMessageRequestTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultTypeDef",
    "DeleteClusterSubnetGroupMessageRequestTypeDef",
    "DeleteEndpointAccessMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteHsmClientCertificateMessageRequestTypeDef",
    "DeleteHsmConfigurationMessageRequestTypeDef",
    "DeleteScheduledActionMessageRequestTypeDef",
    "DeleteSnapshotCopyGrantMessageRequestTypeDef",
    "DeleteSnapshotScheduleMessageRequestTypeDef",
    "DeleteTagsMessageRequestTypeDef",
    "DeleteUsageLimitMessageRequestTypeDef",
    "DescribeAccountAttributesMessageRequestTypeDef",
    "DescribeAuthenticationProfilesMessageRequestTypeDef",
    "DescribeAuthenticationProfilesResultTypeDef",
    "DescribeClusterDbRevisionsMessageRequestTypeDef",
    "DescribeClusterParameterGroupsMessageRequestTypeDef",
    "DescribeClusterParametersMessageRequestTypeDef",
    "DescribeClusterSecurityGroupsMessageRequestTypeDef",
    "DescribeClusterSnapshotsMessageRequestTypeDef",
    "DescribeClusterSubnetGroupsMessageRequestTypeDef",
    "DescribeClusterTracksMessageRequestTypeDef",
    "DescribeClusterVersionsMessageRequestTypeDef",
    "DescribeClustersMessageRequestTypeDef",
    "DescribeDataSharesForConsumerMessageRequestTypeDef",
    "DescribeDataSharesForConsumerResultTypeDef",
    "DescribeDataSharesForProducerMessageRequestTypeDef",
    "DescribeDataSharesForProducerResultTypeDef",
    "DescribeDataSharesMessageRequestTypeDef",
    "DescribeDataSharesResultTypeDef",
    "DescribeDefaultClusterParametersMessageRequestTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "DescribeEndpointAccessMessageRequestTypeDef",
    "DescribeEndpointAuthorizationMessageRequestTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeHsmClientCertificatesMessageRequestTypeDef",
    "DescribeHsmConfigurationsMessageRequestTypeDef",
    "DescribeLoggingStatusMessageRequestTypeDef",
    "DescribeNodeConfigurationOptionsMessageRequestTypeDef",
    "DescribeOrderableClusterOptionsMessageRequestTypeDef",
    "DescribePartnersInputMessageRequestTypeDef",
    "DescribePartnersOutputMessageTypeDef",
    "DescribeReservedNodeExchangeStatusInputMessageRequestTypeDef",
    "DescribeReservedNodeExchangeStatusOutputMessageTypeDef",
    "DescribeReservedNodeOfferingsMessageRequestTypeDef",
    "DescribeReservedNodesMessageRequestTypeDef",
    "DescribeResizeMessageRequestTypeDef",
    "DescribeScheduledActionsMessageRequestTypeDef",
    "DescribeSnapshotCopyGrantsMessageRequestTypeDef",
    "DescribeSnapshotSchedulesMessageRequestTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "DescribeTableRestoreStatusMessageRequestTypeDef",
    "DescribeTagsMessageRequestTypeDef",
    "DescribeUsageLimitsMessageRequestTypeDef",
    "DisableLoggingMessageRequestTypeDef",
    "DisableSnapshotCopyMessageRequestTypeDef",
    "DisableSnapshotCopyResultTypeDef",
    "DisassociateDataShareConsumerMessageRequestTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EnableLoggingMessageRequestTypeDef",
    "EnableSnapshotCopyMessageRequestTypeDef",
    "EnableSnapshotCopyResultTypeDef",
    "EndpointAccessListTypeDef",
    "EndpointAccessResponseMetadataTypeDef",
    "EndpointAccessTypeDef",
    "EndpointAuthorizationListTypeDef",
    "EndpointAuthorizationResponseMetadataTypeDef",
    "EndpointAuthorizationTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "GetClusterCredentialsMessageRequestTypeDef",
    "GetReservedNodeExchangeConfigurationOptionsInputMessageRequestTypeDef",
    "GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef",
    "GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationMessageTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "LoggingStatusTypeDef",
    "MaintenanceTrackTypeDef",
    "ModifyAquaInputMessageRequestTypeDef",
    "ModifyAquaOutputMessageTypeDef",
    "ModifyAuthenticationProfileMessageRequestTypeDef",
    "ModifyAuthenticationProfileResultTypeDef",
    "ModifyClusterDbRevisionMessageRequestTypeDef",
    "ModifyClusterDbRevisionResultTypeDef",
    "ModifyClusterIamRolesMessageRequestTypeDef",
    "ModifyClusterIamRolesResultTypeDef",
    "ModifyClusterMaintenanceMessageRequestTypeDef",
    "ModifyClusterMaintenanceResultTypeDef",
    "ModifyClusterMessageRequestTypeDef",
    "ModifyClusterParameterGroupMessageRequestTypeDef",
    "ModifyClusterResultTypeDef",
    "ModifyClusterSnapshotMessageRequestTypeDef",
    "ModifyClusterSnapshotResultTypeDef",
    "ModifyClusterSnapshotScheduleMessageRequestTypeDef",
    "ModifyClusterSubnetGroupMessageRequestTypeDef",
    "ModifyClusterSubnetGroupResultTypeDef",
    "ModifyEndpointAccessMessageRequestTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyScheduledActionMessageRequestTypeDef",
    "ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    "ModifySnapshotScheduleMessageRequestTypeDef",
    "ModifyUsageLimitMessageRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeConfigurationOptionTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionsMessageTypeDef",
    "OrderableClusterOptionTypeDef",
    "OrderableClusterOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PartnerIntegrationInfoTypeDef",
    "PartnerIntegrationInputMessageRequestTypeDef",
    "PartnerIntegrationOutputMessageTypeDef",
    "PauseClusterMessageRequestTypeDef",
    "PauseClusterMessageTypeDef",
    "PauseClusterResultTypeDef",
    "PendingModifiedValuesTypeDef",
    "PurchaseReservedNodeOfferingMessageRequestTypeDef",
    "PurchaseReservedNodeOfferingResultTypeDef",
    "RebootClusterMessageRequestTypeDef",
    "RebootClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "RejectDataShareMessageRequestTypeDef",
    "ReservedNodeConfigurationOptionTypeDef",
    "ReservedNodeExchangeStatusTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageTypeDef",
    "ResetClusterParameterGroupMessageRequestTypeDef",
    "ResizeClusterMessageRequestTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeClusterResultTypeDef",
    "ResizeInfoTypeDef",
    "ResizeProgressMessageTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromClusterSnapshotMessageRequestTypeDef",
    "RestoreFromClusterSnapshotResultTypeDef",
    "RestoreStatusTypeDef",
    "RestoreTableFromClusterSnapshotMessageRequestTypeDef",
    "RestoreTableFromClusterSnapshotResultTypeDef",
    "ResumeClusterMessageRequestTypeDef",
    "ResumeClusterMessageTypeDef",
    "ResumeClusterResultTypeDef",
    "RevisionTargetTypeDef",
    "RevokeClusterSecurityGroupIngressMessageRequestTypeDef",
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    "RevokeEndpointAccessMessageRequestTypeDef",
    "RevokeSnapshotAccessMessageRequestTypeDef",
    "RevokeSnapshotAccessResultTypeDef",
    "RotateEncryptionKeyMessageRequestTypeDef",
    "RotateEncryptionKeyResultTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionResponseMetadataTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotScheduleResponseMetadataTypeDef",
    "SnapshotScheduleTypeDef",
    "SnapshotSortingEntityTypeDef",
    "SnapshotTypeDef",
    "SubnetTypeDef",
    "SupportedOperationTypeDef",
    "SupportedPlatformTypeDef",
    "TableRestoreStatusMessageTypeDef",
    "TableRestoreStatusTypeDef",
    "TagTypeDef",
    "TaggedResourceListMessageTypeDef",
    "TaggedResourceTypeDef",
    "TrackListMessageTypeDef",
    "UpdatePartnerStatusInputMessageRequestTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitListTypeDef",
    "UsageLimitResponseMetadataTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AcceptReservedNodeExchangeInputMessageRequestTypeDef = TypedDict(
    "AcceptReservedNodeExchangeInputMessageRequestTypeDef",
    {
        "ReservedNodeId": str,
        "TargetReservedNodeOfferingId": str,
    },
)

AcceptReservedNodeExchangeOutputMessageTypeDef = TypedDict(
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    {
        "ExchangedReservedNode": "ReservedNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAttributeListTypeDef = TypedDict(
    "AccountAttributeListTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List["AttributeValueTargetTypeDef"]],
    },
)

AccountWithRestoreAccessTypeDef = TypedDict(
    "AccountWithRestoreAccessTypeDef",
    {
        "AccountId": NotRequired[str],
        "AccountAlias": NotRequired[str],
    },
)

AquaConfigurationTypeDef = TypedDict(
    "AquaConfigurationTypeDef",
    {
        "AquaStatus": NotRequired[AquaStatusType],
        "AquaConfigurationStatus": NotRequired[AquaConfigurationStatusType],
    },
)

AssociateDataShareConsumerMessageRequestTypeDef = TypedDict(
    "AssociateDataShareConsumerMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "AssociateEntireAccount": NotRequired[bool],
        "ConsumerArn": NotRequired[str],
        "ConsumerRegion": NotRequired[str],
    },
)

AttributeValueTargetTypeDef = TypedDict(
    "AttributeValueTargetTypeDef",
    {
        "AttributeValue": NotRequired[str],
    },
)

AuthenticationProfileTypeDef = TypedDict(
    "AuthenticationProfileTypeDef",
    {
        "AuthenticationProfileName": NotRequired[str],
        "AuthenticationProfileContent": NotRequired[str],
    },
)

AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "CIDRIP": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)

AuthorizeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeDataShareMessageRequestTypeDef = TypedDict(
    "AuthorizeDataShareMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "ConsumerIdentifier": str,
    },
)

AuthorizeEndpointAccessMessageRequestTypeDef = TypedDict(
    "AuthorizeEndpointAccessMessageRequestTypeDef",
    {
        "Account": str,
        "ClusterIdentifier": NotRequired[str],
        "VpcIds": NotRequired[Sequence[str]],
    },
)

AuthorizeSnapshotAccessMessageRequestTypeDef = TypedDict(
    "AuthorizeSnapshotAccessMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "AccountWithRestoreAccess": str,
        "SnapshotClusterIdentifier": NotRequired[str],
    },
)

AuthorizeSnapshotAccessResultTypeDef = TypedDict(
    "AuthorizeSnapshotAccessResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
        "SupportedPlatforms": NotRequired[List["SupportedPlatformTypeDef"]],
    },
)

BatchDeleteClusterSnapshotsRequestRequestTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsRequestRequestTypeDef",
    {
        "Identifiers": Sequence["DeleteClusterSnapshotMessageTypeDef"],
    },
)

BatchDeleteClusterSnapshotsResultTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsResultTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchModifyClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "BatchModifyClusterSnapshotsMessageRequestTypeDef",
    {
        "SnapshotIdentifierList": Sequence[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "Force": NotRequired[bool],
    },
)

BatchModifyClusterSnapshotsOutputMessageTypeDef = TypedDict(
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelResizeMessageRequestTypeDef = TypedDict(
    "CancelResizeMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ClusterAssociatedToScheduleTypeDef = TypedDict(
    "ClusterAssociatedToScheduleTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "ScheduleAssociationState": NotRequired[ScheduleStateType],
    },
)

ClusterCredentialsTypeDef = TypedDict(
    "ClusterCredentialsTypeDef",
    {
        "DbUser": str,
        "DbPassword": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterDbRevisionTypeDef = TypedDict(
    "ClusterDbRevisionTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "CurrentDatabaseRevision": NotRequired[str],
        "DatabaseRevisionReleaseDate": NotRequired[datetime],
        "RevisionTargets": NotRequired[List["RevisionTargetTypeDef"]],
    },
)

ClusterDbRevisionsMessageTypeDef = TypedDict(
    "ClusterDbRevisionsMessageTypeDef",
    {
        "Marker": str,
        "ClusterDbRevisions": List["ClusterDbRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterIamRoleTypeDef = TypedDict(
    "ClusterIamRoleTypeDef",
    {
        "IamRoleArn": NotRequired[str],
        "ApplyStatus": NotRequired[str],
    },
)

ClusterNodeTypeDef = TypedDict(
    "ClusterNodeTypeDef",
    {
        "NodeRole": NotRequired[str],
        "PrivateIPAddress": NotRequired[str],
        "PublicIPAddress": NotRequired[str],
    },
)

ClusterParameterGroupDetailsTypeDef = TypedDict(
    "ClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterGroupNameMessageTypeDef = TypedDict(
    "ClusterParameterGroupNameMessageTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterGroupStatusTypeDef = TypedDict(
    "ClusterParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "ClusterParameterStatusList": NotRequired[List["ClusterParameterStatusTypeDef"]],
    },
)

ClusterParameterGroupTypeDef = TypedDict(
    "ClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "ParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ClusterParameterGroupsMessageTypeDef = TypedDict(
    "ClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "ParameterGroups": List["ClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterStatusTypeDef = TypedDict(
    "ClusterParameterStatusTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "ParameterApplyErrorDescription": NotRequired[str],
    },
)

ClusterSecurityGroupMembershipTypeDef = TypedDict(
    "ClusterSecurityGroupMembershipTypeDef",
    {
        "ClusterSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

ClusterSecurityGroupMessageTypeDef = TypedDict(
    "ClusterSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "ClusterSecurityGroups": List["ClusterSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterSecurityGroupTypeDef = TypedDict(
    "ClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "EC2SecurityGroups": NotRequired[List["EC2SecurityGroupTypeDef"]],
        "IPRanges": NotRequired[List["IPRangeTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": NotRequired[str],
        "RetentionPeriod": NotRequired[int],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "SnapshotCopyGrantName": NotRequired[str],
    },
)

ClusterSubnetGroupMessageTypeDef = TypedDict(
    "ClusterSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "ClusterSubnetGroups": List["ClusterSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterSubnetGroupTypeDef = TypedDict(
    "ClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List["SubnetTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "NodeType": NotRequired[str],
        "ClusterStatus": NotRequired[str],
        "ClusterAvailabilityStatus": NotRequired[str],
        "ModifyStatus": NotRequired[str],
        "MasterUsername": NotRequired[str],
        "DBName": NotRequired[str],
        "Endpoint": NotRequired["EndpointTypeDef"],
        "ClusterCreateTime": NotRequired[datetime],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "ClusterSecurityGroups": NotRequired[List["ClusterSecurityGroupMembershipTypeDef"]],
        "VpcSecurityGroups": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
        "ClusterParameterGroups": NotRequired[List["ClusterParameterGroupStatusTypeDef"]],
        "ClusterSubnetGroupName": NotRequired[str],
        "VpcId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired["PendingModifiedValuesTypeDef"],
        "ClusterVersion": NotRequired[str],
        "AllowVersionUpgrade": NotRequired[bool],
        "NumberOfNodes": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "RestoreStatus": NotRequired["RestoreStatusTypeDef"],
        "DataTransferProgress": NotRequired["DataTransferProgressTypeDef"],
        "HsmStatus": NotRequired["HsmStatusTypeDef"],
        "ClusterSnapshotCopyStatus": NotRequired["ClusterSnapshotCopyStatusTypeDef"],
        "ClusterPublicKey": NotRequired[str],
        "ClusterNodes": NotRequired[List["ClusterNodeTypeDef"]],
        "ElasticIpStatus": NotRequired["ElasticIpStatusTypeDef"],
        "ClusterRevisionNumber": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "IamRoles": NotRequired[List["ClusterIamRoleTypeDef"]],
        "PendingActions": NotRequired[List[str]],
        "MaintenanceTrackName": NotRequired[str],
        "ElasticResizeNumberOfNodeOptions": NotRequired[str],
        "DeferredMaintenanceWindows": NotRequired[List["DeferredMaintenanceWindowTypeDef"]],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "SnapshotScheduleState": NotRequired[ScheduleStateType],
        "ExpectedNextSnapshotScheduleTime": NotRequired[datetime],
        "ExpectedNextSnapshotScheduleTimeStatus": NotRequired[str],
        "NextMaintenanceWindowStartTime": NotRequired[datetime],
        "ResizeInfo": NotRequired["ResizeInfoTypeDef"],
        "AvailabilityZoneRelocationStatus": NotRequired[str],
        "ClusterNamespaceArn": NotRequired[str],
        "TotalStorageCapacityInMegaBytes": NotRequired[int],
        "AquaConfiguration": NotRequired["AquaConfigurationTypeDef"],
        "DefaultIamRoleArn": NotRequired[str],
        "ReservedNodeExchangeStatus": NotRequired["ReservedNodeExchangeStatusTypeDef"],
    },
)

ClusterVersionTypeDef = TypedDict(
    "ClusterVersionTypeDef",
    {
        "ClusterVersion": NotRequired[str],
        "ClusterParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ClusterVersionsMessageTypeDef = TypedDict(
    "ClusterVersionsMessageTypeDef",
    {
        "Marker": str,
        "ClusterVersions": List["ClusterVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClustersMessageTypeDef = TypedDict(
    "ClustersMessageTypeDef",
    {
        "Marker": str,
        "Clusters": List["ClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CopyClusterSnapshotMessageRequestTypeDef",
    {
        "SourceSnapshotIdentifier": str,
        "TargetSnapshotIdentifier": str,
        "SourceSnapshotClusterIdentifier": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
    },
)

CopyClusterSnapshotResultTypeDef = TypedDict(
    "CopyClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAuthenticationProfileMessageRequestTypeDef = TypedDict(
    "CreateAuthenticationProfileMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
    },
)

CreateAuthenticationProfileResultTypeDef = TypedDict(
    "CreateAuthenticationProfileResultTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterMessageRequestTypeDef = TypedDict(
    "CreateClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "DBName": NotRequired[str],
        "ClusterType": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "ClusterSubnetGroupName": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ClusterParameterGroupName": NotRequired[str],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "Port": NotRequired[int],
        "ClusterVersion": NotRequired[str],
        "AllowVersionUpgrade": NotRequired[bool],
        "NumberOfNodes": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "Encrypted": NotRequired[bool],
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "ElasticIp": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "AdditionalInfo": NotRequired[str],
        "IamRoles": NotRequired[Sequence[str]],
        "MaintenanceTrackName": NotRequired[str],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "AvailabilityZoneRelocation": NotRequired[bool],
        "AquaConfigurationStatus": NotRequired[AquaConfigurationStatusType],
        "DefaultIamRoleArn": NotRequired[str],
    },
)

CreateClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateClusterParameterGroupResultTypeDef = TypedDict(
    "CreateClusterParameterGroupResultTypeDef",
    {
        "ClusterParameterGroup": "ClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterSecurityGroupMessageRequestTypeDef = TypedDict(
    "CreateClusterSecurityGroupMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateClusterSecurityGroupResultTypeDef = TypedDict(
    "CreateClusterSecurityGroupResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CreateClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateClusterSnapshotResultTypeDef = TypedDict(
    "CreateClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateClusterSubnetGroupMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateClusterSubnetGroupResultTypeDef = TypedDict(
    "CreateClusterSubnetGroupResultTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointAccessMessageRequestTypeDef = TypedDict(
    "CreateEndpointAccessMessageRequestTypeDef",
    {
        "EndpointName": str,
        "SubnetGroupName": str,
        "ClusterIdentifier": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)

CreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "CreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
        "SourceType": NotRequired[str],
        "SourceIds": NotRequired[Sequence[str]],
        "EventCategories": NotRequired[Sequence[str]],
        "Severity": NotRequired[str],
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

CreateHsmClientCertificateMessageRequestTypeDef = TypedDict(
    "CreateHsmClientCertificateMessageRequestTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateHsmClientCertificateResultTypeDef = TypedDict(
    "CreateHsmClientCertificateResultTypeDef",
    {
        "HsmClientCertificate": "HsmClientCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHsmConfigurationMessageRequestTypeDef = TypedDict(
    "CreateHsmConfigurationMessageRequestTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "HsmPartitionPassword": str,
        "HsmServerPublicCertificate": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateHsmConfigurationResultTypeDef = TypedDict(
    "CreateHsmConfigurationResultTypeDef",
    {
        "HsmConfiguration": "HsmConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScheduledActionMessageRequestTypeDef = TypedDict(
    "CreateScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Enable": NotRequired[bool],
    },
)

CreateSnapshotCopyGrantMessageRequestTypeDef = TypedDict(
    "CreateSnapshotCopyGrantMessageRequestTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSnapshotCopyGrantResultTypeDef = TypedDict(
    "CreateSnapshotCopyGrantResultTypeDef",
    {
        "SnapshotCopyGrant": "SnapshotCopyGrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "CreateSnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleDefinitions": NotRequired[Sequence[str]],
        "ScheduleIdentifier": NotRequired[str],
        "ScheduleDescription": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DryRun": NotRequired[bool],
        "NextInvocations": NotRequired[int],
    },
)

CreateTagsMessageRequestTypeDef = TypedDict(
    "CreateTagsMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

CreateUsageLimitMessageRequestTypeDef = TypedDict(
    "CreateUsageLimitMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
        "Period": NotRequired[UsageLimitPeriodType],
        "BreachAction": NotRequired[UsageLimitBreachActionType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CustomerStorageMessageTypeDef = TypedDict(
    "CustomerStorageMessageTypeDef",
    {
        "TotalBackupSizeInMegaBytes": float,
        "TotalProvisionedStorageInMegaBytes": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataShareAssociationTypeDef = TypedDict(
    "DataShareAssociationTypeDef",
    {
        "ConsumerIdentifier": NotRequired[str],
        "Status": NotRequired[DataShareStatusType],
        "ConsumerRegion": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "StatusChangeDate": NotRequired[datetime],
    },
)

DataShareResponseMetadataTypeDef = TypedDict(
    "DataShareResponseMetadataTypeDef",
    {
        "DataShareArn": str,
        "ProducerArn": str,
        "AllowPubliclyAccessibleConsumers": bool,
        "DataShareAssociations": List["DataShareAssociationTypeDef"],
        "ManagedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataShareTypeDef = TypedDict(
    "DataShareTypeDef",
    {
        "DataShareArn": NotRequired[str],
        "ProducerArn": NotRequired[str],
        "AllowPubliclyAccessibleConsumers": NotRequired[bool],
        "DataShareAssociations": NotRequired[List["DataShareAssociationTypeDef"]],
        "ManagedBy": NotRequired[str],
    },
)

DataTransferProgressTypeDef = TypedDict(
    "DataTransferProgressTypeDef",
    {
        "Status": NotRequired[str],
        "CurrentRateInMegaBytesPerSecond": NotRequired[float],
        "TotalDataInMegaBytes": NotRequired[int],
        "DataTransferredInMegaBytes": NotRequired[int],
        "EstimatedTimeToCompletionInSeconds": NotRequired[int],
        "ElapsedTimeInSeconds": NotRequired[int],
    },
)

DeauthorizeDataShareMessageRequestTypeDef = TypedDict(
    "DeauthorizeDataShareMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "ConsumerIdentifier": str,
    },
)

DefaultClusterParametersTypeDef = TypedDict(
    "DefaultClusterParametersTypeDef",
    {
        "ParameterGroupFamily": NotRequired[str],
        "Marker": NotRequired[str],
        "Parameters": NotRequired[List["ParameterTypeDef"]],
    },
)

DeferredMaintenanceWindowTypeDef = TypedDict(
    "DeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceIdentifier": NotRequired[str],
        "DeferMaintenanceStartTime": NotRequired[datetime],
        "DeferMaintenanceEndTime": NotRequired[datetime],
    },
)

DeleteAuthenticationProfileMessageRequestTypeDef = TypedDict(
    "DeleteAuthenticationProfileMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
    },
)

DeleteAuthenticationProfileResultTypeDef = TypedDict(
    "DeleteAuthenticationProfileResultTypeDef",
    {
        "AuthenticationProfileName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterMessageRequestTypeDef = TypedDict(
    "DeleteClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SkipFinalClusterSnapshot": NotRequired[bool],
        "FinalClusterSnapshotIdentifier": NotRequired[str],
        "FinalClusterSnapshotRetentionPeriod": NotRequired[int],
    },
)

DeleteClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)

DeleteClusterResultTypeDef = TypedDict(
    "DeleteClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteClusterSecurityGroupMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
)

DeleteClusterSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": NotRequired[str],
    },
)

DeleteClusterSnapshotMessageTypeDef = TypedDict(
    "DeleteClusterSnapshotMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": NotRequired[str],
    },
)

DeleteClusterSnapshotResultTypeDef = TypedDict(
    "DeleteClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteClusterSubnetGroupMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
    },
)

DeleteEndpointAccessMessageRequestTypeDef = TypedDict(
    "DeleteEndpointAccessMessageRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteHsmClientCertificateMessageRequestTypeDef = TypedDict(
    "DeleteHsmClientCertificateMessageRequestTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
    },
)

DeleteHsmConfigurationMessageRequestTypeDef = TypedDict(
    "DeleteHsmConfigurationMessageRequestTypeDef",
    {
        "HsmConfigurationIdentifier": str,
    },
)

DeleteScheduledActionMessageRequestTypeDef = TypedDict(
    "DeleteScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
    },
)

DeleteSnapshotCopyGrantMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotCopyGrantMessageRequestTypeDef",
    {
        "SnapshotCopyGrantName": str,
    },
)

DeleteSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleIdentifier": str,
    },
)

DeleteTagsMessageRequestTypeDef = TypedDict(
    "DeleteTagsMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)

DeleteUsageLimitMessageRequestTypeDef = TypedDict(
    "DeleteUsageLimitMessageRequestTypeDef",
    {
        "UsageLimitId": str,
    },
)

DescribeAccountAttributesMessageRequestTypeDef = TypedDict(
    "DescribeAccountAttributesMessageRequestTypeDef",
    {
        "AttributeNames": NotRequired[Sequence[str]],
    },
)

DescribeAuthenticationProfilesMessageRequestTypeDef = TypedDict(
    "DescribeAuthenticationProfilesMessageRequestTypeDef",
    {
        "AuthenticationProfileName": NotRequired[str],
    },
)

DescribeAuthenticationProfilesResultTypeDef = TypedDict(
    "DescribeAuthenticationProfilesResultTypeDef",
    {
        "AuthenticationProfiles": List["AuthenticationProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterDbRevisionsMessageRequestTypeDef = TypedDict(
    "DescribeClusterDbRevisionsMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeClusterParameterGroupsMessageRequestTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeClusterParametersMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Source": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeClusterSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeClusterSecurityGroupsMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeClusterSnapshotsMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "SnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
        "ClusterExists": NotRequired[bool],
        "SortingEntities": NotRequired[Sequence["SnapshotSortingEntityTypeDef"]],
    },
)

DescribeClusterSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeClusterSubnetGroupsMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeClusterTracksMessageRequestTypeDef = TypedDict(
    "DescribeClusterTracksMessageRequestTypeDef",
    {
        "MaintenanceTrackName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeClusterVersionsMessageRequestTypeDef = TypedDict(
    "DescribeClusterVersionsMessageRequestTypeDef",
    {
        "ClusterVersion": NotRequired[str],
        "ClusterParameterGroupFamily": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeClustersMessageRequestTypeDef = TypedDict(
    "DescribeClustersMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeDataSharesForConsumerMessageRequestTypeDef = TypedDict(
    "DescribeDataSharesForConsumerMessageRequestTypeDef",
    {
        "ConsumerArn": NotRequired[str],
        "Status": NotRequired[DataShareStatusForConsumerType],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDataSharesForConsumerResultTypeDef = TypedDict(
    "DescribeDataSharesForConsumerResultTypeDef",
    {
        "DataShares": List["DataShareTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSharesForProducerMessageRequestTypeDef = TypedDict(
    "DescribeDataSharesForProducerMessageRequestTypeDef",
    {
        "ProducerArn": NotRequired[str],
        "Status": NotRequired[DataShareStatusForProducerType],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDataSharesForProducerResultTypeDef = TypedDict(
    "DescribeDataSharesForProducerResultTypeDef",
    {
        "DataShares": List["DataShareTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSharesMessageRequestTypeDef = TypedDict(
    "DescribeDataSharesMessageRequestTypeDef",
    {
        "DataShareArn": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDataSharesResultTypeDef = TypedDict(
    "DescribeDataSharesResultTypeDef",
    {
        "DataShares": List["DataShareTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeDefaultClusterParametersMessageRequestTypeDef",
    {
        "ParameterGroupFamily": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeDefaultClusterParametersResultTypeDef",
    {
        "DefaultClusterParameters": "DefaultClusterParametersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointAccessMessageRequestTypeDef = TypedDict(
    "DescribeEndpointAccessMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "EndpointName": NotRequired[str],
        "VpcId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEndpointAuthorizationMessageRequestTypeDef = TypedDict(
    "DescribeEndpointAuthorizationMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "Account": NotRequired[str],
        "Grantee": NotRequired[bool],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": NotRequired[str],
    },
)

DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
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

DescribeHsmClientCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeHsmClientCertificatesMessageRequestTypeDef",
    {
        "HsmClientCertificateIdentifier": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeHsmConfigurationsMessageRequestTypeDef = TypedDict(
    "DescribeHsmConfigurationsMessageRequestTypeDef",
    {
        "HsmConfigurationIdentifier": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeLoggingStatusMessageRequestTypeDef = TypedDict(
    "DescribeLoggingStatusMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DescribeNodeConfigurationOptionsMessageRequestTypeDef = TypedDict(
    "DescribeNodeConfigurationOptionsMessageRequestTypeDef",
    {
        "ActionType": ActionTypeType,
        "ClusterIdentifier": NotRequired[str],
        "SnapshotIdentifier": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "Filters": NotRequired[Sequence["NodeConfigurationOptionsFilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeOrderableClusterOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOrderableClusterOptionsMessageRequestTypeDef",
    {
        "ClusterVersion": NotRequired[str],
        "NodeType": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribePartnersInputMessageRequestTypeDef = TypedDict(
    "DescribePartnersInputMessageRequestTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": NotRequired[str],
        "PartnerName": NotRequired[str],
    },
)

DescribePartnersOutputMessageTypeDef = TypedDict(
    "DescribePartnersOutputMessageTypeDef",
    {
        "PartnerIntegrationInfoList": List["PartnerIntegrationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedNodeExchangeStatusInputMessageRequestTypeDef = TypedDict(
    "DescribeReservedNodeExchangeStatusInputMessageRequestTypeDef",
    {
        "ReservedNodeId": NotRequired[str],
        "ReservedNodeExchangeRequestId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReservedNodeExchangeStatusOutputMessageTypeDef = TypedDict(
    "DescribeReservedNodeExchangeStatusOutputMessageTypeDef",
    {
        "ReservedNodeExchangeStatusDetails": List["ReservedNodeExchangeStatusTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedNodeOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedNodeOfferingsMessageRequestTypeDef",
    {
        "ReservedNodeOfferingId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReservedNodesMessageRequestTypeDef = TypedDict(
    "DescribeReservedNodesMessageRequestTypeDef",
    {
        "ReservedNodeId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeResizeMessageRequestTypeDef = TypedDict(
    "DescribeResizeMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DescribeScheduledActionsMessageRequestTypeDef = TypedDict(
    "DescribeScheduledActionsMessageRequestTypeDef",
    {
        "ScheduledActionName": NotRequired[str],
        "TargetActionType": NotRequired[ScheduledActionTypeValuesType],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Active": NotRequired[bool],
        "Filters": NotRequired[Sequence["ScheduledActionFilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeSnapshotCopyGrantsMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotCopyGrantsMessageRequestTypeDef",
    {
        "SnapshotCopyGrantName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeSnapshotSchedulesMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotSchedulesMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "ScheduleIdentifier": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeSnapshotSchedulesOutputMessageTypeDef = TypedDict(
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    {
        "SnapshotSchedules": List["SnapshotScheduleTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableRestoreStatusMessageRequestTypeDef = TypedDict(
    "DescribeTableRestoreStatusMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "TableRestoreRequestId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeTagsMessageRequestTypeDef = TypedDict(
    "DescribeTagsMessageRequestTypeDef",
    {
        "ResourceName": NotRequired[str],
        "ResourceType": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DescribeUsageLimitsMessageRequestTypeDef = TypedDict(
    "DescribeUsageLimitsMessageRequestTypeDef",
    {
        "UsageLimitId": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "FeatureType": NotRequired[UsageLimitFeatureTypeType],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
        "TagValues": NotRequired[Sequence[str]],
    },
)

DisableLoggingMessageRequestTypeDef = TypedDict(
    "DisableLoggingMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DisableSnapshotCopyMessageRequestTypeDef = TypedDict(
    "DisableSnapshotCopyMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DisableSnapshotCopyResultTypeDef = TypedDict(
    "DisableSnapshotCopyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateDataShareConsumerMessageRequestTypeDef = TypedDict(
    "DisassociateDataShareConsumerMessageRequestTypeDef",
    {
        "DataShareArn": str,
        "DisassociateEntireAccount": NotRequired[bool],
        "ConsumerArn": NotRequired[str],
        "ConsumerRegion": NotRequired[str],
    },
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ElasticIpStatusTypeDef = TypedDict(
    "ElasticIpStatusTypeDef",
    {
        "ElasticIp": NotRequired[str],
        "Status": NotRequired[str],
    },
)

EnableLoggingMessageRequestTypeDef = TypedDict(
    "EnableLoggingMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "BucketName": str,
        "S3KeyPrefix": NotRequired[str],
    },
)

EnableSnapshotCopyMessageRequestTypeDef = TypedDict(
    "EnableSnapshotCopyMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "DestinationRegion": str,
        "RetentionPeriod": NotRequired[int],
        "SnapshotCopyGrantName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
    },
)

EnableSnapshotCopyResultTypeDef = TypedDict(
    "EnableSnapshotCopyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessListTypeDef = TypedDict(
    "EndpointAccessListTypeDef",
    {
        "EndpointAccessList": List["EndpointAccessTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessResponseMetadataTypeDef = TypedDict(
    "EndpointAccessResponseMetadataTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "SubnetGroupName": str,
        "EndpointStatus": str,
        "EndpointName": str,
        "EndpointCreateTime": datetime,
        "Port": int,
        "Address": str,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessTypeDef = TypedDict(
    "EndpointAccessTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "SubnetGroupName": NotRequired[str],
        "EndpointStatus": NotRequired[str],
        "EndpointName": NotRequired[str],
        "EndpointCreateTime": NotRequired[datetime],
        "Port": NotRequired[int],
        "Address": NotRequired[str],
        "VpcSecurityGroups": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
        "VpcEndpoint": NotRequired["VpcEndpointTypeDef"],
    },
)

EndpointAuthorizationListTypeDef = TypedDict(
    "EndpointAuthorizationListTypeDef",
    {
        "EndpointAuthorizationList": List["EndpointAuthorizationTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAuthorizationResponseMetadataTypeDef = TypedDict(
    "EndpointAuthorizationResponseMetadataTypeDef",
    {
        "Grantor": str,
        "Grantee": str,
        "ClusterIdentifier": str,
        "AuthorizeTime": datetime,
        "ClusterStatus": str,
        "Status": AuthorizationStatusType,
        "AllowedAllVPCs": bool,
        "AllowedVPCs": List[str],
        "EndpointCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAuthorizationTypeDef = TypedDict(
    "EndpointAuthorizationTypeDef",
    {
        "Grantor": NotRequired[str],
        "Grantee": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "AuthorizeTime": NotRequired[datetime],
        "ClusterStatus": NotRequired[str],
        "Status": NotRequired[AuthorizationStatusType],
        "AllowedAllVPCs": NotRequired[bool],
        "AllowedVPCs": NotRequired[List[str]],
        "EndpointCount": NotRequired[int],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "VpcEndpoints": NotRequired[List["VpcEndpointTypeDef"]],
    },
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": NotRequired[str],
        "Events": NotRequired[List["EventInfoMapTypeDef"]],
    },
)

EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventInfoMapTypeDef = TypedDict(
    "EventInfoMapTypeDef",
    {
        "EventId": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
        "EventDescription": NotRequired[str],
        "Severity": NotRequired[str],
    },
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": NotRequired[str],
        "CustSubscriptionId": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[datetime],
        "SourceType": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "EventCategoriesList": NotRequired[List[str]],
        "Severity": NotRequired[str],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[List["TagTypeDef"]],
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
        "Severity": NotRequired[str],
        "Date": NotRequired[datetime],
        "EventId": NotRequired[str],
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

GetClusterCredentialsMessageRequestTypeDef = TypedDict(
    "GetClusterCredentialsMessageRequestTypeDef",
    {
        "DbUser": str,
        "ClusterIdentifier": str,
        "DbName": NotRequired[str],
        "DurationSeconds": NotRequired[int],
        "AutoCreate": NotRequired[bool],
        "DbGroups": NotRequired[Sequence[str]],
    },
)

GetReservedNodeExchangeConfigurationOptionsInputMessageRequestTypeDef = TypedDict(
    "GetReservedNodeExchangeConfigurationOptionsInputMessageRequestTypeDef",
    {
        "ActionType": ReservedNodeExchangeActionTypeType,
        "ClusterIdentifier": NotRequired[str],
        "SnapshotIdentifier": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef = TypedDict(
    "GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeConfigurationOptionList": List["ReservedNodeConfigurationOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef",
    {
        "ReservedNodeId": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

GetReservedNodeExchangeOfferingsOutputMessageTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmClientCertificateMessageTypeDef = TypedDict(
    "HsmClientCertificateMessageTypeDef",
    {
        "Marker": str,
        "HsmClientCertificates": List["HsmClientCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmClientCertificateTypeDef = TypedDict(
    "HsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmClientCertificatePublicKey": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

HsmConfigurationMessageTypeDef = TypedDict(
    "HsmConfigurationMessageTypeDef",
    {
        "Marker": str,
        "HsmConfigurations": List["HsmConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmConfigurationTypeDef = TypedDict(
    "HsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": NotRequired[str],
        "Description": NotRequired[str],
        "HsmIpAddress": NotRequired[str],
        "HsmPartitionName": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

HsmStatusTypeDef = TypedDict(
    "HsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "Status": NotRequired[str],
    },
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": NotRequired[str],
        "CIDRIP": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LoggingStatusTypeDef = TypedDict(
    "LoggingStatusTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MaintenanceTrackTypeDef = TypedDict(
    "MaintenanceTrackTypeDef",
    {
        "MaintenanceTrackName": NotRequired[str],
        "DatabaseVersion": NotRequired[str],
        "UpdateTargets": NotRequired[List["UpdateTargetTypeDef"]],
    },
)

ModifyAquaInputMessageRequestTypeDef = TypedDict(
    "ModifyAquaInputMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "AquaConfigurationStatus": NotRequired[AquaConfigurationStatusType],
    },
)

ModifyAquaOutputMessageTypeDef = TypedDict(
    "ModifyAquaOutputMessageTypeDef",
    {
        "AquaConfiguration": "AquaConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyAuthenticationProfileMessageRequestTypeDef = TypedDict(
    "ModifyAuthenticationProfileMessageRequestTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
    },
)

ModifyAuthenticationProfileResultTypeDef = TypedDict(
    "ModifyAuthenticationProfileResultTypeDef",
    {
        "AuthenticationProfileName": str,
        "AuthenticationProfileContent": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterDbRevisionMessageRequestTypeDef = TypedDict(
    "ModifyClusterDbRevisionMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "RevisionTarget": str,
    },
)

ModifyClusterDbRevisionResultTypeDef = TypedDict(
    "ModifyClusterDbRevisionResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterIamRolesMessageRequestTypeDef = TypedDict(
    "ModifyClusterIamRolesMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "AddIamRoles": NotRequired[Sequence[str]],
        "RemoveIamRoles": NotRequired[Sequence[str]],
        "DefaultIamRoleArn": NotRequired[str],
    },
)

ModifyClusterIamRolesResultTypeDef = TypedDict(
    "ModifyClusterIamRolesResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterMaintenanceMessageRequestTypeDef = TypedDict(
    "ModifyClusterMaintenanceMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "DeferMaintenance": NotRequired[bool],
        "DeferMaintenanceIdentifier": NotRequired[str],
        "DeferMaintenanceStartTime": NotRequired[Union[datetime, str]],
        "DeferMaintenanceEndTime": NotRequired[Union[datetime, str]],
        "DeferMaintenanceDuration": NotRequired[int],
    },
)

ModifyClusterMaintenanceResultTypeDef = TypedDict(
    "ModifyClusterMaintenanceResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterMessageRequestTypeDef = TypedDict(
    "ModifyClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "ClusterSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "MasterUserPassword": NotRequired[str],
        "ClusterParameterGroupName": NotRequired[str],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "AllowVersionUpgrade": NotRequired[bool],
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "NewClusterIdentifier": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "ElasticIp": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "MaintenanceTrackName": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "AvailabilityZoneRelocation": NotRequired[bool],
        "AvailabilityZone": NotRequired[str],
        "Port": NotRequired[int],
    },
)

ModifyClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Parameters": Sequence["ParameterTypeDef"],
    },
)

ModifyClusterResultTypeDef = TypedDict(
    "ModifyClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterSnapshotMessageRequestTypeDef = TypedDict(
    "ModifyClusterSnapshotMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "Force": NotRequired[bool],
    },
)

ModifyClusterSnapshotResultTypeDef = TypedDict(
    "ModifyClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterSnapshotScheduleMessageRequestTypeDef = TypedDict(
    "ModifyClusterSnapshotScheduleMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleIdentifier": NotRequired[str],
        "DisassociateSchedule": NotRequired[bool],
    },
)

ModifyClusterSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyClusterSubnetGroupMessageRequestTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "Description": NotRequired[str],
    },
)

ModifyClusterSubnetGroupResultTypeDef = TypedDict(
    "ModifyClusterSubnetGroupResultTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyEndpointAccessMessageRequestTypeDef = TypedDict(
    "ModifyEndpointAccessMessageRequestTypeDef",
    {
        "EndpointName": str,
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)

ModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "ModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "SourceIds": NotRequired[Sequence[str]],
        "EventCategories": NotRequired[Sequence[str]],
        "Severity": NotRequired[str],
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

ModifyScheduledActionMessageRequestTypeDef = TypedDict(
    "ModifyScheduledActionMessageRequestTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": NotRequired["ScheduledActionTypeTypeDef"],
        "Schedule": NotRequired[str],
        "IamRole": NotRequired[str],
        "ScheduledActionDescription": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Enable": NotRequired[bool],
    },
)

ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef = TypedDict(
    "ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "RetentionPeriod": int,
        "Manual": NotRequired[bool],
    },
)

ModifySnapshotCopyRetentionPeriodResultTypeDef = TypedDict(
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySnapshotScheduleMessageRequestTypeDef = TypedDict(
    "ModifySnapshotScheduleMessageRequestTypeDef",
    {
        "ScheduleIdentifier": str,
        "ScheduleDefinitions": Sequence[str],
    },
)

ModifyUsageLimitMessageRequestTypeDef = TypedDict(
    "ModifyUsageLimitMessageRequestTypeDef",
    {
        "UsageLimitId": str,
        "Amount": NotRequired[int],
        "BreachAction": NotRequired[UsageLimitBreachActionType],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "NetworkInterfaceId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
    },
)

NodeConfigurationOptionTypeDef = TypedDict(
    "NodeConfigurationOptionTypeDef",
    {
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "EstimatedDiskUtilizationPercent": NotRequired[float],
        "Mode": NotRequired[ModeType],
    },
)

NodeConfigurationOptionsFilterTypeDef = TypedDict(
    "NodeConfigurationOptionsFilterTypeDef",
    {
        "Name": NotRequired[NodeConfigurationOptionsFilterNameType],
        "Operator": NotRequired[OperatorTypeType],
        "Values": NotRequired[Sequence[str]],
    },
)

NodeConfigurationOptionsMessageTypeDef = TypedDict(
    "NodeConfigurationOptionsMessageTypeDef",
    {
        "NodeConfigurationOptionList": List["NodeConfigurationOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderableClusterOptionTypeDef = TypedDict(
    "OrderableClusterOptionTypeDef",
    {
        "ClusterVersion": NotRequired[str],
        "ClusterType": NotRequired[str],
        "NodeType": NotRequired[str],
        "AvailabilityZones": NotRequired[List["AvailabilityZoneTypeDef"]],
    },
)

OrderableClusterOptionsMessageTypeDef = TypedDict(
    "OrderableClusterOptionsMessageTypeDef",
    {
        "OrderableClusterOptions": List["OrderableClusterOptionTypeDef"],
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
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "ApplyType": NotRequired[ParameterApplyTypeType],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
    },
)

PartnerIntegrationInfoTypeDef = TypedDict(
    "PartnerIntegrationInfoTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "PartnerName": NotRequired[str],
        "Status": NotRequired[PartnerIntegrationStatusType],
        "StatusMessage": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

PartnerIntegrationInputMessageRequestTypeDef = TypedDict(
    "PartnerIntegrationInputMessageRequestTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": str,
        "PartnerName": str,
    },
)

PartnerIntegrationOutputMessageTypeDef = TypedDict(
    "PartnerIntegrationOutputMessageTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PauseClusterMessageRequestTypeDef = TypedDict(
    "PauseClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

PauseClusterMessageTypeDef = TypedDict(
    "PauseClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

PauseClusterResultTypeDef = TypedDict(
    "PauseClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "ClusterType": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ClusterIdentifier": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "EnhancedVpcRouting": NotRequired[bool],
        "MaintenanceTrackName": NotRequired[str],
        "EncryptionType": NotRequired[str],
    },
)

PurchaseReservedNodeOfferingMessageRequestTypeDef = TypedDict(
    "PurchaseReservedNodeOfferingMessageRequestTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeCount": NotRequired[int],
    },
)

PurchaseReservedNodeOfferingResultTypeDef = TypedDict(
    "PurchaseReservedNodeOfferingResultTypeDef",
    {
        "ReservedNode": "ReservedNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootClusterMessageRequestTypeDef = TypedDict(
    "RebootClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

RebootClusterResultTypeDef = TypedDict(
    "RebootClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

RejectDataShareMessageRequestTypeDef = TypedDict(
    "RejectDataShareMessageRequestTypeDef",
    {
        "DataShareArn": str,
    },
)

ReservedNodeConfigurationOptionTypeDef = TypedDict(
    "ReservedNodeConfigurationOptionTypeDef",
    {
        "SourceReservedNode": NotRequired["ReservedNodeTypeDef"],
        "TargetReservedNodeCount": NotRequired[int],
        "TargetReservedNodeOffering": NotRequired["ReservedNodeOfferingTypeDef"],
    },
)

ReservedNodeExchangeStatusTypeDef = TypedDict(
    "ReservedNodeExchangeStatusTypeDef",
    {
        "ReservedNodeExchangeRequestId": NotRequired[str],
        "Status": NotRequired[ReservedNodeExchangeStatusTypeType],
        "RequestTime": NotRequired[datetime],
        "SourceReservedNodeId": NotRequired[str],
        "SourceReservedNodeType": NotRequired[str],
        "SourceReservedNodeCount": NotRequired[int],
        "TargetReservedNodeOfferingId": NotRequired[str],
        "TargetReservedNodeType": NotRequired[str],
        "TargetReservedNodeCount": NotRequired[int],
    },
)

ReservedNodeOfferingTypeDef = TypedDict(
    "ReservedNodeOfferingTypeDef",
    {
        "ReservedNodeOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "OfferingType": NotRequired[str],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
        "ReservedNodeOfferingType": NotRequired[ReservedNodeOfferingTypeType],
    },
)

ReservedNodeOfferingsMessageTypeDef = TypedDict(
    "ReservedNodeOfferingsMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedNodeTypeDef = TypedDict(
    "ReservedNodeTypeDef",
    {
        "ReservedNodeId": NotRequired[str],
        "ReservedNodeOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "NodeCount": NotRequired[int],
        "State": NotRequired[str],
        "OfferingType": NotRequired[str],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
        "ReservedNodeOfferingType": NotRequired[ReservedNodeOfferingTypeType],
    },
)

ReservedNodesMessageTypeDef = TypedDict(
    "ReservedNodesMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodes": List["ReservedNodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetClusterParameterGroupMessageRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "Parameters": NotRequired[Sequence["ParameterTypeDef"]],
    },
)

ResizeClusterMessageRequestTypeDef = TypedDict(
    "ResizeClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "Classic": NotRequired[bool],
        "ReservedNodeId": NotRequired[str],
        "TargetReservedNodeOfferingId": NotRequired[str],
    },
)

ResizeClusterMessageTypeDef = TypedDict(
    "ResizeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "ClusterType": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "Classic": NotRequired[bool],
        "ReservedNodeId": NotRequired[str],
        "TargetReservedNodeOfferingId": NotRequired[str],
    },
)

ResizeClusterResultTypeDef = TypedDict(
    "ResizeClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResizeInfoTypeDef = TypedDict(
    "ResizeInfoTypeDef",
    {
        "ResizeType": NotRequired[str],
        "AllowCancelResize": NotRequired[bool],
    },
)

ResizeProgressMessageTypeDef = TypedDict(
    "ResizeProgressMessageTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
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

RestoreFromClusterSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreFromClusterSnapshotMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "AllowVersionUpgrade": NotRequired[bool],
        "ClusterSubnetGroupName": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "OwnerAccount": NotRequired[str],
        "HsmClientCertificateIdentifier": NotRequired[str],
        "HsmConfigurationIdentifier": NotRequired[str],
        "ElasticIp": NotRequired[str],
        "ClusterParameterGroupName": NotRequired[str],
        "ClusterSecurityGroups": NotRequired[Sequence[str]],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "AutomatedSnapshotRetentionPeriod": NotRequired[int],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "NodeType": NotRequired[str],
        "EnhancedVpcRouting": NotRequired[bool],
        "AdditionalInfo": NotRequired[str],
        "IamRoles": NotRequired[Sequence[str]],
        "MaintenanceTrackName": NotRequired[str],
        "SnapshotScheduleIdentifier": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "AvailabilityZoneRelocation": NotRequired[bool],
        "AquaConfigurationStatus": NotRequired[AquaConfigurationStatusType],
        "DefaultIamRoleArn": NotRequired[str],
        "ReservedNodeId": NotRequired[str],
        "TargetReservedNodeOfferingId": NotRequired[str],
    },
)

RestoreFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreFromClusterSnapshotResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreStatusTypeDef = TypedDict(
    "RestoreStatusTypeDef",
    {
        "Status": NotRequired[str],
        "CurrentRestoreRateInMegaBytesPerSecond": NotRequired[float],
        "SnapshotSizeInMegaBytes": NotRequired[int],
        "ProgressInMegaBytes": NotRequired[int],
        "ElapsedTimeInSeconds": NotRequired[int],
        "EstimatedTimeToCompletionInSeconds": NotRequired[int],
    },
)

RestoreTableFromClusterSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreTableFromClusterSnapshotMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceTableName": str,
        "NewTableName": str,
        "SourceSchemaName": NotRequired[str],
        "TargetDatabaseName": NotRequired[str],
        "TargetSchemaName": NotRequired[str],
        "EnableCaseSensitiveIdentifier": NotRequired[bool],
    },
)

RestoreTableFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreTableFromClusterSnapshotResultTypeDef",
    {
        "TableRestoreStatus": "TableRestoreStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResumeClusterMessageRequestTypeDef = TypedDict(
    "ResumeClusterMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ResumeClusterMessageTypeDef = TypedDict(
    "ResumeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ResumeClusterResultTypeDef = TypedDict(
    "ResumeClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevisionTargetTypeDef = TypedDict(
    "RevisionTargetTypeDef",
    {
        "DatabaseRevision": NotRequired[str],
        "Description": NotRequired[str],
        "DatabaseRevisionReleaseDate": NotRequired[datetime],
    },
)

RevokeClusterSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "RevokeClusterSecurityGroupIngressMessageRequestTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "CIDRIP": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)

RevokeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeEndpointAccessMessageRequestTypeDef = TypedDict(
    "RevokeEndpointAccessMessageRequestTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "Account": NotRequired[str],
        "VpcIds": NotRequired[Sequence[str]],
        "Force": NotRequired[bool],
    },
)

RevokeSnapshotAccessMessageRequestTypeDef = TypedDict(
    "RevokeSnapshotAccessMessageRequestTypeDef",
    {
        "SnapshotIdentifier": str,
        "AccountWithRestoreAccess": str,
        "SnapshotClusterIdentifier": NotRequired[str],
    },
)

RevokeSnapshotAccessResultTypeDef = TypedDict(
    "RevokeSnapshotAccessResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotateEncryptionKeyMessageRequestTypeDef = TypedDict(
    "RotateEncryptionKeyMessageRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

RotateEncryptionKeyResultTypeDef = TypedDict(
    "RotateEncryptionKeyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduledActionFilterTypeDef = TypedDict(
    "ScheduledActionFilterTypeDef",
    {
        "Name": ScheduledActionFilterNameType,
        "Values": Sequence[str],
    },
)

ScheduledActionResponseMetadataTypeDef = TypedDict(
    "ScheduledActionResponseMetadataTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": ScheduledActionStateType,
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": NotRequired[str],
        "TargetAction": NotRequired["ScheduledActionTypeTypeDef"],
        "Schedule": NotRequired[str],
        "IamRole": NotRequired[str],
        "ScheduledActionDescription": NotRequired[str],
        "State": NotRequired[ScheduledActionStateType],
        "NextInvocations": NotRequired[List[datetime]],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

ScheduledActionTypeTypeDef = TypedDict(
    "ScheduledActionTypeTypeDef",
    {
        "ResizeCluster": NotRequired["ResizeClusterMessageTypeDef"],
        "PauseCluster": NotRequired["PauseClusterMessageTypeDef"],
        "ResumeCluster": NotRequired["ResumeClusterMessageTypeDef"],
    },
)

ScheduledActionsMessageTypeDef = TypedDict(
    "ScheduledActionsMessageTypeDef",
    {
        "Marker": str,
        "ScheduledActions": List["ScheduledActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotCopyGrantMessageTypeDef = TypedDict(
    "SnapshotCopyGrantMessageTypeDef",
    {
        "Marker": str,
        "SnapshotCopyGrants": List["SnapshotCopyGrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotCopyGrantTypeDef = TypedDict(
    "SnapshotCopyGrantTypeDef",
    {
        "SnapshotCopyGrantName": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

SnapshotErrorMessageTypeDef = TypedDict(
    "SnapshotErrorMessageTypeDef",
    {
        "SnapshotIdentifier": NotRequired[str],
        "SnapshotClusterIdentifier": NotRequired[str],
        "FailureCode": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)

SnapshotMessageTypeDef = TypedDict(
    "SnapshotMessageTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotScheduleResponseMetadataTypeDef = TypedDict(
    "SnapshotScheduleResponseMetadataTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List["ClusterAssociatedToScheduleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotScheduleTypeDef = TypedDict(
    "SnapshotScheduleTypeDef",
    {
        "ScheduleDefinitions": NotRequired[List[str]],
        "ScheduleIdentifier": NotRequired[str],
        "ScheduleDescription": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "NextInvocations": NotRequired[List[datetime]],
        "AssociatedClusterCount": NotRequired[int],
        "AssociatedClusters": NotRequired[List["ClusterAssociatedToScheduleTypeDef"]],
    },
)

SnapshotSortingEntityTypeDef = TypedDict(
    "SnapshotSortingEntityTypeDef",
    {
        "Attribute": SnapshotAttributeToSortByType,
        "SortOrder": NotRequired[SortByOrderType],
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotIdentifier": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[datetime],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "ClusterVersion": NotRequired[str],
        "EngineFullVersion": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "NodeType": NotRequired[str],
        "NumberOfNodes": NotRequired[int],
        "DBName": NotRequired[str],
        "VpcId": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "EncryptedWithHSM": NotRequired[bool],
        "AccountsWithRestoreAccess": NotRequired[List["AccountWithRestoreAccessTypeDef"]],
        "OwnerAccount": NotRequired[str],
        "TotalBackupSizeInMegaBytes": NotRequired[float],
        "ActualIncrementalBackupSizeInMegaBytes": NotRequired[float],
        "BackupProgressInMegaBytes": NotRequired[float],
        "CurrentBackupRateInMegaBytesPerSecond": NotRequired[float],
        "EstimatedSecondsToCompletion": NotRequired[int],
        "ElapsedTimeInSeconds": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "RestorableNodeTypes": NotRequired[List[str]],
        "EnhancedVpcRouting": NotRequired[bool],
        "MaintenanceTrackName": NotRequired[str],
        "ManualSnapshotRetentionPeriod": NotRequired[int],
        "ManualSnapshotRemainingDays": NotRequired[int],
        "SnapshotRetentionStartTime": NotRequired[datetime],
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

SupportedOperationTypeDef = TypedDict(
    "SupportedOperationTypeDef",
    {
        "OperationName": NotRequired[str],
    },
)

SupportedPlatformTypeDef = TypedDict(
    "SupportedPlatformTypeDef",
    {
        "Name": NotRequired[str],
    },
)

TableRestoreStatusMessageTypeDef = TypedDict(
    "TableRestoreStatusMessageTypeDef",
    {
        "TableRestoreStatusDetails": List["TableRestoreStatusTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableRestoreStatusTypeDef = TypedDict(
    "TableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": NotRequired[str],
        "Status": NotRequired[TableRestoreStatusTypeType],
        "Message": NotRequired[str],
        "RequestTime": NotRequired[datetime],
        "ProgressInMegaBytes": NotRequired[int],
        "TotalDataInMegaBytes": NotRequired[int],
        "ClusterIdentifier": NotRequired[str],
        "SnapshotIdentifier": NotRequired[str],
        "SourceDatabaseName": NotRequired[str],
        "SourceSchemaName": NotRequired[str],
        "SourceTableName": NotRequired[str],
        "TargetDatabaseName": NotRequired[str],
        "TargetSchemaName": NotRequired[str],
        "NewTableName": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TaggedResourceListMessageTypeDef = TypedDict(
    "TaggedResourceListMessageTypeDef",
    {
        "TaggedResources": List["TaggedResourceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TaggedResourceTypeDef = TypedDict(
    "TaggedResourceTypeDef",
    {
        "Tag": NotRequired["TagTypeDef"],
        "ResourceName": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

TrackListMessageTypeDef = TypedDict(
    "TrackListMessageTypeDef",
    {
        "MaintenanceTracks": List["MaintenanceTrackTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePartnerStatusInputMessageRequestTypeDef = TypedDict(
    "UpdatePartnerStatusInputMessageRequestTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": str,
        "PartnerName": str,
        "Status": PartnerIntegrationStatusType,
        "StatusMessage": NotRequired[str],
    },
)

UpdateTargetTypeDef = TypedDict(
    "UpdateTargetTypeDef",
    {
        "MaintenanceTrackName": NotRequired[str],
        "DatabaseVersion": NotRequired[str],
        "SupportedOperations": NotRequired[List["SupportedOperationTypeDef"]],
    },
)

UsageLimitListTypeDef = TypedDict(
    "UsageLimitListTypeDef",
    {
        "UsageLimits": List["UsageLimitTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageLimitResponseMetadataTypeDef = TypedDict(
    "UsageLimitResponseMetadataTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageLimitTypeDef = TypedDict(
    "UsageLimitTypeDef",
    {
        "UsageLimitId": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "FeatureType": NotRequired[UsageLimitFeatureTypeType],
        "LimitType": NotRequired[UsageLimitLimitTypeType],
        "Amount": NotRequired[int],
        "Period": NotRequired[UsageLimitPeriodType],
        "BreachAction": NotRequired[UsageLimitBreachActionType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": NotRequired[str],
        "VpcId": NotRequired[str],
        "NetworkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
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
