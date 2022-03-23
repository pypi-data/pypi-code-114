"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ArchivalSummaryResponseMetadataTypeDef

    data: ArchivalSummaryResponseMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Mapping, Sequence, Set, Union

from boto3.dynamodb.conditions import ConditionBase
from typing_extensions import NotRequired

from .literals import (
    AttributeActionType,
    BackupStatusType,
    BackupTypeFilterType,
    BackupTypeType,
    BatchStatementErrorCodeEnumType,
    BillingModeType,
    ComparisonOperatorType,
    ConditionalOperatorType,
    ContinuousBackupsStatusType,
    ContributorInsightsActionType,
    ContributorInsightsStatusType,
    DestinationStatusType,
    ExportFormatType,
    ExportStatusType,
    GlobalTableStatusType,
    IndexStatusType,
    KeyTypeType,
    PointInTimeRecoveryStatusType,
    ProjectionTypeType,
    ReplicaStatusType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValuesOnConditionCheckFailureType,
    ReturnValueType,
    S3SseAlgorithmType,
    ScalarAttributeTypeType,
    SelectType,
    SSEStatusType,
    SSETypeType,
    StreamViewTypeType,
    TableClassType,
    TableStatusType,
    TimeToLiveStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArchivalSummaryResponseMetadataTypeDef",
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueUpdateTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDescriptionTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BatchExecuteStatementInputRequestTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "BatchGetItemInputRequestTypeDef",
    "BatchGetItemInputServiceResourceBatchGetItemTypeDef",
    "BatchGetItemOutputTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementRequestTypeDef",
    "BatchStatementResponseTypeDef",
    "BatchWriteItemInputRequestTypeDef",
    "BatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    "BatchWriteItemOutputTypeDef",
    "BillingModeSummaryResponseMetadataTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupInputRequestTypeDef",
    "CreateBackupOutputTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalTableInputRequestTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "CreateReplicaActionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "CreateTableInputRequestTypeDef",
    "CreateTableInputServiceResourceCreateTableTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteBackupInputRequestTypeDef",
    "DeleteBackupOutputTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteItemInputRequestTypeDef",
    "DeleteItemInputTableDeleteItemTypeDef",
    "DeleteItemOutputTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTableInputRequestTypeDef",
    "DeleteTableOutputTypeDef",
    "DeleteTypeDef",
    "DescribeBackupInputRequestTypeDef",
    "DescribeBackupOutputTypeDef",
    "DescribeContinuousBackupsInputRequestTypeDef",
    "DescribeContinuousBackupsOutputTypeDef",
    "DescribeContributorInsightsInputRequestTypeDef",
    "DescribeContributorInsightsOutputTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeExportInputRequestTypeDef",
    "DescribeExportOutputTypeDef",
    "DescribeGlobalTableInputRequestTypeDef",
    "DescribeGlobalTableOutputTypeDef",
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    "DescribeGlobalTableSettingsOutputTypeDef",
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeTableInputRequestTypeDef",
    "DescribeTableOutputTypeDef",
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    "DescribeTimeToLiveInputRequestTypeDef",
    "DescribeTimeToLiveOutputTypeDef",
    "EndpointTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionInputRequestTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "ExpectedAttributeValueTypeDef",
    "ExportDescriptionTypeDef",
    "ExportSummaryTypeDef",
    "ExportTableToPointInTimeInputRequestTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "FailureExceptionTypeDef",
    "GetItemInputRequestTypeDef",
    "GetItemInputTableGetItemTypeDef",
    "GetItemOutputTypeDef",
    "GetTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "GlobalTableDescriptionTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "GlobalTableTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeySchemaElementTypeDef",
    "KeysAndAttributesTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "KinesisStreamingDestinationInputRequestTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListBackupsInputRequestTypeDef",
    "ListBackupsOutputTypeDef",
    "ListContributorInsightsInputRequestTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListExportsOutputTypeDef",
    "ListGlobalTablesInputRequestTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ListTablesInputRequestTypeDef",
    "ListTablesOutputTypeDef",
    "ListTagsOfResourceInputRequestTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "LocalSecondaryIndexTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterizedStatementTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputDescriptionResponseMetadataTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "ProvisionedThroughputTypeDef",
    "PutItemInputRequestTypeDef",
    "PutItemInputTablePutItemTypeDef",
    "PutItemOutputTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "QueryInputRequestTypeDef",
    "QueryInputTableQueryTypeDef",
    "QueryOutputTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "ReplicaTypeDef",
    "ReplicaUpdateTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreSummaryResponseMetadataTypeDef",
    "RestoreSummaryTypeDef",
    "RestoreTableFromBackupInputRequestTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeInputRequestTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "SSEDescriptionResponseMetadataTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "ScanInputRequestTypeDef",
    "ScanInputTableScanTypeDef",
    "ScanOutputTypeDef",
    "ServiceResourceTableRequestTypeDef",
    "SourceTableDetailsTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "StreamSpecificationResponseMetadataTypeDef",
    "StreamSpecificationTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "TableBatchWriterRequestTypeDef",
    "TableClassSummaryResponseMetadataTypeDef",
    "TableClassSummaryTypeDef",
    "TableDescriptionTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "TransactGetItemTypeDef",
    "TransactGetItemsInputRequestTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemTypeDef",
    "TransactWriteItemsInputRequestTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateContinuousBackupsInputRequestTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "UpdateContributorInsightsInputRequestTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "UpdateGlobalTableInputRequestTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateItemInputRequestTypeDef",
    "UpdateItemInputTableUpdateItemTypeDef",
    "UpdateItemOutputTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateTableInputRequestTypeDef",
    "UpdateTableInputTableUpdateTypeDef",
    "UpdateTableOutputTypeDef",
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    "UpdateTimeToLiveInputRequestTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "UpdateTypeDef",
    "WaiterConfigTypeDef",
    "WriteRequestTypeDef",
)

ArchivalSummaryResponseMetadataTypeDef = TypedDict(
    "ArchivalSummaryResponseMetadataTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {
        "ArchivalDateTime": NotRequired[datetime],
        "ArchivalReason": NotRequired[str],
        "ArchivalBackupArn": NotRequired[str],
    },
)

AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": NotRequired[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
        "Action": NotRequired[AttributeActionType],
    },
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": NotRequired[str],
        "TargetTrackingScalingPolicyConfiguration": NotRequired[
            "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef"
        ],
    },
)

AutoScalingPolicyUpdateTypeDef = TypedDict(
    "AutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": (
            "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"
        ),
        "PolicyName": NotRequired[str],
    },
)

AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": NotRequired[int],
        "MaximumUnits": NotRequired[int],
        "AutoScalingDisabled": NotRequired[bool],
        "AutoScalingRoleArn": NotRequired[str],
        "ScalingPolicies": NotRequired[List["AutoScalingPolicyDescriptionTypeDef"]],
    },
)

AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": NotRequired[int],
        "MaximumUnits": NotRequired[int],
        "AutoScalingDisabled": NotRequired[bool],
        "AutoScalingRoleArn": NotRequired[str],
        "ScalingPolicyUpdate": NotRequired["AutoScalingPolicyUpdateTypeDef"],
    },
)

AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "TargetValue": float,
        "DisableScaleIn": NotRequired[bool],
        "ScaleInCooldown": NotRequired[int],
        "ScaleOutCooldown": NotRequired[int],
    },
)

AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "TargetValue": float,
        "DisableScaleIn": NotRequired[bool],
        "ScaleInCooldown": NotRequired[int],
        "ScaleOutCooldown": NotRequired[int],
    },
)

BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": NotRequired["BackupDetailsTypeDef"],
        "SourceTableDetails": NotRequired["SourceTableDetailsTypeDef"],
        "SourceTableFeatureDetails": NotRequired["SourceTableFeatureDetailsTypeDef"],
    },
)

BackupDetailsTypeDef = TypedDict(
    "BackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupCreationDateTime": datetime,
        "BackupSizeBytes": NotRequired[int],
        "BackupExpiryDateTime": NotRequired[datetime],
    },
)

BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": NotRequired[str],
        "TableId": NotRequired[str],
        "TableArn": NotRequired[str],
        "BackupArn": NotRequired[str],
        "BackupName": NotRequired[str],
        "BackupCreationDateTime": NotRequired[datetime],
        "BackupExpiryDateTime": NotRequired[datetime],
        "BackupStatus": NotRequired[BackupStatusType],
        "BackupType": NotRequired[BackupTypeType],
        "BackupSizeBytes": NotRequired[int],
    },
)

BatchExecuteStatementInputRequestTypeDef = TypedDict(
    "BatchExecuteStatementInputRequestTypeDef",
    {
        "Statements": Sequence["BatchStatementRequestTypeDef"],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)

BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "Responses": List["BatchStatementResponseTypeDef"],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetItemInputRequestTypeDef = TypedDict(
    "BatchGetItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, "KeysAndAttributesTypeDef"],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)

BatchGetItemInputServiceResourceBatchGetItemTypeDef = TypedDict(
    "BatchGetItemInputServiceResourceBatchGetItemTypeDef",
    {
        "RequestItems": Mapping[str, "KeysAndAttributesTypeDef"],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)

BatchGetItemOutputTypeDef = TypedDict(
    "BatchGetItemOutputTypeDef",
    {
        "Responses": Dict[
            str,
            List[
                Dict[
                    str,
                    Union[
                        bytes,
                        bytearray,
                        str,
                        int,
                        Decimal,
                        bool,
                        Set[int],
                        Set[Decimal],
                        Set[str],
                        Set[bytes],
                        Set[bytearray],
                        Sequence[Any],
                        Mapping[str, Any],
                        None,
                    ],
                ]
            ],
        ],
        "UnprocessedKeys": Dict[str, "KeysAndAttributesTypeDef"],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef",
    {
        "Code": NotRequired[BatchStatementErrorCodeEnumType],
        "Message": NotRequired[str],
    },
)

BatchStatementRequestTypeDef = TypedDict(
    "BatchStatementRequestTypeDef",
    {
        "Statement": str,
        "Parameters": NotRequired[
            Sequence[
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ]
            ]
        ],
        "ConsistentRead": NotRequired[bool],
    },
)

BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": NotRequired["BatchStatementErrorTypeDef"],
        "TableName": NotRequired[str],
        "Item": NotRequired[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

BatchWriteItemInputRequestTypeDef = TypedDict(
    "BatchWriteItemInputRequestTypeDef",
    {
        "RequestItems": Mapping[str, Sequence["WriteRequestTypeDef"]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
    },
)

BatchWriteItemInputServiceResourceBatchWriteItemTypeDef = TypedDict(
    "BatchWriteItemInputServiceResourceBatchWriteItemTypeDef",
    {
        "RequestItems": Mapping[str, Sequence["WriteRequestTypeDef"]],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
    },
)

BatchWriteItemOutputTypeDef = TypedDict(
    "BatchWriteItemOutputTypeDef",
    {
        "UnprocessedItems": Dict[str, List["WriteRequestTypeDef"]],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingModeSummaryResponseMetadataTypeDef = TypedDict(
    "BillingModeSummaryResponseMetadataTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {
        "BillingMode": NotRequired[BillingModeType],
        "LastUpdateToPayPerRequestDateTime": NotRequired[datetime],
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "ReadCapacityUnits": NotRequired[float],
        "WriteCapacityUnits": NotRequired[float],
        "CapacityUnits": NotRequired[float],
    },
)

ConditionCheckTypeDef = TypedDict(
    "ConditionCheckTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": NotRequired[
            Sequence[
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ]
            ]
        ],
    },
)

ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": NotRequired[str],
        "CapacityUnits": NotRequired[float],
        "ReadCapacityUnits": NotRequired[float],
        "WriteCapacityUnits": NotRequired[float],
        "Table": NotRequired["CapacityTypeDef"],
        "LocalSecondaryIndexes": NotRequired[Dict[str, "CapacityTypeDef"]],
        "GlobalSecondaryIndexes": NotRequired[Dict[str, "CapacityTypeDef"]],
    },
)

ContinuousBackupsDescriptionTypeDef = TypedDict(
    "ContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": ContinuousBackupsStatusType,
        "PointInTimeRecoveryDescription": NotRequired["PointInTimeRecoveryDescriptionTypeDef"],
    },
)

ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {
        "TableName": NotRequired[str],
        "IndexName": NotRequired[str],
        "ContributorInsightsStatus": NotRequired[ContributorInsightsStatusType],
    },
)

CreateBackupInputRequestTypeDef = TypedDict(
    "CreateBackupInputRequestTypeDef",
    {
        "TableName": str,
        "BackupName": str,
    },
)

CreateBackupOutputTypeDef = TypedDict(
    "CreateBackupOutputTypeDef",
    {
        "BackupDetails": "BackupDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "CreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
    },
)

CreateGlobalTableInputRequestTypeDef = TypedDict(
    "CreateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": Sequence["ReplicaTypeDef"],
    },
)

CreateGlobalTableOutputTypeDef = TypedDict(
    "CreateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicaActionTypeDef = TypedDict(
    "CreateReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

CreateReplicationGroupMemberActionTypeDef = TypedDict(
    "CreateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputOverrideTypeDef"],
        "GlobalSecondaryIndexes": NotRequired[Sequence["ReplicaGlobalSecondaryIndexTypeDef"]],
        "TableClassOverride": NotRequired[TableClassType],
    },
)

CreateTableInputRequestTypeDef = TypedDict(
    "CreateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": Sequence["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": Sequence["KeySchemaElementTypeDef"],
        "LocalSecondaryIndexes": NotRequired[Sequence["LocalSecondaryIndexTypeDef"]],
        "GlobalSecondaryIndexes": NotRequired[Sequence["GlobalSecondaryIndexTypeDef"]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
        "StreamSpecification": NotRequired["StreamSpecificationTypeDef"],
        "SSESpecification": NotRequired["SSESpecificationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "TableClass": NotRequired[TableClassType],
    },
)

CreateTableInputServiceResourceCreateTableTypeDef = TypedDict(
    "CreateTableInputServiceResourceCreateTableTypeDef",
    {
        "AttributeDefinitions": Sequence["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": Sequence["KeySchemaElementTypeDef"],
        "LocalSecondaryIndexes": NotRequired[Sequence["LocalSecondaryIndexTypeDef"]],
        "GlobalSecondaryIndexes": NotRequired[Sequence["GlobalSecondaryIndexTypeDef"]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
        "StreamSpecification": NotRequired["StreamSpecificationTypeDef"],
        "SSESpecification": NotRequired["SSESpecificationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "TableClass": NotRequired[TableClassType],
    },
)

CreateTableOutputTypeDef = TypedDict(
    "CreateTableOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupInputRequestTypeDef = TypedDict(
    "DeleteBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DeleteBackupOutputTypeDef = TypedDict(
    "DeleteBackupOutputTypeDef",
    {
        "BackupDescription": "BackupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
    },
)

DeleteItemInputRequestTypeDef = TypedDict(
    "DeleteItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "Expected": NotRequired[Mapping[str, "ExpectedAttributeValueTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

DeleteItemInputTableDeleteItemTypeDef = TypedDict(
    "DeleteItemInputTableDeleteItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "Expected": NotRequired[Mapping[str, "ExpectedAttributeValueTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

DeleteItemOutputTypeDef = TypedDict(
    "DeleteItemOutputTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicaActionTypeDef = TypedDict(
    "DeleteReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)

DeleteTableInputRequestTypeDef = TypedDict(
    "DeleteTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DeleteTableOutputTypeDef = TypedDict(
    "DeleteTableOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTypeDef = TypedDict(
    "DeleteTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)

DescribeBackupInputRequestTypeDef = TypedDict(
    "DescribeBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DescribeBackupOutputTypeDef = TypedDict(
    "DescribeBackupOutputTypeDef",
    {
        "BackupDescription": "BackupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousBackupsInputRequestTypeDef = TypedDict(
    "DescribeContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeContinuousBackupsOutputTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "DescribeContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
    },
)

DescribeContributorInsightsOutputTypeDef = TypedDict(
    "DescribeContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "LastUpdateDateTime": datetime,
        "FailureException": "FailureExceptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportInputRequestTypeDef = TypedDict(
    "DescribeExportInputRequestTypeDef",
    {
        "ExportArn": str,
    },
)

DescribeExportOutputTypeDef = TypedDict(
    "DescribeExportOutputTypeDef",
    {
        "ExportDescription": "ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableOutputTypeDef = TypedDict(
    "DescribeGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeKinesisStreamingDestinationOutputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List["KinesisDataStreamDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableInputRequestTypeDef = TypedDict(
    "DescribeTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTableOutputTypeDef = TypedDict(
    "DescribeTableOutputTypeDef",
    {
        "Table": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeToLiveInputRequestTypeDef = TypedDict(
    "DescribeTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTimeToLiveOutputTypeDef = TypedDict(
    "DescribeTimeToLiveOutputTypeDef",
    {
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

ExecuteStatementInputRequestTypeDef = TypedDict(
    "ExecuteStatementInputRequestTypeDef",
    {
        "Statement": str,
        "Parameters": NotRequired[
            Sequence[
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ]
            ]
        ],
        "ConsistentRead": NotRequired[bool],
        "NextToken": NotRequired[str],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "Limit": NotRequired[int],
    },
)

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "NextToken": str,
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteTransactionInputRequestTypeDef = TypedDict(
    "ExecuteTransactionInputRequestTypeDef",
    {
        "TransactStatements": Sequence["ParameterizedStatementTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)

ExecuteTransactionOutputTypeDef = TypedDict(
    "ExecuteTransactionOutputTypeDef",
    {
        "Responses": List["ItemResponseTypeDef"],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": NotRequired[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ]
        ],
        "Exists": NotRequired[bool],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "AttributeValueList": NotRequired[
            Sequence[
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ]
            ]
        ],
    },
)

ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": NotRequired[str],
        "ExportStatus": NotRequired[ExportStatusType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ExportManifest": NotRequired[str],
        "TableArn": NotRequired[str],
        "TableId": NotRequired[str],
        "ExportTime": NotRequired[datetime],
        "ClientToken": NotRequired[str],
        "S3Bucket": NotRequired[str],
        "S3BucketOwner": NotRequired[str],
        "S3Prefix": NotRequired[str],
        "S3SseAlgorithm": NotRequired[S3SseAlgorithmType],
        "S3SseKmsKeyId": NotRequired[str],
        "FailureCode": NotRequired[str],
        "FailureMessage": NotRequired[str],
        "ExportFormat": NotRequired[ExportFormatType],
        "BilledSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
    },
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportArn": NotRequired[str],
        "ExportStatus": NotRequired[ExportStatusType],
    },
)

ExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "ExportTableToPointInTimeInputRequestTypeDef",
    {
        "TableArn": str,
        "S3Bucket": str,
        "ExportTime": NotRequired[Union[datetime, str]],
        "ClientToken": NotRequired[str],
        "S3BucketOwner": NotRequired[str],
        "S3Prefix": NotRequired[str],
        "S3SseAlgorithm": NotRequired[S3SseAlgorithmType],
        "S3SseKmsKeyId": NotRequired[str],
        "ExportFormat": NotRequired[ExportFormatType],
    },
)

ExportTableToPointInTimeOutputTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputTypeDef",
    {
        "ExportDescription": "ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef",
    {
        "ExceptionName": NotRequired[str],
        "ExceptionDescription": NotRequired[str],
    },
)

GetItemInputRequestTypeDef = TypedDict(
    "GetItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)

GetItemInputTableGetItemTypeDef = TypedDict(
    "GetItemInputTableGetItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)

GetItemOutputTypeDef = TypedDict(
    "GetItemOutputTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypeDef = TypedDict(
    "GetTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)

GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedWriteCapacityAutoScalingUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
    },
)

GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List["KeySchemaElementTypeDef"]],
        "Projection": NotRequired["ProjectionTypeDef"],
        "IndexStatus": NotRequired[IndexStatusType],
        "Backfilling": NotRequired[bool],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputDescriptionTypeDef"],
        "IndexSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "IndexArn": NotRequired[str],
    },
)

GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List["KeySchemaElementTypeDef"]],
        "Projection": NotRequired["ProjectionTypeDef"],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
    },
)

GlobalSecondaryIndexTypeDef = TypedDict(
    "GlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
    },
)

GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": NotRequired["UpdateGlobalSecondaryIndexActionTypeDef"],
        "Create": NotRequired["CreateGlobalSecondaryIndexActionTypeDef"],
        "Delete": NotRequired["DeleteGlobalSecondaryIndexActionTypeDef"],
    },
)

GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": NotRequired[List["ReplicaDescriptionTypeDef"]],
        "GlobalTableArn": NotRequired[str],
        "CreationDateTime": NotRequired[datetime],
        "GlobalTableStatus": NotRequired[GlobalTableStatusType],
        "GlobalTableName": NotRequired[str],
    },
)

GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityUnits": NotRequired[int],
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
    },
)

GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {
        "GlobalTableName": NotRequired[str],
        "ReplicationGroup": NotRequired[List["ReplicaTypeDef"]],
    },
)

ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": NotRequired[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "SizeEstimateRangeGB": NotRequired[List[float]],
    },
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": NotRequired[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

KeysAndAttributesTypeDef = TypedDict(
    "KeysAndAttributesTypeDef",
    {
        "Keys": Sequence[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "AttributesToGet": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
        "ProjectionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
    },
)

KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {
        "StreamArn": NotRequired[str],
        "DestinationStatus": NotRequired[DestinationStatusType],
        "DestinationStatusDescription": NotRequired[str],
    },
)

KinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "KinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
    },
)

KinesisStreamingDestinationOutputTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupsInputRequestTypeDef = TypedDict(
    "ListBackupsInputRequestTypeDef",
    {
        "TableName": NotRequired[str],
        "Limit": NotRequired[int],
        "TimeRangeLowerBound": NotRequired[Union[datetime, str]],
        "TimeRangeUpperBound": NotRequired[Union[datetime, str]],
        "ExclusiveStartBackupArn": NotRequired[str],
        "BackupType": NotRequired[BackupTypeFilterType],
    },
)

ListBackupsOutputTypeDef = TypedDict(
    "ListBackupsOutputTypeDef",
    {
        "BackupSummaries": List["BackupSummaryTypeDef"],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContributorInsightsInputRequestTypeDef = TypedDict(
    "ListContributorInsightsInputRequestTypeDef",
    {
        "TableName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListContributorInsightsOutputTypeDef = TypedDict(
    "ListContributorInsightsOutputTypeDef",
    {
        "ContributorInsightsSummaries": List["ContributorInsightsSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "TableArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "ExportSummaries": List["ExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGlobalTablesInputRequestTypeDef = TypedDict(
    "ListGlobalTablesInputRequestTypeDef",
    {
        "ExclusiveStartGlobalTableName": NotRequired[str],
        "Limit": NotRequired[int],
        "RegionName": NotRequired[str],
    },
)

ListGlobalTablesOutputTypeDef = TypedDict(
    "ListGlobalTablesOutputTypeDef",
    {
        "GlobalTables": List["GlobalTableTypeDef"],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesInputRequestTypeDef = TypedDict(
    "ListTablesInputRequestTypeDef",
    {
        "ExclusiveStartTableName": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTablesOutputTypeDef = TypedDict(
    "ListTablesOutputTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsOfResourceInputRequestTypeDef = TypedDict(
    "ListTagsOfResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
    },
)

ListTagsOfResourceOutputTypeDef = TypedDict(
    "ListTagsOfResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List["KeySchemaElementTypeDef"]],
        "Projection": NotRequired["ProjectionTypeDef"],
        "IndexSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "IndexArn": NotRequired[str],
    },
)

LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": NotRequired[str],
        "KeySchema": NotRequired[List["KeySchemaElementTypeDef"]],
        "Projection": NotRequired["ProjectionTypeDef"],
    },
)

LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": Sequence["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
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

ParameterizedStatementTypeDef = TypedDict(
    "ParameterizedStatementTypeDef",
    {
        "Statement": str,
        "Parameters": NotRequired[
            Sequence[
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ]
            ]
        ],
    },
)

PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": NotRequired[PointInTimeRecoveryStatusType],
        "EarliestRestorableDateTime": NotRequired[datetime],
        "LatestRestorableDateTime": NotRequired[datetime],
    },
)

PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef",
    {
        "PointInTimeRecoveryEnabled": bool,
    },
)

ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {
        "ProjectionType": NotRequired[ProjectionTypeType],
        "NonKeyAttributes": NotRequired[Sequence[str]],
    },
)

ProvisionedThroughputDescriptionResponseMetadataTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionResponseMetadataTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": NotRequired[datetime],
        "LastDecreaseDateTime": NotRequired[datetime],
        "NumberOfDecreasesToday": NotRequired[int],
        "ReadCapacityUnits": NotRequired[int],
        "WriteCapacityUnits": NotRequired[int],
    },
)

ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": NotRequired[int],
    },
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

PutItemInputRequestTypeDef = TypedDict(
    "PutItemInputRequestTypeDef",
    {
        "TableName": str,
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "Expected": NotRequired[Mapping[str, "ExpectedAttributeValueTypeDef"]],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

PutItemInputTablePutItemTypeDef = TypedDict(
    "PutItemInputTablePutItemTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "Expected": NotRequired[Mapping[str, "ExpectedAttributeValueTypeDef"]],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

PutItemOutputTypeDef = TypedDict(
    "PutItemOutputTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
    },
)

PutTypeDef = TypedDict(
    "PutTypeDef",
    {
        "Item": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)

QueryInputRequestTypeDef = TypedDict(
    "QueryInputRequestTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
        "Select": NotRequired[SelectType],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "ConsistentRead": NotRequired[bool],
        "KeyConditions": NotRequired[Mapping[str, "ConditionTypeDef"]],
        "QueryFilter": NotRequired[Mapping[str, "ConditionTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ScanIndexForward": NotRequired[bool],
        "ExclusiveStartKey": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "KeyConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

QueryInputTableQueryTypeDef = TypedDict(
    "QueryInputTableQueryTypeDef",
    {
        "IndexName": NotRequired[str],
        "Select": NotRequired[SelectType],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "ConsistentRead": NotRequired[bool],
        "KeyConditions": NotRequired[Mapping[str, "ConditionTypeDef"]],
        "QueryFilter": NotRequired[Mapping[str, "ConditionTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ScanIndexForward": NotRequired[bool],
        "ExclusiveStartKey": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[Union[str, ConditionBase]],
        "KeyConditionExpression": NotRequired[Union[str, ConditionBase]],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": NotRequired[str],
        "GlobalSecondaryIndexes": NotRequired[
            List["ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"]
        ],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
        "ReplicaStatus": NotRequired[ReplicaStatusType],
    },
)

ReplicaAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaAutoScalingUpdateTypeDef",
    {
        "RegionName": str,
        "ReplicaGlobalSecondaryIndexUpdates": NotRequired[
            Sequence["ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"]
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
    },
)

ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": NotRequired[str],
        "ReplicaStatus": NotRequired[ReplicaStatusType],
        "ReplicaStatusDescription": NotRequired[str],
        "ReplicaStatusPercentProgress": NotRequired[str],
        "KMSMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputOverrideTypeDef"],
        "GlobalSecondaryIndexes": NotRequired[
            List["ReplicaGlobalSecondaryIndexDescriptionTypeDef"]
        ],
        "ReplicaInaccessibleDateTime": NotRequired[datetime],
        "ReplicaTableClassSummary": NotRequired["TableClassSummaryTypeDef"],
    },
)

ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "IndexStatus": NotRequired[IndexStatusType],
        "ProvisionedReadCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
        "ProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
    },
)

ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedReadCapacityAutoScalingUpdate": NotRequired["AutoScalingSettingsUpdateTypeDef"],
    },
)

ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputOverrideTypeDef"],
    },
)

ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": NotRequired[IndexStatusType],
        "ProvisionedReadCapacityUnits": NotRequired[int],
        "ProvisionedReadCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
        "ProvisionedWriteCapacityUnits": NotRequired[int],
        "ProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
    },
)

ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityUnits": NotRequired[int],
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
    },
)

ReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputOverrideTypeDef"],
    },
)

ReplicaSettingsDescriptionTypeDef = TypedDict(
    "ReplicaSettingsDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": NotRequired[ReplicaStatusType],
        "ReplicaBillingModeSummary": NotRequired["BillingModeSummaryTypeDef"],
        "ReplicaProvisionedReadCapacityUnits": NotRequired[int],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
        "ReplicaProvisionedWriteCapacityUnits": NotRequired[int],
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": NotRequired[
            "AutoScalingSettingsDescriptionTypeDef"
        ],
        "ReplicaGlobalSecondaryIndexSettings": NotRequired[
            List["ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"]
        ],
        "ReplicaTableClassSummary": NotRequired["TableClassSummaryTypeDef"],
    },
)

ReplicaSettingsUpdateTypeDef = TypedDict(
    "ReplicaSettingsUpdateTypeDef",
    {
        "RegionName": str,
        "ReplicaProvisionedReadCapacityUnits": NotRequired[int],
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
        "ReplicaGlobalSecondaryIndexSettingsUpdate": NotRequired[
            Sequence["ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"]
        ],
        "ReplicaTableClass": NotRequired[TableClassType],
    },
)

ReplicaTypeDef = TypedDict(
    "ReplicaTypeDef",
    {
        "RegionName": NotRequired[str],
    },
)

ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {
        "Create": NotRequired["CreateReplicaActionTypeDef"],
        "Delete": NotRequired["DeleteReplicaActionTypeDef"],
    },
)

ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": NotRequired["CreateReplicationGroupMemberActionTypeDef"],
        "Update": NotRequired["UpdateReplicationGroupMemberActionTypeDef"],
        "Delete": NotRequired["DeleteReplicationGroupMemberActionTypeDef"],
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

RestoreSummaryResponseMetadataTypeDef = TypedDict(
    "RestoreSummaryResponseMetadataTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreSummaryTypeDef = TypedDict(
    "RestoreSummaryTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
        "SourceBackupArn": NotRequired[str],
        "SourceTableArn": NotRequired[str],
    },
)

RestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "RestoreTableFromBackupInputRequestTypeDef",
    {
        "TargetTableName": str,
        "BackupArn": str,
        "BillingModeOverride": NotRequired[BillingModeType],
        "GlobalSecondaryIndexOverride": NotRequired[Sequence["GlobalSecondaryIndexTypeDef"]],
        "LocalSecondaryIndexOverride": NotRequired[Sequence["LocalSecondaryIndexTypeDef"]],
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputTypeDef"],
        "SSESpecificationOverride": NotRequired["SSESpecificationTypeDef"],
    },
)

RestoreTableFromBackupOutputTypeDef = TypedDict(
    "RestoreTableFromBackupOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "RestoreTableToPointInTimeInputRequestTypeDef",
    {
        "TargetTableName": str,
        "SourceTableArn": NotRequired[str],
        "SourceTableName": NotRequired[str],
        "UseLatestRestorableTime": NotRequired[bool],
        "RestoreDateTime": NotRequired[Union[datetime, str]],
        "BillingModeOverride": NotRequired[BillingModeType],
        "GlobalSecondaryIndexOverride": NotRequired[Sequence["GlobalSecondaryIndexTypeDef"]],
        "LocalSecondaryIndexOverride": NotRequired[Sequence["LocalSecondaryIndexTypeDef"]],
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputTypeDef"],
        "SSESpecificationOverride": NotRequired["SSESpecificationTypeDef"],
    },
)

RestoreTableToPointInTimeOutputTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SSEDescriptionResponseMetadataTypeDef = TypedDict(
    "SSEDescriptionResponseMetadataTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": NotRequired[SSEStatusType],
        "SSEType": NotRequired[SSETypeType],
        "KMSMasterKeyArn": NotRequired[str],
        "InaccessibleEncryptionDateTime": NotRequired[datetime],
    },
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "SSEType": NotRequired[SSETypeType],
        "KMSMasterKeyId": NotRequired[str],
    },
)

ScanInputRequestTypeDef = TypedDict(
    "ScanInputRequestTypeDef",
    {
        "TableName": str,
        "IndexName": NotRequired[str],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "Select": NotRequired[SelectType],
        "ScanFilter": NotRequired[Mapping[str, "ConditionTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ExclusiveStartKey": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "TotalSegments": NotRequired[int],
        "Segment": NotRequired[int],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ConsistentRead": NotRequired[bool],
    },
)

ScanInputTableScanTypeDef = TypedDict(
    "ScanInputTableScanTypeDef",
    {
        "IndexName": NotRequired[str],
        "AttributesToGet": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "Select": NotRequired[SelectType],
        "ScanFilter": NotRequired[Mapping[str, "ConditionTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ExclusiveStartKey": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "TotalSegments": NotRequired[int],
        "Segment": NotRequired[int],
        "ProjectionExpression": NotRequired[str],
        "FilterExpression": NotRequired[Union[str, ConditionBase]],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ConsistentRead": NotRequired[bool],
    },
)

ScanOutputTypeDef = TypedDict(
    "ScanOutputTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceResourceTableRequestTypeDef = TypedDict(
    "ServiceResourceTableRequestTypeDef",
    {
        "name": str,
    },
)

SourceTableDetailsTypeDef = TypedDict(
    "SourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "TableArn": NotRequired[str],
        "TableSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "BillingMode": NotRequired[BillingModeType],
    },
)

SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": NotRequired[List["LocalSecondaryIndexInfoTypeDef"]],
        "GlobalSecondaryIndexes": NotRequired[List["GlobalSecondaryIndexInfoTypeDef"]],
        "StreamDescription": NotRequired["StreamSpecificationTypeDef"],
        "TimeToLiveDescription": NotRequired["TimeToLiveDescriptionTypeDef"],
        "SSEDescription": NotRequired["SSEDescriptionTypeDef"],
    },
)

StreamSpecificationResponseMetadataTypeDef = TypedDict(
    "StreamSpecificationResponseMetadataTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": StreamViewTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StreamSpecificationTypeDef = TypedDict(
    "StreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
        "StreamViewType": NotRequired[StreamViewTypeType],
    },
)

TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": NotRequired[str],
        "TableStatus": NotRequired[TableStatusType],
        "Replicas": NotRequired[List["ReplicaAutoScalingDescriptionTypeDef"]],
    },
)

TableBatchWriterRequestTypeDef = TypedDict(
    "TableBatchWriterRequestTypeDef",
    {
        "overwrite_by_pkeys": NotRequired[List[str]],
    },
)

TableClassSummaryResponseMetadataTypeDef = TypedDict(
    "TableClassSummaryResponseMetadataTypeDef",
    {
        "TableClass": TableClassType,
        "LastUpdateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableClassSummaryTypeDef = TypedDict(
    "TableClassSummaryTypeDef",
    {
        "TableClass": NotRequired[TableClassType],
        "LastUpdateDateTime": NotRequired[datetime],
    },
)

TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": NotRequired[List["AttributeDefinitionTypeDef"]],
        "TableName": NotRequired[str],
        "KeySchema": NotRequired[List["KeySchemaElementTypeDef"]],
        "TableStatus": NotRequired[TableStatusType],
        "CreationDateTime": NotRequired[datetime],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputDescriptionTypeDef"],
        "TableSizeBytes": NotRequired[int],
        "ItemCount": NotRequired[int],
        "TableArn": NotRequired[str],
        "TableId": NotRequired[str],
        "BillingModeSummary": NotRequired["BillingModeSummaryTypeDef"],
        "LocalSecondaryIndexes": NotRequired[List["LocalSecondaryIndexDescriptionTypeDef"]],
        "GlobalSecondaryIndexes": NotRequired[List["GlobalSecondaryIndexDescriptionTypeDef"]],
        "StreamSpecification": NotRequired["StreamSpecificationTypeDef"],
        "LatestStreamLabel": NotRequired[str],
        "LatestStreamArn": NotRequired[str],
        "GlobalTableVersion": NotRequired[str],
        "Replicas": NotRequired[List["ReplicaDescriptionTypeDef"]],
        "RestoreSummary": NotRequired["RestoreSummaryTypeDef"],
        "SSEDescription": NotRequired["SSEDescriptionTypeDef"],
        "ArchivalSummary": NotRequired["ArchivalSummaryTypeDef"],
        "TableClassSummary": NotRequired["TableClassSummaryTypeDef"],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
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

TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": NotRequired[TimeToLiveStatusType],
        "AttributeName": NotRequired[str],
    },
)

TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)

TransactGetItemTypeDef = TypedDict(
    "TransactGetItemTypeDef",
    {
        "Get": "GetTypeDef",
    },
)

TransactGetItemsInputRequestTypeDef = TypedDict(
    "TransactGetItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence["TransactGetItemTypeDef"],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
    },
)

TransactGetItemsOutputTypeDef = TypedDict(
    "TransactGetItemsOutputTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "Responses": List["ItemResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": NotRequired["ConditionCheckTypeDef"],
        "Put": NotRequired["PutTypeDef"],
        "Delete": NotRequired["DeleteTypeDef"],
        "Update": NotRequired["UpdateTypeDef"],
    },
)

TransactWriteItemsInputRequestTypeDef = TypedDict(
    "TransactWriteItemsInputRequestTypeDef",
    {
        "TransactItems": Sequence["TransactWriteItemTypeDef"],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "ClientRequestToken": NotRequired[str],
    },
)

TransactWriteItemsOutputTypeDef = TypedDict(
    "TransactWriteItemsOutputTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateContinuousBackupsInputRequestTypeDef = TypedDict(
    "UpdateContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "PointInTimeRecoverySpecification": "PointInTimeRecoverySpecificationTypeDef",
    },
)

UpdateContinuousBackupsOutputTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "UpdateContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "ContributorInsightsAction": ContributorInsightsActionType,
        "IndexName": NotRequired[str],
    },
)

UpdateContributorInsightsOutputTypeDef = TypedDict(
    "UpdateContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
)

UpdateGlobalTableInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaUpdates": Sequence["ReplicaUpdateTypeDef"],
    },
)

UpdateGlobalTableOutputTypeDef = TypedDict(
    "UpdateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "GlobalTableBillingMode": NotRequired[BillingModeType],
        "GlobalTableProvisionedWriteCapacityUnits": NotRequired[int],
        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
        "GlobalTableGlobalSecondaryIndexSettingsUpdate": NotRequired[
            Sequence["GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef"]
        ],
        "ReplicaSettingsUpdate": NotRequired[Sequence["ReplicaSettingsUpdateTypeDef"]],
    },
)

UpdateGlobalTableSettingsOutputTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateItemInputRequestTypeDef = TypedDict(
    "UpdateItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "AttributeUpdates": NotRequired[Mapping[str, "AttributeValueUpdateTypeDef"]],
        "Expected": NotRequired[Mapping[str, "ExpectedAttributeValueTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "UpdateExpression": NotRequired[str],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

UpdateItemInputTableUpdateItemTypeDef = TypedDict(
    "UpdateItemInputTableUpdateItemTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "AttributeUpdates": NotRequired[Mapping[str, "AttributeValueUpdateTypeDef"]],
        "Expected": NotRequired[Mapping[str, "ExpectedAttributeValueTypeDef"]],
        "ConditionalOperator": NotRequired[ConditionalOperatorType],
        "ReturnValues": NotRequired[ReturnValueType],
        "ReturnConsumedCapacity": NotRequired[ReturnConsumedCapacityType],
        "ReturnItemCollectionMetrics": NotRequired[ReturnItemCollectionMetricsType],
        "UpdateExpression": NotRequired[str],
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
    },
)

UpdateItemOutputTypeDef = TypedDict(
    "UpdateItemOutputTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "UpdateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
        "KMSMasterKeyId": NotRequired[str],
        "ProvisionedThroughputOverride": NotRequired["ProvisionedThroughputOverrideTypeDef"],
        "GlobalSecondaryIndexes": NotRequired[Sequence["ReplicaGlobalSecondaryIndexTypeDef"]],
        "TableClassOverride": NotRequired[TableClassType],
    },
)

UpdateTableInputRequestTypeDef = TypedDict(
    "UpdateTableInputRequestTypeDef",
    {
        "TableName": str,
        "AttributeDefinitions": NotRequired[Sequence["AttributeDefinitionTypeDef"]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
        "GlobalSecondaryIndexUpdates": NotRequired[Sequence["GlobalSecondaryIndexUpdateTypeDef"]],
        "StreamSpecification": NotRequired["StreamSpecificationTypeDef"],
        "SSESpecification": NotRequired["SSESpecificationTypeDef"],
        "ReplicaUpdates": NotRequired[Sequence["ReplicationGroupUpdateTypeDef"]],
        "TableClass": NotRequired[TableClassType],
    },
)

UpdateTableInputTableUpdateTypeDef = TypedDict(
    "UpdateTableInputTableUpdateTypeDef",
    {
        "AttributeDefinitions": NotRequired[Sequence["AttributeDefinitionTypeDef"]],
        "BillingMode": NotRequired[BillingModeType],
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
        "GlobalSecondaryIndexUpdates": NotRequired[Sequence["GlobalSecondaryIndexUpdateTypeDef"]],
        "StreamSpecification": NotRequired["StreamSpecificationTypeDef"],
        "SSESpecification": NotRequired["SSESpecificationTypeDef"],
        "ReplicaUpdates": NotRequired[Sequence["ReplicationGroupUpdateTypeDef"]],
        "TableClass": NotRequired[TableClassType],
    },
)

UpdateTableOutputTypeDef = TypedDict(
    "UpdateTableOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
        "GlobalSecondaryIndexUpdates": NotRequired[
            Sequence["GlobalSecondaryIndexAutoScalingUpdateTypeDef"]
        ],
        "ProvisionedWriteCapacityAutoScalingUpdate": NotRequired[
            "AutoScalingSettingsUpdateTypeDef"
        ],
        "ReplicaUpdates": NotRequired[Sequence["ReplicaAutoScalingUpdateTypeDef"]],
    },
)

UpdateTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTimeToLiveInputRequestTypeDef = TypedDict(
    "UpdateTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
    },
)

UpdateTimeToLiveOutputTypeDef = TypedDict(
    "UpdateTimeToLiveOutputTypeDef",
    {
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "Key": Mapping[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                Sequence[Any],
                Mapping[str, Any],
                None,
            ],
        ],
        "UpdateExpression": str,
        "TableName": str,
        "ConditionExpression": NotRequired[str],
        "ExpressionAttributeNames": NotRequired[Mapping[str, str]],
        "ExpressionAttributeValues": NotRequired[
            Mapping[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    Sequence[Any],
                    Mapping[str, Any],
                    None,
                ],
            ]
        ],
        "ReturnValuesOnConditionCheckFailure": NotRequired[ReturnValuesOnConditionCheckFailureType],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {
        "PutRequest": NotRequired["PutRequestTypeDef"],
        "DeleteRequest": NotRequired["DeleteRequestTypeDef"],
    },
)
