"""
Type annotations for resiliencehub service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_resiliencehub/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_resiliencehub.type_defs import AddDraftAppVersionResourceMappingsRequestRequestTypeDef

    data: AddDraftAppVersionResourceMappingsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AlarmTypeType,
    AppComplianceStatusTypeType,
    AppStatusTypeType,
    AssessmentInvokerType,
    AssessmentStatusType,
    ComplianceStatusType,
    ConfigRecommendationOptimizationTypeType,
    CostFrequencyType,
    DataLocationConstraintType,
    DisruptionTypeType,
    EstimatedCostTierType,
    HaArchitectureType,
    PhysicalIdentifierTypeType,
    RecommendationComplianceStatusType,
    RecommendationTemplateStatusType,
    RenderRecommendationTypeType,
    ResiliencyPolicyTierType,
    ResourceImportStatusTypeType,
    ResourceMappingTypeType,
    ResourceResolutionStatusTypeType,
    TemplateFormatType,
    TestRiskType,
    TestTypeType,
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
    "AddDraftAppVersionResourceMappingsRequestRequestTypeDef",
    "AddDraftAppVersionResourceMappingsResponseTypeDef",
    "AlarmRecommendationTypeDef",
    "AppAssessmentSummaryTypeDef",
    "AppAssessmentTypeDef",
    "AppComponentComplianceTypeDef",
    "AppComponentTypeDef",
    "AppSummaryTypeDef",
    "AppTypeDef",
    "AppVersionSummaryTypeDef",
    "ComponentRecommendationTypeDef",
    "ConfigRecommendationTypeDef",
    "CostTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateRecommendationTemplateRequestRequestTypeDef",
    "CreateRecommendationTemplateResponseTypeDef",
    "CreateResiliencyPolicyRequestRequestTypeDef",
    "CreateResiliencyPolicyResponseTypeDef",
    "DeleteAppAssessmentRequestRequestTypeDef",
    "DeleteAppAssessmentResponseTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteRecommendationTemplateRequestRequestTypeDef",
    "DeleteRecommendationTemplateResponseTypeDef",
    "DeleteResiliencyPolicyRequestRequestTypeDef",
    "DeleteResiliencyPolicyResponseTypeDef",
    "DescribeAppAssessmentRequestRequestTypeDef",
    "DescribeAppAssessmentResponseTypeDef",
    "DescribeAppRequestRequestTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef",
    "DescribeAppVersionResourcesResolutionStatusResponseTypeDef",
    "DescribeAppVersionTemplateRequestRequestTypeDef",
    "DescribeAppVersionTemplateResponseTypeDef",
    "DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef",
    "DescribeDraftAppVersionResourcesImportStatusResponseTypeDef",
    "DescribeResiliencyPolicyRequestRequestTypeDef",
    "DescribeResiliencyPolicyResponseTypeDef",
    "DisruptionComplianceTypeDef",
    "FailurePolicyTypeDef",
    "ImportResourcesToDraftAppVersionRequestRequestTypeDef",
    "ImportResourcesToDraftAppVersionResponseTypeDef",
    "ListAlarmRecommendationsRequestRequestTypeDef",
    "ListAlarmRecommendationsResponseTypeDef",
    "ListAppAssessmentsRequestRequestTypeDef",
    "ListAppAssessmentsResponseTypeDef",
    "ListAppComponentCompliancesRequestRequestTypeDef",
    "ListAppComponentCompliancesResponseTypeDef",
    "ListAppComponentRecommendationsRequestRequestTypeDef",
    "ListAppComponentRecommendationsResponseTypeDef",
    "ListAppVersionResourceMappingsRequestRequestTypeDef",
    "ListAppVersionResourceMappingsResponseTypeDef",
    "ListAppVersionResourcesRequestRequestTypeDef",
    "ListAppVersionResourcesResponseTypeDef",
    "ListAppVersionsRequestRequestTypeDef",
    "ListAppVersionsResponseTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResponseTypeDef",
    "ListRecommendationTemplatesRequestRequestTypeDef",
    "ListRecommendationTemplatesResponseTypeDef",
    "ListResiliencyPoliciesRequestRequestTypeDef",
    "ListResiliencyPoliciesResponseTypeDef",
    "ListSopRecommendationsRequestRequestTypeDef",
    "ListSopRecommendationsResponseTypeDef",
    "ListSuggestedResiliencyPoliciesRequestRequestTypeDef",
    "ListSuggestedResiliencyPoliciesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestRecommendationsRequestRequestTypeDef",
    "ListTestRecommendationsResponseTypeDef",
    "ListUnsupportedAppVersionResourcesRequestRequestTypeDef",
    "ListUnsupportedAppVersionResourcesResponseTypeDef",
    "LogicalResourceIdTypeDef",
    "PhysicalResourceIdTypeDef",
    "PhysicalResourceTypeDef",
    "PublishAppVersionRequestRequestTypeDef",
    "PublishAppVersionResponseTypeDef",
    "PutDraftAppVersionTemplateRequestRequestTypeDef",
    "PutDraftAppVersionTemplateResponseTypeDef",
    "RecommendationDisruptionComplianceTypeDef",
    "RecommendationItemTypeDef",
    "RecommendationTemplateTypeDef",
    "RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef",
    "RemoveDraftAppVersionResourceMappingsResponseTypeDef",
    "ResiliencyPolicyTypeDef",
    "ResiliencyScoreTypeDef",
    "ResolveAppVersionResourcesRequestRequestTypeDef",
    "ResolveAppVersionResourcesResponseTypeDef",
    "ResourceMappingTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SopRecommendationTypeDef",
    "StartAppAssessmentRequestRequestTypeDef",
    "StartAppAssessmentResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestRecommendationTypeDef",
    "UnsupportedResourceTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "UpdateResiliencyPolicyRequestRequestTypeDef",
    "UpdateResiliencyPolicyResponseTypeDef",
)

AddDraftAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "AddDraftAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appArn": str,
        "resourceMappings": Sequence["ResourceMappingTypeDef"],
    },
)

AddDraftAppVersionResourceMappingsResponseTypeDef = TypedDict(
    "AddDraftAppVersionResourceMappingsResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "resourceMappings": List["ResourceMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AlarmRecommendationTypeDef = TypedDict(
    "AlarmRecommendationTypeDef",
    {
        "name": str,
        "recommendationId": str,
        "referenceId": str,
        "type": AlarmTypeType,
        "appComponentName": NotRequired[str],
        "description": NotRequired[str],
        "items": NotRequired[List["RecommendationItemTypeDef"]],
        "prerequisite": NotRequired[str],
    },
)

AppAssessmentSummaryTypeDef = TypedDict(
    "AppAssessmentSummaryTypeDef",
    {
        "assessmentArn": str,
        "assessmentStatus": AssessmentStatusType,
        "appArn": NotRequired[str],
        "appVersion": NotRequired[str],
        "assessmentName": NotRequired[str],
        "complianceStatus": NotRequired[ComplianceStatusType],
        "cost": NotRequired["CostTypeDef"],
        "endTime": NotRequired[datetime],
        "invoker": NotRequired[AssessmentInvokerType],
        "message": NotRequired[str],
        "resiliencyScore": NotRequired[float],
        "startTime": NotRequired[datetime],
    },
)

AppAssessmentTypeDef = TypedDict(
    "AppAssessmentTypeDef",
    {
        "assessmentArn": str,
        "assessmentStatus": AssessmentStatusType,
        "invoker": AssessmentInvokerType,
        "appArn": NotRequired[str],
        "appVersion": NotRequired[str],
        "assessmentName": NotRequired[str],
        "compliance": NotRequired[Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"]],
        "complianceStatus": NotRequired[ComplianceStatusType],
        "cost": NotRequired["CostTypeDef"],
        "endTime": NotRequired[datetime],
        "message": NotRequired[str],
        "policy": NotRequired["ResiliencyPolicyTypeDef"],
        "resiliencyScore": NotRequired["ResiliencyScoreTypeDef"],
        "startTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

AppComponentComplianceTypeDef = TypedDict(
    "AppComponentComplianceTypeDef",
    {
        "appComponentName": NotRequired[str],
        "compliance": NotRequired[Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"]],
        "cost": NotRequired["CostTypeDef"],
        "message": NotRequired[str],
        "resiliencyScore": NotRequired["ResiliencyScoreTypeDef"],
        "status": NotRequired[ComplianceStatusType],
    },
)

AppComponentTypeDef = TypedDict(
    "AppComponentTypeDef",
    {
        "name": str,
        "type": str,
    },
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appArn": str,
        "creationTime": datetime,
        "name": str,
        "complianceStatus": NotRequired[AppComplianceStatusTypeType],
        "description": NotRequired[str],
        "resiliencyScore": NotRequired[float],
    },
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "appArn": str,
        "creationTime": datetime,
        "name": str,
        "complianceStatus": NotRequired[AppComplianceStatusTypeType],
        "description": NotRequired[str],
        "lastAppComplianceEvaluationTime": NotRequired[datetime],
        "lastResiliencyScoreEvaluationTime": NotRequired[datetime],
        "policyArn": NotRequired[str],
        "resiliencyScore": NotRequired[float],
        "status": NotRequired[AppStatusTypeType],
        "tags": NotRequired[Dict[str, str]],
    },
)

AppVersionSummaryTypeDef = TypedDict(
    "AppVersionSummaryTypeDef",
    {
        "appVersion": str,
    },
)

ComponentRecommendationTypeDef = TypedDict(
    "ComponentRecommendationTypeDef",
    {
        "appComponentName": str,
        "configRecommendations": List["ConfigRecommendationTypeDef"],
        "recommendationStatus": RecommendationComplianceStatusType,
    },
)

ConfigRecommendationTypeDef = TypedDict(
    "ConfigRecommendationTypeDef",
    {
        "name": str,
        "optimizationType": ConfigRecommendationOptimizationTypeType,
        "referenceId": str,
        "appComponentName": NotRequired[str],
        "compliance": NotRequired[Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"]],
        "cost": NotRequired["CostTypeDef"],
        "description": NotRequired[str],
        "haArchitecture": NotRequired[HaArchitectureType],
        "recommendationCompliance": NotRequired[
            Dict[DisruptionTypeType, "RecommendationDisruptionComplianceTypeDef"]
        ],
        "suggestedChanges": NotRequired[List[str]],
    },
)

CostTypeDef = TypedDict(
    "CostTypeDef",
    {
        "amount": float,
        "currency": str,
        "frequency": CostFrequencyType,
    },
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "policyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecommendationTemplateRequestRequestTypeDef = TypedDict(
    "CreateRecommendationTemplateRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "name": str,
        "bucketName": NotRequired[str],
        "clientToken": NotRequired[str],
        "format": NotRequired[TemplateFormatType],
        "recommendationIds": NotRequired[Sequence[str]],
        "recommendationTypes": NotRequired[Sequence[RenderRecommendationTypeType]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateRecommendationTemplateResponseTypeDef = TypedDict(
    "CreateRecommendationTemplateResponseTypeDef",
    {
        "recommendationTemplate": "RecommendationTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "CreateResiliencyPolicyRequestRequestTypeDef",
    {
        "policy": Mapping[DisruptionTypeType, "FailurePolicyTypeDef"],
        "policyName": str,
        "tier": ResiliencyPolicyTierType,
        "clientToken": NotRequired[str],
        "dataLocationConstraint": NotRequired[DataLocationConstraintType],
        "policyDescription": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateResiliencyPolicyResponseTypeDef = TypedDict(
    "CreateResiliencyPolicyResponseTypeDef",
    {
        "policy": "ResiliencyPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppAssessmentRequestRequestTypeDef = TypedDict(
    "DeleteAppAssessmentRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "clientToken": NotRequired[str],
    },
)

DeleteAppAssessmentResponseTypeDef = TypedDict(
    "DeleteAppAssessmentResponseTypeDef",
    {
        "assessmentArn": str,
        "assessmentStatus": AssessmentStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "appArn": str,
        "clientToken": NotRequired[str],
        "forceDelete": NotRequired[bool],
    },
)

DeleteAppResponseTypeDef = TypedDict(
    "DeleteAppResponseTypeDef",
    {
        "appArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecommendationTemplateRequestRequestTypeDef = TypedDict(
    "DeleteRecommendationTemplateRequestRequestTypeDef",
    {
        "recommendationTemplateArn": str,
        "clientToken": NotRequired[str],
    },
)

DeleteRecommendationTemplateResponseTypeDef = TypedDict(
    "DeleteRecommendationTemplateResponseTypeDef",
    {
        "recommendationTemplateArn": str,
        "status": RecommendationTemplateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "DeleteResiliencyPolicyRequestRequestTypeDef",
    {
        "policyArn": str,
        "clientToken": NotRequired[str],
    },
)

DeleteResiliencyPolicyResponseTypeDef = TypedDict(
    "DeleteResiliencyPolicyResponseTypeDef",
    {
        "policyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppAssessmentRequestRequestTypeDef = TypedDict(
    "DescribeAppAssessmentRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)

DescribeAppAssessmentResponseTypeDef = TypedDict(
    "DescribeAppAssessmentResponseTypeDef",
    {
        "assessment": "AppAssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppRequestRequestTypeDef = TypedDict(
    "DescribeAppRequestRequestTypeDef",
    {
        "appArn": str,
    },
)

DescribeAppResponseTypeDef = TypedDict(
    "DescribeAppResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef = TypedDict(
    "DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "resolutionId": NotRequired[str],
    },
)

DescribeAppVersionResourcesResolutionStatusResponseTypeDef = TypedDict(
    "DescribeAppVersionResourcesResolutionStatusResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "errorMessage": str,
        "resolutionId": str,
        "status": ResourceResolutionStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppVersionTemplateRequestRequestTypeDef = TypedDict(
    "DescribeAppVersionTemplateRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)

DescribeAppVersionTemplateResponseTypeDef = TypedDict(
    "DescribeAppVersionTemplateResponseTypeDef",
    {
        "appArn": str,
        "appTemplateBody": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef = TypedDict(
    "DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef",
    {
        "appArn": str,
    },
)

DescribeDraftAppVersionResourcesImportStatusResponseTypeDef = TypedDict(
    "DescribeDraftAppVersionResourcesImportStatusResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "errorMessage": str,
        "status": ResourceImportStatusTypeType,
        "statusChangeTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "DescribeResiliencyPolicyRequestRequestTypeDef",
    {
        "policyArn": str,
    },
)

DescribeResiliencyPolicyResponseTypeDef = TypedDict(
    "DescribeResiliencyPolicyResponseTypeDef",
    {
        "policy": "ResiliencyPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisruptionComplianceTypeDef = TypedDict(
    "DisruptionComplianceTypeDef",
    {
        "complianceStatus": ComplianceStatusType,
        "achievableRpoInSecs": NotRequired[int],
        "achievableRtoInSecs": NotRequired[int],
        "currentRpoInSecs": NotRequired[int],
        "currentRtoInSecs": NotRequired[int],
        "message": NotRequired[str],
        "rpoDescription": NotRequired[str],
        "rpoReferenceId": NotRequired[str],
        "rtoDescription": NotRequired[str],
        "rtoReferenceId": NotRequired[str],
    },
)

FailurePolicyTypeDef = TypedDict(
    "FailurePolicyTypeDef",
    {
        "rpoInSecs": int,
        "rtoInSecs": int,
    },
)

ImportResourcesToDraftAppVersionRequestRequestTypeDef = TypedDict(
    "ImportResourcesToDraftAppVersionRequestRequestTypeDef",
    {
        "appArn": str,
        "sourceArns": Sequence[str],
    },
)

ImportResourcesToDraftAppVersionResponseTypeDef = TypedDict(
    "ImportResourcesToDraftAppVersionResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "sourceArns": List[str],
        "status": ResourceImportStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlarmRecommendationsRequestRequestTypeDef = TypedDict(
    "ListAlarmRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAlarmRecommendationsResponseTypeDef = TypedDict(
    "ListAlarmRecommendationsResponseTypeDef",
    {
        "alarmRecommendations": List["AlarmRecommendationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppAssessmentsRequestRequestTypeDef = TypedDict(
    "ListAppAssessmentsRequestRequestTypeDef",
    {
        "appArn": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentStatus": NotRequired[Sequence[AssessmentStatusType]],
        "complianceStatus": NotRequired[ComplianceStatusType],
        "invoker": NotRequired[AssessmentInvokerType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "reverseOrder": NotRequired[bool],
    },
)

ListAppAssessmentsResponseTypeDef = TypedDict(
    "ListAppAssessmentsResponseTypeDef",
    {
        "assessmentSummaries": List["AppAssessmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppComponentCompliancesRequestRequestTypeDef = TypedDict(
    "ListAppComponentCompliancesRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAppComponentCompliancesResponseTypeDef = TypedDict(
    "ListAppComponentCompliancesResponseTypeDef",
    {
        "componentCompliances": List["AppComponentComplianceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppComponentRecommendationsRequestRequestTypeDef = TypedDict(
    "ListAppComponentRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAppComponentRecommendationsResponseTypeDef = TypedDict(
    "ListAppComponentRecommendationsResponseTypeDef",
    {
        "componentRecommendations": List["ComponentRecommendationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "ListAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAppVersionResourceMappingsResponseTypeDef = TypedDict(
    "ListAppVersionResourceMappingsResponseTypeDef",
    {
        "nextToken": str,
        "resourceMappings": List["ResourceMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "ListAppVersionResourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "resolutionId": NotRequired[str],
    },
)

ListAppVersionResourcesResponseTypeDef = TypedDict(
    "ListAppVersionResourcesResponseTypeDef",
    {
        "nextToken": str,
        "physicalResources": List["PhysicalResourceTypeDef"],
        "resolutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppVersionsRequestRequestTypeDef = TypedDict(
    "ListAppVersionsRequestRequestTypeDef",
    {
        "appArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAppVersionsResponseTypeDef = TypedDict(
    "ListAppVersionsResponseTypeDef",
    {
        "appVersions": List["AppVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "appArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "appSummaries": List["AppSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationTemplatesRequestRequestTypeDef = TypedDict(
    "ListRecommendationTemplatesRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "recommendationTemplateArn": NotRequired[str],
        "reverseOrder": NotRequired[bool],
        "status": NotRequired[Sequence[RecommendationTemplateStatusType]],
    },
)

ListRecommendationTemplatesResponseTypeDef = TypedDict(
    "ListRecommendationTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationTemplates": List["RecommendationTemplateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResiliencyPoliciesRequestRequestTypeDef = TypedDict(
    "ListResiliencyPoliciesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "policyName": NotRequired[str],
    },
)

ListResiliencyPoliciesResponseTypeDef = TypedDict(
    "ListResiliencyPoliciesResponseTypeDef",
    {
        "nextToken": str,
        "resiliencyPolicies": List["ResiliencyPolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSopRecommendationsRequestRequestTypeDef = TypedDict(
    "ListSopRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSopRecommendationsResponseTypeDef = TypedDict(
    "ListSopRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "sopRecommendations": List["SopRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSuggestedResiliencyPoliciesRequestRequestTypeDef = TypedDict(
    "ListSuggestedResiliencyPoliciesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSuggestedResiliencyPoliciesResponseTypeDef = TypedDict(
    "ListSuggestedResiliencyPoliciesResponseTypeDef",
    {
        "nextToken": str,
        "resiliencyPolicies": List["ResiliencyPolicyTypeDef"],
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

ListTestRecommendationsRequestRequestTypeDef = TypedDict(
    "ListTestRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTestRecommendationsResponseTypeDef = TypedDict(
    "ListTestRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "testRecommendations": List["TestRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUnsupportedAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "ListUnsupportedAppVersionResourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "resolutionId": NotRequired[str],
    },
)

ListUnsupportedAppVersionResourcesResponseTypeDef = TypedDict(
    "ListUnsupportedAppVersionResourcesResponseTypeDef",
    {
        "nextToken": str,
        "resolutionId": str,
        "unsupportedResources": List["UnsupportedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogicalResourceIdTypeDef = TypedDict(
    "LogicalResourceIdTypeDef",
    {
        "identifier": str,
        "logicalStackName": NotRequired[str],
        "resourceGroupName": NotRequired[str],
    },
)

PhysicalResourceIdTypeDef = TypedDict(
    "PhysicalResourceIdTypeDef",
    {
        "identifier": str,
        "type": PhysicalIdentifierTypeType,
        "awsAccountId": NotRequired[str],
        "awsRegion": NotRequired[str],
    },
)

PhysicalResourceTypeDef = TypedDict(
    "PhysicalResourceTypeDef",
    {
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": "PhysicalResourceIdTypeDef",
        "resourceType": str,
        "appComponents": NotRequired[List["AppComponentTypeDef"]],
        "resourceName": NotRequired[str],
    },
)

PublishAppVersionRequestRequestTypeDef = TypedDict(
    "PublishAppVersionRequestRequestTypeDef",
    {
        "appArn": str,
    },
)

PublishAppVersionResponseTypeDef = TypedDict(
    "PublishAppVersionResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDraftAppVersionTemplateRequestRequestTypeDef = TypedDict(
    "PutDraftAppVersionTemplateRequestRequestTypeDef",
    {
        "appArn": str,
        "appTemplateBody": str,
    },
)

PutDraftAppVersionTemplateResponseTypeDef = TypedDict(
    "PutDraftAppVersionTemplateResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationDisruptionComplianceTypeDef = TypedDict(
    "RecommendationDisruptionComplianceTypeDef",
    {
        "expectedComplianceStatus": ComplianceStatusType,
        "expectedRpoDescription": NotRequired[str],
        "expectedRpoInSecs": NotRequired[int],
        "expectedRtoDescription": NotRequired[str],
        "expectedRtoInSecs": NotRequired[int],
    },
)

RecommendationItemTypeDef = TypedDict(
    "RecommendationItemTypeDef",
    {
        "alreadyImplemented": NotRequired[bool],
        "resourceId": NotRequired[str],
        "targetAccountId": NotRequired[str],
        "targetRegion": NotRequired[str],
    },
)

RecommendationTemplateTypeDef = TypedDict(
    "RecommendationTemplateTypeDef",
    {
        "assessmentArn": str,
        "format": TemplateFormatType,
        "name": str,
        "recommendationTemplateArn": str,
        "recommendationTypes": List[RenderRecommendationTypeType],
        "status": RecommendationTemplateStatusType,
        "appArn": NotRequired[str],
        "endTime": NotRequired[datetime],
        "message": NotRequired[str],
        "needsReplacements": NotRequired[bool],
        "recommendationIds": NotRequired[List[str]],
        "startTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "templatesLocation": NotRequired["S3LocationTypeDef"],
    },
)

RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appArn": str,
        "appRegistryAppNames": NotRequired[Sequence[str]],
        "logicalStackNames": NotRequired[Sequence[str]],
        "resourceGroupNames": NotRequired[Sequence[str]],
        "resourceNames": NotRequired[Sequence[str]],
    },
)

RemoveDraftAppVersionResourceMappingsResponseTypeDef = TypedDict(
    "RemoveDraftAppVersionResourceMappingsResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResiliencyPolicyTypeDef = TypedDict(
    "ResiliencyPolicyTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "dataLocationConstraint": NotRequired[DataLocationConstraintType],
        "estimatedCostTier": NotRequired[EstimatedCostTierType],
        "policy": NotRequired[Dict[DisruptionTypeType, "FailurePolicyTypeDef"]],
        "policyArn": NotRequired[str],
        "policyDescription": NotRequired[str],
        "policyName": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "tier": NotRequired[ResiliencyPolicyTierType],
    },
)

ResiliencyScoreTypeDef = TypedDict(
    "ResiliencyScoreTypeDef",
    {
        "disruptionScore": Dict[DisruptionTypeType, float],
        "score": float,
    },
)

ResolveAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "ResolveAppVersionResourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)

ResolveAppVersionResourcesResponseTypeDef = TypedDict(
    "ResolveAppVersionResourcesResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "resolutionId": str,
        "status": ResourceResolutionStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceMappingTypeDef = TypedDict(
    "ResourceMappingTypeDef",
    {
        "mappingType": ResourceMappingTypeType,
        "physicalResourceId": "PhysicalResourceIdTypeDef",
        "appRegistryAppName": NotRequired[str],
        "logicalStackName": NotRequired[str],
        "resourceGroupName": NotRequired[str],
        "resourceName": NotRequired[str],
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

SopRecommendationTypeDef = TypedDict(
    "SopRecommendationTypeDef",
    {
        "recommendationId": str,
        "referenceId": str,
        "serviceType": Literal["SSM"],
        "appComponentName": NotRequired[str],
        "description": NotRequired[str],
        "items": NotRequired[List["RecommendationItemTypeDef"]],
        "name": NotRequired[str],
        "prerequisite": NotRequired[str],
    },
)

StartAppAssessmentRequestRequestTypeDef = TypedDict(
    "StartAppAssessmentRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "assessmentName": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartAppAssessmentResponseTypeDef = TypedDict(
    "StartAppAssessmentResponseTypeDef",
    {
        "assessment": "AppAssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TestRecommendationTypeDef = TypedDict(
    "TestRecommendationTypeDef",
    {
        "referenceId": str,
        "appComponentName": NotRequired[str],
        "description": NotRequired[str],
        "intent": NotRequired[str],
        "items": NotRequired[List["RecommendationItemTypeDef"]],
        "name": NotRequired[str],
        "prerequisite": NotRequired[str],
        "recommendationId": NotRequired[str],
        "risk": NotRequired[TestRiskType],
        "type": NotRequired[TestTypeType],
    },
)

UnsupportedResourceTypeDef = TypedDict(
    "UnsupportedResourceTypeDef",
    {
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": "PhysicalResourceIdTypeDef",
        "resourceType": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "appArn": str,
        "clearResiliencyPolicyArn": NotRequired[bool],
        "description": NotRequired[str],
        "policyArn": NotRequired[str],
    },
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "UpdateResiliencyPolicyRequestRequestTypeDef",
    {
        "policyArn": str,
        "dataLocationConstraint": NotRequired[DataLocationConstraintType],
        "policy": NotRequired[Mapping[DisruptionTypeType, "FailurePolicyTypeDef"]],
        "policyDescription": NotRequired[str],
        "policyName": NotRequired[str],
        "tier": NotRequired[ResiliencyPolicyTierType],
    },
)

UpdateResiliencyPolicyResponseTypeDef = TypedDict(
    "UpdateResiliencyPolicyResponseTypeDef",
    {
        "policy": "ResiliencyPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
