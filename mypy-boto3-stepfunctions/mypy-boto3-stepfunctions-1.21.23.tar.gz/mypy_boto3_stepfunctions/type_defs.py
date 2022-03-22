"""
Type annotations for stepfunctions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ExecutionStatusType,
    HistoryEventTypeType,
    LogLevelType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "CreateActivityInputRequestTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineInputRequestTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DeleteActivityInputRequestTypeDef",
    "DeleteStateMachineInputRequestTypeDef",
    "DescribeActivityInputRequestTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineInputRequestTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputRequestTypeDef",
    "GetActivityTaskOutputTypeDef",
    "GetExecutionHistoryInputRequestTypeDef",
    "GetExecutionHistoryOutputTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "HistoryEventTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "ListActivitiesInputRequestTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListStateMachinesInputRequestTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SendTaskFailureInputRequestTypeDef",
    "SendTaskHeartbeatInputRequestTypeDef",
    "SendTaskSuccessInputRequestTypeDef",
    "StartExecutionInputRequestTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionInputRequestTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineListItemTypeDef",
    "StopExecutionInputRequestTypeDef",
    "StopExecutionOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "TracingConfigurationTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateStateMachineInputRequestTypeDef",
    "UpdateStateMachineOutputTypeDef",
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
    },
)

ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

ActivityScheduledEventDetailsTypeDef = TypedDict(
    "ActivityScheduledEventDetailsTypeDef",
    {
        "resource": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
        "timeoutInSeconds": NotRequired[int],
        "heartbeatInSeconds": NotRequired[int],
    },
)

ActivityStartedEventDetailsTypeDef = TypedDict(
    "ActivityStartedEventDetailsTypeDef",
    {
        "workerName": NotRequired[str],
    },
)

ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef",
    {
        "output": NotRequired[str],
        "outputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

BillingDetailsTypeDef = TypedDict(
    "BillingDetailsTypeDef",
    {
        "billedMemoryUsedInMB": NotRequired[int],
        "billedDurationInMilliseconds": NotRequired[int],
    },
)

CloudWatchEventsExecutionDataDetailsTypeDef = TypedDict(
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    {
        "included": NotRequired[bool],
    },
)

CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef",
    {
        "logGroupArn": NotRequired[str],
    },
)

CreateActivityInputRequestTypeDef = TypedDict(
    "CreateActivityInputRequestTypeDef",
    {
        "name": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateActivityOutputTypeDef = TypedDict(
    "CreateActivityOutputTypeDef",
    {
        "activityArn": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStateMachineInputRequestTypeDef = TypedDict(
    "CreateStateMachineInputRequestTypeDef",
    {
        "name": str,
        "definition": str,
        "roleArn": str,
        "type": NotRequired[StateMachineTypeType],
        "loggingConfiguration": NotRequired["LoggingConfigurationTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "tracingConfiguration": NotRequired["TracingConfigurationTypeDef"],
    },
)

CreateStateMachineOutputTypeDef = TypedDict(
    "CreateStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteActivityInputRequestTypeDef = TypedDict(
    "DeleteActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DeleteStateMachineInputRequestTypeDef = TypedDict(
    "DeleteStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

DescribeActivityInputRequestTypeDef = TypedDict(
    "DescribeActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)

DescribeActivityOutputTypeDef = TypedDict(
    "DescribeActivityOutputTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)

DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineForExecutionInputRequestTypeDef = TypedDict(
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    {
        "executionArn": str,
    },
)

DescribeStateMachineForExecutionOutputTypeDef = TypedDict(
    "DescribeStateMachineForExecutionOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineInputRequestTypeDef = TypedDict(
    "DescribeStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)

DescribeStateMachineOutputTypeDef = TypedDict(
    "DescribeStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": StateMachineStatusType,
        "definition": str,
        "roleArn": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

ExecutionListItemTypeDef = TypedDict(
    "ExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": NotRequired[datetime],
    },
)

ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": NotRequired[str],
        "inputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
        "roleArn": NotRequired[str],
    },
)

ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef",
    {
        "output": NotRequired[str],
        "outputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

GetActivityTaskInputRequestTypeDef = TypedDict(
    "GetActivityTaskInputRequestTypeDef",
    {
        "activityArn": str,
        "workerName": NotRequired[str],
    },
)

GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {
        "taskToken": str,
        "input": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExecutionHistoryInputRequestTypeDef = TypedDict(
    "GetExecutionHistoryInputRequestTypeDef",
    {
        "executionArn": str,
        "maxResults": NotRequired[int],
        "reverseOrder": NotRequired[bool],
        "nextToken": NotRequired[str],
        "includeExecutionData": NotRequired[bool],
    },
)

GetExecutionHistoryOutputTypeDef = TypedDict(
    "GetExecutionHistoryOutputTypeDef",
    {
        "events": List["HistoryEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HistoryEventExecutionDataDetailsTypeDef = TypedDict(
    "HistoryEventExecutionDataDetailsTypeDef",
    {
        "truncated": NotRequired[bool],
    },
)

HistoryEventTypeDef = TypedDict(
    "HistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": HistoryEventTypeType,
        "id": int,
        "previousEventId": NotRequired[int],
        "activityFailedEventDetails": NotRequired["ActivityFailedEventDetailsTypeDef"],
        "activityScheduleFailedEventDetails": NotRequired[
            "ActivityScheduleFailedEventDetailsTypeDef"
        ],
        "activityScheduledEventDetails": NotRequired["ActivityScheduledEventDetailsTypeDef"],
        "activityStartedEventDetails": NotRequired["ActivityStartedEventDetailsTypeDef"],
        "activitySucceededEventDetails": NotRequired["ActivitySucceededEventDetailsTypeDef"],
        "activityTimedOutEventDetails": NotRequired["ActivityTimedOutEventDetailsTypeDef"],
        "taskFailedEventDetails": NotRequired["TaskFailedEventDetailsTypeDef"],
        "taskScheduledEventDetails": NotRequired["TaskScheduledEventDetailsTypeDef"],
        "taskStartFailedEventDetails": NotRequired["TaskStartFailedEventDetailsTypeDef"],
        "taskStartedEventDetails": NotRequired["TaskStartedEventDetailsTypeDef"],
        "taskSubmitFailedEventDetails": NotRequired["TaskSubmitFailedEventDetailsTypeDef"],
        "taskSubmittedEventDetails": NotRequired["TaskSubmittedEventDetailsTypeDef"],
        "taskSucceededEventDetails": NotRequired["TaskSucceededEventDetailsTypeDef"],
        "taskTimedOutEventDetails": NotRequired["TaskTimedOutEventDetailsTypeDef"],
        "executionFailedEventDetails": NotRequired["ExecutionFailedEventDetailsTypeDef"],
        "executionStartedEventDetails": NotRequired["ExecutionStartedEventDetailsTypeDef"],
        "executionSucceededEventDetails": NotRequired["ExecutionSucceededEventDetailsTypeDef"],
        "executionAbortedEventDetails": NotRequired["ExecutionAbortedEventDetailsTypeDef"],
        "executionTimedOutEventDetails": NotRequired["ExecutionTimedOutEventDetailsTypeDef"],
        "mapStateStartedEventDetails": NotRequired["MapStateStartedEventDetailsTypeDef"],
        "mapIterationStartedEventDetails": NotRequired["MapIterationEventDetailsTypeDef"],
        "mapIterationSucceededEventDetails": NotRequired["MapIterationEventDetailsTypeDef"],
        "mapIterationFailedEventDetails": NotRequired["MapIterationEventDetailsTypeDef"],
        "mapIterationAbortedEventDetails": NotRequired["MapIterationEventDetailsTypeDef"],
        "lambdaFunctionFailedEventDetails": NotRequired["LambdaFunctionFailedEventDetailsTypeDef"],
        "lambdaFunctionScheduleFailedEventDetails": NotRequired[
            "LambdaFunctionScheduleFailedEventDetailsTypeDef"
        ],
        "lambdaFunctionScheduledEventDetails": NotRequired[
            "LambdaFunctionScheduledEventDetailsTypeDef"
        ],
        "lambdaFunctionStartFailedEventDetails": NotRequired[
            "LambdaFunctionStartFailedEventDetailsTypeDef"
        ],
        "lambdaFunctionSucceededEventDetails": NotRequired[
            "LambdaFunctionSucceededEventDetailsTypeDef"
        ],
        "lambdaFunctionTimedOutEventDetails": NotRequired[
            "LambdaFunctionTimedOutEventDetailsTypeDef"
        ],
        "stateEnteredEventDetails": NotRequired["StateEnteredEventDetailsTypeDef"],
        "stateExitedEventDetails": NotRequired["StateExitedEventDetailsTypeDef"],
    },
)

LambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

LambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduledEventDetailsTypeDef",
    {
        "resource": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
        "timeoutInSeconds": NotRequired[int],
    },
)

LambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef",
    {
        "output": NotRequired[str],
        "outputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

ListActivitiesInputRequestTypeDef = TypedDict(
    "ListActivitiesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListActivitiesOutputTypeDef = TypedDict(
    "ListActivitiesOutputTypeDef",
    {
        "activities": List["ActivityListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExecutionsInputRequestTypeDef = TypedDict(
    "ListExecutionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "statusFilter": NotRequired[ExecutionStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List["ExecutionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStateMachinesInputRequestTypeDef = TypedDict(
    "ListStateMachinesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListStateMachinesOutputTypeDef = TypedDict(
    "ListStateMachinesOutputTypeDef",
    {
        "stateMachines": List["StateMachineListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {
        "cloudWatchLogsLogGroup": NotRequired["CloudWatchLogsLogGroupTypeDef"],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "level": NotRequired[LogLevelType],
        "includeExecutionData": NotRequired[bool],
        "destinations": NotRequired[Sequence["LogDestinationTypeDef"]],
    },
)

MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef",
    {
        "name": NotRequired[str],
        "index": NotRequired[int],
    },
)

MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef",
    {
        "length": NotRequired[int],
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

SendTaskFailureInputRequestTypeDef = TypedDict(
    "SendTaskFailureInputRequestTypeDef",
    {
        "taskToken": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

SendTaskHeartbeatInputRequestTypeDef = TypedDict(
    "SendTaskHeartbeatInputRequestTypeDef",
    {
        "taskToken": str,
    },
)

SendTaskSuccessInputRequestTypeDef = TypedDict(
    "SendTaskSuccessInputRequestTypeDef",
    {
        "taskToken": str,
        "output": str,
    },
)

StartExecutionInputRequestTypeDef = TypedDict(
    "StartExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "name": NotRequired[str],
        "input": NotRequired[str],
        "traceHeader": NotRequired[str],
    },
)

StartExecutionOutputTypeDef = TypedDict(
    "StartExecutionOutputTypeDef",
    {
        "executionArn": str,
        "startDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSyncExecutionInputRequestTypeDef = TypedDict(
    "StartSyncExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "name": NotRequired[str],
        "input": NotRequired[str],
        "traceHeader": NotRequired[str],
    },
)

StartSyncExecutionOutputTypeDef = TypedDict(
    "StartSyncExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": SyncExecutionStatusType,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "billingDetails": "BillingDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StateEnteredEventDetailsTypeDef = TypedDict(
    "StateEnteredEventDetailsTypeDef",
    {
        "name": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

StateExitedEventDetailsTypeDef = TypedDict(
    "StateExitedEventDetailsTypeDef",
    {
        "name": str,
        "output": NotRequired[str],
        "outputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)

StopExecutionInputRequestTypeDef = TypedDict(
    "StopExecutionInputRequestTypeDef",
    {
        "executionArn": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

StopExecutionOutputTypeDef = TypedDict(
    "StopExecutionOutputTypeDef",
    {
        "stopDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TaskFailedEventDetailsTypeDef = TypedDict(
    "TaskFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

TaskScheduledEventDetailsTypeDef = TypedDict(
    "TaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": NotRequired[int],
        "heartbeatInSeconds": NotRequired[int],
    },
)

TaskStartFailedEventDetailsTypeDef = TypedDict(
    "TaskStartFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)

TaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "TaskSubmitFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

TaskSubmittedEventDetailsTypeDef = TypedDict(
    "TaskSubmittedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "output": NotRequired[str],
        "outputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

TaskSucceededEventDetailsTypeDef = TypedDict(
    "TaskSucceededEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "output": NotRequired[str],
        "outputDetails": NotRequired["HistoryEventExecutionDataDetailsTypeDef"],
    },
)

TaskTimedOutEventDetailsTypeDef = TypedDict(
    "TaskTimedOutEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)

TracingConfigurationTypeDef = TypedDict(
    "TracingConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateStateMachineInputRequestTypeDef = TypedDict(
    "UpdateStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "definition": NotRequired[str],
        "roleArn": NotRequired[str],
        "loggingConfiguration": NotRequired["LoggingConfigurationTypeDef"],
        "tracingConfiguration": NotRequired["TracingConfigurationTypeDef"],
    },
)

UpdateStateMachineOutputTypeDef = TypedDict(
    "UpdateStateMachineOutputTypeDef",
    {
        "updateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
