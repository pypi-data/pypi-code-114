"""
Type annotations for config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceTypeDef

    data: AccountAggregationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AggregateConformancePackComplianceSummaryGroupKeyType,
    AggregatedSourceStatusTypeType,
    AggregatedSourceTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ConfigRuleComplianceSummaryGroupKeyType,
    ConfigRuleStateType,
    ConfigurationItemStatusType,
    ConformancePackComplianceTypeType,
    ConformancePackStateType,
    DeliveryStatusType,
    MaximumExecutionFrequencyType,
    MemberAccountRuleStatusType,
    MessageTypeType,
    OrganizationConfigRuleTriggerTypeType,
    OrganizationResourceDetailedStatusType,
    OrganizationResourceStatusType,
    OrganizationRuleStatusType,
    OwnerType,
    RecorderStatusType,
    RemediationExecutionStateType,
    RemediationExecutionStepStateType,
    ResourceCountGroupKeyType,
    ResourceTypeType,
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
    "AccountAggregationSourceTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "AggregateComplianceByConformancePackTypeDef",
    "AggregateComplianceCountTypeDef",
    "AggregateConformancePackComplianceCountTypeDef",
    "AggregateConformancePackComplianceFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryTypeDef",
    "AggregateConformancePackComplianceTypeDef",
    "AggregateEvaluationResultTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "BaseConfigurationItemTypeDef",
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "BatchGetResourceConfigRequestRequestTypeDef",
    "BatchGetResourceConfigResponseTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "ComplianceContributorCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "ConfigRuleTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConfigurationRecorderTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackDetailTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "ConformancePackInputParameterTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    "DeleteConfigRuleRequestRequestTypeDef",
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    "DeleteConformancePackRequestRequestTypeDef",
    "DeleteDeliveryChannelRequestRequestTypeDef",
    "DeleteEvaluationResultsRequestRequestTypeDef",
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    "DeleteRemediationConfigurationRequestRequestTypeDef",
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "DeleteResourceConfigRequestRequestTypeDef",
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    "DeleteStoredQueryRequestRequestTypeDef",
    "DeliverConfigSnapshotRequestRequestTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DeliveryChannelStatusTypeDef",
    "DeliveryChannelTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceRequestRequestTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DescribeConfigRulesRequestRequestTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "DescribeConformancePackComplianceRequestRequestTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusRequestRequestTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DescribeConformancePacksRequestRequestTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "DescribeRemediationExceptionsRequestRequestTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "DescribeRemediationExecutionStatusRequestRequestTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationTypeDef",
    "ExecutionControlsTypeDef",
    "ExternalEvaluationTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "FailedRemediationBatchTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    "GetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetAggregateResourceConfigRequestRequestTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "GetConformancePackComplianceDetailsRequestRequestTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetConformancePackComplianceSummaryRequestRequestTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetResourceConfigHistoryRequestRequestTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "GetStoredQueryRequestRequestTypeDef",
    "GetStoredQueryResponseTypeDef",
    "GroupedResourceCountTypeDef",
    "ListAggregateDiscoveredResourcesRequestRequestTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListStoredQueriesRequestRequestTypeDef",
    "ListStoredQueriesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "OrganizationConfigRuleTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "OrganizationConformancePackTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "PaginatorConfigTypeDef",
    "PendingAggregationRequestTypeDef",
    "PutAggregationAuthorizationRequestRequestTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConfigRuleRequestRequestTypeDef",
    "PutConfigurationAggregatorRequestRequestTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "PutConfigurationRecorderRequestRequestTypeDef",
    "PutConformancePackRequestRequestTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutDeliveryChannelRequestRequestTypeDef",
    "PutEvaluationsRequestRequestTypeDef",
    "PutEvaluationsResponseTypeDef",
    "PutExternalEvaluationRequestRequestTypeDef",
    "PutOrganizationConfigRuleRequestRequestTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackRequestRequestTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutRemediationConfigurationsRequestRequestTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
    "PutRemediationExceptionsRequestRequestTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "PutResourceConfigRequestRequestTypeDef",
    "PutRetentionConfigurationRequestRequestTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "PutStoredQueryRequestRequestTypeDef",
    "PutStoredQueryResponseTypeDef",
    "QueryInfoTypeDef",
    "RecordingGroupTypeDef",
    "RelationshipTypeDef",
    "RemediationConfigurationTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "RemediationExceptionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationExecutionStepTypeDef",
    "RemediationParameterValueTypeDef",
    "ResourceCountFiltersTypeDef",
    "ResourceCountTypeDef",
    "ResourceFiltersTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceKeyTypeDef",
    "ResourceValueTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionConfigurationTypeDef",
    "ScopeTypeDef",
    "SelectAggregateResourceConfigRequestRequestTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigRequestRequestTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "SourceDetailTypeDef",
    "SourceTypeDef",
    "SsmControlsTypeDef",
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    "StartConfigurationRecorderRequestRequestTypeDef",
    "StartRemediationExecutionRequestRequestTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "StaticValueTypeDef",
    "StatusDetailFiltersTypeDef",
    "StopConfigurationRecorderRequestRequestTypeDef",
    "StoredQueryMetadataTypeDef",
    "StoredQueryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AccountAggregationSourceTypeDef = TypedDict(
    "AccountAggregationSourceTypeDef",
    {
        "AccountIds": List[str],
        "AllAwsRegions": NotRequired[bool],
        "AwsRegions": NotRequired[List[str]],
    },
)

AggregateComplianceByConfigRuleTypeDef = TypedDict(
    "AggregateComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "Compliance": NotRequired["ComplianceTypeDef"],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

AggregateComplianceByConformancePackTypeDef = TypedDict(
    "AggregateComplianceByConformancePackTypeDef",
    {
        "ConformancePackName": NotRequired[str],
        "Compliance": NotRequired["AggregateConformancePackComplianceTypeDef"],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

AggregateComplianceCountTypeDef = TypedDict(
    "AggregateComplianceCountTypeDef",
    {
        "GroupName": NotRequired[str],
        "ComplianceSummary": NotRequired["ComplianceSummaryTypeDef"],
    },
)

AggregateConformancePackComplianceCountTypeDef = TypedDict(
    "AggregateConformancePackComplianceCountTypeDef",
    {
        "CompliantConformancePackCount": NotRequired[int],
        "NonCompliantConformancePackCount": NotRequired[int],
    },
)

AggregateConformancePackComplianceFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceFiltersTypeDef",
    {
        "ConformancePackName": NotRequired[str],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

AggregateConformancePackComplianceSummaryFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

AggregateConformancePackComplianceSummaryTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryTypeDef",
    {
        "ComplianceSummary": NotRequired["AggregateConformancePackComplianceCountTypeDef"],
        "GroupName": NotRequired[str],
    },
)

AggregateConformancePackComplianceTypeDef = TypedDict(
    "AggregateConformancePackComplianceTypeDef",
    {
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "CompliantRuleCount": NotRequired[int],
        "NonCompliantRuleCount": NotRequired[int],
        "TotalRuleCount": NotRequired[int],
    },
)

AggregateEvaluationResultTypeDef = TypedDict(
    "AggregateEvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": NotRequired["EvaluationResultIdentifierTypeDef"],
        "ComplianceType": NotRequired[ComplianceTypeType],
        "ResultRecordedTime": NotRequired[datetime],
        "ConfigRuleInvokedTime": NotRequired[datetime],
        "Annotation": NotRequired[str],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

AggregateResourceIdentifierTypeDef = TypedDict(
    "AggregateResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "ResourceName": NotRequired[str],
    },
)

AggregatedSourceStatusTypeDef = TypedDict(
    "AggregatedSourceStatusTypeDef",
    {
        "SourceId": NotRequired[str],
        "SourceType": NotRequired[AggregatedSourceTypeType],
        "AwsRegion": NotRequired[str],
        "LastUpdateStatus": NotRequired[AggregatedSourceStatusTypeType],
        "LastUpdateTime": NotRequired[datetime],
        "LastErrorCode": NotRequired[str],
        "LastErrorMessage": NotRequired[str],
    },
)

AggregationAuthorizationTypeDef = TypedDict(
    "AggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": NotRequired[str],
        "AuthorizedAccountId": NotRequired[str],
        "AuthorizedAwsRegion": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)

BaseConfigurationItemTypeDef = TypedDict(
    "BaseConfigurationItemTypeDef",
    {
        "version": NotRequired[str],
        "accountId": NotRequired[str],
        "configurationItemCaptureTime": NotRequired[datetime],
        "configurationItemStatus": NotRequired[ConfigurationItemStatusType],
        "configurationStateId": NotRequired[str],
        "arn": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "awsRegion": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "resourceCreationTime": NotRequired[datetime],
        "configuration": NotRequired[str],
        "supplementaryConfiguration": NotRequired[Dict[str, str]],
    },
)

BatchGetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifiers": Sequence["AggregateResourceIdentifierTypeDef"],
    },
)

BatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "UnprocessedResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetResourceConfigRequestRequestTypeDef",
    {
        "resourceKeys": Sequence["ResourceKeyTypeDef"],
    },
)

BatchGetResourceConfigResponseTypeDef = TypedDict(
    "BatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "unprocessedResourceKeys": List["ResourceKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComplianceByConfigRuleTypeDef = TypedDict(
    "ComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "Compliance": NotRequired["ComplianceTypeDef"],
    },
)

ComplianceByResourceTypeDef = TypedDict(
    "ComplianceByResourceTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Compliance": NotRequired["ComplianceTypeDef"],
    },
)

ComplianceContributorCountTypeDef = TypedDict(
    "ComplianceContributorCountTypeDef",
    {
        "CappedCount": NotRequired[int],
        "CapExceeded": NotRequired[bool],
    },
)

ComplianceSummaryByResourceTypeTypeDef = TypedDict(
    "ComplianceSummaryByResourceTypeTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ComplianceSummary": NotRequired["ComplianceSummaryTypeDef"],
    },
)

ComplianceSummaryTypeDef = TypedDict(
    "ComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": NotRequired["ComplianceContributorCountTypeDef"],
        "NonCompliantResourceCount": NotRequired["ComplianceContributorCountTypeDef"],
        "ComplianceSummaryTimestamp": NotRequired[datetime],
    },
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "ComplianceType": NotRequired[ComplianceTypeType],
        "ComplianceContributorCount": NotRequired["ComplianceContributorCountTypeDef"],
    },
)

ConfigExportDeliveryInfoTypeDef = TypedDict(
    "ConfigExportDeliveryInfoTypeDef",
    {
        "lastStatus": NotRequired[DeliveryStatusType],
        "lastErrorCode": NotRequired[str],
        "lastErrorMessage": NotRequired[str],
        "lastAttemptTime": NotRequired[datetime],
        "lastSuccessfulTime": NotRequired[datetime],
        "nextDeliveryTime": NotRequired[datetime],
    },
)

ConfigRuleComplianceFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceFiltersTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ComplianceType": NotRequired[ComplianceTypeType],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

ConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)

ConfigRuleEvaluationStatusTypeDef = TypedDict(
    "ConfigRuleEvaluationStatusTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ConfigRuleArn": NotRequired[str],
        "ConfigRuleId": NotRequired[str],
        "LastSuccessfulInvocationTime": NotRequired[datetime],
        "LastFailedInvocationTime": NotRequired[datetime],
        "LastSuccessfulEvaluationTime": NotRequired[datetime],
        "LastFailedEvaluationTime": NotRequired[datetime],
        "FirstActivatedTime": NotRequired[datetime],
        "LastDeactivatedTime": NotRequired[datetime],
        "LastErrorCode": NotRequired[str],
        "LastErrorMessage": NotRequired[str],
        "FirstEvaluationStarted": NotRequired[bool],
    },
)

ConfigRuleTypeDef = TypedDict(
    "ConfigRuleTypeDef",
    {
        "Source": "SourceTypeDef",
        "ConfigRuleName": NotRequired[str],
        "ConfigRuleArn": NotRequired[str],
        "ConfigRuleId": NotRequired[str],
        "Description": NotRequired[str],
        "Scope": NotRequired["ScopeTypeDef"],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ConfigRuleState": NotRequired[ConfigRuleStateType],
        "CreatedBy": NotRequired[str],
    },
)

ConfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": NotRequired[MaximumExecutionFrequencyType],
    },
)

ConfigStreamDeliveryInfoTypeDef = TypedDict(
    "ConfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": NotRequired[DeliveryStatusType],
        "lastErrorCode": NotRequired[str],
        "lastErrorMessage": NotRequired[str],
        "lastStatusChangeTime": NotRequired[datetime],
    },
)

ConfigurationAggregatorTypeDef = TypedDict(
    "ConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": NotRequired[str],
        "ConfigurationAggregatorArn": NotRequired[str],
        "AccountAggregationSources": NotRequired[List["AccountAggregationSourceTypeDef"]],
        "OrganizationAggregationSource": NotRequired["OrganizationAggregationSourceTypeDef"],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)

ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "version": NotRequired[str],
        "accountId": NotRequired[str],
        "configurationItemCaptureTime": NotRequired[datetime],
        "configurationItemStatus": NotRequired[ConfigurationItemStatusType],
        "configurationStateId": NotRequired[str],
        "configurationItemMD5Hash": NotRequired[str],
        "arn": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "awsRegion": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "resourceCreationTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "relatedEvents": NotRequired[List[str]],
        "relationships": NotRequired[List["RelationshipTypeDef"]],
        "configuration": NotRequired[str],
        "supplementaryConfiguration": NotRequired[Dict[str, str]],
    },
)

ConfigurationRecorderStatusTypeDef = TypedDict(
    "ConfigurationRecorderStatusTypeDef",
    {
        "name": NotRequired[str],
        "lastStartTime": NotRequired[datetime],
        "lastStopTime": NotRequired[datetime],
        "recording": NotRequired[bool],
        "lastStatus": NotRequired[RecorderStatusType],
        "lastErrorCode": NotRequired[str],
        "lastErrorMessage": NotRequired[str],
        "lastStatusChangeTime": NotRequired[datetime],
    },
)

ConfigurationRecorderTypeDef = TypedDict(
    "ConfigurationRecorderTypeDef",
    {
        "name": NotRequired[str],
        "roleARN": NotRequired[str],
        "recordingGroup": NotRequired["RecordingGroupTypeDef"],
    },
)

ConformancePackComplianceFiltersTypeDef = TypedDict(
    "ConformancePackComplianceFiltersTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
    },
)

ConformancePackComplianceSummaryTypeDef = TypedDict(
    "ConformancePackComplianceSummaryTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": ConformancePackComplianceTypeType,
    },
)

ConformancePackDetailTypeDef = TypedDict(
    "ConformancePackDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[List["ConformancePackInputParameterTypeDef"]],
        "LastUpdateRequestedTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)

ConformancePackEvaluationFiltersTypeDef = TypedDict(
    "ConformancePackEvaluationFiltersTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "ResourceType": NotRequired[str],
        "ResourceIds": NotRequired[Sequence[str]],
    },
)

ConformancePackEvaluationResultTypeDef = TypedDict(
    "ConformancePackEvaluationResultTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
        "Annotation": NotRequired[str],
    },
)

ConformancePackInputParameterTypeDef = TypedDict(
    "ConformancePackInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
)

ConformancePackRuleComplianceTypeDef = TypedDict(
    "ConformancePackRuleComplianceTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "Controls": NotRequired[List[str]],
    },
)

ConformancePackStatusDetailTypeDef = TypedDict(
    "ConformancePackStatusDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": ConformancePackStateType,
        "StackArn": str,
        "LastUpdateRequestedTime": datetime,
        "ConformancePackStatusReason": NotRequired[str],
        "LastUpdateCompletedTime": NotRequired[datetime],
    },
)

DeleteAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)

DeleteConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)

DeleteConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

DeleteConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)

DeleteDeliveryChannelRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannelName": str,
    },
)

DeleteEvaluationResultsRequestRequestTypeDef = TypedDict(
    "DeleteEvaluationResultsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)

DeleteOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)

DeletePendingAggregationRequestRequestRequestTypeDef = TypedDict(
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
)

DeleteRemediationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRemediationConfigurationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": NotRequired[str],
    },
)

DeleteRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence["RemediationExceptionResourceKeyTypeDef"],
    },
)

DeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "DeleteRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List["FailedDeleteRemediationExceptionsBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceConfigRequestRequestTypeDef = TypedDict(
    "DeleteResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)

DeleteRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionConfigurationName": str,
    },
)

DeleteStoredQueryRequestRequestTypeDef = TypedDict(
    "DeleteStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)

DeliverConfigSnapshotRequestRequestTypeDef = TypedDict(
    "DeliverConfigSnapshotRequestRequestTypeDef",
    {
        "deliveryChannelName": str,
    },
)

DeliverConfigSnapshotResponseTypeDef = TypedDict(
    "DeliverConfigSnapshotResponseTypeDef",
    {
        "configSnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeliveryChannelStatusTypeDef = TypedDict(
    "DeliveryChannelStatusTypeDef",
    {
        "name": NotRequired[str],
        "configSnapshotDeliveryInfo": NotRequired["ConfigExportDeliveryInfoTypeDef"],
        "configHistoryDeliveryInfo": NotRequired["ConfigExportDeliveryInfoTypeDef"],
        "configStreamDeliveryInfo": NotRequired["ConfigStreamDeliveryInfoTypeDef"],
    },
)

DeliveryChannelTypeDef = TypedDict(
    "DeliveryChannelTypeDef",
    {
        "name": NotRequired[str],
        "s3BucketName": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
        "s3KmsKeyArn": NotRequired[str],
        "snsTopicARN": NotRequired[str],
        "configSnapshotDeliveryProperties": NotRequired["ConfigSnapshotDeliveryPropertiesTypeDef"],
    },
)

DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired["ConfigRuleComplianceFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List["AggregateComplianceByConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired["AggregateConformancePackComplianceFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAggregateComplianceByConformancePacksResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    {
        "AggregateComplianceByConformancePacks": List[
            "AggregateComplianceByConformancePackTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregationAuthorizationsRequestRequestTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List["AggregationAuthorizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComplianceByConfigRuleRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "NextToken": NotRequired[str],
    },
)

DescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List["ComplianceByConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComplianceByResourceRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestRequestTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeComplianceByResourceResponseTypeDef = TypedDict(
    "DescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List["ComplianceByResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigRuleEvaluationStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List["ConfigRuleEvaluationStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeConfigRulesRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeConfigRulesResponseTypeDef = TypedDict(
    "DescribeConfigRulesResponseTypeDef",
    {
        "ConfigRules": List["ConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "UpdateStatus": NotRequired[Sequence[AggregatedSourceStatusTypeType]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List["AggregatedSourceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationAggregatorsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List["ConfigurationAggregatorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRecorderStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": NotRequired[Sequence[str]],
    },
)

DescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List["ConfigurationRecorderStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRecordersRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": NotRequired[Sequence[str]],
    },
)

DescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "DescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List["ConfigurationRecorderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePackComplianceRequestRequestTypeDef = TypedDict(
    "DescribeConformancePackComplianceRequestRequestTypeDef",
    {
        "ConformancePackName": str,
        "Filters": NotRequired["ConformancePackComplianceFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "DescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List["ConformancePackRuleComplianceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePackStatusRequestRequestTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestRequestTypeDef",
    {
        "ConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeConformancePackStatusResponseTypeDef = TypedDict(
    "DescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List["ConformancePackStatusDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeConformancePacksRequestRequestTypeDef",
    {
        "ConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeConformancePacksResponseTypeDef = TypedDict(
    "DescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List["ConformancePackDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryChannelStatusRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    {
        "DeliveryChannelNames": NotRequired[Sequence[str]],
    },
)

DescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List["DeliveryChannelStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryChannelsRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    {
        "DeliveryChannelNames": NotRequired[Sequence[str]],
    },
)

DescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelsResponseTypeDef",
    {
        "DeliveryChannels": List["DeliveryChannelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List["OrganizationConfigRuleStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List["OrganizationConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConformancePackStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List["OrganizationConformancePackStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List["OrganizationConformancePackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingAggregationRequestsRequestRequestTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List["PendingAggregationRequestTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
    },
)

DescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "DescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List["RemediationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "DescribeRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": NotRequired[Sequence["RemediationExceptionResourceKeyTypeDef"]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "DescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List["RemediationExceptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRemediationExecutionStatusRequestRequestTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": NotRequired[Sequence["ResourceKeyTypeDef"]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List["RemediationExecutionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRetentionConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    {
        "RetentionConfigurationNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List["RetentionConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationResultIdentifierTypeDef = TypedDict(
    "EvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": NotRequired["EvaluationResultQualifierTypeDef"],
        "OrderingTimestamp": NotRequired[datetime],
    },
)

EvaluationResultQualifierTypeDef = TypedDict(
    "EvaluationResultQualifierTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": NotRequired["EvaluationResultIdentifierTypeDef"],
        "ComplianceType": NotRequired[ComplianceTypeType],
        "ResultRecordedTime": NotRequired[datetime],
        "ConfigRuleInvokedTime": NotRequired[datetime],
        "Annotation": NotRequired[str],
        "ResultToken": NotRequired[str],
    },
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
        "Annotation": NotRequired[str],
    },
)

ExecutionControlsTypeDef = TypedDict(
    "ExecutionControlsTypeDef",
    {
        "SsmControls": NotRequired["SsmControlsTypeDef"],
    },
)

ExternalEvaluationTypeDef = TypedDict(
    "ExternalEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
        "Annotation": NotRequired[str],
    },
)

FailedDeleteRemediationExceptionsBatchTypeDef = TypedDict(
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    {
        "FailureMessage": NotRequired[str],
        "FailedItems": NotRequired[List["RemediationExceptionResourceKeyTypeDef"]],
    },
)

FailedRemediationBatchTypeDef = TypedDict(
    "FailedRemediationBatchTypeDef",
    {
        "FailureMessage": NotRequired[str],
        "FailedItems": NotRequired[List["RemediationConfigurationTypeDef"]],
    },
)

FailedRemediationExceptionBatchTypeDef = TypedDict(
    "FailedRemediationExceptionBatchTypeDef",
    {
        "FailureMessage": NotRequired[str],
        "FailedItems": NotRequired[List["RemediationExceptionTypeDef"]],
    },
)

FieldInfoTypeDef = TypedDict(
    "FieldInfoTypeDef",
    {
        "Name": NotRequired[str],
    },
)

GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
        "ComplianceType": NotRequired[ComplianceTypeType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List["AggregateEvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired["ConfigRuleComplianceSummaryFiltersTypeDef"],
        "GroupByKey": NotRequired[ConfigRuleComplianceSummaryGroupKeyType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List["AggregateComplianceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired["AggregateConformancePackComplianceSummaryFiltersTypeDef"],
        "GroupByKey": NotRequired[AggregateConformancePackComplianceSummaryGroupKeyType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetAggregateConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    {
        "AggregateConformancePackComplianceSummaries": List[
            "AggregateConformancePackComplianceSummaryTypeDef"
        ],
        "GroupByKey": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAggregateDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired["ResourceCountFiltersTypeDef"],
        "GroupByKey": NotRequired[ResourceCountGroupKeyType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List["GroupedResourceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "GetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifier": "AggregateResourceIdentifierTypeDef",
    },
)

GetAggregateResourceConfigResponseTypeDef = TypedDict(
    "GetAggregateResourceConfigResponseTypeDef",
    {
        "ConfigurationItem": "ConfigurationItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceDetailsByResourceRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "NextToken": NotRequired[str],
    },
)

GetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    {
        "ComplianceSummary": "ComplianceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceSummaryByResourceTypeRequestRequestTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    {
        "ResourceTypes": NotRequired[Sequence[str]],
    },
)

GetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List["ComplianceSummaryByResourceTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConformancePackComplianceDetailsRequestRequestTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsRequestRequestTypeDef",
    {
        "ConformancePackName": str,
        "Filters": NotRequired["ConformancePackEvaluationFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List["ConformancePackEvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List["ConformancePackComplianceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "resourceTypes": NotRequired[Sequence[str]],
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List["ResourceCountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "Filters": NotRequired["StatusDetailFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List["MemberAccountStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Filters": NotRequired["OrganizationResourceDetailedStatusFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            "OrganizationConformancePackDetailedStatusTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceConfigHistoryRequestRequestTypeDef = TypedDict(
    "GetResourceConfigHistoryRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "laterTime": NotRequired[Union[datetime, str]],
        "earlierTime": NotRequired[Union[datetime, str]],
        "chronologicalOrder": NotRequired[ChronologicalOrderType],
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetResourceConfigHistoryResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List["ConfigurationItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStoredQueryRequestRequestTypeDef = TypedDict(
    "GetStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)

GetStoredQueryResponseTypeDef = TypedDict(
    "GetStoredQueryResponseTypeDef",
    {
        "StoredQuery": "StoredQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupedResourceCountTypeDef = TypedDict(
    "GroupedResourceCountTypeDef",
    {
        "GroupName": str,
        "ResourceCount": int,
    },
)

ListAggregateDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
        "Filters": NotRequired["ResourceFiltersTypeDef"],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIds": NotRequired[Sequence[str]],
        "resourceName": NotRequired[str],
        "limit": NotRequired[int],
        "includeDeletedResources": NotRequired[bool],
        "nextToken": NotRequired[str],
    },
)

ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStoredQueriesRequestRequestTypeDef = TypedDict(
    "ListStoredQueriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListStoredQueriesResponseTypeDef = TypedDict(
    "ListStoredQueriesResponseTypeDef",
    {
        "StoredQueryMetadata": List["StoredQueryMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberAccountStatusTypeDef = TypedDict(
    "MemberAccountStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)

OrganizationAggregationSourceTypeDef = TypedDict(
    "OrganizationAggregationSourceTypeDef",
    {
        "RoleArn": str,
        "AwsRegions": NotRequired[List[str]],
        "AllAwsRegions": NotRequired[bool],
    },
)

OrganizationConfigRuleStatusTypeDef = TypedDict(
    "OrganizationConfigRuleStatusTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": OrganizationRuleStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)

OrganizationConfigRuleTypeDef = TypedDict(
    "OrganizationConfigRuleTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
        "OrganizationManagedRuleMetadata": NotRequired["OrganizationManagedRuleMetadataTypeDef"],
        "OrganizationCustomRuleMetadata": NotRequired["OrganizationCustomRuleMetadataTypeDef"],
        "ExcludedAccounts": NotRequired[List[str]],
        "LastUpdateTime": NotRequired[datetime],
    },
)

OrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "OrganizationConformancePackDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": OrganizationResourceDetailedStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)

OrganizationConformancePackStatusTypeDef = TypedDict(
    "OrganizationConformancePackStatusTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": OrganizationResourceStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)

OrganizationConformancePackTypeDef = TypedDict(
    "OrganizationConformancePackTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "LastUpdateTime": datetime,
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[List["ConformancePackInputParameterTypeDef"]],
        "ExcludedAccounts": NotRequired[List[str]],
    },
)

OrganizationCustomRuleMetadataTypeDef = TypedDict(
    "OrganizationCustomRuleMetadataTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[OrganizationConfigRuleTriggerTypeType],
        "Description": NotRequired[str],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[List[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
    },
)

OrganizationManagedRuleMetadataTypeDef = TypedDict(
    "OrganizationManagedRuleMetadataTypeDef",
    {
        "RuleIdentifier": str,
        "Description": NotRequired[str],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[List[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
    },
)

OrganizationResourceDetailedStatusFiltersTypeDef = TypedDict(
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "Status": NotRequired[OrganizationResourceDetailedStatusType],
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

PendingAggregationRequestTypeDef = TypedDict(
    "PendingAggregationRequestTypeDef",
    {
        "RequesterAccountId": NotRequired[str],
        "RequesterAwsRegion": NotRequired[str],
    },
)

PutAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "PutAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutAggregationAuthorizationResponseTypeDef = TypedDict(
    "PutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": "AggregationAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutConfigRuleRequestRequestTypeDef = TypedDict(
    "PutConfigRuleRequestRequestTypeDef",
    {
        "ConfigRule": "ConfigRuleTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "PutConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "AccountAggregationSources": NotRequired[Sequence["AccountAggregationSourceTypeDef"]],
        "OrganizationAggregationSource": NotRequired["OrganizationAggregationSourceTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutConfigurationAggregatorResponseTypeDef = TypedDict(
    "PutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": "ConfigurationAggregatorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "PutConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorder": "ConfigurationRecorderTypeDef",
    },
)

PutConformancePackRequestRequestTypeDef = TypedDict(
    "PutConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
        "TemplateS3Uri": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[
            Sequence["ConformancePackInputParameterTypeDef"]
        ],
    },
)

PutConformancePackResponseTypeDef = TypedDict(
    "PutConformancePackResponseTypeDef",
    {
        "ConformancePackArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDeliveryChannelRequestRequestTypeDef = TypedDict(
    "PutDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannel": "DeliveryChannelTypeDef",
    },
)

PutEvaluationsRequestRequestTypeDef = TypedDict(
    "PutEvaluationsRequestRequestTypeDef",
    {
        "ResultToken": str,
        "Evaluations": NotRequired[Sequence["EvaluationTypeDef"]],
        "TestMode": NotRequired[bool],
    },
)

PutEvaluationsResponseTypeDef = TypedDict(
    "PutEvaluationsResponseTypeDef",
    {
        "FailedEvaluations": List["EvaluationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutExternalEvaluationRequestRequestTypeDef = TypedDict(
    "PutExternalEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ExternalEvaluation": "ExternalEvaluationTypeDef",
    },
)

PutOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "PutOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationManagedRuleMetadata": NotRequired["OrganizationManagedRuleMetadataTypeDef"],
        "OrganizationCustomRuleMetadata": NotRequired["OrganizationCustomRuleMetadataTypeDef"],
        "ExcludedAccounts": NotRequired[Sequence[str]],
    },
)

PutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "PutOrganizationConfigRuleResponseTypeDef",
    {
        "OrganizationConfigRuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "PutOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
        "TemplateS3Uri": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[
            Sequence["ConformancePackInputParameterTypeDef"]
        ],
        "ExcludedAccounts": NotRequired[Sequence[str]],
    },
)

PutOrganizationConformancePackResponseTypeDef = TypedDict(
    "PutOrganizationConformancePackResponseTypeDef",
    {
        "OrganizationConformancePackArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "PutRemediationConfigurationsRequestRequestTypeDef",
    {
        "RemediationConfigurations": Sequence["RemediationConfigurationTypeDef"],
    },
)

PutRemediationConfigurationsResponseTypeDef = TypedDict(
    "PutRemediationConfigurationsResponseTypeDef",
    {
        "FailedBatches": List["FailedRemediationBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "PutRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence["RemediationExceptionResourceKeyTypeDef"],
        "Message": NotRequired[str],
        "ExpirationTime": NotRequired[Union[datetime, str]],
    },
)

PutRemediationExceptionsResponseTypeDef = TypedDict(
    "PutRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List["FailedRemediationExceptionBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourceConfigRequestRequestTypeDef = TypedDict(
    "PutResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "SchemaVersionId": str,
        "ResourceId": str,
        "Configuration": str,
        "ResourceName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

PutRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "PutRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionPeriodInDays": int,
    },
)

PutRetentionConfigurationResponseTypeDef = TypedDict(
    "PutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": "RetentionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutStoredQueryRequestRequestTypeDef = TypedDict(
    "PutStoredQueryRequestRequestTypeDef",
    {
        "StoredQuery": "StoredQueryTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutStoredQueryResponseTypeDef = TypedDict(
    "PutStoredQueryResponseTypeDef",
    {
        "QueryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "SelectFields": NotRequired[List["FieldInfoTypeDef"]],
    },
)

RecordingGroupTypeDef = TypedDict(
    "RecordingGroupTypeDef",
    {
        "allSupported": NotRequired[bool],
        "includeGlobalResourceTypes": NotRequired[bool],
        "resourceTypes": NotRequired[List[ResourceTypeType]],
    },
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "relationshipName": NotRequired[str],
    },
)

RemediationConfigurationTypeDef = TypedDict(
    "RemediationConfigurationTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
        "TargetVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, "RemediationParameterValueTypeDef"]],
        "ResourceType": NotRequired[str],
        "Automatic": NotRequired[bool],
        "ExecutionControls": NotRequired["ExecutionControlsTypeDef"],
        "MaximumAutomaticAttempts": NotRequired[int],
        "RetryAttemptSeconds": NotRequired[int],
        "Arn": NotRequired[str],
        "CreatedByService": NotRequired[str],
    },
)

RemediationExceptionResourceKeyTypeDef = TypedDict(
    "RemediationExceptionResourceKeyTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)

RemediationExceptionTypeDef = TypedDict(
    "RemediationExceptionTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": NotRequired[str],
        "ExpirationTime": NotRequired[datetime],
    },
)

RemediationExecutionStatusTypeDef = TypedDict(
    "RemediationExecutionStatusTypeDef",
    {
        "ResourceKey": NotRequired["ResourceKeyTypeDef"],
        "State": NotRequired[RemediationExecutionStateType],
        "StepDetails": NotRequired[List["RemediationExecutionStepTypeDef"]],
        "InvocationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

RemediationExecutionStepTypeDef = TypedDict(
    "RemediationExecutionStepTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[RemediationExecutionStepStateType],
        "ErrorMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "StopTime": NotRequired[datetime],
    },
)

RemediationParameterValueTypeDef = TypedDict(
    "RemediationParameterValueTypeDef",
    {
        "ResourceValue": NotRequired["ResourceValueTypeDef"],
        "StaticValue": NotRequired["StaticValueTypeDef"],
    },
)

ResourceCountFiltersTypeDef = TypedDict(
    "ResourceCountFiltersTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "AccountId": NotRequired[str],
        "Region": NotRequired[str],
    },
)

ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "resourceType": NotRequired[ResourceTypeType],
        "count": NotRequired[int],
    },
)

ResourceFiltersTypeDef = TypedDict(
    "ResourceFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceName": NotRequired[str],
        "Region": NotRequired[str],
    },
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "resourceDeletionTime": NotRequired[datetime],
    },
)

ResourceKeyTypeDef = TypedDict(
    "ResourceKeyTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)

ResourceValueTypeDef = TypedDict(
    "ResourceValueTypeDef",
    {
        "Value": Literal["RESOURCE_ID"],
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

RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef",
    {
        "Name": str,
        "RetentionPeriodInDays": int,
    },
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "ComplianceResourceTypes": NotRequired[List[str]],
        "TagKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "ComplianceResourceId": NotRequired[str],
    },
)

SelectAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "SelectAggregateResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
        "ConfigurationAggregatorName": str,
        "Limit": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SelectAggregateResourceConfigResponseTypeDef = TypedDict(
    "SelectAggregateResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": "QueryInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SelectResourceConfigRequestRequestTypeDef = TypedDict(
    "SelectResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SelectResourceConfigResponseTypeDef = TypedDict(
    "SelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": "QueryInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceDetailTypeDef = TypedDict(
    "SourceDetailTypeDef",
    {
        "EventSource": NotRequired[Literal["aws.config"]],
        "MessageType": NotRequired[MessageTypeType],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Owner": OwnerType,
        "SourceIdentifier": str,
        "SourceDetails": NotRequired[List["SourceDetailTypeDef"]],
    },
)

SsmControlsTypeDef = TypedDict(
    "SsmControlsTypeDef",
    {
        "ConcurrentExecutionRatePercentage": NotRequired[int],
        "ErrorPercentage": NotRequired[int],
    },
)

StartConfigRulesEvaluationRequestRequestTypeDef = TypedDict(
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
    },
)

StartConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StartConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

StartRemediationExecutionRequestRequestTypeDef = TypedDict(
    "StartRemediationExecutionRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence["ResourceKeyTypeDef"],
    },
)

StartRemediationExecutionResponseTypeDef = TypedDict(
    "StartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["ResourceKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StaticValueTypeDef = TypedDict(
    "StaticValueTypeDef",
    {
        "Values": List[str],
    },
)

StatusDetailFiltersTypeDef = TypedDict(
    "StatusDetailFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "MemberAccountRuleStatus": NotRequired[MemberAccountRuleStatusType],
    },
)

StopConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StopConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

StoredQueryMetadataTypeDef = TypedDict(
    "StoredQueryMetadataTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "QueryName": str,
        "Description": NotRequired[str],
    },
)

StoredQueryTypeDef = TypedDict(
    "StoredQueryTypeDef",
    {
        "QueryName": str,
        "QueryId": NotRequired[str],
        "QueryArn": NotRequired[str],
        "Description": NotRequired[str],
        "Expression": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
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
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
