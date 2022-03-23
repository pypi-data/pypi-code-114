"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import CreateDatabaseRequestRequestTypeDef

    data: CreateDatabaseRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import MeasureValueTypeType, S3EncryptionOptionType, TableStatusType, TimeUnitType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatabaseRequestRequestTypeDef",
    "CreateDatabaseResponseTypeDef",
    "CreateTableRequestRequestTypeDef",
    "CreateTableResponseTypeDef",
    "DatabaseTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DescribeDatabaseRequestRequestTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeTableRequestRequestTypeDef",
    "DescribeTableResponseTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "ListDatabasesRequestRequestTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MagneticStoreRejectedDataLocationTypeDef",
    "MagneticStoreWritePropertiesTypeDef",
    "MeasureValueTypeDef",
    "RecordTypeDef",
    "RecordsIngestedTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPropertiesTypeDef",
    "S3ConfigurationTypeDef",
    "TableTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "UpdateDatabaseResponseTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "UpdateTableResponseTypeDef",
    "WriteRecordsRequestRequestTypeDef",
    "WriteRecordsResponseTypeDef",
)

CreateDatabaseRequestRequestTypeDef = TypedDict(
    "CreateDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDatabaseResponseTypeDef = TypedDict(
    "CreateDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTableRequestRequestTypeDef = TypedDict(
    "CreateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "RetentionProperties": NotRequired["RetentionPropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "MagneticStoreWriteProperties": NotRequired["MagneticStoreWritePropertiesTypeDef"],
    },
)

CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Arn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableCount": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

DeleteDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)

DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

DescribeDatabaseRequestRequestTypeDef = TypedDict(
    "DescribeDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)

DescribeDatabaseResponseTypeDef = TypedDict(
    "DescribeDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
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

DescribeTableRequestRequestTypeDef = TypedDict(
    "DescribeTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
        "DimensionValueType": NotRequired[Literal["VARCHAR"]],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

ListDatabasesRequestRequestTypeDef = TypedDict(
    "ListDatabasesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "Tables": List["TableTypeDef"],
        "NextToken": str,
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

MagneticStoreRejectedDataLocationTypeDef = TypedDict(
    "MagneticStoreRejectedDataLocationTypeDef",
    {
        "S3Configuration": NotRequired["S3ConfigurationTypeDef"],
    },
)

MagneticStoreWritePropertiesTypeDef = TypedDict(
    "MagneticStoreWritePropertiesTypeDef",
    {
        "EnableMagneticStoreWrites": bool,
        "MagneticStoreRejectedDataLocation": NotRequired[
            "MagneticStoreRejectedDataLocationTypeDef"
        ],
    },
)

MeasureValueTypeDef = TypedDict(
    "MeasureValueTypeDef",
    {
        "Name": str,
        "Value": str,
        "Type": MeasureValueTypeType,
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "MeasureName": NotRequired[str],
        "MeasureValue": NotRequired[str],
        "MeasureValueType": NotRequired[MeasureValueTypeType],
        "Time": NotRequired[str],
        "TimeUnit": NotRequired[TimeUnitType],
        "Version": NotRequired[int],
        "MeasureValues": NotRequired[Sequence["MeasureValueTypeDef"]],
    },
)

RecordsIngestedTypeDef = TypedDict(
    "RecordsIngestedTypeDef",
    {
        "Total": NotRequired[int],
        "MemoryStore": NotRequired[int],
        "MagneticStore": NotRequired[int],
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

RetentionPropertiesTypeDef = TypedDict(
    "RetentionPropertiesTypeDef",
    {
        "MemoryStoreRetentionPeriodInHours": int,
        "MagneticStoreRetentionPeriodInDays": int,
    },
)

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectKeyPrefix": NotRequired[str],
        "EncryptionOption": NotRequired[S3EncryptionOptionType],
        "KmsKeyId": NotRequired[str],
    },
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Arn": NotRequired[str],
        "TableName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableStatus": NotRequired[TableStatusType],
        "RetentionProperties": NotRequired["RetentionPropertiesTypeDef"],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "MagneticStoreWriteProperties": NotRequired["MagneticStoreWritePropertiesTypeDef"],
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
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "KmsKeyId": str,
    },
)

UpdateDatabaseResponseTypeDef = TypedDict(
    "UpdateDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTableRequestRequestTypeDef = TypedDict(
    "UpdateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "RetentionProperties": NotRequired["RetentionPropertiesTypeDef"],
        "MagneticStoreWriteProperties": NotRequired["MagneticStoreWritePropertiesTypeDef"],
    },
)

UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WriteRecordsRequestRequestTypeDef = TypedDict(
    "WriteRecordsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Records": Sequence["RecordTypeDef"],
        "CommonAttributes": NotRequired["RecordTypeDef"],
    },
)

WriteRecordsResponseTypeDef = TypedDict(
    "WriteRecordsResponseTypeDef",
    {
        "RecordsIngested": "RecordsIngestedTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
