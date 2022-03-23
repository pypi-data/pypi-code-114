"""
Type annotations for iotevents-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotevents_data.type_defs import AcknowledgeActionConfigurationTypeDef

    data: AcknowledgeActionConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AlarmStateNameType,
    ComparisonOperatorType,
    CustomerActionNameType,
    ErrorCodeType,
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
    "AcknowledgeActionConfigurationTypeDef",
    "AcknowledgeAlarmActionRequestTypeDef",
    "AlarmStateTypeDef",
    "AlarmSummaryTypeDef",
    "AlarmTypeDef",
    "BatchAcknowledgeAlarmRequestRequestTypeDef",
    "BatchAcknowledgeAlarmResponseTypeDef",
    "BatchAlarmActionErrorEntryTypeDef",
    "BatchDisableAlarmRequestRequestTypeDef",
    "BatchDisableAlarmResponseTypeDef",
    "BatchEnableAlarmRequestRequestTypeDef",
    "BatchEnableAlarmResponseTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchResetAlarmRequestRequestTypeDef",
    "BatchResetAlarmResponseTypeDef",
    "BatchSnoozeAlarmRequestRequestTypeDef",
    "BatchSnoozeAlarmResponseTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "BatchUpdateDetectorRequestRequestTypeDef",
    "BatchUpdateDetectorResponseTypeDef",
    "CustomerActionTypeDef",
    "DescribeAlarmRequestRequestTypeDef",
    "DescribeAlarmResponseTypeDef",
    "DescribeDetectorRequestRequestTypeDef",
    "DescribeDetectorResponseTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "DetectorStateTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorTypeDef",
    "DisableActionConfigurationTypeDef",
    "DisableAlarmActionRequestTypeDef",
    "EnableActionConfigurationTypeDef",
    "EnableAlarmActionRequestTypeDef",
    "ListAlarmsRequestRequestTypeDef",
    "ListAlarmsResponseTypeDef",
    "ListDetectorsRequestRequestTypeDef",
    "ListDetectorsResponseTypeDef",
    "MessageTypeDef",
    "ResetActionConfigurationTypeDef",
    "ResetAlarmActionRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleEvaluationTypeDef",
    "SimpleRuleEvaluationTypeDef",
    "SnoozeActionConfigurationTypeDef",
    "SnoozeAlarmActionRequestTypeDef",
    "StateChangeConfigurationTypeDef",
    "SystemEventTypeDef",
    "TimerDefinitionTypeDef",
    "TimerTypeDef",
    "TimestampValueTypeDef",
    "UpdateDetectorRequestTypeDef",
    "VariableDefinitionTypeDef",
    "VariableTypeDef",
)

AcknowledgeActionConfigurationTypeDef = TypedDict(
    "AcknowledgeActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)

AcknowledgeAlarmActionRequestTypeDef = TypedDict(
    "AcknowledgeAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)

AlarmStateTypeDef = TypedDict(
    "AlarmStateTypeDef",
    {
        "stateName": NotRequired[AlarmStateNameType],
        "ruleEvaluation": NotRequired["RuleEvaluationTypeDef"],
        "customerAction": NotRequired["CustomerActionTypeDef"],
        "systemEvent": NotRequired["SystemEventTypeDef"],
    },
)

AlarmSummaryTypeDef = TypedDict(
    "AlarmSummaryTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "keyValue": NotRequired[str],
        "stateName": NotRequired[AlarmStateNameType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "keyValue": NotRequired[str],
        "alarmState": NotRequired["AlarmStateTypeDef"],
        "severity": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

BatchAcknowledgeAlarmRequestRequestTypeDef = TypedDict(
    "BatchAcknowledgeAlarmRequestRequestTypeDef",
    {
        "acknowledgeActionRequests": Sequence["AcknowledgeAlarmActionRequestTypeDef"],
    },
)

BatchAcknowledgeAlarmResponseTypeDef = TypedDict(
    "BatchAcknowledgeAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchAlarmActionErrorEntryTypeDef = TypedDict(
    "BatchAlarmActionErrorEntryTypeDef",
    {
        "requestId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)

BatchDisableAlarmRequestRequestTypeDef = TypedDict(
    "BatchDisableAlarmRequestRequestTypeDef",
    {
        "disableActionRequests": Sequence["DisableAlarmActionRequestTypeDef"],
    },
)

BatchDisableAlarmResponseTypeDef = TypedDict(
    "BatchDisableAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEnableAlarmRequestRequestTypeDef = TypedDict(
    "BatchEnableAlarmRequestRequestTypeDef",
    {
        "enableActionRequests": Sequence["EnableAlarmActionRequestTypeDef"],
    },
)

BatchEnableAlarmResponseTypeDef = TypedDict(
    "BatchEnableAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)

BatchPutMessageRequestRequestTypeDef = TypedDict(
    "BatchPutMessageRequestRequestTypeDef",
    {
        "messages": Sequence["MessageTypeDef"],
    },
)

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchResetAlarmRequestRequestTypeDef = TypedDict(
    "BatchResetAlarmRequestRequestTypeDef",
    {
        "resetActionRequests": Sequence["ResetAlarmActionRequestTypeDef"],
    },
)

BatchResetAlarmResponseTypeDef = TypedDict(
    "BatchResetAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSnoozeAlarmRequestRequestTypeDef = TypedDict(
    "BatchSnoozeAlarmRequestRequestTypeDef",
    {
        "snoozeActionRequests": Sequence["SnoozeAlarmActionRequestTypeDef"],
    },
)

BatchSnoozeAlarmResponseTypeDef = TypedDict(
    "BatchSnoozeAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateDetectorErrorEntryTypeDef = TypedDict(
    "BatchUpdateDetectorErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)

BatchUpdateDetectorRequestRequestTypeDef = TypedDict(
    "BatchUpdateDetectorRequestRequestTypeDef",
    {
        "detectors": Sequence["UpdateDetectorRequestTypeDef"],
    },
)

BatchUpdateDetectorResponseTypeDef = TypedDict(
    "BatchUpdateDetectorResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List["BatchUpdateDetectorErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerActionTypeDef = TypedDict(
    "CustomerActionTypeDef",
    {
        "actionName": NotRequired[CustomerActionNameType],
        "snoozeActionConfiguration": NotRequired["SnoozeActionConfigurationTypeDef"],
        "enableActionConfiguration": NotRequired["EnableActionConfigurationTypeDef"],
        "disableActionConfiguration": NotRequired["DisableActionConfigurationTypeDef"],
        "acknowledgeActionConfiguration": NotRequired["AcknowledgeActionConfigurationTypeDef"],
        "resetActionConfiguration": NotRequired["ResetActionConfigurationTypeDef"],
    },
)

DescribeAlarmRequestRequestTypeDef = TypedDict(
    "DescribeAlarmRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "keyValue": NotRequired[str],
    },
)

DescribeAlarmResponseTypeDef = TypedDict(
    "DescribeAlarmResponseTypeDef",
    {
        "alarm": "AlarmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectorRequestRequestTypeDef = TypedDict(
    "DescribeDetectorRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "keyValue": NotRequired[str],
    },
)

DescribeDetectorResponseTypeDef = TypedDict(
    "DescribeDetectorResponseTypeDef",
    {
        "detector": "DetectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorStateDefinitionTypeDef = TypedDict(
    "DetectorStateDefinitionTypeDef",
    {
        "stateName": str,
        "variables": Sequence["VariableDefinitionTypeDef"],
        "timers": Sequence["TimerDefinitionTypeDef"],
    },
)

DetectorStateSummaryTypeDef = TypedDict(
    "DetectorStateSummaryTypeDef",
    {
        "stateName": NotRequired[str],
    },
)

DetectorStateTypeDef = TypedDict(
    "DetectorStateTypeDef",
    {
        "stateName": str,
        "variables": List["VariableTypeDef"],
        "timers": List["TimerTypeDef"],
    },
)

DetectorSummaryTypeDef = TypedDict(
    "DetectorSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "keyValue": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "state": NotRequired["DetectorStateSummaryTypeDef"],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "keyValue": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "state": NotRequired["DetectorStateTypeDef"],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

DisableActionConfigurationTypeDef = TypedDict(
    "DisableActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)

DisableAlarmActionRequestTypeDef = TypedDict(
    "DisableAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)

EnableActionConfigurationTypeDef = TypedDict(
    "EnableActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)

EnableAlarmActionRequestTypeDef = TypedDict(
    "EnableAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)

ListAlarmsRequestRequestTypeDef = TypedDict(
    "ListAlarmsRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAlarmsResponseTypeDef = TypedDict(
    "ListAlarmsResponseTypeDef",
    {
        "alarmSummaries": List["AlarmSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectorsRequestRequestTypeDef = TypedDict(
    "ListDetectorsRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "stateName": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {
        "detectorSummaries": List["DetectorSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "inputName": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
        "timestamp": NotRequired["TimestampValueTypeDef"],
    },
)

ResetActionConfigurationTypeDef = TypedDict(
    "ResetActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)

ResetAlarmActionRequestTypeDef = TypedDict(
    "ResetAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
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

RuleEvaluationTypeDef = TypedDict(
    "RuleEvaluationTypeDef",
    {
        "simpleRuleEvaluation": NotRequired["SimpleRuleEvaluationTypeDef"],
    },
)

SimpleRuleEvaluationTypeDef = TypedDict(
    "SimpleRuleEvaluationTypeDef",
    {
        "inputPropertyValue": NotRequired[str],
        "operator": NotRequired[ComparisonOperatorType],
        "thresholdValue": NotRequired[str],
    },
)

SnoozeActionConfigurationTypeDef = TypedDict(
    "SnoozeActionConfigurationTypeDef",
    {
        "snoozeDuration": NotRequired[int],
        "note": NotRequired[str],
    },
)

SnoozeAlarmActionRequestTypeDef = TypedDict(
    "SnoozeAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "snoozeDuration": int,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)

StateChangeConfigurationTypeDef = TypedDict(
    "StateChangeConfigurationTypeDef",
    {
        "triggerType": NotRequired[Literal["SNOOZE_TIMEOUT"]],
    },
)

SystemEventTypeDef = TypedDict(
    "SystemEventTypeDef",
    {
        "eventType": NotRequired[Literal["STATE_CHANGE"]],
        "stateChangeConfiguration": NotRequired["StateChangeConfigurationTypeDef"],
    },
)

TimerDefinitionTypeDef = TypedDict(
    "TimerDefinitionTypeDef",
    {
        "name": str,
        "seconds": int,
    },
)

TimerTypeDef = TypedDict(
    "TimerTypeDef",
    {
        "name": str,
        "timestamp": datetime,
    },
)

TimestampValueTypeDef = TypedDict(
    "TimestampValueTypeDef",
    {
        "timeInMillis": NotRequired[int],
    },
)

UpdateDetectorRequestTypeDef = TypedDict(
    "UpdateDetectorRequestTypeDef",
    {
        "messageId": str,
        "detectorModelName": str,
        "state": "DetectorStateDefinitionTypeDef",
        "keyValue": NotRequired[str],
    },
)

VariableDefinitionTypeDef = TypedDict(
    "VariableDefinitionTypeDef",
    {
        "name": str,
        "value": str,
    },
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "value": str,
    },
)
