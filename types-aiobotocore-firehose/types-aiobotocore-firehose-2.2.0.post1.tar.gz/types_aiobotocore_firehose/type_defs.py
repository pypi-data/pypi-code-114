"""
Type annotations for firehose service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_firehose/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_firehose.type_defs import AmazonopensearchserviceBufferingHintsTypeDef

    data: AmazonopensearchserviceBufferingHintsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AmazonopensearchserviceIndexRotationPeriodType,
    AmazonopensearchserviceS3BackupModeType,
    CompressionFormatType,
    ContentEncodingType,
    DeliveryStreamEncryptionStatusType,
    DeliveryStreamFailureTypeType,
    DeliveryStreamStatusType,
    DeliveryStreamTypeType,
    ElasticsearchIndexRotationPeriodType,
    ElasticsearchS3BackupModeType,
    HECEndpointTypeType,
    HttpEndpointS3BackupModeType,
    KeyTypeType,
    OrcCompressionType,
    OrcFormatVersionType,
    ParquetCompressionType,
    ParquetWriterVersionType,
    ProcessorParameterNameType,
    ProcessorTypeType,
    RedshiftS3BackupModeType,
    S3BackupModeType,
    SplunkS3BackupModeType,
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
    "AmazonopensearchserviceBufferingHintsTypeDef",
    "AmazonopensearchserviceDestinationConfigurationTypeDef",
    "AmazonopensearchserviceDestinationDescriptionTypeDef",
    "AmazonopensearchserviceDestinationUpdateTypeDef",
    "AmazonopensearchserviceRetryOptionsTypeDef",
    "BufferingHintsTypeDef",
    "CloudWatchLoggingOptionsTypeDef",
    "CopyCommandTypeDef",
    "CreateDeliveryStreamInputRequestTypeDef",
    "CreateDeliveryStreamOutputTypeDef",
    "DataFormatConversionConfigurationTypeDef",
    "DeleteDeliveryStreamInputRequestTypeDef",
    "DeliveryStreamDescriptionTypeDef",
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    "DeliveryStreamEncryptionConfigurationTypeDef",
    "DescribeDeliveryStreamInputRequestTypeDef",
    "DescribeDeliveryStreamOutputTypeDef",
    "DeserializerTypeDef",
    "DestinationDescriptionTypeDef",
    "DynamicPartitioningConfigurationTypeDef",
    "ElasticsearchBufferingHintsTypeDef",
    "ElasticsearchDestinationConfigurationTypeDef",
    "ElasticsearchDestinationDescriptionTypeDef",
    "ElasticsearchDestinationUpdateTypeDef",
    "ElasticsearchRetryOptionsTypeDef",
    "EncryptionConfigurationTypeDef",
    "ExtendedS3DestinationConfigurationTypeDef",
    "ExtendedS3DestinationDescriptionTypeDef",
    "ExtendedS3DestinationUpdateTypeDef",
    "FailureDescriptionTypeDef",
    "HiveJsonSerDeTypeDef",
    "HttpEndpointBufferingHintsTypeDef",
    "HttpEndpointCommonAttributeTypeDef",
    "HttpEndpointConfigurationTypeDef",
    "HttpEndpointDescriptionTypeDef",
    "HttpEndpointDestinationConfigurationTypeDef",
    "HttpEndpointDestinationDescriptionTypeDef",
    "HttpEndpointDestinationUpdateTypeDef",
    "HttpEndpointRequestConfigurationTypeDef",
    "HttpEndpointRetryOptionsTypeDef",
    "InputFormatConfigurationTypeDef",
    "KMSEncryptionConfigTypeDef",
    "KinesisStreamSourceConfigurationTypeDef",
    "KinesisStreamSourceDescriptionTypeDef",
    "ListDeliveryStreamsInputRequestTypeDef",
    "ListDeliveryStreamsOutputTypeDef",
    "ListTagsForDeliveryStreamInputRequestTypeDef",
    "ListTagsForDeliveryStreamOutputTypeDef",
    "OpenXJsonSerDeTypeDef",
    "OrcSerDeTypeDef",
    "OutputFormatConfigurationTypeDef",
    "ParquetSerDeTypeDef",
    "ProcessingConfigurationTypeDef",
    "ProcessorParameterTypeDef",
    "ProcessorTypeDef",
    "PutRecordBatchInputRequestTypeDef",
    "PutRecordBatchOutputTypeDef",
    "PutRecordBatchResponseEntryTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordOutputTypeDef",
    "RecordTypeDef",
    "RedshiftDestinationConfigurationTypeDef",
    "RedshiftDestinationDescriptionTypeDef",
    "RedshiftDestinationUpdateTypeDef",
    "RedshiftRetryOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "RetryOptionsTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DestinationDescriptionTypeDef",
    "S3DestinationUpdateTypeDef",
    "SchemaConfigurationTypeDef",
    "SerializerTypeDef",
    "SourceDescriptionTypeDef",
    "SplunkDestinationConfigurationTypeDef",
    "SplunkDestinationDescriptionTypeDef",
    "SplunkDestinationUpdateTypeDef",
    "SplunkRetryOptionsTypeDef",
    "StartDeliveryStreamEncryptionInputRequestTypeDef",
    "StopDeliveryStreamEncryptionInputRequestTypeDef",
    "TagDeliveryStreamInputRequestTypeDef",
    "TagTypeDef",
    "UntagDeliveryStreamInputRequestTypeDef",
    "UpdateDestinationInputRequestTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
)

AmazonopensearchserviceBufferingHintsTypeDef = TypedDict(
    "AmazonopensearchserviceBufferingHintsTypeDef",
    {
        "IntervalInSeconds": NotRequired[int],
        "SizeInMBs": NotRequired[int],
    },
)

AmazonopensearchserviceDestinationConfigurationTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
        "DomainARN": NotRequired[str],
        "ClusterEndpoint": NotRequired[str],
        "TypeName": NotRequired[str],
        "IndexRotationPeriod": NotRequired[AmazonopensearchserviceIndexRotationPeriodType],
        "BufferingHints": NotRequired["AmazonopensearchserviceBufferingHintsTypeDef"],
        "RetryOptions": NotRequired["AmazonopensearchserviceRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[AmazonopensearchserviceS3BackupModeType],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "VpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
    },
)

AmazonopensearchserviceDestinationDescriptionTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationDescriptionTypeDef",
    {
        "RoleARN": NotRequired[str],
        "DomainARN": NotRequired[str],
        "ClusterEndpoint": NotRequired[str],
        "IndexName": NotRequired[str],
        "TypeName": NotRequired[str],
        "IndexRotationPeriod": NotRequired[AmazonopensearchserviceIndexRotationPeriodType],
        "BufferingHints": NotRequired["AmazonopensearchserviceBufferingHintsTypeDef"],
        "RetryOptions": NotRequired["AmazonopensearchserviceRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[AmazonopensearchserviceS3BackupModeType],
        "S3DestinationDescription": NotRequired["S3DestinationDescriptionTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "VpcConfigurationDescription": NotRequired["VpcConfigurationDescriptionTypeDef"],
    },
)

AmazonopensearchserviceDestinationUpdateTypeDef = TypedDict(
    "AmazonopensearchserviceDestinationUpdateTypeDef",
    {
        "RoleARN": NotRequired[str],
        "DomainARN": NotRequired[str],
        "ClusterEndpoint": NotRequired[str],
        "IndexName": NotRequired[str],
        "TypeName": NotRequired[str],
        "IndexRotationPeriod": NotRequired[AmazonopensearchserviceIndexRotationPeriodType],
        "BufferingHints": NotRequired["AmazonopensearchserviceBufferingHintsTypeDef"],
        "RetryOptions": NotRequired["AmazonopensearchserviceRetryOptionsTypeDef"],
        "S3Update": NotRequired["S3DestinationUpdateTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

AmazonopensearchserviceRetryOptionsTypeDef = TypedDict(
    "AmazonopensearchserviceRetryOptionsTypeDef",
    {
        "DurationInSeconds": NotRequired[int],
    },
)

BufferingHintsTypeDef = TypedDict(
    "BufferingHintsTypeDef",
    {
        "SizeInMBs": NotRequired[int],
        "IntervalInSeconds": NotRequired[int],
    },
)

CloudWatchLoggingOptionsTypeDef = TypedDict(
    "CloudWatchLoggingOptionsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LogGroupName": NotRequired[str],
        "LogStreamName": NotRequired[str],
    },
)

CopyCommandTypeDef = TypedDict(
    "CopyCommandTypeDef",
    {
        "DataTableName": str,
        "DataTableColumns": NotRequired[str],
        "CopyOptions": NotRequired[str],
    },
)

CreateDeliveryStreamInputRequestTypeDef = TypedDict(
    "CreateDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamType": NotRequired[DeliveryStreamTypeType],
        "KinesisStreamSourceConfiguration": NotRequired["KinesisStreamSourceConfigurationTypeDef"],
        "DeliveryStreamEncryptionConfigurationInput": NotRequired[
            "DeliveryStreamEncryptionConfigurationInputTypeDef"
        ],
        "S3DestinationConfiguration": NotRequired["S3DestinationConfigurationTypeDef"],
        "ExtendedS3DestinationConfiguration": NotRequired[
            "ExtendedS3DestinationConfigurationTypeDef"
        ],
        "RedshiftDestinationConfiguration": NotRequired["RedshiftDestinationConfigurationTypeDef"],
        "ElasticsearchDestinationConfiguration": NotRequired[
            "ElasticsearchDestinationConfigurationTypeDef"
        ],
        "AmazonopensearchserviceDestinationConfiguration": NotRequired[
            "AmazonopensearchserviceDestinationConfigurationTypeDef"
        ],
        "SplunkDestinationConfiguration": NotRequired["SplunkDestinationConfigurationTypeDef"],
        "HttpEndpointDestinationConfiguration": NotRequired[
            "HttpEndpointDestinationConfigurationTypeDef"
        ],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDeliveryStreamOutputTypeDef = TypedDict(
    "CreateDeliveryStreamOutputTypeDef",
    {
        "DeliveryStreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataFormatConversionConfigurationTypeDef = TypedDict(
    "DataFormatConversionConfigurationTypeDef",
    {
        "SchemaConfiguration": NotRequired["SchemaConfigurationTypeDef"],
        "InputFormatConfiguration": NotRequired["InputFormatConfigurationTypeDef"],
        "OutputFormatConfiguration": NotRequired["OutputFormatConfigurationTypeDef"],
        "Enabled": NotRequired[bool],
    },
)

DeleteDeliveryStreamInputRequestTypeDef = TypedDict(
    "DeleteDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "AllowForceDelete": NotRequired[bool],
    },
)

DeliveryStreamDescriptionTypeDef = TypedDict(
    "DeliveryStreamDescriptionTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamARN": str,
        "DeliveryStreamStatus": DeliveryStreamStatusType,
        "DeliveryStreamType": DeliveryStreamTypeType,
        "VersionId": str,
        "Destinations": List["DestinationDescriptionTypeDef"],
        "HasMoreDestinations": bool,
        "FailureDescription": NotRequired["FailureDescriptionTypeDef"],
        "DeliveryStreamEncryptionConfiguration": NotRequired[
            "DeliveryStreamEncryptionConfigurationTypeDef"
        ],
        "CreateTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "Source": NotRequired["SourceDescriptionTypeDef"],
    },
)

DeliveryStreamEncryptionConfigurationInputTypeDef = TypedDict(
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    {
        "KeyType": KeyTypeType,
        "KeyARN": NotRequired[str],
    },
)

DeliveryStreamEncryptionConfigurationTypeDef = TypedDict(
    "DeliveryStreamEncryptionConfigurationTypeDef",
    {
        "KeyARN": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Status": NotRequired[DeliveryStreamEncryptionStatusType],
        "FailureDescription": NotRequired["FailureDescriptionTypeDef"],
    },
)

DescribeDeliveryStreamInputRequestTypeDef = TypedDict(
    "DescribeDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Limit": NotRequired[int],
        "ExclusiveStartDestinationId": NotRequired[str],
    },
)

DescribeDeliveryStreamOutputTypeDef = TypedDict(
    "DescribeDeliveryStreamOutputTypeDef",
    {
        "DeliveryStreamDescription": "DeliveryStreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeserializerTypeDef = TypedDict(
    "DeserializerTypeDef",
    {
        "OpenXJsonSerDe": NotRequired["OpenXJsonSerDeTypeDef"],
        "HiveJsonSerDe": NotRequired["HiveJsonSerDeTypeDef"],
    },
)

DestinationDescriptionTypeDef = TypedDict(
    "DestinationDescriptionTypeDef",
    {
        "DestinationId": str,
        "S3DestinationDescription": NotRequired["S3DestinationDescriptionTypeDef"],
        "ExtendedS3DestinationDescription": NotRequired["ExtendedS3DestinationDescriptionTypeDef"],
        "RedshiftDestinationDescription": NotRequired["RedshiftDestinationDescriptionTypeDef"],
        "ElasticsearchDestinationDescription": NotRequired[
            "ElasticsearchDestinationDescriptionTypeDef"
        ],
        "AmazonopensearchserviceDestinationDescription": NotRequired[
            "AmazonopensearchserviceDestinationDescriptionTypeDef"
        ],
        "SplunkDestinationDescription": NotRequired["SplunkDestinationDescriptionTypeDef"],
        "HttpEndpointDestinationDescription": NotRequired[
            "HttpEndpointDestinationDescriptionTypeDef"
        ],
    },
)

DynamicPartitioningConfigurationTypeDef = TypedDict(
    "DynamicPartitioningConfigurationTypeDef",
    {
        "RetryOptions": NotRequired["RetryOptionsTypeDef"],
        "Enabled": NotRequired[bool],
    },
)

ElasticsearchBufferingHintsTypeDef = TypedDict(
    "ElasticsearchBufferingHintsTypeDef",
    {
        "IntervalInSeconds": NotRequired[int],
        "SizeInMBs": NotRequired[int],
    },
)

ElasticsearchDestinationConfigurationTypeDef = TypedDict(
    "ElasticsearchDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "IndexName": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
        "DomainARN": NotRequired[str],
        "ClusterEndpoint": NotRequired[str],
        "TypeName": NotRequired[str],
        "IndexRotationPeriod": NotRequired[ElasticsearchIndexRotationPeriodType],
        "BufferingHints": NotRequired["ElasticsearchBufferingHintsTypeDef"],
        "RetryOptions": NotRequired["ElasticsearchRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[ElasticsearchS3BackupModeType],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "VpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
    },
)

ElasticsearchDestinationDescriptionTypeDef = TypedDict(
    "ElasticsearchDestinationDescriptionTypeDef",
    {
        "RoleARN": NotRequired[str],
        "DomainARN": NotRequired[str],
        "ClusterEndpoint": NotRequired[str],
        "IndexName": NotRequired[str],
        "TypeName": NotRequired[str],
        "IndexRotationPeriod": NotRequired[ElasticsearchIndexRotationPeriodType],
        "BufferingHints": NotRequired["ElasticsearchBufferingHintsTypeDef"],
        "RetryOptions": NotRequired["ElasticsearchRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[ElasticsearchS3BackupModeType],
        "S3DestinationDescription": NotRequired["S3DestinationDescriptionTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "VpcConfigurationDescription": NotRequired["VpcConfigurationDescriptionTypeDef"],
    },
)

ElasticsearchDestinationUpdateTypeDef = TypedDict(
    "ElasticsearchDestinationUpdateTypeDef",
    {
        "RoleARN": NotRequired[str],
        "DomainARN": NotRequired[str],
        "ClusterEndpoint": NotRequired[str],
        "IndexName": NotRequired[str],
        "TypeName": NotRequired[str],
        "IndexRotationPeriod": NotRequired[ElasticsearchIndexRotationPeriodType],
        "BufferingHints": NotRequired["ElasticsearchBufferingHintsTypeDef"],
        "RetryOptions": NotRequired["ElasticsearchRetryOptionsTypeDef"],
        "S3Update": NotRequired["S3DestinationUpdateTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

ElasticsearchRetryOptionsTypeDef = TypedDict(
    "ElasticsearchRetryOptionsTypeDef",
    {
        "DurationInSeconds": NotRequired[int],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "NoEncryptionConfig": NotRequired[Literal["NoEncryption"]],
        "KMSEncryptionConfig": NotRequired["KMSEncryptionConfigTypeDef"],
    },
)

ExtendedS3DestinationConfigurationTypeDef = TypedDict(
    "ExtendedS3DestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": NotRequired[str],
        "ErrorOutputPrefix": NotRequired[str],
        "BufferingHints": NotRequired["BufferingHintsTypeDef"],
        "CompressionFormat": NotRequired[CompressionFormatType],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "S3BackupMode": NotRequired[S3BackupModeType],
        "S3BackupConfiguration": NotRequired["S3DestinationConfigurationTypeDef"],
        "DataFormatConversionConfiguration": NotRequired[
            "DataFormatConversionConfigurationTypeDef"
        ],
        "DynamicPartitioningConfiguration": NotRequired["DynamicPartitioningConfigurationTypeDef"],
    },
)

ExtendedS3DestinationDescriptionTypeDef = TypedDict(
    "ExtendedS3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "Prefix": NotRequired[str],
        "ErrorOutputPrefix": NotRequired[str],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "S3BackupMode": NotRequired[S3BackupModeType],
        "S3BackupDescription": NotRequired["S3DestinationDescriptionTypeDef"],
        "DataFormatConversionConfiguration": NotRequired[
            "DataFormatConversionConfigurationTypeDef"
        ],
        "DynamicPartitioningConfiguration": NotRequired["DynamicPartitioningConfigurationTypeDef"],
    },
)

ExtendedS3DestinationUpdateTypeDef = TypedDict(
    "ExtendedS3DestinationUpdateTypeDef",
    {
        "RoleARN": NotRequired[str],
        "BucketARN": NotRequired[str],
        "Prefix": NotRequired[str],
        "ErrorOutputPrefix": NotRequired[str],
        "BufferingHints": NotRequired["BufferingHintsTypeDef"],
        "CompressionFormat": NotRequired[CompressionFormatType],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "S3BackupMode": NotRequired[S3BackupModeType],
        "S3BackupUpdate": NotRequired["S3DestinationUpdateTypeDef"],
        "DataFormatConversionConfiguration": NotRequired[
            "DataFormatConversionConfigurationTypeDef"
        ],
        "DynamicPartitioningConfiguration": NotRequired["DynamicPartitioningConfigurationTypeDef"],
    },
)

FailureDescriptionTypeDef = TypedDict(
    "FailureDescriptionTypeDef",
    {
        "Type": DeliveryStreamFailureTypeType,
        "Details": str,
    },
)

HiveJsonSerDeTypeDef = TypedDict(
    "HiveJsonSerDeTypeDef",
    {
        "TimestampFormats": NotRequired[Sequence[str]],
    },
)

HttpEndpointBufferingHintsTypeDef = TypedDict(
    "HttpEndpointBufferingHintsTypeDef",
    {
        "SizeInMBs": NotRequired[int],
        "IntervalInSeconds": NotRequired[int],
    },
)

HttpEndpointCommonAttributeTypeDef = TypedDict(
    "HttpEndpointCommonAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
)

HttpEndpointConfigurationTypeDef = TypedDict(
    "HttpEndpointConfigurationTypeDef",
    {
        "Url": str,
        "Name": NotRequired[str],
        "AccessKey": NotRequired[str],
    },
)

HttpEndpointDescriptionTypeDef = TypedDict(
    "HttpEndpointDescriptionTypeDef",
    {
        "Url": NotRequired[str],
        "Name": NotRequired[str],
    },
)

HttpEndpointDestinationConfigurationTypeDef = TypedDict(
    "HttpEndpointDestinationConfigurationTypeDef",
    {
        "EndpointConfiguration": "HttpEndpointConfigurationTypeDef",
        "S3Configuration": "S3DestinationConfigurationTypeDef",
        "BufferingHints": NotRequired["HttpEndpointBufferingHintsTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "RequestConfiguration": NotRequired["HttpEndpointRequestConfigurationTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "RoleARN": NotRequired[str],
        "RetryOptions": NotRequired["HttpEndpointRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[HttpEndpointS3BackupModeType],
    },
)

HttpEndpointDestinationDescriptionTypeDef = TypedDict(
    "HttpEndpointDestinationDescriptionTypeDef",
    {
        "EndpointConfiguration": NotRequired["HttpEndpointDescriptionTypeDef"],
        "BufferingHints": NotRequired["HttpEndpointBufferingHintsTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "RequestConfiguration": NotRequired["HttpEndpointRequestConfigurationTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "RoleARN": NotRequired[str],
        "RetryOptions": NotRequired["HttpEndpointRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[HttpEndpointS3BackupModeType],
        "S3DestinationDescription": NotRequired["S3DestinationDescriptionTypeDef"],
    },
)

HttpEndpointDestinationUpdateTypeDef = TypedDict(
    "HttpEndpointDestinationUpdateTypeDef",
    {
        "EndpointConfiguration": NotRequired["HttpEndpointConfigurationTypeDef"],
        "BufferingHints": NotRequired["HttpEndpointBufferingHintsTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
        "RequestConfiguration": NotRequired["HttpEndpointRequestConfigurationTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "RoleARN": NotRequired[str],
        "RetryOptions": NotRequired["HttpEndpointRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[HttpEndpointS3BackupModeType],
        "S3Update": NotRequired["S3DestinationUpdateTypeDef"],
    },
)

HttpEndpointRequestConfigurationTypeDef = TypedDict(
    "HttpEndpointRequestConfigurationTypeDef",
    {
        "ContentEncoding": NotRequired[ContentEncodingType],
        "CommonAttributes": NotRequired[Sequence["HttpEndpointCommonAttributeTypeDef"]],
    },
)

HttpEndpointRetryOptionsTypeDef = TypedDict(
    "HttpEndpointRetryOptionsTypeDef",
    {
        "DurationInSeconds": NotRequired[int],
    },
)

InputFormatConfigurationTypeDef = TypedDict(
    "InputFormatConfigurationTypeDef",
    {
        "Deserializer": NotRequired["DeserializerTypeDef"],
    },
)

KMSEncryptionConfigTypeDef = TypedDict(
    "KMSEncryptionConfigTypeDef",
    {
        "AWSKMSKeyARN": str,
    },
)

KinesisStreamSourceConfigurationTypeDef = TypedDict(
    "KinesisStreamSourceConfigurationTypeDef",
    {
        "KinesisStreamARN": str,
        "RoleARN": str,
    },
)

KinesisStreamSourceDescriptionTypeDef = TypedDict(
    "KinesisStreamSourceDescriptionTypeDef",
    {
        "KinesisStreamARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "DeliveryStartTimestamp": NotRequired[datetime],
    },
)

ListDeliveryStreamsInputRequestTypeDef = TypedDict(
    "ListDeliveryStreamsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "DeliveryStreamType": NotRequired[DeliveryStreamTypeType],
        "ExclusiveStartDeliveryStreamName": NotRequired[str],
    },
)

ListDeliveryStreamsOutputTypeDef = TypedDict(
    "ListDeliveryStreamsOutputTypeDef",
    {
        "DeliveryStreamNames": List[str],
        "HasMoreDeliveryStreams": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForDeliveryStreamInputRequestTypeDef = TypedDict(
    "ListTagsForDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "ExclusiveStartTagKey": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTagsForDeliveryStreamOutputTypeDef = TypedDict(
    "ListTagsForDeliveryStreamOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OpenXJsonSerDeTypeDef = TypedDict(
    "OpenXJsonSerDeTypeDef",
    {
        "ConvertDotsInJsonKeysToUnderscores": NotRequired[bool],
        "CaseInsensitive": NotRequired[bool],
        "ColumnToJsonKeyMappings": NotRequired[Mapping[str, str]],
    },
)

OrcSerDeTypeDef = TypedDict(
    "OrcSerDeTypeDef",
    {
        "StripeSizeBytes": NotRequired[int],
        "BlockSizeBytes": NotRequired[int],
        "RowIndexStride": NotRequired[int],
        "EnablePadding": NotRequired[bool],
        "PaddingTolerance": NotRequired[float],
        "Compression": NotRequired[OrcCompressionType],
        "BloomFilterColumns": NotRequired[Sequence[str]],
        "BloomFilterFalsePositiveProbability": NotRequired[float],
        "DictionaryKeyThreshold": NotRequired[float],
        "FormatVersion": NotRequired[OrcFormatVersionType],
    },
)

OutputFormatConfigurationTypeDef = TypedDict(
    "OutputFormatConfigurationTypeDef",
    {
        "Serializer": NotRequired["SerializerTypeDef"],
    },
)

ParquetSerDeTypeDef = TypedDict(
    "ParquetSerDeTypeDef",
    {
        "BlockSizeBytes": NotRequired[int],
        "PageSizeBytes": NotRequired[int],
        "Compression": NotRequired[ParquetCompressionType],
        "EnableDictionaryCompression": NotRequired[bool],
        "MaxPaddingBytes": NotRequired[int],
        "WriterVersion": NotRequired[ParquetWriterVersionType],
    },
)

ProcessingConfigurationTypeDef = TypedDict(
    "ProcessingConfigurationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "Processors": NotRequired[Sequence["ProcessorTypeDef"]],
    },
)

ProcessorParameterTypeDef = TypedDict(
    "ProcessorParameterTypeDef",
    {
        "ParameterName": ProcessorParameterNameType,
        "ParameterValue": str,
    },
)

ProcessorTypeDef = TypedDict(
    "ProcessorTypeDef",
    {
        "Type": ProcessorTypeType,
        "Parameters": NotRequired[Sequence["ProcessorParameterTypeDef"]],
    },
)

PutRecordBatchInputRequestTypeDef = TypedDict(
    "PutRecordBatchInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Records": Sequence["RecordTypeDef"],
    },
)

PutRecordBatchOutputTypeDef = TypedDict(
    "PutRecordBatchOutputTypeDef",
    {
        "FailedPutCount": int,
        "Encrypted": bool,
        "RequestResponses": List["PutRecordBatchResponseEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordBatchResponseEntryTypeDef = TypedDict(
    "PutRecordBatchResponseEntryTypeDef",
    {
        "RecordId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

PutRecordInputRequestTypeDef = TypedDict(
    "PutRecordInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "Record": "RecordTypeDef",
    },
)

PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "RecordId": str,
        "Encrypted": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

RedshiftDestinationConfigurationTypeDef = TypedDict(
    "RedshiftDestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "Username": str,
        "Password": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
        "RetryOptions": NotRequired["RedshiftRetryOptionsTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "S3BackupMode": NotRequired[RedshiftS3BackupModeType],
        "S3BackupConfiguration": NotRequired["S3DestinationConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

RedshiftDestinationDescriptionTypeDef = TypedDict(
    "RedshiftDestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "ClusterJDBCURL": str,
        "CopyCommand": "CopyCommandTypeDef",
        "Username": str,
        "S3DestinationDescription": "S3DestinationDescriptionTypeDef",
        "RetryOptions": NotRequired["RedshiftRetryOptionsTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "S3BackupMode": NotRequired[RedshiftS3BackupModeType],
        "S3BackupDescription": NotRequired["S3DestinationDescriptionTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

RedshiftDestinationUpdateTypeDef = TypedDict(
    "RedshiftDestinationUpdateTypeDef",
    {
        "RoleARN": NotRequired[str],
        "ClusterJDBCURL": NotRequired[str],
        "CopyCommand": NotRequired["CopyCommandTypeDef"],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "RetryOptions": NotRequired["RedshiftRetryOptionsTypeDef"],
        "S3Update": NotRequired["S3DestinationUpdateTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "S3BackupMode": NotRequired[RedshiftS3BackupModeType],
        "S3BackupUpdate": NotRequired["S3DestinationUpdateTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

RedshiftRetryOptionsTypeDef = TypedDict(
    "RedshiftRetryOptionsTypeDef",
    {
        "DurationInSeconds": NotRequired[int],
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

RetryOptionsTypeDef = TypedDict(
    "RetryOptionsTypeDef",
    {
        "DurationInSeconds": NotRequired[int],
    },
)

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "Prefix": NotRequired[str],
        "ErrorOutputPrefix": NotRequired[str],
        "BufferingHints": NotRequired["BufferingHintsTypeDef"],
        "CompressionFormat": NotRequired[CompressionFormatType],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

S3DestinationDescriptionTypeDef = TypedDict(
    "S3DestinationDescriptionTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "BufferingHints": "BufferingHintsTypeDef",
        "CompressionFormat": CompressionFormatType,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "Prefix": NotRequired[str],
        "ErrorOutputPrefix": NotRequired[str],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

S3DestinationUpdateTypeDef = TypedDict(
    "S3DestinationUpdateTypeDef",
    {
        "RoleARN": NotRequired[str],
        "BucketARN": NotRequired[str],
        "Prefix": NotRequired[str],
        "ErrorOutputPrefix": NotRequired[str],
        "BufferingHints": NotRequired["BufferingHintsTypeDef"],
        "CompressionFormat": NotRequired[CompressionFormatType],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

SchemaConfigurationTypeDef = TypedDict(
    "SchemaConfigurationTypeDef",
    {
        "RoleARN": NotRequired[str],
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Region": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

SerializerTypeDef = TypedDict(
    "SerializerTypeDef",
    {
        "ParquetSerDe": NotRequired["ParquetSerDeTypeDef"],
        "OrcSerDe": NotRequired["OrcSerDeTypeDef"],
    },
)

SourceDescriptionTypeDef = TypedDict(
    "SourceDescriptionTypeDef",
    {
        "KinesisStreamSourceDescription": NotRequired["KinesisStreamSourceDescriptionTypeDef"],
    },
)

SplunkDestinationConfigurationTypeDef = TypedDict(
    "SplunkDestinationConfigurationTypeDef",
    {
        "HECEndpoint": str,
        "HECEndpointType": HECEndpointTypeType,
        "HECToken": str,
        "S3Configuration": "S3DestinationConfigurationTypeDef",
        "HECAcknowledgmentTimeoutInSeconds": NotRequired[int],
        "RetryOptions": NotRequired["SplunkRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[SplunkS3BackupModeType],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

SplunkDestinationDescriptionTypeDef = TypedDict(
    "SplunkDestinationDescriptionTypeDef",
    {
        "HECEndpoint": NotRequired[str],
        "HECEndpointType": NotRequired[HECEndpointTypeType],
        "HECToken": NotRequired[str],
        "HECAcknowledgmentTimeoutInSeconds": NotRequired[int],
        "RetryOptions": NotRequired["SplunkRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[SplunkS3BackupModeType],
        "S3DestinationDescription": NotRequired["S3DestinationDescriptionTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

SplunkDestinationUpdateTypeDef = TypedDict(
    "SplunkDestinationUpdateTypeDef",
    {
        "HECEndpoint": NotRequired[str],
        "HECEndpointType": NotRequired[HECEndpointTypeType],
        "HECToken": NotRequired[str],
        "HECAcknowledgmentTimeoutInSeconds": NotRequired[int],
        "RetryOptions": NotRequired["SplunkRetryOptionsTypeDef"],
        "S3BackupMode": NotRequired[SplunkS3BackupModeType],
        "S3Update": NotRequired["S3DestinationUpdateTypeDef"],
        "ProcessingConfiguration": NotRequired["ProcessingConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired["CloudWatchLoggingOptionsTypeDef"],
    },
)

SplunkRetryOptionsTypeDef = TypedDict(
    "SplunkRetryOptionsTypeDef",
    {
        "DurationInSeconds": NotRequired[int],
    },
)

StartDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "StartDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "DeliveryStreamEncryptionConfigurationInput": NotRequired[
            "DeliveryStreamEncryptionConfigurationInputTypeDef"
        ],
    },
)

StopDeliveryStreamEncryptionInputRequestTypeDef = TypedDict(
    "StopDeliveryStreamEncryptionInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
    },
)

TagDeliveryStreamInputRequestTypeDef = TypedDict(
    "TagDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
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

UntagDeliveryStreamInputRequestTypeDef = TypedDict(
    "UntagDeliveryStreamInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDestinationInputRequestTypeDef = TypedDict(
    "UpdateDestinationInputRequestTypeDef",
    {
        "DeliveryStreamName": str,
        "CurrentDeliveryStreamVersionId": str,
        "DestinationId": str,
        "S3DestinationUpdate": NotRequired["S3DestinationUpdateTypeDef"],
        "ExtendedS3DestinationUpdate": NotRequired["ExtendedS3DestinationUpdateTypeDef"],
        "RedshiftDestinationUpdate": NotRequired["RedshiftDestinationUpdateTypeDef"],
        "ElasticsearchDestinationUpdate": NotRequired["ElasticsearchDestinationUpdateTypeDef"],
        "AmazonopensearchserviceDestinationUpdate": NotRequired[
            "AmazonopensearchserviceDestinationUpdateTypeDef"
        ],
        "SplunkDestinationUpdate": NotRequired["SplunkDestinationUpdateTypeDef"],
        "HttpEndpointDestinationUpdate": NotRequired["HttpEndpointDestinationUpdateTypeDef"],
    },
)

VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "SubnetIds": List[str],
        "RoleARN": str,
        "SecurityGroupIds": List[str],
        "VpcId": str,
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "RoleARN": str,
        "SecurityGroupIds": Sequence[str],
    },
)
