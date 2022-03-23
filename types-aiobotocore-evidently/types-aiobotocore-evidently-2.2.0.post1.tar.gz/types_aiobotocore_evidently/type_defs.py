"""
Type annotations for evidently service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_evidently/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_evidently.type_defs import BatchEvaluateFeatureRequestRequestTypeDef

    data: BatchEvaluateFeatureRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ChangeDirectionEnumType,
    EventTypeType,
    ExperimentResultRequestTypeType,
    ExperimentResultResponseTypeType,
    ExperimentStatusType,
    ExperimentStopDesiredStateType,
    FeatureEvaluationStrategyType,
    FeatureStatusType,
    LaunchStatusType,
    LaunchStopDesiredStateType,
    ProjectStatusType,
    VariationValueTypeType,
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
    "BatchEvaluateFeatureRequestRequestTypeDef",
    "BatchEvaluateFeatureResponseTypeDef",
    "CloudWatchLogsDestinationConfigTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFeatureRequestRequestTypeDef",
    "CreateFeatureResponseTypeDef",
    "CreateLaunchRequestRequestTypeDef",
    "CreateLaunchResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteFeatureRequestRequestTypeDef",
    "DeleteLaunchRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "EvaluateFeatureRequestRequestTypeDef",
    "EvaluateFeatureResponseTypeDef",
    "EvaluationRequestTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationRuleTypeDef",
    "EventTypeDef",
    "ExperimentExecutionTypeDef",
    "ExperimentReportTypeDef",
    "ExperimentResultsDataTypeDef",
    "ExperimentScheduleTypeDef",
    "ExperimentTypeDef",
    "FeatureSummaryTypeDef",
    "FeatureTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetExperimentResponseTypeDef",
    "GetExperimentResultsRequestRequestTypeDef",
    "GetExperimentResultsResponseTypeDef",
    "GetFeatureRequestRequestTypeDef",
    "GetFeatureResponseTypeDef",
    "GetLaunchRequestRequestTypeDef",
    "GetLaunchResponseTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetProjectResponseTypeDef",
    "LaunchExecutionTypeDef",
    "LaunchGroupConfigTypeDef",
    "LaunchGroupTypeDef",
    "LaunchTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFeaturesRequestRequestTypeDef",
    "ListFeaturesResponseTypeDef",
    "ListLaunchesRequestRequestTypeDef",
    "ListLaunchesResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDefinitionConfigTypeDef",
    "MetricDefinitionTypeDef",
    "MetricGoalConfigTypeDef",
    "MetricGoalTypeDef",
    "MetricMonitorConfigTypeDef",
    "MetricMonitorTypeDef",
    "OnlineAbConfigTypeDef",
    "OnlineAbDefinitionTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDataDeliveryConfigTypeDef",
    "ProjectDataDeliveryTypeDef",
    "ProjectSummaryTypeDef",
    "ProjectTypeDef",
    "PutProjectEventsRequestRequestTypeDef",
    "PutProjectEventsResponseTypeDef",
    "PutProjectEventsResultEntryTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "ScheduledSplitConfigTypeDef",
    "ScheduledSplitTypeDef",
    "ScheduledSplitsLaunchConfigTypeDef",
    "ScheduledSplitsLaunchDefinitionTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "StartExperimentResponseTypeDef",
    "StartLaunchRequestRequestTypeDef",
    "StartLaunchResponseTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "StopExperimentResponseTypeDef",
    "StopLaunchRequestRequestTypeDef",
    "StopLaunchResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TreatmentConfigTypeDef",
    "TreatmentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateFeatureRequestRequestTypeDef",
    "UpdateFeatureResponseTypeDef",
    "UpdateLaunchRequestRequestTypeDef",
    "UpdateLaunchResponseTypeDef",
    "UpdateProjectDataDeliveryRequestRequestTypeDef",
    "UpdateProjectDataDeliveryResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "VariableValueTypeDef",
    "VariationConfigTypeDef",
    "VariationTypeDef",
)

BatchEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "BatchEvaluateFeatureRequestRequestTypeDef",
    {
        "project": str,
        "requests": Sequence["EvaluationRequestTypeDef"],
    },
)

BatchEvaluateFeatureResponseTypeDef = TypedDict(
    "BatchEvaluateFeatureResponseTypeDef",
    {
        "results": List["EvaluationResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsDestinationConfigTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigTypeDef",
    {
        "logGroup": NotRequired[str],
    },
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "logGroup": NotRequired[str],
    },
)

CreateExperimentRequestRequestTypeDef = TypedDict(
    "CreateExperimentRequestRequestTypeDef",
    {
        "metricGoals": Sequence["MetricGoalConfigTypeDef"],
        "name": str,
        "project": str,
        "treatments": Sequence["TreatmentConfigTypeDef"],
        "description": NotRequired[str],
        "onlineAbConfig": NotRequired["OnlineAbConfigTypeDef"],
        "randomizationSalt": NotRequired[str],
        "samplingRate": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFeatureRequestRequestTypeDef = TypedDict(
    "CreateFeatureRequestRequestTypeDef",
    {
        "name": str,
        "project": str,
        "variations": Sequence["VariationConfigTypeDef"],
        "defaultVariation": NotRequired[str],
        "description": NotRequired[str],
        "entityOverrides": NotRequired[Mapping[str, str]],
        "evaluationStrategy": NotRequired[FeatureEvaluationStrategyType],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFeatureResponseTypeDef = TypedDict(
    "CreateFeatureResponseTypeDef",
    {
        "feature": "FeatureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLaunchRequestRequestTypeDef = TypedDict(
    "CreateLaunchRequestRequestTypeDef",
    {
        "groups": Sequence["LaunchGroupConfigTypeDef"],
        "name": str,
        "project": str,
        "description": NotRequired[str],
        "metricMonitors": NotRequired[Sequence["MetricMonitorConfigTypeDef"]],
        "randomizationSalt": NotRequired[str],
        "scheduledSplitsConfig": NotRequired["ScheduledSplitsLaunchConfigTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateLaunchResponseTypeDef = TypedDict(
    "CreateLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "dataDelivery": NotRequired["ProjectDataDeliveryConfigTypeDef"],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)

DeleteFeatureRequestRequestTypeDef = TypedDict(
    "DeleteFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)

DeleteLaunchRequestRequestTypeDef = TypedDict(
    "DeleteLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)

EvaluateFeatureRequestRequestTypeDef = TypedDict(
    "EvaluateFeatureRequestRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
        "project": str,
        "evaluationContext": NotRequired[str],
    },
)

EvaluateFeatureResponseTypeDef = TypedDict(
    "EvaluateFeatureResponseTypeDef",
    {
        "details": str,
        "reason": str,
        "value": "VariableValueTypeDef",
        "variation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationRequestTypeDef = TypedDict(
    "EvaluationRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
        "evaluationContext": NotRequired[str],
    },
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "entityId": str,
        "feature": str,
        "details": NotRequired[str],
        "project": NotRequired[str],
        "reason": NotRequired[str],
        "value": NotRequired["VariableValueTypeDef"],
        "variation": NotRequired[str],
    },
)

EvaluationRuleTypeDef = TypedDict(
    "EvaluationRuleTypeDef",
    {
        "type": str,
        "name": NotRequired[str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "data": str,
        "timestamp": Union[datetime, str],
        "type": EventTypeType,
    },
)

ExperimentExecutionTypeDef = TypedDict(
    "ExperimentExecutionTypeDef",
    {
        "endedTime": NotRequired[datetime],
        "startedTime": NotRequired[datetime],
    },
)

ExperimentReportTypeDef = TypedDict(
    "ExperimentReportTypeDef",
    {
        "content": NotRequired[str],
        "metricName": NotRequired[str],
        "reportName": NotRequired[Literal["BayesianInference"]],
        "treatmentName": NotRequired[str],
    },
)

ExperimentResultsDataTypeDef = TypedDict(
    "ExperimentResultsDataTypeDef",
    {
        "metricName": NotRequired[str],
        "resultStat": NotRequired[ExperimentResultResponseTypeType],
        "treatmentName": NotRequired[str],
        "values": NotRequired[List[float]],
    },
)

ExperimentScheduleTypeDef = TypedDict(
    "ExperimentScheduleTypeDef",
    {
        "analysisCompleteTime": NotRequired[datetime],
    },
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ExperimentStatusType,
        "type": Literal["aws.evidently.onlineab"],
        "description": NotRequired[str],
        "execution": NotRequired["ExperimentExecutionTypeDef"],
        "metricGoals": NotRequired[List["MetricGoalTypeDef"]],
        "onlineAbDefinition": NotRequired["OnlineAbDefinitionTypeDef"],
        "project": NotRequired[str],
        "randomizationSalt": NotRequired[str],
        "samplingRate": NotRequired[int],
        "schedule": NotRequired["ExperimentScheduleTypeDef"],
        "statusReason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "treatments": NotRequired[List["TreatmentTypeDef"]],
    },
)

FeatureSummaryTypeDef = TypedDict(
    "FeatureSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
        "defaultVariation": NotRequired[str],
        "evaluationRules": NotRequired[List["EvaluationRuleTypeDef"]],
        "project": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

FeatureTypeDef = TypedDict(
    "FeatureTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
        "valueType": VariationValueTypeType,
        "variations": List["VariationTypeDef"],
        "defaultVariation": NotRequired[str],
        "description": NotRequired[str],
        "entityOverrides": NotRequired[Dict[str, str]],
        "evaluationRules": NotRequired[List["EvaluationRuleTypeDef"]],
        "project": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)

GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentResultsRequestRequestTypeDef = TypedDict(
    "GetExperimentResultsRequestRequestTypeDef",
    {
        "experiment": str,
        "metricNames": Sequence[str],
        "project": str,
        "treatmentNames": Sequence[str],
        "baseStat": NotRequired[Literal["Mean"]],
        "endTime": NotRequired[Union[datetime, str]],
        "period": NotRequired[int],
        "reportNames": NotRequired[Sequence[Literal["BayesianInference"]]],
        "resultStats": NotRequired[Sequence[ExperimentResultRequestTypeType]],
        "startTime": NotRequired[Union[datetime, str]],
    },
)

GetExperimentResultsResponseTypeDef = TypedDict(
    "GetExperimentResultsResponseTypeDef",
    {
        "reports": List["ExperimentReportTypeDef"],
        "resultsData": List["ExperimentResultsDataTypeDef"],
        "timestamps": List[datetime],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFeatureRequestRequestTypeDef = TypedDict(
    "GetFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)

GetFeatureResponseTypeDef = TypedDict(
    "GetFeatureResponseTypeDef",
    {
        "feature": "FeatureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchRequestRequestTypeDef = TypedDict(
    "GetLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

GetLaunchResponseTypeDef = TypedDict(
    "GetLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)

GetProjectResponseTypeDef = TypedDict(
    "GetProjectResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchExecutionTypeDef = TypedDict(
    "LaunchExecutionTypeDef",
    {
        "endedTime": NotRequired[datetime],
        "startedTime": NotRequired[datetime],
    },
)

LaunchGroupConfigTypeDef = TypedDict(
    "LaunchGroupConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
        "description": NotRequired[str],
    },
)

LaunchGroupTypeDef = TypedDict(
    "LaunchGroupTypeDef",
    {
        "featureVariations": Dict[str, str],
        "name": str,
        "description": NotRequired[str],
    },
)

LaunchTypeDef = TypedDict(
    "LaunchTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": LaunchStatusType,
        "type": Literal["aws.evidently.splits"],
        "description": NotRequired[str],
        "execution": NotRequired["LaunchExecutionTypeDef"],
        "groups": NotRequired[List["LaunchGroupTypeDef"]],
        "metricMonitors": NotRequired[List["MetricMonitorTypeDef"]],
        "project": NotRequired[str],
        "randomizationSalt": NotRequired[str],
        "scheduledSplitsDefinition": NotRequired["ScheduledSplitsLaunchDefinitionTypeDef"],
        "statusReason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "project": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[ExperimentStatusType],
    },
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List["ExperimentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFeaturesRequestRequestTypeDef = TypedDict(
    "ListFeaturesRequestRequestTypeDef",
    {
        "project": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFeaturesResponseTypeDef = TypedDict(
    "ListFeaturesResponseTypeDef",
    {
        "features": List["FeatureSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLaunchesRequestRequestTypeDef = TypedDict(
    "ListLaunchesRequestRequestTypeDef",
    {
        "project": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[LaunchStatusType],
    },
)

ListLaunchesResponseTypeDef = TypedDict(
    "ListLaunchesResponseTypeDef",
    {
        "launches": List["LaunchTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "nextToken": str,
        "projects": List["ProjectSummaryTypeDef"],
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

MetricDefinitionConfigTypeDef = TypedDict(
    "MetricDefinitionConfigTypeDef",
    {
        "entityIdKey": str,
        "name": str,
        "valueKey": str,
        "eventPattern": NotRequired[str],
        "unitLabel": NotRequired[str],
    },
)

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "entityIdKey": NotRequired[str],
        "eventPattern": NotRequired[str],
        "name": NotRequired[str],
        "unitLabel": NotRequired[str],
        "valueKey": NotRequired[str],
    },
)

MetricGoalConfigTypeDef = TypedDict(
    "MetricGoalConfigTypeDef",
    {
        "metricDefinition": "MetricDefinitionConfigTypeDef",
        "desiredChange": NotRequired[ChangeDirectionEnumType],
    },
)

MetricGoalTypeDef = TypedDict(
    "MetricGoalTypeDef",
    {
        "metricDefinition": "MetricDefinitionTypeDef",
        "desiredChange": NotRequired[ChangeDirectionEnumType],
    },
)

MetricMonitorConfigTypeDef = TypedDict(
    "MetricMonitorConfigTypeDef",
    {
        "metricDefinition": "MetricDefinitionConfigTypeDef",
    },
)

MetricMonitorTypeDef = TypedDict(
    "MetricMonitorTypeDef",
    {
        "metricDefinition": "MetricDefinitionTypeDef",
    },
)

OnlineAbConfigTypeDef = TypedDict(
    "OnlineAbConfigTypeDef",
    {
        "controlTreatmentName": NotRequired[str],
        "treatmentWeights": NotRequired[Mapping[str, int]],
    },
)

OnlineAbDefinitionTypeDef = TypedDict(
    "OnlineAbDefinitionTypeDef",
    {
        "controlTreatmentName": NotRequired[str],
        "treatmentWeights": NotRequired[Dict[str, int]],
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

ProjectDataDeliveryConfigTypeDef = TypedDict(
    "ProjectDataDeliveryConfigTypeDef",
    {
        "cloudWatchLogs": NotRequired["CloudWatchLogsDestinationConfigTypeDef"],
        "s3Destination": NotRequired["S3DestinationConfigTypeDef"],
    },
)

ProjectDataDeliveryTypeDef = TypedDict(
    "ProjectDataDeliveryTypeDef",
    {
        "cloudWatchLogs": NotRequired["CloudWatchLogsDestinationTypeDef"],
        "s3Destination": NotRequired["S3DestinationTypeDef"],
    },
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
        "activeExperimentCount": NotRequired[int],
        "activeLaunchCount": NotRequired[int],
        "description": NotRequired[str],
        "experimentCount": NotRequired[int],
        "featureCount": NotRequired[int],
        "launchCount": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
        "activeExperimentCount": NotRequired[int],
        "activeLaunchCount": NotRequired[int],
        "dataDelivery": NotRequired["ProjectDataDeliveryTypeDef"],
        "description": NotRequired[str],
        "experimentCount": NotRequired[int],
        "featureCount": NotRequired[int],
        "launchCount": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
    },
)

PutProjectEventsRequestRequestTypeDef = TypedDict(
    "PutProjectEventsRequestRequestTypeDef",
    {
        "events": Sequence["EventTypeDef"],
        "project": str,
    },
)

PutProjectEventsResponseTypeDef = TypedDict(
    "PutProjectEventsResponseTypeDef",
    {
        "eventResults": List["PutProjectEventsResultEntryTypeDef"],
        "failedEventCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutProjectEventsResultEntryTypeDef = TypedDict(
    "PutProjectEventsResultEntryTypeDef",
    {
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
        "eventId": NotRequired[str],
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
        "prefix": NotRequired[str],
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

ScheduledSplitConfigTypeDef = TypedDict(
    "ScheduledSplitConfigTypeDef",
    {
        "groupWeights": Mapping[str, int],
        "startTime": Union[datetime, str],
    },
)

ScheduledSplitTypeDef = TypedDict(
    "ScheduledSplitTypeDef",
    {
        "startTime": datetime,
        "groupWeights": NotRequired[Dict[str, int]],
    },
)

ScheduledSplitsLaunchConfigTypeDef = TypedDict(
    "ScheduledSplitsLaunchConfigTypeDef",
    {
        "steps": Sequence["ScheduledSplitConfigTypeDef"],
    },
)

ScheduledSplitsLaunchDefinitionTypeDef = TypedDict(
    "ScheduledSplitsLaunchDefinitionTypeDef",
    {
        "steps": NotRequired[List["ScheduledSplitTypeDef"]],
    },
)

StartExperimentRequestRequestTypeDef = TypedDict(
    "StartExperimentRequestRequestTypeDef",
    {
        "analysisCompleteTime": Union[datetime, str],
        "experiment": str,
        "project": str,
    },
)

StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "startedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartLaunchRequestRequestTypeDef = TypedDict(
    "StartLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)

StartLaunchResponseTypeDef = TypedDict(
    "StartLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExperimentRequestRequestTypeDef = TypedDict(
    "StopExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
        "desiredState": NotRequired[ExperimentStopDesiredStateType],
        "reason": NotRequired[str],
    },
)

StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopLaunchRequestRequestTypeDef = TypedDict(
    "StopLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
        "desiredState": NotRequired[LaunchStopDesiredStateType],
        "reason": NotRequired[str],
    },
)

StopLaunchResponseTypeDef = TypedDict(
    "StopLaunchResponseTypeDef",
    {
        "endedTime": datetime,
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

TreatmentConfigTypeDef = TypedDict(
    "TreatmentConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
        "description": NotRequired[str],
    },
)

TreatmentTypeDef = TypedDict(
    "TreatmentTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "featureVariations": NotRequired[Dict[str, str]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateExperimentRequestRequestTypeDef = TypedDict(
    "UpdateExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
        "description": NotRequired[str],
        "metricGoals": NotRequired[Sequence["MetricGoalConfigTypeDef"]],
        "onlineAbConfig": NotRequired["OnlineAbConfigTypeDef"],
        "randomizationSalt": NotRequired[str],
        "samplingRate": NotRequired[int],
        "treatments": NotRequired[Sequence["TreatmentConfigTypeDef"]],
    },
)

UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFeatureRequestRequestTypeDef = TypedDict(
    "UpdateFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
        "addOrUpdateVariations": NotRequired[Sequence["VariationConfigTypeDef"]],
        "defaultVariation": NotRequired[str],
        "description": NotRequired[str],
        "entityOverrides": NotRequired[Mapping[str, str]],
        "evaluationStrategy": NotRequired[FeatureEvaluationStrategyType],
        "removeVariations": NotRequired[Sequence[str]],
    },
)

UpdateFeatureResponseTypeDef = TypedDict(
    "UpdateFeatureResponseTypeDef",
    {
        "feature": "FeatureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLaunchRequestRequestTypeDef = TypedDict(
    "UpdateLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
        "description": NotRequired[str],
        "groups": NotRequired[Sequence["LaunchGroupConfigTypeDef"]],
        "metricMonitors": NotRequired[Sequence["MetricMonitorConfigTypeDef"]],
        "randomizationSalt": NotRequired[str],
        "scheduledSplitsConfig": NotRequired["ScheduledSplitsLaunchConfigTypeDef"],
    },
)

UpdateLaunchResponseTypeDef = TypedDict(
    "UpdateLaunchResponseTypeDef",
    {
        "launch": "LaunchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectDataDeliveryRequestRequestTypeDef = TypedDict(
    "UpdateProjectDataDeliveryRequestRequestTypeDef",
    {
        "project": str,
        "cloudWatchLogs": NotRequired["CloudWatchLogsDestinationConfigTypeDef"],
        "s3Destination": NotRequired["S3DestinationConfigTypeDef"],
    },
)

UpdateProjectDataDeliveryResponseTypeDef = TypedDict(
    "UpdateProjectDataDeliveryResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "project": str,
        "description": NotRequired[str],
    },
)

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "boolValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "longValue": NotRequired[int],
        "stringValue": NotRequired[str],
    },
)

VariationConfigTypeDef = TypedDict(
    "VariationConfigTypeDef",
    {
        "name": str,
        "value": "VariableValueTypeDef",
    },
)

VariationTypeDef = TypedDict(
    "VariationTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired["VariableValueTypeDef"],
    },
)
