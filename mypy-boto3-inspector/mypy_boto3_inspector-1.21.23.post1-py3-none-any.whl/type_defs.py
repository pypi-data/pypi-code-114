"""
Type annotations for inspector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AddAttributesToFindingsRequestRequestTypeDef

    data: AddAttributesToFindingsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AgentHealthCodeType,
    AgentHealthType,
    AssessmentRunNotificationSnsStatusCodeType,
    AssessmentRunStateType,
    FailedItemErrorCodeType,
    InspectorEventType,
    PreviewStatusType,
    ReportFileFormatType,
    ReportStatusType,
    ReportTypeType,
    ScopeTypeType,
    SeverityType,
    StopActionType,
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
    "AddAttributesToFindingsRequestRequestTypeDef",
    "AddAttributesToFindingsResponseTypeDef",
    "AgentFilterTypeDef",
    "AgentPreviewTypeDef",
    "AssessmentRunAgentTypeDef",
    "AssessmentRunFilterTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentRunTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "AssessmentTemplateTypeDef",
    "AssetAttributesTypeDef",
    "AttributeTypeDef",
    "CreateAssessmentTargetRequestRequestTypeDef",
    "CreateAssessmentTargetResponseTypeDef",
    "CreateAssessmentTemplateRequestRequestTypeDef",
    "CreateAssessmentTemplateResponseTypeDef",
    "CreateExclusionsPreviewRequestRequestTypeDef",
    "CreateExclusionsPreviewResponseTypeDef",
    "CreateResourceGroupRequestRequestTypeDef",
    "CreateResourceGroupResponseTypeDef",
    "DeleteAssessmentRunRequestRequestTypeDef",
    "DeleteAssessmentTargetRequestRequestTypeDef",
    "DeleteAssessmentTemplateRequestRequestTypeDef",
    "DescribeAssessmentRunsRequestRequestTypeDef",
    "DescribeAssessmentRunsResponseTypeDef",
    "DescribeAssessmentTargetsRequestRequestTypeDef",
    "DescribeAssessmentTargetsResponseTypeDef",
    "DescribeAssessmentTemplatesRequestRequestTypeDef",
    "DescribeAssessmentTemplatesResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    "DescribeExclusionsRequestRequestTypeDef",
    "DescribeExclusionsResponseTypeDef",
    "DescribeFindingsRequestRequestTypeDef",
    "DescribeFindingsResponseTypeDef",
    "DescribeResourceGroupsRequestRequestTypeDef",
    "DescribeResourceGroupsResponseTypeDef",
    "DescribeRulesPackagesRequestRequestTypeDef",
    "DescribeRulesPackagesResponseTypeDef",
    "DurationRangeTypeDef",
    "EventSubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "FailedItemDetailsTypeDef",
    "FindingFilterTypeDef",
    "FindingTypeDef",
    "GetAssessmentReportRequestRequestTypeDef",
    "GetAssessmentReportResponseTypeDef",
    "GetExclusionsPreviewRequestRequestTypeDef",
    "GetExclusionsPreviewResponseTypeDef",
    "GetTelemetryMetadataRequestRequestTypeDef",
    "GetTelemetryMetadataResponseTypeDef",
    "InspectorServiceAttributesTypeDef",
    "ListAssessmentRunAgentsRequestRequestTypeDef",
    "ListAssessmentRunAgentsResponseTypeDef",
    "ListAssessmentRunsRequestRequestTypeDef",
    "ListAssessmentRunsResponseTypeDef",
    "ListAssessmentTargetsRequestRequestTypeDef",
    "ListAssessmentTargetsResponseTypeDef",
    "ListAssessmentTemplatesRequestRequestTypeDef",
    "ListAssessmentTemplatesResponseTypeDef",
    "ListEventSubscriptionsRequestRequestTypeDef",
    "ListEventSubscriptionsResponseTypeDef",
    "ListExclusionsRequestRequestTypeDef",
    "ListExclusionsResponseTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "ListFindingsResponseTypeDef",
    "ListRulesPackagesRequestRequestTypeDef",
    "ListRulesPackagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewAgentsRequestRequestTypeDef",
    "PreviewAgentsResponseTypeDef",
    "PrivateIpTypeDef",
    "RegisterCrossAccountAccessRoleRequestRequestTypeDef",
    "RemoveAttributesFromFindingsRequestRequestTypeDef",
    "RemoveAttributesFromFindingsResponseTypeDef",
    "ResourceGroupTagTypeDef",
    "ResourceGroupTypeDef",
    "ResponseMetadataTypeDef",
    "RulesPackageTypeDef",
    "ScopeTypeDef",
    "SecurityGroupTypeDef",
    "SetTagsForResourceRequestRequestTypeDef",
    "StartAssessmentRunRequestRequestTypeDef",
    "StartAssessmentRunResponseTypeDef",
    "StopAssessmentRunRequestRequestTypeDef",
    "SubscribeToEventRequestRequestTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TelemetryMetadataTypeDef",
    "TimestampRangeTypeDef",
    "UnsubscribeFromEventRequestRequestTypeDef",
    "UpdateAssessmentTargetRequestRequestTypeDef",
)

AddAttributesToFindingsRequestRequestTypeDef = TypedDict(
    "AddAttributesToFindingsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
        "attributes": Sequence["AttributeTypeDef"],
    },
)

AddAttributesToFindingsResponseTypeDef = TypedDict(
    "AddAttributesToFindingsResponseTypeDef",
    {
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentFilterTypeDef = TypedDict(
    "AgentFilterTypeDef",
    {
        "agentHealths": Sequence[AgentHealthType],
        "agentHealthCodes": Sequence[AgentHealthCodeType],
    },
)

AgentPreviewTypeDef = TypedDict(
    "AgentPreviewTypeDef",
    {
        "agentId": str,
        "hostname": NotRequired[str],
        "autoScalingGroup": NotRequired[str],
        "agentHealth": NotRequired[AgentHealthType],
        "agentVersion": NotRequired[str],
        "operatingSystem": NotRequired[str],
        "kernelVersion": NotRequired[str],
        "ipv4Address": NotRequired[str],
    },
)

AssessmentRunAgentTypeDef = TypedDict(
    "AssessmentRunAgentTypeDef",
    {
        "agentId": str,
        "assessmentRunArn": str,
        "agentHealth": AgentHealthType,
        "agentHealthCode": AgentHealthCodeType,
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
        "agentHealthDetails": NotRequired[str],
        "autoScalingGroup": NotRequired[str],
    },
)

AssessmentRunFilterTypeDef = TypedDict(
    "AssessmentRunFilterTypeDef",
    {
        "namePattern": NotRequired[str],
        "states": NotRequired[Sequence[AssessmentRunStateType]],
        "durationRange": NotRequired["DurationRangeTypeDef"],
        "rulesPackageArns": NotRequired[Sequence[str]],
        "startTimeRange": NotRequired["TimestampRangeTypeDef"],
        "completionTimeRange": NotRequired["TimestampRangeTypeDef"],
        "stateChangeTimeRange": NotRequired["TimestampRangeTypeDef"],
    },
)

AssessmentRunNotificationTypeDef = TypedDict(
    "AssessmentRunNotificationTypeDef",
    {
        "date": datetime,
        "event": InspectorEventType,
        "error": bool,
        "message": NotRequired[str],
        "snsTopicArn": NotRequired[str],
        "snsPublishStatusCode": NotRequired[AssessmentRunNotificationSnsStatusCodeType],
    },
)

AssessmentRunStateChangeTypeDef = TypedDict(
    "AssessmentRunStateChangeTypeDef",
    {
        "stateChangedAt": datetime,
        "state": AssessmentRunStateType,
    },
)

AssessmentRunTypeDef = TypedDict(
    "AssessmentRunTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTemplateArn": str,
        "state": AssessmentRunStateType,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "createdAt": datetime,
        "stateChangedAt": datetime,
        "dataCollected": bool,
        "stateChanges": List["AssessmentRunStateChangeTypeDef"],
        "notifications": List["AssessmentRunNotificationTypeDef"],
        "findingCounts": Dict[SeverityType, int],
        "startedAt": NotRequired[datetime],
        "completedAt": NotRequired[datetime],
    },
)

AssessmentTargetFilterTypeDef = TypedDict(
    "AssessmentTargetFilterTypeDef",
    {
        "assessmentTargetNamePattern": NotRequired[str],
    },
)

AssessmentTargetTypeDef = TypedDict(
    "AssessmentTargetTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "resourceGroupArn": NotRequired[str],
    },
)

AssessmentTemplateFilterTypeDef = TypedDict(
    "AssessmentTemplateFilterTypeDef",
    {
        "namePattern": NotRequired[str],
        "durationRange": NotRequired["DurationRangeTypeDef"],
        "rulesPackageArns": NotRequired[Sequence[str]],
    },
)

AssessmentTemplateTypeDef = TypedDict(
    "AssessmentTemplateTypeDef",
    {
        "arn": str,
        "name": str,
        "assessmentTargetArn": str,
        "durationInSeconds": int,
        "rulesPackageArns": List[str],
        "userAttributesForFindings": List["AttributeTypeDef"],
        "assessmentRunCount": int,
        "createdAt": datetime,
        "lastAssessmentRunArn": NotRequired[str],
    },
)

AssetAttributesTypeDef = TypedDict(
    "AssetAttributesTypeDef",
    {
        "schemaVersion": int,
        "agentId": NotRequired[str],
        "autoScalingGroup": NotRequired[str],
        "amiId": NotRequired[str],
        "hostname": NotRequired[str],
        "ipv4Addresses": NotRequired[List[str]],
        "tags": NotRequired[List["TagTypeDef"]],
        "networkInterfaces": NotRequired[List["NetworkInterfaceTypeDef"]],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)

CreateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "CreateAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetName": str,
        "resourceGroupArn": NotRequired[str],
    },
)

CreateAssessmentTargetResponseTypeDef = TypedDict(
    "CreateAssessmentTargetResponseTypeDef",
    {
        "assessmentTargetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "CreateAssessmentTemplateRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTemplateName": str,
        "durationInSeconds": int,
        "rulesPackageArns": Sequence[str],
        "userAttributesForFindings": NotRequired[Sequence["AttributeTypeDef"]],
    },
)

CreateAssessmentTemplateResponseTypeDef = TypedDict(
    "CreateAssessmentTemplateResponseTypeDef",
    {
        "assessmentTemplateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "CreateExclusionsPreviewRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)

CreateExclusionsPreviewResponseTypeDef = TypedDict(
    "CreateExclusionsPreviewResponseTypeDef",
    {
        "previewToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceGroupRequestRequestTypeDef = TypedDict(
    "CreateResourceGroupRequestRequestTypeDef",
    {
        "resourceGroupTags": Sequence["ResourceGroupTagTypeDef"],
    },
)

CreateResourceGroupResponseTypeDef = TypedDict(
    "CreateResourceGroupResponseTypeDef",
    {
        "resourceGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssessmentRunRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)

DeleteAssessmentTargetRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
    },
)

DeleteAssessmentTemplateRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentTemplateRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
    },
)

DescribeAssessmentRunsRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentRunsRequestRequestTypeDef",
    {
        "assessmentRunArns": Sequence[str],
    },
)

DescribeAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeAssessmentRunsResponseTypeDef",
    {
        "assessmentRuns": List["AssessmentRunTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssessmentTargetsRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentTargetsRequestRequestTypeDef",
    {
        "assessmentTargetArns": Sequence[str],
    },
)

DescribeAssessmentTargetsResponseTypeDef = TypedDict(
    "DescribeAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargets": List["AssessmentTargetTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssessmentTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeAssessmentTemplatesRequestRequestTypeDef",
    {
        "assessmentTemplateArns": Sequence[str],
    },
)

DescribeAssessmentTemplatesResponseTypeDef = TypedDict(
    "DescribeAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplates": List["AssessmentTemplateTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCrossAccountAccessRoleResponseTypeDef = TypedDict(
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    {
        "roleArn": str,
        "valid": bool,
        "registeredAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExclusionsRequestRequestTypeDef = TypedDict(
    "DescribeExclusionsRequestRequestTypeDef",
    {
        "exclusionArns": Sequence[str],
        "locale": NotRequired[Literal["EN_US"]],
    },
)

DescribeExclusionsResponseTypeDef = TypedDict(
    "DescribeExclusionsResponseTypeDef",
    {
        "exclusions": Dict[str, "ExclusionTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFindingsRequestRequestTypeDef = TypedDict(
    "DescribeFindingsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
        "locale": NotRequired[Literal["EN_US"]],
    },
)

DescribeFindingsResponseTypeDef = TypedDict(
    "DescribeFindingsResponseTypeDef",
    {
        "findings": List["FindingTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceGroupsRequestRequestTypeDef = TypedDict(
    "DescribeResourceGroupsRequestRequestTypeDef",
    {
        "resourceGroupArns": Sequence[str],
    },
)

DescribeResourceGroupsResponseTypeDef = TypedDict(
    "DescribeResourceGroupsResponseTypeDef",
    {
        "resourceGroups": List["ResourceGroupTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesPackagesRequestRequestTypeDef = TypedDict(
    "DescribeRulesPackagesRequestRequestTypeDef",
    {
        "rulesPackageArns": Sequence[str],
        "locale": NotRequired[Literal["EN_US"]],
    },
)

DescribeRulesPackagesResponseTypeDef = TypedDict(
    "DescribeRulesPackagesResponseTypeDef",
    {
        "rulesPackages": List["RulesPackageTypeDef"],
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DurationRangeTypeDef = TypedDict(
    "DurationRangeTypeDef",
    {
        "minSeconds": NotRequired[int],
        "maxSeconds": NotRequired[int],
    },
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "event": InspectorEventType,
        "subscribedAt": datetime,
    },
)

ExclusionPreviewTypeDef = TypedDict(
    "ExclusionPreviewTypeDef",
    {
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
        "attributes": NotRequired[List["AttributeTypeDef"]],
    },
)

ExclusionTypeDef = TypedDict(
    "ExclusionTypeDef",
    {
        "arn": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "scopes": List["ScopeTypeDef"],
        "attributes": NotRequired[List["AttributeTypeDef"]],
    },
)

FailedItemDetailsTypeDef = TypedDict(
    "FailedItemDetailsTypeDef",
    {
        "failureCode": FailedItemErrorCodeType,
        "retryable": bool,
    },
)

FindingFilterTypeDef = TypedDict(
    "FindingFilterTypeDef",
    {
        "agentIds": NotRequired[Sequence[str]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "ruleNames": NotRequired[Sequence[str]],
        "severities": NotRequired[Sequence[SeverityType]],
        "rulesPackageArns": NotRequired[Sequence[str]],
        "attributes": NotRequired[Sequence["AttributeTypeDef"]],
        "userAttributes": NotRequired[Sequence["AttributeTypeDef"]],
        "creationTimeRange": NotRequired["TimestampRangeTypeDef"],
    },
)

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "arn": str,
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "createdAt": datetime,
        "updatedAt": datetime,
        "schemaVersion": NotRequired[int],
        "service": NotRequired[str],
        "serviceAttributes": NotRequired["InspectorServiceAttributesTypeDef"],
        "assetType": NotRequired[Literal["ec2-instance"]],
        "assetAttributes": NotRequired["AssetAttributesTypeDef"],
        "id": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "recommendation": NotRequired[str],
        "severity": NotRequired[SeverityType],
        "numericSeverity": NotRequired[float],
        "confidence": NotRequired[int],
        "indicatorOfCompromise": NotRequired[bool],
    },
)

GetAssessmentReportRequestRequestTypeDef = TypedDict(
    "GetAssessmentReportRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "reportFileFormat": ReportFileFormatType,
        "reportType": ReportTypeType,
    },
)

GetAssessmentReportResponseTypeDef = TypedDict(
    "GetAssessmentReportResponseTypeDef",
    {
        "status": ReportStatusType,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExclusionsPreviewRequestRequestTypeDef = TypedDict(
    "GetExclusionsPreviewRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
        "previewToken": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[Literal["EN_US"]],
    },
)

GetExclusionsPreviewResponseTypeDef = TypedDict(
    "GetExclusionsPreviewResponseTypeDef",
    {
        "previewStatus": PreviewStatusType,
        "exclusionPreviews": List["ExclusionPreviewTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTelemetryMetadataRequestRequestTypeDef = TypedDict(
    "GetTelemetryMetadataRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
    },
)

GetTelemetryMetadataResponseTypeDef = TypedDict(
    "GetTelemetryMetadataResponseTypeDef",
    {
        "telemetryMetadata": List["TelemetryMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InspectorServiceAttributesTypeDef = TypedDict(
    "InspectorServiceAttributesTypeDef",
    {
        "schemaVersion": int,
        "assessmentRunArn": NotRequired[str],
        "rulesPackageArn": NotRequired[str],
    },
)

ListAssessmentRunAgentsRequestRequestTypeDef = TypedDict(
    "ListAssessmentRunAgentsRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "filter": NotRequired["AgentFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentRunAgentsResponseTypeDef = TypedDict(
    "ListAssessmentRunAgentsResponseTypeDef",
    {
        "assessmentRunAgents": List["AssessmentRunAgentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentRunsRequestRequestTypeDef = TypedDict(
    "ListAssessmentRunsRequestRequestTypeDef",
    {
        "assessmentTemplateArns": NotRequired[Sequence[str]],
        "filter": NotRequired["AssessmentRunFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentRunsResponseTypeDef = TypedDict(
    "ListAssessmentRunsResponseTypeDef",
    {
        "assessmentRunArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentTargetsRequestRequestTypeDef = TypedDict(
    "ListAssessmentTargetsRequestRequestTypeDef",
    {
        "filter": NotRequired["AssessmentTargetFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentTargetsResponseTypeDef = TypedDict(
    "ListAssessmentTargetsResponseTypeDef",
    {
        "assessmentTargetArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentTemplatesRequestRequestTypeDef = TypedDict(
    "ListAssessmentTemplatesRequestRequestTypeDef",
    {
        "assessmentTargetArns": NotRequired[Sequence[str]],
        "filter": NotRequired["AssessmentTemplateFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssessmentTemplatesResponseTypeDef = TypedDict(
    "ListAssessmentTemplatesResponseTypeDef",
    {
        "assessmentTemplateArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListEventSubscriptionsRequestRequestTypeDef",
    {
        "resourceArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListEventSubscriptionsResponseTypeDef = TypedDict(
    "ListEventSubscriptionsResponseTypeDef",
    {
        "subscriptions": List["SubscriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExclusionsRequestRequestTypeDef = TypedDict(
    "ListExclusionsRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListExclusionsResponseTypeDef = TypedDict(
    "ListExclusionsResponseTypeDef",
    {
        "exclusionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "assessmentRunArns": NotRequired[Sequence[str]],
        "filter": NotRequired["FindingFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesPackagesRequestRequestTypeDef = TypedDict(
    "ListRulesPackagesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListRulesPackagesResponseTypeDef = TypedDict(
    "ListRulesPackagesResponseTypeDef",
    {
        "rulesPackageArns": List[str],
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

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": NotRequired[str],
        "subnetId": NotRequired[str],
        "vpcId": NotRequired[str],
        "privateDnsName": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "privateIpAddresses": NotRequired[List["PrivateIpTypeDef"]],
        "publicDnsName": NotRequired[str],
        "publicIp": NotRequired[str],
        "ipv6Addresses": NotRequired[List[str]],
        "securityGroups": NotRequired[List["SecurityGroupTypeDef"]],
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

PreviewAgentsRequestRequestTypeDef = TypedDict(
    "PreviewAgentsRequestRequestTypeDef",
    {
        "previewAgentsArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

PreviewAgentsResponseTypeDef = TypedDict(
    "PreviewAgentsResponseTypeDef",
    {
        "agentPreviews": List["AgentPreviewTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PrivateIpTypeDef = TypedDict(
    "PrivateIpTypeDef",
    {
        "privateDnsName": NotRequired[str],
        "privateIpAddress": NotRequired[str],
    },
)

RegisterCrossAccountAccessRoleRequestRequestTypeDef = TypedDict(
    "RegisterCrossAccountAccessRoleRequestRequestTypeDef",
    {
        "roleArn": str,
    },
)

RemoveAttributesFromFindingsRequestRequestTypeDef = TypedDict(
    "RemoveAttributesFromFindingsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
        "attributeKeys": Sequence[str],
    },
)

RemoveAttributesFromFindingsResponseTypeDef = TypedDict(
    "RemoveAttributesFromFindingsResponseTypeDef",
    {
        "failedItems": Dict[str, "FailedItemDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceGroupTagTypeDef = TypedDict(
    "ResourceGroupTagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)

ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "arn": str,
        "tags": List["ResourceGroupTagTypeDef"],
        "createdAt": datetime,
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

RulesPackageTypeDef = TypedDict(
    "RulesPackageTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "provider": str,
        "description": NotRequired[str],
    },
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "key": NotRequired[ScopeTypeType],
        "value": NotRequired[str],
    },
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "groupName": NotRequired[str],
        "groupId": NotRequired[str],
    },
)

SetTagsForResourceRequestRequestTypeDef = TypedDict(
    "SetTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartAssessmentRunRequestRequestTypeDef = TypedDict(
    "StartAssessmentRunRequestRequestTypeDef",
    {
        "assessmentTemplateArn": str,
        "assessmentRunName": NotRequired[str],
    },
)

StartAssessmentRunResponseTypeDef = TypedDict(
    "StartAssessmentRunResponseTypeDef",
    {
        "assessmentRunArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAssessmentRunRequestRequestTypeDef = TypedDict(
    "StopAssessmentRunRequestRequestTypeDef",
    {
        "assessmentRunArn": str,
        "stopAction": NotRequired[StopActionType],
    },
)

SubscribeToEventRequestRequestTypeDef = TypedDict(
    "SubscribeToEventRequestRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "resourceArn": str,
        "topicArn": str,
        "eventSubscriptions": List["EventSubscriptionTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)

TelemetryMetadataTypeDef = TypedDict(
    "TelemetryMetadataTypeDef",
    {
        "messageType": str,
        "count": int,
        "dataSize": NotRequired[int],
    },
)

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "beginDate": NotRequired[Union[datetime, str]],
        "endDate": NotRequired[Union[datetime, str]],
    },
)

UnsubscribeFromEventRequestRequestTypeDef = TypedDict(
    "UnsubscribeFromEventRequestRequestTypeDef",
    {
        "resourceArn": str,
        "event": InspectorEventType,
        "topicArn": str,
    },
)

UpdateAssessmentTargetRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentTargetRequestRequestTypeDef",
    {
        "assessmentTargetArn": str,
        "assessmentTargetName": str,
        "resourceGroupArn": NotRequired[str],
    },
)
