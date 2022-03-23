"""
Type annotations for health service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_health/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_health.type_defs import AffectedEntityTypeDef

    data: AffectedEntityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    entityStatusCodeType,
    eventScopeCodeType,
    eventStatusCodeType,
    eventTypeCategoryType,
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
    "AffectedEntityTypeDef",
    "DateTimeRangeTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesRequestRequestTypeDef",
    "DescribeAffectedEntitiesResponseTypeDef",
    "DescribeEntityAggregatesRequestRequestTypeDef",
    "DescribeEntityAggregatesResponseTypeDef",
    "DescribeEventAggregatesRequestRequestTypeDef",
    "DescribeEventAggregatesResponseTypeDef",
    "DescribeEventDetailsForOrganizationRequestRequestTypeDef",
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    "DescribeEventDetailsRequestRequestTypeDef",
    "DescribeEventDetailsResponseTypeDef",
    "DescribeEventTypesRequestRequestTypeDef",
    "DescribeEventTypesResponseTypeDef",
    "DescribeEventsForOrganizationRequestRequestTypeDef",
    "DescribeEventsForOrganizationResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    "EntityAggregateTypeDef",
    "EntityFilterTypeDef",
    "EventAccountFilterTypeDef",
    "EventAggregateTypeDef",
    "EventDescriptionTypeDef",
    "EventDetailsErrorItemTypeDef",
    "EventDetailsTypeDef",
    "EventFilterTypeDef",
    "EventTypeDef",
    "EventTypeFilterTypeDef",
    "EventTypeTypeDef",
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    "OrganizationEventDetailsErrorItemTypeDef",
    "OrganizationEventDetailsTypeDef",
    "OrganizationEventFilterTypeDef",
    "OrganizationEventTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

AffectedEntityTypeDef = TypedDict(
    "AffectedEntityTypeDef",
    {
        "entityArn": NotRequired[str],
        "eventArn": NotRequired[str],
        "entityValue": NotRequired[str],
        "entityUrl": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "lastUpdatedTime": NotRequired[datetime],
        "statusCode": NotRequired[entityStatusCodeType],
        "tags": NotRequired[Dict[str, str]],
    },
)

DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef",
    {
        "from": NotRequired[Union[datetime, str]],
        "to": NotRequired[Union[datetime, str]],
    },
)

DescribeAffectedAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    {
        "eventArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeAffectedAccountsForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    {
        "affectedAccounts": List[str],
        "eventScopeCode": eventScopeCodeType,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    {
        "organizationEntityFilters": Sequence["EventAccountFilterTypeDef"],
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeAffectedEntitiesForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    {
        "entities": List["AffectedEntityTypeDef"],
        "failedSet": List["OrganizationAffectedEntitiesErrorItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAffectedEntitiesRequestRequestTypeDef = TypedDict(
    "DescribeAffectedEntitiesRequestRequestTypeDef",
    {
        "filter": "EntityFilterTypeDef",
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesResponseTypeDef",
    {
        "entities": List["AffectedEntityTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityAggregatesRequestRequestTypeDef = TypedDict(
    "DescribeEntityAggregatesRequestRequestTypeDef",
    {
        "eventArns": NotRequired[Sequence[str]],
    },
)

DescribeEntityAggregatesResponseTypeDef = TypedDict(
    "DescribeEntityAggregatesResponseTypeDef",
    {
        "entityAggregates": List["EntityAggregateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventAggregatesRequestRequestTypeDef = TypedDict(
    "DescribeEventAggregatesRequestRequestTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
        "filter": NotRequired["EventFilterTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeEventAggregatesResponseTypeDef = TypedDict(
    "DescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List["EventAggregateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventDetailsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeEventDetailsForOrganizationRequestRequestTypeDef",
    {
        "organizationEventDetailFilters": Sequence["EventAccountFilterTypeDef"],
        "locale": NotRequired[str],
    },
)

DescribeEventDetailsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    {
        "successfulSet": List["OrganizationEventDetailsTypeDef"],
        "failedSet": List["OrganizationEventDetailsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventDetailsRequestRequestTypeDef = TypedDict(
    "DescribeEventDetailsRequestRequestTypeDef",
    {
        "eventArns": Sequence[str],
        "locale": NotRequired[str],
    },
)

DescribeEventDetailsResponseTypeDef = TypedDict(
    "DescribeEventDetailsResponseTypeDef",
    {
        "successfulSet": List["EventDetailsTypeDef"],
        "failedSet": List["EventDetailsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTypesRequestRequestTypeDef = TypedDict(
    "DescribeEventTypesRequestRequestTypeDef",
    {
        "filter": NotRequired["EventTypeFilterTypeDef"],
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeEventTypesResponseTypeDef = TypedDict(
    "DescribeEventTypesResponseTypeDef",
    {
        "eventTypes": List["EventTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestRequestTypeDef",
    {
        "filter": NotRequired["OrganizationEventFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[str],
    },
)

DescribeEventsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventsForOrganizationResponseTypeDef",
    {
        "events": List["OrganizationEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "filter": NotRequired["EventFilterTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[str],
    },
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "events": List["EventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHealthServiceStatusForOrganizationResponseTypeDef = TypedDict(
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    {
        "healthServiceAccessStatusForOrganization": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityAggregateTypeDef = TypedDict(
    "EntityAggregateTypeDef",
    {
        "eventArn": NotRequired[str],
        "count": NotRequired[int],
    },
)

EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef",
    {
        "eventArns": Sequence[str],
        "entityArns": NotRequired[Sequence[str]],
        "entityValues": NotRequired[Sequence[str]],
        "lastUpdatedTimes": NotRequired[Sequence["DateTimeRangeTypeDef"]],
        "tags": NotRequired[Sequence[Mapping[str, str]]],
        "statusCodes": NotRequired[Sequence[entityStatusCodeType]],
    },
)

EventAccountFilterTypeDef = TypedDict(
    "EventAccountFilterTypeDef",
    {
        "eventArn": str,
        "awsAccountId": NotRequired[str],
    },
)

EventAggregateTypeDef = TypedDict(
    "EventAggregateTypeDef",
    {
        "aggregateValue": NotRequired[str],
        "count": NotRequired[int],
    },
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "latestDescription": NotRequired[str],
    },
)

EventDetailsErrorItemTypeDef = TypedDict(
    "EventDetailsErrorItemTypeDef",
    {
        "eventArn": NotRequired[str],
        "errorName": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

EventDetailsTypeDef = TypedDict(
    "EventDetailsTypeDef",
    {
        "event": NotRequired["EventTypeDef"],
        "eventDescription": NotRequired["EventDescriptionTypeDef"],
        "eventMetadata": NotRequired[Dict[str, str]],
    },
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "eventArns": NotRequired[Sequence[str]],
        "eventTypeCodes": NotRequired[Sequence[str]],
        "services": NotRequired[Sequence[str]],
        "regions": NotRequired[Sequence[str]],
        "availabilityZones": NotRequired[Sequence[str]],
        "startTimes": NotRequired[Sequence["DateTimeRangeTypeDef"]],
        "endTimes": NotRequired[Sequence["DateTimeRangeTypeDef"]],
        "lastUpdatedTimes": NotRequired[Sequence["DateTimeRangeTypeDef"]],
        "entityArns": NotRequired[Sequence[str]],
        "entityValues": NotRequired[Sequence[str]],
        "eventTypeCategories": NotRequired[Sequence[eventTypeCategoryType]],
        "tags": NotRequired[Sequence[Mapping[str, str]]],
        "eventStatusCodes": NotRequired[Sequence[eventStatusCodeType]],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "arn": NotRequired[str],
        "service": NotRequired[str],
        "eventTypeCode": NotRequired[str],
        "eventTypeCategory": NotRequired[eventTypeCategoryType],
        "region": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "statusCode": NotRequired[eventStatusCodeType],
        "eventScopeCode": NotRequired[eventScopeCodeType],
    },
)

EventTypeFilterTypeDef = TypedDict(
    "EventTypeFilterTypeDef",
    {
        "eventTypeCodes": NotRequired[Sequence[str]],
        "services": NotRequired[Sequence[str]],
        "eventTypeCategories": NotRequired[Sequence[eventTypeCategoryType]],
    },
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "service": NotRequired[str],
        "code": NotRequired[str],
        "category": NotRequired[eventTypeCategoryType],
    },
)

OrganizationAffectedEntitiesErrorItemTypeDef = TypedDict(
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "eventArn": NotRequired[str],
        "errorName": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

OrganizationEventDetailsErrorItemTypeDef = TypedDict(
    "OrganizationEventDetailsErrorItemTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "eventArn": NotRequired[str],
        "errorName": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

OrganizationEventDetailsTypeDef = TypedDict(
    "OrganizationEventDetailsTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "event": NotRequired["EventTypeDef"],
        "eventDescription": NotRequired["EventDescriptionTypeDef"],
        "eventMetadata": NotRequired[Dict[str, str]],
    },
)

OrganizationEventFilterTypeDef = TypedDict(
    "OrganizationEventFilterTypeDef",
    {
        "eventTypeCodes": NotRequired[Sequence[str]],
        "awsAccountIds": NotRequired[Sequence[str]],
        "services": NotRequired[Sequence[str]],
        "regions": NotRequired[Sequence[str]],
        "startTime": NotRequired["DateTimeRangeTypeDef"],
        "endTime": NotRequired["DateTimeRangeTypeDef"],
        "lastUpdatedTime": NotRequired["DateTimeRangeTypeDef"],
        "entityArns": NotRequired[Sequence[str]],
        "entityValues": NotRequired[Sequence[str]],
        "eventTypeCategories": NotRequired[Sequence[eventTypeCategoryType]],
        "eventStatusCodes": NotRequired[Sequence[eventStatusCodeType]],
    },
)

OrganizationEventTypeDef = TypedDict(
    "OrganizationEventTypeDef",
    {
        "arn": NotRequired[str],
        "service": NotRequired[str],
        "eventTypeCode": NotRequired[str],
        "eventTypeCategory": NotRequired[eventTypeCategoryType],
        "eventScopeCode": NotRequired[eventScopeCodeType],
        "region": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "statusCode": NotRequired[eventStatusCodeType],
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
