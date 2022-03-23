"""
Type annotations for ecr service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ecr/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    EncryptionTypeType,
    FindingSeverityType,
    ImageFailureCodeType,
    ImageTagMutabilityType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    LifecyclePolicyPreviewStatusType,
    ReplicationStatusType,
    ScanFrequencyType,
    ScanStatusType,
    ScanTypeType,
    TagStatusType,
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
    "AttributeTypeDef",
    "AuthorizationDataTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageRequestRequestTypeDef",
    "BatchGetImageResponseTypeDef",
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreatePullThroughCacheRuleRequestRequestTypeDef",
    "CreatePullThroughCacheRuleResponseTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResponseTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeletePullThroughCacheRuleRequestRequestTypeDef",
    "DeletePullThroughCacheRuleResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageReplicationStatusRequestRequestTypeDef",
    "DescribeImageReplicationStatusResponseTypeDef",
    "DescribeImageScanFindingsRequestRequestTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    "DescribePullThroughCacheRulesResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "EnhancedImageScanFindingTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetDownloadUrlForLayerRequestRequestTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "GetLifecyclePolicyPreviewRequestRequestTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRegistryScanningConfigurationResponseTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageReplicationStatusTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PullThroughCacheRuleTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutImageResponseTypeDef",
    "PutImageScanningConfigurationRequestRequestTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "PutImageTagMutabilityRequestRequestTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyRequestRequestTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyRequestRequestTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    "PutRegistryScanningConfigurationResponseTypeDef",
    "PutReplicationConfigurationRequestRequestTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "RecommendationTypeDef",
    "RegistryScanningConfigurationTypeDef",
    "RegistryScanningRuleTypeDef",
    "RemediationTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationRuleTypeDef",
    "RepositoryFilterTypeDef",
    "RepositoryScanningConfigurationFailureTypeDef",
    "RepositoryScanningConfigurationTypeDef",
    "RepositoryTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScanningRepositoryFilterTypeDef",
    "ScoreDetailsTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartImageScanRequestRequestTypeDef",
    "StartImageScanResponseTypeDef",
    "StartLifecyclePolicyPreviewRequestRequestTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "UploadLayerPartResponseTypeDef",
    "VulnerablePackageTypeDef",
    "WaiterConfigTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "proxyEndpoint": NotRequired[str],
    },
)

AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "architecture": NotRequired[str],
        "author": NotRequired[str],
        "imageHash": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "platform": NotRequired[str],
        "pushedAt": NotRequired[datetime],
        "registry": NotRequired[str],
        "repositoryName": NotRequired[str],
    },
)

BatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List["LayerTypeDef"],
        "failures": List["LayerFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteImageRequestRequestTypeDef = TypedDict(
    "BatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence["ImageIdentifierTypeDef"],
        "registryId": NotRequired[str],
    },
)

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetImageRequestRequestTypeDef = TypedDict(
    "BatchGetImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence["ImageIdentifierTypeDef"],
        "registryId": NotRequired[str],
        "acceptedMediaTypes": NotRequired[Sequence[str]],
    },
)

BatchGetImageResponseTypeDef = TypedDict(
    "BatchGetImageResponseTypeDef",
    {
        "images": List["ImageTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRepositoryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryNames": Sequence[str],
    },
)

BatchGetRepositoryScanningConfigurationResponseTypeDef = TypedDict(
    "BatchGetRepositoryScanningConfigurationResponseTypeDef",
    {
        "scanningConfigurations": List["RepositoryScanningConfigurationTypeDef"],
        "failures": List["RepositoryScanningConfigurationFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "CompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "CreatePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "registryId": NotRequired[str],
    },
)

CreatePullThroughCacheRuleResponseTypeDef = TypedDict(
    "CreatePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryRequestRequestTypeDef = TypedDict(
    "CreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "imageTagMutability": NotRequired[ImageTagMutabilityType],
        "imageScanningConfiguration": NotRequired["ImageScanningConfigurationTypeDef"],
        "encryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
    },
)

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": NotRequired[str],
        "reason": NotRequired[str],
    },
)

CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "adjustments": NotRequired[List["CvssScoreAdjustmentTypeDef"]],
        "score": NotRequired[float],
        "scoreSource": NotRequired[str],
        "scoringVector": NotRequired[str],
        "version": NotRequired[str],
    },
)

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": NotRequired[float],
        "scoringVector": NotRequired[str],
        "source": NotRequired[str],
        "version": NotRequired[str],
    },
)

DeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePullThroughCacheRuleRequestRequestTypeDef = TypedDict(
    "DeletePullThroughCacheRuleRequestRequestTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "registryId": NotRequired[str],
    },
)

DeletePullThroughCacheRuleResponseTypeDef = TypedDict(
    "DeletePullThroughCacheRuleResponseTypeDef",
    {
        "ecrRepositoryPrefix": str,
        "upstreamRegistryUrl": str,
        "createdAt": datetime,
        "registryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistryPolicyResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageReplicationStatusRequestRequestTypeDef = TypedDict(
    "DescribeImageReplicationStatusRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "registryId": NotRequired[str],
    },
)

DescribeImageReplicationStatusResponseTypeDef = TypedDict(
    "DescribeImageReplicationStatusResponseTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "replicationStatuses": List["ImageReplicationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageScanFindingsRequestRequestTypeDef = TypedDict(
    "DescribeImageScanFindingsRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindings": "ImageScanFindingsTypeDef",
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef",
    {
        "tagStatus": NotRequired[TagStatusType],
    },
)

DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence["ImageIdentifierTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired["DescribeImagesFilterTypeDef"],
    },
)

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List["ImageDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePullThroughCacheRulesRequestRequestTypeDef = TypedDict(
    "DescribePullThroughCacheRulesRequestRequestTypeDef",
    {
        "registryId": NotRequired[str],
        "ecrRepositoryPrefixes": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribePullThroughCacheRulesResponseTypeDef = TypedDict(
    "DescribePullThroughCacheRulesResponseTypeDef",
    {
        "pullThroughCacheRules": List["PullThroughCacheRuleTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "registryId": str,
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryNames": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKey": NotRequired[str],
    },
)

EnhancedImageScanFindingTypeDef = TypedDict(
    "EnhancedImageScanFindingTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "description": NotRequired[str],
        "findingArn": NotRequired[str],
        "firstObservedAt": NotRequired[datetime],
        "lastObservedAt": NotRequired[datetime],
        "packageVulnerabilityDetails": NotRequired["PackageVulnerabilityDetailsTypeDef"],
        "remediation": NotRequired["RemediationTypeDef"],
        "resources": NotRequired[List["ResourceTypeDef"]],
        "score": NotRequired[float],
        "scoreDetails": NotRequired["ScoreDetailsTypeDef"],
        "severity": NotRequired[str],
        "status": NotRequired[str],
        "title": NotRequired[str],
        "type": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)

GetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestRequestTypeDef",
    {
        "registryIds": NotRequired[Sequence[str]],
    },
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": List["AuthorizationDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDownloadUrlForLayerRequestRequestTypeDef = TypedDict(
    "GetDownloadUrlForLayerRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigest": str,
        "registryId": NotRequired[str],
    },
)

GetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseTypeDef",
    {
        "downloadUrl": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence["ImageIdentifierTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired["LifecyclePolicyPreviewFilterTypeDef"],
    },
)

GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "nextToken": str,
        "previewResults": List["LifecyclePolicyPreviewResultTypeDef"],
        "summary": "LifecyclePolicyPreviewSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryPolicyResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "GetRegistryScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "scanningConfiguration": "RegistryScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "GetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageDigest": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "imageSizeInBytes": NotRequired[int],
        "imagePushedAt": NotRequired[datetime],
        "imageScanStatus": NotRequired["ImageScanStatusTypeDef"],
        "imageScanFindingsSummary": NotRequired["ImageScanFindingsSummaryTypeDef"],
        "imageManifestMediaType": NotRequired[str],
        "artifactMediaType": NotRequired[str],
        "lastRecordedPullTime": NotRequired[datetime],
    },
)

ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": NotRequired["ImageIdentifierTypeDef"],
        "failureCode": NotRequired[ImageFailureCodeType],
        "failureReason": NotRequired[str],
    },
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": NotRequired[str],
        "imageTag": NotRequired[str],
    },
)

ImageReplicationStatusTypeDef = TypedDict(
    "ImageReplicationStatusTypeDef",
    {
        "region": NotRequired[str],
        "registryId": NotRequired[str],
        "status": NotRequired[ReplicationStatusType],
        "failureCode": NotRequired[str],
    },
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "uri": NotRequired[str],
        "severity": NotRequired[FindingSeverityType],
        "attributes": NotRequired[List["AttributeTypeDef"]],
    },
)

ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": NotRequired[datetime],
        "vulnerabilitySourceUpdatedAt": NotRequired[datetime],
        "findingSeverityCounts": NotRequired[Dict[FindingSeverityType, int]],
    },
)

ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": NotRequired[datetime],
        "vulnerabilitySourceUpdatedAt": NotRequired[datetime],
        "findingSeverityCounts": NotRequired[Dict[FindingSeverityType, int]],
        "findings": NotRequired[List["ImageScanFindingTypeDef"]],
        "enhancedFindings": NotRequired[List["EnhancedImageScanFindingTypeDef"]],
    },
)

ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {
        "status": NotRequired[ScanStatusType],
        "description": NotRequired[str],
    },
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "scanOnPush": NotRequired[bool],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageId": NotRequired["ImageIdentifierTypeDef"],
        "imageManifest": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
    },
)

InitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "InitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": NotRequired[str],
        "failureCode": NotRequired[LayerFailureCodeType],
        "failureReason": NotRequired[str],
    },
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": NotRequired[str],
        "layerAvailability": NotRequired[LayerAvailabilityType],
        "layerSize": NotRequired[int],
        "mediaType": NotRequired[str],
    },
)

LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {
        "tagStatus": NotRequired[TagStatusType],
    },
)

LifecyclePolicyPreviewResultTypeDef = TypedDict(
    "LifecyclePolicyPreviewResultTypeDef",
    {
        "imageTags": NotRequired[List[str]],
        "imageDigest": NotRequired[str],
        "imagePushedAt": NotRequired[datetime],
        "action": NotRequired["LifecyclePolicyRuleActionTypeDef"],
        "appliedRulePriority": NotRequired[int],
    },
)

LifecyclePolicyPreviewSummaryTypeDef = TypedDict(
    "LifecyclePolicyPreviewSummaryTypeDef",
    {
        "expiringImageTotalCount": NotRequired[int],
    },
)

LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef",
    {
        "type": NotRequired[Literal["EXPIRE"]],
    },
)

ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef",
    {
        "tagStatus": NotRequired[TagStatusType],
    },
)

ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired["ListImagesFilterTypeDef"],
    },
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
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

PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "cvss": NotRequired[List["CvssScoreTypeDef"]],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "source": NotRequired[str],
        "sourceUrl": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorSeverity": NotRequired[str],
        "vendorUpdatedAt": NotRequired[datetime],
        "vulnerabilityId": NotRequired[str],
        "vulnerablePackages": NotRequired[List["VulnerablePackageTypeDef"]],
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

PullThroughCacheRuleTypeDef = TypedDict(
    "PullThroughCacheRuleTypeDef",
    {
        "ecrRepositoryPrefix": NotRequired[str],
        "upstreamRegistryUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "registryId": NotRequired[str],
    },
)

PutImageRequestRequestTypeDef = TypedDict(
    "PutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
        "registryId": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
        "imageTag": NotRequired[str],
        "imageDigest": NotRequired[str],
    },
)

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageScanningConfigurationRequestRequestTypeDef = TypedDict(
    "PutImageScanningConfigurationRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "registryId": NotRequired[str],
    },
)

PutImageScanningConfigurationResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageTagMutabilityRequestRequestTypeDef = TypedDict(
    "PutImageTagMutabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "registryId": NotRequired[str],
    },
)

PutImageTagMutabilityResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "PutLifecyclePolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "registryId": NotRequired[str],
    },
)

PutLifecyclePolicyResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryPolicyRequestRequestTypeDef = TypedDict(
    "PutRegistryPolicyRequestRequestTypeDef",
    {
        "policyText": str,
    },
)

PutRegistryPolicyResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryScanningConfigurationRequestRequestTypeDef = TypedDict(
    "PutRegistryScanningConfigurationRequestRequestTypeDef",
    {
        "scanType": NotRequired[ScanTypeType],
        "rules": NotRequired[Sequence["RegistryScanningRuleTypeDef"]],
    },
)

PutRegistryScanningConfigurationResponseTypeDef = TypedDict(
    "PutRegistryScanningConfigurationResponseTypeDef",
    {
        "registryScanningConfiguration": "RegistryScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutReplicationConfigurationRequestRequestTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
    },
)

PutReplicationConfigurationResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "url": NotRequired[str],
        "text": NotRequired[str],
    },
)

RegistryScanningConfigurationTypeDef = TypedDict(
    "RegistryScanningConfigurationTypeDef",
    {
        "scanType": NotRequired[ScanTypeType],
        "rules": NotRequired[List["RegistryScanningRuleTypeDef"]],
    },
)

RegistryScanningRuleTypeDef = TypedDict(
    "RegistryScanningRuleTypeDef",
    {
        "scanFrequency": ScanFrequencyType,
        "repositoryFilters": List["ScanningRepositoryFilterTypeDef"],
    },
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": NotRequired["RecommendationTypeDef"],
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "rules": List["ReplicationRuleTypeDef"],
    },
)

ReplicationDestinationTypeDef = TypedDict(
    "ReplicationDestinationTypeDef",
    {
        "region": str,
        "registryId": str,
    },
)

ReplicationRuleTypeDef = TypedDict(
    "ReplicationRuleTypeDef",
    {
        "destinations": List["ReplicationDestinationTypeDef"],
        "repositoryFilters": NotRequired[List["RepositoryFilterTypeDef"]],
    },
)

RepositoryFilterTypeDef = TypedDict(
    "RepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["PREFIX_MATCH"],
    },
)

RepositoryScanningConfigurationFailureTypeDef = TypedDict(
    "RepositoryScanningConfigurationFailureTypeDef",
    {
        "repositoryName": NotRequired[str],
        "failureCode": NotRequired[Literal["REPOSITORY_NOT_FOUND"]],
        "failureReason": NotRequired[str],
    },
)

RepositoryScanningConfigurationTypeDef = TypedDict(
    "RepositoryScanningConfigurationTypeDef",
    {
        "repositoryArn": NotRequired[str],
        "repositoryName": NotRequired[str],
        "scanOnPush": NotRequired[bool],
        "scanFrequency": NotRequired[ScanFrequencyType],
        "appliedScanFilters": NotRequired[List["ScanningRepositoryFilterTypeDef"]],
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": NotRequired[str],
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "repositoryUri": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "imageTagMutability": NotRequired[ImageTagMutabilityType],
        "imageScanningConfiguration": NotRequired["ImageScanningConfigurationTypeDef"],
        "encryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEcrContainerImage": NotRequired["AwsEcrContainerImageDetailsTypeDef"],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "details": NotRequired["ResourceDetailsTypeDef"],
        "id": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[str],
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

ScanningRepositoryFilterTypeDef = TypedDict(
    "ScanningRepositoryFilterTypeDef",
    {
        "filter": str,
        "filterType": Literal["WILDCARD"],
    },
)

ScoreDetailsTypeDef = TypedDict(
    "ScoreDetailsTypeDef",
    {
        "cvss": NotRequired["CvssScoreDetailsTypeDef"],
    },
)

SetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "SetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImageScanRequestRequestTypeDef = TypedDict(
    "StartImageScanRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "registryId": NotRequired[str],
    },
)

StartImageScanResponseTypeDef = TypedDict(
    "StartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartLifecyclePolicyPreviewRequestRequestTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "lifecyclePolicyText": NotRequired[str],
    },
)

StartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
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
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UploadLayerPartRequestRequestTypeDef = TypedDict(
    "UploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": Union[bytes, IO[bytes], StreamingBody],
        "registryId": NotRequired[str],
    },
)

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "arch": NotRequired[str],
        "epoch": NotRequired[int],
        "filePath": NotRequired[str],
        "name": NotRequired[str],
        "packageManager": NotRequired[str],
        "release": NotRequired[str],
        "sourceLayerHash": NotRequired[str],
        "version": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
