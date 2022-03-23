"""
Type annotations for iotevents service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_iotevents.type_defs import AcknowledgeFlowTypeDef

    data: AcknowledgeFlowTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AlarmModelVersionStatusType,
    AnalysisResultLevelType,
    AnalysisStatusType,
    ComparisonOperatorType,
    DetectorModelVersionStatusType,
    EvaluationMethodType,
    InputStatusType,
    LoggingLevelType,
    PayloadTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcknowledgeFlowTypeDef",
    "ActionTypeDef",
    "AlarmActionTypeDef",
    "AlarmCapabilitiesTypeDef",
    "AlarmEventActionsTypeDef",
    "AlarmModelSummaryTypeDef",
    "AlarmModelVersionSummaryTypeDef",
    "AlarmNotificationTypeDef",
    "AlarmRuleTypeDef",
    "AnalysisResultLocationTypeDef",
    "AnalysisResultTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetPropertyVariantTypeDef",
    "AttributeTypeDef",
    "ClearTimerActionTypeDef",
    "CreateAlarmModelRequestRequestTypeDef",
    "CreateAlarmModelResponseTypeDef",
    "CreateDetectorModelRequestRequestTypeDef",
    "CreateDetectorModelResponseTypeDef",
    "CreateInputRequestRequestTypeDef",
    "CreateInputResponseTypeDef",
    "DeleteAlarmModelRequestRequestTypeDef",
    "DeleteDetectorModelRequestRequestTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DescribeAlarmModelRequestRequestTypeDef",
    "DescribeAlarmModelResponseTypeDef",
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    "DescribeDetectorModelAnalysisResponseTypeDef",
    "DescribeDetectorModelRequestRequestTypeDef",
    "DescribeDetectorModelResponseTypeDef",
    "DescribeInputRequestRequestTypeDef",
    "DescribeInputResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DetectorDebugOptionTypeDef",
    "DetectorModelConfigurationTypeDef",
    "DetectorModelDefinitionTypeDef",
    "DetectorModelSummaryTypeDef",
    "DetectorModelTypeDef",
    "DetectorModelVersionSummaryTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "EmailConfigurationTypeDef",
    "EmailContentTypeDef",
    "EmailRecipientsTypeDef",
    "EventTypeDef",
    "FirehoseActionTypeDef",
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    "InitializationConfigurationTypeDef",
    "InputConfigurationTypeDef",
    "InputDefinitionTypeDef",
    "InputIdentifierTypeDef",
    "InputSummaryTypeDef",
    "InputTypeDef",
    "IotEventsActionTypeDef",
    "IotEventsInputIdentifierTypeDef",
    "IotSiteWiseActionTypeDef",
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    "IotSiteWiseInputIdentifierTypeDef",
    "IotTopicPublishActionTypeDef",
    "LambdaActionTypeDef",
    "ListAlarmModelVersionsRequestRequestTypeDef",
    "ListAlarmModelVersionsResponseTypeDef",
    "ListAlarmModelsRequestRequestTypeDef",
    "ListAlarmModelsResponseTypeDef",
    "ListDetectorModelVersionsRequestRequestTypeDef",
    "ListDetectorModelVersionsResponseTypeDef",
    "ListDetectorModelsRequestRequestTypeDef",
    "ListDetectorModelsResponseTypeDef",
    "ListInputRoutingsRequestRequestTypeDef",
    "ListInputRoutingsResponseTypeDef",
    "ListInputsRequestRequestTypeDef",
    "ListInputsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "NotificationActionTypeDef",
    "NotificationTargetActionsTypeDef",
    "OnEnterLifecycleTypeDef",
    "OnExitLifecycleTypeDef",
    "OnInputLifecycleTypeDef",
    "PayloadTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "RecipientDetailTypeDef",
    "ResetTimerActionTypeDef",
    "ResponseMetadataTypeDef",
    "RoutedResourceTypeDef",
    "SMSConfigurationTypeDef",
    "SNSTopicPublishActionTypeDef",
    "SSOIdentityTypeDef",
    "SetTimerActionTypeDef",
    "SetVariableActionTypeDef",
    "SimpleRuleTypeDef",
    "SqsActionTypeDef",
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    "StartDetectorModelAnalysisResponseTypeDef",
    "StateTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TransitionEventTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAlarmModelRequestRequestTypeDef",
    "UpdateAlarmModelResponseTypeDef",
    "UpdateDetectorModelRequestRequestTypeDef",
    "UpdateDetectorModelResponseTypeDef",
    "UpdateInputRequestRequestTypeDef",
    "UpdateInputResponseTypeDef",
)

AcknowledgeFlowTypeDef = TypedDict(
    "AcknowledgeFlowTypeDef",
    {
        "enabled": bool,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "setVariable": NotRequired["SetVariableActionTypeDef"],
        "sns": NotRequired["SNSTopicPublishActionTypeDef"],
        "iotTopicPublish": NotRequired["IotTopicPublishActionTypeDef"],
        "setTimer": NotRequired["SetTimerActionTypeDef"],
        "clearTimer": NotRequired["ClearTimerActionTypeDef"],
        "resetTimer": NotRequired["ResetTimerActionTypeDef"],
        "lambda": NotRequired["LambdaActionTypeDef"],
        "iotEvents": NotRequired["IotEventsActionTypeDef"],
        "sqs": NotRequired["SqsActionTypeDef"],
        "firehose": NotRequired["FirehoseActionTypeDef"],
        "dynamoDB": NotRequired["DynamoDBActionTypeDef"],
        "dynamoDBv2": NotRequired["DynamoDBv2ActionTypeDef"],
        "iotSiteWise": NotRequired["IotSiteWiseActionTypeDef"],
    },
)

AlarmActionTypeDef = TypedDict(
    "AlarmActionTypeDef",
    {
        "sns": NotRequired["SNSTopicPublishActionTypeDef"],
        "iotTopicPublish": NotRequired["IotTopicPublishActionTypeDef"],
        "lambda": NotRequired["LambdaActionTypeDef"],
        "iotEvents": NotRequired["IotEventsActionTypeDef"],
        "sqs": NotRequired["SqsActionTypeDef"],
        "firehose": NotRequired["FirehoseActionTypeDef"],
        "dynamoDB": NotRequired["DynamoDBActionTypeDef"],
        "dynamoDBv2": NotRequired["DynamoDBv2ActionTypeDef"],
        "iotSiteWise": NotRequired["IotSiteWiseActionTypeDef"],
    },
)

AlarmCapabilitiesTypeDef = TypedDict(
    "AlarmCapabilitiesTypeDef",
    {
        "initializationConfiguration": NotRequired["InitializationConfigurationTypeDef"],
        "acknowledgeFlow": NotRequired["AcknowledgeFlowTypeDef"],
    },
)

AlarmEventActionsTypeDef = TypedDict(
    "AlarmEventActionsTypeDef",
    {
        "alarmActions": NotRequired[Sequence["AlarmActionTypeDef"]],
    },
)

AlarmModelSummaryTypeDef = TypedDict(
    "AlarmModelSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "alarmModelDescription": NotRequired[str],
        "alarmModelName": NotRequired[str],
    },
)

AlarmModelVersionSummaryTypeDef = TypedDict(
    "AlarmModelVersionSummaryTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelArn": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[AlarmModelVersionStatusType],
        "statusMessage": NotRequired[str],
    },
)

AlarmNotificationTypeDef = TypedDict(
    "AlarmNotificationTypeDef",
    {
        "notificationActions": NotRequired[Sequence["NotificationActionTypeDef"]],
    },
)

AlarmRuleTypeDef = TypedDict(
    "AlarmRuleTypeDef",
    {
        "simpleRule": NotRequired["SimpleRuleTypeDef"],
    },
)

AnalysisResultLocationTypeDef = TypedDict(
    "AnalysisResultLocationTypeDef",
    {
        "path": NotRequired[str],
    },
)

AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "type": NotRequired[str],
        "level": NotRequired[AnalysisResultLevelType],
        "message": NotRequired[str],
        "locations": NotRequired[List["AnalysisResultLocationTypeDef"]],
    },
)

AssetPropertyTimestampTypeDef = TypedDict(
    "AssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
        "offsetInNanos": NotRequired[str],
    },
)

AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": NotRequired["AssetPropertyVariantTypeDef"],
        "timestamp": NotRequired["AssetPropertyTimestampTypeDef"],
        "quality": NotRequired[str],
    },
)

AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": NotRequired[str],
        "integerValue": NotRequired[str],
        "doubleValue": NotRequired[str],
        "booleanValue": NotRequired[str],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "jsonPath": str,
    },
)

ClearTimerActionTypeDef = TypedDict(
    "ClearTimerActionTypeDef",
    {
        "timerName": str,
    },
)

CreateAlarmModelRequestRequestTypeDef = TypedDict(
    "CreateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": "AlarmRuleTypeDef",
        "alarmModelDescription": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "key": NotRequired[str],
        "severity": NotRequired[int],
        "alarmNotification": NotRequired["AlarmNotificationTypeDef"],
        "alarmEventActions": NotRequired["AlarmEventActionsTypeDef"],
        "alarmCapabilities": NotRequired["AlarmCapabilitiesTypeDef"],
    },
)

CreateAlarmModelResponseTypeDef = TypedDict(
    "CreateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDetectorModelRequestRequestTypeDef = TypedDict(
    "CreateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
        "roleArn": str,
        "detectorModelDescription": NotRequired[str],
        "key": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)

CreateDetectorModelResponseTypeDef = TypedDict(
    "CreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": "DetectorModelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInputRequestRequestTypeDef = TypedDict(
    "CreateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": "InputDefinitionTypeDef",
        "inputDescription": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef",
    {
        "inputConfiguration": "InputConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlarmModelRequestRequestTypeDef = TypedDict(
    "DeleteAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
    },
)

DeleteDetectorModelRequestRequestTypeDef = TypedDict(
    "DeleteDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
    },
)

DeleteInputRequestRequestTypeDef = TypedDict(
    "DeleteInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)

DescribeAlarmModelRequestRequestTypeDef = TypedDict(
    "DescribeAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "alarmModelVersion": NotRequired[str],
    },
)

DescribeAlarmModelResponseTypeDef = TypedDict(
    "DescribeAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
        "alarmModelName": str,
        "alarmModelDescription": str,
        "roleArn": str,
        "key": str,
        "severity": int,
        "alarmRule": "AlarmRuleTypeDef",
        "alarmNotification": "AlarmNotificationTypeDef",
        "alarmEventActions": "AlarmEventActionsTypeDef",
        "alarmCapabilities": "AlarmCapabilitiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    {
        "analysisId": str,
    },
)

DescribeDetectorModelAnalysisResponseTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisResponseTypeDef",
    {
        "status": AnalysisStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectorModelRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": NotRequired[str],
    },
)

DescribeDetectorModelResponseTypeDef = TypedDict(
    "DescribeDetectorModelResponseTypeDef",
    {
        "detectorModel": "DetectorModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputRequestRequestTypeDef = TypedDict(
    "DescribeInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)

DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorDebugOptionTypeDef = TypedDict(
    "DetectorDebugOptionTypeDef",
    {
        "detectorModelName": str,
        "keyValue": NotRequired[str],
    },
)

DetectorModelConfigurationTypeDef = TypedDict(
    "DetectorModelConfigurationTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "detectorModelDescription": NotRequired[str],
        "detectorModelArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[DetectorModelVersionStatusType],
        "key": NotRequired[str],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)

DetectorModelDefinitionTypeDef = TypedDict(
    "DetectorModelDefinitionTypeDef",
    {
        "states": Sequence["StateTypeDef"],
        "initialStateName": str,
    },
)

DetectorModelSummaryTypeDef = TypedDict(
    "DetectorModelSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelDescription": NotRequired[str],
        "creationTime": NotRequired[datetime],
    },
)

DetectorModelTypeDef = TypedDict(
    "DetectorModelTypeDef",
    {
        "detectorModelDefinition": NotRequired["DetectorModelDefinitionTypeDef"],
        "detectorModelConfiguration": NotRequired["DetectorModelConfigurationTypeDef"],
    },
)

DetectorModelVersionSummaryTypeDef = TypedDict(
    "DetectorModelVersionSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "detectorModelArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[DetectorModelVersionStatusType],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)

DynamoDBActionTypeDef = TypedDict(
    "DynamoDBActionTypeDef",
    {
        "hashKeyField": str,
        "hashKeyValue": str,
        "tableName": str,
        "hashKeyType": NotRequired[str],
        "rangeKeyType": NotRequired[str],
        "rangeKeyField": NotRequired[str],
        "rangeKeyValue": NotRequired[str],
        "operation": NotRequired[str],
        "payloadField": NotRequired[str],
        "payload": NotRequired["PayloadTypeDef"],
    },
)

DynamoDBv2ActionTypeDef = TypedDict(
    "DynamoDBv2ActionTypeDef",
    {
        "tableName": str,
        "payload": NotRequired["PayloadTypeDef"],
    },
)

EmailConfigurationTypeDef = TypedDict(
    "EmailConfigurationTypeDef",
    {
        "from": str,
        "recipients": "EmailRecipientsTypeDef",
        "content": NotRequired["EmailContentTypeDef"],
    },
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "subject": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)

EmailRecipientsTypeDef = TypedDict(
    "EmailRecipientsTypeDef",
    {
        "to": NotRequired[Sequence["RecipientDetailTypeDef"]],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventName": str,
        "condition": NotRequired[str],
        "actions": NotRequired[Sequence["ActionTypeDef"]],
    },
)

FirehoseActionTypeDef = TypedDict(
    "FirehoseActionTypeDef",
    {
        "deliveryStreamName": str,
        "separator": NotRequired[str],
        "payload": NotRequired["PayloadTypeDef"],
    },
)

GetDetectorModelAnalysisResultsRequestRequestTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    {
        "analysisId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetDetectorModelAnalysisResultsResponseTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    {
        "analysisResults": List["AnalysisResultTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitializationConfigurationTypeDef = TypedDict(
    "InitializationConfigurationTypeDef",
    {
        "disabledOnInitialization": bool,
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "inputName": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
        "inputDescription": NotRequired[str],
    },
)

InputDefinitionTypeDef = TypedDict(
    "InputDefinitionTypeDef",
    {
        "attributes": Sequence["AttributeTypeDef"],
    },
)

InputIdentifierTypeDef = TypedDict(
    "InputIdentifierTypeDef",
    {
        "iotEventsInputIdentifier": NotRequired["IotEventsInputIdentifierTypeDef"],
        "iotSiteWiseInputIdentifier": NotRequired["IotSiteWiseInputIdentifierTypeDef"],
    },
)

InputSummaryTypeDef = TypedDict(
    "InputSummaryTypeDef",
    {
        "inputName": NotRequired[str],
        "inputDescription": NotRequired[str],
        "inputArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[InputStatusType],
    },
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "inputConfiguration": NotRequired["InputConfigurationTypeDef"],
        "inputDefinition": NotRequired["InputDefinitionTypeDef"],
    },
)

IotEventsActionTypeDef = TypedDict(
    "IotEventsActionTypeDef",
    {
        "inputName": str,
        "payload": NotRequired["PayloadTypeDef"],
    },
)

IotEventsInputIdentifierTypeDef = TypedDict(
    "IotEventsInputIdentifierTypeDef",
    {
        "inputName": str,
    },
)

IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "entryId": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "propertyValue": NotRequired["AssetPropertyValueTypeDef"],
    },
)

IotSiteWiseAssetModelPropertyIdentifierTypeDef = TypedDict(
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    {
        "assetModelId": str,
        "propertyId": str,
    },
)

IotSiteWiseInputIdentifierTypeDef = TypedDict(
    "IotSiteWiseInputIdentifierTypeDef",
    {
        "iotSiteWiseAssetModelPropertyIdentifier": NotRequired[
            "IotSiteWiseAssetModelPropertyIdentifierTypeDef"
        ],
    },
)

IotTopicPublishActionTypeDef = TypedDict(
    "IotTopicPublishActionTypeDef",
    {
        "mqttTopic": str,
        "payload": NotRequired["PayloadTypeDef"],
    },
)

LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "functionArn": str,
        "payload": NotRequired["PayloadTypeDef"],
    },
)

ListAlarmModelVersionsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelVersionsRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAlarmModelVersionsResponseTypeDef = TypedDict(
    "ListAlarmModelVersionsResponseTypeDef",
    {
        "alarmModelVersionSummaries": List["AlarmModelVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlarmModelsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAlarmModelsResponseTypeDef = TypedDict(
    "ListAlarmModelsResponseTypeDef",
    {
        "alarmModelSummaries": List["AlarmModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectorModelVersionsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelVersionsRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDetectorModelVersionsResponseTypeDef = TypedDict(
    "ListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List["DetectorModelVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectorModelsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDetectorModelsResponseTypeDef = TypedDict(
    "ListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List["DetectorModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputRoutingsRequestRequestTypeDef = TypedDict(
    "ListInputRoutingsRequestRequestTypeDef",
    {
        "inputIdentifier": "InputIdentifierTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListInputRoutingsResponseTypeDef = TypedDict(
    "ListInputRoutingsResponseTypeDef",
    {
        "routedResources": List["RoutedResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputsRequestRequestTypeDef = TypedDict(
    "ListInputsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef",
    {
        "inputSummaries": List["InputSummaryTypeDef"],
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

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
        "detectorDebugOptions": NotRequired[List["DetectorDebugOptionTypeDef"]],
    },
)

NotificationActionTypeDef = TypedDict(
    "NotificationActionTypeDef",
    {
        "action": "NotificationTargetActionsTypeDef",
        "smsConfigurations": NotRequired[Sequence["SMSConfigurationTypeDef"]],
        "emailConfigurations": NotRequired[Sequence["EmailConfigurationTypeDef"]],
    },
)

NotificationTargetActionsTypeDef = TypedDict(
    "NotificationTargetActionsTypeDef",
    {
        "lambdaAction": NotRequired["LambdaActionTypeDef"],
    },
)

OnEnterLifecycleTypeDef = TypedDict(
    "OnEnterLifecycleTypeDef",
    {
        "events": NotRequired[Sequence["EventTypeDef"]],
    },
)

OnExitLifecycleTypeDef = TypedDict(
    "OnExitLifecycleTypeDef",
    {
        "events": NotRequired[Sequence["EventTypeDef"]],
    },
)

OnInputLifecycleTypeDef = TypedDict(
    "OnInputLifecycleTypeDef",
    {
        "events": NotRequired[Sequence["EventTypeDef"]],
        "transitionEvents": NotRequired[Sequence["TransitionEventTypeDef"]],
    },
)

PayloadTypeDef = TypedDict(
    "PayloadTypeDef",
    {
        "contentExpression": str,
        "type": PayloadTypeType,
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

RecipientDetailTypeDef = TypedDict(
    "RecipientDetailTypeDef",
    {
        "ssoIdentity": NotRequired["SSOIdentityTypeDef"],
    },
)

ResetTimerActionTypeDef = TypedDict(
    "ResetTimerActionTypeDef",
    {
        "timerName": str,
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

RoutedResourceTypeDef = TypedDict(
    "RoutedResourceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)

SMSConfigurationTypeDef = TypedDict(
    "SMSConfigurationTypeDef",
    {
        "recipients": Sequence["RecipientDetailTypeDef"],
        "senderId": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)

SNSTopicPublishActionTypeDef = TypedDict(
    "SNSTopicPublishActionTypeDef",
    {
        "targetArn": str,
        "payload": NotRequired["PayloadTypeDef"],
    },
)

SSOIdentityTypeDef = TypedDict(
    "SSOIdentityTypeDef",
    {
        "identityStoreId": str,
        "userId": NotRequired[str],
    },
)

SetTimerActionTypeDef = TypedDict(
    "SetTimerActionTypeDef",
    {
        "timerName": str,
        "seconds": NotRequired[int],
        "durationExpression": NotRequired[str],
    },
)

SetVariableActionTypeDef = TypedDict(
    "SetVariableActionTypeDef",
    {
        "variableName": str,
        "value": str,
    },
)

SimpleRuleTypeDef = TypedDict(
    "SimpleRuleTypeDef",
    {
        "inputProperty": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": str,
    },
)

SqsActionTypeDef = TypedDict(
    "SqsActionTypeDef",
    {
        "queueUrl": str,
        "useBase64": NotRequired[bool],
        "payload": NotRequired["PayloadTypeDef"],
    },
)

StartDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    {
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
    },
)

StartDetectorModelAnalysisResponseTypeDef = TypedDict(
    "StartDetectorModelAnalysisResponseTypeDef",
    {
        "analysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StateTypeDef = TypedDict(
    "StateTypeDef",
    {
        "stateName": str,
        "onInput": NotRequired["OnInputLifecycleTypeDef"],
        "onEnter": NotRequired["OnEnterLifecycleTypeDef"],
        "onExit": NotRequired["OnExitLifecycleTypeDef"],
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
        "key": str,
        "value": str,
    },
)

TransitionEventTypeDef = TypedDict(
    "TransitionEventTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
        "actions": NotRequired[Sequence["ActionTypeDef"]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAlarmModelRequestRequestTypeDef = TypedDict(
    "UpdateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": "AlarmRuleTypeDef",
        "alarmModelDescription": NotRequired[str],
        "severity": NotRequired[int],
        "alarmNotification": NotRequired["AlarmNotificationTypeDef"],
        "alarmEventActions": NotRequired["AlarmEventActionsTypeDef"],
        "alarmCapabilities": NotRequired["AlarmCapabilitiesTypeDef"],
    },
)

UpdateAlarmModelResponseTypeDef = TypedDict(
    "UpdateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDetectorModelRequestRequestTypeDef = TypedDict(
    "UpdateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
        "roleArn": str,
        "detectorModelDescription": NotRequired[str],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)

UpdateDetectorModelResponseTypeDef = TypedDict(
    "UpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": "DetectorModelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInputRequestRequestTypeDef = TypedDict(
    "UpdateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": "InputDefinitionTypeDef",
        "inputDescription": NotRequired[str],
    },
)

UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef",
    {
        "inputConfiguration": "InputConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
