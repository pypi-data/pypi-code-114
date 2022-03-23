"""
Type annotations for dms service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_dms/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AuthMechanismValueType,
    AuthTypeValueType,
    CannedAclForObjectsValueType,
    CharLengthSemanticsType,
    CompressionTypeValueType,
    DataFormatValueType,
    DatePartitionDelimiterValueType,
    DatePartitionSequenceValueType,
    DmsSslModeValueType,
    EncodingTypeValueType,
    EncryptionModeValueType,
    EndpointSettingTypeValueType,
    KafkaSecurityProtocolType,
    MessageFormatValueType,
    MigrationTypeValueType,
    NestingLevelValueType,
    ParquetVersionValueType,
    PluginNameValueType,
    RedisAuthTypeValueType,
    RefreshSchemasStatusTypeValueType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    SafeguardPolicyType,
    SslSecurityProtocolValueType,
    StartReplicationTaskTypeValueType,
    TargetDbTypeType,
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
    "AccountQuotaTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "CertificateTypeDef",
    "ConnectionTypeDef",
    "CreateEndpointMessageRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "CreateReplicationInstanceMessageRequestTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "CreateReplicationSubnetGroupMessageRequestTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "CreateReplicationTaskMessageRequestTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DeleteCertificateMessageRequestTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DeleteConnectionMessageRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEndpointMessageRequestTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DeleteReplicationInstanceMessageRequestTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskMessageRequestTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "DescribeConnectionsMessageRequestTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "DescribeEndpointSettingsMessageRequestTypeDef",
    "DescribeEndpointSettingsResponseTypeDef",
    "DescribeEndpointTypesMessageRequestTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEndpointsMessageRequestTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationInstancesMessageRequestTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "DescribeReplicationTasksMessageRequestTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeSchemasMessageRequestTypeDef",
    "DescribeSchemasResponseTypeDef",
    "DescribeTableStatisticsMessageRequestTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EndpointSettingTypeDef",
    "EndpointTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "FilterTypeDef",
    "GcpMySQLSettingsTypeDef",
    "IBMDb2SettingsTypeDef",
    "ImportCertificateMessageRequestTypeDef",
    "ImportCertificateResponseTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "ModifyEndpointMessageRequestTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "ModifyReplicationInstanceMessageRequestTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "ModifyReplicationSubnetGroupMessageRequestTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ModifyReplicationTaskMessageRequestTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MongoDbSettingsTypeDef",
    "MoveReplicationTaskMessageRequestTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "MySQLSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleSettingsTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "RebootReplicationInstanceMessageRequestTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "RedisSettingsTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasMessageRequestTypeDef",
    "RefreshSchemasResponseTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReloadTablesMessageRequestTypeDef",
    "ReloadTablesResponseTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3SettingsTypeDef",
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskAssessmentRunMessageRequestTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "StartReplicationTaskMessageRequestTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopReplicationTaskMessageRequestTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TableToReloadTypeDef",
    "TagTypeDef",
    "TestConnectionMessageRequestTypeDef",
    "TestConnectionResponseTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": NotRequired[str],
        "Used": NotRequired[int],
        "Max": NotRequired[int],
    },
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResponseTypeDef",
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

CancelReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

CancelReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "CertificateCreationDate": NotRequired[datetime],
        "CertificatePem": NotRequired[str],
        "CertificateWallet": NotRequired[bytes],
        "CertificateArn": NotRequired[str],
        "CertificateOwner": NotRequired[str],
        "ValidFromDate": NotRequired[datetime],
        "ValidToDate": NotRequired[datetime],
        "SigningAlgorithm": NotRequired[str],
        "KeyLength": NotRequired[int],
    },
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ReplicationInstanceArn": NotRequired[str],
        "EndpointArn": NotRequired[str],
        "Status": NotRequired[str],
        "LastFailureMessage": NotRequired[str],
        "EndpointIdentifier": NotRequired[str],
        "ReplicationInstanceIdentifier": NotRequired[str],
    },
)

CreateEndpointMessageRequestTypeDef = TypedDict(
    "CreateEndpointMessageRequestTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "CertificateArn": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "DynamoDbSettings": NotRequired["DynamoDbSettingsTypeDef"],
        "S3Settings": NotRequired["S3SettingsTypeDef"],
        "DmsTransferSettings": NotRequired["DmsTransferSettingsTypeDef"],
        "MongoDbSettings": NotRequired["MongoDbSettingsTypeDef"],
        "KinesisSettings": NotRequired["KinesisSettingsTypeDef"],
        "KafkaSettings": NotRequired["KafkaSettingsTypeDef"],
        "ElasticsearchSettings": NotRequired["ElasticsearchSettingsTypeDef"],
        "NeptuneSettings": NotRequired["NeptuneSettingsTypeDef"],
        "RedshiftSettings": NotRequired["RedshiftSettingsTypeDef"],
        "PostgreSQLSettings": NotRequired["PostgreSQLSettingsTypeDef"],
        "MySQLSettings": NotRequired["MySQLSettingsTypeDef"],
        "OracleSettings": NotRequired["OracleSettingsTypeDef"],
        "SybaseSettings": NotRequired["SybaseSettingsTypeDef"],
        "MicrosoftSQLServerSettings": NotRequired["MicrosoftSQLServerSettingsTypeDef"],
        "IBMDb2Settings": NotRequired["IBMDb2SettingsTypeDef"],
        "ResourceIdentifier": NotRequired[str],
        "DocDbSettings": NotRequired["DocDbSettingsTypeDef"],
        "RedisSettings": NotRequired["RedisSettingsTypeDef"],
        "GcpMySQLSettings": NotRequired["GcpMySQLSettingsTypeDef"],
    },
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
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

CreateEventSubscriptionResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicationInstanceMessageRequestTypeDef = TypedDict(
    "CreateReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "AllocatedStorage": NotRequired[int],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
        "ReplicationSubnetGroupIdentifier": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
        "PubliclyAccessible": NotRequired[bool],
        "DnsNameServers": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
    },
)

CreateReplicationInstanceResponseTypeDef = TypedDict(
    "CreateReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "CreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicationTaskMessageRequestTypeDef = TypedDict(
    "CreateReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": NotRequired[str],
        "CdcStartTime": NotRequired[Union[datetime, str]],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "TaskData": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
    },
)

CreateReplicationTaskResponseTypeDef = TypedDict(
    "CreateReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCertificateMessageRequestTypeDef = TypedDict(
    "DeleteCertificateMessageRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DeleteCertificateResponseTypeDef = TypedDict(
    "DeleteCertificateResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionMessageRequestTypeDef = TypedDict(
    "DeleteConnectionMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointMessageRequestTypeDef = TypedDict(
    "DeleteEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationInstanceMessageRequestTypeDef = TypedDict(
    "DeleteReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)

DeleteReplicationInstanceResponseTypeDef = TypedDict(
    "DeleteReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
    },
)

DeleteReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

DeleteReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationTaskMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

DeleteReplicationTaskResponseTypeDef = TypedDict(
    "DeleteReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "UniqueAccountIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicableIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "SourceEngineName": NotRequired[str],
        "TargetEngineName": NotRequired[str],
        "MigrationType": NotRequired[MigrationTypeValueType],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeApplicableIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    {
        "IndividualAssessmentNames": List[str],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeCertificatesResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseTypeDef",
    {
        "Marker": str,
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionsMessageRequestTypeDef = TypedDict(
    "DescribeConnectionsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeConnectionsResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseTypeDef",
    {
        "Marker": str,
        "Connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointSettingsMessageRequestTypeDef = TypedDict(
    "DescribeEndpointSettingsMessageRequestTypeDef",
    {
        "EngineName": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEndpointSettingsResponseTypeDef = TypedDict(
    "DescribeEndpointSettingsResponseTypeDef",
    {
        "Marker": str,
        "EndpointSettings": List["EndpointSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointTypesMessageRequestTypeDef = TypedDict(
    "DescribeEndpointTypesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEndpointTypesResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List["SupportedEndpointTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeEndpointsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Marker": str,
        "Endpoints": List["EndpointTypeDef"],
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

DescribeEventCategoriesResponseTypeDef = TypedDict(
    "DescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List["EventCategoryGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[Literal["replication-instance"]],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Duration": NotRequired[int],
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrderableReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    {
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List["OrderableReplicationInstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)

DescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRefreshSchemasStatusMessageRequestTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationInstanceTaskLogsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List["ReplicationInstanceTaskLogTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List["ReplicationInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List["ReplicationSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List["ReplicationTaskAssessmentResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReplicationTaskAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskAssessmentRuns": List["ReplicationTaskAssessmentRunTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeReplicationTaskIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskIndividualAssessments": List["ReplicationTaskIndividualAssessmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTasksMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTasksMessageRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WithoutSettings": NotRequired[bool],
    },
)

DescribeReplicationTasksResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List["ReplicationTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchemasMessageRequestTypeDef = TypedDict(
    "DescribeSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeSchemasResponseTypeDef = TypedDict(
    "DescribeSchemasResponseTypeDef",
    {
        "Marker": str,
        "Schemas": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableStatisticsMessageRequestTypeDef = TypedDict(
    "DescribeTableStatisticsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

DescribeTableStatisticsResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List["TableStatisticsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef",
    {
        "ServiceAccessRoleArn": NotRequired[str],
        "BucketName": NotRequired[str],
    },
)

DocDbSettingsTypeDef = TypedDict(
    "DocDbSettingsTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "NestingLevel": NotRequired[NestingLevelValueType],
        "ExtractDocId": NotRequired[bool],
        "DocsToInvestigate": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

DynamoDbSettingsTypeDef = TypedDict(
    "DynamoDbSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
    },
)

ElasticsearchSettingsTypeDef = TypedDict(
    "ElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
        "FullLoadErrorPercentage": NotRequired[int],
        "ErrorRetryDuration": NotRequired[int],
    },
)

EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[EndpointSettingTypeValueType],
        "EnumValues": NotRequired[List[str]],
        "Sensitive": NotRequired[bool],
        "Units": NotRequired[str],
        "Applicability": NotRequired[str],
        "IntValueMin": NotRequired[int],
        "IntValueMax": NotRequired[int],
        "DefaultValue": NotRequired[str],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": NotRequired[str],
        "EndpointType": NotRequired[ReplicationEndpointTypeValueType],
        "EngineName": NotRequired[str],
        "EngineDisplayName": NotRequired[str],
        "Username": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "Status": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "EndpointArn": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "ExternalId": NotRequired[str],
        "DynamoDbSettings": NotRequired["DynamoDbSettingsTypeDef"],
        "S3Settings": NotRequired["S3SettingsTypeDef"],
        "DmsTransferSettings": NotRequired["DmsTransferSettingsTypeDef"],
        "MongoDbSettings": NotRequired["MongoDbSettingsTypeDef"],
        "KinesisSettings": NotRequired["KinesisSettingsTypeDef"],
        "KafkaSettings": NotRequired["KafkaSettingsTypeDef"],
        "ElasticsearchSettings": NotRequired["ElasticsearchSettingsTypeDef"],
        "NeptuneSettings": NotRequired["NeptuneSettingsTypeDef"],
        "RedshiftSettings": NotRequired["RedshiftSettingsTypeDef"],
        "PostgreSQLSettings": NotRequired["PostgreSQLSettingsTypeDef"],
        "MySQLSettings": NotRequired["MySQLSettingsTypeDef"],
        "OracleSettings": NotRequired["OracleSettingsTypeDef"],
        "SybaseSettings": NotRequired["SybaseSettingsTypeDef"],
        "MicrosoftSQLServerSettings": NotRequired["MicrosoftSQLServerSettingsTypeDef"],
        "IBMDb2Settings": NotRequired["IBMDb2SettingsTypeDef"],
        "DocDbSettings": NotRequired["DocDbSettingsTypeDef"],
        "RedisSettings": NotRequired["RedisSettingsTypeDef"],
        "GcpMySQLSettings": NotRequired["GcpMySQLSettingsTypeDef"],
    },
)

EventCategoryGroupTypeDef = TypedDict(
    "EventCategoryGroupTypeDef",
    {
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
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
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[Literal["replication-instance"]],
        "Message": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
        "Date": NotRequired[datetime],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)

GcpMySQLSettingsTypeDef = TypedDict(
    "GcpMySQLSettingsTypeDef",
    {
        "AfterConnectScript": NotRequired[str],
        "CleanSourceMetadataOnMismatch": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "EventsPollInterval": NotRequired[int],
        "TargetDbType": NotRequired[TargetDbTypeType],
        "MaxFileSize": NotRequired[int],
        "ParallelLoadThreads": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "ServerTimezone": NotRequired[str],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

IBMDb2SettingsTypeDef = TypedDict(
    "IBMDb2SettingsTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "SetDataCaptureChanges": NotRequired[bool],
        "CurrentLsn": NotRequired[str],
        "MaxKBytesPerRead": NotRequired[int],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

ImportCertificateMessageRequestTypeDef = TypedDict(
    "ImportCertificateMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificatePem": NotRequired[str],
        "CertificateWallet": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KafkaSettingsTypeDef = TypedDict(
    "KafkaSettingsTypeDef",
    {
        "Broker": NotRequired[str],
        "Topic": NotRequired[str],
        "MessageFormat": NotRequired[MessageFormatValueType],
        "IncludeTransactionDetails": NotRequired[bool],
        "IncludePartitionValue": NotRequired[bool],
        "PartitionIncludeSchemaTable": NotRequired[bool],
        "IncludeTableAlterOperations": NotRequired[bool],
        "IncludeControlDetails": NotRequired[bool],
        "MessageMaxBytes": NotRequired[int],
        "IncludeNullAndEmpty": NotRequired[bool],
        "SecurityProtocol": NotRequired[KafkaSecurityProtocolType],
        "SslClientCertificateArn": NotRequired[str],
        "SslClientKeyArn": NotRequired[str],
        "SslClientKeyPassword": NotRequired[str],
        "SslCaCertificateArn": NotRequired[str],
        "SaslUsername": NotRequired[str],
        "SaslPassword": NotRequired[str],
        "NoHexPrefix": NotRequired[bool],
    },
)

KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {
        "StreamArn": NotRequired[str],
        "MessageFormat": NotRequired[MessageFormatValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "IncludeTransactionDetails": NotRequired[bool],
        "IncludePartitionValue": NotRequired[bool],
        "PartitionIncludeSchemaTable": NotRequired[bool],
        "IncludeTableAlterOperations": NotRequired[bool],
        "IncludeControlDetails": NotRequired[bool],
        "IncludeNullAndEmpty": NotRequired[bool],
        "NoHexPrefix": NotRequired[bool],
    },
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceArnList": NotRequired[Sequence[str]],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MicrosoftSQLServerSettingsTypeDef = TypedDict(
    "MicrosoftSQLServerSettingsTypeDef",
    {
        "Port": NotRequired[int],
        "BcpPacketSize": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ControlTablesFileGroup": NotRequired[str],
        "Password": NotRequired[str],
        "QuerySingleAlwaysOnNode": NotRequired[bool],
        "ReadBackupOnly": NotRequired[bool],
        "SafeguardPolicy": NotRequired[SafeguardPolicyType],
        "ServerName": NotRequired[str],
        "Username": NotRequired[str],
        "UseBcpFullLoad": NotRequired[bool],
        "UseThirdPartyBackupDevice": NotRequired[bool],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

ModifyEndpointMessageRequestTypeDef = TypedDict(
    "ModifyEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "EndpointIdentifier": NotRequired[str],
        "EndpointType": NotRequired[ReplicationEndpointTypeValueType],
        "EngineName": NotRequired[str],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "ExtraConnectionAttributes": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "SslMode": NotRequired[DmsSslModeValueType],
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "DynamoDbSettings": NotRequired["DynamoDbSettingsTypeDef"],
        "S3Settings": NotRequired["S3SettingsTypeDef"],
        "DmsTransferSettings": NotRequired["DmsTransferSettingsTypeDef"],
        "MongoDbSettings": NotRequired["MongoDbSettingsTypeDef"],
        "KinesisSettings": NotRequired["KinesisSettingsTypeDef"],
        "KafkaSettings": NotRequired["KafkaSettingsTypeDef"],
        "ElasticsearchSettings": NotRequired["ElasticsearchSettingsTypeDef"],
        "NeptuneSettings": NotRequired["NeptuneSettingsTypeDef"],
        "RedshiftSettings": NotRequired["RedshiftSettingsTypeDef"],
        "PostgreSQLSettings": NotRequired["PostgreSQLSettingsTypeDef"],
        "MySQLSettings": NotRequired["MySQLSettingsTypeDef"],
        "OracleSettings": NotRequired["OracleSettingsTypeDef"],
        "SybaseSettings": NotRequired["SybaseSettingsTypeDef"],
        "MicrosoftSQLServerSettings": NotRequired["MicrosoftSQLServerSettingsTypeDef"],
        "IBMDb2Settings": NotRequired["IBMDb2SettingsTypeDef"],
        "DocDbSettings": NotRequired["DocDbSettingsTypeDef"],
        "RedisSettings": NotRequired["RedisSettingsTypeDef"],
        "ExactSettings": NotRequired[bool],
        "GcpMySQLSettings": NotRequired["GcpMySQLSettingsTypeDef"],
    },
)

ModifyEndpointResponseTypeDef = TypedDict(
    "ModifyEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
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

ModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReplicationInstanceMessageRequestTypeDef = TypedDict(
    "ModifyReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "AllocatedStorage": NotRequired[int],
        "ApplyImmediately": NotRequired[bool],
        "ReplicationInstanceClass": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "ReplicationInstanceIdentifier": NotRequired[str],
    },
)

ModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ModifyReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "SubnetIds": Sequence[str],
        "ReplicationSubnetGroupDescription": NotRequired[str],
    },
)

ModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReplicationTaskMessageRequestTypeDef = TypedDict(
    "ModifyReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ReplicationTaskIdentifier": NotRequired[str],
        "MigrationType": NotRequired[MigrationTypeValueType],
        "TableMappings": NotRequired[str],
        "ReplicationTaskSettings": NotRequired[str],
        "CdcStartTime": NotRequired[Union[datetime, str]],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "TaskData": NotRequired[str],
    },
)

ModifyReplicationTaskResponseTypeDef = TypedDict(
    "ModifyReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MongoDbSettingsTypeDef = TypedDict(
    "MongoDbSettingsTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ServerName": NotRequired[str],
        "Port": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "AuthType": NotRequired[AuthTypeValueType],
        "AuthMechanism": NotRequired[AuthMechanismValueType],
        "NestingLevel": NotRequired[NestingLevelValueType],
        "ExtractDocId": NotRequired[str],
        "DocsToInvestigate": NotRequired[str],
        "AuthSource": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

MoveReplicationTaskMessageRequestTypeDef = TypedDict(
    "MoveReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TargetReplicationInstanceArn": str,
    },
)

MoveReplicationTaskResponseTypeDef = TypedDict(
    "MoveReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MySQLSettingsTypeDef = TypedDict(
    "MySQLSettingsTypeDef",
    {
        "AfterConnectScript": NotRequired[str],
        "CleanSourceMetadataOnMismatch": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "EventsPollInterval": NotRequired[int],
        "TargetDbType": NotRequired[TargetDbTypeType],
        "MaxFileSize": NotRequired[int],
        "ParallelLoadThreads": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "ServerTimezone": NotRequired[str],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

NeptuneSettingsTypeDef = TypedDict(
    "NeptuneSettingsTypeDef",
    {
        "S3BucketName": str,
        "S3BucketFolder": str,
        "ServiceAccessRoleArn": NotRequired[str],
        "ErrorRetryDuration": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "MaxRetryCount": NotRequired[int],
        "IamAuthEnabled": NotRequired[bool],
    },
)

OracleSettingsTypeDef = TypedDict(
    "OracleSettingsTypeDef",
    {
        "AddSupplementalLogging": NotRequired[bool],
        "ArchivedLogDestId": NotRequired[int],
        "AdditionalArchivedLogDestId": NotRequired[int],
        "ExtraArchivedLogDestIds": NotRequired[Sequence[int]],
        "AllowSelectNestedTables": NotRequired[bool],
        "ParallelAsmReadThreads": NotRequired[int],
        "ReadAheadBlocks": NotRequired[int],
        "AccessAlternateDirectly": NotRequired[bool],
        "UseAlternateFolderForOnline": NotRequired[bool],
        "OraclePathPrefix": NotRequired[str],
        "UsePathPrefix": NotRequired[str],
        "ReplacePathPrefix": NotRequired[bool],
        "EnableHomogenousTablespace": NotRequired[bool],
        "DirectPathNoLog": NotRequired[bool],
        "ArchivedLogsOnly": NotRequired[bool],
        "AsmPassword": NotRequired[str],
        "AsmServer": NotRequired[str],
        "AsmUser": NotRequired[str],
        "CharLengthSemantics": NotRequired[CharLengthSemanticsType],
        "DatabaseName": NotRequired[str],
        "DirectPathParallelLoad": NotRequired[bool],
        "FailTasksOnLobTruncation": NotRequired[bool],
        "NumberDatatypeScale": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ReadTableSpaceName": NotRequired[bool],
        "RetryInterval": NotRequired[int],
        "SecurityDbEncryption": NotRequired[str],
        "SecurityDbEncryptionName": NotRequired[str],
        "ServerName": NotRequired[str],
        "SpatialDataOptionToGeoJsonFunctionName": NotRequired[str],
        "StandbyDelayTime": NotRequired[int],
        "Username": NotRequired[str],
        "UseBFile": NotRequired[bool],
        "UseDirectPathFullLoad": NotRequired[bool],
        "UseLogminerReader": NotRequired[bool],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
        "SecretsManagerOracleAsmAccessRoleArn": NotRequired[str],
        "SecretsManagerOracleAsmSecretId": NotRequired[str],
    },
)

OrderableReplicationInstanceTypeDef = TypedDict(
    "OrderableReplicationInstanceTypeDef",
    {
        "EngineVersion": NotRequired[str],
        "ReplicationInstanceClass": NotRequired[str],
        "StorageType": NotRequired[str],
        "MinAllocatedStorage": NotRequired[int],
        "MaxAllocatedStorage": NotRequired[int],
        "DefaultAllocatedStorage": NotRequired[int],
        "IncludedAllocatedStorage": NotRequired[int],
        "AvailabilityZones": NotRequired[List[str]],
        "ReleaseStatus": NotRequired[Literal["beta"]],
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

PostgreSQLSettingsTypeDef = TypedDict(
    "PostgreSQLSettingsTypeDef",
    {
        "AfterConnectScript": NotRequired[str],
        "CaptureDdls": NotRequired[bool],
        "MaxFileSize": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "DdlArtifactsSchema": NotRequired[str],
        "ExecuteTimeout": NotRequired[int],
        "FailTasksOnLobTruncation": NotRequired[bool],
        "HeartbeatEnable": NotRequired[bool],
        "HeartbeatSchema": NotRequired[str],
        "HeartbeatFrequency": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "Username": NotRequired[str],
        "SlotName": NotRequired[str],
        "PluginName": NotRequired[PluginNameValueType],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

RebootReplicationInstanceMessageRequestTypeDef = TypedDict(
    "RebootReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ForceFailover": NotRequired[bool],
        "ForcePlannedFailover": NotRequired[bool],
    },
)

RebootReplicationInstanceResponseTypeDef = TypedDict(
    "RebootReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedisSettingsTypeDef = TypedDict(
    "RedisSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "SslSecurityProtocol": NotRequired[SslSecurityProtocolValueType],
        "AuthType": NotRequired[RedisAuthTypeValueType],
        "AuthUserName": NotRequired[str],
        "AuthPassword": NotRequired[str],
        "SslCaCertificateArn": NotRequired[str],
    },
)

RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": NotRequired[bool],
        "AfterConnectScript": NotRequired[str],
        "BucketFolder": NotRequired[str],
        "BucketName": NotRequired[str],
        "CaseSensitiveNames": NotRequired[bool],
        "CompUpdate": NotRequired[bool],
        "ConnectionTimeout": NotRequired[int],
        "DatabaseName": NotRequired[str],
        "DateFormat": NotRequired[str],
        "EmptyAsNull": NotRequired[bool],
        "EncryptionMode": NotRequired[EncryptionModeValueType],
        "ExplicitIds": NotRequired[bool],
        "FileTransferUploadStreams": NotRequired[int],
        "LoadTimeout": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "RemoveQuotes": NotRequired[bool],
        "ReplaceInvalidChars": NotRequired[str],
        "ReplaceChars": NotRequired[str],
        "ServerName": NotRequired[str],
        "ServiceAccessRoleArn": NotRequired[str],
        "ServerSideEncryptionKmsKeyId": NotRequired[str],
        "TimeFormat": NotRequired[str],
        "TrimBlanks": NotRequired[bool],
        "TruncateColumns": NotRequired[bool],
        "Username": NotRequired[str],
        "WriteBufferSize": NotRequired[int],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

RefreshSchemasMessageRequestTypeDef = TypedDict(
    "RefreshSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

RefreshSchemasResponseTypeDef = TypedDict(
    "RefreshSchemasResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RefreshSchemasStatusTypeDef = TypedDict(
    "RefreshSchemasStatusTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "Status": NotRequired[RefreshSchemasStatusTypeValueType],
        "LastRefreshDate": NotRequired[datetime],
        "LastFailureMessage": NotRequired[str],
    },
)

ReloadTablesMessageRequestTypeDef = TypedDict(
    "ReloadTablesMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TablesToReload": Sequence["TableToReloadTypeDef"],
        "ReloadOption": NotRequired[ReloadOptionValueType],
    },
)

ReloadTablesResponseTypeDef = TypedDict(
    "ReloadTablesResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

ReplicationInstanceTaskLogTypeDef = TypedDict(
    "ReplicationInstanceTaskLogTypeDef",
    {
        "ReplicationTaskName": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationInstanceTaskLogSize": NotRequired[int],
    },
)

ReplicationInstanceTypeDef = TypedDict(
    "ReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": NotRequired[str],
        "ReplicationInstanceClass": NotRequired[str],
        "ReplicationInstanceStatus": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "InstanceCreateTime": NotRequired[datetime],
        "VpcSecurityGroups": NotRequired[List["VpcSecurityGroupMembershipTypeDef"]],
        "AvailabilityZone": NotRequired[str],
        "ReplicationSubnetGroup": NotRequired["ReplicationSubnetGroupTypeDef"],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired["ReplicationPendingModifiedValuesTypeDef"],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "ReplicationInstancePublicIpAddress": NotRequired[str],
        "ReplicationInstancePrivateIpAddress": NotRequired[str],
        "ReplicationInstancePublicIpAddresses": NotRequired[List[str]],
        "ReplicationInstancePrivateIpAddresses": NotRequired[List[str]],
        "PubliclyAccessible": NotRequired[bool],
        "SecondaryAvailabilityZone": NotRequired[str],
        "FreeUntil": NotRequired[datetime],
        "DnsNameServers": NotRequired[str],
    },
)

ReplicationPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
    },
)

ReplicationSubnetGroupTypeDef = TypedDict(
    "ReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": NotRequired[str],
        "ReplicationSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List["SubnetTypeDef"]],
    },
)

ReplicationTaskAssessmentResultTypeDef = TypedDict(
    "ReplicationTaskAssessmentResultTypeDef",
    {
        "ReplicationTaskIdentifier": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationTaskLastAssessmentDate": NotRequired[datetime],
        "AssessmentStatus": NotRequired[str],
        "AssessmentResultsFile": NotRequired[str],
        "AssessmentResults": NotRequired[str],
        "S3ObjectUrl": NotRequired[str],
    },
)

ReplicationTaskAssessmentRunProgressTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunProgressTypeDef",
    {
        "IndividualAssessmentCount": NotRequired[int],
        "IndividualAssessmentCompletedCount": NotRequired[int],
    },
)

ReplicationTaskAssessmentRunTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "Status": NotRequired[str],
        "ReplicationTaskAssessmentRunCreationDate": NotRequired[datetime],
        "AssessmentProgress": NotRequired["ReplicationTaskAssessmentRunProgressTypeDef"],
        "LastFailureMessage": NotRequired[str],
        "ServiceAccessRoleArn": NotRequired[str],
        "ResultLocationBucket": NotRequired[str],
        "ResultLocationFolder": NotRequired[str],
        "ResultEncryptionMode": NotRequired[str],
        "ResultKmsKeyArn": NotRequired[str],
        "AssessmentRunName": NotRequired[str],
    },
)

ReplicationTaskIndividualAssessmentTypeDef = TypedDict(
    "ReplicationTaskIndividualAssessmentTypeDef",
    {
        "ReplicationTaskIndividualAssessmentArn": NotRequired[str],
        "ReplicationTaskAssessmentRunArn": NotRequired[str],
        "IndividualAssessmentName": NotRequired[str],
        "Status": NotRequired[str],
        "ReplicationTaskIndividualAssessmentStartDate": NotRequired[datetime],
    },
)

ReplicationTaskStatsTypeDef = TypedDict(
    "ReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": NotRequired[int],
        "ElapsedTimeMillis": NotRequired[int],
        "TablesLoaded": NotRequired[int],
        "TablesLoading": NotRequired[int],
        "TablesQueued": NotRequired[int],
        "TablesErrored": NotRequired[int],
        "FreshStartDate": NotRequired[datetime],
        "StartDate": NotRequired[datetime],
        "StopDate": NotRequired[datetime],
        "FullLoadStartDate": NotRequired[datetime],
        "FullLoadFinishDate": NotRequired[datetime],
    },
)

ReplicationTaskTypeDef = TypedDict(
    "ReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": NotRequired[str],
        "SourceEndpointArn": NotRequired[str],
        "TargetEndpointArn": NotRequired[str],
        "ReplicationInstanceArn": NotRequired[str],
        "MigrationType": NotRequired[MigrationTypeValueType],
        "TableMappings": NotRequired[str],
        "ReplicationTaskSettings": NotRequired[str],
        "Status": NotRequired[str],
        "LastFailureMessage": NotRequired[str],
        "StopReason": NotRequired[str],
        "ReplicationTaskCreationDate": NotRequired[datetime],
        "ReplicationTaskStartDate": NotRequired[datetime],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
        "RecoveryCheckpoint": NotRequired[str],
        "ReplicationTaskArn": NotRequired[str],
        "ReplicationTaskStats": NotRequired["ReplicationTaskStatsTypeDef"],
        "TaskData": NotRequired[str],
        "TargetReplicationInstanceArn": NotRequired[str],
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

S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": NotRequired[str],
        "ExternalTableDefinition": NotRequired[str],
        "CsvRowDelimiter": NotRequired[str],
        "CsvDelimiter": NotRequired[str],
        "BucketFolder": NotRequired[str],
        "BucketName": NotRequired[str],
        "CompressionType": NotRequired[CompressionTypeValueType],
        "EncryptionMode": NotRequired[EncryptionModeValueType],
        "ServerSideEncryptionKmsKeyId": NotRequired[str],
        "DataFormat": NotRequired[DataFormatValueType],
        "EncodingType": NotRequired[EncodingTypeValueType],
        "DictPageSizeLimit": NotRequired[int],
        "RowGroupLength": NotRequired[int],
        "DataPageSize": NotRequired[int],
        "ParquetVersion": NotRequired[ParquetVersionValueType],
        "EnableStatistics": NotRequired[bool],
        "IncludeOpForFullLoad": NotRequired[bool],
        "CdcInsertsOnly": NotRequired[bool],
        "TimestampColumnName": NotRequired[str],
        "ParquetTimestampInMillisecond": NotRequired[bool],
        "CdcInsertsAndUpdates": NotRequired[bool],
        "DatePartitionEnabled": NotRequired[bool],
        "DatePartitionSequence": NotRequired[DatePartitionSequenceValueType],
        "DatePartitionDelimiter": NotRequired[DatePartitionDelimiterValueType],
        "UseCsvNoSupValue": NotRequired[bool],
        "CsvNoSupValue": NotRequired[str],
        "PreserveTransactions": NotRequired[bool],
        "CdcPath": NotRequired[str],
        "UseTaskStartTimeForFullLoadTimestamp": NotRequired[bool],
        "CannedAclForObjects": NotRequired[CannedAclForObjectsValueType],
        "AddColumnName": NotRequired[bool],
        "CdcMaxBatchInterval": NotRequired[int],
        "CdcMinFileSize": NotRequired[int],
        "CsvNullValue": NotRequired[str],
        "IgnoreHeaderRows": NotRequired[int],
        "MaxFileSize": NotRequired[int],
        "Rfc4180": NotRequired[bool],
        "DatePartitionTimezone": NotRequired[str],
    },
)

StartReplicationTaskAssessmentMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "AssessmentRunName": str,
        "ResultLocationFolder": NotRequired[str],
        "ResultEncryptionMode": NotRequired[str],
        "ResultKmsKeyArn": NotRequired[str],
        "IncludeOnly": NotRequired[Sequence[str]],
        "Exclude": NotRequired[Sequence[str]],
    },
)

StartReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReplicationTaskMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "StartReplicationTaskType": StartReplicationTaskTypeValueType,
        "CdcStartTime": NotRequired[Union[datetime, str]],
        "CdcStartPosition": NotRequired[str],
        "CdcStopPosition": NotRequired[str],
    },
)

StartReplicationTaskResponseTypeDef = TypedDict(
    "StartReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopReplicationTaskMessageRequestTypeDef = TypedDict(
    "StopReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StopReplicationTaskResponseTypeDef = TypedDict(
    "StopReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
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

SupportedEndpointTypeTypeDef = TypedDict(
    "SupportedEndpointTypeTypeDef",
    {
        "EngineName": NotRequired[str],
        "SupportsCDC": NotRequired[bool],
        "EndpointType": NotRequired[ReplicationEndpointTypeValueType],
        "ReplicationInstanceEngineMinimumVersion": NotRequired[str],
        "EngineDisplayName": NotRequired[str],
    },
)

SybaseSettingsTypeDef = TypedDict(
    "SybaseSettingsTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "Password": NotRequired[str],
        "Port": NotRequired[int],
        "ServerName": NotRequired[str],
        "Username": NotRequired[str],
        "SecretsManagerAccessRoleArn": NotRequired[str],
        "SecretsManagerSecretId": NotRequired[str],
    },
)

TableStatisticsTypeDef = TypedDict(
    "TableStatisticsTypeDef",
    {
        "SchemaName": NotRequired[str],
        "TableName": NotRequired[str],
        "Inserts": NotRequired[int],
        "Deletes": NotRequired[int],
        "Updates": NotRequired[int],
        "Ddls": NotRequired[int],
        "FullLoadRows": NotRequired[int],
        "FullLoadCondtnlChkFailedRows": NotRequired[int],
        "FullLoadErrorRows": NotRequired[int],
        "FullLoadStartTime": NotRequired[datetime],
        "FullLoadEndTime": NotRequired[datetime],
        "FullLoadReloaded": NotRequired[bool],
        "LastUpdateTime": NotRequired[datetime],
        "TableState": NotRequired[str],
        "ValidationPendingRecords": NotRequired[int],
        "ValidationFailedRecords": NotRequired[int],
        "ValidationSuspendedRecords": NotRequired[int],
        "ValidationState": NotRequired[str],
        "ValidationStateDetails": NotRequired[str],
    },
)

TableToReloadTypeDef = TypedDict(
    "TableToReloadTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)

TestConnectionMessageRequestTypeDef = TypedDict(
    "TestConnectionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
    },
)

TestConnectionResponseTypeDef = TypedDict(
    "TestConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
