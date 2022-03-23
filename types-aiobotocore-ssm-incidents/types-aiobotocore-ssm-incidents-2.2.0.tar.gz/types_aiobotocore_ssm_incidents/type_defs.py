"""
Type annotations for ssm-incidents service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_incidents/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_ssm_incidents.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SortOrderType,
    SsmTargetAccountType,
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
    "ActionTypeDef",
    "AddRegionActionTypeDef",
    "AttributeValueListTypeDef",
    "AutomationExecutionTypeDef",
    "ChatChannelTypeDef",
    "ConditionTypeDef",
    "CreateReplicationSetInputRequestTypeDef",
    "CreateReplicationSetOutputTypeDef",
    "CreateResponsePlanInputRequestTypeDef",
    "CreateResponsePlanOutputTypeDef",
    "CreateTimelineEventInputRequestTypeDef",
    "CreateTimelineEventOutputTypeDef",
    "DeleteIncidentRecordInputRequestTypeDef",
    "DeleteRegionActionTypeDef",
    "DeleteReplicationSetInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteResponsePlanInputRequestTypeDef",
    "DeleteTimelineEventInputRequestTypeDef",
    "EventSummaryTypeDef",
    "FilterTypeDef",
    "GetIncidentRecordInputRequestTypeDef",
    "GetIncidentRecordOutputTypeDef",
    "GetReplicationSetInputRequestTypeDef",
    "GetReplicationSetOutputTypeDef",
    "GetResourcePoliciesInputRequestTypeDef",
    "GetResourcePoliciesOutputTypeDef",
    "GetResponsePlanInputRequestTypeDef",
    "GetResponsePlanOutputTypeDef",
    "GetTimelineEventInputRequestTypeDef",
    "GetTimelineEventOutputTypeDef",
    "IncidentRecordSourceTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateTypeDef",
    "ItemIdentifierTypeDef",
    "ItemValueTypeDef",
    "ListIncidentRecordsInputRequestTypeDef",
    "ListIncidentRecordsOutputTypeDef",
    "ListRelatedItemsInputRequestTypeDef",
    "ListRelatedItemsOutputTypeDef",
    "ListReplicationSetsInputRequestTypeDef",
    "ListReplicationSetsOutputTypeDef",
    "ListResponsePlansInputRequestTypeDef",
    "ListResponsePlansOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimelineEventsInputRequestTypeDef",
    "ListTimelineEventsOutputTypeDef",
    "NotificationTargetItemTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegionInfoTypeDef",
    "RegionMapInputValueTypeDef",
    "RelatedItemTypeDef",
    "RelatedItemsUpdateTypeDef",
    "ReplicationSetTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePlanSummaryTypeDef",
    "SsmAutomationTypeDef",
    "StartIncidentInputRequestTypeDef",
    "StartIncidentOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimelineEventTypeDef",
    "TriggerDetailsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeletionProtectionInputRequestTypeDef",
    "UpdateIncidentRecordInputRequestTypeDef",
    "UpdateRelatedItemsInputRequestTypeDef",
    "UpdateReplicationSetActionTypeDef",
    "UpdateReplicationSetInputRequestTypeDef",
    "UpdateResponsePlanInputRequestTypeDef",
    "UpdateTimelineEventInputRequestTypeDef",
    "WaiterConfigTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ssmAutomation": NotRequired["SsmAutomationTypeDef"],
    },
)

AddRegionActionTypeDef = TypedDict(
    "AddRegionActionTypeDef",
    {
        "regionName": str,
        "sseKmsKeyId": NotRequired[str],
    },
)

AttributeValueListTypeDef = TypedDict(
    "AttributeValueListTypeDef",
    {
        "integerValues": NotRequired[Sequence[int]],
        "stringValues": NotRequired[Sequence[str]],
    },
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "ssmExecutionArn": NotRequired[str],
    },
)

ChatChannelTypeDef = TypedDict(
    "ChatChannelTypeDef",
    {
        "chatbotSns": NotRequired[Sequence[str]],
        "empty": NotRequired[Mapping[str, Any]],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "after": NotRequired[Union[datetime, str]],
        "before": NotRequired[Union[datetime, str]],
        "equals": NotRequired["AttributeValueListTypeDef"],
    },
)

CreateReplicationSetInputRequestTypeDef = TypedDict(
    "CreateReplicationSetInputRequestTypeDef",
    {
        "regions": Mapping[str, "RegionMapInputValueTypeDef"],
        "clientToken": NotRequired[str],
    },
)

CreateReplicationSetOutputTypeDef = TypedDict(
    "CreateReplicationSetOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResponsePlanInputRequestTypeDef = TypedDict(
    "CreateResponsePlanInputRequestTypeDef",
    {
        "incidentTemplate": "IncidentTemplateTypeDef",
        "name": str,
        "actions": NotRequired[Sequence["ActionTypeDef"]],
        "chatChannel": NotRequired["ChatChannelTypeDef"],
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "engagements": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateResponsePlanOutputTypeDef = TypedDict(
    "CreateResponsePlanOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTimelineEventInputRequestTypeDef = TypedDict(
    "CreateTimelineEventInputRequestTypeDef",
    {
        "eventData": str,
        "eventTime": Union[datetime, str],
        "eventType": str,
        "incidentRecordArn": str,
        "clientToken": NotRequired[str],
    },
)

CreateTimelineEventOutputTypeDef = TypedDict(
    "CreateTimelineEventOutputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIncidentRecordInputRequestTypeDef = TypedDict(
    "DeleteIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRegionActionTypeDef = TypedDict(
    "DeleteRegionActionTypeDef",
    {
        "regionName": str,
    },
)

DeleteReplicationSetInputRequestTypeDef = TypedDict(
    "DeleteReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "policyId": str,
        "resourceArn": str,
    },
)

DeleteResponsePlanInputRequestTypeDef = TypedDict(
    "DeleteResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTimelineEventInputRequestTypeDef = TypedDict(
    "DeleteTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

EventSummaryTypeDef = TypedDict(
    "EventSummaryTypeDef",
    {
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "condition": "ConditionTypeDef",
        "key": str,
    },
)

GetIncidentRecordInputRequestTypeDef = TypedDict(
    "GetIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetIncidentRecordOutputTypeDef = TypedDict(
    "GetIncidentRecordOutputTypeDef",
    {
        "incidentRecord": "IncidentRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationSetInputRequestTypeDef = TypedDict(
    "GetReplicationSetInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetReplicationSetOutputTypeDef = TypedDict(
    "GetReplicationSetOutputTypeDef",
    {
        "replicationSet": "ReplicationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePoliciesInputRequestTypeDef = TypedDict(
    "GetResourcePoliciesInputRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetResourcePoliciesOutputTypeDef = TypedDict(
    "GetResourcePoliciesOutputTypeDef",
    {
        "nextToken": str,
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponsePlanInputRequestTypeDef = TypedDict(
    "GetResponsePlanInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetResponsePlanOutputTypeDef = TypedDict(
    "GetResponsePlanOutputTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "arn": str,
        "chatChannel": "ChatChannelTypeDef",
        "displayName": str,
        "engagements": List[str],
        "incidentTemplate": "IncidentTemplateTypeDef",
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTimelineEventInputRequestTypeDef = TypedDict(
    "GetTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

GetTimelineEventOutputTypeDef = TypedDict(
    "GetTimelineEventOutputTypeDef",
    {
        "event": "TimelineEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncidentRecordSourceTypeDef = TypedDict(
    "IncidentRecordSourceTypeDef",
    {
        "createdBy": str,
        "source": str,
        "invokedBy": NotRequired[str],
        "resourceArn": NotRequired[str],
    },
)

IncidentRecordSummaryTypeDef = TypedDict(
    "IncidentRecordSummaryTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "impact": int,
        "incidentRecordSource": "IncidentRecordSourceTypeDef",
        "status": IncidentRecordStatusType,
        "title": str,
        "resolvedTime": NotRequired[datetime],
    },
)

IncidentRecordTypeDef = TypedDict(
    "IncidentRecordTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "dedupeString": str,
        "impact": int,
        "incidentRecordSource": "IncidentRecordSourceTypeDef",
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "status": IncidentRecordStatusType,
        "title": str,
        "automationExecutions": NotRequired[List["AutomationExecutionTypeDef"]],
        "chatChannel": NotRequired["ChatChannelTypeDef"],
        "notificationTargets": NotRequired[List["NotificationTargetItemTypeDef"]],
        "resolvedTime": NotRequired[datetime],
        "summary": NotRequired[str],
    },
)

IncidentTemplateTypeDef = TypedDict(
    "IncidentTemplateTypeDef",
    {
        "impact": int,
        "title": str,
        "dedupeString": NotRequired[str],
        "notificationTargets": NotRequired[Sequence["NotificationTargetItemTypeDef"]],
        "summary": NotRequired[str],
    },
)

ItemIdentifierTypeDef = TypedDict(
    "ItemIdentifierTypeDef",
    {
        "type": ItemTypeType,
        "value": "ItemValueTypeDef",
    },
)

ItemValueTypeDef = TypedDict(
    "ItemValueTypeDef",
    {
        "arn": NotRequired[str],
        "metricDefinition": NotRequired[str],
        "url": NotRequired[str],
    },
)

ListIncidentRecordsInputRequestTypeDef = TypedDict(
    "ListIncidentRecordsInputRequestTypeDef",
    {
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListIncidentRecordsOutputTypeDef = TypedDict(
    "ListIncidentRecordsOutputTypeDef",
    {
        "incidentRecordSummaries": List["IncidentRecordSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRelatedItemsInputRequestTypeDef = TypedDict(
    "ListRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListRelatedItemsOutputTypeDef = TypedDict(
    "ListRelatedItemsOutputTypeDef",
    {
        "nextToken": str,
        "relatedItems": List["RelatedItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplicationSetsInputRequestTypeDef = TypedDict(
    "ListReplicationSetsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListReplicationSetsOutputTypeDef = TypedDict(
    "ListReplicationSetsOutputTypeDef",
    {
        "nextToken": str,
        "replicationSetArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResponsePlansInputRequestTypeDef = TypedDict(
    "ListResponsePlansInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListResponsePlansOutputTypeDef = TypedDict(
    "ListResponsePlansOutputTypeDef",
    {
        "nextToken": str,
        "responsePlanSummaries": List["ResponsePlanSummaryTypeDef"],
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

ListTimelineEventsInputRequestTypeDef = TypedDict(
    "ListTimelineEventsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["EVENT_TIME"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)

ListTimelineEventsOutputTypeDef = TypedDict(
    "ListTimelineEventsOutputTypeDef",
    {
        "eventSummaries": List["EventSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationTargetItemTypeDef = TypedDict(
    "NotificationTargetItemTypeDef",
    {
        "snsTopicArn": NotRequired[str],
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

PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {
        "policyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionInfoTypeDef = TypedDict(
    "RegionInfoTypeDef",
    {
        "status": RegionStatusType,
        "statusUpdateDateTime": datetime,
        "sseKmsKeyId": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)

RegionMapInputValueTypeDef = TypedDict(
    "RegionMapInputValueTypeDef",
    {
        "sseKmsKeyId": NotRequired[str],
    },
)

RelatedItemTypeDef = TypedDict(
    "RelatedItemTypeDef",
    {
        "identifier": "ItemIdentifierTypeDef",
        "title": NotRequired[str],
    },
)

RelatedItemsUpdateTypeDef = TypedDict(
    "RelatedItemsUpdateTypeDef",
    {
        "itemToAdd": NotRequired["RelatedItemTypeDef"],
        "itemToRemove": NotRequired["ItemIdentifierTypeDef"],
    },
)

ReplicationSetTypeDef = TypedDict(
    "ReplicationSetTypeDef",
    {
        "createdBy": str,
        "createdTime": datetime,
        "deletionProtected": bool,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "regionMap": Dict[str, "RegionInfoTypeDef"],
        "status": ReplicationSetStatusType,
        "arn": NotRequired[str],
    },
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyDocument": str,
        "policyId": str,
        "ramResourceShareRegion": str,
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

ResponsePlanSummaryTypeDef = TypedDict(
    "ResponsePlanSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "displayName": NotRequired[str],
    },
)

SsmAutomationTypeDef = TypedDict(
    "SsmAutomationTypeDef",
    {
        "documentName": str,
        "roleArn": str,
        "documentVersion": NotRequired[str],
        "parameters": NotRequired[Mapping[str, Sequence[str]]],
        "targetAccount": NotRequired[SsmTargetAccountType],
    },
)

StartIncidentInputRequestTypeDef = TypedDict(
    "StartIncidentInputRequestTypeDef",
    {
        "responsePlanArn": str,
        "clientToken": NotRequired[str],
        "impact": NotRequired[int],
        "relatedItems": NotRequired[Sequence["RelatedItemTypeDef"]],
        "title": NotRequired[str],
        "triggerDetails": NotRequired["TriggerDetailsTypeDef"],
    },
)

StartIncidentOutputTypeDef = TypedDict(
    "StartIncidentOutputTypeDef",
    {
        "incidentRecordArn": str,
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

TimelineEventTypeDef = TypedDict(
    "TimelineEventTypeDef",
    {
        "eventData": str,
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)

TriggerDetailsTypeDef = TypedDict(
    "TriggerDetailsTypeDef",
    {
        "source": str,
        "timestamp": Union[datetime, str],
        "rawData": NotRequired[str],
        "triggerArn": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateDeletionProtectionInputRequestTypeDef = TypedDict(
    "UpdateDeletionProtectionInputRequestTypeDef",
    {
        "arn": str,
        "deletionProtected": bool,
        "clientToken": NotRequired[str],
    },
)

UpdateIncidentRecordInputRequestTypeDef = TypedDict(
    "UpdateIncidentRecordInputRequestTypeDef",
    {
        "arn": str,
        "chatChannel": NotRequired["ChatChannelTypeDef"],
        "clientToken": NotRequired[str],
        "impact": NotRequired[int],
        "notificationTargets": NotRequired[Sequence["NotificationTargetItemTypeDef"]],
        "status": NotRequired[IncidentRecordStatusType],
        "summary": NotRequired[str],
        "title": NotRequired[str],
    },
)

UpdateRelatedItemsInputRequestTypeDef = TypedDict(
    "UpdateRelatedItemsInputRequestTypeDef",
    {
        "incidentRecordArn": str,
        "relatedItemsUpdate": "RelatedItemsUpdateTypeDef",
        "clientToken": NotRequired[str],
    },
)

UpdateReplicationSetActionTypeDef = TypedDict(
    "UpdateReplicationSetActionTypeDef",
    {
        "addRegionAction": NotRequired["AddRegionActionTypeDef"],
        "deleteRegionAction": NotRequired["DeleteRegionActionTypeDef"],
    },
)

UpdateReplicationSetInputRequestTypeDef = TypedDict(
    "UpdateReplicationSetInputRequestTypeDef",
    {
        "actions": Sequence["UpdateReplicationSetActionTypeDef"],
        "arn": str,
        "clientToken": NotRequired[str],
    },
)

UpdateResponsePlanInputRequestTypeDef = TypedDict(
    "UpdateResponsePlanInputRequestTypeDef",
    {
        "arn": str,
        "actions": NotRequired[Sequence["ActionTypeDef"]],
        "chatChannel": NotRequired["ChatChannelTypeDef"],
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "engagements": NotRequired[Sequence[str]],
        "incidentTemplateDedupeString": NotRequired[str],
        "incidentTemplateImpact": NotRequired[int],
        "incidentTemplateNotificationTargets": NotRequired[
            Sequence["NotificationTargetItemTypeDef"]
        ],
        "incidentTemplateSummary": NotRequired[str],
        "incidentTemplateTitle": NotRequired[str],
    },
)

UpdateTimelineEventInputRequestTypeDef = TypedDict(
    "UpdateTimelineEventInputRequestTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "clientToken": NotRequired[str],
        "eventData": NotRequired[str],
        "eventTime": NotRequired[Union[datetime, str]],
        "eventType": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
