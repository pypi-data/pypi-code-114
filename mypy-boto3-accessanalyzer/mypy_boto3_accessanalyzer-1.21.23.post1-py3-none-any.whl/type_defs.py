"""
Type annotations for accessanalyzer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AccessPreviewFindingTypeDef

    data: AccessPreviewFindingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AccessPreviewStatusReasonCodeType,
    AccessPreviewStatusType,
    AclPermissionType,
    AnalyzerStatusType,
    FindingChangeTypeType,
    FindingSourceTypeType,
    FindingStatusType,
    FindingStatusUpdateType,
    JobErrorCodeType,
    JobStatusType,
    KmsGrantOperationType,
    LocaleType,
    OrderByType,
    PolicyTypeType,
    ReasonCodeType,
    ResourceTypeType,
    TypeType,
    ValidatePolicyFindingTypeType,
    ValidatePolicyResourceTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPreviewFindingTypeDef",
    "AccessPreviewStatusReasonTypeDef",
    "AccessPreviewSummaryTypeDef",
    "AccessPreviewTypeDef",
    "AclGranteeTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerSummaryTypeDef",
    "ApplyArchiveRuleRequestRequestTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CancelPolicyGenerationRequestRequestTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationTypeDef",
    "CreateAccessPreviewRequestRequestTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerRequestRequestTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "CreateArchiveRuleRequestRequestTypeDef",
    "CriterionTypeDef",
    "DeleteAnalyzerRequestRequestTypeDef",
    "DeleteArchiveRuleRequestRequestTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewRequestRequestTypeDef",
    "GetAccessPreviewResponseTypeDef",
    "GetAnalyzedResourceRequestRequestTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerRequestRequestTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleRequestRequestTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingRequestRequestTypeDef",
    "GetFindingResponseTypeDef",
    "GetGeneratedPolicyRequestRequestTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsKeyConfigurationTypeDef",
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListAccessPreviewsRequestRequestTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "ListAnalyzedResourcesRequestRequestTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersRequestRequestTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesRequestRequestTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListPolicyGenerationsRequestRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationRequestRequestTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StartResourceScanRequestRequestTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateArchiveRuleRequestRequestTypeDef",
    "UpdateFindingsRequestRequestTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyRequestRequestTypeDef",
    "ValidatePolicyResponseTypeDef",
    "VpcConfigurationTypeDef",
)

AccessPreviewFindingTypeDef = TypedDict(
    "AccessPreviewFindingTypeDef",
    {
        "changeType": FindingChangeTypeType,
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "action": NotRequired[List[str]],
        "condition": NotRequired[Dict[str, str]],
        "error": NotRequired[str],
        "existingFindingId": NotRequired[str],
        "existingFindingStatus": NotRequired[FindingStatusType],
        "isPublic": NotRequired[bool],
        "principal": NotRequired[Dict[str, str]],
        "resource": NotRequired[str],
        "sources": NotRequired[List["FindingSourceTypeDef"]],
    },
)

AccessPreviewStatusReasonTypeDef = TypedDict(
    "AccessPreviewStatusReasonTypeDef",
    {
        "code": AccessPreviewStatusReasonCodeType,
    },
)

AccessPreviewSummaryTypeDef = TypedDict(
    "AccessPreviewSummaryTypeDef",
    {
        "analyzerArn": str,
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired["AccessPreviewStatusReasonTypeDef"],
    },
)

AccessPreviewTypeDef = TypedDict(
    "AccessPreviewTypeDef",
    {
        "analyzerArn": str,
        "configurations": Dict[str, "ConfigurationTypeDef"],
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatusType,
        "statusReason": NotRequired["AccessPreviewStatusReasonTypeDef"],
    },
)

AclGranteeTypeDef = TypedDict(
    "AclGranteeTypeDef",
    {
        "id": NotRequired[str],
        "uri": NotRequired[str],
    },
)

AnalyzedResourceSummaryTypeDef = TypedDict(
    "AnalyzedResourceSummaryTypeDef",
    {
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
    },
)

AnalyzedResourceTypeDef = TypedDict(
    "AnalyzedResourceTypeDef",
    {
        "analyzedAt": datetime,
        "createdAt": datetime,
        "isPublic": bool,
        "resourceArn": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "updatedAt": datetime,
        "actions": NotRequired[List[str]],
        "error": NotRequired[str],
        "sharedVia": NotRequired[List[str]],
        "status": NotRequired[FindingStatusType],
    },
)

AnalyzerSummaryTypeDef = TypedDict(
    "AnalyzerSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "name": str,
        "status": AnalyzerStatusType,
        "type": TypeType,
        "lastResourceAnalyzed": NotRequired[str],
        "lastResourceAnalyzedAt": NotRequired[datetime],
        "statusReason": NotRequired["StatusReasonTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

ApplyArchiveRuleRequestRequestTypeDef = TypedDict(
    "ApplyArchiveRuleRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "ruleName": str,
        "clientToken": NotRequired[str],
    },
)

ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
        "updatedAt": datetime,
    },
)

CancelPolicyGenerationRequestRequestTypeDef = TypedDict(
    "CancelPolicyGenerationRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

CloudTrailDetailsTypeDef = TypedDict(
    "CloudTrailDetailsTypeDef",
    {
        "accessRole": str,
        "startTime": Union[datetime, str],
        "trails": Sequence["TrailTypeDef"],
        "endTime": NotRequired[Union[datetime, str]],
    },
)

CloudTrailPropertiesTypeDef = TypedDict(
    "CloudTrailPropertiesTypeDef",
    {
        "endTime": datetime,
        "startTime": datetime,
        "trailProperties": List["TrailPropertiesTypeDef"],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "iamRole": NotRequired["IamRoleConfigurationTypeDef"],
        "kmsKey": NotRequired["KmsKeyConfigurationTypeDef"],
        "s3Bucket": NotRequired["S3BucketConfigurationTypeDef"],
        "secretsManagerSecret": NotRequired["SecretsManagerSecretConfigurationTypeDef"],
        "sqsQueue": NotRequired["SqsQueueConfigurationTypeDef"],
    },
)

CreateAccessPreviewRequestRequestTypeDef = TypedDict(
    "CreateAccessPreviewRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "configurations": Mapping[str, "ConfigurationTypeDef"],
        "clientToken": NotRequired[str],
    },
)

CreateAccessPreviewResponseTypeDef = TypedDict(
    "CreateAccessPreviewResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAnalyzerRequestRequestTypeDef = TypedDict(
    "CreateAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "type": TypeType,
        "archiveRules": NotRequired[Sequence["InlineArchiveRuleTypeDef"]],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAnalyzerResponseTypeDef = TypedDict(
    "CreateAnalyzerResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateArchiveRuleRequestRequestTypeDef = TypedDict(
    "CreateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "filter": Mapping[str, "CriterionTypeDef"],
        "ruleName": str,
        "clientToken": NotRequired[str],
    },
)

CriterionTypeDef = TypedDict(
    "CriterionTypeDef",
    {
        "contains": NotRequired[Sequence[str]],
        "eq": NotRequired[Sequence[str]],
        "exists": NotRequired[bool],
        "neq": NotRequired[Sequence[str]],
    },
)

DeleteAnalyzerRequestRequestTypeDef = TypedDict(
    "DeleteAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
        "clientToken": NotRequired[str],
    },
)

DeleteArchiveRuleRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
        "clientToken": NotRequired[str],
    },
)

FindingSourceDetailTypeDef = TypedDict(
    "FindingSourceDetailTypeDef",
    {
        "accessPointArn": NotRequired[str],
    },
)

FindingSourceTypeDef = TypedDict(
    "FindingSourceTypeDef",
    {
        "type": FindingSourceTypeType,
        "detail": NotRequired["FindingSourceDetailTypeDef"],
    },
)

FindingSummaryTypeDef = TypedDict(
    "FindingSummaryTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "action": NotRequired[List[str]],
        "error": NotRequired[str],
        "isPublic": NotRequired[bool],
        "principal": NotRequired[Dict[str, str]],
        "resource": NotRequired[str],
        "sources": NotRequired[List["FindingSourceTypeDef"]],
    },
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceTypeType,
        "status": FindingStatusType,
        "updatedAt": datetime,
        "action": NotRequired[List[str]],
        "error": NotRequired[str],
        "isPublic": NotRequired[bool],
        "principal": NotRequired[Dict[str, str]],
        "resource": NotRequired[str],
        "sources": NotRequired[List["FindingSourceTypeDef"]],
    },
)

GeneratedPolicyPropertiesTypeDef = TypedDict(
    "GeneratedPolicyPropertiesTypeDef",
    {
        "principalArn": str,
        "cloudTrailProperties": NotRequired["CloudTrailPropertiesTypeDef"],
        "isComplete": NotRequired[bool],
    },
)

GeneratedPolicyResultTypeDef = TypedDict(
    "GeneratedPolicyResultTypeDef",
    {
        "properties": "GeneratedPolicyPropertiesTypeDef",
        "generatedPolicies": NotRequired[List["GeneratedPolicyTypeDef"]],
    },
)

GeneratedPolicyTypeDef = TypedDict(
    "GeneratedPolicyTypeDef",
    {
        "policy": str,
    },
)

GetAccessPreviewRequestRequestTypeDef = TypedDict(
    "GetAccessPreviewRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
    },
)

GetAccessPreviewResponseTypeDef = TypedDict(
    "GetAccessPreviewResponseTypeDef",
    {
        "accessPreview": "AccessPreviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnalyzedResourceRequestRequestTypeDef = TypedDict(
    "GetAnalyzedResourceRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

GetAnalyzedResourceResponseTypeDef = TypedDict(
    "GetAnalyzedResourceResponseTypeDef",
    {
        "resource": "AnalyzedResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnalyzerRequestRequestTypeDef = TypedDict(
    "GetAnalyzerRequestRequestTypeDef",
    {
        "analyzerName": str,
    },
)

GetAnalyzerResponseTypeDef = TypedDict(
    "GetAnalyzerResponseTypeDef",
    {
        "analyzer": "AnalyzerSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArchiveRuleRequestRequestTypeDef = TypedDict(
    "GetArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "ruleName": str,
    },
)

GetArchiveRuleResponseTypeDef = TypedDict(
    "GetArchiveRuleResponseTypeDef",
    {
        "archiveRule": "ArchiveRuleSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFindingRequestRequestTypeDef = TypedDict(
    "GetFindingRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "id": str,
    },
)

GetFindingResponseTypeDef = TypedDict(
    "GetFindingResponseTypeDef",
    {
        "finding": "FindingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeneratedPolicyRequestRequestTypeDef = TypedDict(
    "GetGeneratedPolicyRequestRequestTypeDef",
    {
        "jobId": str,
        "includeResourcePlaceholders": NotRequired[bool],
        "includeServiceLevelTemplate": NotRequired[bool],
    },
)

GetGeneratedPolicyResponseTypeDef = TypedDict(
    "GetGeneratedPolicyResponseTypeDef",
    {
        "generatedPolicyResult": "GeneratedPolicyResultTypeDef",
        "jobDetails": "JobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamRoleConfigurationTypeDef = TypedDict(
    "IamRoleConfigurationTypeDef",
    {
        "trustPolicy": NotRequired[str],
    },
)

InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef",
    {
        "filter": Mapping[str, "CriterionTypeDef"],
        "ruleName": str,
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "jobId": str,
        "startedOn": datetime,
        "status": JobStatusType,
        "completedOn": NotRequired[datetime],
        "jobError": NotRequired["JobErrorTypeDef"],
    },
)

JobErrorTypeDef = TypedDict(
    "JobErrorTypeDef",
    {
        "code": JobErrorCodeType,
        "message": str,
    },
)

KmsGrantConfigurationTypeDef = TypedDict(
    "KmsGrantConfigurationTypeDef",
    {
        "granteePrincipal": str,
        "issuingAccount": str,
        "operations": Sequence[KmsGrantOperationType],
        "constraints": NotRequired["KmsGrantConstraintsTypeDef"],
        "retiringPrincipal": NotRequired[str],
    },
)

KmsGrantConstraintsTypeDef = TypedDict(
    "KmsGrantConstraintsTypeDef",
    {
        "encryptionContextEquals": NotRequired[Mapping[str, str]],
        "encryptionContextSubset": NotRequired[Mapping[str, str]],
    },
)

KmsKeyConfigurationTypeDef = TypedDict(
    "KmsKeyConfigurationTypeDef",
    {
        "grants": NotRequired[Sequence["KmsGrantConfigurationTypeDef"]],
        "keyPolicies": NotRequired[Mapping[str, str]],
    },
)

ListAccessPreviewFindingsRequestRequestTypeDef = TypedDict(
    "ListAccessPreviewFindingsRequestRequestTypeDef",
    {
        "accessPreviewId": str,
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, "CriterionTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAccessPreviewFindingsResponseTypeDef = TypedDict(
    "ListAccessPreviewFindingsResponseTypeDef",
    {
        "findings": List["AccessPreviewFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccessPreviewsRequestRequestTypeDef = TypedDict(
    "ListAccessPreviewsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAccessPreviewsResponseTypeDef = TypedDict(
    "ListAccessPreviewsResponseTypeDef",
    {
        "accessPreviews": List["AccessPreviewSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnalyzedResourcesRequestRequestTypeDef = TypedDict(
    "ListAnalyzedResourcesRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
    },
)

ListAnalyzedResourcesResponseTypeDef = TypedDict(
    "ListAnalyzedResourcesResponseTypeDef",
    {
        "analyzedResources": List["AnalyzedResourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnalyzersRequestRequestTypeDef = TypedDict(
    "ListAnalyzersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "type": NotRequired[TypeType],
    },
)

ListAnalyzersResponseTypeDef = TypedDict(
    "ListAnalyzersResponseTypeDef",
    {
        "analyzers": List["AnalyzerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArchiveRulesRequestRequestTypeDef = TypedDict(
    "ListArchiveRulesRequestRequestTypeDef",
    {
        "analyzerName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListArchiveRulesResponseTypeDef = TypedDict(
    "ListArchiveRulesResponseTypeDef",
    {
        "archiveRules": List["ArchiveRuleSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "filter": NotRequired[Mapping[str, "CriterionTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired["SortCriteriaTypeDef"],
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List["FindingSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyGenerationsRequestRequestTypeDef = TypedDict(
    "ListPolicyGenerationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "principalArn": NotRequired[str],
    },
)

ListPolicyGenerationsResponseTypeDef = TypedDict(
    "ListPolicyGenerationsResponseTypeDef",
    {
        "nextToken": str,
        "policyGenerations": List["PolicyGenerationTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "path": List["PathElementTypeDef"],
        "span": "SpanTypeDef",
    },
)

NetworkOriginConfigurationTypeDef = TypedDict(
    "NetworkOriginConfigurationTypeDef",
    {
        "internetConfiguration": NotRequired[Mapping[str, Any]],
        "vpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
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

PathElementTypeDef = TypedDict(
    "PathElementTypeDef",
    {
        "index": NotRequired[int],
        "key": NotRequired[str],
        "substring": NotRequired["SubstringTypeDef"],
        "value": NotRequired[str],
    },
)

PolicyGenerationDetailsTypeDef = TypedDict(
    "PolicyGenerationDetailsTypeDef",
    {
        "principalArn": str,
    },
)

PolicyGenerationTypeDef = TypedDict(
    "PolicyGenerationTypeDef",
    {
        "jobId": str,
        "principalArn": str,
        "startedOn": datetime,
        "status": JobStatusType,
        "completedOn": NotRequired[datetime],
    },
)

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "column": int,
        "line": int,
        "offset": int,
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

S3AccessPointConfigurationTypeDef = TypedDict(
    "S3AccessPointConfigurationTypeDef",
    {
        "accessPointPolicy": NotRequired[str],
        "networkOrigin": NotRequired["NetworkOriginConfigurationTypeDef"],
        "publicAccessBlock": NotRequired["S3PublicAccessBlockConfigurationTypeDef"],
    },
)

S3BucketAclGrantConfigurationTypeDef = TypedDict(
    "S3BucketAclGrantConfigurationTypeDef",
    {
        "grantee": "AclGranteeTypeDef",
        "permission": AclPermissionType,
    },
)

S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "accessPoints": NotRequired[Mapping[str, "S3AccessPointConfigurationTypeDef"]],
        "bucketAclGrants": NotRequired[Sequence["S3BucketAclGrantConfigurationTypeDef"]],
        "bucketPolicy": NotRequired[str],
        "bucketPublicAccessBlock": NotRequired["S3PublicAccessBlockConfigurationTypeDef"],
    },
)

S3PublicAccessBlockConfigurationTypeDef = TypedDict(
    "S3PublicAccessBlockConfigurationTypeDef",
    {
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
)

SecretsManagerSecretConfigurationTypeDef = TypedDict(
    "SecretsManagerSecretConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
        "secretPolicy": NotRequired[str],
    },
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)

SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "end": "PositionTypeDef",
        "start": "PositionTypeDef",
    },
)

SqsQueueConfigurationTypeDef = TypedDict(
    "SqsQueueConfigurationTypeDef",
    {
        "queuePolicy": NotRequired[str],
    },
)

StartPolicyGenerationRequestRequestTypeDef = TypedDict(
    "StartPolicyGenerationRequestRequestTypeDef",
    {
        "policyGenerationDetails": "PolicyGenerationDetailsTypeDef",
        "clientToken": NotRequired[str],
        "cloudTrailDetails": NotRequired["CloudTrailDetailsTypeDef"],
    },
)

StartPolicyGenerationResponseTypeDef = TypedDict(
    "StartPolicyGenerationResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartResourceScanRequestRequestTypeDef = TypedDict(
    "StartResourceScanRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "resourceArn": str,
    },
)

StatusReasonTypeDef = TypedDict(
    "StatusReasonTypeDef",
    {
        "code": ReasonCodeType,
    },
)

SubstringTypeDef = TypedDict(
    "SubstringTypeDef",
    {
        "length": int,
        "start": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TrailPropertiesTypeDef = TypedDict(
    "TrailPropertiesTypeDef",
    {
        "cloudTrailArn": str,
        "allRegions": NotRequired[bool],
        "regions": NotRequired[List[str]],
    },
)

TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "cloudTrailArn": str,
        "allRegions": NotRequired[bool],
        "regions": NotRequired[Sequence[str]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateArchiveRuleRequestRequestTypeDef = TypedDict(
    "UpdateArchiveRuleRequestRequestTypeDef",
    {
        "analyzerName": str,
        "filter": Mapping[str, "CriterionTypeDef"],
        "ruleName": str,
        "clientToken": NotRequired[str],
    },
)

UpdateFindingsRequestRequestTypeDef = TypedDict(
    "UpdateFindingsRequestRequestTypeDef",
    {
        "analyzerArn": str,
        "status": FindingStatusUpdateType,
        "clientToken": NotRequired[str],
        "ids": NotRequired[Sequence[str]],
        "resourceArn": NotRequired[str],
    },
)

ValidatePolicyFindingTypeDef = TypedDict(
    "ValidatePolicyFindingTypeDef",
    {
        "findingDetails": str,
        "findingType": ValidatePolicyFindingTypeType,
        "issueCode": str,
        "learnMoreLink": str,
        "locations": List["LocationTypeDef"],
    },
)

ValidatePolicyRequestRequestTypeDef = TypedDict(
    "ValidatePolicyRequestRequestTypeDef",
    {
        "policyDocument": str,
        "policyType": PolicyTypeType,
        "locale": NotRequired[LocaleType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "validatePolicyResourceType": NotRequired[ValidatePolicyResourceTypeType],
    },
)

ValidatePolicyResponseTypeDef = TypedDict(
    "ValidatePolicyResponseTypeDef",
    {
        "findings": List["ValidatePolicyFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": str,
    },
)
