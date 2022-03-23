"""
Type annotations for ce service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ce/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_ce.type_defs import AnomalyDateIntervalTypeDef

    data: AnomalyDateIntervalTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccountScopeType,
    AnomalyFeedbackTypeType,
    AnomalySubscriptionFrequencyType,
    ContextType,
    CostCategoryInheritedValueDimensionNameType,
    CostCategoryRuleTypeType,
    CostCategorySplitChargeMethodType,
    CostCategoryStatusType,
    DimensionType,
    FindingReasonCodeType,
    GranularityType,
    GroupDefinitionTypeType,
    LookbackPeriodInDaysType,
    MatchOptionType,
    MetricType,
    MonitorTypeType,
    NumericOperatorType,
    OfferingClassType,
    PaymentOptionType,
    PlatformDifferenceType,
    RecommendationTargetType,
    RightsizingTypeType,
    SavingsPlansDataTypeType,
    SortOrderType,
    SubscriberStatusType,
    SubscriberTypeType,
    SupportedSavingsPlansTypeType,
    TermInYearsType,
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
    "AnomalyDateIntervalTypeDef",
    "AnomalyMonitorTypeDef",
    "AnomalyScoreTypeDef",
    "AnomalySubscriptionTypeDef",
    "AnomalyTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategoryRuleTypeDef",
    "CostCategorySplitChargeRuleParameterTypeDef",
    "CostCategorySplitChargeRuleTypeDef",
    "CostCategoryTypeDef",
    "CostCategoryValuesTypeDef",
    "CoverageByTimeTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "CoverageTypeDef",
    "CreateAnomalyMonitorRequestRequestTypeDef",
    "CreateAnomalyMonitorResponseTypeDef",
    "CreateAnomalySubscriptionRequestRequestTypeDef",
    "CreateAnomalySubscriptionResponseTypeDef",
    "CreateCostCategoryDefinitionRequestRequestTypeDef",
    "CreateCostCategoryDefinitionResponseTypeDef",
    "CurrentInstanceTypeDef",
    "DateIntervalTypeDef",
    "DeleteAnomalyMonitorRequestRequestTypeDef",
    "DeleteAnomalySubscriptionRequestRequestTypeDef",
    "DeleteCostCategoryDefinitionRequestRequestTypeDef",
    "DeleteCostCategoryDefinitionResponseTypeDef",
    "DescribeCostCategoryDefinitionRequestRequestTypeDef",
    "DescribeCostCategoryDefinitionResponseTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "DiskResourceUtilizationTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "ExpressionTypeDef",
    "ForecastResultTypeDef",
    "GetAnomaliesRequestRequestTypeDef",
    "GetAnomaliesResponseTypeDef",
    "GetAnomalyMonitorsRequestRequestTypeDef",
    "GetAnomalyMonitorsResponseTypeDef",
    "GetAnomalySubscriptionsRequestRequestTypeDef",
    "GetAnomalySubscriptionsResponseTypeDef",
    "GetCostAndUsageRequestRequestTypeDef",
    "GetCostAndUsageResponseTypeDef",
    "GetCostAndUsageWithResourcesRequestRequestTypeDef",
    "GetCostAndUsageWithResourcesResponseTypeDef",
    "GetCostCategoriesRequestRequestTypeDef",
    "GetCostCategoriesResponseTypeDef",
    "GetCostForecastRequestRequestTypeDef",
    "GetCostForecastResponseTypeDef",
    "GetDimensionValuesRequestRequestTypeDef",
    "GetDimensionValuesResponseTypeDef",
    "GetReservationCoverageRequestRequestTypeDef",
    "GetReservationCoverageResponseTypeDef",
    "GetReservationPurchaseRecommendationRequestRequestTypeDef",
    "GetReservationPurchaseRecommendationResponseTypeDef",
    "GetReservationUtilizationRequestRequestTypeDef",
    "GetReservationUtilizationResponseTypeDef",
    "GetRightsizingRecommendationRequestRequestTypeDef",
    "GetRightsizingRecommendationResponseTypeDef",
    "GetSavingsPlansCoverageRequestRequestTypeDef",
    "GetSavingsPlansCoverageResponseTypeDef",
    "GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    "GetSavingsPlansUtilizationRequestRequestTypeDef",
    "GetSavingsPlansUtilizationResponseTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetUsageForecastRequestRequestTypeDef",
    "GetUsageForecastResponseTypeDef",
    "GroupDefinitionTypeDef",
    "GroupTypeDef",
    "ImpactTypeDef",
    "InstanceDetailsTypeDef",
    "ListCostCategoryDefinitionsRequestRequestTypeDef",
    "ListCostCategoryDefinitionsResponseTypeDef",
    "MetricValueTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "NetworkResourceUtilizationTypeDef",
    "ProvideAnomalyFeedbackRequestRequestTypeDef",
    "ProvideAnomalyFeedbackResponseTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ReservationAggregatesTypeDef",
    "ReservationCoverageGroupTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceUtilizationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultByTimeTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "RightsizingRecommendationTypeDef",
    "RootCauseTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "SortDefinitionTypeDef",
    "SubscriberTypeDef",
    "TagValuesTypeDef",
    "TargetInstanceTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "TotalImpactFilterTypeDef",
    "UpdateAnomalyMonitorRequestRequestTypeDef",
    "UpdateAnomalyMonitorResponseTypeDef",
    "UpdateAnomalySubscriptionRequestRequestTypeDef",
    "UpdateAnomalySubscriptionResponseTypeDef",
    "UpdateCostCategoryDefinitionRequestRequestTypeDef",
    "UpdateCostCategoryDefinitionResponseTypeDef",
    "UtilizationByTimeTypeDef",
)

AnomalyDateIntervalTypeDef = TypedDict(
    "AnomalyDateIntervalTypeDef",
    {
        "StartDate": str,
        "EndDate": NotRequired[str],
    },
)

AnomalyMonitorTypeDef = TypedDict(
    "AnomalyMonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorType": MonitorTypeType,
        "MonitorArn": NotRequired[str],
        "CreationDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "LastEvaluatedDate": NotRequired[str],
        "MonitorDimension": NotRequired[Literal["SERVICE"]],
        "MonitorSpecification": NotRequired["ExpressionTypeDef"],
        "DimensionalValueCount": NotRequired[int],
    },
)

AnomalyScoreTypeDef = TypedDict(
    "AnomalyScoreTypeDef",
    {
        "MaxScore": float,
        "CurrentScore": float,
    },
)

AnomalySubscriptionTypeDef = TypedDict(
    "AnomalySubscriptionTypeDef",
    {
        "MonitorArnList": Sequence[str],
        "Subscribers": Sequence["SubscriberTypeDef"],
        "Threshold": float,
        "Frequency": AnomalySubscriptionFrequencyType,
        "SubscriptionName": str,
        "SubscriptionArn": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)

AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "AnomalyId": str,
        "AnomalyScore": "AnomalyScoreTypeDef",
        "Impact": "ImpactTypeDef",
        "MonitorArn": str,
        "AnomalyStartDate": NotRequired[str],
        "AnomalyEndDate": NotRequired[str],
        "DimensionValue": NotRequired[str],
        "RootCauses": NotRequired[List["RootCauseTypeDef"]],
        "Feedback": NotRequired[AnomalyFeedbackTypeType],
    },
)

CostCategoryInheritedValueDimensionTypeDef = TypedDict(
    "CostCategoryInheritedValueDimensionTypeDef",
    {
        "DimensionName": NotRequired[CostCategoryInheritedValueDimensionNameType],
        "DimensionKey": NotRequired[str],
    },
)

CostCategoryProcessingStatusTypeDef = TypedDict(
    "CostCategoryProcessingStatusTypeDef",
    {
        "Component": NotRequired[Literal["COST_EXPLORER"]],
        "Status": NotRequired[CostCategoryStatusType],
    },
)

CostCategoryReferenceTypeDef = TypedDict(
    "CostCategoryReferenceTypeDef",
    {
        "CostCategoryArn": NotRequired[str],
        "Name": NotRequired[str],
        "EffectiveStart": NotRequired[str],
        "EffectiveEnd": NotRequired[str],
        "NumberOfRules": NotRequired[int],
        "ProcessingStatus": NotRequired[List["CostCategoryProcessingStatusTypeDef"]],
        "Values": NotRequired[List[str]],
        "DefaultValue": NotRequired[str],
    },
)

CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": NotRequired[str],
        "Rule": NotRequired["ExpressionTypeDef"],
        "InheritedValue": NotRequired["CostCategoryInheritedValueDimensionTypeDef"],
        "Type": NotRequired[CostCategoryRuleTypeType],
    },
)

CostCategorySplitChargeRuleParameterTypeDef = TypedDict(
    "CostCategorySplitChargeRuleParameterTypeDef",
    {
        "Type": Literal["ALLOCATION_PERCENTAGES"],
        "Values": Sequence[str],
    },
)

CostCategorySplitChargeRuleTypeDef = TypedDict(
    "CostCategorySplitChargeRuleTypeDef",
    {
        "Source": str,
        "Targets": Sequence[str],
        "Method": CostCategorySplitChargeMethodType,
        "Parameters": NotRequired[Sequence["CostCategorySplitChargeRuleParameterTypeDef"]],
    },
)

CostCategoryTypeDef = TypedDict(
    "CostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
        "EffectiveEnd": NotRequired[str],
        "SplitChargeRules": NotRequired[List["CostCategorySplitChargeRuleTypeDef"]],
        "ProcessingStatus": NotRequired[List["CostCategoryProcessingStatusTypeDef"]],
        "DefaultValue": NotRequired[str],
    },
)

CostCategoryValuesTypeDef = TypedDict(
    "CostCategoryValuesTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MatchOptions": NotRequired[Sequence[MatchOptionType]],
    },
)

CoverageByTimeTypeDef = TypedDict(
    "CoverageByTimeTypeDef",
    {
        "TimePeriod": NotRequired["DateIntervalTypeDef"],
        "Groups": NotRequired[List["ReservationCoverageGroupTypeDef"]],
        "Total": NotRequired["CoverageTypeDef"],
    },
)

CoverageCostTypeDef = TypedDict(
    "CoverageCostTypeDef",
    {
        "OnDemandCost": NotRequired[str],
    },
)

CoverageHoursTypeDef = TypedDict(
    "CoverageHoursTypeDef",
    {
        "OnDemandHours": NotRequired[str],
        "ReservedHours": NotRequired[str],
        "TotalRunningHours": NotRequired[str],
        "CoverageHoursPercentage": NotRequired[str],
    },
)

CoverageNormalizedUnitsTypeDef = TypedDict(
    "CoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": NotRequired[str],
        "ReservedNormalizedUnits": NotRequired[str],
        "TotalRunningNormalizedUnits": NotRequired[str],
        "CoverageNormalizedUnitsPercentage": NotRequired[str],
    },
)

CoverageTypeDef = TypedDict(
    "CoverageTypeDef",
    {
        "CoverageHours": NotRequired["CoverageHoursTypeDef"],
        "CoverageNormalizedUnits": NotRequired["CoverageNormalizedUnitsTypeDef"],
        "CoverageCost": NotRequired["CoverageCostTypeDef"],
    },
)

CreateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "CreateAnomalyMonitorRequestRequestTypeDef",
    {
        "AnomalyMonitor": "AnomalyMonitorTypeDef",
    },
)

CreateAnomalyMonitorResponseTypeDef = TypedDict(
    "CreateAnomalyMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "CreateAnomalySubscriptionRequestRequestTypeDef",
    {
        "AnomalySubscription": "AnomalySubscriptionTypeDef",
    },
)

CreateAnomalySubscriptionResponseTypeDef = TypedDict(
    "CreateAnomalySubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": Sequence["CostCategoryRuleTypeDef"],
        "DefaultValue": NotRequired[str],
        "SplitChargeRules": NotRequired[Sequence["CostCategorySplitChargeRuleTypeDef"]],
    },
)

CreateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "CreateCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CurrentInstanceTypeDef = TypedDict(
    "CurrentInstanceTypeDef",
    {
        "ResourceId": NotRequired[str],
        "InstanceName": NotRequired[str],
        "Tags": NotRequired[List["TagValuesTypeDef"]],
        "ResourceDetails": NotRequired["ResourceDetailsTypeDef"],
        "ResourceUtilization": NotRequired["ResourceUtilizationTypeDef"],
        "ReservationCoveredHoursInLookbackPeriod": NotRequired[str],
        "SavingsPlansCoveredHoursInLookbackPeriod": NotRequired[str],
        "OnDemandHoursInLookbackPeriod": NotRequired[str],
        "TotalRunningHoursInLookbackPeriod": NotRequired[str],
        "MonthlyCost": NotRequired[str],
        "CurrencyCode": NotRequired[str],
    },
)

DateIntervalTypeDef = TypedDict(
    "DateIntervalTypeDef",
    {
        "Start": str,
        "End": str,
    },
)

DeleteAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)

DeleteAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAnomalySubscriptionRequestRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

DeleteCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
    },
)

DeleteCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveEnd": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveOn": NotRequired[str],
    },
)

DescribeCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategory": "CostCategoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": NotRequired[DimensionType],
        "Values": NotRequired[Sequence[str]],
        "MatchOptions": NotRequired[Sequence[MatchOptionType]],
    },
)

DimensionValuesWithAttributesTypeDef = TypedDict(
    "DimensionValuesWithAttributesTypeDef",
    {
        "Value": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

DiskResourceUtilizationTypeDef = TypedDict(
    "DiskResourceUtilizationTypeDef",
    {
        "DiskReadOpsPerSecond": NotRequired[str],
        "DiskWriteOpsPerSecond": NotRequired[str],
        "DiskReadBytesPerSecond": NotRequired[str],
        "DiskWriteBytesPerSecond": NotRequired[str],
    },
)

EBSResourceUtilizationTypeDef = TypedDict(
    "EBSResourceUtilizationTypeDef",
    {
        "EbsReadOpsPerSecond": NotRequired[str],
        "EbsWriteOpsPerSecond": NotRequired[str],
        "EbsReadBytesPerSecond": NotRequired[str],
        "EbsWriteBytesPerSecond": NotRequired[str],
    },
)

EC2InstanceDetailsTypeDef = TypedDict(
    "EC2InstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Region": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Platform": NotRequired[str],
        "Tenancy": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)

EC2ResourceDetailsTypeDef = TypedDict(
    "EC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Platform": NotRequired[str],
        "Region": NotRequired[str],
        "Sku": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkPerformance": NotRequired[str],
        "Storage": NotRequired[str],
        "Vcpu": NotRequired[str],
    },
)

EC2ResourceUtilizationTypeDef = TypedDict(
    "EC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": NotRequired[str],
        "MaxMemoryUtilizationPercentage": NotRequired[str],
        "MaxStorageUtilizationPercentage": NotRequired[str],
        "EBSResourceUtilization": NotRequired["EBSResourceUtilizationTypeDef"],
        "DiskResourceUtilization": NotRequired["DiskResourceUtilizationTypeDef"],
        "NetworkResourceUtilization": NotRequired["NetworkResourceUtilizationTypeDef"],
    },
)

EC2SpecificationTypeDef = TypedDict(
    "EC2SpecificationTypeDef",
    {
        "OfferingClass": NotRequired[OfferingClassType],
    },
)

ESInstanceDetailsTypeDef = TypedDict(
    "ESInstanceDetailsTypeDef",
    {
        "InstanceClass": NotRequired[str],
        "InstanceSize": NotRequired[str],
        "Region": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)

ElastiCacheInstanceDetailsTypeDef = TypedDict(
    "ElastiCacheInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "NodeType": NotRequired[str],
        "Region": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "Or": NotRequired[Sequence[Dict[str, Any]]],
        "And": NotRequired[Sequence[Dict[str, Any]]],
        "Not": NotRequired[Dict[str, Any]],
        "Dimensions": NotRequired["DimensionValuesTypeDef"],
        "Tags": NotRequired["TagValuesTypeDef"],
        "CostCategories": NotRequired["CostCategoryValuesTypeDef"],
    },
)

ForecastResultTypeDef = TypedDict(
    "ForecastResultTypeDef",
    {
        "TimePeriod": NotRequired["DateIntervalTypeDef"],
        "MeanValue": NotRequired[str],
        "PredictionIntervalLowerBound": NotRequired[str],
        "PredictionIntervalUpperBound": NotRequired[str],
    },
)

GetAnomaliesRequestRequestTypeDef = TypedDict(
    "GetAnomaliesRequestRequestTypeDef",
    {
        "DateInterval": "AnomalyDateIntervalTypeDef",
        "MonitorArn": NotRequired[str],
        "Feedback": NotRequired[AnomalyFeedbackTypeType],
        "TotalImpact": NotRequired["TotalImpactFilterTypeDef"],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetAnomaliesResponseTypeDef = TypedDict(
    "GetAnomaliesResponseTypeDef",
    {
        "Anomalies": List["AnomalyTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnomalyMonitorsRequestRequestTypeDef = TypedDict(
    "GetAnomalyMonitorsRequestRequestTypeDef",
    {
        "MonitorArnList": NotRequired[Sequence[str]],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetAnomalyMonitorsResponseTypeDef = TypedDict(
    "GetAnomalyMonitorsResponseTypeDef",
    {
        "AnomalyMonitors": List["AnomalyMonitorTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnomalySubscriptionsRequestRequestTypeDef = TypedDict(
    "GetAnomalySubscriptionsRequestRequestTypeDef",
    {
        "SubscriptionArnList": NotRequired[Sequence[str]],
        "MonitorArn": NotRequired[str],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetAnomalySubscriptionsResponseTypeDef = TypedDict(
    "GetAnomalySubscriptionsResponseTypeDef",
    {
        "AnomalySubscriptions": List["AnomalySubscriptionTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCostAndUsageRequestRequestTypeDef = TypedDict(
    "GetCostAndUsageRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": GranularityType,
        "Metrics": Sequence[str],
        "Filter": NotRequired["ExpressionTypeDef"],
        "GroupBy": NotRequired[Sequence["GroupDefinitionTypeDef"]],
        "NextPageToken": NotRequired[str],
    },
)

GetCostAndUsageResponseTypeDef = TypedDict(
    "GetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCostAndUsageWithResourcesRequestRequestTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "Metrics": NotRequired[Sequence[str]],
        "GroupBy": NotRequired[Sequence["GroupDefinitionTypeDef"]],
        "NextPageToken": NotRequired[str],
    },
)

GetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCostCategoriesRequestRequestTypeDef = TypedDict(
    "GetCostCategoriesRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "SearchString": NotRequired[str],
        "CostCategoryName": NotRequired[str],
        "Filter": NotRequired["ExpressionTypeDef"],
        "SortBy": NotRequired[Sequence["SortDefinitionTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)

GetCostCategoriesResponseTypeDef = TypedDict(
    "GetCostCategoriesResponseTypeDef",
    {
        "NextPageToken": str,
        "CostCategoryNames": List[str],
        "CostCategoryValues": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCostForecastRequestRequestTypeDef = TypedDict(
    "GetCostForecastRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Metric": MetricType,
        "Granularity": GranularityType,
        "Filter": NotRequired["ExpressionTypeDef"],
        "PredictionIntervalLevel": NotRequired[int],
    },
)

GetCostForecastResponseTypeDef = TypedDict(
    "GetCostForecastResponseTypeDef",
    {
        "Total": "MetricValueTypeDef",
        "ForecastResultsByTime": List["ForecastResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDimensionValuesRequestRequestTypeDef = TypedDict(
    "GetDimensionValuesRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Dimension": DimensionType,
        "SearchString": NotRequired[str],
        "Context": NotRequired[ContextType],
        "Filter": NotRequired["ExpressionTypeDef"],
        "SortBy": NotRequired[Sequence["SortDefinitionTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)

GetDimensionValuesResponseTypeDef = TypedDict(
    "GetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List["DimensionValuesWithAttributesTypeDef"],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReservationCoverageRequestRequestTypeDef = TypedDict(
    "GetReservationCoverageRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "GroupBy": NotRequired[Sequence["GroupDefinitionTypeDef"]],
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired["ExpressionTypeDef"],
        "Metrics": NotRequired[Sequence[str]],
        "NextPageToken": NotRequired[str],
        "SortBy": NotRequired["SortDefinitionTypeDef"],
        "MaxResults": NotRequired[int],
    },
)

GetReservationCoverageResponseTypeDef = TypedDict(
    "GetReservationCoverageResponseTypeDef",
    {
        "CoveragesByTime": List["CoverageByTimeTypeDef"],
        "Total": "CoverageTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReservationPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationRequestRequestTypeDef",
    {
        "Service": str,
        "AccountId": NotRequired[str],
        "Filter": NotRequired["ExpressionTypeDef"],
        "AccountScope": NotRequired[AccountScopeType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "ServiceSpecification": NotRequired["ServiceSpecificationTypeDef"],
        "PageSize": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)

GetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": "ReservationPurchaseRecommendationMetadataTypeDef",
        "Recommendations": List["ReservationPurchaseRecommendationTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReservationUtilizationRequestRequestTypeDef = TypedDict(
    "GetReservationUtilizationRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "GroupBy": NotRequired[Sequence["GroupDefinitionTypeDef"]],
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired["ExpressionTypeDef"],
        "SortBy": NotRequired["SortDefinitionTypeDef"],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetReservationUtilizationResponseTypeDef = TypedDict(
    "GetReservationUtilizationResponseTypeDef",
    {
        "UtilizationsByTime": List["UtilizationByTimeTypeDef"],
        "Total": "ReservationAggregatesTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRightsizingRecommendationRequestRequestTypeDef = TypedDict(
    "GetRightsizingRecommendationRequestRequestTypeDef",
    {
        "Service": str,
        "Filter": NotRequired["ExpressionTypeDef"],
        "Configuration": NotRequired["RightsizingRecommendationConfigurationTypeDef"],
        "PageSize": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)

GetRightsizingRecommendationResponseTypeDef = TypedDict(
    "GetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": "RightsizingRecommendationMetadataTypeDef",
        "Summary": "RightsizingRecommendationSummaryTypeDef",
        "RightsizingRecommendations": List["RightsizingRecommendationTypeDef"],
        "NextPageToken": str,
        "Configuration": "RightsizingRecommendationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSavingsPlansCoverageRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansCoverageRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "GroupBy": NotRequired[Sequence["GroupDefinitionTypeDef"]],
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired["ExpressionTypeDef"],
        "Metrics": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired["SortDefinitionTypeDef"],
    },
)

GetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "GetSavingsPlansCoverageResponseTypeDef",
    {
        "SavingsPlansCoverages": List["SavingsPlansCoverageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    {
        "SavingsPlansType": SupportedSavingsPlansTypeType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "AccountScope": NotRequired[AccountScopeType],
        "NextPageToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "Filter": NotRequired["ExpressionTypeDef"],
    },
)

GetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": "SavingsPlansPurchaseRecommendationMetadataTypeDef",
        "SavingsPlansPurchaseRecommendation": "SavingsPlansPurchaseRecommendationTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSavingsPlansUtilizationDetailsRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Filter": NotRequired["ExpressionTypeDef"],
        "DataType": NotRequired[Sequence[SavingsPlansDataTypeType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired["SortDefinitionTypeDef"],
    },
)

GetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List["SavingsPlansUtilizationDetailTypeDef"],
        "Total": "SavingsPlansUtilizationAggregatesTypeDef",
        "TimePeriod": "DateIntervalTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSavingsPlansUtilizationRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansUtilizationRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired["ExpressionTypeDef"],
        "SortBy": NotRequired["SortDefinitionTypeDef"],
    },
)

GetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List["SavingsPlansUtilizationByTimeTypeDef"],
        "Total": "SavingsPlansUtilizationAggregatesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "SearchString": NotRequired[str],
        "TagKey": NotRequired[str],
        "Filter": NotRequired["ExpressionTypeDef"],
        "SortBy": NotRequired[Sequence["SortDefinitionTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)

GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "NextPageToken": str,
        "Tags": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageForecastRequestRequestTypeDef = TypedDict(
    "GetUsageForecastRequestRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Metric": MetricType,
        "Granularity": GranularityType,
        "Filter": NotRequired["ExpressionTypeDef"],
        "PredictionIntervalLevel": NotRequired[int],
    },
)

GetUsageForecastResponseTypeDef = TypedDict(
    "GetUsageForecastResponseTypeDef",
    {
        "Total": "MetricValueTypeDef",
        "ForecastResultsByTime": List["ForecastResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef",
    {
        "Type": NotRequired[GroupDefinitionTypeType],
        "Key": NotRequired[str],
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Keys": NotRequired[List[str]],
        "Metrics": NotRequired[Dict[str, "MetricValueTypeDef"]],
    },
)

ImpactTypeDef = TypedDict(
    "ImpactTypeDef",
    {
        "MaxImpact": float,
        "TotalImpact": NotRequired[float],
    },
)

InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": NotRequired["EC2InstanceDetailsTypeDef"],
        "RDSInstanceDetails": NotRequired["RDSInstanceDetailsTypeDef"],
        "RedshiftInstanceDetails": NotRequired["RedshiftInstanceDetailsTypeDef"],
        "ElastiCacheInstanceDetails": NotRequired["ElastiCacheInstanceDetailsTypeDef"],
        "ESInstanceDetails": NotRequired["ESInstanceDetailsTypeDef"],
    },
)

ListCostCategoryDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCostCategoryDefinitionsRequestRequestTypeDef",
    {
        "EffectiveOn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCostCategoryDefinitionsResponseTypeDef = TypedDict(
    "ListCostCategoryDefinitionsResponseTypeDef",
    {
        "CostCategoryReferences": List["CostCategoryReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "Amount": NotRequired[str],
        "Unit": NotRequired[str],
    },
)

ModifyRecommendationDetailTypeDef = TypedDict(
    "ModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": NotRequired[List["TargetInstanceTypeDef"]],
    },
)

NetworkResourceUtilizationTypeDef = TypedDict(
    "NetworkResourceUtilizationTypeDef",
    {
        "NetworkInBytesPerSecond": NotRequired[str],
        "NetworkOutBytesPerSecond": NotRequired[str],
        "NetworkPacketsInPerSecond": NotRequired[str],
        "NetworkPacketsOutPerSecond": NotRequired[str],
    },
)

ProvideAnomalyFeedbackRequestRequestTypeDef = TypedDict(
    "ProvideAnomalyFeedbackRequestRequestTypeDef",
    {
        "AnomalyId": str,
        "Feedback": AnomalyFeedbackTypeType,
    },
)

ProvideAnomalyFeedbackResponseTypeDef = TypedDict(
    "ProvideAnomalyFeedbackResponseTypeDef",
    {
        "AnomalyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RDSInstanceDetailsTypeDef = TypedDict(
    "RDSInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Region": NotRequired[str],
        "DatabaseEngine": NotRequired[str],
        "DatabaseEdition": NotRequired[str],
        "DeploymentOption": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)

RedshiftInstanceDetailsTypeDef = TypedDict(
    "RedshiftInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "NodeType": NotRequired[str],
        "Region": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)

ReservationAggregatesTypeDef = TypedDict(
    "ReservationAggregatesTypeDef",
    {
        "UtilizationPercentage": NotRequired[str],
        "UtilizationPercentageInUnits": NotRequired[str],
        "PurchasedHours": NotRequired[str],
        "PurchasedUnits": NotRequired[str],
        "TotalActualHours": NotRequired[str],
        "TotalActualUnits": NotRequired[str],
        "UnusedHours": NotRequired[str],
        "UnusedUnits": NotRequired[str],
        "OnDemandCostOfRIHoursUsed": NotRequired[str],
        "NetRISavings": NotRequired[str],
        "TotalPotentialRISavings": NotRequired[str],
        "AmortizedUpfrontFee": NotRequired[str],
        "AmortizedRecurringFee": NotRequired[str],
        "TotalAmortizedFee": NotRequired[str],
        "RICostForUnusedHours": NotRequired[str],
        "RealizedSavings": NotRequired[str],
        "UnrealizedSavings": NotRequired[str],
    },
)

ReservationCoverageGroupTypeDef = TypedDict(
    "ReservationCoverageGroupTypeDef",
    {
        "Attributes": NotRequired[Dict[str, str]],
        "Coverage": NotRequired["CoverageTypeDef"],
    },
)

ReservationPurchaseRecommendationDetailTypeDef = TypedDict(
    "ReservationPurchaseRecommendationDetailTypeDef",
    {
        "AccountId": NotRequired[str],
        "InstanceDetails": NotRequired["InstanceDetailsTypeDef"],
        "RecommendedNumberOfInstancesToPurchase": NotRequired[str],
        "RecommendedNormalizedUnitsToPurchase": NotRequired[str],
        "MinimumNumberOfInstancesUsedPerHour": NotRequired[str],
        "MinimumNormalizedUnitsUsedPerHour": NotRequired[str],
        "MaximumNumberOfInstancesUsedPerHour": NotRequired[str],
        "MaximumNormalizedUnitsUsedPerHour": NotRequired[str],
        "AverageNumberOfInstancesUsedPerHour": NotRequired[str],
        "AverageNormalizedUnitsUsedPerHour": NotRequired[str],
        "AverageUtilization": NotRequired[str],
        "EstimatedBreakEvenInMonths": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "EstimatedMonthlySavingsPercentage": NotRequired[str],
        "EstimatedMonthlyOnDemandCost": NotRequired[str],
        "EstimatedReservationCostForLookbackPeriod": NotRequired[str],
        "UpfrontCost": NotRequired[str],
        "RecurringStandardMonthlyCost": NotRequired[str],
    },
)

ReservationPurchaseRecommendationMetadataTypeDef = TypedDict(
    "ReservationPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
    },
)

ReservationPurchaseRecommendationSummaryTypeDef = TypedDict(
    "ReservationPurchaseRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": NotRequired[str],
        "TotalEstimatedMonthlySavingsPercentage": NotRequired[str],
        "CurrencyCode": NotRequired[str],
    },
)

ReservationPurchaseRecommendationTypeDef = TypedDict(
    "ReservationPurchaseRecommendationTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "ServiceSpecification": NotRequired["ServiceSpecificationTypeDef"],
        "RecommendationDetails": NotRequired[
            List["ReservationPurchaseRecommendationDetailTypeDef"]
        ],
        "RecommendationSummary": NotRequired["ReservationPurchaseRecommendationSummaryTypeDef"],
    },
)

ReservationUtilizationGroupTypeDef = TypedDict(
    "ReservationUtilizationGroupTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
        "Utilization": NotRequired["ReservationAggregatesTypeDef"],
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": NotRequired["EC2ResourceDetailsTypeDef"],
    },
)

ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": NotRequired["EC2ResourceUtilizationTypeDef"],
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

ResultByTimeTypeDef = TypedDict(
    "ResultByTimeTypeDef",
    {
        "TimePeriod": NotRequired["DateIntervalTypeDef"],
        "Total": NotRequired[Dict[str, "MetricValueTypeDef"]],
        "Groups": NotRequired[List["GroupTypeDef"]],
        "Estimated": NotRequired[bool],
    },
)

RightsizingRecommendationConfigurationTypeDef = TypedDict(
    "RightsizingRecommendationConfigurationTypeDef",
    {
        "RecommendationTarget": RecommendationTargetType,
        "BenefitsConsidered": bool,
    },
)

RightsizingRecommendationMetadataTypeDef = TypedDict(
    "RightsizingRecommendationMetadataTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "AdditionalMetadata": NotRequired[str],
    },
)

RightsizingRecommendationSummaryTypeDef = TypedDict(
    "RightsizingRecommendationSummaryTypeDef",
    {
        "TotalRecommendationCount": NotRequired[str],
        "EstimatedTotalMonthlySavingsAmount": NotRequired[str],
        "SavingsCurrencyCode": NotRequired[str],
        "SavingsPercentage": NotRequired[str],
    },
)

RightsizingRecommendationTypeDef = TypedDict(
    "RightsizingRecommendationTypeDef",
    {
        "AccountId": NotRequired[str],
        "CurrentInstance": NotRequired["CurrentInstanceTypeDef"],
        "RightsizingType": NotRequired[RightsizingTypeType],
        "ModifyRecommendationDetail": NotRequired["ModifyRecommendationDetailTypeDef"],
        "TerminateRecommendationDetail": NotRequired["TerminateRecommendationDetailTypeDef"],
        "FindingReasonCodes": NotRequired[List[FindingReasonCodeType]],
    },
)

RootCauseTypeDef = TypedDict(
    "RootCauseTypeDef",
    {
        "Service": NotRequired[str],
        "Region": NotRequired[str],
        "LinkedAccount": NotRequired[str],
        "UsageType": NotRequired[str],
    },
)

SavingsPlansAmortizedCommitmentTypeDef = TypedDict(
    "SavingsPlansAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": NotRequired[str],
        "AmortizedUpfrontCommitment": NotRequired[str],
        "TotalAmortizedCommitment": NotRequired[str],
    },
)

SavingsPlansCoverageDataTypeDef = TypedDict(
    "SavingsPlansCoverageDataTypeDef",
    {
        "SpendCoveredBySavingsPlans": NotRequired[str],
        "OnDemandCost": NotRequired[str],
        "TotalCost": NotRequired[str],
        "CoveragePercentage": NotRequired[str],
    },
)

SavingsPlansCoverageTypeDef = TypedDict(
    "SavingsPlansCoverageTypeDef",
    {
        "Attributes": NotRequired[Dict[str, str]],
        "Coverage": NotRequired["SavingsPlansCoverageDataTypeDef"],
        "TimePeriod": NotRequired["DateIntervalTypeDef"],
    },
)

SavingsPlansDetailsTypeDef = TypedDict(
    "SavingsPlansDetailsTypeDef",
    {
        "Region": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "OfferingId": NotRequired[str],
    },
)

SavingsPlansPurchaseRecommendationDetailTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    {
        "SavingsPlansDetails": NotRequired["SavingsPlansDetailsTypeDef"],
        "AccountId": NotRequired[str],
        "UpfrontCost": NotRequired[str],
        "EstimatedROI": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "EstimatedSPCost": NotRequired[str],
        "EstimatedOnDemandCost": NotRequired[str],
        "EstimatedOnDemandCostWithCurrentCommitment": NotRequired[str],
        "EstimatedSavingsAmount": NotRequired[str],
        "EstimatedSavingsPercentage": NotRequired[str],
        "HourlyCommitmentToPurchase": NotRequired[str],
        "EstimatedAverageUtilization": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "CurrentMinimumHourlyOnDemandSpend": NotRequired[str],
        "CurrentMaximumHourlyOnDemandSpend": NotRequired[str],
        "CurrentAverageHourlyOnDemandSpend": NotRequired[str],
    },
)

SavingsPlansPurchaseRecommendationMetadataTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
        "AdditionalMetadata": NotRequired[str],
    },
)

SavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "EstimatedTotalCost": NotRequired[str],
        "CurrentOnDemandSpend": NotRequired[str],
        "EstimatedSavingsAmount": NotRequired[str],
        "TotalRecommendationCount": NotRequired[str],
        "DailyCommitmentToPurchase": NotRequired[str],
        "HourlyCommitmentToPurchase": NotRequired[str],
        "EstimatedSavingsPercentage": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "EstimatedOnDemandCostWithCurrentCommitment": NotRequired[str],
    },
)

SavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeType],
        "SavingsPlansType": NotRequired[SupportedSavingsPlansTypeType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "SavingsPlansPurchaseRecommendationDetails": NotRequired[
            List["SavingsPlansPurchaseRecommendationDetailTypeDef"]
        ],
        "SavingsPlansPurchaseRecommendationSummary": NotRequired[
            "SavingsPlansPurchaseRecommendationSummaryTypeDef"
        ],
    },
)

SavingsPlansSavingsTypeDef = TypedDict(
    "SavingsPlansSavingsTypeDef",
    {
        "NetSavings": NotRequired[str],
        "OnDemandCostEquivalent": NotRequired[str],
    },
)

SavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "SavingsPlansUtilizationAggregatesTypeDef",
    {
        "Utilization": "SavingsPlansUtilizationTypeDef",
        "Savings": NotRequired["SavingsPlansSavingsTypeDef"],
        "AmortizedCommitment": NotRequired["SavingsPlansAmortizedCommitmentTypeDef"],
    },
)

SavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "SavingsPlansUtilizationByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Utilization": "SavingsPlansUtilizationTypeDef",
        "Savings": NotRequired["SavingsPlansSavingsTypeDef"],
        "AmortizedCommitment": NotRequired["SavingsPlansAmortizedCommitmentTypeDef"],
    },
)

SavingsPlansUtilizationDetailTypeDef = TypedDict(
    "SavingsPlansUtilizationDetailTypeDef",
    {
        "SavingsPlanArn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
        "Utilization": NotRequired["SavingsPlansUtilizationTypeDef"],
        "Savings": NotRequired["SavingsPlansSavingsTypeDef"],
        "AmortizedCommitment": NotRequired["SavingsPlansAmortizedCommitmentTypeDef"],
    },
)

SavingsPlansUtilizationTypeDef = TypedDict(
    "SavingsPlansUtilizationTypeDef",
    {
        "TotalCommitment": NotRequired[str],
        "UsedCommitment": NotRequired[str],
        "UnusedCommitment": NotRequired[str],
        "UtilizationPercentage": NotRequired[str],
    },
)

ServiceSpecificationTypeDef = TypedDict(
    "ServiceSpecificationTypeDef",
    {
        "EC2Specification": NotRequired["EC2SpecificationTypeDef"],
    },
)

SortDefinitionTypeDef = TypedDict(
    "SortDefinitionTypeDef",
    {
        "Key": str,
        "SortOrder": NotRequired[SortOrderType],
    },
)

SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "Address": NotRequired[str],
        "Type": NotRequired[SubscriberTypeType],
        "Status": NotRequired[SubscriberStatusType],
    },
)

TagValuesTypeDef = TypedDict(
    "TagValuesTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MatchOptions": NotRequired[Sequence[MatchOptionType]],
    },
)

TargetInstanceTypeDef = TypedDict(
    "TargetInstanceTypeDef",
    {
        "EstimatedMonthlyCost": NotRequired[str],
        "EstimatedMonthlySavings": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "DefaultTargetInstance": NotRequired[bool],
        "ResourceDetails": NotRequired["ResourceDetailsTypeDef"],
        "ExpectedResourceUtilization": NotRequired["ResourceUtilizationTypeDef"],
        "PlatformDifferences": NotRequired[List[PlatformDifferenceType]],
    },
)

TerminateRecommendationDetailTypeDef = TypedDict(
    "TerminateRecommendationDetailTypeDef",
    {
        "EstimatedMonthlySavings": NotRequired[str],
        "CurrencyCode": NotRequired[str],
    },
)

TotalImpactFilterTypeDef = TypedDict(
    "TotalImpactFilterTypeDef",
    {
        "NumericOperator": NumericOperatorType,
        "StartValue": float,
        "EndValue": NotRequired[float],
    },
)

UpdateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "UpdateAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
        "MonitorName": NotRequired[str],
    },
)

UpdateAnomalyMonitorResponseTypeDef = TypedDict(
    "UpdateAnomalyMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateAnomalySubscriptionRequestRequestTypeDef",
    {
        "SubscriptionArn": str,
        "Threshold": NotRequired[float],
        "Frequency": NotRequired[AnomalySubscriptionFrequencyType],
        "MonitorArnList": NotRequired[Sequence[str]],
        "Subscribers": NotRequired[Sequence["SubscriberTypeDef"]],
        "SubscriptionName": NotRequired[str],
    },
)

UpdateAnomalySubscriptionResponseTypeDef = TypedDict(
    "UpdateAnomalySubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": Sequence["CostCategoryRuleTypeDef"],
        "DefaultValue": NotRequired[str],
        "SplitChargeRules": NotRequired[Sequence["CostCategorySplitChargeRuleTypeDef"]],
    },
)

UpdateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtilizationByTimeTypeDef = TypedDict(
    "UtilizationByTimeTypeDef",
    {
        "TimePeriod": NotRequired["DateIntervalTypeDef"],
        "Groups": NotRequired[List["ReservationUtilizationGroupTypeDef"]],
        "Total": NotRequired["ReservationAggregatesTypeDef"],
    },
)
