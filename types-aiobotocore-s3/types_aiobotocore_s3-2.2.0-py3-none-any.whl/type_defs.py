"""
Type annotations for s3 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_s3.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Callable, Dict, List, Mapping, Sequence, Union

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ArchiveStatusType,
    BucketAccelerateStatusType,
    BucketCannedACLType,
    BucketLocationConstraintType,
    BucketLogsPermissionType,
    BucketVersioningStatusType,
    ChecksumAlgorithmType,
    CompressionTypeType,
    DeleteMarkerReplicationStatusType,
    EventType,
    ExistingObjectReplicationStatusType,
    ExpirationStatusType,
    FileHeaderInfoType,
    FilterRuleNameType,
    IntelligentTieringAccessTierType,
    IntelligentTieringStatusType,
    InventoryFormatType,
    InventoryFrequencyType,
    InventoryIncludedObjectVersionsType,
    InventoryOptionalFieldType,
    JSONTypeType,
    MetadataDirectiveType,
    MetricsStatusType,
    MFADeleteStatusType,
    MFADeleteType,
    ObjectAttributesType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ObjectLockRetentionModeType,
    ObjectOwnershipType,
    ObjectStorageClassType,
    PayerType,
    PermissionType,
    ProtocolType,
    QuoteFieldsType,
    ReplicaModificationsStatusType,
    ReplicationRuleStatusType,
    ReplicationStatusType,
    ReplicationTimeStatusType,
    ServerSideEncryptionType,
    SseKmsEncryptedObjectsStatusType,
    StorageClassType,
    TaggingDirectiveType,
    TierType,
    TransitionStorageClassType,
    TypeType,
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
    "AbortIncompleteMultipartUploadTypeDef",
    "AbortMultipartUploadOutputTypeDef",
    "AbortMultipartUploadRequestMultipartUploadAbortTypeDef",
    "AbortMultipartUploadRequestRequestTypeDef",
    "AccelerateConfigurationTypeDef",
    "AccessControlPolicyTypeDef",
    "AccessControlTranslationTypeDef",
    "AnalyticsAndOperatorTypeDef",
    "AnalyticsConfigurationTypeDef",
    "AnalyticsExportDestinationTypeDef",
    "AnalyticsFilterTypeDef",
    "AnalyticsS3BucketDestinationTypeDef",
    "BucketCopyRequestTypeDef",
    "BucketDownloadFileRequestTypeDef",
    "BucketDownloadFileobjRequestTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "BucketLoggingStatusTypeDef",
    "BucketObjectRequestTypeDef",
    "BucketTypeDef",
    "BucketUploadFileRequestTypeDef",
    "BucketUploadFileobjRequestTypeDef",
    "CORSConfigurationTypeDef",
    "CORSRuleTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "ChecksumTypeDef",
    "ClientCopyRequestTypeDef",
    "ClientDownloadFileRequestTypeDef",
    "ClientDownloadFileobjRequestTypeDef",
    "ClientGeneratePresignedPostRequestTypeDef",
    "ClientUploadFileRequestTypeDef",
    "ClientUploadFileobjRequestTypeDef",
    "CloudFunctionConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "CompleteMultipartUploadOutputTypeDef",
    "CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef",
    "CompleteMultipartUploadRequestRequestTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CompletedPartTypeDef",
    "ConditionTypeDef",
    "CopyObjectOutputTypeDef",
    "CopyObjectRequestObjectCopyFromTypeDef",
    "CopyObjectRequestObjectSummaryCopyFromTypeDef",
    "CopyObjectRequestRequestTypeDef",
    "CopyObjectResultTypeDef",
    "CopyPartResultTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputTypeDef",
    "CreateBucketRequestBucketCreateTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketRequestServiceResourceCreateBucketTypeDef",
    "CreateMultipartUploadOutputTypeDef",
    "CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef",
    "CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef",
    "CreateMultipartUploadRequestRequestTypeDef",
    "DefaultRetentionTypeDef",
    "DeleteBucketAnalyticsConfigurationRequestRequestTypeDef",
    "DeleteBucketCorsRequestBucketCorsDeleteTypeDef",
    "DeleteBucketCorsRequestRequestTypeDef",
    "DeleteBucketEncryptionRequestRequestTypeDef",
    "DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    "DeleteBucketInventoryConfigurationRequestRequestTypeDef",
    "DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef",
    "DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef",
    "DeleteBucketLifecycleRequestRequestTypeDef",
    "DeleteBucketMetricsConfigurationRequestRequestTypeDef",
    "DeleteBucketOwnershipControlsRequestRequestTypeDef",
    "DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketReplicationRequestRequestTypeDef",
    "DeleteBucketRequestBucketDeleteTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef",
    "DeleteBucketWebsiteRequestRequestTypeDef",
    "DeleteMarkerEntryTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteObjectOutputTypeDef",
    "DeleteObjectRequestObjectDeleteTypeDef",
    "DeleteObjectRequestObjectSummaryDeleteTypeDef",
    "DeleteObjectRequestObjectVersionDeleteTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DeleteObjectTaggingOutputTypeDef",
    "DeleteObjectTaggingRequestRequestTypeDef",
    "DeleteObjectsOutputTypeDef",
    "DeleteObjectsRequestBucketDeleteObjectsTypeDef",
    "DeleteObjectsRequestRequestTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteTypeDef",
    "DeletedObjectTypeDef",
    "DestinationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionTypeDef",
    "ErrorDocumentResponseMetadataTypeDef",
    "ErrorDocumentTypeDef",
    "ErrorTypeDef",
    "ExistingObjectReplicationTypeDef",
    "FilterRuleTypeDef",
    "GetBucketAccelerateConfigurationOutputTypeDef",
    "GetBucketAccelerateConfigurationRequestRequestTypeDef",
    "GetBucketAclOutputTypeDef",
    "GetBucketAclRequestRequestTypeDef",
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    "GetBucketAnalyticsConfigurationRequestRequestTypeDef",
    "GetBucketCorsOutputTypeDef",
    "GetBucketCorsRequestRequestTypeDef",
    "GetBucketEncryptionOutputTypeDef",
    "GetBucketEncryptionRequestRequestTypeDef",
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    "GetBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    "GetBucketInventoryConfigurationOutputTypeDef",
    "GetBucketInventoryConfigurationRequestRequestTypeDef",
    "GetBucketLifecycleConfigurationOutputTypeDef",
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketLifecycleOutputTypeDef",
    "GetBucketLifecycleRequestRequestTypeDef",
    "GetBucketLocationOutputTypeDef",
    "GetBucketLocationRequestRequestTypeDef",
    "GetBucketLoggingOutputTypeDef",
    "GetBucketLoggingRequestRequestTypeDef",
    "GetBucketMetricsConfigurationOutputTypeDef",
    "GetBucketMetricsConfigurationRequestRequestTypeDef",
    "GetBucketNotificationConfigurationRequestRequestTypeDef",
    "GetBucketOwnershipControlsOutputTypeDef",
    "GetBucketOwnershipControlsRequestRequestTypeDef",
    "GetBucketPolicyOutputTypeDef",
    "GetBucketPolicyRequestRequestTypeDef",
    "GetBucketPolicyStatusOutputTypeDef",
    "GetBucketPolicyStatusRequestRequestTypeDef",
    "GetBucketReplicationOutputTypeDef",
    "GetBucketReplicationRequestRequestTypeDef",
    "GetBucketRequestPaymentOutputTypeDef",
    "GetBucketRequestPaymentRequestRequestTypeDef",
    "GetBucketTaggingOutputTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "GetBucketVersioningOutputTypeDef",
    "GetBucketVersioningRequestRequestTypeDef",
    "GetBucketWebsiteOutputTypeDef",
    "GetBucketWebsiteRequestRequestTypeDef",
    "GetObjectAclOutputTypeDef",
    "GetObjectAclRequestRequestTypeDef",
    "GetObjectAttributesOutputTypeDef",
    "GetObjectAttributesPartsTypeDef",
    "GetObjectAttributesRequestRequestTypeDef",
    "GetObjectLegalHoldOutputTypeDef",
    "GetObjectLegalHoldRequestRequestTypeDef",
    "GetObjectLockConfigurationOutputTypeDef",
    "GetObjectLockConfigurationRequestRequestTypeDef",
    "GetObjectOutputTypeDef",
    "GetObjectRequestObjectGetTypeDef",
    "GetObjectRequestObjectSummaryGetTypeDef",
    "GetObjectRequestObjectVersionGetTypeDef",
    "GetObjectRequestRequestTypeDef",
    "GetObjectRetentionOutputTypeDef",
    "GetObjectRetentionRequestRequestTypeDef",
    "GetObjectTaggingOutputTypeDef",
    "GetObjectTaggingRequestRequestTypeDef",
    "GetObjectTorrentOutputTypeDef",
    "GetObjectTorrentRequestRequestTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GlacierJobParametersTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "HeadBucketRequestRequestTypeDef",
    "HeadObjectOutputTypeDef",
    "HeadObjectRequestObjectVersionHeadTypeDef",
    "HeadObjectRequestRequestTypeDef",
    "IndexDocumentResponseMetadataTypeDef",
    "IndexDocumentTypeDef",
    "InitiatorResponseMetadataTypeDef",
    "InitiatorTypeDef",
    "InputSerializationTypeDef",
    "IntelligentTieringAndOperatorTypeDef",
    "IntelligentTieringConfigurationTypeDef",
    "IntelligentTieringFilterTypeDef",
    "InventoryConfigurationTypeDef",
    "InventoryDestinationTypeDef",
    "InventoryEncryptionTypeDef",
    "InventoryFilterTypeDef",
    "InventoryS3BucketDestinationTypeDef",
    "InventoryScheduleTypeDef",
    "JSONInputTypeDef",
    "JSONOutputTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    "ListBucketAnalyticsConfigurationsRequestRequestTypeDef",
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    "ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef",
    "ListBucketInventoryConfigurationsOutputTypeDef",
    "ListBucketInventoryConfigurationsRequestRequestTypeDef",
    "ListBucketMetricsConfigurationsOutputTypeDef",
    "ListBucketMetricsConfigurationsRequestRequestTypeDef",
    "ListBucketsOutputTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListMultipartUploadsRequestRequestTypeDef",
    "ListObjectVersionsOutputTypeDef",
    "ListObjectVersionsRequestRequestTypeDef",
    "ListObjectsOutputTypeDef",
    "ListObjectsRequestRequestTypeDef",
    "ListObjectsV2OutputTypeDef",
    "ListObjectsV2RequestRequestTypeDef",
    "ListPartsOutputTypeDef",
    "ListPartsRequestRequestTypeDef",
    "LoggingEnabledResponseMetadataTypeDef",
    "LoggingEnabledTypeDef",
    "MetadataEntryTypeDef",
    "MetricsAndOperatorTypeDef",
    "MetricsConfigurationTypeDef",
    "MetricsFilterTypeDef",
    "MetricsTypeDef",
    "MultipartUploadPartRequestTypeDef",
    "MultipartUploadTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "NotificationConfigurationDeprecatedResponseMetadataTypeDef",
    "NotificationConfigurationDeprecatedTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "NotificationConfigurationResponseMetadataTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectCopyRequestTypeDef",
    "ObjectDownloadFileRequestTypeDef",
    "ObjectDownloadFileobjRequestTypeDef",
    "ObjectIdentifierTypeDef",
    "ObjectLockConfigurationTypeDef",
    "ObjectLockLegalHoldTypeDef",
    "ObjectLockRetentionTypeDef",
    "ObjectLockRuleTypeDef",
    "ObjectMultipartUploadRequestTypeDef",
    "ObjectPartTypeDef",
    "ObjectSummaryMultipartUploadRequestTypeDef",
    "ObjectSummaryVersionRequestTypeDef",
    "ObjectTypeDef",
    "ObjectUploadFileRequestTypeDef",
    "ObjectUploadFileobjRequestTypeDef",
    "ObjectVersionRequestTypeDef",
    "ObjectVersionTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "OwnerResponseMetadataTypeDef",
    "OwnerTypeDef",
    "OwnershipControlsRuleTypeDef",
    "OwnershipControlsTypeDef",
    "PaginatorConfigTypeDef",
    "PartTypeDef",
    "PolicyStatusTypeDef",
    "ProgressEventTypeDef",
    "ProgressTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutBucketAccelerateConfigurationRequestRequestTypeDef",
    "PutBucketAclRequestBucketAclPutTypeDef",
    "PutBucketAclRequestRequestTypeDef",
    "PutBucketAnalyticsConfigurationRequestRequestTypeDef",
    "PutBucketCorsRequestBucketCorsPutTypeDef",
    "PutBucketCorsRequestRequestTypeDef",
    "PutBucketEncryptionRequestRequestTypeDef",
    "PutBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    "PutBucketInventoryConfigurationRequestRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "PutBucketLifecycleRequestBucketLifecyclePutTypeDef",
    "PutBucketLifecycleRequestRequestTypeDef",
    "PutBucketLoggingRequestBucketLoggingPutTypeDef",
    "PutBucketLoggingRequestRequestTypeDef",
    "PutBucketMetricsConfigurationRequestRequestTypeDef",
    "PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef",
    "PutBucketNotificationConfigurationRequestRequestTypeDef",
    "PutBucketNotificationRequestRequestTypeDef",
    "PutBucketOwnershipControlsRequestRequestTypeDef",
    "PutBucketPolicyRequestBucketPolicyPutTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "PutBucketReplicationRequestRequestTypeDef",
    "PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef",
    "PutBucketRequestPaymentRequestRequestTypeDef",
    "PutBucketTaggingRequestBucketTaggingPutTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "PutBucketVersioningRequestBucketVersioningEnableTypeDef",
    "PutBucketVersioningRequestBucketVersioningPutTypeDef",
    "PutBucketVersioningRequestBucketVersioningSuspendTypeDef",
    "PutBucketVersioningRequestRequestTypeDef",
    "PutBucketWebsiteRequestBucketWebsitePutTypeDef",
    "PutBucketWebsiteRequestRequestTypeDef",
    "PutObjectAclOutputTypeDef",
    "PutObjectAclRequestObjectAclPutTypeDef",
    "PutObjectAclRequestRequestTypeDef",
    "PutObjectLegalHoldOutputTypeDef",
    "PutObjectLegalHoldRequestRequestTypeDef",
    "PutObjectLockConfigurationOutputTypeDef",
    "PutObjectLockConfigurationRequestRequestTypeDef",
    "PutObjectOutputTypeDef",
    "PutObjectRequestBucketPutObjectTypeDef",
    "PutObjectRequestObjectPutTypeDef",
    "PutObjectRequestObjectSummaryPutTypeDef",
    "PutObjectRequestRequestTypeDef",
    "PutObjectRetentionOutputTypeDef",
    "PutObjectRetentionRequestRequestTypeDef",
    "PutObjectTaggingOutputTypeDef",
    "PutObjectTaggingRequestRequestTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "QueueConfigurationDeprecatedTypeDef",
    "QueueConfigurationTypeDef",
    "RecordsEventTypeDef",
    "RedirectAllRequestsToResponseMetadataTypeDef",
    "RedirectAllRequestsToTypeDef",
    "RedirectTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "RequestPaymentConfigurationTypeDef",
    "RequestProgressTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreObjectOutputTypeDef",
    "RestoreObjectRequestObjectRestoreObjectTypeDef",
    "RestoreObjectRequestObjectSummaryRestoreObjectTypeDef",
    "RestoreObjectRequestRequestTypeDef",
    "RestoreRequestTypeDef",
    "RoutingRuleTypeDef",
    "RuleTypeDef",
    "S3KeyFilterTypeDef",
    "S3LocationTypeDef",
    "SSEKMSTypeDef",
    "ScanRangeTypeDef",
    "SelectObjectContentEventStreamTypeDef",
    "SelectObjectContentOutputTypeDef",
    "SelectObjectContentRequestRequestTypeDef",
    "SelectParametersTypeDef",
    "ServerSideEncryptionByDefaultTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionRuleTypeDef",
    "ServiceResourceBucketAclRequestTypeDef",
    "ServiceResourceBucketCorsRequestTypeDef",
    "ServiceResourceBucketLifecycleConfigurationRequestTypeDef",
    "ServiceResourceBucketLifecycleRequestTypeDef",
    "ServiceResourceBucketLoggingRequestTypeDef",
    "ServiceResourceBucketNotificationRequestTypeDef",
    "ServiceResourceBucketPolicyRequestTypeDef",
    "ServiceResourceBucketRequestPaymentRequestTypeDef",
    "ServiceResourceBucketRequestTypeDef",
    "ServiceResourceBucketTaggingRequestTypeDef",
    "ServiceResourceBucketVersioningRequestTypeDef",
    "ServiceResourceBucketWebsiteRequestTypeDef",
    "ServiceResourceMultipartUploadPartRequestTypeDef",
    "ServiceResourceMultipartUploadRequestTypeDef",
    "ServiceResourceObjectAclRequestTypeDef",
    "ServiceResourceObjectRequestTypeDef",
    "ServiceResourceObjectSummaryRequestTypeDef",
    "ServiceResourceObjectVersionRequestTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StatsEventTypeDef",
    "StatsTypeDef",
    "StorageClassAnalysisDataExportTypeDef",
    "StorageClassAnalysisTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TargetGrantTypeDef",
    "TieringTypeDef",
    "TopicConfigurationDeprecatedTypeDef",
    "TopicConfigurationTypeDef",
    "TransitionTypeDef",
    "UploadPartCopyOutputTypeDef",
    "UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef",
    "UploadPartCopyRequestRequestTypeDef",
    "UploadPartOutputTypeDef",
    "UploadPartRequestMultipartUploadPartUploadTypeDef",
    "UploadPartRequestRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WebsiteConfigurationTypeDef",
    "WriteGetObjectResponseRequestRequestTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": NotRequired[int],
    },
)

AbortMultipartUploadOutputTypeDef = TypedDict(
    "AbortMultipartUploadOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AbortMultipartUploadRequestMultipartUploadAbortTypeDef = TypedDict(
    "AbortMultipartUploadRequestMultipartUploadAbortTypeDef",
    {
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

AbortMultipartUploadRequestRequestTypeDef = TypedDict(
    "AbortMultipartUploadRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

AccelerateConfigurationTypeDef = TypedDict(
    "AccelerateConfigurationTypeDef",
    {
        "Status": NotRequired[BucketAccelerateStatusType],
    },
)

AccessControlPolicyTypeDef = TypedDict(
    "AccessControlPolicyTypeDef",
    {
        "Grants": NotRequired[Sequence["GrantTypeDef"]],
        "Owner": NotRequired["OwnerTypeDef"],
    },
)

AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)

AnalyticsAndOperatorTypeDef = TypedDict(
    "AnalyticsAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

AnalyticsConfigurationTypeDef = TypedDict(
    "AnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "StorageClassAnalysis": "StorageClassAnalysisTypeDef",
        "Filter": NotRequired["AnalyticsFilterTypeDef"],
    },
)

AnalyticsExportDestinationTypeDef = TypedDict(
    "AnalyticsExportDestinationTypeDef",
    {
        "S3BucketDestination": "AnalyticsS3BucketDestinationTypeDef",
    },
)

AnalyticsFilterTypeDef = TypedDict(
    "AnalyticsFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired["TagTypeDef"],
        "And": NotRequired["AnalyticsAndOperatorTypeDef"],
    },
)

AnalyticsS3BucketDestinationTypeDef = TypedDict(
    "AnalyticsS3BucketDestinationTypeDef",
    {
        "Format": Literal["CSV"],
        "Bucket": str,
        "BucketAccountId": NotRequired[str],
        "Prefix": NotRequired[str],
    },
)

BucketCopyRequestTypeDef = TypedDict(
    "BucketCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "Key": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "SourceClient": NotRequired[BaseClient],
        "Config": NotRequired[TransferConfig],
    },
)

BucketDownloadFileRequestTypeDef = TypedDict(
    "BucketDownloadFileRequestTypeDef",
    {
        "Key": str,
        "Filename": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

BucketDownloadFileobjRequestTypeDef = TypedDict(
    "BucketDownloadFileobjRequestTypeDef",
    {
        "Key": str,
        "Fileobj": Union[IO[Any], StreamingBody],
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

BucketLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecycleConfigurationTypeDef",
    {
        "Rules": Sequence["LifecycleRuleTypeDef"],
    },
)

BucketLoggingStatusTypeDef = TypedDict(
    "BucketLoggingStatusTypeDef",
    {
        "LoggingEnabled": NotRequired["LoggingEnabledTypeDef"],
    },
)

BucketObjectRequestTypeDef = TypedDict(
    "BucketObjectRequestTypeDef",
    {
        "key": str,
    },
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "Name": NotRequired[str],
        "CreationDate": NotRequired[datetime],
    },
)

BucketUploadFileRequestTypeDef = TypedDict(
    "BucketUploadFileRequestTypeDef",
    {
        "Filename": str,
        "Key": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

BucketUploadFileobjRequestTypeDef = TypedDict(
    "BucketUploadFileobjRequestTypeDef",
    {
        "Fileobj": Union[IO[Any], StreamingBody],
        "Key": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

CORSConfigurationTypeDef = TypedDict(
    "CORSConfigurationTypeDef",
    {
        "CORSRules": Sequence["CORSRuleTypeDef"],
    },
)

CORSRuleTypeDef = TypedDict(
    "CORSRuleTypeDef",
    {
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
        "ID": NotRequired[str],
        "AllowedHeaders": NotRequired[List[str]],
        "ExposeHeaders": NotRequired[List[str]],
        "MaxAgeSeconds": NotRequired[int],
    },
)

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": NotRequired[FileHeaderInfoType],
        "Comments": NotRequired[str],
        "QuoteEscapeCharacter": NotRequired[str],
        "RecordDelimiter": NotRequired[str],
        "FieldDelimiter": NotRequired[str],
        "QuoteCharacter": NotRequired[str],
        "AllowQuotedRecordDelimiter": NotRequired[bool],
    },
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": NotRequired[QuoteFieldsType],
        "QuoteEscapeCharacter": NotRequired[str],
        "RecordDelimiter": NotRequired[str],
        "FieldDelimiter": NotRequired[str],
        "QuoteCharacter": NotRequired[str],
    },
)

ChecksumTypeDef = TypedDict(
    "ChecksumTypeDef",
    {
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
    },
)

ClientCopyRequestTypeDef = TypedDict(
    "ClientCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "Bucket": str,
        "Key": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "SourceClient": NotRequired[BaseClient],
        "Config": NotRequired[TransferConfig],
    },
)

ClientDownloadFileRequestTypeDef = TypedDict(
    "ClientDownloadFileRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Filename": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ClientDownloadFileobjRequestTypeDef = TypedDict(
    "ClientDownloadFileobjRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Fileobj": Union[IO[Any], StreamingBody],
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ClientGeneratePresignedPostRequestTypeDef = TypedDict(
    "ClientGeneratePresignedPostRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Fields": NotRequired[Dict[str, Any]],
        "Conditions": NotRequired[List[Any]],
        "ExpiresIn": NotRequired[int],
    },
)

ClientUploadFileRequestTypeDef = TypedDict(
    "ClientUploadFileRequestTypeDef",
    {
        "Filename": str,
        "Bucket": str,
        "Key": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ClientUploadFileobjRequestTypeDef = TypedDict(
    "ClientUploadFileobjRequestTypeDef",
    {
        "Fileobj": Union[IO[Any], StreamingBody],
        "Bucket": str,
        "Key": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

CloudFunctionConfigurationTypeDef = TypedDict(
    "CloudFunctionConfigurationTypeDef",
    {
        "Id": NotRequired[str],
        "Event": NotRequired[EventType],
        "Events": NotRequired[List[EventType]],
        "CloudFunction": NotRequired[str],
        "InvocationRole": NotRequired[str],
    },
)

CommonPrefixTypeDef = TypedDict(
    "CommonPrefixTypeDef",
    {
        "Prefix": NotRequired[str],
    },
)

CompleteMultipartUploadOutputTypeDef = TypedDict(
    "CompleteMultipartUploadOutputTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ChecksumCRC32": str,
        "ChecksumCRC32C": str,
        "ChecksumSHA1": str,
        "ChecksumSHA256": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "VersionId": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef = TypedDict(
    "CompleteMultipartUploadRequestMultipartUploadCompleteTypeDef",
    {
        "MultipartUpload": NotRequired["CompletedMultipartUploadTypeDef"],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
    },
)

CompleteMultipartUploadRequestRequestTypeDef = TypedDict(
    "CompleteMultipartUploadRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "MultipartUpload": NotRequired["CompletedMultipartUploadTypeDef"],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
    },
)

CompletedMultipartUploadTypeDef = TypedDict(
    "CompletedMultipartUploadTypeDef",
    {
        "Parts": NotRequired[Sequence["CompletedPartTypeDef"]],
    },
)

CompletedPartTypeDef = TypedDict(
    "CompletedPartTypeDef",
    {
        "ETag": NotRequired[str],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "PartNumber": NotRequired[int],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": NotRequired[str],
        "KeyPrefixEquals": NotRequired[str],
    },
)

CopyObjectOutputTypeDef = TypedDict(
    "CopyObjectOutputTypeDef",
    {
        "CopyObjectResult": "CopyObjectResultTypeDef",
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyObjectRequestObjectCopyFromTypeDef = TypedDict(
    "CopyObjectRequestObjectCopyFromTypeDef",
    {
        "CopySource": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "CacheControl": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentType": NotRequired[str],
        "CopySourceIfMatch": NotRequired[str],
        "CopySourceIfModifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceIfNoneMatch": NotRequired[str],
        "CopySourceIfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "MetadataDirective": NotRequired[MetadataDirectiveType],
        "TaggingDirective": NotRequired[TaggingDirectiveType],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "CopySourceSSECustomerAlgorithm": NotRequired[str],
        "CopySourceSSECustomerKey": NotRequired[str],
        "CopySourceSSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
        "ExpectedSourceBucketOwner": NotRequired[str],
    },
)

CopyObjectRequestObjectSummaryCopyFromTypeDef = TypedDict(
    "CopyObjectRequestObjectSummaryCopyFromTypeDef",
    {
        "CopySource": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "CacheControl": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentType": NotRequired[str],
        "CopySourceIfMatch": NotRequired[str],
        "CopySourceIfModifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceIfNoneMatch": NotRequired[str],
        "CopySourceIfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "MetadataDirective": NotRequired[MetadataDirectiveType],
        "TaggingDirective": NotRequired[TaggingDirectiveType],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "CopySourceSSECustomerAlgorithm": NotRequired[str],
        "CopySourceSSECustomerKey": NotRequired[str],
        "CopySourceSSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
        "ExpectedSourceBucketOwner": NotRequired[str],
    },
)

CopyObjectRequestRequestTypeDef = TypedDict(
    "CopyObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "CopySource": Union[str, "CopySourceTypeDef"],
        "Key": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "CacheControl": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentType": NotRequired[str],
        "CopySourceIfMatch": NotRequired[str],
        "CopySourceIfModifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceIfNoneMatch": NotRequired[str],
        "CopySourceIfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "MetadataDirective": NotRequired[MetadataDirectiveType],
        "TaggingDirective": NotRequired[TaggingDirectiveType],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "CopySourceSSECustomerAlgorithm": NotRequired[str],
        "CopySourceSSECustomerKey": NotRequired[str],
        "CopySourceSSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
        "ExpectedSourceBucketOwner": NotRequired[str],
    },
)

CopyObjectResultTypeDef = TypedDict(
    "CopyObjectResultTypeDef",
    {
        "ETag": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
    },
)

CopyPartResultTypeDef = TypedDict(
    "CopyPartResultTypeDef",
    {
        "ETag": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
    },
)

CopySourceTypeDef = TypedDict(
    "CopySourceTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
    },
)

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": NotRequired[BucketLocationConstraintType],
    },
)

CreateBucketOutputTypeDef = TypedDict(
    "CreateBucketOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketRequestBucketCreateTypeDef = TypedDict(
    "CreateBucketRequestBucketCreateTypeDef",
    {
        "ACL": NotRequired[BucketCannedACLType],
        "CreateBucketConfiguration": NotRequired["CreateBucketConfigurationTypeDef"],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "ObjectLockEnabledForBucket": NotRequired[bool],
        "ObjectOwnership": NotRequired[ObjectOwnershipType],
    },
)

CreateBucketRequestRequestTypeDef = TypedDict(
    "CreateBucketRequestRequestTypeDef",
    {
        "Bucket": str,
        "ACL": NotRequired[BucketCannedACLType],
        "CreateBucketConfiguration": NotRequired["CreateBucketConfigurationTypeDef"],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "ObjectLockEnabledForBucket": NotRequired[bool],
        "ObjectOwnership": NotRequired[ObjectOwnershipType],
    },
)

CreateBucketRequestServiceResourceCreateBucketTypeDef = TypedDict(
    "CreateBucketRequestServiceResourceCreateBucketTypeDef",
    {
        "Bucket": str,
        "ACL": NotRequired[BucketCannedACLType],
        "CreateBucketConfiguration": NotRequired["CreateBucketConfigurationTypeDef"],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "ObjectLockEnabledForBucket": NotRequired[bool],
        "ObjectOwnership": NotRequired[ObjectOwnershipType],
    },
)

CreateMultipartUploadOutputTypeDef = TypedDict(
    "CreateMultipartUploadOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ChecksumAlgorithm": ChecksumAlgorithmType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef = TypedDict(
    "CreateMultipartUploadRequestObjectInitiateMultipartUploadTypeDef",
    {
        "ACL": NotRequired[ObjectCannedACLType],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentType": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef = TypedDict(
    "CreateMultipartUploadRequestObjectSummaryInitiateMultipartUploadTypeDef",
    {
        "ACL": NotRequired[ObjectCannedACLType],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentType": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

CreateMultipartUploadRequestRequestTypeDef = TypedDict(
    "CreateMultipartUploadRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentType": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

DefaultRetentionTypeDef = TypedDict(
    "DefaultRetentionTypeDef",
    {
        "Mode": NotRequired[ObjectLockRetentionModeType],
        "Days": NotRequired[int],
        "Years": NotRequired[int],
    },
)

DeleteBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketCorsRequestBucketCorsDeleteTypeDef = TypedDict(
    "DeleteBucketCorsRequestBucketCorsDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketCorsRequestRequestTypeDef = TypedDict(
    "DeleteBucketCorsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketEncryptionRequestRequestTypeDef = TypedDict(
    "DeleteBucketEncryptionRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)

DeleteBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestBucketLifecycleConfigurationDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestBucketLifecycleDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketLifecycleRequestRequestTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "DeleteBucketOwnershipControlsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef = TypedDict(
    "DeleteBucketPolicyRequestBucketPolicyDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "DeleteBucketPolicyRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketReplicationRequestRequestTypeDef = TypedDict(
    "DeleteBucketReplicationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketRequestBucketDeleteTypeDef = TypedDict(
    "DeleteBucketRequestBucketDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef = TypedDict(
    "DeleteBucketTaggingRequestBucketTaggingDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "DeleteBucketTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef = TypedDict(
    "DeleteBucketWebsiteRequestBucketWebsiteDeleteTypeDef",
    {
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteBucketWebsiteRequestRequestTypeDef = TypedDict(
    "DeleteBucketWebsiteRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteMarkerEntryTypeDef = TypedDict(
    "DeleteMarkerEntryTypeDef",
    {
        "Owner": NotRequired["OwnerTypeDef"],
        "Key": NotRequired[str],
        "VersionId": NotRequired[str],
        "IsLatest": NotRequired[bool],
        "LastModified": NotRequired[datetime],
    },
)

DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef",
    {
        "Status": NotRequired[DeleteMarkerReplicationStatusType],
    },
)

DeleteObjectOutputTypeDef = TypedDict(
    "DeleteObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "VersionId": str,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectRequestObjectDeleteTypeDef = TypedDict(
    "DeleteObjectRequestObjectDeleteTypeDef",
    {
        "MFA": NotRequired[str],
        "VersionId": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "BypassGovernanceRetention": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteObjectRequestObjectSummaryDeleteTypeDef = TypedDict(
    "DeleteObjectRequestObjectSummaryDeleteTypeDef",
    {
        "MFA": NotRequired[str],
        "VersionId": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "BypassGovernanceRetention": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteObjectRequestObjectVersionDeleteTypeDef = TypedDict(
    "DeleteObjectRequestObjectVersionDeleteTypeDef",
    {
        "MFA": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "BypassGovernanceRetention": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "MFA": NotRequired[str],
        "VersionId": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "BypassGovernanceRetention": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteObjectTaggingOutputTypeDef = TypedDict(
    "DeleteObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectTaggingRequestRequestTypeDef = TypedDict(
    "DeleteObjectTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteObjectsOutputTypeDef = TypedDict(
    "DeleteObjectsOutputTypeDef",
    {
        "Deleted": List["DeletedObjectTypeDef"],
        "RequestCharged": Literal["requester"],
        "Errors": List["ErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectsRequestBucketDeleteObjectsTypeDef = TypedDict(
    "DeleteObjectsRequestBucketDeleteObjectsTypeDef",
    {
        "Delete": "DeleteTypeDef",
        "MFA": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "BypassGovernanceRetention": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

DeleteObjectsRequestRequestTypeDef = TypedDict(
    "DeleteObjectsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Delete": "DeleteTypeDef",
        "MFA": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "BypassGovernanceRetention": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

DeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "DeletePublicAccessBlockRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

DeleteTypeDef = TypedDict(
    "DeleteTypeDef",
    {
        "Objects": Sequence["ObjectIdentifierTypeDef"],
        "Quiet": NotRequired[bool],
    },
)

DeletedObjectTypeDef = TypedDict(
    "DeletedObjectTypeDef",
    {
        "Key": NotRequired[str],
        "VersionId": NotRequired[str],
        "DeleteMarker": NotRequired[bool],
        "DeleteMarkerVersionId": NotRequired[str],
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Bucket": str,
        "Account": NotRequired[str],
        "StorageClass": NotRequired[StorageClassType],
        "AccessControlTranslation": NotRequired["AccessControlTranslationTypeDef"],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "ReplicationTime": NotRequired["ReplicationTimeTypeDef"],
        "Metrics": NotRequired["MetricsTypeDef"],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "ReplicaKmsKeyID": NotRequired[str],
    },
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "EncryptionType": ServerSideEncryptionType,
        "KMSKeyId": NotRequired[str],
        "KMSContext": NotRequired[str],
    },
)

ErrorDocumentResponseMetadataTypeDef = TypedDict(
    "ErrorDocumentResponseMetadataTypeDef",
    {
        "Key": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDocumentTypeDef = TypedDict(
    "ErrorDocumentTypeDef",
    {
        "Key": str,
    },
)

ErrorTypeDef = TypedDict(
    "ErrorTypeDef",
    {
        "Key": NotRequired[str],
        "VersionId": NotRequired[str],
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "Name": NotRequired[FilterRuleNameType],
        "Value": NotRequired[str],
    },
)

GetBucketAccelerateConfigurationOutputTypeDef = TypedDict(
    "GetBucketAccelerateConfigurationOutputTypeDef",
    {
        "Status": BucketAccelerateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAccelerateConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketAccelerateConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketAclOutputTypeDef = TypedDict(
    "GetBucketAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAclRequestRequestTypeDef = TypedDict(
    "GetBucketAclRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketAnalyticsConfigurationOutputTypeDef = TypedDict(
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    {
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketCorsOutputTypeDef = TypedDict(
    "GetBucketCorsOutputTypeDef",
    {
        "CORSRules": List["CORSRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketCorsRequestRequestTypeDef = TypedDict(
    "GetBucketCorsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketEncryptionOutputTypeDef = TypedDict(
    "GetBucketEncryptionOutputTypeDef",
    {
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketEncryptionRequestRequestTypeDef = TypedDict(
    "GetBucketEncryptionRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketIntelligentTieringConfigurationOutputTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    {
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketIntelligentTieringConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)

GetBucketInventoryConfigurationOutputTypeDef = TypedDict(
    "GetBucketInventoryConfigurationOutputTypeDef",
    {
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketLifecycleConfigurationOutputTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationOutputTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketLifecycleOutputTypeDef = TypedDict(
    "GetBucketLifecycleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleRequestRequestTypeDef = TypedDict(
    "GetBucketLifecycleRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketLocationOutputTypeDef = TypedDict(
    "GetBucketLocationOutputTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLocationRequestRequestTypeDef = TypedDict(
    "GetBucketLocationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketLoggingOutputTypeDef = TypedDict(
    "GetBucketLoggingOutputTypeDef",
    {
        "LoggingEnabled": "LoggingEnabledTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLoggingRequestRequestTypeDef = TypedDict(
    "GetBucketLoggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketMetricsConfigurationOutputTypeDef = TypedDict(
    "GetBucketMetricsConfigurationOutputTypeDef",
    {
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketNotificationConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketOwnershipControlsOutputTypeDef = TypedDict(
    "GetBucketOwnershipControlsOutputTypeDef",
    {
        "OwnershipControls": "OwnershipControlsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "GetBucketOwnershipControlsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketPolicyOutputTypeDef = TypedDict(
    "GetBucketPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyRequestRequestTypeDef = TypedDict(
    "GetBucketPolicyRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketPolicyStatusOutputTypeDef = TypedDict(
    "GetBucketPolicyStatusOutputTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetBucketPolicyStatusRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketReplicationOutputTypeDef = TypedDict(
    "GetBucketReplicationOutputTypeDef",
    {
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketReplicationRequestRequestTypeDef = TypedDict(
    "GetBucketReplicationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketRequestPaymentOutputTypeDef = TypedDict(
    "GetBucketRequestPaymentOutputTypeDef",
    {
        "Payer": PayerType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketRequestPaymentRequestRequestTypeDef = TypedDict(
    "GetBucketRequestPaymentRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketTaggingOutputTypeDef = TypedDict(
    "GetBucketTaggingOutputTypeDef",
    {
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketTaggingRequestRequestTypeDef = TypedDict(
    "GetBucketTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketVersioningOutputTypeDef = TypedDict(
    "GetBucketVersioningOutputTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketVersioningRequestRequestTypeDef = TypedDict(
    "GetBucketVersioningRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetBucketWebsiteOutputTypeDef = TypedDict(
    "GetBucketWebsiteOutputTypeDef",
    {
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "ErrorDocument": "ErrorDocumentTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketWebsiteRequestRequestTypeDef = TypedDict(
    "GetBucketWebsiteRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetObjectAclOutputTypeDef = TypedDict(
    "GetObjectAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectAclRequestRequestTypeDef = TypedDict(
    "GetObjectAclRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetObjectAttributesOutputTypeDef = TypedDict(
    "GetObjectAttributesOutputTypeDef",
    {
        "DeleteMarker": bool,
        "LastModified": datetime,
        "VersionId": str,
        "RequestCharged": Literal["requester"],
        "ETag": str,
        "Checksum": "ChecksumTypeDef",
        "ObjectParts": "GetObjectAttributesPartsTypeDef",
        "StorageClass": StorageClassType,
        "ObjectSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectAttributesPartsTypeDef = TypedDict(
    "GetObjectAttributesPartsTypeDef",
    {
        "TotalPartsCount": NotRequired[int],
        "PartNumberMarker": NotRequired[int],
        "NextPartNumberMarker": NotRequired[int],
        "MaxParts": NotRequired[int],
        "IsTruncated": NotRequired[bool],
        "Parts": NotRequired[List["ObjectPartTypeDef"]],
    },
)

GetObjectAttributesRequestRequestTypeDef = TypedDict(
    "GetObjectAttributesRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "ObjectAttributes": Sequence[ObjectAttributesType],
        "VersionId": NotRequired[str],
        "MaxParts": NotRequired[int],
        "PartNumberMarker": NotRequired[int],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetObjectLegalHoldOutputTypeDef = TypedDict(
    "GetObjectLegalHoldOutputTypeDef",
    {
        "LegalHold": "ObjectLockLegalHoldTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectLegalHoldRequestRequestTypeDef = TypedDict(
    "GetObjectLegalHoldRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetObjectLockConfigurationOutputTypeDef = TypedDict(
    "GetObjectLockConfigurationOutputTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectLockConfigurationRequestRequestTypeDef = TypedDict(
    "GetObjectLockConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetObjectOutputTypeDef = TypedDict(
    "GetObjectOutputTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "ChecksumCRC32": str,
        "ChecksumCRC32C": str,
        "ChecksumSHA1": str,
        "ChecksumSHA256": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": ReplicationStatusType,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectRequestObjectGetTypeDef = TypedDict(
    "GetObjectRequestObjectGetTypeDef",
    {
        "IfMatch": NotRequired[str],
        "IfModifiedSince": NotRequired[Union[datetime, str]],
        "IfNoneMatch": NotRequired[str],
        "IfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Range": NotRequired[str],
        "ResponseCacheControl": NotRequired[str],
        "ResponseContentDisposition": NotRequired[str],
        "ResponseContentEncoding": NotRequired[str],
        "ResponseContentLanguage": NotRequired[str],
        "ResponseContentType": NotRequired[str],
        "ResponseExpires": NotRequired[Union[datetime, str]],
        "VersionId": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "PartNumber": NotRequired[int],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumMode": NotRequired[Literal["ENABLED"]],
    },
)

GetObjectRequestObjectSummaryGetTypeDef = TypedDict(
    "GetObjectRequestObjectSummaryGetTypeDef",
    {
        "IfMatch": NotRequired[str],
        "IfModifiedSince": NotRequired[Union[datetime, str]],
        "IfNoneMatch": NotRequired[str],
        "IfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Range": NotRequired[str],
        "ResponseCacheControl": NotRequired[str],
        "ResponseContentDisposition": NotRequired[str],
        "ResponseContentEncoding": NotRequired[str],
        "ResponseContentLanguage": NotRequired[str],
        "ResponseContentType": NotRequired[str],
        "ResponseExpires": NotRequired[Union[datetime, str]],
        "VersionId": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "PartNumber": NotRequired[int],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumMode": NotRequired[Literal["ENABLED"]],
    },
)

GetObjectRequestObjectVersionGetTypeDef = TypedDict(
    "GetObjectRequestObjectVersionGetTypeDef",
    {
        "IfMatch": NotRequired[str],
        "IfModifiedSince": NotRequired[Union[datetime, str]],
        "IfNoneMatch": NotRequired[str],
        "IfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Range": NotRequired[str],
        "ResponseCacheControl": NotRequired[str],
        "ResponseContentDisposition": NotRequired[str],
        "ResponseContentEncoding": NotRequired[str],
        "ResponseContentLanguage": NotRequired[str],
        "ResponseContentType": NotRequired[str],
        "ResponseExpires": NotRequired[Union[datetime, str]],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "PartNumber": NotRequired[int],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumMode": NotRequired[Literal["ENABLED"]],
    },
)

GetObjectRequestRequestTypeDef = TypedDict(
    "GetObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "IfMatch": NotRequired[str],
        "IfModifiedSince": NotRequired[Union[datetime, str]],
        "IfNoneMatch": NotRequired[str],
        "IfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Range": NotRequired[str],
        "ResponseCacheControl": NotRequired[str],
        "ResponseContentDisposition": NotRequired[str],
        "ResponseContentEncoding": NotRequired[str],
        "ResponseContentLanguage": NotRequired[str],
        "ResponseContentType": NotRequired[str],
        "ResponseExpires": NotRequired[Union[datetime, str]],
        "VersionId": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "PartNumber": NotRequired[int],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumMode": NotRequired[Literal["ENABLED"]],
    },
)

GetObjectRetentionOutputTypeDef = TypedDict(
    "GetObjectRetentionOutputTypeDef",
    {
        "Retention": "ObjectLockRetentionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectRetentionRequestRequestTypeDef = TypedDict(
    "GetObjectRetentionRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetObjectTaggingOutputTypeDef = TypedDict(
    "GetObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectTaggingRequestRequestTypeDef = TypedDict(
    "GetObjectTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
    },
)

GetObjectTorrentOutputTypeDef = TypedDict(
    "GetObjectTorrentOutputTypeDef",
    {
        "Body": StreamingBody,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectTorrentRequestRequestTypeDef = TypedDict(
    "GetObjectTorrentRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "GetPublicAccessBlockRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

GlacierJobParametersTypeDef = TypedDict(
    "GlacierJobParametersTypeDef",
    {
        "Tier": TierType,
    },
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": NotRequired["GranteeTypeDef"],
        "Permission": NotRequired[PermissionType],
    },
)

GranteeTypeDef = TypedDict(
    "GranteeTypeDef",
    {
        "Type": TypeType,
        "DisplayName": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "ID": NotRequired[str],
        "URI": NotRequired[str],
    },
)

HeadBucketRequestRequestTypeDef = TypedDict(
    "HeadBucketRequestRequestTypeDef",
    {
        "Bucket": str,
        "ExpectedBucketOwner": NotRequired[str],
    },
)

HeadObjectOutputTypeDef = TypedDict(
    "HeadObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "ArchiveStatus": ArchiveStatusType,
        "LastModified": datetime,
        "ContentLength": int,
        "ChecksumCRC32": str,
        "ChecksumCRC32C": str,
        "ChecksumSHA1": str,
        "ChecksumSHA256": str,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": ReplicationStatusType,
        "PartsCount": int,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HeadObjectRequestObjectVersionHeadTypeDef = TypedDict(
    "HeadObjectRequestObjectVersionHeadTypeDef",
    {
        "IfMatch": NotRequired[str],
        "IfModifiedSince": NotRequired[Union[datetime, str]],
        "IfNoneMatch": NotRequired[str],
        "IfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Range": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "PartNumber": NotRequired[int],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumMode": NotRequired[Literal["ENABLED"]],
    },
)

HeadObjectRequestRequestTypeDef = TypedDict(
    "HeadObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "IfMatch": NotRequired[str],
        "IfModifiedSince": NotRequired[Union[datetime, str]],
        "IfNoneMatch": NotRequired[str],
        "IfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "Range": NotRequired[str],
        "VersionId": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "PartNumber": NotRequired[int],
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumMode": NotRequired[Literal["ENABLED"]],
    },
)

IndexDocumentResponseMetadataTypeDef = TypedDict(
    "IndexDocumentResponseMetadataTypeDef",
    {
        "Suffix": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexDocumentTypeDef = TypedDict(
    "IndexDocumentTypeDef",
    {
        "Suffix": str,
    },
)

InitiatorResponseMetadataTypeDef = TypedDict(
    "InitiatorResponseMetadataTypeDef",
    {
        "ID": str,
        "DisplayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiatorTypeDef = TypedDict(
    "InitiatorTypeDef",
    {
        "ID": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "CSV": NotRequired["CSVInputTypeDef"],
        "CompressionType": NotRequired[CompressionTypeType],
        "JSON": NotRequired["JSONInputTypeDef"],
        "Parquet": NotRequired[Mapping[str, Any]],
    },
)

IntelligentTieringAndOperatorTypeDef = TypedDict(
    "IntelligentTieringAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

IntelligentTieringConfigurationTypeDef = TypedDict(
    "IntelligentTieringConfigurationTypeDef",
    {
        "Id": str,
        "Status": IntelligentTieringStatusType,
        "Tierings": List["TieringTypeDef"],
        "Filter": NotRequired["IntelligentTieringFilterTypeDef"],
    },
)

IntelligentTieringFilterTypeDef = TypedDict(
    "IntelligentTieringFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired["TagTypeDef"],
        "And": NotRequired["IntelligentTieringAndOperatorTypeDef"],
    },
)

InventoryConfigurationTypeDef = TypedDict(
    "InventoryConfigurationTypeDef",
    {
        "Destination": "InventoryDestinationTypeDef",
        "IsEnabled": bool,
        "Id": str,
        "IncludedObjectVersions": InventoryIncludedObjectVersionsType,
        "Schedule": "InventoryScheduleTypeDef",
        "Filter": NotRequired["InventoryFilterTypeDef"],
        "OptionalFields": NotRequired[List[InventoryOptionalFieldType]],
    },
)

InventoryDestinationTypeDef = TypedDict(
    "InventoryDestinationTypeDef",
    {
        "S3BucketDestination": "InventoryS3BucketDestinationTypeDef",
    },
)

InventoryEncryptionTypeDef = TypedDict(
    "InventoryEncryptionTypeDef",
    {
        "SSES3": NotRequired[Dict[str, Any]],
        "SSEKMS": NotRequired["SSEKMSTypeDef"],
    },
)

InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Prefix": str,
    },
)

InventoryS3BucketDestinationTypeDef = TypedDict(
    "InventoryS3BucketDestinationTypeDef",
    {
        "Bucket": str,
        "Format": InventoryFormatType,
        "AccountId": NotRequired[str],
        "Prefix": NotRequired[str],
        "Encryption": NotRequired["InventoryEncryptionTypeDef"],
    },
)

InventoryScheduleTypeDef = TypedDict(
    "InventoryScheduleTypeDef",
    {
        "Frequency": InventoryFrequencyType,
    },
)

JSONInputTypeDef = TypedDict(
    "JSONInputTypeDef",
    {
        "Type": NotRequired[JSONTypeType],
    },
)

JSONOutputTypeDef = TypedDict(
    "JSONOutputTypeDef",
    {
        "RecordDelimiter": NotRequired[str],
    },
)

LambdaFunctionConfigurationTypeDef = TypedDict(
    "LambdaFunctionConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "Events": List[EventType],
        "Id": NotRequired[str],
        "Filter": NotRequired["NotificationConfigurationFilterTypeDef"],
    },
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": Sequence["RuleTypeDef"],
    },
)

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {
        "Date": NotRequired[datetime],
        "Days": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
    },
)

LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "ObjectSizeGreaterThan": NotRequired[int],
        "ObjectSizeLessThan": NotRequired[int],
    },
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired["TagTypeDef"],
        "ObjectSizeGreaterThan": NotRequired[int],
        "ObjectSizeLessThan": NotRequired[int],
        "And": NotRequired["LifecycleRuleAndOperatorTypeDef"],
    },
)

LifecycleRuleTypeDef = TypedDict(
    "LifecycleRuleTypeDef",
    {
        "Status": ExpirationStatusType,
        "Expiration": NotRequired["LifecycleExpirationTypeDef"],
        "ID": NotRequired[str],
        "Prefix": NotRequired[str],
        "Filter": NotRequired["LifecycleRuleFilterTypeDef"],
        "Transitions": NotRequired[List["TransitionTypeDef"]],
        "NoncurrentVersionTransitions": NotRequired[List["NoncurrentVersionTransitionTypeDef"]],
        "NoncurrentVersionExpiration": NotRequired["NoncurrentVersionExpirationTypeDef"],
        "AbortIncompleteMultipartUpload": NotRequired["AbortIncompleteMultipartUploadTypeDef"],
    },
)

ListBucketAnalyticsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List["AnalyticsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketAnalyticsConfigurationsRequestRequestTypeDef = TypedDict(
    "ListBucketAnalyticsConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ContinuationToken": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListBucketIntelligentTieringConfigurationsOutputTypeDef = TypedDict(
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "IntelligentTieringConfigurationList": List["IntelligentTieringConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef = TypedDict(
    "ListBucketIntelligentTieringConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ContinuationToken": NotRequired[str],
    },
)

ListBucketInventoryConfigurationsOutputTypeDef = TypedDict(
    "ListBucketInventoryConfigurationsOutputTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List["InventoryConfigurationTypeDef"],
        "IsTruncated": bool,
        "NextContinuationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketInventoryConfigurationsRequestRequestTypeDef = TypedDict(
    "ListBucketInventoryConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ContinuationToken": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListBucketMetricsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketMetricsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List["MetricsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketMetricsConfigurationsRequestRequestTypeDef = TypedDict(
    "ListBucketMetricsConfigurationsRequestRequestTypeDef",
    {
        "Bucket": str,
        "ContinuationToken": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListBucketsOutputTypeDef = TypedDict(
    "ListBucketsOutputTypeDef",
    {
        "Buckets": List["BucketTypeDef"],
        "Owner": "OwnerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List["MultipartUploadTypeDef"],
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultipartUploadsRequestRequestTypeDef = TypedDict(
    "ListMultipartUploadsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Delimiter": NotRequired[str],
        "EncodingType": NotRequired[Literal["url"]],
        "KeyMarker": NotRequired[str],
        "MaxUploads": NotRequired[int],
        "Prefix": NotRequired[str],
        "UploadIdMarker": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListObjectVersionsOutputTypeDef = TypedDict(
    "ListObjectVersionsOutputTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List["ObjectVersionTypeDef"],
        "DeleteMarkers": List["DeleteMarkerEntryTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectVersionsRequestRequestTypeDef = TypedDict(
    "ListObjectVersionsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Delimiter": NotRequired[str],
        "EncodingType": NotRequired[Literal["url"]],
        "KeyMarker": NotRequired[str],
        "MaxKeys": NotRequired[int],
        "Prefix": NotRequired[str],
        "VersionIdMarker": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListObjectsOutputTypeDef = TypedDict(
    "ListObjectsOutputTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectsRequestRequestTypeDef = TypedDict(
    "ListObjectsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Delimiter": NotRequired[str],
        "EncodingType": NotRequired[Literal["url"]],
        "Marker": NotRequired[str],
        "MaxKeys": NotRequired[int],
        "Prefix": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListObjectsV2OutputTypeDef = TypedDict(
    "ListObjectsV2OutputTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectsV2RequestRequestTypeDef = TypedDict(
    "ListObjectsV2RequestRequestTypeDef",
    {
        "Bucket": str,
        "Delimiter": NotRequired[str],
        "EncodingType": NotRequired[Literal["url"]],
        "MaxKeys": NotRequired[int],
        "Prefix": NotRequired[str],
        "ContinuationToken": NotRequired[str],
        "FetchOwner": NotRequired[bool],
        "StartAfter": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List["PartTypeDef"],
        "Initiator": "InitiatorTypeDef",
        "Owner": "OwnerTypeDef",
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ChecksumAlgorithm": ChecksumAlgorithmType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartsRequestRequestTypeDef = TypedDict(
    "ListPartsRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "MaxParts": NotRequired[int],
        "PartNumberMarker": NotRequired[int],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
    },
)

LoggingEnabledResponseMetadataTypeDef = TypedDict(
    "LoggingEnabledResponseMetadataTypeDef",
    {
        "TargetBucket": str,
        "TargetGrants": List["TargetGrantTypeDef"],
        "TargetPrefix": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingEnabledTypeDef = TypedDict(
    "LoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetPrefix": str,
        "TargetGrants": NotRequired[List["TargetGrantTypeDef"]],
    },
)

MetadataEntryTypeDef = TypedDict(
    "MetadataEntryTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

MetricsAndOperatorTypeDef = TypedDict(
    "MetricsAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "AccessPointArn": NotRequired[str],
    },
)

MetricsConfigurationTypeDef = TypedDict(
    "MetricsConfigurationTypeDef",
    {
        "Id": str,
        "Filter": NotRequired["MetricsFilterTypeDef"],
    },
)

MetricsFilterTypeDef = TypedDict(
    "MetricsFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired["TagTypeDef"],
        "AccessPointArn": NotRequired[str],
        "And": NotRequired["MetricsAndOperatorTypeDef"],
    },
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "Status": MetricsStatusType,
        "EventThreshold": NotRequired["ReplicationTimeValueTypeDef"],
    },
)

MultipartUploadPartRequestTypeDef = TypedDict(
    "MultipartUploadPartRequestTypeDef",
    {
        "part_number": str,
    },
)

MultipartUploadTypeDef = TypedDict(
    "MultipartUploadTypeDef",
    {
        "UploadId": NotRequired[str],
        "Key": NotRequired[str],
        "Initiated": NotRequired[datetime],
        "StorageClass": NotRequired[StorageClassType],
        "Owner": NotRequired["OwnerTypeDef"],
        "Initiator": NotRequired["InitiatorTypeDef"],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": NotRequired[int],
        "NewerNoncurrentVersions": NotRequired[int],
    },
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": NotRequired[int],
        "StorageClass": NotRequired[TransitionStorageClassType],
        "NewerNoncurrentVersions": NotRequired[int],
    },
)

NotificationConfigurationDeprecatedResponseMetadataTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedResponseMetadataTypeDef",
    {
        "TopicConfiguration": "TopicConfigurationDeprecatedTypeDef",
        "QueueConfiguration": "QueueConfigurationDeprecatedTypeDef",
        "CloudFunctionConfiguration": "CloudFunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationConfigurationDeprecatedTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedTypeDef",
    {
        "TopicConfiguration": NotRequired["TopicConfigurationDeprecatedTypeDef"],
        "QueueConfiguration": NotRequired["QueueConfigurationDeprecatedTypeDef"],
        "CloudFunctionConfiguration": NotRequired["CloudFunctionConfigurationTypeDef"],
    },
)

NotificationConfigurationFilterTypeDef = TypedDict(
    "NotificationConfigurationFilterTypeDef",
    {
        "Key": NotRequired["S3KeyFilterTypeDef"],
    },
)

NotificationConfigurationResponseMetadataTypeDef = TypedDict(
    "NotificationConfigurationResponseMetadataTypeDef",
    {
        "TopicConfigurations": List["TopicConfigurationTypeDef"],
        "QueueConfigurations": List["QueueConfigurationTypeDef"],
        "LambdaFunctionConfigurations": List["LambdaFunctionConfigurationTypeDef"],
        "EventBridgeConfiguration": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicConfigurations": NotRequired[Sequence["TopicConfigurationTypeDef"]],
        "QueueConfigurations": NotRequired[Sequence["QueueConfigurationTypeDef"]],
        "LambdaFunctionConfigurations": NotRequired[Sequence["LambdaFunctionConfigurationTypeDef"]],
        "EventBridgeConfiguration": NotRequired[Mapping[str, Any]],
    },
)

ObjectCopyRequestTypeDef = TypedDict(
    "ObjectCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "SourceClient": NotRequired[BaseClient],
        "Config": NotRequired[TransferConfig],
    },
)

ObjectDownloadFileRequestTypeDef = TypedDict(
    "ObjectDownloadFileRequestTypeDef",
    {
        "Filename": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ObjectDownloadFileobjRequestTypeDef = TypedDict(
    "ObjectDownloadFileobjRequestTypeDef",
    {
        "Fileobj": Union[IO[Any], StreamingBody],
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ObjectIdentifierTypeDef = TypedDict(
    "ObjectIdentifierTypeDef",
    {
        "Key": str,
        "VersionId": NotRequired[str],
    },
)

ObjectLockConfigurationTypeDef = TypedDict(
    "ObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": NotRequired[Literal["Enabled"]],
        "Rule": NotRequired["ObjectLockRuleTypeDef"],
    },
)

ObjectLockLegalHoldTypeDef = TypedDict(
    "ObjectLockLegalHoldTypeDef",
    {
        "Status": NotRequired[ObjectLockLegalHoldStatusType],
    },
)

ObjectLockRetentionTypeDef = TypedDict(
    "ObjectLockRetentionTypeDef",
    {
        "Mode": NotRequired[ObjectLockRetentionModeType],
        "RetainUntilDate": NotRequired[datetime],
    },
)

ObjectLockRuleTypeDef = TypedDict(
    "ObjectLockRuleTypeDef",
    {
        "DefaultRetention": NotRequired["DefaultRetentionTypeDef"],
    },
)

ObjectMultipartUploadRequestTypeDef = TypedDict(
    "ObjectMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

ObjectPartTypeDef = TypedDict(
    "ObjectPartTypeDef",
    {
        "PartNumber": NotRequired[int],
        "Size": NotRequired[int],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
    },
)

ObjectSummaryMultipartUploadRequestTypeDef = TypedDict(
    "ObjectSummaryMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

ObjectSummaryVersionRequestTypeDef = TypedDict(
    "ObjectSummaryVersionRequestTypeDef",
    {
        "id": str,
    },
)

ObjectTypeDef = TypedDict(
    "ObjectTypeDef",
    {
        "Key": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "ETag": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[List[ChecksumAlgorithmType]],
        "Size": NotRequired[int],
        "StorageClass": NotRequired[ObjectStorageClassType],
        "Owner": NotRequired["OwnerTypeDef"],
    },
)

ObjectUploadFileRequestTypeDef = TypedDict(
    "ObjectUploadFileRequestTypeDef",
    {
        "Filename": str,
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ObjectUploadFileobjRequestTypeDef = TypedDict(
    "ObjectUploadFileobjRequestTypeDef",
    {
        "Fileobj": Union[IO[Any], StreamingBody],
        "ExtraArgs": NotRequired[Dict[str, Any]],
        "Callback": NotRequired[Callable[..., Any]],
        "Config": NotRequired[TransferConfig],
    },
)

ObjectVersionRequestTypeDef = TypedDict(
    "ObjectVersionRequestTypeDef",
    {
        "id": str,
    },
)

ObjectVersionTypeDef = TypedDict(
    "ObjectVersionTypeDef",
    {
        "ETag": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[List[ChecksumAlgorithmType]],
        "Size": NotRequired[int],
        "StorageClass": NotRequired[Literal["STANDARD"]],
        "Key": NotRequired[str],
        "VersionId": NotRequired[str],
        "IsLatest": NotRequired[bool],
        "LastModified": NotRequired[datetime],
        "Owner": NotRequired["OwnerTypeDef"],
    },
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "S3": NotRequired["S3LocationTypeDef"],
    },
)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {
        "CSV": NotRequired["CSVOutputTypeDef"],
        "JSON": NotRequired["JSONOutputTypeDef"],
    },
)

OwnerResponseMetadataTypeDef = TypedDict(
    "OwnerResponseMetadataTypeDef",
    {
        "DisplayName": str,
        "ID": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "DisplayName": NotRequired[str],
        "ID": NotRequired[str],
    },
)

OwnershipControlsRuleTypeDef = TypedDict(
    "OwnershipControlsRuleTypeDef",
    {
        "ObjectOwnership": ObjectOwnershipType,
    },
)

OwnershipControlsTypeDef = TypedDict(
    "OwnershipControlsTypeDef",
    {
        "Rules": List["OwnershipControlsRuleTypeDef"],
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

PartTypeDef = TypedDict(
    "PartTypeDef",
    {
        "PartNumber": NotRequired[int],
        "LastModified": NotRequired[datetime],
        "ETag": NotRequired[str],
        "Size": NotRequired[int],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
    },
)

PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": NotRequired[bool],
    },
)

ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef",
    {
        "Details": NotRequired["ProgressTypeDef"],
    },
)

ProgressTypeDef = TypedDict(
    "ProgressTypeDef",
    {
        "BytesScanned": NotRequired[int],
        "BytesProcessed": NotRequired[int],
        "BytesReturned": NotRequired[int],
    },
)

PublicAccessBlockConfigurationTypeDef = TypedDict(
    "PublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": NotRequired[bool],
        "IgnorePublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
    },
)

PutBucketAccelerateConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketAccelerateConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "AccelerateConfiguration": "AccelerateConfigurationTypeDef",
        "ExpectedBucketOwner": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
    },
)

PutBucketAclRequestBucketAclPutTypeDef = TypedDict(
    "PutBucketAclRequestBucketAclPutTypeDef",
    {
        "ACL": NotRequired[BucketCannedACLType],
        "AccessControlPolicy": NotRequired["AccessControlPolicyTypeDef"],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketAclRequestRequestTypeDef = TypedDict(
    "PutBucketAclRequestRequestTypeDef",
    {
        "Bucket": str,
        "ACL": NotRequired[BucketCannedACLType],
        "AccessControlPolicy": NotRequired["AccessControlPolicyTypeDef"],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketAnalyticsConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketAnalyticsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketCorsRequestBucketCorsPutTypeDef = TypedDict(
    "PutBucketCorsRequestBucketCorsPutTypeDef",
    {
        "CORSConfiguration": "CORSConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketCorsRequestRequestTypeDef = TypedDict(
    "PutBucketCorsRequestRequestTypeDef",
    {
        "Bucket": str,
        "CORSConfiguration": "CORSConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketEncryptionRequestRequestTypeDef = TypedDict(
    "PutBucketEncryptionRequestRequestTypeDef",
    {
        "Bucket": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketIntelligentTieringConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketIntelligentTieringConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
    },
)

PutBucketInventoryConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketInventoryConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef = TypedDict(
    "PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationPutTypeDef",
    {
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "LifecycleConfiguration": NotRequired["BucketLifecycleConfigurationTypeDef"],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "LifecycleConfiguration": NotRequired["BucketLifecycleConfigurationTypeDef"],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketLifecycleRequestBucketLifecyclePutTypeDef = TypedDict(
    "PutBucketLifecycleRequestBucketLifecyclePutTypeDef",
    {
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "LifecycleConfiguration": NotRequired["LifecycleConfigurationTypeDef"],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketLifecycleRequestRequestTypeDef = TypedDict(
    "PutBucketLifecycleRequestRequestTypeDef",
    {
        "Bucket": str,
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "LifecycleConfiguration": NotRequired["LifecycleConfigurationTypeDef"],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketLoggingRequestBucketLoggingPutTypeDef = TypedDict(
    "PutBucketLoggingRequestBucketLoggingPutTypeDef",
    {
        "BucketLoggingStatus": "BucketLoggingStatusTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketLoggingRequestRequestTypeDef = TypedDict(
    "PutBucketLoggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "BucketLoggingStatus": "BucketLoggingStatusTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketMetricsConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketMetricsConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef = TypedDict(
    "PutBucketNotificationConfigurationRequestBucketNotificationPutTypeDef",
    {
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "ExpectedBucketOwner": NotRequired[str],
        "SkipDestinationValidation": NotRequired[bool],
    },
)

PutBucketNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketNotificationConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "ExpectedBucketOwner": NotRequired[str],
        "SkipDestinationValidation": NotRequired[bool],
    },
)

PutBucketNotificationRequestRequestTypeDef = TypedDict(
    "PutBucketNotificationRequestRequestTypeDef",
    {
        "Bucket": str,
        "NotificationConfiguration": "NotificationConfigurationDeprecatedTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketOwnershipControlsRequestRequestTypeDef = TypedDict(
    "PutBucketOwnershipControlsRequestRequestTypeDef",
    {
        "Bucket": str,
        "OwnershipControls": "OwnershipControlsTypeDef",
        "ContentMD5": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketPolicyRequestBucketPolicyPutTypeDef = TypedDict(
    "PutBucketPolicyRequestBucketPolicyPutTypeDef",
    {
        "Policy": str,
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ConfirmRemoveSelfBucketAccess": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketPolicyRequestRequestTypeDef = TypedDict(
    "PutBucketPolicyRequestRequestTypeDef",
    {
        "Bucket": str,
        "Policy": str,
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ConfirmRemoveSelfBucketAccess": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketReplicationRequestRequestTypeDef = TypedDict(
    "PutBucketReplicationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "Token": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef = TypedDict(
    "PutBucketRequestPaymentRequestBucketRequestPaymentPutTypeDef",
    {
        "RequestPaymentConfiguration": "RequestPaymentConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketRequestPaymentRequestRequestTypeDef = TypedDict(
    "PutBucketRequestPaymentRequestRequestTypeDef",
    {
        "Bucket": str,
        "RequestPaymentConfiguration": "RequestPaymentConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketTaggingRequestBucketTaggingPutTypeDef = TypedDict(
    "PutBucketTaggingRequestBucketTaggingPutTypeDef",
    {
        "Tagging": "TaggingTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketTaggingRequestRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketVersioningRequestBucketVersioningEnableTypeDef = TypedDict(
    "PutBucketVersioningRequestBucketVersioningEnableTypeDef",
    {
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "MFA": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketVersioningRequestBucketVersioningPutTypeDef = TypedDict(
    "PutBucketVersioningRequestBucketVersioningPutTypeDef",
    {
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "MFA": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketVersioningRequestBucketVersioningSuspendTypeDef = TypedDict(
    "PutBucketVersioningRequestBucketVersioningSuspendTypeDef",
    {
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "MFA": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketVersioningRequestRequestTypeDef = TypedDict(
    "PutBucketVersioningRequestRequestTypeDef",
    {
        "Bucket": str,
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "MFA": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketWebsiteRequestBucketWebsitePutTypeDef = TypedDict(
    "PutBucketWebsiteRequestBucketWebsitePutTypeDef",
    {
        "WebsiteConfiguration": "WebsiteConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutBucketWebsiteRequestRequestTypeDef = TypedDict(
    "PutBucketWebsiteRequestRequestTypeDef",
    {
        "Bucket": str,
        "WebsiteConfiguration": "WebsiteConfigurationTypeDef",
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectAclOutputTypeDef = TypedDict(
    "PutObjectAclOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectAclRequestObjectAclPutTypeDef = TypedDict(
    "PutObjectAclRequestObjectAclPutTypeDef",
    {
        "ACL": NotRequired[ObjectCannedACLType],
        "AccessControlPolicy": NotRequired["AccessControlPolicyTypeDef"],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "VersionId": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectAclRequestRequestTypeDef = TypedDict(
    "PutObjectAclRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "AccessControlPolicy": NotRequired["AccessControlPolicyTypeDef"],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "VersionId": NotRequired[str],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectLegalHoldOutputTypeDef = TypedDict(
    "PutObjectLegalHoldOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectLegalHoldRequestRequestTypeDef = TypedDict(
    "PutObjectLegalHoldRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "LegalHold": NotRequired["ObjectLockLegalHoldTypeDef"],
        "RequestPayer": NotRequired[Literal["requester"]],
        "VersionId": NotRequired[str],
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectLockConfigurationOutputTypeDef = TypedDict(
    "PutObjectLockConfigurationOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectLockConfigurationRequestRequestTypeDef = TypedDict(
    "PutObjectLockConfigurationRequestRequestTypeDef",
    {
        "Bucket": str,
        "ObjectLockConfiguration": NotRequired["ObjectLockConfigurationTypeDef"],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Token": NotRequired[str],
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectOutputTypeDef = TypedDict(
    "PutObjectOutputTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ChecksumCRC32": str,
        "ChecksumCRC32C": str,
        "ChecksumSHA1": str,
        "ChecksumSHA256": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectRequestBucketPutObjectTypeDef = TypedDict(
    "PutObjectRequestBucketPutObjectTypeDef",
    {
        "Key": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectRequestObjectPutTypeDef = TypedDict(
    "PutObjectRequestObjectPutTypeDef",
    {
        "ACL": NotRequired[ObjectCannedACLType],
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectRequestObjectSummaryPutTypeDef = TypedDict(
    "PutObjectRequestObjectSummaryPutTypeDef",
    {
        "ACL": NotRequired[ObjectCannedACLType],
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectRequestRequestTypeDef = TypedDict(
    "PutObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "ACL": NotRequired[ObjectCannedACLType],
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "Metadata": NotRequired[Mapping[str, str]],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "StorageClass": NotRequired[StorageClassType],
        "WebsiteRedirectLocation": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSEKMSEncryptionContext": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
        "RequestPayer": NotRequired[Literal["requester"]],
        "Tagging": NotRequired[str],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectRetentionOutputTypeDef = TypedDict(
    "PutObjectRetentionOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectRetentionRequestRequestTypeDef = TypedDict(
    "PutObjectRetentionRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Retention": NotRequired["ObjectLockRetentionTypeDef"],
        "RequestPayer": NotRequired[Literal["requester"]],
        "VersionId": NotRequired[str],
        "BypassGovernanceRetention": NotRequired[bool],
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

PutObjectTaggingOutputTypeDef = TypedDict(
    "PutObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectTaggingRequestRequestTypeDef = TypedDict(
    "PutObjectTaggingRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Tagging": "TaggingTypeDef",
        "VersionId": NotRequired[str],
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
    },
)

PutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "PutPublicAccessBlockRequestRequestTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

QueueConfigurationDeprecatedTypeDef = TypedDict(
    "QueueConfigurationDeprecatedTypeDef",
    {
        "Id": NotRequired[str],
        "Event": NotRequired[EventType],
        "Events": NotRequired[List[EventType]],
        "Queue": NotRequired[str],
    },
)

QueueConfigurationTypeDef = TypedDict(
    "QueueConfigurationTypeDef",
    {
        "QueueArn": str,
        "Events": List[EventType],
        "Id": NotRequired[str],
        "Filter": NotRequired["NotificationConfigurationFilterTypeDef"],
    },
)

RecordsEventTypeDef = TypedDict(
    "RecordsEventTypeDef",
    {
        "Payload": NotRequired[bytes],
    },
)

RedirectAllRequestsToResponseMetadataTypeDef = TypedDict(
    "RedirectAllRequestsToResponseMetadataTypeDef",
    {
        "HostName": str,
        "Protocol": ProtocolType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedirectAllRequestsToTypeDef = TypedDict(
    "RedirectAllRequestsToTypeDef",
    {
        "HostName": str,
        "Protocol": NotRequired[ProtocolType],
    },
)

RedirectTypeDef = TypedDict(
    "RedirectTypeDef",
    {
        "HostName": NotRequired[str],
        "HttpRedirectCode": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "ReplaceKeyPrefixWith": NotRequired[str],
        "ReplaceKeyWith": NotRequired[str],
    },
)

ReplicaModificationsTypeDef = TypedDict(
    "ReplicaModificationsTypeDef",
    {
        "Status": ReplicaModificationsStatusType,
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List["ReplicationRuleTypeDef"],
    },
)

ReplicationRuleAndOperatorTypeDef = TypedDict(
    "ReplicationRuleAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired["TagTypeDef"],
        "And": NotRequired["ReplicationRuleAndOperatorTypeDef"],
    },
)

ReplicationRuleTypeDef = TypedDict(
    "ReplicationRuleTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": "DestinationTypeDef",
        "ID": NotRequired[str],
        "Priority": NotRequired[int],
        "Prefix": NotRequired[str],
        "Filter": NotRequired["ReplicationRuleFilterTypeDef"],
        "SourceSelectionCriteria": NotRequired["SourceSelectionCriteriaTypeDef"],
        "ExistingObjectReplication": NotRequired["ExistingObjectReplicationTypeDef"],
        "DeleteMarkerReplication": NotRequired["DeleteMarkerReplicationTypeDef"],
    },
)

ReplicationTimeTypeDef = TypedDict(
    "ReplicationTimeTypeDef",
    {
        "Status": ReplicationTimeStatusType,
        "Time": "ReplicationTimeValueTypeDef",
    },
)

ReplicationTimeValueTypeDef = TypedDict(
    "ReplicationTimeValueTypeDef",
    {
        "Minutes": NotRequired[int],
    },
)

RequestPaymentConfigurationTypeDef = TypedDict(
    "RequestPaymentConfigurationTypeDef",
    {
        "Payer": PayerType,
    },
)

RequestProgressTypeDef = TypedDict(
    "RequestProgressTypeDef",
    {
        "Enabled": NotRequired[bool],
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

RestoreObjectOutputTypeDef = TypedDict(
    "RestoreObjectOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "RestoreOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreObjectRequestObjectRestoreObjectTypeDef = TypedDict(
    "RestoreObjectRequestObjectRestoreObjectTypeDef",
    {
        "VersionId": NotRequired[str],
        "RestoreRequest": NotRequired["RestoreRequestTypeDef"],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

RestoreObjectRequestObjectSummaryRestoreObjectTypeDef = TypedDict(
    "RestoreObjectRequestObjectSummaryRestoreObjectTypeDef",
    {
        "VersionId": NotRequired[str],
        "RestoreRequest": NotRequired["RestoreRequestTypeDef"],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

RestoreObjectRequestRequestTypeDef = TypedDict(
    "RestoreObjectRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
        "RestoreRequest": NotRequired["RestoreRequestTypeDef"],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

RestoreRequestTypeDef = TypedDict(
    "RestoreRequestTypeDef",
    {
        "Days": NotRequired[int],
        "GlacierJobParameters": NotRequired["GlacierJobParametersTypeDef"],
        "Type": NotRequired[Literal["SELECT"]],
        "Tier": NotRequired[TierType],
        "Description": NotRequired[str],
        "SelectParameters": NotRequired["SelectParametersTypeDef"],
        "OutputLocation": NotRequired["OutputLocationTypeDef"],
    },
)

RoutingRuleTypeDef = TypedDict(
    "RoutingRuleTypeDef",
    {
        "Redirect": "RedirectTypeDef",
        "Condition": NotRequired["ConditionTypeDef"],
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Prefix": str,
        "Status": ExpirationStatusType,
        "Expiration": NotRequired["LifecycleExpirationTypeDef"],
        "ID": NotRequired[str],
        "Transition": NotRequired["TransitionTypeDef"],
        "NoncurrentVersionTransition": NotRequired["NoncurrentVersionTransitionTypeDef"],
        "NoncurrentVersionExpiration": NotRequired["NoncurrentVersionExpirationTypeDef"],
        "AbortIncompleteMultipartUpload": NotRequired["AbortIncompleteMultipartUploadTypeDef"],
    },
)

S3KeyFilterTypeDef = TypedDict(
    "S3KeyFilterTypeDef",
    {
        "FilterRules": NotRequired[List["FilterRuleTypeDef"]],
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": NotRequired["EncryptionTypeDef"],
        "CannedACL": NotRequired[ObjectCannedACLType],
        "AccessControlList": NotRequired[Sequence["GrantTypeDef"]],
        "Tagging": NotRequired["TaggingTypeDef"],
        "UserMetadata": NotRequired[Sequence["MetadataEntryTypeDef"]],
        "StorageClass": NotRequired[StorageClassType],
    },
)

SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

ScanRangeTypeDef = TypedDict(
    "ScanRangeTypeDef",
    {
        "Start": NotRequired[int],
        "End": NotRequired[int],
    },
)

SelectObjectContentEventStreamTypeDef = TypedDict(
    "SelectObjectContentEventStreamTypeDef",
    {
        "Records": NotRequired["RecordsEventTypeDef"],
        "Stats": NotRequired["StatsEventTypeDef"],
        "Progress": NotRequired["ProgressEventTypeDef"],
        "Cont": NotRequired[Dict[str, Any]],
        "End": NotRequired[Dict[str, Any]],
    },
)

SelectObjectContentOutputTypeDef = TypedDict(
    "SelectObjectContentOutputTypeDef",
    {
        "Payload": "SelectObjectContentEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SelectObjectContentRequestRequestTypeDef = TypedDict(
    "SelectObjectContentRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Expression": str,
        "ExpressionType": Literal["SQL"],
        "InputSerialization": "InputSerializationTypeDef",
        "OutputSerialization": "OutputSerializationTypeDef",
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestProgress": NotRequired["RequestProgressTypeDef"],
        "ScanRange": NotRequired["ScanRangeTypeDef"],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
    },
)

ServerSideEncryptionByDefaultTypeDef = TypedDict(
    "ServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": ServerSideEncryptionType,
        "KMSMasterKeyID": NotRequired[str],
    },
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": List["ServerSideEncryptionRuleTypeDef"],
    },
)

ServerSideEncryptionRuleTypeDef = TypedDict(
    "ServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": NotRequired["ServerSideEncryptionByDefaultTypeDef"],
        "BucketKeyEnabled": NotRequired[bool],
    },
)

ServiceResourceBucketAclRequestTypeDef = TypedDict(
    "ServiceResourceBucketAclRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketCorsRequestTypeDef = TypedDict(
    "ServiceResourceBucketCorsRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "ServiceResourceBucketLifecycleConfigurationRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLifecycleRequestTypeDef = TypedDict(
    "ServiceResourceBucketLifecycleRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLoggingRequestTypeDef = TypedDict(
    "ServiceResourceBucketLoggingRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketNotificationRequestTypeDef = TypedDict(
    "ServiceResourceBucketNotificationRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketPolicyRequestTypeDef = TypedDict(
    "ServiceResourceBucketPolicyRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketRequestPaymentRequestTypeDef = TypedDict(
    "ServiceResourceBucketRequestPaymentRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketRequestTypeDef = TypedDict(
    "ServiceResourceBucketRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceBucketTaggingRequestTypeDef = TypedDict(
    "ServiceResourceBucketTaggingRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketVersioningRequestTypeDef = TypedDict(
    "ServiceResourceBucketVersioningRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketWebsiteRequestTypeDef = TypedDict(
    "ServiceResourceBucketWebsiteRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceMultipartUploadPartRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadPartRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "multipart_upload_id": str,
        "part_number": str,
    },
)

ServiceResourceMultipartUploadRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "id": str,
    },
)

ServiceResourceObjectAclRequestTypeDef = TypedDict(
    "ServiceResourceObjectAclRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
    },
)

ServiceResourceObjectRequestTypeDef = TypedDict(
    "ServiceResourceObjectRequestTypeDef",
    {
        "bucket_name": str,
        "key": str,
    },
)

ServiceResourceObjectSummaryRequestTypeDef = TypedDict(
    "ServiceResourceObjectSummaryRequestTypeDef",
    {
        "bucket_name": str,
        "key": str,
    },
)

ServiceResourceObjectVersionRequestTypeDef = TypedDict(
    "ServiceResourceObjectVersionRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "id": str,
    },
)

SourceSelectionCriteriaTypeDef = TypedDict(
    "SourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": NotRequired["SseKmsEncryptedObjectsTypeDef"],
        "ReplicaModifications": NotRequired["ReplicaModificationsTypeDef"],
    },
)

SseKmsEncryptedObjectsTypeDef = TypedDict(
    "SseKmsEncryptedObjectsTypeDef",
    {
        "Status": SseKmsEncryptedObjectsStatusType,
    },
)

StatsEventTypeDef = TypedDict(
    "StatsEventTypeDef",
    {
        "Details": NotRequired["StatsTypeDef"],
    },
)

StatsTypeDef = TypedDict(
    "StatsTypeDef",
    {
        "BytesScanned": NotRequired[int],
        "BytesProcessed": NotRequired[int],
        "BytesReturned": NotRequired[int],
    },
)

StorageClassAnalysisDataExportTypeDef = TypedDict(
    "StorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": Literal["V_1"],
        "Destination": "AnalyticsExportDestinationTypeDef",
    },
)

StorageClassAnalysisTypeDef = TypedDict(
    "StorageClassAnalysisTypeDef",
    {
        "DataExport": NotRequired["StorageClassAnalysisDataExportTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": Sequence["TagTypeDef"],
    },
)

TargetGrantTypeDef = TypedDict(
    "TargetGrantTypeDef",
    {
        "Grantee": NotRequired["GranteeTypeDef"],
        "Permission": NotRequired[BucketLogsPermissionType],
    },
)

TieringTypeDef = TypedDict(
    "TieringTypeDef",
    {
        "Days": int,
        "AccessTier": IntelligentTieringAccessTierType,
    },
)

TopicConfigurationDeprecatedTypeDef = TypedDict(
    "TopicConfigurationDeprecatedTypeDef",
    {
        "Id": NotRequired[str],
        "Events": NotRequired[List[EventType]],
        "Event": NotRequired[EventType],
        "Topic": NotRequired[str],
    },
)

TopicConfigurationTypeDef = TypedDict(
    "TopicConfigurationTypeDef",
    {
        "TopicArn": str,
        "Events": List[EventType],
        "Id": NotRequired[str],
        "Filter": NotRequired["NotificationConfigurationFilterTypeDef"],
    },
)

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": NotRequired[datetime],
        "Days": NotRequired[int],
        "StorageClass": NotRequired[TransitionStorageClassType],
    },
)

UploadPartCopyOutputTypeDef = TypedDict(
    "UploadPartCopyOutputTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": "CopyPartResultTypeDef",
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef = TypedDict(
    "UploadPartCopyRequestMultipartUploadPartCopyFromTypeDef",
    {
        "CopySource": str,
        "CopySourceIfMatch": NotRequired[str],
        "CopySourceIfModifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceIfNoneMatch": NotRequired[str],
        "CopySourceIfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceRange": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "CopySourceSSECustomerAlgorithm": NotRequired[str],
        "CopySourceSSECustomerKey": NotRequired[str],
        "CopySourceSSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
        "ExpectedSourceBucketOwner": NotRequired[str],
    },
)

UploadPartCopyRequestRequestTypeDef = TypedDict(
    "UploadPartCopyRequestRequestTypeDef",
    {
        "Bucket": str,
        "CopySource": Union[str, "CopySourceTypeDef"],
        "Key": str,
        "PartNumber": int,
        "UploadId": str,
        "CopySourceIfMatch": NotRequired[str],
        "CopySourceIfModifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceIfNoneMatch": NotRequired[str],
        "CopySourceIfUnmodifiedSince": NotRequired[Union[datetime, str]],
        "CopySourceRange": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "CopySourceSSECustomerAlgorithm": NotRequired[str],
        "CopySourceSSECustomerKey": NotRequired[str],
        "CopySourceSSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
        "ExpectedSourceBucketOwner": NotRequired[str],
    },
)

UploadPartOutputTypeDef = TypedDict(
    "UploadPartOutputTypeDef",
    {
        "ServerSideEncryption": ServerSideEncryptionType,
        "ETag": str,
        "ChecksumCRC32": str,
        "ChecksumCRC32C": str,
        "ChecksumSHA1": str,
        "ChecksumSHA256": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadPartRequestMultipartUploadPartUploadTypeDef = TypedDict(
    "UploadPartRequestMultipartUploadPartUploadTypeDef",
    {
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

UploadPartRequestRequestTypeDef = TypedDict(
    "UploadPartRequestRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "PartNumber": int,
        "UploadId": str,
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[ChecksumAlgorithmType],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSECustomerKey": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "RequestPayer": NotRequired[Literal["requester"]],
        "ExpectedBucketOwner": NotRequired[str],
    },
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "MFADelete": NotRequired[MFADeleteType],
        "Status": NotRequired[BucketVersioningStatusType],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WebsiteConfigurationTypeDef = TypedDict(
    "WebsiteConfigurationTypeDef",
    {
        "ErrorDocument": NotRequired["ErrorDocumentTypeDef"],
        "IndexDocument": NotRequired["IndexDocumentTypeDef"],
        "RedirectAllRequestsTo": NotRequired["RedirectAllRequestsToTypeDef"],
        "RoutingRules": NotRequired[Sequence["RoutingRuleTypeDef"]],
    },
)

WriteGetObjectResponseRequestRequestTypeDef = TypedDict(
    "WriteGetObjectResponseRequestRequestTypeDef",
    {
        "RequestRoute": str,
        "RequestToken": str,
        "Body": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "StatusCode": NotRequired[int],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "AcceptRanges": NotRequired[str],
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "ContentLength": NotRequired[int],
        "ContentRange": NotRequired[str],
        "ContentType": NotRequired[str],
        "ChecksumCRC32": NotRequired[str],
        "ChecksumCRC32C": NotRequired[str],
        "ChecksumSHA1": NotRequired[str],
        "ChecksumSHA256": NotRequired[str],
        "DeleteMarker": NotRequired[bool],
        "ETag": NotRequired[str],
        "Expires": NotRequired[Union[datetime, str]],
        "Expiration": NotRequired[str],
        "LastModified": NotRequired[Union[datetime, str]],
        "MissingMeta": NotRequired[int],
        "Metadata": NotRequired[Mapping[str, str]],
        "ObjectLockMode": NotRequired[ObjectLockModeType],
        "ObjectLockLegalHoldStatus": NotRequired[ObjectLockLegalHoldStatusType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "PartsCount": NotRequired[int],
        "ReplicationStatus": NotRequired[ReplicationStatusType],
        "RequestCharged": NotRequired[Literal["requester"]],
        "Restore": NotRequired[str],
        "ServerSideEncryption": NotRequired[ServerSideEncryptionType],
        "SSECustomerAlgorithm": NotRequired[str],
        "SSEKMSKeyId": NotRequired[str],
        "SSECustomerKeyMD5": NotRequired[str],
        "StorageClass": NotRequired[StorageClassType],
        "TagCount": NotRequired[int],
        "VersionId": NotRequired[str],
        "BucketKeyEnabled": NotRequired[bool],
    },
)
