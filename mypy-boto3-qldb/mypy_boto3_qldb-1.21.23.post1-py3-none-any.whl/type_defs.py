"""
Type annotations for qldb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamRequestRequestTypeDef

    data: CancelJournalKinesisStreamRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EncryptionStatusType,
    ErrorCauseType,
    ExportStatusType,
    LedgerStateType,
    OutputFormatType,
    PermissionsModeType,
    S3ObjectEncryptionTypeType,
    StreamStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelJournalKinesisStreamRequestRequestTypeDef",
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerRequestRequestTypeDef",
    "CreateLedgerResponseTypeDef",
    "DeleteLedgerRequestRequestTypeDef",
    "DescribeJournalKinesisStreamRequestRequestTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "DescribeJournalS3ExportRequestRequestTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "DescribeLedgerRequestRequestTypeDef",
    "DescribeLedgerResponseTypeDef",
    "ExportJournalToS3RequestRequestTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "GetBlockRequestRequestTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestRequestRequestTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionRequestRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerEncryptionDescriptionTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ListJournalS3ExportsForLedgerRequestRequestTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsRequestRequestTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
    "ListLedgersRequestRequestTypeDef",
    "ListLedgersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "StreamJournalToKinesisRequestRequestTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLedgerPermissionsModeRequestRequestTypeDef",
    "UpdateLedgerPermissionsModeResponseTypeDef",
    "UpdateLedgerRequestRequestTypeDef",
    "UpdateLedgerResponseTypeDef",
    "ValueHolderTypeDef",
)

CancelJournalKinesisStreamRequestRequestTypeDef = TypedDict(
    "CancelJournalKinesisStreamRequestRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)

CancelJournalKinesisStreamResponseTypeDef = TypedDict(
    "CancelJournalKinesisStreamResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLedgerRequestRequestTypeDef = TypedDict(
    "CreateLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
        "Tags": NotRequired[Mapping[str, str]],
        "DeletionProtection": NotRequired[bool],
        "KmsKey": NotRequired[str],
    },
)

CreateLedgerResponseTypeDef = TypedDict(
    "CreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "KmsKeyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLedgerRequestRequestTypeDef = TypedDict(
    "DeleteLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeJournalKinesisStreamRequestRequestTypeDef = TypedDict(
    "DescribeJournalKinesisStreamRequestRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)

DescribeJournalKinesisStreamResponseTypeDef = TypedDict(
    "DescribeJournalKinesisStreamResponseTypeDef",
    {
        "Stream": "JournalKinesisStreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJournalS3ExportRequestRequestTypeDef = TypedDict(
    "DescribeJournalS3ExportRequestRequestTypeDef",
    {
        "Name": str,
        "ExportId": str,
    },
)

DescribeJournalS3ExportResponseTypeDef = TypedDict(
    "DescribeJournalS3ExportResponseTypeDef",
    {
        "ExportDescription": "JournalS3ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLedgerRequestRequestTypeDef = TypedDict(
    "DescribeLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeLedgerResponseTypeDef = TypedDict(
    "DescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "EncryptionDescription": "LedgerEncryptionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportJournalToS3RequestRequestTypeDef = TypedDict(
    "ExportJournalToS3RequestRequestTypeDef",
    {
        "Name": str,
        "InclusiveStartTime": Union[datetime, str],
        "ExclusiveEndTime": Union[datetime, str],
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
        "OutputFormat": NotRequired[OutputFormatType],
    },
)

ExportJournalToS3ResponseTypeDef = TypedDict(
    "ExportJournalToS3ResponseTypeDef",
    {
        "ExportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlockRequestRequestTypeDef = TypedDict(
    "GetBlockRequestRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": "ValueHolderTypeDef",
        "DigestTipAddress": NotRequired["ValueHolderTypeDef"],
    },
)

GetBlockResponseTypeDef = TypedDict(
    "GetBlockResponseTypeDef",
    {
        "Block": "ValueHolderTypeDef",
        "Proof": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDigestRequestRequestTypeDef = TypedDict(
    "GetDigestRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetDigestResponseTypeDef = TypedDict(
    "GetDigestResponseTypeDef",
    {
        "Digest": bytes,
        "DigestTipAddress": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRevisionRequestRequestTypeDef = TypedDict(
    "GetRevisionRequestRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": "ValueHolderTypeDef",
        "DocumentId": str,
        "DigestTipAddress": NotRequired["ValueHolderTypeDef"],
    },
)

GetRevisionResponseTypeDef = TypedDict(
    "GetRevisionResponseTypeDef",
    {
        "Proof": "ValueHolderTypeDef",
        "Revision": "ValueHolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JournalKinesisStreamDescriptionTypeDef = TypedDict(
    "JournalKinesisStreamDescriptionTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "StreamId": str,
        "Status": StreamStatusType,
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
        "CreationTime": NotRequired[datetime],
        "InclusiveStartTime": NotRequired[datetime],
        "ExclusiveEndTime": NotRequired[datetime],
        "Arn": NotRequired[str],
        "ErrorCause": NotRequired[ErrorCauseType],
    },
)

JournalS3ExportDescriptionTypeDef = TypedDict(
    "JournalS3ExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": ExportStatusType,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
        "OutputFormat": NotRequired[OutputFormatType],
    },
)

KinesisConfigurationTypeDef = TypedDict(
    "KinesisConfigurationTypeDef",
    {
        "StreamArn": str,
        "AggregationEnabled": NotRequired[bool],
    },
)

LedgerEncryptionDescriptionTypeDef = TypedDict(
    "LedgerEncryptionDescriptionTypeDef",
    {
        "KmsKeyArn": str,
        "EncryptionStatus": EncryptionStatusType,
        "InaccessibleKmsKeyDateTime": NotRequired[datetime],
    },
)

LedgerSummaryTypeDef = TypedDict(
    "LedgerSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[LedgerStateType],
        "CreationDateTime": NotRequired[datetime],
    },
)

ListJournalKinesisStreamsForLedgerRequestRequestTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    {
        "LedgerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListJournalKinesisStreamsForLedgerResponseTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    {
        "Streams": List["JournalKinesisStreamDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJournalS3ExportsForLedgerRequestRequestTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJournalS3ExportsRequestRequestTypeDef = TypedDict(
    "ListJournalS3ExportsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListJournalS3ExportsResponseTypeDef = TypedDict(
    "ListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLedgersRequestRequestTypeDef = TypedDict(
    "ListLedgersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListLedgersResponseTypeDef = TypedDict(
    "ListLedgersResponseTypeDef",
    {
        "Ledgers": List["LedgerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
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

S3EncryptionConfigurationTypeDef = TypedDict(
    "S3EncryptionConfigurationTypeDef",
    {
        "ObjectEncryptionType": S3ObjectEncryptionTypeType,
        "KmsKeyArn": NotRequired[str],
    },
)

S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": "S3EncryptionConfigurationTypeDef",
    },
)

StreamJournalToKinesisRequestRequestTypeDef = TypedDict(
    "StreamJournalToKinesisRequestRequestTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "InclusiveStartTime": Union[datetime, str],
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
        "Tags": NotRequired[Mapping[str, str]],
        "ExclusiveEndTime": NotRequired[Union[datetime, str]],
    },
)

StreamJournalToKinesisResponseTypeDef = TypedDict(
    "StreamJournalToKinesisResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateLedgerPermissionsModeRequestRequestTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
    },
)

UpdateLedgerPermissionsModeResponseTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "PermissionsMode": PermissionsModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLedgerRequestRequestTypeDef = TypedDict(
    "UpdateLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "DeletionProtection": NotRequired[bool],
        "KmsKey": NotRequired[str],
    },
)

UpdateLedgerResponseTypeDef = TypedDict(
    "UpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
        "EncryptionDescription": "LedgerEncryptionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonText": NotRequired[str],
    },
)
