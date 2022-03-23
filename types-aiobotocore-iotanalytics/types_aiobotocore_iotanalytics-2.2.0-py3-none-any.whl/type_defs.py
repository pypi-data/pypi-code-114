"""
Type annotations for iotanalytics service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_iotanalytics/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_iotanalytics.type_defs import AddAttributesActivityTypeDef

    data: AddAttributesActivityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ChannelStatusType,
    ComputeTypeType,
    DatasetActionTypeType,
    DatasetContentStateType,
    DatasetStatusType,
    DatastoreStatusType,
    FileFormatTypeType,
    ReprocessingStatusType,
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
    "AddAttributesActivityTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "CancelPipelineReprocessingRequestRequestTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "ChannelStatisticsTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ColumnTypeDef",
    "ContainerDatasetActionTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetContentRequestRequestTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "CreateDatastoreResponseTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionSummaryTypeDef",
    "DatasetActionTypeDef",
    "DatasetContentDeliveryDestinationTypeDef",
    "DatasetContentDeliveryRuleTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentSummaryTypeDef",
    "DatasetContentVersionValueTypeDef",
    "DatasetEntryTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTriggerTypeDef",
    "DatasetTypeDef",
    "DatastoreActivityTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    "DatastorePartitionTypeDef",
    "DatastorePartitionsTypeDef",
    "DatastoreStatisticsTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastoreSummaryTypeDef",
    "DatastoreTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteDatasetContentRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeDatastoreRequestRequestTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DescribePipelineResponseTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EstimatedResourceSizeTypeDef",
    "FileFormatConfigurationTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentRequestRequestTypeDef",
    "GetDatasetContentResponseTypeDef",
    "GlueConfigurationTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    "LambdaActivityTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "LateDataRuleTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDatasetContentsRequestRequestTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListDatastoresResponseTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityTypeDef",
    "MessageTypeDef",
    "OutputFileUriValueTypeDef",
    "PaginatorConfigTypeDef",
    "ParquetConfigurationTypeDef",
    "PartitionTypeDef",
    "PipelineActivityTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "QueryFilterTypeDef",
    "RemoveAttributesActivityTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResourceConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RunPipelineActivityRequestRequestTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SampleChannelDataRequestRequestTypeDef",
    "SampleChannelDataResponseTypeDef",
    "ScheduleTypeDef",
    "SchemaDefinitionTypeDef",
    "SelectAttributesActivityTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "StartPipelineReprocessingRequestRequestTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimestampPartitionTypeDef",
    "TriggeringDatasetTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatastoreRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "VariableTypeDef",
    "VersioningConfigurationTypeDef",
)

AddAttributesActivityTypeDef = TypedDict(
    "AddAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Mapping[str, str],
        "next": NotRequired[str],
    },
)

BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchPutMessageRequestRequestTypeDef = TypedDict(
    "BatchPutMessageRequestRequestTypeDef",
    {
        "channelName": str,
        "messages": Sequence["MessageTypeDef"],
    },
)

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "CancelPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
        "reprocessingId": str,
    },
)

ChannelActivityTypeDef = TypedDict(
    "ChannelActivityTypeDef",
    {
        "name": str,
        "channelName": str,
        "next": NotRequired[str],
    },
)

ChannelMessagesTypeDef = TypedDict(
    "ChannelMessagesTypeDef",
    {
        "s3Paths": NotRequired[Sequence[str]],
    },
)

ChannelStatisticsTypeDef = TypedDict(
    "ChannelStatisticsTypeDef",
    {
        "size": NotRequired["EstimatedResourceSizeTypeDef"],
    },
)

ChannelStorageSummaryTypeDef = TypedDict(
    "ChannelStorageSummaryTypeDef",
    {
        "serviceManagedS3": NotRequired[Dict[str, Any]],
        "customerManagedS3": NotRequired["CustomerManagedChannelS3StorageSummaryTypeDef"],
    },
)

ChannelStorageTypeDef = TypedDict(
    "ChannelStorageTypeDef",
    {
        "serviceManagedS3": NotRequired[Mapping[str, Any]],
        "customerManagedS3": NotRequired["CustomerManagedChannelS3StorageTypeDef"],
    },
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "channelName": NotRequired[str],
        "channelStorage": NotRequired["ChannelStorageSummaryTypeDef"],
        "status": NotRequired[ChannelStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "name": NotRequired[str],
        "storage": NotRequired["ChannelStorageTypeDef"],
        "arn": NotRequired[str],
        "status": NotRequired[ChannelStatusType],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
    },
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)

ContainerDatasetActionTypeDef = TypedDict(
    "ContainerDatasetActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": "ResourceConfigurationTypeDef",
        "variables": NotRequired[Sequence["VariableTypeDef"]],
    },
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "channelName": str,
        "channelStorage": NotRequired["ChannelStorageTypeDef"],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetContentRequestRequestTypeDef = TypedDict(
    "CreateDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
        "versionId": NotRequired[str],
    },
)

CreateDatasetContentResponseTypeDef = TypedDict(
    "CreateDatasetContentResponseTypeDef",
    {
        "versionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": Sequence["DatasetActionTypeDef"],
        "triggers": NotRequired[Sequence["DatasetTriggerTypeDef"]],
        "contentDeliveryRules": NotRequired[Sequence["DatasetContentDeliveryRuleTypeDef"]],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "versioningConfiguration": NotRequired["VersioningConfigurationTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "lateDataRules": NotRequired[Sequence["LateDataRuleTypeDef"]],
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatastoreRequestRequestTypeDef = TypedDict(
    "CreateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": NotRequired["DatastoreStorageTypeDef"],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "fileFormatConfiguration": NotRequired["FileFormatConfigurationTypeDef"],
        "datastorePartitions": NotRequired["DatastorePartitionsTypeDef"],
    },
)

CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePipelineRequestRequestTypeDef = TypedDict(
    "CreatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": Sequence["PipelineActivityTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)

CustomerManagedChannelS3StorageTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
        "keyPrefix": NotRequired[str],
    },
)

CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)

CustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
        "keyPrefix": NotRequired[str],
    },
)

DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {
        "actionName": NotRequired[str],
        "actionType": NotRequired[DatasetActionTypeType],
    },
)

DatasetActionTypeDef = TypedDict(
    "DatasetActionTypeDef",
    {
        "actionName": NotRequired[str],
        "queryAction": NotRequired["SqlQueryDatasetActionTypeDef"],
        "containerAction": NotRequired["ContainerDatasetActionTypeDef"],
    },
)

DatasetContentDeliveryDestinationTypeDef = TypedDict(
    "DatasetContentDeliveryDestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": NotRequired[
            "IotEventsDestinationConfigurationTypeDef"
        ],
        "s3DestinationConfiguration": NotRequired["S3DestinationConfigurationTypeDef"],
    },
)

DatasetContentDeliveryRuleTypeDef = TypedDict(
    "DatasetContentDeliveryRuleTypeDef",
    {
        "destination": "DatasetContentDeliveryDestinationTypeDef",
        "entryName": NotRequired[str],
    },
)

DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {
        "state": NotRequired[DatasetContentStateType],
        "reason": NotRequired[str],
    },
)

DatasetContentSummaryTypeDef = TypedDict(
    "DatasetContentSummaryTypeDef",
    {
        "version": NotRequired[str],
        "status": NotRequired["DatasetContentStatusTypeDef"],
        "creationTime": NotRequired[datetime],
        "scheduleTime": NotRequired[datetime],
        "completionTime": NotRequired[datetime],
    },
)

DatasetContentVersionValueTypeDef = TypedDict(
    "DatasetContentVersionValueTypeDef",
    {
        "datasetName": str,
    },
)

DatasetEntryTypeDef = TypedDict(
    "DatasetEntryTypeDef",
    {
        "entryName": NotRequired[str],
        "dataURI": NotRequired[str],
    },
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": NotRequired[str],
        "status": NotRequired[DatasetStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "triggers": NotRequired[List["DatasetTriggerTypeDef"]],
        "actions": NotRequired[List["DatasetActionSummaryTypeDef"]],
    },
)

DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {
        "schedule": NotRequired["ScheduleTypeDef"],
        "dataset": NotRequired["TriggeringDatasetTypeDef"],
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "actions": NotRequired[List["DatasetActionTypeDef"]],
        "triggers": NotRequired[List["DatasetTriggerTypeDef"]],
        "contentDeliveryRules": NotRequired[List["DatasetContentDeliveryRuleTypeDef"]],
        "status": NotRequired[DatasetStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "versioningConfiguration": NotRequired["VersioningConfigurationTypeDef"],
        "lateDataRules": NotRequired[List["LateDataRuleTypeDef"]],
    },
)

DatastoreActivityTypeDef = TypedDict(
    "DatastoreActivityTypeDef",
    {
        "name": str,
        "datastoreName": str,
    },
)

DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    {
        "customerManagedS3Storage": NotRequired[
            "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef"
        ],
    },
)

DatastoreIotSiteWiseMultiLayerStorageTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    },
)

DatastorePartitionTypeDef = TypedDict(
    "DatastorePartitionTypeDef",
    {
        "attributePartition": NotRequired["PartitionTypeDef"],
        "timestampPartition": NotRequired["TimestampPartitionTypeDef"],
    },
)

DatastorePartitionsTypeDef = TypedDict(
    "DatastorePartitionsTypeDef",
    {
        "partitions": NotRequired[Sequence["DatastorePartitionTypeDef"]],
    },
)

DatastoreStatisticsTypeDef = TypedDict(
    "DatastoreStatisticsTypeDef",
    {
        "size": NotRequired["EstimatedResourceSizeTypeDef"],
    },
)

DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": NotRequired[Dict[str, Any]],
        "customerManagedS3": NotRequired["CustomerManagedDatastoreS3StorageSummaryTypeDef"],
        "iotSiteWiseMultiLayerStorage": NotRequired[
            "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef"
        ],
    },
)

DatastoreStorageTypeDef = TypedDict(
    "DatastoreStorageTypeDef",
    {
        "serviceManagedS3": NotRequired[Mapping[str, Any]],
        "customerManagedS3": NotRequired["CustomerManagedDatastoreS3StorageTypeDef"],
        "iotSiteWiseMultiLayerStorage": NotRequired["DatastoreIotSiteWiseMultiLayerStorageTypeDef"],
    },
)

DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": NotRequired[str],
        "datastoreStorage": NotRequired["DatastoreStorageSummaryTypeDef"],
        "status": NotRequired[DatastoreStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
        "fileFormatType": NotRequired[FileFormatTypeType],
        "datastorePartitions": NotRequired["DatastorePartitionsTypeDef"],
    },
)

DatastoreTypeDef = TypedDict(
    "DatastoreTypeDef",
    {
        "name": NotRequired[str],
        "storage": NotRequired["DatastoreStorageTypeDef"],
        "arn": NotRequired[str],
        "status": NotRequired[DatastoreStatusType],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
        "fileFormatConfiguration": NotRequired["FileFormatConfigurationTypeDef"],
        "datastorePartitions": NotRequired["DatastorePartitionsTypeDef"],
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)

DeleteDatasetContentRequestRequestTypeDef = TypedDict(
    "DeleteDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
        "versionId": NotRequired[str],
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)

DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DeltaTimeSessionWindowConfigurationTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationTypeDef",
    {
        "timeoutInMinutes": int,
    },
)

DeltaTimeTypeDef = TypedDict(
    "DeltaTimeTypeDef",
    {
        "offsetSeconds": int,
        "timeExpression": str,
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "channelName": str,
        "includeStatistics": NotRequired[bool],
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "statistics": "ChannelStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "includeStatistics": NotRequired[bool],
    },
)

DescribeDatastoreResponseTypeDef = TypedDict(
    "DescribeDatastoreResponseTypeDef",
    {
        "datastore": "DatastoreTypeDef",
        "statistics": "DatastoreStatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceRegistryEnrichActivityTypeDef = TypedDict(
    "DeviceRegistryEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
        "next": NotRequired[str],
    },
)

DeviceShadowEnrichActivityTypeDef = TypedDict(
    "DeviceShadowEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
        "next": NotRequired[str],
    },
)

EstimatedResourceSizeTypeDef = TypedDict(
    "EstimatedResourceSizeTypeDef",
    {
        "estimatedSizeInBytes": NotRequired[float],
        "estimatedOn": NotRequired[datetime],
    },
)

FileFormatConfigurationTypeDef = TypedDict(
    "FileFormatConfigurationTypeDef",
    {
        "jsonConfiguration": NotRequired[Mapping[str, Any]],
        "parquetConfiguration": NotRequired["ParquetConfigurationTypeDef"],
    },
)

FilterActivityTypeDef = TypedDict(
    "FilterActivityTypeDef",
    {
        "name": str,
        "filter": str,
        "next": NotRequired[str],
    },
)

GetDatasetContentRequestRequestTypeDef = TypedDict(
    "GetDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
        "versionId": NotRequired[str],
    },
)

GetDatasetContentResponseTypeDef = TypedDict(
    "GetDatasetContentResponseTypeDef",
    {
        "entries": List["DatasetEntryTypeDef"],
        "timestamp": datetime,
        "status": "DatasetContentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlueConfigurationTypeDef = TypedDict(
    "GlueConfigurationTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)

IotEventsDestinationConfigurationTypeDef = TypedDict(
    "IotEventsDestinationConfigurationTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)

IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
    },
)

IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "keyPrefix": NotRequired[str],
    },
)

LambdaActivityTypeDef = TypedDict(
    "LambdaActivityTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
        "next": NotRequired[str],
    },
)

LateDataRuleConfigurationTypeDef = TypedDict(
    "LateDataRuleConfigurationTypeDef",
    {
        "deltaTimeSessionWindowConfiguration": NotRequired[
            "DeltaTimeSessionWindowConfigurationTypeDef"
        ],
    },
)

LateDataRuleTypeDef = TypedDict(
    "LateDataRuleTypeDef",
    {
        "ruleConfiguration": "LateDataRuleConfigurationTypeDef",
        "ruleName": NotRequired[str],
    },
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "channelSummaries": List["ChannelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetContentsRequestRequestTypeDef = TypedDict(
    "ListDatasetContentsRequestRequestTypeDef",
    {
        "datasetName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "scheduledOnOrAfter": NotRequired[Union[datetime, str]],
        "scheduledBefore": NotRequired[Union[datetime, str]],
    },
)

ListDatasetContentsResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List["DatasetContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasetSummaries": List["DatasetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List["DatastoreSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List["PipelineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR"],
        "enabled": bool,
    },
)

MathActivityTypeDef = TypedDict(
    "MathActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
        "next": NotRequired[str],
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)

OutputFileUriValueTypeDef = TypedDict(
    "OutputFileUriValueTypeDef",
    {
        "fileName": str,
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

ParquetConfigurationTypeDef = TypedDict(
    "ParquetConfigurationTypeDef",
    {
        "schemaDefinition": NotRequired["SchemaDefinitionTypeDef"],
    },
)

PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "attributeName": str,
    },
)

PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": NotRequired["ChannelActivityTypeDef"],
        "lambda": NotRequired["LambdaActivityTypeDef"],
        "datastore": NotRequired["DatastoreActivityTypeDef"],
        "addAttributes": NotRequired["AddAttributesActivityTypeDef"],
        "removeAttributes": NotRequired["RemoveAttributesActivityTypeDef"],
        "selectAttributes": NotRequired["SelectAttributesActivityTypeDef"],
        "filter": NotRequired["FilterActivityTypeDef"],
        "math": NotRequired["MathActivityTypeDef"],
        "deviceRegistryEnrich": NotRequired["DeviceRegistryEnrichActivityTypeDef"],
        "deviceShadowEnrich": NotRequired["DeviceShadowEnrichActivityTypeDef"],
    },
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "pipelineName": NotRequired[str],
        "reprocessingSummaries": NotRequired[List["ReprocessingSummaryTypeDef"]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "activities": NotRequired[List["PipelineActivityTypeDef"]],
        "reprocessingSummaries": NotRequired[List["ReprocessingSummaryTypeDef"]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "deltaTime": NotRequired["DeltaTimeTypeDef"],
    },
)

RemoveAttributesActivityTypeDef = TypedDict(
    "RemoveAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
        "next": NotRequired[str],
    },
)

ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[ReprocessingStatusType],
        "creationTime": NotRequired[datetime],
    },
)

ResourceConfigurationTypeDef = TypedDict(
    "ResourceConfigurationTypeDef",
    {
        "computeType": ComputeTypeType,
        "volumeSizeInGB": int,
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "unlimited": NotRequired[bool],
        "numberOfDays": NotRequired[int],
    },
)

RunPipelineActivityRequestRequestTypeDef = TypedDict(
    "RunPipelineActivityRequestRequestTypeDef",
    {
        "pipelineActivity": "PipelineActivityTypeDef",
        "payloads": Sequence[Union[bytes, IO[bytes], StreamingBody]],
    },
)

RunPipelineActivityResponseTypeDef = TypedDict(
    "RunPipelineActivityResponseTypeDef",
    {
        "payloads": List[bytes],
        "logResult": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "roleArn": str,
        "glueConfiguration": NotRequired["GlueConfigurationTypeDef"],
    },
)

SampleChannelDataRequestRequestTypeDef = TypedDict(
    "SampleChannelDataRequestRequestTypeDef",
    {
        "channelName": str,
        "maxMessages": NotRequired[int],
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
    },
)

SampleChannelDataResponseTypeDef = TypedDict(
    "SampleChannelDataResponseTypeDef",
    {
        "payloads": List[bytes],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "expression": NotRequired[str],
    },
)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": NotRequired[Sequence["ColumnTypeDef"]],
    },
)

SelectAttributesActivityTypeDef = TypedDict(
    "SelectAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
        "next": NotRequired[str],
    },
)

SqlQueryDatasetActionTypeDef = TypedDict(
    "SqlQueryDatasetActionTypeDef",
    {
        "sqlQuery": str,
        "filters": NotRequired[Sequence["QueryFilterTypeDef"]],
    },
)

StartPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "StartPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
        "channelMessages": NotRequired["ChannelMessagesTypeDef"],
    },
)

StartPipelineReprocessingResponseTypeDef = TypedDict(
    "StartPipelineReprocessingResponseTypeDef",
    {
        "reprocessingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TimestampPartitionTypeDef = TypedDict(
    "TimestampPartitionTypeDef",
    {
        "attributeName": str,
        "timestampFormat": NotRequired[str],
    },
)

TriggeringDatasetTypeDef = TypedDict(
    "TriggeringDatasetTypeDef",
    {
        "name": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "channelName": str,
        "channelStorage": NotRequired["ChannelStorageTypeDef"],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
    },
)

UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": Sequence["DatasetActionTypeDef"],
        "triggers": NotRequired[Sequence["DatasetTriggerTypeDef"]],
        "contentDeliveryRules": NotRequired[Sequence["DatasetContentDeliveryRuleTypeDef"]],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "versioningConfiguration": NotRequired["VersioningConfigurationTypeDef"],
        "lateDataRules": NotRequired[Sequence["LateDataRuleTypeDef"]],
    },
)

UpdateDatastoreRequestRequestTypeDef = TypedDict(
    "UpdateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
        "datastoreStorage": NotRequired["DatastoreStorageTypeDef"],
        "fileFormatConfiguration": NotRequired["FileFormatConfigurationTypeDef"],
    },
)

UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": Sequence["PipelineActivityTypeDef"],
    },
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "stringValue": NotRequired[str],
        "doubleValue": NotRequired[float],
        "datasetContentVersionValue": NotRequired["DatasetContentVersionValueTypeDef"],
        "outputFileUriValue": NotRequired["OutputFileUriValueTypeDef"],
    },
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "unlimited": NotRequired[bool],
        "maxVersions": NotRequired[int],
    },
)
