"""
Type annotations for s3control service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AsyncOperationNameType,
    BucketCannedACLType,
    BucketLocationConstraintType,
    ExpirationStatusType,
    FormatType,
    JobManifestFieldNameType,
    JobManifestFormatType,
    JobReportScopeType,
    JobStatusType,
    MultiRegionAccessPointStatusType,
    NetworkOriginType,
    ObjectLambdaAllowedFeatureType,
    OperationNameType,
    ReplicationStatusType,
    RequestedJobStatusType,
    S3CannedAccessControlListType,
    S3ChecksumAlgorithmType,
    S3GlacierJobTierType,
    S3GranteeTypeIdentifierType,
    S3MetadataDirectiveType,
    S3ObjectLockLegalHoldStatusType,
    S3ObjectLockModeType,
    S3ObjectLockRetentionModeType,
    S3PermissionType,
    S3SSEAlgorithmType,
    S3StorageClassType,
    TransitionStorageClassType,
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
    "AccessPointTypeDef",
    "AccountLevelTypeDef",
    "ActivityMetricsTypeDef",
    "AsyncErrorDetailsTypeDef",
    "AsyncOperationTypeDef",
    "AsyncRequestParametersTypeDef",
    "AsyncResponseDetailsTypeDef",
    "AwsLambdaTransformationTypeDef",
    "BucketLevelTypeDef",
    "CloudWatchMetricsTypeDef",
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResultTypeDef",
    "CreateMultiRegionAccessPointInputTypeDef",
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    "CreateMultiRegionAccessPointResultTypeDef",
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteJobTaggingRequestRequestTypeDef",
    "DeleteMultiRegionAccessPointInputTypeDef",
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    "DeleteMultiRegionAccessPointResultTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    "ExcludeTypeDef",
    "GeneratedManifestEncryptionTypeDef",
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyRequestRequestTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetAccessPointRequestRequestTypeDef",
    "GetAccessPointResultTypeDef",
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "GetBucketPolicyRequestRequestTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketRequestRequestTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetJobTaggingRequestRequestTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    "GetMultiRegionAccessPointResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GetStorageLensConfigurationRequestRequestTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "IncludeTypeDef",
    "JobDescriptorTypeDef",
    "JobFailureTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestGeneratorFilterTypeDef",
    "JobManifestGeneratorTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecTypeDef",
    "JobManifestTypeDef",
    "JobOperationTypeDef",
    "JobProgressSummaryTypeDef",
    "JobReportTypeDef",
    "JobTimersTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "ListAccessPointsRequestRequestTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListMultiRegionAccessPointsRequestRequestTypeDef",
    "ListMultiRegionAccessPointsResultTypeDef",
    "ListRegionalBucketsRequestRequestTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    "MultiRegionAccessPointRegionalResponseTypeDef",
    "MultiRegionAccessPointReportTypeDef",
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyStatusTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PrefixLevelTypeDef",
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyRequestRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "PutJobTaggingRequestRequestTypeDef",
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "PutStorageLensConfigurationRequestRequestTypeDef",
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    "RegionReportTypeDef",
    "RegionTypeDef",
    "RegionalBucketTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3GeneratedManifestDescriptorTypeDef",
    "S3GrantTypeDef",
    "S3GranteeTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "S3JobManifestGeneratorTypeDef",
    "S3ManifestOutputLocationTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3RetentionTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "S3TagTypeDef",
    "SSEKMSEncryptionTypeDef",
    "SSEKMSTypeDef",
    "SelectionCriteriaTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensConfigurationTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "StorageLensDataExportTypeDef",
    "StorageLensTagTypeDef",
    "TaggingTypeDef",
    "TransitionTypeDef",
    "UpdateJobPriorityRequestRequestTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusRequestRequestTypeDef",
    "UpdateJobStatusResultTypeDef",
    "VpcConfigurationTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": NotRequired[int],
    },
)

AccessPointTypeDef = TypedDict(
    "AccessPointTypeDef",
    {
        "Name": str,
        "NetworkOrigin": NetworkOriginType,
        "Bucket": str,
        "VpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
        "AccessPointArn": NotRequired[str],
        "Alias": NotRequired[str],
    },
)

AccountLevelTypeDef = TypedDict(
    "AccountLevelTypeDef",
    {
        "BucketLevel": "BucketLevelTypeDef",
        "ActivityMetrics": NotRequired["ActivityMetricsTypeDef"],
    },
)

ActivityMetricsTypeDef = TypedDict(
    "ActivityMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
    },
)

AsyncErrorDetailsTypeDef = TypedDict(
    "AsyncErrorDetailsTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
        "Resource": NotRequired[str],
        "RequestId": NotRequired[str],
    },
)

AsyncOperationTypeDef = TypedDict(
    "AsyncOperationTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "Operation": NotRequired[AsyncOperationNameType],
        "RequestTokenARN": NotRequired[str],
        "RequestParameters": NotRequired["AsyncRequestParametersTypeDef"],
        "RequestStatus": NotRequired[str],
        "ResponseDetails": NotRequired["AsyncResponseDetailsTypeDef"],
    },
)

AsyncRequestParametersTypeDef = TypedDict(
    "AsyncRequestParametersTypeDef",
    {
        "CreateMultiRegionAccessPointRequest": NotRequired[
            "CreateMultiRegionAccessPointInputTypeDef"
        ],
        "DeleteMultiRegionAccessPointRequest": NotRequired[
            "DeleteMultiRegionAccessPointInputTypeDef"
        ],
        "PutMultiRegionAccessPointPolicyRequest": NotRequired[
            "PutMultiRegionAccessPointPolicyInputTypeDef"
        ],
    },
)

AsyncResponseDetailsTypeDef = TypedDict(
    "AsyncResponseDetailsTypeDef",
    {
        "MultiRegionAccessPointDetails": NotRequired["MultiRegionAccessPointsAsyncResponseTypeDef"],
        "ErrorDetails": NotRequired["AsyncErrorDetailsTypeDef"],
    },
)

AwsLambdaTransformationTypeDef = TypedDict(
    "AwsLambdaTransformationTypeDef",
    {
        "FunctionArn": str,
        "FunctionPayload": NotRequired[str],
    },
)

BucketLevelTypeDef = TypedDict(
    "BucketLevelTypeDef",
    {
        "ActivityMetrics": NotRequired["ActivityMetricsTypeDef"],
        "PrefixLevel": NotRequired["PrefixLevelTypeDef"],
    },
)

CloudWatchMetricsTypeDef = TypedDict(
    "CloudWatchMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
)

CreateAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": "ObjectLambdaConfigurationTypeDef",
    },
)

CreateAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAccessPointRequestRequestTypeDef = TypedDict(
    "CreateAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Bucket": str,
        "VpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
        "PublicAccessBlockConfiguration": NotRequired["PublicAccessBlockConfigurationTypeDef"],
    },
)

CreateAccessPointResultTypeDef = TypedDict(
    "CreateAccessPointResultTypeDef",
    {
        "AccessPointArn": str,
        "Alias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": NotRequired[BucketLocationConstraintType],
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
        "OutpostId": NotRequired[str],
    },
)

CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "Location": str,
        "BucketArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "Operation": "JobOperationTypeDef",
        "Report": "JobReportTypeDef",
        "ClientRequestToken": str,
        "Priority": int,
        "RoleArn": str,
        "ConfirmationRequired": NotRequired[bool],
        "Manifest": NotRequired["JobManifestTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["S3TagTypeDef"]],
        "ManifestGenerator": NotRequired["JobManifestGeneratorTypeDef"],
    },
)

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultiRegionAccessPointInputTypeDef = TypedDict(
    "CreateMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
        "Regions": Sequence["RegionTypeDef"],
        "PublicAccessBlock": NotRequired["PublicAccessBlockConfigurationTypeDef"],
    },
)

CreateMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": "CreateMultiRegionAccessPointInputTypeDef",
    },
)

CreateMultiRegionAccessPointResultTypeDef = TypedDict(
    "CreateMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "DeleteBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "DeleteBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteJobTaggingRequestRequestTypeDef = TypedDict(
    "DeleteJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DeleteMultiRegionAccessPointInputTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
    },
)

DeleteMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": "DeleteMultiRegionAccessPointInputTypeDef",
    },
)

DeleteMultiRegionAccessPointResultTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "DeletePublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "Job": "JobDescriptorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMultiRegionAccessPointOperationRequestRequestTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    {
        "AccountId": str,
        "RequestTokenARN": str,
    },
)

DescribeMultiRegionAccessPointOperationResultTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    {
        "AsyncOperation": "AsyncOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EstablishedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)

ExcludeTypeDef = TypedDict(
    "ExcludeTypeDef",
    {
        "Buckets": NotRequired[List[str]],
        "Regions": NotRequired[List[str]],
    },
)

GeneratedManifestEncryptionTypeDef = TypedDict(
    "GeneratedManifestEncryptionTypeDef",
    {
        "SSES3": NotRequired[Mapping[str, Any]],
        "SSEKMS": NotRequired["SSEKMSEncryptionTypeDef"],
    },
)

GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointConfigurationForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    {
        "Configuration": "ObjectLambdaConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaResultTypeDef",
    {
        "Name": str,
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyResultTypeDef = TypedDict(
    "GetAccessPointPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusResultTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointRequestRequestTypeDef = TypedDict(
    "GetAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointResultTypeDef = TypedDict(
    "GetAccessPointResultTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": NetworkOriginType,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
        "Alias": str,
        "AccessPointArn": str,
        "Endpoints": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketLifecycleConfigurationResultTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationResultTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyRequestRequestTypeDef = TypedDict(
    "GetBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketPolicyResultTypeDef = TypedDict(
    "GetBucketPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketRequestRequestTypeDef = TypedDict(
    "GetBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketResultTypeDef = TypedDict(
    "GetBucketResultTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketTaggingRequestRequestTypeDef = TypedDict(
    "GetBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketTaggingResultTypeDef = TypedDict(
    "GetBucketTaggingResultTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobTaggingRequestRequestTypeDef = TypedDict(
    "GetJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

GetJobTaggingResultTypeDef = TypedDict(
    "GetJobTaggingResultTypeDef",
    {
        "Tags": List["S3TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    {
        "Policy": "MultiRegionAccessPointPolicyDocumentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    {
        "Established": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetMultiRegionAccessPointResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointResultTypeDef",
    {
        "AccessPoint": "MultiRegionAccessPointReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "AccountId": str,
    },
)

GetStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationResultTypeDef = TypedDict(
    "GetStorageLensConfigurationResultTypeDef",
    {
        "StorageLensConfiguration": "StorageLensConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationTaggingResultTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingResultTypeDef",
    {
        "Tags": List["StorageLensTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncludeTypeDef = TypedDict(
    "IncludeTypeDef",
    {
        "Buckets": NotRequired[List[str]],
        "Regions": NotRequired[List[str]],
    },
)

JobDescriptorTypeDef = TypedDict(
    "JobDescriptorTypeDef",
    {
        "JobId": NotRequired[str],
        "ConfirmationRequired": NotRequired[bool],
        "Description": NotRequired[str],
        "JobArn": NotRequired[str],
        "Status": NotRequired[JobStatusType],
        "Manifest": NotRequired["JobManifestTypeDef"],
        "Operation": NotRequired["JobOperationTypeDef"],
        "Priority": NotRequired[int],
        "ProgressSummary": NotRequired["JobProgressSummaryTypeDef"],
        "StatusUpdateReason": NotRequired[str],
        "FailureReasons": NotRequired[List["JobFailureTypeDef"]],
        "Report": NotRequired["JobReportTypeDef"],
        "CreationTime": NotRequired[datetime],
        "TerminationDate": NotRequired[datetime],
        "RoleArn": NotRequired[str],
        "SuspendedDate": NotRequired[datetime],
        "SuspendedCause": NotRequired[str],
        "ManifestGenerator": NotRequired["JobManifestGeneratorTypeDef"],
        "GeneratedManifestDescriptor": NotRequired["S3GeneratedManifestDescriptorTypeDef"],
    },
)

JobFailureTypeDef = TypedDict(
    "JobFailureTypeDef",
    {
        "FailureCode": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)

JobListDescriptorTypeDef = TypedDict(
    "JobListDescriptorTypeDef",
    {
        "JobId": NotRequired[str],
        "Description": NotRequired[str],
        "Operation": NotRequired[OperationNameType],
        "Priority": NotRequired[int],
        "Status": NotRequired[JobStatusType],
        "CreationTime": NotRequired[datetime],
        "TerminationDate": NotRequired[datetime],
        "ProgressSummary": NotRequired["JobProgressSummaryTypeDef"],
    },
)

JobManifestGeneratorFilterTypeDef = TypedDict(
    "JobManifestGeneratorFilterTypeDef",
    {
        "EligibleForReplication": NotRequired[bool],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "ObjectReplicationStatuses": NotRequired[Sequence[ReplicationStatusType]],
    },
)

JobManifestGeneratorTypeDef = TypedDict(
    "JobManifestGeneratorTypeDef",
    {
        "S3JobManifestGenerator": NotRequired["S3JobManifestGeneratorTypeDef"],
    },
)

JobManifestLocationTypeDef = TypedDict(
    "JobManifestLocationTypeDef",
    {
        "ObjectArn": str,
        "ETag": str,
        "ObjectVersionId": NotRequired[str],
    },
)

JobManifestSpecTypeDef = TypedDict(
    "JobManifestSpecTypeDef",
    {
        "Format": JobManifestFormatType,
        "Fields": NotRequired[Sequence[JobManifestFieldNameType]],
    },
)

JobManifestTypeDef = TypedDict(
    "JobManifestTypeDef",
    {
        "Spec": "JobManifestSpecTypeDef",
        "Location": "JobManifestLocationTypeDef",
    },
)

JobOperationTypeDef = TypedDict(
    "JobOperationTypeDef",
    {
        "LambdaInvoke": NotRequired["LambdaInvokeOperationTypeDef"],
        "S3PutObjectCopy": NotRequired["S3CopyObjectOperationTypeDef"],
        "S3PutObjectAcl": NotRequired["S3SetObjectAclOperationTypeDef"],
        "S3PutObjectTagging": NotRequired["S3SetObjectTaggingOperationTypeDef"],
        "S3DeleteObjectTagging": NotRequired[Mapping[str, Any]],
        "S3InitiateRestoreObject": NotRequired["S3InitiateRestoreObjectOperationTypeDef"],
        "S3PutObjectLegalHold": NotRequired["S3SetObjectLegalHoldOperationTypeDef"],
        "S3PutObjectRetention": NotRequired["S3SetObjectRetentionOperationTypeDef"],
        "S3ReplicateObject": NotRequired[Mapping[str, Any]],
    },
)

JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": NotRequired[int],
        "NumberOfTasksSucceeded": NotRequired[int],
        "NumberOfTasksFailed": NotRequired[int],
        "Timers": NotRequired["JobTimersTypeDef"],
    },
)

JobReportTypeDef = TypedDict(
    "JobReportTypeDef",
    {
        "Enabled": bool,
        "Bucket": NotRequired[str],
        "Format": NotRequired[Literal["Report_CSV_20180820"]],
        "Prefix": NotRequired[str],
        "ReportScope": NotRequired[JobReportScopeType],
    },
)

JobTimersTypeDef = TypedDict(
    "JobTimersTypeDef",
    {
        "ElapsedTimeInActiveSeconds": NotRequired[int],
    },
)

LambdaInvokeOperationTypeDef = TypedDict(
    "LambdaInvokeOperationTypeDef",
    {
        "FunctionArn": NotRequired[str],
    },
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": NotRequired[Sequence["LifecycleRuleTypeDef"]],
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
        "Tags": NotRequired[List["S3TagTypeDef"]],
    },
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired["S3TagTypeDef"],
        "And": NotRequired["LifecycleRuleAndOperatorTypeDef"],
    },
)

LifecycleRuleTypeDef = TypedDict(
    "LifecycleRuleTypeDef",
    {
        "Status": ExpirationStatusType,
        "Expiration": NotRequired["LifecycleExpirationTypeDef"],
        "ID": NotRequired[str],
        "Filter": NotRequired["LifecycleRuleFilterTypeDef"],
        "Transitions": NotRequired[List["TransitionTypeDef"]],
        "NoncurrentVersionTransitions": NotRequired[List["NoncurrentVersionTransitionTypeDef"]],
        "NoncurrentVersionExpiration": NotRequired["NoncurrentVersionExpirationTypeDef"],
        "AbortIncompleteMultipartUpload": NotRequired["AbortIncompleteMultipartUploadTypeDef"],
    },
)

ListAccessPointsForObjectLambdaRequestRequestTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAccessPointsForObjectLambdaResultTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointList": List["ObjectLambdaAccessPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccessPointsRequestRequestTypeDef = TypedDict(
    "ListAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAccessPointsResultTypeDef = TypedDict(
    "ListAccessPointsResultTypeDef",
    {
        "AccessPointList": List["AccessPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobStatuses": NotRequired[Sequence[JobStatusType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "NextToken": str,
        "Jobs": List["JobListDescriptorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultiRegionAccessPointsRequestRequestTypeDef = TypedDict(
    "ListMultiRegionAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMultiRegionAccessPointsResultTypeDef = TypedDict(
    "ListMultiRegionAccessPointsResultTypeDef",
    {
        "AccessPoints": List["MultiRegionAccessPointReportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegionalBucketsRequestRequestTypeDef = TypedDict(
    "ListRegionalBucketsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "OutpostId": NotRequired[str],
    },
)

ListRegionalBucketsResultTypeDef = TypedDict(
    "ListRegionalBucketsResultTypeDef",
    {
        "RegionalBucketList": List["RegionalBucketTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStorageLensConfigurationEntryTypeDef = TypedDict(
    "ListStorageLensConfigurationEntryTypeDef",
    {
        "Id": str,
        "StorageLensArn": str,
        "HomeRegion": str,
        "IsEnabled": NotRequired[bool],
    },
)

ListStorageLensConfigurationsRequestRequestTypeDef = TypedDict(
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
    },
)

ListStorageLensConfigurationsResultTypeDef = TypedDict(
    "ListStorageLensConfigurationsResultTypeDef",
    {
        "NextToken": str,
        "StorageLensConfigurationList": List["ListStorageLensConfigurationEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MultiRegionAccessPointPolicyDocumentTypeDef = TypedDict(
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    {
        "Established": NotRequired["EstablishedMultiRegionAccessPointPolicyTypeDef"],
        "Proposed": NotRequired["ProposedMultiRegionAccessPointPolicyTypeDef"],
    },
)

MultiRegionAccessPointRegionalResponseTypeDef = TypedDict(
    "MultiRegionAccessPointRegionalResponseTypeDef",
    {
        "Name": NotRequired[str],
        "RequestStatus": NotRequired[str],
    },
)

MultiRegionAccessPointReportTypeDef = TypedDict(
    "MultiRegionAccessPointReportTypeDef",
    {
        "Name": NotRequired[str],
        "Alias": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "PublicAccessBlock": NotRequired["PublicAccessBlockConfigurationTypeDef"],
        "Status": NotRequired[MultiRegionAccessPointStatusType],
        "Regions": NotRequired[List["RegionReportTypeDef"]],
    },
)

MultiRegionAccessPointsAsyncResponseTypeDef = TypedDict(
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    {
        "Regions": NotRequired[List["MultiRegionAccessPointRegionalResponseTypeDef"]],
    },
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": NotRequired[int],
    },
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": NotRequired[int],
        "StorageClass": NotRequired[TransitionStorageClassType],
    },
)

ObjectLambdaAccessPointTypeDef = TypedDict(
    "ObjectLambdaAccessPointTypeDef",
    {
        "Name": str,
        "ObjectLambdaAccessPointArn": NotRequired[str],
    },
)

ObjectLambdaConfigurationTypeDef = TypedDict(
    "ObjectLambdaConfigurationTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": Sequence["ObjectLambdaTransformationConfigurationTypeDef"],
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "AllowedFeatures": NotRequired[Sequence[ObjectLambdaAllowedFeatureType]],
    },
)

ObjectLambdaContentTransformationTypeDef = TypedDict(
    "ObjectLambdaContentTransformationTypeDef",
    {
        "AwsLambda": NotRequired["AwsLambdaTransformationTypeDef"],
    },
)

ObjectLambdaTransformationConfigurationTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationTypeDef",
    {
        "Actions": Sequence[Literal["GetObject"]],
        "ContentTransformation": "ObjectLambdaContentTransformationTypeDef",
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

PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": NotRequired[bool],
    },
)

PrefixLevelStorageMetricsTypeDef = TypedDict(
    "PrefixLevelStorageMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
        "SelectionCriteria": NotRequired["SelectionCriteriaTypeDef"],
    },
)

PrefixLevelTypeDef = TypedDict(
    "PrefixLevelTypeDef",
    {
        "StorageMetrics": "PrefixLevelStorageMetricsTypeDef",
    },
)

ProposedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": NotRequired[str],
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

PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": "ObjectLambdaConfigurationTypeDef",
    },
)

PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

PutAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

PutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "LifecycleConfiguration": NotRequired["LifecycleConfigurationTypeDef"],
    },
)

PutBucketPolicyRequestRequestTypeDef = TypedDict(
    "PutBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Policy": str,
        "ConfirmRemoveSelfBucketAccess": NotRequired[bool],
    },
)

PutBucketTaggingRequestRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
    },
)

PutJobTaggingRequestRequestTypeDef = TypedDict(
    "PutJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Tags": Sequence["S3TagTypeDef"],
    },
)

PutMultiRegionAccessPointPolicyInputTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    {
        "Name": str,
        "Policy": str,
    },
)

PutMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": "PutMultiRegionAccessPointPolicyInputTypeDef",
    },
)

PutMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "PutPublicAccessBlockRequestRequestTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "AccountId": str,
    },
)

PutStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "StorageLensConfiguration": "StorageLensConfigurationTypeDef",
        "Tags": NotRequired[Sequence["StorageLensTagTypeDef"]],
    },
)

PutStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "Tags": Sequence["StorageLensTagTypeDef"],
    },
)

RegionReportTypeDef = TypedDict(
    "RegionReportTypeDef",
    {
        "Bucket": NotRequired[str],
        "Region": NotRequired[str],
    },
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "Bucket": str,
    },
)

RegionalBucketTypeDef = TypedDict(
    "RegionalBucketTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "BucketArn": NotRequired[str],
        "OutpostId": NotRequired[str],
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

S3AccessControlListTypeDef = TypedDict(
    "S3AccessControlListTypeDef",
    {
        "Owner": "S3ObjectOwnerTypeDef",
        "Grants": NotRequired[Sequence["S3GrantTypeDef"]],
    },
)

S3AccessControlPolicyTypeDef = TypedDict(
    "S3AccessControlPolicyTypeDef",
    {
        "AccessControlList": NotRequired["S3AccessControlListTypeDef"],
        "CannedAccessControlList": NotRequired[S3CannedAccessControlListType],
    },
)

S3BucketDestinationTypeDef = TypedDict(
    "S3BucketDestinationTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
        "Prefix": NotRequired[str],
        "Encryption": NotRequired["StorageLensDataExportEncryptionTypeDef"],
    },
)

S3CopyObjectOperationTypeDef = TypedDict(
    "S3CopyObjectOperationTypeDef",
    {
        "TargetResource": NotRequired[str],
        "CannedAccessControlList": NotRequired[S3CannedAccessControlListType],
        "AccessControlGrants": NotRequired[Sequence["S3GrantTypeDef"]],
        "MetadataDirective": NotRequired[S3MetadataDirectiveType],
        "ModifiedSinceConstraint": NotRequired[Union[datetime, str]],
        "NewObjectMetadata": NotRequired["S3ObjectMetadataTypeDef"],
        "NewObjectTagging": NotRequired[Sequence["S3TagTypeDef"]],
        "RedirectLocation": NotRequired[str],
        "RequesterPays": NotRequired[bool],
        "StorageClass": NotRequired[S3StorageClassType],
        "UnModifiedSinceConstraint": NotRequired[Union[datetime, str]],
        "SSEAwsKmsKeyId": NotRequired[str],
        "TargetKeyPrefix": NotRequired[str],
        "ObjectLockLegalHoldStatus": NotRequired[S3ObjectLockLegalHoldStatusType],
        "ObjectLockMode": NotRequired[S3ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[Union[datetime, str]],
        "BucketKeyEnabled": NotRequired[bool],
        "ChecksumAlgorithm": NotRequired[S3ChecksumAlgorithmType],
    },
)

S3GeneratedManifestDescriptorTypeDef = TypedDict(
    "S3GeneratedManifestDescriptorTypeDef",
    {
        "Format": NotRequired[Literal["S3InventoryReport_CSV_20211130"]],
        "Location": NotRequired["JobManifestLocationTypeDef"],
    },
)

S3GrantTypeDef = TypedDict(
    "S3GrantTypeDef",
    {
        "Grantee": NotRequired["S3GranteeTypeDef"],
        "Permission": NotRequired[S3PermissionType],
    },
)

S3GranteeTypeDef = TypedDict(
    "S3GranteeTypeDef",
    {
        "TypeIdentifier": NotRequired[S3GranteeTypeIdentifierType],
        "Identifier": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)

S3InitiateRestoreObjectOperationTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationTypeDef",
    {
        "ExpirationInDays": NotRequired[int],
        "GlacierJobTier": NotRequired[S3GlacierJobTierType],
    },
)

S3JobManifestGeneratorTypeDef = TypedDict(
    "S3JobManifestGeneratorTypeDef",
    {
        "SourceBucket": str,
        "EnableManifestOutput": bool,
        "ExpectedBucketOwner": NotRequired[str],
        "ManifestOutputLocation": NotRequired["S3ManifestOutputLocationTypeDef"],
        "Filter": NotRequired["JobManifestGeneratorFilterTypeDef"],
    },
)

S3ManifestOutputLocationTypeDef = TypedDict(
    "S3ManifestOutputLocationTypeDef",
    {
        "Bucket": str,
        "ManifestFormat": Literal["S3InventoryReport_CSV_20211130"],
        "ExpectedManifestBucketOwner": NotRequired[str],
        "ManifestPrefix": NotRequired[str],
        "ManifestEncryption": NotRequired["GeneratedManifestEncryptionTypeDef"],
    },
)

S3ObjectLockLegalHoldTypeDef = TypedDict(
    "S3ObjectLockLegalHoldTypeDef",
    {
        "Status": S3ObjectLockLegalHoldStatusType,
    },
)

S3ObjectMetadataTypeDef = TypedDict(
    "S3ObjectMetadataTypeDef",
    {
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "UserMetadata": NotRequired[Mapping[str, str]],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "HttpExpiresDate": NotRequired[Union[datetime, str]],
        "RequesterCharged": NotRequired[bool],
        "SSEAlgorithm": NotRequired[S3SSEAlgorithmType],
    },
)

S3ObjectOwnerTypeDef = TypedDict(
    "S3ObjectOwnerTypeDef",
    {
        "ID": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)

S3RetentionTypeDef = TypedDict(
    "S3RetentionTypeDef",
    {
        "RetainUntilDate": NotRequired[Union[datetime, str]],
        "Mode": NotRequired[S3ObjectLockRetentionModeType],
    },
)

S3SetObjectAclOperationTypeDef = TypedDict(
    "S3SetObjectAclOperationTypeDef",
    {
        "AccessControlPolicy": NotRequired["S3AccessControlPolicyTypeDef"],
    },
)

S3SetObjectLegalHoldOperationTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationTypeDef",
    {
        "LegalHold": "S3ObjectLockLegalHoldTypeDef",
    },
)

S3SetObjectRetentionOperationTypeDef = TypedDict(
    "S3SetObjectRetentionOperationTypeDef",
    {
        "Retention": "S3RetentionTypeDef",
        "BypassGovernanceRetention": NotRequired[bool],
    },
)

S3SetObjectTaggingOperationTypeDef = TypedDict(
    "S3SetObjectTaggingOperationTypeDef",
    {
        "TagSet": NotRequired[Sequence["S3TagTypeDef"]],
    },
)

S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SSEKMSEncryptionTypeDef = TypedDict(
    "SSEKMSEncryptionTypeDef",
    {
        "KeyId": str,
    },
)

SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

SelectionCriteriaTypeDef = TypedDict(
    "SelectionCriteriaTypeDef",
    {
        "Delimiter": NotRequired[str],
        "MaxDepth": NotRequired[int],
        "MinStorageBytesPercentage": NotRequired[float],
    },
)

StorageLensAwsOrgTypeDef = TypedDict(
    "StorageLensAwsOrgTypeDef",
    {
        "Arn": str,
    },
)

StorageLensConfigurationTypeDef = TypedDict(
    "StorageLensConfigurationTypeDef",
    {
        "Id": str,
        "AccountLevel": "AccountLevelTypeDef",
        "IsEnabled": bool,
        "Include": NotRequired["IncludeTypeDef"],
        "Exclude": NotRequired["ExcludeTypeDef"],
        "DataExport": NotRequired["StorageLensDataExportTypeDef"],
        "AwsOrg": NotRequired["StorageLensAwsOrgTypeDef"],
        "StorageLensArn": NotRequired[str],
    },
)

StorageLensDataExportEncryptionTypeDef = TypedDict(
    "StorageLensDataExportEncryptionTypeDef",
    {
        "SSES3": NotRequired[Dict[str, Any]],
        "SSEKMS": NotRequired["SSEKMSTypeDef"],
    },
)

StorageLensDataExportTypeDef = TypedDict(
    "StorageLensDataExportTypeDef",
    {
        "S3BucketDestination": NotRequired["S3BucketDestinationTypeDef"],
        "CloudWatchMetrics": NotRequired["CloudWatchMetricsTypeDef"],
    },
)

StorageLensTagTypeDef = TypedDict(
    "StorageLensTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": Sequence["S3TagTypeDef"],
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

UpdateJobPriorityRequestRequestTypeDef = TypedDict(
    "UpdateJobPriorityRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Priority": int,
    },
)

UpdateJobPriorityResultTypeDef = TypedDict(
    "UpdateJobPriorityResultTypeDef",
    {
        "JobId": str,
        "Priority": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJobStatusRequestRequestTypeDef = TypedDict(
    "UpdateJobStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "RequestedJobStatus": RequestedJobStatusType,
        "StatusUpdateReason": NotRequired[str],
    },
)

UpdateJobStatusResultTypeDef = TypedDict(
    "UpdateJobStatusResultTypeDef",
    {
        "JobId": str,
        "Status": JobStatusType,
        "StatusUpdateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
    },
)
