"""
Type annotations for compute-optimizer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    CpuVendorArchitectureType,
    CurrencyType,
    CurrentPerformanceRiskType,
    EBSFindingType,
    EBSMetricNameType,
    EnhancedInfrastructureMetricsType,
    ExportableAutoScalingGroupFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableVolumeFieldType,
    FilterNameType,
    FindingReasonCodeType,
    FindingType,
    InferredWorkloadTypesPreferenceType,
    InferredWorkloadTypeType,
    InstanceRecommendationFindingReasonCodeType,
    JobFilterNameType,
    JobStatusType,
    LambdaFunctionMemoryMetricStatisticType,
    LambdaFunctionMetricNameType,
    LambdaFunctionMetricStatisticType,
    LambdaFunctionRecommendationFilterNameType,
    LambdaFunctionRecommendationFindingReasonCodeType,
    LambdaFunctionRecommendationFindingType,
    MetricNameType,
    MetricStatisticType,
    MigrationEffortType,
    PlatformDifferenceType,
    RecommendationPreferenceNameType,
    RecommendationSourceTypeType,
    ResourceTypeType,
    ScopeNameType,
    StatusType,
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
    "AccountEnrollmentStatusTypeDef",
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "CurrentPerformanceRiskRatingsTypeDef",
    "DeleteRecommendationPreferencesRequestRequestTypeDef",
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "EBSFilterTypeDef",
    "EBSUtilizationMetricTypeDef",
    "EffectiveRecommendationPreferencesTypeDef",
    "EnrollmentFilterTypeDef",
    "EstimatedMonthlySavingsTypeDef",
    "ExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEBSVolumeRecommendationsRequestRequestTypeDef",
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsRequestRequestTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "ExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetEffectiveRecommendationPreferencesRequestRequestTypeDef",
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetEnrollmentStatusesForOrganizationRequestRequestTypeDef",
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetRecommendationErrorTypeDef",
    "GetRecommendationPreferencesRequestRequestTypeDef",
    "GetRecommendationPreferencesResponseTypeDef",
    "GetRecommendationSummariesRequestRequestTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "JobFilterTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "ProjectedMetricTypeDef",
    "PutRecommendationPreferencesRequestRequestTypeDef",
    "ReasonCodeSummaryTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationPreferencesDetailTypeDef",
    "RecommendationPreferencesTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "SavingsOpportunityTypeDef",
    "ScopeTypeDef",
    "SummaryTypeDef",
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UtilizationMetricTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
)

AccountEnrollmentStatusTypeDef = TypedDict(
    "AccountEnrollmentStatusTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[StatusType],
        "statusReason": NotRequired[str],
        "lastUpdatedTimestamp": NotRequired[datetime],
    },
)

AutoScalingGroupConfigurationTypeDef = TypedDict(
    "AutoScalingGroupConfigurationTypeDef",
    {
        "desiredCapacity": NotRequired[int],
        "minSize": NotRequired[int],
        "maxSize": NotRequired[int],
        "instanceType": NotRequired[str],
    },
)

AutoScalingGroupRecommendationOptionTypeDef = TypedDict(
    "AutoScalingGroupRecommendationOptionTypeDef",
    {
        "configuration": NotRequired["AutoScalingGroupConfigurationTypeDef"],
        "projectedUtilizationMetrics": NotRequired[List["UtilizationMetricTypeDef"]],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired["SavingsOpportunityTypeDef"],
        "migrationEffort": NotRequired[MigrationEffortType],
    },
)

AutoScalingGroupRecommendationTypeDef = TypedDict(
    "AutoScalingGroupRecommendationTypeDef",
    {
        "accountId": NotRequired[str],
        "autoScalingGroupArn": NotRequired[str],
        "autoScalingGroupName": NotRequired[str],
        "finding": NotRequired[FindingType],
        "utilizationMetrics": NotRequired[List["UtilizationMetricTypeDef"]],
        "lookBackPeriodInDays": NotRequired[float],
        "currentConfiguration": NotRequired["AutoScalingGroupConfigurationTypeDef"],
        "recommendationOptions": NotRequired[List["AutoScalingGroupRecommendationOptionTypeDef"]],
        "lastRefreshTimestamp": NotRequired[datetime],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            "EffectiveRecommendationPreferencesTypeDef"
        ],
        "inferredWorkloadTypes": NotRequired[List[InferredWorkloadTypeType]],
    },
)

CurrentPerformanceRiskRatingsTypeDef = TypedDict(
    "CurrentPerformanceRiskRatingsTypeDef",
    {
        "high": NotRequired[int],
        "medium": NotRequired[int],
        "low": NotRequired[int],
        "veryLow": NotRequired[int],
    },
)

DeleteRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "DeleteRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "recommendationPreferenceNames": Sequence[RecommendationPreferenceNameType],
        "scope": NotRequired["ScopeTypeDef"],
    },
)

DescribeRecommendationExportJobsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    {
        "jobIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["JobFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeRecommendationExportJobsResponseTypeDef = TypedDict(
    "DescribeRecommendationExportJobsResponseTypeDef",
    {
        "recommendationExportJobs": List["RecommendationExportJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSFilterTypeDef = TypedDict(
    "EBSFilterTypeDef",
    {
        "name": NotRequired[Literal["Finding"]],
        "values": NotRequired[Sequence[str]],
    },
)

EBSUtilizationMetricTypeDef = TypedDict(
    "EBSUtilizationMetricTypeDef",
    {
        "name": NotRequired[EBSMetricNameType],
        "statistic": NotRequired[MetricStatisticType],
        "value": NotRequired[float],
    },
)

EffectiveRecommendationPreferencesTypeDef = TypedDict(
    "EffectiveRecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": NotRequired[List[CpuVendorArchitectureType]],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "inferredWorkloadTypes": NotRequired[InferredWorkloadTypesPreferenceType],
    },
)

EnrollmentFilterTypeDef = TypedDict(
    "EnrollmentFilterTypeDef",
    {
        "name": NotRequired[Literal["Status"]],
        "values": NotRequired[Sequence[str]],
    },
)

EstimatedMonthlySavingsTypeDef = TypedDict(
    "EstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)

ExportAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "fieldsToExport": NotRequired[Sequence[ExportableAutoScalingGroupFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
        "recommendationPreferences": NotRequired["RecommendationPreferencesTypeDef"],
    },
)

ExportAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportDestinationTypeDef = TypedDict(
    "ExportDestinationTypeDef",
    {
        "s3": NotRequired["S3DestinationTypeDef"],
    },
)

ExportEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["EBSFilterTypeDef"]],
        "fieldsToExport": NotRequired[Sequence[ExportableVolumeFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
    },
)

ExportEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "fieldsToExport": NotRequired[Sequence[ExportableInstanceFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
        "recommendationPreferences": NotRequired["RecommendationPreferencesTypeDef"],
    },
)

ExportEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": "S3DestinationConfigTypeDef",
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["LambdaFunctionRecommendationFilterTypeDef"]],
        "fieldsToExport": NotRequired[Sequence[ExportableLambdaFunctionFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
    },
)

ExportLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": "S3DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[FilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)

GetAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "autoScalingGroupArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "recommendationPreferences": NotRequired["RecommendationPreferencesTypeDef"],
    },
)

GetAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "autoScalingGroupRecommendations": List["AutoScalingGroupRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "volumeArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["EBSFilterTypeDef"]],
        "accountIds": NotRequired[Sequence[str]],
    },
)

GetEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "volumeRecommendations": List["VolumeRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "instanceArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "accountIds": NotRequired[Sequence[str]],
        "recommendationPreferences": NotRequired["RecommendationPreferencesTypeDef"],
    },
)

GetEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "instanceRecommendations": List["InstanceRecommendationTypeDef"],
        "errors": List["GetRecommendationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEC2RecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "instanceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "recommendationPreferences": NotRequired["RecommendationPreferencesTypeDef"],
    },
)

GetEC2RecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List["RecommendedOptionProjectedMetricTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEffectiveRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "GetEffectiveRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetEffectiveRecommendationPreferencesResponseTypeDef = TypedDict(
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    {
        "enhancedInfrastructureMetrics": EnhancedInfrastructureMetricsType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnrollmentStatusResponseTypeDef = TypedDict(
    "GetEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "memberAccountsEnrolled": bool,
        "lastUpdatedTimestamp": datetime,
        "numberOfMemberAccountsOptedIn": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnrollmentStatusesForOrganizationRequestRequestTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["EnrollmentFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetEnrollmentStatusesForOrganizationResponseTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    {
        "accountEnrollmentStatuses": List["AccountEnrollmentStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "functionArns": NotRequired[Sequence[str]],
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["LambdaFunctionRecommendationFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "lambdaFunctionRecommendations": List["LambdaFunctionRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationErrorTypeDef = TypedDict(
    "GetRecommendationErrorTypeDef",
    {
        "identifier": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

GetRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "GetRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scope": NotRequired["ScopeTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetRecommendationPreferencesResponseTypeDef = TypedDict(
    "GetRecommendationPreferencesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationPreferencesDetails": List["RecommendationPreferencesDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationSummariesRequestRequestTypeDef = TypedDict(
    "GetRecommendationSummariesRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetRecommendationSummariesResponseTypeDef = TypedDict(
    "GetRecommendationSummariesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List["RecommendationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceRecommendationOptionTypeDef = TypedDict(
    "InstanceRecommendationOptionTypeDef",
    {
        "instanceType": NotRequired[str],
        "projectedUtilizationMetrics": NotRequired[List["UtilizationMetricTypeDef"]],
        "platformDifferences": NotRequired[List[PlatformDifferenceType]],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired["SavingsOpportunityTypeDef"],
        "migrationEffort": NotRequired[MigrationEffortType],
    },
)

InstanceRecommendationTypeDef = TypedDict(
    "InstanceRecommendationTypeDef",
    {
        "instanceArn": NotRequired[str],
        "accountId": NotRequired[str],
        "instanceName": NotRequired[str],
        "currentInstanceType": NotRequired[str],
        "finding": NotRequired[FindingType],
        "findingReasonCodes": NotRequired[List[InstanceRecommendationFindingReasonCodeType]],
        "utilizationMetrics": NotRequired[List["UtilizationMetricTypeDef"]],
        "lookBackPeriodInDays": NotRequired[float],
        "recommendationOptions": NotRequired[List["InstanceRecommendationOptionTypeDef"]],
        "recommendationSources": NotRequired[List["RecommendationSourceTypeDef"]],
        "lastRefreshTimestamp": NotRequired[datetime],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            "EffectiveRecommendationPreferencesTypeDef"
        ],
        "inferredWorkloadTypes": NotRequired[List[InferredWorkloadTypeType]],
    },
)

JobFilterTypeDef = TypedDict(
    "JobFilterTypeDef",
    {
        "name": NotRequired[JobFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)

LambdaFunctionMemoryProjectedMetricTypeDef = TypedDict(
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    {
        "name": NotRequired[Literal["Duration"]],
        "statistic": NotRequired[LambdaFunctionMemoryMetricStatisticType],
        "value": NotRequired[float],
    },
)

LambdaFunctionMemoryRecommendationOptionTypeDef = TypedDict(
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    {
        "rank": NotRequired[int],
        "memorySize": NotRequired[int],
        "projectedUtilizationMetrics": NotRequired[
            List["LambdaFunctionMemoryProjectedMetricTypeDef"]
        ],
        "savingsOpportunity": NotRequired["SavingsOpportunityTypeDef"],
    },
)

LambdaFunctionRecommendationFilterTypeDef = TypedDict(
    "LambdaFunctionRecommendationFilterTypeDef",
    {
        "name": NotRequired[LambdaFunctionRecommendationFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)

LambdaFunctionRecommendationTypeDef = TypedDict(
    "LambdaFunctionRecommendationTypeDef",
    {
        "functionArn": NotRequired[str],
        "functionVersion": NotRequired[str],
        "accountId": NotRequired[str],
        "currentMemorySize": NotRequired[int],
        "numberOfInvocations": NotRequired[int],
        "utilizationMetrics": NotRequired[List["LambdaFunctionUtilizationMetricTypeDef"]],
        "lookbackPeriodInDays": NotRequired[float],
        "lastRefreshTimestamp": NotRequired[datetime],
        "finding": NotRequired[LambdaFunctionRecommendationFindingType],
        "findingReasonCodes": NotRequired[List[LambdaFunctionRecommendationFindingReasonCodeType]],
        "memorySizeRecommendationOptions": NotRequired[
            List["LambdaFunctionMemoryRecommendationOptionTypeDef"]
        ],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
    },
)

LambdaFunctionUtilizationMetricTypeDef = TypedDict(
    "LambdaFunctionUtilizationMetricTypeDef",
    {
        "name": NotRequired[LambdaFunctionMetricNameType],
        "statistic": NotRequired[LambdaFunctionMetricStatisticType],
        "value": NotRequired[float],
    },
)

ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {
        "name": NotRequired[MetricNameType],
        "timestamps": NotRequired[List[datetime]],
        "values": NotRequired[List[float]],
    },
)

PutRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "PutRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scope": NotRequired["ScopeTypeDef"],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "inferredWorkloadTypes": NotRequired[InferredWorkloadTypesPreferenceType],
    },
)

ReasonCodeSummaryTypeDef = TypedDict(
    "ReasonCodeSummaryTypeDef",
    {
        "name": NotRequired[FindingReasonCodeType],
        "value": NotRequired[float],
    },
)

RecommendationExportJobTypeDef = TypedDict(
    "RecommendationExportJobTypeDef",
    {
        "jobId": NotRequired[str],
        "destination": NotRequired["ExportDestinationTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "status": NotRequired[JobStatusType],
        "creationTimestamp": NotRequired[datetime],
        "lastUpdatedTimestamp": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)

RecommendationPreferencesDetailTypeDef = TypedDict(
    "RecommendationPreferencesDetailTypeDef",
    {
        "scope": NotRequired["ScopeTypeDef"],
        "resourceType": NotRequired[ResourceTypeType],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "inferredWorkloadTypes": NotRequired[InferredWorkloadTypesPreferenceType],
    },
)

RecommendationPreferencesTypeDef = TypedDict(
    "RecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": NotRequired[Sequence[CpuVendorArchitectureType]],
    },
)

RecommendationSourceTypeDef = TypedDict(
    "RecommendationSourceTypeDef",
    {
        "recommendationSourceArn": NotRequired[str],
        "recommendationSourceType": NotRequired[RecommendationSourceTypeType],
    },
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "summaries": NotRequired[List["SummaryTypeDef"]],
        "recommendationResourceType": NotRequired[RecommendationSourceTypeType],
        "accountId": NotRequired[str],
        "savingsOpportunity": NotRequired["SavingsOpportunityTypeDef"],
        "currentPerformanceRiskRatings": NotRequired["CurrentPerformanceRiskRatingsTypeDef"],
    },
)

RecommendedOptionProjectedMetricTypeDef = TypedDict(
    "RecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedInstanceType": NotRequired[str],
        "rank": NotRequired[int],
        "projectedMetrics": NotRequired[List["ProjectedMetricTypeDef"]],
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

S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "metadataKey": NotRequired[str],
    },
)

SavingsOpportunityTypeDef = TypedDict(
    "SavingsOpportunityTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired["EstimatedMonthlySavingsTypeDef"],
    },
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "name": NotRequired[ScopeNameType],
        "value": NotRequired[str],
    },
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "name": NotRequired[FindingType],
        "value": NotRequired[float],
        "reasonCodeSummaries": NotRequired[List["ReasonCodeSummaryTypeDef"]],
    },
)

UpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "status": StatusType,
        "includeMemberAccounts": NotRequired[bool],
    },
)

UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtilizationMetricTypeDef = TypedDict(
    "UtilizationMetricTypeDef",
    {
        "name": NotRequired[MetricNameType],
        "statistic": NotRequired[MetricStatisticType],
        "value": NotRequired[float],
    },
)

VolumeConfigurationTypeDef = TypedDict(
    "VolumeConfigurationTypeDef",
    {
        "volumeType": NotRequired[str],
        "volumeSize": NotRequired[int],
        "volumeBaselineIOPS": NotRequired[int],
        "volumeBurstIOPS": NotRequired[int],
        "volumeBaselineThroughput": NotRequired[int],
        "volumeBurstThroughput": NotRequired[int],
    },
)

VolumeRecommendationOptionTypeDef = TypedDict(
    "VolumeRecommendationOptionTypeDef",
    {
        "configuration": NotRequired["VolumeConfigurationTypeDef"],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired["SavingsOpportunityTypeDef"],
    },
)

VolumeRecommendationTypeDef = TypedDict(
    "VolumeRecommendationTypeDef",
    {
        "volumeArn": NotRequired[str],
        "accountId": NotRequired[str],
        "currentConfiguration": NotRequired["VolumeConfigurationTypeDef"],
        "finding": NotRequired[EBSFindingType],
        "utilizationMetrics": NotRequired[List["EBSUtilizationMetricTypeDef"]],
        "lookBackPeriodInDays": NotRequired[float],
        "volumeRecommendationOptions": NotRequired[List["VolumeRecommendationOptionTypeDef"]],
        "lastRefreshTimestamp": NotRequired[datetime],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
    },
)
