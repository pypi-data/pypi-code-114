"""
Type annotations for rds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds.type_defs import AccountAttributesMessageTypeDef

    data: AccountAttributesMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActivityStreamModeType,
    ActivityStreamStatusType,
    ApplyMethodType,
    AutomationModeType,
    CustomEngineVersionStatusType,
    DBProxyEndpointStatusType,
    DBProxyEndpointTargetRoleType,
    DBProxyStatusType,
    EngineFamilyType,
    FailoverStatusType,
    IAMAuthModeType,
    ReplicaModeType,
    SourceTypeType,
    TargetHealthReasonType,
    TargetRoleType,
    TargetStateType,
    TargetTypeType,
    WriteForwardingStatusType,
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
    "AccountAttributesMessageTypeDef",
    "AccountQuotaTypeDef",
    "AddRoleToDBClusterMessageRequestTypeDef",
    "AddRoleToDBInstanceMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "BacktrackDBClusterMessageRequestTypeDef",
    "CancelExportTaskMessageRequestTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CharacterSetTypeDef",
    "ClientGenerateDbAuthTokenRequestTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "ConnectionPoolConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupMessageRequestTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CopyDBSnapshotMessageRequestTypeDef",
    "CopyDBSnapshotResultTypeDef",
    "CopyOptionGroupMessageRequestTypeDef",
    "CopyOptionGroupResultTypeDef",
    "CreateCustomAvailabilityZoneMessageRequestTypeDef",
    "CreateCustomAvailabilityZoneResultTypeDef",
    "CreateCustomDBEngineVersionMessageRequestTypeDef",
    "CreateDBClusterEndpointMessageRequestTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBInstanceReadReplicaMessageRequestTypeDef",
    "CreateDBInstanceReadReplicaResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupMessageRequestTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBProxyEndpointRequestRequestTypeDef",
    "CreateDBProxyEndpointResponseTypeDef",
    "CreateDBProxyRequestRequestTypeDef",
    "CreateDBProxyResponseTypeDef",
    "CreateDBSecurityGroupMessageRequestTypeDef",
    "CreateDBSecurityGroupResultTypeDef",
    "CreateDBSnapshotMessageRequestTypeDef",
    "CreateDBSnapshotResultTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterMessageRequestTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "CreateOptionGroupMessageRequestTypeDef",
    "CreateOptionGroupResultTypeDef",
    "CustomAvailabilityZoneMessageTypeDef",
    "CustomAvailabilityZoneTypeDef",
    "DBClusterBacktrackMessageTypeDef",
    "DBClusterBacktrackResponseMetadataTypeDef",
    "DBClusterBacktrackTypeDef",
    "DBClusterCapacityInfoTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterEndpointResponseMetadataTypeDef",
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
    "DBEngineVersionResponseMetadataTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceAutomatedBackupMessageTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    "DBInstanceMessageTypeDef",
    "DBInstanceRoleTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBProxyEndpointTypeDef",
    "DBProxyTargetGroupTypeDef",
    "DBProxyTargetTypeDef",
    "DBProxyTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSecurityGroupMessageTypeDef",
    "DBSecurityGroupTypeDef",
    "DBSnapshotAttributeTypeDef",
    "DBSnapshotAttributesResultTypeDef",
    "DBSnapshotMessageTypeDef",
    "DBSnapshotTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteCustomAvailabilityZoneMessageRequestTypeDef",
    "DeleteCustomAvailabilityZoneResultTypeDef",
    "DeleteCustomDBEngineVersionMessageRequestTypeDef",
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceAutomatedBackupMessageRequestTypeDef",
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBParameterGroupMessageRequestTypeDef",
    "DeleteDBProxyEndpointRequestRequestTypeDef",
    "DeleteDBProxyEndpointResponseTypeDef",
    "DeleteDBProxyRequestRequestTypeDef",
    "DeleteDBProxyResponseTypeDef",
    "DeleteDBSecurityGroupMessageRequestTypeDef",
    "DeleteDBSnapshotMessageRequestTypeDef",
    "DeleteDBSnapshotResultTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterMessageRequestTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DeleteInstallationMediaMessageRequestTypeDef",
    "DeleteOptionGroupMessageRequestTypeDef",
    "DeregisterDBProxyTargetsRequestRequestTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeCustomAvailabilityZonesMessageRequestTypeDef",
    "DescribeDBClusterBacktracksMessageRequestTypeDef",
    "DescribeDBClusterEndpointsMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBLogFilesMessageRequestTypeDef",
    "DescribeDBLogFilesResponseTypeDef",
    "DescribeDBParameterGroupsMessageRequestTypeDef",
    "DescribeDBParametersMessageRequestTypeDef",
    "DescribeDBProxiesRequestRequestTypeDef",
    "DescribeDBProxiesResponseTypeDef",
    "DescribeDBProxyEndpointsRequestRequestTypeDef",
    "DescribeDBProxyEndpointsResponseTypeDef",
    "DescribeDBProxyTargetGroupsRequestRequestTypeDef",
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    "DescribeDBProxyTargetsRequestRequestTypeDef",
    "DescribeDBProxyTargetsResponseTypeDef",
    "DescribeDBSecurityGroupsMessageRequestTypeDef",
    "DescribeDBSnapshotAttributesMessageRequestTypeDef",
    "DescribeDBSnapshotAttributesResultTypeDef",
    "DescribeDBSnapshotsMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeExportTasksMessageRequestTypeDef",
    "DescribeGlobalClustersMessageRequestTypeDef",
    "DescribeInstallationMediaMessageRequestTypeDef",
    "DescribeOptionGroupOptionsMessageRequestTypeDef",
    "DescribeOptionGroupsMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribeReservedDBInstancesMessageRequestTypeDef",
    "DescribeReservedDBInstancesOfferingsMessageRequestTypeDef",
    "DescribeSourceRegionsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsMessageRequestTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "DownloadDBLogFilePortionDetailsTypeDef",
    "DownloadDBLogFilePortionMessageRequestTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "ExportTaskResponseMetadataTypeDef",
    "ExportTaskTypeDef",
    "ExportTasksMessageTypeDef",
    "FailoverDBClusterMessageRequestTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FailoverGlobalClusterMessageRequestTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "FailoverStateTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "IPRangeTypeDef",
    "ImportInstallationMediaMessageRequestTypeDef",
    "InstallationMediaFailureCauseTypeDef",
    "InstallationMediaMessageTypeDef",
    "InstallationMediaResponseMetadataTypeDef",
    "InstallationMediaTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "ModifyCertificatesMessageRequestTypeDef",
    "ModifyCertificatesResultTypeDef",
    "ModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    "ModifyCustomDBEngineVersionMessageRequestTypeDef",
    "ModifyDBClusterEndpointMessageRequestTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBParameterGroupMessageRequestTypeDef",
    "ModifyDBProxyEndpointRequestRequestTypeDef",
    "ModifyDBProxyEndpointResponseTypeDef",
    "ModifyDBProxyRequestRequestTypeDef",
    "ModifyDBProxyResponseTypeDef",
    "ModifyDBProxyTargetGroupRequestRequestTypeDef",
    "ModifyDBProxyTargetGroupResponseTypeDef",
    "ModifyDBSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBSnapshotAttributeResultTypeDef",
    "ModifyDBSnapshotMessageRequestTypeDef",
    "ModifyDBSnapshotResultTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterMessageRequestTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "ModifyOptionGroupMessageRequestTypeDef",
    "ModifyOptionGroupResultTypeDef",
    "OptionConfigurationTypeDef",
    "OptionGroupMembershipTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "OptionGroupOptionTypeDef",
    "OptionGroupOptionsMessageTypeDef",
    "OptionGroupTypeDef",
    "OptionGroupsTypeDef",
    "OptionSettingTypeDef",
    "OptionTypeDef",
    "OptionVersionTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessorFeatureTypeDef",
    "PromoteReadReplicaDBClusterMessageRequestTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "PromoteReadReplicaMessageRequestTypeDef",
    "PromoteReadReplicaResultTypeDef",
    "PurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    "RangeTypeDef",
    "RebootDBClusterMessageRequestTypeDef",
    "RebootDBClusterResultTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RecurringChargeTypeDef",
    "RegisterDBProxyTargetsRequestRequestTypeDef",
    "RegisterDBProxyTargetsResponseTypeDef",
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveRoleFromDBClusterMessageRequestTypeDef",
    "RemoveRoleFromDBInstanceMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReservedDBInstanceMessageTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstancesOfferingMessageTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "ResetDBParameterGroupMessageRequestTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromS3MessageRequestTypeDef",
    "RestoreDBClusterFromS3ResultTypeDef",
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    "RestoreDBInstanceFromS3MessageRequestTypeDef",
    "RestoreDBInstanceFromS3ResultTypeDef",
    "RestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    "RestoreWindowTypeDef",
    "RevokeDBSecurityGroupIngressMessageRequestTypeDef",
    "RevokeDBSecurityGroupIngressResultTypeDef",
    "ScalingConfigurationInfoTypeDef",
    "ScalingConfigurationTypeDef",
    "SourceRegionMessageTypeDef",
    "SourceRegionTypeDef",
    "StartActivityStreamRequestRequestTypeDef",
    "StartActivityStreamResponseTypeDef",
    "StartDBClusterMessageRequestTypeDef",
    "StartDBClusterResultTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StartDBInstanceMessageRequestTypeDef",
    "StartDBInstanceResultTypeDef",
    "StartExportTaskMessageRequestTypeDef",
    "StopActivityStreamRequestRequestTypeDef",
    "StopActivityStreamResponseTypeDef",
    "StopDBClusterMessageRequestTypeDef",
    "StopDBClusterResultTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StopDBInstanceMessageRequestTypeDef",
    "StopDBInstanceResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TargetHealthTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "UserAuthConfigInfoTypeDef",
    "UserAuthConfigTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "VpnDetailsTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributesMessageTypeDef = TypedDict(
    "AccountAttributesMessageTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": NotRequired[str],
        "Used": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AddRoleToDBClusterMessageRequestTypeDef = TypedDict(
    "AddRoleToDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
        "FeatureName": NotRequired[str],
    },
)

AddRoleToDBInstanceMessageRequestTypeDef = TypedDict(
    "AddRoleToDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
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

AuthorizeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "CIDRIP": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupId": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)

AuthorizeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)

AvailableProcessorFeatureTypeDef = TypedDict(
    "AvailableProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[str],
    },
)

BacktrackDBClusterMessageRequestTypeDef = TypedDict(
    "BacktrackDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackTo": Union[datetime, str],
        "Force": NotRequired[bool],
        "UseEarliestTimeOnPointInTimeUnavailable": NotRequired[bool],
    },
)

CancelExportTaskMessageRequestTypeDef = TypedDict(
    "CancelExportTaskMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
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
        "CustomerOverride": NotRequired[bool],
        "CustomerOverrideValidTill": NotRequired[datetime],
    },
)

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef",
    {
        "CharacterSetName": NotRequired[str],
        "CharacterSetDescription": NotRequired[str],
    },
)

ClientGenerateDbAuthTokenRequestTypeDef = TypedDict(
    "ClientGenerateDbAuthTokenRequestTypeDef",
    {
        "DBHostname": str,
        "Port": int,
        "DBUsername": str,
        "Region": NotRequired[str],
    },
)

CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": NotRequired[Sequence[str]],
        "DisableLogTypes": NotRequired[Sequence[str]],
    },
)

ClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClusterPendingModifiedValuesTypeDef",
    {
        "PendingCloudwatchLogsExports": NotRequired["PendingCloudwatchLogsExportsTypeDef"],
        "DBClusterIdentifier": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "EngineVersion": NotRequired[str],
    },
)

ConnectionPoolConfigurationInfoTypeDef = TypedDict(
    "ConnectionPoolConfigurationInfoTypeDef",
    {
        "MaxConnectionsPercent": NotRequired[int],
        "MaxIdleConnectionsPercent": NotRequired[int],
        "ConnectionBorrowTimeout": NotRequired[int],
        "SessionPinningFilters": NotRequired[List[str]],
        "InitQuery": NotRequired[str],
    },
)

ConnectionPoolConfigurationTypeDef = TypedDict(
    "ConnectionPoolConfigurationTypeDef",
    {
        "MaxConnectionsPercent": NotRequired[int],
        "MaxIdleConnectionsPercent": NotRequired[int],
        "ConnectionBorrowTimeout": NotRequired[int],
        "SessionPinningFilters": NotRequired[Sequence[str]],
        "InitQuery": NotRequired[str],
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

CopyDBSnapshotMessageRequestTypeDef = TypedDict(
    "CopyDBSnapshotMessageRequestTypeDef",
    {
        "SourceDBSnapshotIdentifier": str,
        "TargetDBSnapshotIdentifier": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "CopyTags": NotRequired[bool],
        "PreSignedUrl": NotRequired[str],
        "OptionGroupName": NotRequired[str],
        "TargetCustomAvailabilityZone": NotRequired[str],
        "SourceRegion": NotRequired[str],
    },
)

CopyDBSnapshotResultTypeDef = TypedDict(
    "CopyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyOptionGroupMessageRequestTypeDef = TypedDict(
    "CopyOptionGroupMessageRequestTypeDef",
    {
        "SourceOptionGroupIdentifier": str,
        "TargetOptionGroupIdentifier": str,
        "TargetOptionGroupDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopyOptionGroupResultTypeDef = TypedDict(
    "CopyOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomAvailabilityZoneMessageRequestTypeDef = TypedDict(
    "CreateCustomAvailabilityZoneMessageRequestTypeDef",
    {
        "CustomAvailabilityZoneName": str,
        "ExistingVpnId": NotRequired[str],
        "NewVpnTunnelName": NotRequired[str],
        "VpnTunnelOriginatorIP": NotRequired[str],
    },
)

CreateCustomAvailabilityZoneResultTypeDef = TypedDict(
    "CreateCustomAvailabilityZoneResultTypeDef",
    {
        "CustomAvailabilityZone": "CustomAvailabilityZoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "CreateCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DatabaseInstallationFilesS3BucketName": str,
        "KMSKeyId": str,
        "Manifest": str,
        "DatabaseInstallationFilesS3Prefix": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
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

CreateDBClusterMessageRequestTypeDef = TypedDict(
    "CreateDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "CharacterSetName": NotRequired[str],
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
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "ScalingConfiguration": NotRequired["ScalingConfigurationTypeDef"],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterIdentifier": NotRequired[str],
        "EnableHttpEndpoint": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "EnableGlobalWriteForwarding": NotRequired[bool],
        "DBClusterInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
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
        "NcharCharacterSetName": NotRequired[str],
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
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence["ProcessorFeatureTypeDef"]],
        "DeletionProtection": NotRequired[bool],
        "MaxAllocatedStorage": NotRequired[int],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
    },
)

CreateDBInstanceReadReplicaMessageRequestTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "SourceDBInstanceIdentifier": str,
        "DBInstanceClass": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Port": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "DBParameterGroupName": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DBSubnetGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "StorageType": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence["ProcessorFeatureTypeDef"]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "ReplicaMode": NotRequired[ReplicaModeType],
        "MaxAllocatedStorage": NotRequired[int],
        "CustomIamInstanceProfile": NotRequired[str],
        "SourceRegion": NotRequired[str],
    },
)

CreateDBInstanceReadReplicaResultTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

CreateDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "CreateDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "DBProxyEndpointName": str,
        "VpcSubnetIds": Sequence[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "TargetRole": NotRequired[DBProxyEndpointTargetRoleType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBProxyEndpointResponseTypeDef = TypedDict(
    "CreateDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBProxyRequestRequestTypeDef = TypedDict(
    "CreateDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "EngineFamily": EngineFamilyType,
        "Auth": Sequence["UserAuthConfigTypeDef"],
        "RoleArn": str,
        "VpcSubnetIds": Sequence[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "RequireTLS": NotRequired[bool],
        "IdleClientTimeout": NotRequired[int],
        "DebugLogging": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBProxyResponseTypeDef = TypedDict(
    "CreateDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "CreateDBSecurityGroupMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBSecurityGroupResultTypeDef = TypedDict(
    "CreateDBSecurityGroupResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBSnapshotMessageRequestTypeDef = TypedDict(
    "CreateDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDBSnapshotResultTypeDef = TypedDict(
    "CreateDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
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
        "GlobalClusterIdentifier": NotRequired[str],
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

CreateOptionGroupMessageRequestTypeDef = TypedDict(
    "CreateOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "OptionGroupDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateOptionGroupResultTypeDef = TypedDict(
    "CreateOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAvailabilityZoneMessageTypeDef = TypedDict(
    "CustomAvailabilityZoneMessageTypeDef",
    {
        "Marker": str,
        "CustomAvailabilityZones": List["CustomAvailabilityZoneTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAvailabilityZoneTypeDef = TypedDict(
    "CustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": NotRequired[str],
        "CustomAvailabilityZoneName": NotRequired[str],
        "CustomAvailabilityZoneStatus": NotRequired[str],
        "VpnDetails": NotRequired["VpnDetailsTypeDef"],
    },
)

DBClusterBacktrackMessageTypeDef = TypedDict(
    "DBClusterBacktrackMessageTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List["DBClusterBacktrackTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterBacktrackResponseMetadataTypeDef = TypedDict(
    "DBClusterBacktrackResponseMetadataTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterBacktrackTypeDef = TypedDict(
    "DBClusterBacktrackTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "BacktrackIdentifier": NotRequired[str],
        "BacktrackTo": NotRequired[datetime],
        "BacktrackedFrom": NotRequired[datetime],
        "BacktrackRequestCreationTime": NotRequired[datetime],
        "Status": NotRequired[str],
    },
)

DBClusterCapacityInfoTypeDef = TypedDict(
    "DBClusterCapacityInfoTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
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

DBClusterEndpointResponseMetadataTypeDef = TypedDict(
    "DBClusterEndpointResponseMetadataTypeDef",
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
        "EngineMode": NotRequired[str],
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
        "TagList": NotRequired[List["TagTypeDef"]],
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
        "AutomaticRestartTime": NotRequired[datetime],
        "PercentProgress": NotRequired[str],
        "EarliestRestorableTime": NotRequired[datetime],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "CustomEndpoints": NotRequired[List[str]],
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
        "EarliestBacktrackTime": NotRequired[datetime],
        "BacktrackWindow": NotRequired[int],
        "BacktrackConsumedChangeRecords": NotRequired[int],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "Capacity": NotRequired[int],
        "EngineMode": NotRequired[str],
        "ScalingConfigurationInfo": NotRequired["ScalingConfigurationInfoTypeDef"],
        "DeletionProtection": NotRequired[bool],
        "HttpEndpointEnabled": NotRequired[bool],
        "ActivityStreamMode": NotRequired[ActivityStreamModeType],
        "ActivityStreamStatus": NotRequired[ActivityStreamStatusType],
        "ActivityStreamKmsKeyId": NotRequired[str],
        "ActivityStreamKinesisStreamName": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "CrossAccountClone": NotRequired[bool],
        "DomainMemberships": NotRequired[List["DomainMembershipTypeDef"]],
        "TagList": NotRequired[List["TagTypeDef"]],
        "GlobalWriteForwardingStatus": NotRequired[WriteForwardingStatusType],
        "GlobalWriteForwardingRequested": NotRequired[bool],
        "PendingModifiedValues": NotRequired["ClusterPendingModifiedValuesTypeDef"],
        "DBClusterInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
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

DBEngineVersionResponseMetadataTypeDef = TypedDict(
    "DBEngineVersionResponseMetadataTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": "CharacterSetTypeDef",
        "SupportedCharacterSets": List["CharacterSetTypeDef"],
        "SupportedNcharCharacterSets": List["CharacterSetTypeDef"],
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "SupportedTimezones": List["TimezoneTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
        "MajorEngineVersion": str,
        "DatabaseInstallationFilesS3BucketName": str,
        "DatabaseInstallationFilesS3Prefix": str,
        "DBEngineVersionArn": str,
        "KMSKeyId": str,
        "CreateTime": datetime,
        "TagList": List["TagTypeDef"],
        "SupportsBabelfish": bool,
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
        "SupportedNcharCharacterSets": NotRequired[List["CharacterSetTypeDef"]],
        "ValidUpgradeTarget": NotRequired[List["UpgradeTargetTypeDef"]],
        "SupportedTimezones": NotRequired[List["TimezoneTypeDef"]],
        "ExportableLogTypes": NotRequired[List[str]],
        "SupportsLogExportsToCloudwatchLogs": NotRequired[bool],
        "SupportsReadReplica": NotRequired[bool],
        "SupportedEngineModes": NotRequired[List[str]],
        "SupportedFeatureNames": NotRequired[List[str]],
        "Status": NotRequired[str],
        "SupportsParallelQuery": NotRequired[bool],
        "SupportsGlobalDatabases": NotRequired[bool],
        "MajorEngineVersion": NotRequired[str],
        "DatabaseInstallationFilesS3BucketName": NotRequired[str],
        "DatabaseInstallationFilesS3Prefix": NotRequired[str],
        "DBEngineVersionArn": NotRequired[str],
        "KMSKeyId": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "TagList": NotRequired[List["TagTypeDef"]],
        "SupportsBabelfish": NotRequired[bool],
    },
)

DBInstanceAutomatedBackupMessageTypeDef = TypedDict(
    "DBInstanceAutomatedBackupMessageTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List["DBInstanceAutomatedBackupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBInstanceAutomatedBackupTypeDef = TypedDict(
    "DBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "Region": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "RestoreWindow": NotRequired["RestoreWindowTypeDef"],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "StorageType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Timezone": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "BackupRetentionPeriod": NotRequired[int],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
        "DBInstanceAutomatedBackupsReplications": NotRequired[
            List["DBInstanceAutomatedBackupsReplicationTypeDef"]
        ],
        "BackupTarget": NotRequired[str],
    },
)

DBInstanceAutomatedBackupsReplicationTypeDef = TypedDict(
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    {
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
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

DBInstanceRoleTypeDef = TypedDict(
    "DBInstanceRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FeatureName": NotRequired[str],
        "Status": NotRequired[str],
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
        "AutomaticRestartTime": NotRequired[datetime],
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
        "ReplicaMode": NotRequired[ReplicaModeType],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupMemberships": NotRequired[List["OptionGroupMembershipTypeDef"]],
        "CharacterSetName": NotRequired[str],
        "NcharCharacterSetName": NotRequired[str],
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
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "ProcessorFeatures": NotRequired[List["ProcessorFeatureTypeDef"]],
        "DeletionProtection": NotRequired[bool],
        "AssociatedRoles": NotRequired[List["DBInstanceRoleTypeDef"]],
        "ListenerEndpoint": NotRequired["EndpointTypeDef"],
        "MaxAllocatedStorage": NotRequired[int],
        "TagList": NotRequired[List["TagTypeDef"]],
        "DBInstanceAutomatedBackupsReplications": NotRequired[
            List["DBInstanceAutomatedBackupsReplicationTypeDef"]
        ],
        "CustomerOwnedIpEnabled": NotRequired[bool],
        "AwsBackupRecoveryPointArn": NotRequired[str],
        "ActivityStreamStatus": NotRequired[ActivityStreamStatusType],
        "ActivityStreamKmsKeyId": NotRequired[str],
        "ActivityStreamKinesisStreamName": NotRequired[str],
        "ActivityStreamMode": NotRequired[ActivityStreamModeType],
        "ActivityStreamEngineNativeAuditFieldsIncluded": NotRequired[bool],
        "AutomationMode": NotRequired[AutomationModeType],
        "ResumeFullAutomationModeTime": NotRequired[datetime],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
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

DBProxyEndpointTypeDef = TypedDict(
    "DBProxyEndpointTypeDef",
    {
        "DBProxyEndpointName": NotRequired[str],
        "DBProxyEndpointArn": NotRequired[str],
        "DBProxyName": NotRequired[str],
        "Status": NotRequired[DBProxyEndpointStatusType],
        "VpcId": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[List[str]],
        "VpcSubnetIds": NotRequired[List[str]],
        "Endpoint": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "TargetRole": NotRequired[DBProxyEndpointTargetRoleType],
        "IsDefault": NotRequired[bool],
    },
)

DBProxyTargetGroupTypeDef = TypedDict(
    "DBProxyTargetGroupTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "TargetGroupName": NotRequired[str],
        "TargetGroupArn": NotRequired[str],
        "IsDefault": NotRequired[bool],
        "Status": NotRequired[str],
        "ConnectionPoolConfig": NotRequired["ConnectionPoolConfigurationInfoTypeDef"],
        "CreatedDate": NotRequired[datetime],
        "UpdatedDate": NotRequired[datetime],
    },
)

DBProxyTargetTypeDef = TypedDict(
    "DBProxyTargetTypeDef",
    {
        "TargetArn": NotRequired[str],
        "Endpoint": NotRequired[str],
        "TrackedClusterId": NotRequired[str],
        "RdsResourceId": NotRequired[str],
        "Port": NotRequired[int],
        "Type": NotRequired[TargetTypeType],
        "Role": NotRequired[TargetRoleType],
        "TargetHealth": NotRequired["TargetHealthTypeDef"],
    },
)

DBProxyTypeDef = TypedDict(
    "DBProxyTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "DBProxyArn": NotRequired[str],
        "Status": NotRequired[DBProxyStatusType],
        "EngineFamily": NotRequired[str],
        "VpcId": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[List[str]],
        "VpcSubnetIds": NotRequired[List[str]],
        "Auth": NotRequired[List["UserAuthConfigInfoTypeDef"]],
        "RoleArn": NotRequired[str],
        "Endpoint": NotRequired[str],
        "RequireTLS": NotRequired[bool],
        "IdleClientTimeout": NotRequired[int],
        "DebugLogging": NotRequired[bool],
        "CreatedDate": NotRequired[datetime],
        "UpdatedDate": NotRequired[datetime],
    },
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

DBSecurityGroupMessageTypeDef = TypedDict(
    "DBSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List["DBSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSecurityGroupTypeDef = TypedDict(
    "DBSecurityGroupTypeDef",
    {
        "OwnerId": NotRequired[str],
        "DBSecurityGroupName": NotRequired[str],
        "DBSecurityGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "EC2SecurityGroups": NotRequired[List["EC2SecurityGroupTypeDef"]],
        "IPRanges": NotRequired[List["IPRangeTypeDef"]],
        "DBSecurityGroupArn": NotRequired[str],
    },
)

DBSnapshotAttributeTypeDef = TypedDict(
    "DBSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)

DBSnapshotAttributesResultTypeDef = TypedDict(
    "DBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": NotRequired[str],
        "DBSnapshotAttributes": NotRequired[List["DBSnapshotAttributeTypeDef"]],
    },
)

DBSnapshotMessageTypeDef = TypedDict(
    "DBSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBSnapshots": List["DBSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSnapshotTypeDef = TypedDict(
    "DBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[datetime],
        "Engine": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "InstanceCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "SourceRegion": NotRequired[str],
        "SourceDBSnapshotIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DBSnapshotArn": NotRequired[str],
        "Timezone": NotRequired[str],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "ProcessorFeatures": NotRequired[List["ProcessorFeatureTypeDef"]],
        "DbiResourceId": NotRequired[str],
        "TagList": NotRequired[List["TagTypeDef"]],
        "OriginalSnapshotCreateTime": NotRequired[datetime],
        "SnapshotTarget": NotRequired[str],
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

DeleteCustomAvailabilityZoneMessageRequestTypeDef = TypedDict(
    "DeleteCustomAvailabilityZoneMessageRequestTypeDef",
    {
        "CustomAvailabilityZoneId": str,
    },
)

DeleteCustomAvailabilityZoneResultTypeDef = TypedDict(
    "DeleteCustomAvailabilityZoneResultTypeDef",
    {
        "CustomAvailabilityZone": "CustomAvailabilityZoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "DeleteCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
    },
)

DeleteDBClusterEndpointMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageRequestTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
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

DeleteDBInstanceAutomatedBackupMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupMessageRequestTypeDef",
    {
        "DbiResourceId": NotRequired[str],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
    },
)

DeleteDBInstanceAutomatedBackupResultTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
        "DeleteAutomatedBackups": NotRequired[bool],
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

DeleteDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "DeleteDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyEndpointName": str,
    },
)

DeleteDBProxyEndpointResponseTypeDef = TypedDict(
    "DeleteDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBProxyRequestRequestTypeDef = TypedDict(
    "DeleteDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
    },
)

DeleteDBProxyResponseTypeDef = TypedDict(
    "DeleteDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSecurityGroupMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)

DeleteDBSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)

DeleteDBSnapshotResultTypeDef = TypedDict(
    "DeleteDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
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

DeleteInstallationMediaMessageRequestTypeDef = TypedDict(
    "DeleteInstallationMediaMessageRequestTypeDef",
    {
        "InstallationMediaId": str,
    },
)

DeleteOptionGroupMessageRequestTypeDef = TypedDict(
    "DeleteOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
    },
)

DeregisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "DeregisterDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "DBInstanceIdentifiers": NotRequired[Sequence[str]],
        "DBClusterIdentifiers": NotRequired[Sequence[str]],
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

DescribeCustomAvailabilityZonesMessageRequestTypeDef = TypedDict(
    "DescribeCustomAvailabilityZonesMessageRequestTypeDef",
    {
        "CustomAvailabilityZoneId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBClusterBacktracksMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterBacktracksMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
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
        "IncludeShared": NotRequired[bool],
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
        "IncludeAll": NotRequired[bool],
    },
)

DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef = TypedDict(
    "DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef",
    {
        "DbiResourceId": NotRequired[str],
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DBInstanceAutomatedBackupsArn": NotRequired[str],
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

DescribeDBLogFilesDetailsTypeDef = TypedDict(
    "DescribeDBLogFilesDetailsTypeDef",
    {
        "LogFileName": NotRequired[str],
        "LastWritten": NotRequired[int],
        "Size": NotRequired[int],
    },
)

DescribeDBLogFilesMessageRequestTypeDef = TypedDict(
    "DescribeDBLogFilesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "FilenameContains": NotRequired[str],
        "FileLastWritten": NotRequired[int],
        "FileSize": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBLogFilesResponseTypeDef = TypedDict(
    "DescribeDBLogFilesResponseTypeDef",
    {
        "DescribeDBLogFiles": List["DescribeDBLogFilesDetailsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DescribeDBProxiesRequestRequestTypeDef = TypedDict(
    "DescribeDBProxiesRequestRequestTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeDBProxiesResponseTypeDef = TypedDict(
    "DescribeDBProxiesResponseTypeDef",
    {
        "DBProxies": List["DBProxyTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBProxyEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyEndpointsRequestRequestTypeDef",
    {
        "DBProxyName": NotRequired[str],
        "DBProxyEndpointName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeDBProxyEndpointsResponseTypeDef = TypedDict(
    "DescribeDBProxyEndpointsResponseTypeDef",
    {
        "DBProxyEndpoints": List["DBProxyEndpointTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBProxyTargetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeDBProxyTargetGroupsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List["DBProxyTargetGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "DescribeDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribeDBProxyTargetsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetsResponseTypeDef",
    {
        "Targets": List["DBProxyTargetTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSecurityGroupsMessageRequestTypeDef",
    {
        "DBSecurityGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeDBSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)

DescribeDBSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "DbiResourceId": NotRequired[str],
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

DescribeExportTasksMessageRequestTypeDef = TypedDict(
    "DescribeExportTasksMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": NotRequired[str],
        "SourceArn": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
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

DescribeInstallationMediaMessageRequestTypeDef = TypedDict(
    "DescribeInstallationMediaMessageRequestTypeDef",
    {
        "InstallationMediaId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeOptionGroupOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOptionGroupOptionsMessageRequestTypeDef",
    {
        "EngineName": str,
        "MajorEngineVersion": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeOptionGroupsMessageRequestTypeDef = TypedDict(
    "DescribeOptionGroupsMessageRequestTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
    },
)

DescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
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

DescribeReservedDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReservedDBInstancesMessageRequestTypeDef",
    {
        "ReservedDBInstanceId": NotRequired[str],
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "LeaseId": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReservedDBInstancesOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedDBInstancesOfferingsMessageRequestTypeDef",
    {
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeSourceRegionsMessageRequestTypeDef = TypedDict(
    "DescribeSourceRegionsMessageRequestTypeDef",
    {
        "RegionName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
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

DownloadDBLogFilePortionDetailsTypeDef = TypedDict(
    "DownloadDBLogFilePortionDetailsTypeDef",
    {
        "LogFileData": str,
        "Marker": str,
        "AdditionalDataPending": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DownloadDBLogFilePortionMessageRequestTypeDef = TypedDict(
    "DownloadDBLogFilePortionMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "LogFileName": str,
        "Marker": NotRequired[str],
        "NumberOfLines": NotRequired[int],
    },
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupId": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
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

ExportTaskResponseMetadataTypeDef = TypedDict(
    "ExportTaskResponseMetadataTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "ExportTaskIdentifier": NotRequired[str],
        "SourceArn": NotRequired[str],
        "ExportOnly": NotRequired[List[str]],
        "SnapshotTime": NotRequired[datetime],
        "TaskStartTime": NotRequired[datetime],
        "TaskEndTime": NotRequired[datetime],
        "S3Bucket": NotRequired[str],
        "S3Prefix": NotRequired[str],
        "IamRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Status": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "TotalExtractedDataInGB": NotRequired[int],
        "FailureCause": NotRequired[str],
        "WarningMessage": NotRequired[str],
    },
)

ExportTasksMessageTypeDef = TypedDict(
    "ExportTasksMessageTypeDef",
    {
        "Marker": str,
        "ExportTasks": List["ExportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverDBClusterMessageRequestTypeDef = TypedDict(
    "FailoverDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
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

FailoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "FailoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
    },
)

FailoverGlobalClusterResultTypeDef = TypedDict(
    "FailoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverStateTypeDef = TypedDict(
    "FailoverStateTypeDef",
    {
        "Status": NotRequired[FailoverStatusType],
        "FromDbClusterArn": NotRequired[str],
        "ToDbClusterArn": NotRequired[str],
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
        "GlobalWriteForwardingStatus": NotRequired[WriteForwardingStatusType],
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
        "FailoverState": NotRequired["FailoverStateTypeDef"],
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

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": NotRequired[str],
        "CIDRIP": NotRequired[str],
    },
)

ImportInstallationMediaMessageRequestTypeDef = TypedDict(
    "ImportInstallationMediaMessageRequestTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
    },
)

InstallationMediaFailureCauseTypeDef = TypedDict(
    "InstallationMediaFailureCauseTypeDef",
    {
        "Message": NotRequired[str],
    },
)

InstallationMediaMessageTypeDef = TypedDict(
    "InstallationMediaMessageTypeDef",
    {
        "Marker": str,
        "InstallationMedia": List["InstallationMediaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstallationMediaResponseMetadataTypeDef = TypedDict(
    "InstallationMediaResponseMetadataTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": "InstallationMediaFailureCauseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstallationMediaTypeDef = TypedDict(
    "InstallationMediaTypeDef",
    {
        "InstallationMediaId": NotRequired[str],
        "CustomAvailabilityZoneId": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EngineInstallationMediaPath": NotRequired[str],
        "OSInstallationMediaPath": NotRequired[str],
        "Status": NotRequired[str],
        "FailureCause": NotRequired["InstallationMediaFailureCauseTypeDef"],
    },
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

MinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "MinimumEngineVersionPerAllowedValueTypeDef",
    {
        "AllowedValue": NotRequired[str],
        "MinimumEngineVersion": NotRequired[str],
    },
)

ModifyCertificatesMessageRequestTypeDef = TypedDict(
    "ModifyCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "RemoveCustomerOverride": NotRequired[bool],
    },
)

ModifyCertificatesResultTypeDef = TypedDict(
    "ModifyCertificatesResultTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCurrentDBClusterCapacityMessageRequestTypeDef = TypedDict(
    "ModifyCurrentDBClusterCapacityMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Capacity": NotRequired[int],
        "SecondsBeforeTimeout": NotRequired[int],
        "TimeoutAction": NotRequired[str],
    },
)

ModifyCustomDBEngineVersionMessageRequestTypeDef = TypedDict(
    "ModifyCustomDBEngineVersionMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": NotRequired[str],
        "Status": NotRequired[CustomEngineVersionStatusType],
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
        "BacktrackWindow": NotRequired[int],
        "CloudwatchLogsExportConfiguration": NotRequired[
            "CloudwatchLogsExportConfigurationTypeDef"
        ],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "DBInstanceParameterGroupName": NotRequired[str],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "ScalingConfiguration": NotRequired["ScalingConfigurationTypeDef"],
        "DeletionProtection": NotRequired[bool],
        "EnableHttpEndpoint": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "EnableGlobalWriteForwarding": NotRequired[bool],
        "DBClusterInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
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
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "CloudwatchLogsExportConfiguration": NotRequired[
            "CloudwatchLogsExportConfigurationTypeDef"
        ],
        "ProcessorFeatures": NotRequired[Sequence["ProcessorFeatureTypeDef"]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "MaxAllocatedStorage": NotRequired[int],
        "CertificateRotationRestart": NotRequired[bool],
        "ReplicaMode": NotRequired[ReplicaModeType],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "AwsBackupRecoveryPointArn": NotRequired[str],
        "AutomationMode": NotRequired[AutomationModeType],
        "ResumeFullAutomationModeMinutes": NotRequired[int],
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

ModifyDBProxyEndpointRequestRequestTypeDef = TypedDict(
    "ModifyDBProxyEndpointRequestRequestTypeDef",
    {
        "DBProxyEndpointName": str,
        "NewDBProxyEndpointName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)

ModifyDBProxyEndpointResponseTypeDef = TypedDict(
    "ModifyDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBProxyRequestRequestTypeDef = TypedDict(
    "ModifyDBProxyRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "NewDBProxyName": NotRequired[str],
        "Auth": NotRequired[Sequence["UserAuthConfigTypeDef"]],
        "RequireTLS": NotRequired[bool],
        "IdleClientTimeout": NotRequired[int],
        "DebugLogging": NotRequired[bool],
        "RoleArn": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)

ModifyDBProxyResponseTypeDef = TypedDict(
    "ModifyDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBProxyTargetGroupRequestRequestTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupRequestRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBProxyName": str,
        "ConnectionPoolConfig": NotRequired["ConnectionPoolConfigurationTypeDef"],
        "NewName": NotRequired[str],
    },
)

ModifyDBProxyTargetGroupResponseTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupResponseTypeDef",
    {
        "DBProxyTargetGroup": "DBProxyTargetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "AttributeName": str,
        "ValuesToAdd": NotRequired[Sequence[str]],
        "ValuesToRemove": NotRequired[Sequence[str]],
    },
)

ModifyDBSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeResultTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBSnapshotMessageRequestTypeDef = TypedDict(
    "ModifyDBSnapshotMessageRequestTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "EngineVersion": NotRequired[str],
        "OptionGroupName": NotRequired[str],
    },
)

ModifyDBSnapshotResultTypeDef = TypedDict(
    "ModifyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
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
        "GlobalClusterIdentifier": NotRequired[str],
        "NewGlobalClusterIdentifier": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
    },
)

ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyOptionGroupMessageRequestTypeDef = TypedDict(
    "ModifyOptionGroupMessageRequestTypeDef",
    {
        "OptionGroupName": str,
        "OptionsToInclude": NotRequired[Sequence["OptionConfigurationTypeDef"]],
        "OptionsToRemove": NotRequired[Sequence[str]],
        "ApplyImmediately": NotRequired[bool],
    },
)

ModifyOptionGroupResultTypeDef = TypedDict(
    "ModifyOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionConfigurationTypeDef = TypedDict(
    "OptionConfigurationTypeDef",
    {
        "OptionName": str,
        "Port": NotRequired[int],
        "OptionVersion": NotRequired[str],
        "DBSecurityGroupMemberships": NotRequired[Sequence[str]],
        "VpcSecurityGroupMemberships": NotRequired[Sequence[str]],
        "OptionSettings": NotRequired[Sequence["OptionSettingTypeDef"]],
    },
)

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)

OptionGroupOptionSettingTypeDef = TypedDict(
    "OptionGroupOptionSettingTypeDef",
    {
        "SettingName": NotRequired[str],
        "SettingDescription": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ApplyType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "IsRequired": NotRequired[bool],
        "MinimumEngineVersionPerAllowedValue": NotRequired[
            List["MinimumEngineVersionPerAllowedValueTypeDef"]
        ],
    },
)

OptionGroupOptionTypeDef = TypedDict(
    "OptionGroupOptionTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "MinimumRequiredMinorEngineVersion": NotRequired[str],
        "PortRequired": NotRequired[bool],
        "DefaultPort": NotRequired[int],
        "OptionsDependedOn": NotRequired[List[str]],
        "OptionsConflictsWith": NotRequired[List[str]],
        "Persistent": NotRequired[bool],
        "Permanent": NotRequired[bool],
        "RequiresAutoMinorEngineVersionUpgrade": NotRequired[bool],
        "VpcOnly": NotRequired[bool],
        "SupportsOptionVersionDowngrade": NotRequired[bool],
        "OptionGroupOptionSettings": NotRequired[List["OptionGroupOptionSettingTypeDef"]],
        "OptionGroupOptionVersions": NotRequired[List["OptionVersionTypeDef"]],
    },
)

OptionGroupOptionsMessageTypeDef = TypedDict(
    "OptionGroupOptionsMessageTypeDef",
    {
        "OptionGroupOptions": List["OptionGroupOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionGroupTypeDef = TypedDict(
    "OptionGroupTypeDef",
    {
        "OptionGroupName": NotRequired[str],
        "OptionGroupDescription": NotRequired[str],
        "EngineName": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "Options": NotRequired[List["OptionTypeDef"]],
        "AllowsVpcAndNonVpcInstanceMemberships": NotRequired[bool],
        "VpcId": NotRequired[str],
        "OptionGroupArn": NotRequired[str],
    },
)

OptionGroupsTypeDef = TypedDict(
    "OptionGroupsTypeDef",
    {
        "OptionGroupsList": List["OptionGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionSettingTypeDef = TypedDict(
    "OptionSettingTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "ApplyType": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "IsCollection": NotRequired[bool],
    },
)

OptionTypeDef = TypedDict(
    "OptionTypeDef",
    {
        "OptionName": NotRequired[str],
        "OptionDescription": NotRequired[str],
        "Persistent": NotRequired[bool],
        "Permanent": NotRequired[bool],
        "Port": NotRequired[int],
        "OptionVersion": NotRequired[str],
        "OptionSettings": NotRequired[List["OptionSettingTypeDef"]],
        "DBSecurityGroupMemberships": NotRequired[List["DBSecurityGroupMembershipTypeDef"]],
        "VpcSecurityGroupMemberships": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
    },
)

OptionVersionTypeDef = TypedDict(
    "OptionVersionTypeDef",
    {
        "Version": NotRequired[str],
        "IsDefault": NotRequired[bool],
    },
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZoneGroup": NotRequired[str],
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
        "AvailableProcessorFeatures": NotRequired[List["AvailableProcessorFeatureTypeDef"]],
        "SupportedEngineModes": NotRequired[List[str]],
        "SupportsStorageAutoscaling": NotRequired[bool],
        "SupportsKerberosAuthentication": NotRequired[bool],
        "OutpostCapable": NotRequired[bool],
        "SupportedActivityStreamModes": NotRequired[List[str]],
        "SupportsGlobalDatabases": NotRequired[bool],
        "SupportsClusters": NotRequired[bool],
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

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "Arn": NotRequired[str],
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
        "SupportedEngineModes": NotRequired[List[str]],
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
        "ProcessorFeatures": NotRequired[List["ProcessorFeatureTypeDef"]],
        "IAMDatabaseAuthenticationEnabled": NotRequired[bool],
        "AutomationMode": NotRequired[AutomationModeType],
        "ResumeFullAutomationModeTime": NotRequired[datetime],
    },
)

ProcessorFeatureTypeDef = TypedDict(
    "ProcessorFeatureTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
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

PromoteReadReplicaMessageRequestTypeDef = TypedDict(
    "PromoteReadReplicaMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "BackupRetentionPeriod": NotRequired[int],
        "PreferredBackupWindow": NotRequired[str],
    },
)

PromoteReadReplicaResultTypeDef = TypedDict(
    "PromoteReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseReservedDBInstancesOfferingMessageRequestTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingMessageRequestTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "ReservedDBInstanceId": NotRequired[str],
        "DBInstanceCount": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PurchaseReservedDBInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    {
        "ReservedDBInstance": "ReservedDBInstanceTypeDef",
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

RebootDBClusterMessageRequestTypeDef = TypedDict(
    "RebootDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

RebootDBClusterResultTypeDef = TypedDict(
    "RebootDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": NotRequired[float],
        "RecurringChargeFrequency": NotRequired[str],
    },
)

RegisterDBProxyTargetsRequestRequestTypeDef = TypedDict(
    "RegisterDBProxyTargetsRequestRequestTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": NotRequired[str],
        "DBInstanceIdentifiers": NotRequired[Sequence[str]],
        "DBClusterIdentifiers": NotRequired[Sequence[str]],
    },
)

RegisterDBProxyTargetsResponseTypeDef = TypedDict(
    "RegisterDBProxyTargetsResponseTypeDef",
    {
        "DBProxyTargets": List["DBProxyTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFromGlobalClusterMessageRequestTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "DbClusterIdentifier": NotRequired[str],
    },
)

RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
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

RemoveRoleFromDBInstanceMessageRequestTypeDef = TypedDict(
    "RemoveRoleFromDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
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

ReservedDBInstanceMessageTypeDef = TypedDict(
    "ReservedDBInstanceMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List["ReservedDBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedDBInstanceTypeDef = TypedDict(
    "ReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": NotRequired[str],
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "DBInstanceCount": NotRequired[int],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "State": NotRequired[str],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
        "ReservedDBInstanceArn": NotRequired[str],
        "LeaseId": NotRequired[str],
    },
)

ReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "ReservedDBInstancesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List["ReservedDBInstancesOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedDBInstancesOfferingTypeDef = TypedDict(
    "ReservedDBInstancesOfferingTypeDef",
    {
        "ReservedDBInstancesOfferingId": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CurrencyCode": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "RecurringCharges": NotRequired[List["RecurringChargeTypeDef"]],
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

RestoreDBClusterFromS3MessageRequestTypeDef = TypedDict(
    "RestoreDBClusterFromS3MessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "CharacterSetName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "DBSubnetGroupName": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "S3Prefix": NotRequired[str],
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
    },
)

RestoreDBClusterFromS3ResultTypeDef = TypedDict(
    "RestoreDBClusterFromS3ResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "EngineMode": NotRequired[str],
        "ScalingConfiguration": NotRequired["ScalingConfigurationTypeDef"],
        "DBClusterParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "DBClusterInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "Iops": NotRequired[int],
        "PubliclyAccessible": NotRequired[bool],
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
        "BacktrackWindow": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DBClusterParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "ScalingConfiguration": NotRequired["ScalingConfigurationTypeDef"],
        "EngineMode": NotRequired[str],
        "DBClusterInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "Iops": NotRequired[int],
    },
)

RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": str,
        "DBInstanceClass": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "DBName": NotRequired[str],
        "Engine": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Domain": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "DomainIAMRoleName": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence["ProcessorFeatureTypeDef"]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DBParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
    },
)

RestoreDBInstanceFromDBSnapshotResultTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreDBInstanceFromS3MessageRequestTypeDef = TypedDict(
    "RestoreDBInstanceFromS3MessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
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
        "PubliclyAccessible": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "StorageType": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "MonitoringInterval": NotRequired[int],
        "MonitoringRoleArn": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "S3Prefix": NotRequired[str],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "PerformanceInsightsRetentionPeriod": NotRequired[int],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence["ProcessorFeatureTypeDef"]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "MaxAllocatedStorage": NotRequired[int],
    },
)

RestoreDBInstanceFromS3ResultTypeDef = TypedDict(
    "RestoreDBInstanceFromS3ResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreDBInstanceToPointInTimeMessageRequestTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeMessageRequestTypeDef",
    {
        "TargetDBInstanceIdentifier": str,
        "SourceDBInstanceIdentifier": NotRequired[str],
        "RestoreTime": NotRequired[Union[datetime, str]],
        "UseLatestRestorableTime": NotRequired[bool],
        "DBInstanceClass": NotRequired[str],
        "Port": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "PubliclyAccessible": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "LicenseModel": NotRequired[str],
        "DBName": NotRequired[str],
        "Engine": NotRequired[str],
        "Iops": NotRequired[int],
        "OptionGroupName": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "StorageType": NotRequired[str],
        "TdeCredentialArn": NotRequired[str],
        "TdeCredentialPassword": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Domain": NotRequired[str],
        "DomainIAMRoleName": NotRequired[str],
        "EnableIAMDatabaseAuthentication": NotRequired[bool],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "ProcessorFeatures": NotRequired[Sequence["ProcessorFeatureTypeDef"]],
        "UseDefaultProcessorFeatures": NotRequired[bool],
        "DBParameterGroupName": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "SourceDbiResourceId": NotRequired[str],
        "MaxAllocatedStorage": NotRequired[int],
        "SourceDBInstanceAutomatedBackupsArn": NotRequired[str],
        "EnableCustomerOwnedIp": NotRequired[bool],
        "CustomIamInstanceProfile": NotRequired[str],
        "BackupTarget": NotRequired[str],
    },
)

RestoreDBInstanceToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreWindowTypeDef = TypedDict(
    "RestoreWindowTypeDef",
    {
        "EarliestTime": NotRequired[datetime],
        "LatestTime": NotRequired[datetime],
    },
)

RevokeDBSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressMessageRequestTypeDef",
    {
        "DBSecurityGroupName": str,
        "CIDRIP": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupId": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)

RevokeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScalingConfigurationInfoTypeDef = TypedDict(
    "ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
        "AutoPause": NotRequired[bool],
        "SecondsUntilAutoPause": NotRequired[int],
        "TimeoutAction": NotRequired[str],
        "SecondsBeforeTimeout": NotRequired[int],
    },
)

ScalingConfigurationTypeDef = TypedDict(
    "ScalingConfigurationTypeDef",
    {
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
        "AutoPause": NotRequired[bool],
        "SecondsUntilAutoPause": NotRequired[int],
        "TimeoutAction": NotRequired[str],
        "SecondsBeforeTimeout": NotRequired[int],
    },
)

SourceRegionMessageTypeDef = TypedDict(
    "SourceRegionMessageTypeDef",
    {
        "Marker": str,
        "SourceRegions": List["SourceRegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceRegionTypeDef = TypedDict(
    "SourceRegionTypeDef",
    {
        "RegionName": NotRequired[str],
        "Endpoint": NotRequired[str],
        "Status": NotRequired[str],
        "SupportsDBInstanceAutomatedBackupsReplication": NotRequired[bool],
    },
)

StartActivityStreamRequestRequestTypeDef = TypedDict(
    "StartActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Mode": ActivityStreamModeType,
        "KmsKeyId": str,
        "ApplyImmediately": NotRequired[bool],
        "EngineNativeAuditFieldsIncluded": NotRequired[bool],
    },
)

StartActivityStreamResponseTypeDef = TypedDict(
    "StartActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
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

StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "SourceDBInstanceArn": str,
        "BackupRetentionPeriod": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "SourceRegion": NotRequired[str],
    },
)

StartDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBInstanceMessageRequestTypeDef = TypedDict(
    "StartDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

StartDBInstanceResultTypeDef = TypedDict(
    "StartDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartExportTaskMessageRequestTypeDef = TypedDict(
    "StartExportTaskMessageRequestTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "S3BucketName": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "S3Prefix": NotRequired[str],
        "ExportOnly": NotRequired[Sequence[str]],
    },
)

StopActivityStreamRequestRequestTypeDef = TypedDict(
    "StopActivityStreamRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ApplyImmediately": NotRequired[bool],
    },
)

StopActivityStreamResponseTypeDef = TypedDict(
    "StopActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
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

StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef",
    {
        "SourceDBInstanceArn": str,
    },
)

StopDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDBInstanceMessageRequestTypeDef = TypedDict(
    "StopDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": NotRequired[str],
    },
)

StopDBInstanceResultTypeDef = TypedDict(
    "StopDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired["AvailabilityZoneTypeDef"],
        "SubnetOutpost": NotRequired["OutpostTypeDef"],
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

TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": NotRequired[TargetStateType],
        "Reason": NotRequired[TargetHealthReasonType],
        "Description": NotRequired[str],
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
        "SupportedEngineModes": NotRequired[List[str]],
        "SupportsParallelQuery": NotRequired[bool],
        "SupportsGlobalDatabases": NotRequired[bool],
        "SupportsBabelfish": NotRequired[bool],
    },
)

UserAuthConfigInfoTypeDef = TypedDict(
    "UserAuthConfigInfoTypeDef",
    {
        "Description": NotRequired[str],
        "UserName": NotRequired[str],
        "AuthScheme": NotRequired[Literal["SECRETS"]],
        "SecretArn": NotRequired[str],
        "IAMAuth": NotRequired[IAMAuthModeType],
    },
)

UserAuthConfigTypeDef = TypedDict(
    "UserAuthConfigTypeDef",
    {
        "Description": NotRequired[str],
        "UserName": NotRequired[str],
        "AuthScheme": NotRequired[Literal["SECRETS"]],
        "SecretArn": NotRequired[str],
        "IAMAuth": NotRequired[IAMAuthModeType],
    },
)

ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": NotRequired[List["ValidStorageOptionsTypeDef"]],
        "ValidProcessorFeatures": NotRequired[List["AvailableProcessorFeatureTypeDef"]],
    },
)

ValidStorageOptionsTypeDef = TypedDict(
    "ValidStorageOptionsTypeDef",
    {
        "StorageType": NotRequired[str],
        "StorageSize": NotRequired[List["RangeTypeDef"]],
        "ProvisionedIops": NotRequired[List["RangeTypeDef"]],
        "IopsToStorageRatio": NotRequired[List["DoubleRangeTypeDef"]],
        "SupportsStorageAutoscaling": NotRequired[bool],
    },
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)

VpnDetailsTypeDef = TypedDict(
    "VpnDetailsTypeDef",
    {
        "VpnId": NotRequired[str],
        "VpnTunnelOriginatorIP": NotRequired[str],
        "VpnGatewayIp": NotRequired[str],
        "VpnPSK": NotRequired[str],
        "VpnName": NotRequired[str],
        "VpnState": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
