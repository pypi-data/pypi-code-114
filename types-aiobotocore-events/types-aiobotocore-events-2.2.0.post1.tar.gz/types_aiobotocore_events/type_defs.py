"""
Type annotations for events service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_events/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_events.type_defs import ActivateEventSourceRequestRequestTypeDef

    data: ActivateEventSourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ApiDestinationHttpMethodType,
    ApiDestinationStateType,
    ArchiveStateType,
    AssignPublicIpType,
    ConnectionAuthorizationTypeType,
    ConnectionOAuthHttpMethodType,
    ConnectionStateType,
    EventSourceStateType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ReplayStateType,
    RuleStateType,
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
    "ActivateEventSourceRequestRequestTypeDef",
    "ApiDestinationTypeDef",
    "ArchiveTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchParametersTypeDef",
    "BatchRetryStrategyTypeDef",
    "CancelReplayRequestRequestTypeDef",
    "CancelReplayResponseTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "ConditionTypeDef",
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    "ConnectionAuthResponseParametersTypeDef",
    "ConnectionBasicAuthResponseParametersTypeDef",
    "ConnectionBodyParameterTypeDef",
    "ConnectionHeaderParameterTypeDef",
    "ConnectionHttpParametersTypeDef",
    "ConnectionOAuthClientResponseParametersTypeDef",
    "ConnectionOAuthResponseParametersTypeDef",
    "ConnectionQueryStringParameterTypeDef",
    "ConnectionTypeDef",
    "CreateApiDestinationRequestRequestTypeDef",
    "CreateApiDestinationResponseTypeDef",
    "CreateArchiveRequestRequestTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    "CreateConnectionAuthRequestParametersTypeDef",
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    "CreateConnectionOAuthRequestParametersTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateEventBusRequestRequestTypeDef",
    "CreateEventBusResponseTypeDef",
    "CreatePartnerEventSourceRequestRequestTypeDef",
    "CreatePartnerEventSourceResponseTypeDef",
    "DeactivateEventSourceRequestRequestTypeDef",
    "DeadLetterConfigTypeDef",
    "DeauthorizeConnectionRequestRequestTypeDef",
    "DeauthorizeConnectionResponseTypeDef",
    "DeleteApiDestinationRequestRequestTypeDef",
    "DeleteArchiveRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEventBusRequestRequestTypeDef",
    "DeletePartnerEventSourceRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DescribeApiDestinationRequestRequestTypeDef",
    "DescribeApiDestinationResponseTypeDef",
    "DescribeArchiveRequestRequestTypeDef",
    "DescribeArchiveResponseTypeDef",
    "DescribeConnectionRequestRequestTypeDef",
    "DescribeConnectionResponseTypeDef",
    "DescribeEventBusRequestRequestTypeDef",
    "DescribeEventBusResponseTypeDef",
    "DescribeEventSourceRequestRequestTypeDef",
    "DescribeEventSourceResponseTypeDef",
    "DescribePartnerEventSourceRequestRequestTypeDef",
    "DescribePartnerEventSourceResponseTypeDef",
    "DescribeReplayRequestRequestTypeDef",
    "DescribeReplayResponseTypeDef",
    "DescribeRuleRequestRequestTypeDef",
    "DescribeRuleResponseTypeDef",
    "DisableRuleRequestRequestTypeDef",
    "EcsParametersTypeDef",
    "EnableRuleRequestRequestTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "ListApiDestinationsRequestRequestTypeDef",
    "ListApiDestinationsResponseTypeDef",
    "ListArchivesRequestRequestTypeDef",
    "ListArchivesResponseTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListEventBusesRequestRequestTypeDef",
    "ListEventBusesResponseTypeDef",
    "ListEventSourcesRequestRequestTypeDef",
    "ListEventSourcesResponseTypeDef",
    "ListPartnerEventSourceAccountsRequestRequestTypeDef",
    "ListPartnerEventSourceAccountsResponseTypeDef",
    "ListPartnerEventSourcesRequestRequestTypeDef",
    "ListPartnerEventSourcesResponseTypeDef",
    "ListReplaysRequestRequestTypeDef",
    "ListReplaysResponseTypeDef",
    "ListRuleNamesByTargetRequestRequestTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsByRuleRequestRequestTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "PartnerEventSourceTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutEventsResponseTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutPartnerEventsRequestRequestTypeDef",
    "PutPartnerEventsResponseTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "PutRuleRequestRequestTypeDef",
    "PutRuleResponseTypeDef",
    "PutTargetsRequestRequestTypeDef",
    "PutTargetsResponseTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "RemoveTargetsRequestRequestTypeDef",
    "RemoveTargetsResponseTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "ReplayTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyTypeDef",
    "RuleTypeDef",
    "RunCommandParametersTypeDef",
    "RunCommandTargetTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "SqsParametersTypeDef",
    "StartReplayRequestRequestTypeDef",
    "StartReplayResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TestEventPatternRequestRequestTypeDef",
    "TestEventPatternResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiDestinationRequestRequestTypeDef",
    "UpdateApiDestinationResponseTypeDef",
    "UpdateArchiveRequestRequestTypeDef",
    "UpdateArchiveResponseTypeDef",
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    "UpdateConnectionAuthRequestParametersTypeDef",
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    "UpdateConnectionOAuthRequestParametersTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateConnectionResponseTypeDef",
)

ActivateEventSourceRequestRequestTypeDef = TypedDict(
    "ActivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

ApiDestinationTypeDef = TypedDict(
    "ApiDestinationTypeDef",
    {
        "ApiDestinationArn": NotRequired[str],
        "Name": NotRequired[str],
        "ApiDestinationState": NotRequired[ApiDestinationStateType],
        "ConnectionArn": NotRequired[str],
        "InvocationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ApiDestinationHttpMethodType],
        "InvocationRateLimitPerSecond": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveName": NotRequired[str],
        "EventSourceArn": NotRequired[str],
        "State": NotRequired[ArchiveStateType],
        "StateReason": NotRequired[str],
        "RetentionDays": NotRequired[int],
        "SizeBytes": NotRequired[int],
        "EventCount": NotRequired[int],
        "CreationTime": NotRequired[datetime],
    },
)

AwsVpcConfigurationTypeDef = TypedDict(
    "AwsVpcConfigurationTypeDef",
    {
        "Subnets": List[str],
        "SecurityGroups": NotRequired[List[str]],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
    },
)

BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": NotRequired[int],
    },
)

BatchParametersTypeDef = TypedDict(
    "BatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
        "ArrayProperties": NotRequired["BatchArrayPropertiesTypeDef"],
        "RetryStrategy": NotRequired["BatchRetryStrategyTypeDef"],
    },
)

BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": NotRequired[int],
    },
)

CancelReplayRequestRequestTypeDef = TypedDict(
    "CancelReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)

CancelReplayResponseTypeDef = TypedDict(
    "CancelReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityProviderStrategyItemTypeDef = TypedDict(
    "CapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
        "weight": NotRequired[int],
        "base": NotRequired[int],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Type": str,
        "Key": str,
        "Value": str,
    },
)

ConnectionApiKeyAuthResponseParametersTypeDef = TypedDict(
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    {
        "ApiKeyName": NotRequired[str],
    },
)

ConnectionAuthResponseParametersTypeDef = TypedDict(
    "ConnectionAuthResponseParametersTypeDef",
    {
        "BasicAuthParameters": NotRequired["ConnectionBasicAuthResponseParametersTypeDef"],
        "OAuthParameters": NotRequired["ConnectionOAuthResponseParametersTypeDef"],
        "ApiKeyAuthParameters": NotRequired["ConnectionApiKeyAuthResponseParametersTypeDef"],
        "InvocationHttpParameters": NotRequired["ConnectionHttpParametersTypeDef"],
    },
)

ConnectionBasicAuthResponseParametersTypeDef = TypedDict(
    "ConnectionBasicAuthResponseParametersTypeDef",
    {
        "Username": NotRequired[str],
    },
)

ConnectionBodyParameterTypeDef = TypedDict(
    "ConnectionBodyParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "IsValueSecret": NotRequired[bool],
    },
)

ConnectionHeaderParameterTypeDef = TypedDict(
    "ConnectionHeaderParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "IsValueSecret": NotRequired[bool],
    },
)

ConnectionHttpParametersTypeDef = TypedDict(
    "ConnectionHttpParametersTypeDef",
    {
        "HeaderParameters": NotRequired[Sequence["ConnectionHeaderParameterTypeDef"]],
        "QueryStringParameters": NotRequired[Sequence["ConnectionQueryStringParameterTypeDef"]],
        "BodyParameters": NotRequired[Sequence["ConnectionBodyParameterTypeDef"]],
    },
)

ConnectionOAuthClientResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthClientResponseParametersTypeDef",
    {
        "ClientID": NotRequired[str],
    },
)

ConnectionOAuthResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthResponseParametersTypeDef",
    {
        "ClientParameters": NotRequired["ConnectionOAuthClientResponseParametersTypeDef"],
        "AuthorizationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ConnectionOAuthHttpMethodType],
        "OAuthHttpParameters": NotRequired["ConnectionHttpParametersTypeDef"],
    },
)

ConnectionQueryStringParameterTypeDef = TypedDict(
    "ConnectionQueryStringParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "IsValueSecret": NotRequired[bool],
    },
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionArn": NotRequired[str],
        "Name": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateType],
        "StateReason": NotRequired[str],
        "AuthorizationType": NotRequired[ConnectionAuthorizationTypeType],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LastAuthorizedTime": NotRequired[datetime],
    },
)

CreateApiDestinationRequestRequestTypeDef = TypedDict(
    "CreateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "Description": NotRequired[str],
        "InvocationRateLimitPerSecond": NotRequired[int],
    },
)

CreateApiDestinationResponseTypeDef = TypedDict(
    "CreateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateArchiveRequestRequestTypeDef = TypedDict(
    "CreateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": NotRequired[str],
        "EventPattern": NotRequired[str],
        "RetentionDays": NotRequired[int],
    },
)

CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
)

CreateConnectionAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": NotRequired["CreateConnectionBasicAuthRequestParametersTypeDef"],
        "OAuthParameters": NotRequired["CreateConnectionOAuthRequestParametersTypeDef"],
        "ApiKeyAuthParameters": NotRequired["CreateConnectionApiKeyAuthRequestParametersTypeDef"],
        "InvocationHttpParameters": NotRequired["ConnectionHttpParametersTypeDef"],
    },
)

CreateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

CreateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
)

CreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": "CreateConnectionOAuthClientRequestParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": NotRequired["ConnectionHttpParametersTypeDef"],
    },
)

CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": "CreateConnectionAuthRequestParametersTypeDef",
        "Description": NotRequired[str],
    },
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventBusRequestRequestTypeDef = TypedDict(
    "CreateEventBusRequestRequestTypeDef",
    {
        "Name": str,
        "EventSourceName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEventBusResponseTypeDef = TypedDict(
    "CreateEventBusResponseTypeDef",
    {
        "EventBusArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "CreatePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

CreatePartnerEventSourceResponseTypeDef = TypedDict(
    "CreatePartnerEventSourceResponseTypeDef",
    {
        "EventSourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateEventSourceRequestRequestTypeDef = TypedDict(
    "DeactivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

DeauthorizeConnectionRequestRequestTypeDef = TypedDict(
    "DeauthorizeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeauthorizeConnectionResponseTypeDef = TypedDict(
    "DeauthorizeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApiDestinationRequestRequestTypeDef = TypedDict(
    "DeleteApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteArchiveRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventBusRequestRequestTypeDef = TypedDict(
    "DeleteEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeletePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DeletePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
        "Force": NotRequired[bool],
    },
)

DescribeApiDestinationRequestRequestTypeDef = TypedDict(
    "DescribeApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeApiDestinationResponseTypeDef = TypedDict(
    "DescribeApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "Description": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArchiveRequestRequestTypeDef = TypedDict(
    "DescribeArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DescribeArchiveResponseTypeDef = TypedDict(
    "DescribeArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": str,
        "EventPattern": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionRequestRequestTypeDef = TypedDict(
    "DescribeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeConnectionResponseTypeDef = TypedDict(
    "DescribeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "Description": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "SecretArn": str,
        "AuthParameters": "ConnectionAuthResponseParametersTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventBusRequestRequestTypeDef = TypedDict(
    "DescribeEventBusRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
    },
)

DescribeEventBusResponseTypeDef = TypedDict(
    "DescribeEventBusResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSourceRequestRequestTypeDef = TypedDict(
    "DescribeEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeEventSourceResponseTypeDef = TypedDict(
    "DescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DescribePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribePartnerEventSourceResponseTypeDef = TypedDict(
    "DescribePartnerEventSourceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplayRequestRequestTypeDef = TypedDict(
    "DescribeReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)

DescribeReplayResponseTypeDef = TypedDict(
    "DescribeReplayResponseTypeDef",
    {
        "ReplayName": str,
        "ReplayArn": str,
        "Description": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventSourceArn": str,
        "Destination": "ReplayDestinationTypeDef",
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleRequestRequestTypeDef = TypedDict(
    "DescribeRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
    },
)

DescribeRuleResponseTypeDef = TypedDict(
    "DescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
        "CreatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableRuleRequestRequestTypeDef = TypedDict(
    "DisableRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
    },
)

EcsParametersTypeDef = TypedDict(
    "EcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "TaskCount": NotRequired[int],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
        "PlatformVersion": NotRequired[str],
        "Group": NotRequired[str],
        "CapacityProviderStrategy": NotRequired[List["CapacityProviderStrategyItemTypeDef"]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "PlacementConstraints": NotRequired[List["PlacementConstraintTypeDef"]],
        "PlacementStrategy": NotRequired[List["PlacementStrategyTypeDef"]],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

EnableRuleRequestRequestTypeDef = TypedDict(
    "EnableRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventBusName": NotRequired[str],
    },
)

EventBusTypeDef = TypedDict(
    "EventBusTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Policy": NotRequired[str],
    },
)

EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "State": NotRequired[EventSourceStateType],
    },
)

HttpParametersTypeDef = TypedDict(
    "HttpParametersTypeDef",
    {
        "PathParameterValues": NotRequired[List[str]],
        "HeaderParameters": NotRequired[Dict[str, str]],
        "QueryStringParameters": NotRequired[Dict[str, str]],
    },
)

InputTransformerTypeDef = TypedDict(
    "InputTransformerTypeDef",
    {
        "InputTemplate": str,
        "InputPathsMap": NotRequired[Dict[str, str]],
    },
)

KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKeyPath": str,
    },
)

ListApiDestinationsRequestRequestTypeDef = TypedDict(
    "ListApiDestinationsRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListApiDestinationsResponseTypeDef = TypedDict(
    "ListApiDestinationsResponseTypeDef",
    {
        "ApiDestinations": List["ApiDestinationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArchivesRequestRequestTypeDef = TypedDict(
    "ListArchivesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "EventSourceArn": NotRequired[str],
        "State": NotRequired[ArchiveStateType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {
        "Archives": List["ArchiveTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventBusesRequestRequestTypeDef = TypedDict(
    "ListEventBusesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListEventBusesResponseTypeDef = TypedDict(
    "ListEventBusesResponseTypeDef",
    {
        "EventBuses": List["EventBusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourcesRequestRequestTypeDef = TypedDict(
    "ListEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListEventSourcesResponseTypeDef = TypedDict(
    "ListEventSourcesResponseTypeDef",
    {
        "EventSources": List["EventSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnerEventSourceAccountsRequestRequestTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsRequestRequestTypeDef",
    {
        "EventSourceName": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List["PartnerEventSourceAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnerEventSourcesRequestRequestTypeDef = TypedDict(
    "ListPartnerEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List["PartnerEventSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplaysRequestRequestTypeDef = TypedDict(
    "ListReplaysRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "State": NotRequired[ReplayStateType],
        "EventSourceArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListReplaysResponseTypeDef = TypedDict(
    "ListReplaysResponseTypeDef",
    {
        "Replays": List["ReplayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleNamesByTargetRequestRequestTypeDef = TypedDict(
    "ListRuleNamesByTargetRequestRequestTypeDef",
    {
        "TargetArn": str,
        "EventBusName": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseTypeDef",
    {
        "RuleNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "EventBusName": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetsByRuleRequestRequestTypeDef = TypedDict(
    "ListTargetsByRuleRequestRequestTypeDef",
    {
        "Rule": str,
        "EventBusName": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTargetsByRuleResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": NotRequired["AwsVpcConfigurationTypeDef"],
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

PartnerEventSourceAccountTypeDef = TypedDict(
    "PartnerEventSourceAccountTypeDef",
    {
        "Account": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
        "State": NotRequired[EventSourceStateType],
    },
)

PartnerEventSourceTypeDef = TypedDict(
    "PartnerEventSourceTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": NotRequired[PlacementConstraintTypeType],
        "expression": NotRequired[str],
    },
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": NotRequired[PlacementStrategyTypeType],
        "field": NotRequired[str],
    },
)

PutEventsRequestEntryTypeDef = TypedDict(
    "PutEventsRequestEntryTypeDef",
    {
        "Time": NotRequired[Union[datetime, str]],
        "Source": NotRequired[str],
        "Resources": NotRequired[Sequence[str]],
        "DetailType": NotRequired[str],
        "Detail": NotRequired[str],
        "EventBusName": NotRequired[str],
        "TraceHeader": NotRequired[str],
    },
)

PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "Entries": Sequence["PutEventsRequestEntryTypeDef"],
    },
)

PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List["PutEventsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsResultEntryTypeDef = TypedDict(
    "PutEventsResultEntryTypeDef",
    {
        "EventId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

PutPartnerEventsRequestEntryTypeDef = TypedDict(
    "PutPartnerEventsRequestEntryTypeDef",
    {
        "Time": NotRequired[Union[datetime, str]],
        "Source": NotRequired[str],
        "Resources": NotRequired[Sequence[str]],
        "DetailType": NotRequired[str],
        "Detail": NotRequired[str],
    },
)

PutPartnerEventsRequestRequestTypeDef = TypedDict(
    "PutPartnerEventsRequestRequestTypeDef",
    {
        "Entries": Sequence["PutPartnerEventsRequestEntryTypeDef"],
    },
)

PutPartnerEventsResponseTypeDef = TypedDict(
    "PutPartnerEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List["PutPartnerEventsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPartnerEventsResultEntryTypeDef = TypedDict(
    "PutPartnerEventsResultEntryTypeDef",
    {
        "EventId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

PutPermissionRequestRequestTypeDef = TypedDict(
    "PutPermissionRequestRequestTypeDef",
    {
        "EventBusName": NotRequired[str],
        "Action": NotRequired[str],
        "Principal": NotRequired[str],
        "StatementId": NotRequired[str],
        "Condition": NotRequired["ConditionTypeDef"],
        "Policy": NotRequired[str],
    },
)

PutRuleRequestRequestTypeDef = TypedDict(
    "PutRuleRequestRequestTypeDef",
    {
        "Name": str,
        "ScheduleExpression": NotRequired[str],
        "EventPattern": NotRequired[str],
        "State": NotRequired[RuleStateType],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "EventBusName": NotRequired[str],
    },
)

PutRuleResponseTypeDef = TypedDict(
    "PutRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTargetsRequestRequestTypeDef = TypedDict(
    "PutTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Targets": Sequence["TargetTypeDef"],
        "EventBusName": NotRequired[str],
    },
)

PutTargetsResponseTypeDef = TypedDict(
    "PutTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List["PutTargetsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTargetsResultEntryTypeDef = TypedDict(
    "PutTargetsResultEntryTypeDef",
    {
        "TargetId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

RedshiftDataParametersTypeDef = TypedDict(
    "RedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sql": str,
        "SecretManagerArn": NotRequired[str],
        "DbUser": NotRequired[str],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
    },
)

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "StatementId": NotRequired[str],
        "RemoveAllPermissions": NotRequired[bool],
        "EventBusName": NotRequired[str],
    },
)

RemoveTargetsRequestRequestTypeDef = TypedDict(
    "RemoveTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Ids": Sequence[str],
        "EventBusName": NotRequired[str],
        "Force": NotRequired[bool],
    },
)

RemoveTargetsResponseTypeDef = TypedDict(
    "RemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List["RemoveTargetsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTargetsResultEntryTypeDef = TypedDict(
    "RemoveTargetsResultEntryTypeDef",
    {
        "TargetId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

ReplayDestinationTypeDef = TypedDict(
    "ReplayDestinationTypeDef",
    {
        "Arn": str,
        "FilterArns": NotRequired[List[str]],
    },
)

ReplayTypeDef = TypedDict(
    "ReplayTypeDef",
    {
        "ReplayName": NotRequired[str],
        "EventSourceArn": NotRequired[str],
        "State": NotRequired[ReplayStateType],
        "StateReason": NotRequired[str],
        "EventStartTime": NotRequired[datetime],
        "EventEndTime": NotRequired[datetime],
        "EventLastReplayedTime": NotRequired[datetime],
        "ReplayStartTime": NotRequired[datetime],
        "ReplayEndTime": NotRequired[datetime],
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

RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumRetryAttempts": NotRequired[int],
        "MaximumEventAgeInSeconds": NotRequired[int],
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "EventPattern": NotRequired[str],
        "State": NotRequired[RuleStateType],
        "Description": NotRequired[str],
        "ScheduleExpression": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ManagedBy": NotRequired[str],
        "EventBusName": NotRequired[str],
    },
)

RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef",
    {
        "RunCommandTargets": List["RunCommandTargetTypeDef"],
    },
)

RunCommandTargetTypeDef = TypedDict(
    "RunCommandTargetTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": NotRequired[List["SageMakerPipelineParameterTypeDef"]],
    },
)

SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": NotRequired[str],
    },
)

StartReplayRequestRequestTypeDef = TypedDict(
    "StartReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "EventStartTime": Union[datetime, str],
        "EventEndTime": Union[datetime, str],
        "Destination": "ReplayDestinationTypeDef",
        "Description": NotRequired[str],
    },
)

StartReplayResponseTypeDef = TypedDict(
    "StartReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ReplayStartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Id": str,
        "Arn": str,
        "RoleArn": NotRequired[str],
        "Input": NotRequired[str],
        "InputPath": NotRequired[str],
        "InputTransformer": NotRequired["InputTransformerTypeDef"],
        "KinesisParameters": NotRequired["KinesisParametersTypeDef"],
        "RunCommandParameters": NotRequired["RunCommandParametersTypeDef"],
        "EcsParameters": NotRequired["EcsParametersTypeDef"],
        "BatchParameters": NotRequired["BatchParametersTypeDef"],
        "SqsParameters": NotRequired["SqsParametersTypeDef"],
        "HttpParameters": NotRequired["HttpParametersTypeDef"],
        "RedshiftDataParameters": NotRequired["RedshiftDataParametersTypeDef"],
        "SageMakerPipelineParameters": NotRequired["SageMakerPipelineParametersTypeDef"],
        "DeadLetterConfig": NotRequired["DeadLetterConfigTypeDef"],
        "RetryPolicy": NotRequired["RetryPolicyTypeDef"],
    },
)

TestEventPatternRequestRequestTypeDef = TypedDict(
    "TestEventPatternRequestRequestTypeDef",
    {
        "EventPattern": str,
        "Event": str,
    },
)

TestEventPatternResponseTypeDef = TypedDict(
    "TestEventPatternResponseTypeDef",
    {
        "Result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApiDestinationRequestRequestTypeDef = TypedDict(
    "UpdateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "InvocationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ApiDestinationHttpMethodType],
        "InvocationRateLimitPerSecond": NotRequired[int],
    },
)

UpdateApiDestinationResponseTypeDef = TypedDict(
    "UpdateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateArchiveRequestRequestTypeDef = TypedDict(
    "UpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "Description": NotRequired[str],
        "EventPattern": NotRequired[str],
        "RetentionDays": NotRequired[int],
    },
)

UpdateArchiveResponseTypeDef = TypedDict(
    "UpdateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": NotRequired[str],
        "ApiKeyValue": NotRequired[str],
    },
)

UpdateConnectionAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": NotRequired["UpdateConnectionBasicAuthRequestParametersTypeDef"],
        "OAuthParameters": NotRequired["UpdateConnectionOAuthRequestParametersTypeDef"],
        "ApiKeyAuthParameters": NotRequired["UpdateConnectionApiKeyAuthRequestParametersTypeDef"],
        "InvocationHttpParameters": NotRequired["ConnectionHttpParametersTypeDef"],
    },
)

UpdateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
    },
)

UpdateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": NotRequired[str],
        "ClientSecret": NotRequired[str],
    },
)

UpdateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": NotRequired["UpdateConnectionOAuthClientRequestParametersTypeDef"],
        "AuthorizationEndpoint": NotRequired[str],
        "HttpMethod": NotRequired[ConnectionOAuthHttpMethodType],
        "OAuthHttpParameters": NotRequired["ConnectionHttpParametersTypeDef"],
    },
)

UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "AuthorizationType": NotRequired[ConnectionAuthorizationTypeType],
        "AuthParameters": NotRequired["UpdateConnectionAuthRequestParametersTypeDef"],
    },
)

UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
