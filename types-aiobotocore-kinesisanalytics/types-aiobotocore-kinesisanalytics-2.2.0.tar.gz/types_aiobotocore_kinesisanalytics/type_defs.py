"""
Type annotations for kinesisanalytics service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalytics/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kinesisanalytics.type_defs import AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef

    data: AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import ApplicationStatusType, InputStartingPositionType, RecordFormatTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "AddApplicationInputRequestRequestTypeDef",
    "AddApplicationOutputRequestRequestTypeDef",
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationUpdateTypeDef",
    "CSVMappingParametersTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DeleteApplicationOutputRequestRequestTypeDef",
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaRequestRequestTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "InputConfigurationTypeDef",
    "InputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismTypeDef",
    "InputParallelismUpdateTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "InputSchemaUpdateTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "InputTypeDef",
    "InputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SourceSchemaTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
)

AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOption": "CloudWatchLoggingOptionTypeDef",
    },
)

AddApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfiguration": "InputProcessingConfigurationTypeDef",
    },
)

AddApplicationInputRequestRequestTypeDef = TypedDict(
    "AddApplicationInputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Input": "InputTypeDef",
    },
)

AddApplicationOutputRequestRequestTypeDef = TypedDict(
    "AddApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Output": "OutputTypeDef",
    },
)

AddApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceDataSource": "ReferenceDataSourceTypeDef",
    },
)

ApplicationDetailTypeDef = TypedDict(
    "ApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "ApplicationDescription": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "InputDescriptions": NotRequired[List["InputDescriptionTypeDef"]],
        "OutputDescriptions": NotRequired[List["OutputDescriptionTypeDef"]],
        "ReferenceDataSourceDescriptions": NotRequired[
            List["ReferenceDataSourceDescriptionTypeDef"]
        ],
        "CloudWatchLoggingOptionDescriptions": NotRequired[
            List["CloudWatchLoggingOptionDescriptionTypeDef"]
        ],
        "ApplicationCode": NotRequired[str],
    },
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
    },
)

ApplicationUpdateTypeDef = TypedDict(
    "ApplicationUpdateTypeDef",
    {
        "InputUpdates": NotRequired[Sequence["InputUpdateTypeDef"]],
        "ApplicationCodeUpdate": NotRequired[str],
        "OutputUpdates": NotRequired[Sequence["OutputUpdateTypeDef"]],
        "ReferenceDataSourceUpdates": NotRequired[Sequence["ReferenceDataSourceUpdateTypeDef"]],
        "CloudWatchLoggingOptionUpdates": NotRequired[
            Sequence["CloudWatchLoggingOptionUpdateTypeDef"]
        ],
    },
)

CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)

CloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
        "CloudWatchLoggingOptionId": NotRequired[str],
    },
)

CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
    },
)

CloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "CloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
        "LogStreamARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "ApplicationDescription": NotRequired[str],
        "Inputs": NotRequired[Sequence["InputTypeDef"]],
        "Outputs": NotRequired[Sequence["OutputTypeDef"]],
        "CloudWatchLoggingOptions": NotRequired[Sequence["CloudWatchLoggingOptionTypeDef"]],
        "ApplicationCode": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationSummary": "ApplicationSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOptionId": str,
    },
)

DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
    },
)

DeleteApplicationOutputRequestRequestTypeDef = TypedDict(
    "DeleteApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "OutputId": str,
    },
)

DeleteApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceId": str,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CreateTimestamp": Union[datetime, str],
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)

DiscoverInputSchemaRequestRequestTypeDef = TypedDict(
    "DiscoverInputSchemaRequestRequestTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "InputStartingPositionConfiguration": NotRequired[
            "InputStartingPositionConfigurationTypeDef"
        ],
        "S3Configuration": NotRequired["S3ConfigurationTypeDef"],
        "InputProcessingConfiguration": NotRequired["InputProcessingConfigurationTypeDef"],
    },
)

DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": "SourceSchemaTypeDef",
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "Id": str,
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
)

InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": NotRequired[str],
        "NamePrefix": NotRequired[str],
        "InAppStreamNames": NotRequired[List[str]],
        "InputProcessingConfigurationDescription": NotRequired[
            "InputProcessingConfigurationDescriptionTypeDef"
        ],
        "KinesisStreamsInputDescription": NotRequired["KinesisStreamsInputDescriptionTypeDef"],
        "KinesisFirehoseInputDescription": NotRequired["KinesisFirehoseInputDescriptionTypeDef"],
        "InputSchema": NotRequired["SourceSchemaTypeDef"],
        "InputParallelism": NotRequired["InputParallelismTypeDef"],
        "InputStartingPositionConfiguration": NotRequired[
            "InputStartingPositionConfigurationTypeDef"
        ],
    },
)

InputLambdaProcessorDescriptionTypeDef = TypedDict(
    "InputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": NotRequired[int],
    },
)

InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": NotRequired[int],
    },
)

InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": NotRequired["InputLambdaProcessorDescriptionTypeDef"],
    },
)

InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": "InputLambdaProcessorTypeDef",
    },
)

InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": "InputLambdaProcessorUpdateTypeDef",
    },
)

InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": NotRequired["RecordFormatTypeDef"],
        "RecordEncodingUpdate": NotRequired[str],
        "RecordColumnUpdates": NotRequired[Sequence["RecordColumnTypeDef"]],
    },
)

InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": NotRequired[InputStartingPositionType],
    },
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": "SourceSchemaTypeDef",
        "InputProcessingConfiguration": NotRequired["InputProcessingConfigurationTypeDef"],
        "KinesisStreamsInput": NotRequired["KinesisStreamsInputTypeDef"],
        "KinesisFirehoseInput": NotRequired["KinesisFirehoseInputTypeDef"],
        "InputParallelism": NotRequired["InputParallelismTypeDef"],
    },
)

InputUpdateTypeDef = TypedDict(
    "InputUpdateTypeDef",
    {
        "InputId": str,
        "NamePrefixUpdate": NotRequired[str],
        "InputProcessingConfigurationUpdate": NotRequired[
            "InputProcessingConfigurationUpdateTypeDef"
        ],
        "KinesisStreamsInputUpdate": NotRequired["KinesisStreamsInputUpdateTypeDef"],
        "KinesisFirehoseInputUpdate": NotRequired["KinesisFirehoseInputUpdateTypeDef"],
        "InputSchemaUpdate": NotRequired["InputSchemaUpdateTypeDef"],
        "InputParallelismUpdate": NotRequired["InputParallelismUpdateTypeDef"],
    },
)

JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)

KinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

KinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

KinesisStreamsInputDescriptionTypeDef = TypedDict(
    "KinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

KinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "KinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

LambdaOutputDescriptionTypeDef = TypedDict(
    "LambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)

LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "ExclusiveStartApplicationName": NotRequired[str],
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List["ApplicationSummaryTypeDef"],
        "HasMoreApplications": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": NotRequired["JSONMappingParametersTypeDef"],
        "CSVMappingParameters": NotRequired["CSVMappingParametersTypeDef"],
    },
)

OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": NotRequired[str],
        "Name": NotRequired[str],
        "KinesisStreamsOutputDescription": NotRequired["KinesisStreamsOutputDescriptionTypeDef"],
        "KinesisFirehoseOutputDescription": NotRequired["KinesisFirehoseOutputDescriptionTypeDef"],
        "LambdaOutputDescription": NotRequired["LambdaOutputDescriptionTypeDef"],
        "DestinationSchema": NotRequired["DestinationSchemaTypeDef"],
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": "DestinationSchemaTypeDef",
        "KinesisStreamsOutput": NotRequired["KinesisStreamsOutputTypeDef"],
        "KinesisFirehoseOutput": NotRequired["KinesisFirehoseOutputTypeDef"],
        "LambdaOutput": NotRequired["LambdaOutputTypeDef"],
    },
)

OutputUpdateTypeDef = TypedDict(
    "OutputUpdateTypeDef",
    {
        "OutputId": str,
        "NameUpdate": NotRequired[str],
        "KinesisStreamsOutputUpdate": NotRequired["KinesisStreamsOutputUpdateTypeDef"],
        "KinesisFirehoseOutputUpdate": NotRequired["KinesisFirehoseOutputUpdateTypeDef"],
        "LambdaOutputUpdate": NotRequired["LambdaOutputUpdateTypeDef"],
        "DestinationSchemaUpdate": NotRequired["DestinationSchemaTypeDef"],
    },
)

RecordColumnTypeDef = TypedDict(
    "RecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
        "Mapping": NotRequired[str],
    },
)

RecordFormatTypeDef = TypedDict(
    "RecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
        "MappingParameters": NotRequired["MappingParametersTypeDef"],
    },
)

ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "ReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": "S3ReferenceDataSourceDescriptionTypeDef",
        "ReferenceSchema": NotRequired["SourceSchemaTypeDef"],
    },
)

ReferenceDataSourceTypeDef = TypedDict(
    "ReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": "SourceSchemaTypeDef",
        "S3ReferenceDataSource": NotRequired["S3ReferenceDataSourceTypeDef"],
    },
)

ReferenceDataSourceUpdateTypeDef = TypedDict(
    "ReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
        "TableNameUpdate": NotRequired[str],
        "S3ReferenceDataSourceUpdate": NotRequired["S3ReferenceDataSourceUpdateTypeDef"],
        "ReferenceSchemaUpdate": NotRequired["SourceSchemaTypeDef"],
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

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "FileKey": str,
    },
)

S3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "S3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)

S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)

S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "FileKeyUpdate": NotRequired[str],
        "ReferenceRoleARNUpdate": NotRequired[str],
    },
)

SourceSchemaTypeDef = TypedDict(
    "SourceSchemaTypeDef",
    {
        "RecordFormat": "RecordFormatTypeDef",
        "RecordColumns": Sequence["RecordColumnTypeDef"],
        "RecordEncoding": NotRequired[str],
    },
)

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "InputConfigurations": Sequence["InputConfigurationTypeDef"],
    },
)

StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ApplicationUpdate": "ApplicationUpdateTypeDef",
    },
)
