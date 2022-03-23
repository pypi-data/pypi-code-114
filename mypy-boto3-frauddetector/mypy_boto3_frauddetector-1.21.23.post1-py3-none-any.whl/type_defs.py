"""
Type annotations for frauddetector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_frauddetector.type_defs import BatchCreateVariableErrorTypeDef

    data: BatchCreateVariableErrorTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AsyncJobStatusType,
    DataSourceType,
    DataTypeType,
    DetectorVersionStatusType,
    EventIngestionType,
    ModelEndpointStatusType,
    ModelInputDataFormatType,
    ModelOutputDataFormatType,
    ModelTypeEnumType,
    ModelVersionStatusType,
    RuleExecutionModeType,
    TrainingDataSourceEnumType,
    UnlabeledEventsTreatmentType,
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
    "BatchCreateVariableErrorTypeDef",
    "BatchCreateVariableRequestRequestTypeDef",
    "BatchCreateVariableResultTypeDef",
    "BatchGetVariableErrorTypeDef",
    "BatchGetVariableRequestRequestTypeDef",
    "BatchGetVariableResultTypeDef",
    "BatchImportTypeDef",
    "BatchPredictionTypeDef",
    "CancelBatchImportJobRequestRequestTypeDef",
    "CancelBatchPredictionJobRequestRequestTypeDef",
    "CreateBatchImportJobRequestRequestTypeDef",
    "CreateBatchPredictionJobRequestRequestTypeDef",
    "CreateDetectorVersionRequestRequestTypeDef",
    "CreateDetectorVersionResultTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelVersionRequestRequestTypeDef",
    "CreateModelVersionResultTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResultTypeDef",
    "CreateVariableRequestRequestTypeDef",
    "DataValidationMetricsTypeDef",
    "DeleteBatchImportJobRequestRequestTypeDef",
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteDetectorVersionRequestRequestTypeDef",
    "DeleteEntityTypeRequestRequestTypeDef",
    "DeleteEventRequestRequestTypeDef",
    "DeleteEventTypeRequestRequestTypeDef",
    "DeleteEventsByEventTypeRequestRequestTypeDef",
    "DeleteEventsByEventTypeResultTypeDef",
    "DeleteExternalModelRequestRequestTypeDef",
    "DeleteLabelRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteModelVersionRequestRequestTypeDef",
    "DeleteOutcomeRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteVariableRequestRequestTypeDef",
    "DescribeDetectorRequestRequestTypeDef",
    "DescribeDetectorResultTypeDef",
    "DescribeModelVersionsRequestRequestTypeDef",
    "DescribeModelVersionsResultTypeDef",
    "DetectorTypeDef",
    "DetectorVersionSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypeTypeDef",
    "EvaluatedExternalModelTypeDef",
    "EvaluatedModelVersionTypeDef",
    "EvaluatedRuleTypeDef",
    "EventPredictionSummaryTypeDef",
    "EventTypeDef",
    "EventTypeTypeDef",
    "EventVariableSummaryTypeDef",
    "ExternalEventsDetailTypeDef",
    "ExternalModelOutputsTypeDef",
    "ExternalModelSummaryTypeDef",
    "ExternalModelTypeDef",
    "FieldValidationMessageTypeDef",
    "FileValidationMessageTypeDef",
    "FilterConditionTypeDef",
    "GetBatchImportJobsRequestRequestTypeDef",
    "GetBatchImportJobsResultTypeDef",
    "GetBatchPredictionJobsRequestRequestTypeDef",
    "GetBatchPredictionJobsResultTypeDef",
    "GetDeleteEventsByEventTypeStatusRequestRequestTypeDef",
    "GetDeleteEventsByEventTypeStatusResultTypeDef",
    "GetDetectorVersionRequestRequestTypeDef",
    "GetDetectorVersionResultTypeDef",
    "GetDetectorsRequestRequestTypeDef",
    "GetDetectorsResultTypeDef",
    "GetEntityTypesRequestRequestTypeDef",
    "GetEntityTypesResultTypeDef",
    "GetEventPredictionMetadataRequestRequestTypeDef",
    "GetEventPredictionMetadataResultTypeDef",
    "GetEventPredictionRequestRequestTypeDef",
    "GetEventPredictionResultTypeDef",
    "GetEventRequestRequestTypeDef",
    "GetEventResultTypeDef",
    "GetEventTypesRequestRequestTypeDef",
    "GetEventTypesResultTypeDef",
    "GetExternalModelsRequestRequestTypeDef",
    "GetExternalModelsResultTypeDef",
    "GetKMSEncryptionKeyResultTypeDef",
    "GetLabelsRequestRequestTypeDef",
    "GetLabelsResultTypeDef",
    "GetModelVersionRequestRequestTypeDef",
    "GetModelVersionResultTypeDef",
    "GetModelsRequestRequestTypeDef",
    "GetModelsResultTypeDef",
    "GetOutcomesRequestRequestTypeDef",
    "GetOutcomesResultTypeDef",
    "GetRulesRequestRequestTypeDef",
    "GetRulesResultTypeDef",
    "GetVariablesRequestRequestTypeDef",
    "GetVariablesResultTypeDef",
    "IngestedEventStatisticsTypeDef",
    "IngestedEventsDetailTypeDef",
    "IngestedEventsTimeWindowTypeDef",
    "KMSKeyTypeDef",
    "LabelSchemaTypeDef",
    "LabelTypeDef",
    "ListEventPredictionsRequestRequestTypeDef",
    "ListEventPredictionsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogOddsMetricTypeDef",
    "MetricDataPointTypeDef",
    "ModelEndpointDataBlobTypeDef",
    "ModelInputConfigurationTypeDef",
    "ModelOutputConfigurationTypeDef",
    "ModelScoresTypeDef",
    "ModelTypeDef",
    "ModelVersionDetailTypeDef",
    "ModelVersionEvaluationTypeDef",
    "ModelVersionTypeDef",
    "OutcomeTypeDef",
    "PredictionExplanationsTypeDef",
    "PredictionTimeRangeTypeDef",
    "PutDetectorRequestRequestTypeDef",
    "PutEntityTypeRequestRequestTypeDef",
    "PutEventTypeRequestRequestTypeDef",
    "PutExternalModelRequestRequestTypeDef",
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    "PutLabelRequestRequestTypeDef",
    "PutOutcomeRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleDetailTypeDef",
    "RuleResultTypeDef",
    "RuleTypeDef",
    "SendEventRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrainingDataSchemaTypeDef",
    "TrainingMetricsTypeDef",
    "TrainingResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    "UpdateDetectorVersionRequestRequestTypeDef",
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    "UpdateEventLabelRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateModelVersionRequestRequestTypeDef",
    "UpdateModelVersionResultTypeDef",
    "UpdateModelVersionStatusRequestRequestTypeDef",
    "UpdateRuleMetadataRequestRequestTypeDef",
    "UpdateRuleVersionRequestRequestTypeDef",
    "UpdateRuleVersionResultTypeDef",
    "UpdateVariableRequestRequestTypeDef",
    "VariableEntryTypeDef",
    "VariableImpactExplanationTypeDef",
    "VariableImportanceMetricsTypeDef",
    "VariableTypeDef",
)

BatchCreateVariableErrorTypeDef = TypedDict(
    "BatchCreateVariableErrorTypeDef",
    {
        "name": NotRequired[str],
        "code": NotRequired[int],
        "message": NotRequired[str],
    },
)

BatchCreateVariableRequestRequestTypeDef = TypedDict(
    "BatchCreateVariableRequestRequestTypeDef",
    {
        "variableEntries": Sequence["VariableEntryTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

BatchCreateVariableResultTypeDef = TypedDict(
    "BatchCreateVariableResultTypeDef",
    {
        "errors": List["BatchCreateVariableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetVariableErrorTypeDef = TypedDict(
    "BatchGetVariableErrorTypeDef",
    {
        "name": NotRequired[str],
        "code": NotRequired[int],
        "message": NotRequired[str],
    },
)

BatchGetVariableRequestRequestTypeDef = TypedDict(
    "BatchGetVariableRequestRequestTypeDef",
    {
        "names": Sequence[str],
    },
)

BatchGetVariableResultTypeDef = TypedDict(
    "BatchGetVariableResultTypeDef",
    {
        "variables": List["VariableTypeDef"],
        "errors": List["BatchGetVariableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchImportTypeDef = TypedDict(
    "BatchImportTypeDef",
    {
        "jobId": NotRequired[str],
        "status": NotRequired[AsyncJobStatusType],
        "failureReason": NotRequired[str],
        "startTime": NotRequired[str],
        "completionTime": NotRequired[str],
        "inputPath": NotRequired[str],
        "outputPath": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "iamRoleArn": NotRequired[str],
        "arn": NotRequired[str],
        "processedRecordsCount": NotRequired[int],
        "failedRecordsCount": NotRequired[int],
        "totalRecordsCount": NotRequired[int],
    },
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "jobId": NotRequired[str],
        "status": NotRequired[AsyncJobStatusType],
        "failureReason": NotRequired[str],
        "startTime": NotRequired[str],
        "completionTime": NotRequired[str],
        "lastHeartbeatTime": NotRequired[str],
        "inputPath": NotRequired[str],
        "outputPath": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "detectorName": NotRequired[str],
        "detectorVersion": NotRequired[str],
        "iamRoleArn": NotRequired[str],
        "arn": NotRequired[str],
        "processedRecordsCount": NotRequired[int],
        "totalRecordsCount": NotRequired[int],
    },
)

CancelBatchImportJobRequestRequestTypeDef = TypedDict(
    "CancelBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

CancelBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "CancelBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

CreateBatchImportJobRequestRequestTypeDef = TypedDict(
    "CreateBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "iamRoleArn": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "CreateBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "iamRoleArn": str,
        "detectorVersion": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDetectorVersionRequestRequestTypeDef = TypedDict(
    "CreateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "rules": Sequence["RuleTypeDef"],
        "description": NotRequired[str],
        "externalModelEndpoints": NotRequired[Sequence[str]],
        "modelVersions": NotRequired[Sequence["ModelVersionTypeDef"]],
        "ruleExecutionMode": NotRequired[RuleExecutionModeType],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDetectorVersionResultTypeDef = TypedDict(
    "CreateDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelRequestRequestTypeDef = TypedDict(
    "CreateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "eventTypeName": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelVersionRequestRequestTypeDef = TypedDict(
    "CreateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
        "externalEventsDetail": NotRequired["ExternalEventsDetailTypeDef"],
        "ingestedEventsDetail": NotRequired["IngestedEventsDetailTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelVersionResultTypeDef = TypedDict(
    "CreateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "ruleId": str,
        "detectorId": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": Sequence[str],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRuleResultTypeDef = TypedDict(
    "CreateRuleResultTypeDef",
    {
        "rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVariableRequestRequestTypeDef = TypedDict(
    "CreateVariableRequestRequestTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
        "description": NotRequired[str],
        "variableType": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

DataValidationMetricsTypeDef = TypedDict(
    "DataValidationMetricsTypeDef",
    {
        "fileLevelMessages": NotRequired[List["FileValidationMessageTypeDef"]],
        "fieldLevelMessages": NotRequired[List["FieldValidationMessageTypeDef"]],
    },
)

DeleteBatchImportJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DeleteBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)

DeleteDetectorVersionRequestRequestTypeDef = TypedDict(
    "DeleteDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

DeleteEntityTypeRequestRequestTypeDef = TypedDict(
    "DeleteEntityTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEventRequestRequestTypeDef = TypedDict(
    "DeleteEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "deleteAuditHistory": NotRequired[bool],
    },
)

DeleteEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEventsByEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventsByEventTypeRequestRequestTypeDef",
    {
        "eventTypeName": str,
    },
)

DeleteEventsByEventTypeResultTypeDef = TypedDict(
    "DeleteEventsByEventTypeResultTypeDef",
    {
        "eventTypeName": str,
        "eventsDeletionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExternalModelRequestRequestTypeDef = TypedDict(
    "DeleteExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
    },
)

DeleteLabelRequestRequestTypeDef = TypedDict(
    "DeleteLabelRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
    },
)

DeleteModelVersionRequestRequestTypeDef = TypedDict(
    "DeleteModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)

DeleteOutcomeRequestRequestTypeDef = TypedDict(
    "DeleteOutcomeRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "rule": "RuleTypeDef",
    },
)

DeleteVariableRequestRequestTypeDef = TypedDict(
    "DeleteVariableRequestRequestTypeDef",
    {
        "name": str,
    },
)

DescribeDetectorRequestRequestTypeDef = TypedDict(
    "DescribeDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeDetectorResultTypeDef = TypedDict(
    "DescribeDetectorResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionSummaries": List["DetectorVersionSummaryTypeDef"],
        "nextToken": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelVersionsRequestRequestTypeDef = TypedDict(
    "DescribeModelVersionsRequestRequestTypeDef",
    {
        "modelId": NotRequired[str],
        "modelVersionNumber": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeModelVersionsResultTypeDef = TypedDict(
    "DescribeModelVersionsResultTypeDef",
    {
        "modelVersionDetails": List["ModelVersionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorId": NotRequired[str],
        "description": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

DetectorVersionSummaryTypeDef = TypedDict(
    "DetectorVersionSummaryTypeDef",
    {
        "detectorVersionId": NotRequired[str],
        "status": NotRequired[DetectorVersionStatusType],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "entityType": str,
        "entityId": str,
    },
)

EntityTypeTypeDef = TypedDict(
    "EntityTypeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

EvaluatedExternalModelTypeDef = TypedDict(
    "EvaluatedExternalModelTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "useEventVariables": NotRequired[bool],
        "inputVariables": NotRequired[Dict[str, str]],
        "outputVariables": NotRequired[Dict[str, str]],
    },
)

EvaluatedModelVersionTypeDef = TypedDict(
    "EvaluatedModelVersionTypeDef",
    {
        "modelId": NotRequired[str],
        "modelVersion": NotRequired[str],
        "modelType": NotRequired[str],
        "evaluations": NotRequired[List["ModelVersionEvaluationTypeDef"]],
    },
)

EvaluatedRuleTypeDef = TypedDict(
    "EvaluatedRuleTypeDef",
    {
        "ruleId": NotRequired[str],
        "ruleVersion": NotRequired[str],
        "expression": NotRequired[str],
        "expressionWithValues": NotRequired[str],
        "outcomes": NotRequired[List[str]],
        "evaluated": NotRequired[bool],
        "matched": NotRequired[bool],
    },
)

EventPredictionSummaryTypeDef = TypedDict(
    "EventPredictionSummaryTypeDef",
    {
        "eventId": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "eventTimestamp": NotRequired[str],
        "predictionTimestamp": NotRequired[str],
        "detectorId": NotRequired[str],
        "detectorVersionId": NotRequired[str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventId": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "eventTimestamp": NotRequired[str],
        "eventVariables": NotRequired[Dict[str, str]],
        "currentLabel": NotRequired[str],
        "labelTimestamp": NotRequired[str],
        "entities": NotRequired[List["EntityTypeDef"]],
    },
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "eventVariables": NotRequired[List[str]],
        "labels": NotRequired[List[str]],
        "entityTypes": NotRequired[List[str]],
        "eventIngestion": NotRequired[EventIngestionType],
        "ingestedEventStatistics": NotRequired["IngestedEventStatisticsTypeDef"],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

EventVariableSummaryTypeDef = TypedDict(
    "EventVariableSummaryTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
        "source": NotRequired[str],
    },
)

ExternalEventsDetailTypeDef = TypedDict(
    "ExternalEventsDetailTypeDef",
    {
        "dataLocation": str,
        "dataAccessRoleArn": str,
    },
)

ExternalModelOutputsTypeDef = TypedDict(
    "ExternalModelOutputsTypeDef",
    {
        "externalModel": NotRequired["ExternalModelSummaryTypeDef"],
        "outputs": NotRequired[Dict[str, str]],
    },
)

ExternalModelSummaryTypeDef = TypedDict(
    "ExternalModelSummaryTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "modelSource": NotRequired[Literal["SAGEMAKER"]],
    },
)

ExternalModelTypeDef = TypedDict(
    "ExternalModelTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "modelSource": NotRequired[Literal["SAGEMAKER"]],
        "invokeModelEndpointRoleArn": NotRequired[str],
        "inputConfiguration": NotRequired["ModelInputConfigurationTypeDef"],
        "outputConfiguration": NotRequired["ModelOutputConfigurationTypeDef"],
        "modelEndpointStatus": NotRequired[ModelEndpointStatusType],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

FieldValidationMessageTypeDef = TypedDict(
    "FieldValidationMessageTypeDef",
    {
        "fieldName": NotRequired[str],
        "identifier": NotRequired[str],
        "title": NotRequired[str],
        "content": NotRequired[str],
        "type": NotRequired[str],
    },
)

FileValidationMessageTypeDef = TypedDict(
    "FileValidationMessageTypeDef",
    {
        "title": NotRequired[str],
        "content": NotRequired[str],
        "type": NotRequired[str],
    },
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "value": NotRequired[str],
    },
)

GetBatchImportJobsRequestRequestTypeDef = TypedDict(
    "GetBatchImportJobsRequestRequestTypeDef",
    {
        "jobId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetBatchImportJobsResultTypeDef = TypedDict(
    "GetBatchImportJobsResultTypeDef",
    {
        "batchImports": List["BatchImportTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBatchPredictionJobsRequestRequestTypeDef = TypedDict(
    "GetBatchPredictionJobsRequestRequestTypeDef",
    {
        "jobId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetBatchPredictionJobsResultTypeDef = TypedDict(
    "GetBatchPredictionJobsResultTypeDef",
    {
        "batchPredictions": List["BatchPredictionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeleteEventsByEventTypeStatusRequestRequestTypeDef = TypedDict(
    "GetDeleteEventsByEventTypeStatusRequestRequestTypeDef",
    {
        "eventTypeName": str,
    },
)

GetDeleteEventsByEventTypeStatusResultTypeDef = TypedDict(
    "GetDeleteEventsByEventTypeStatusResultTypeDef",
    {
        "eventTypeName": str,
        "eventsDeletionStatus": AsyncJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorVersionRequestRequestTypeDef = TypedDict(
    "GetDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

GetDetectorVersionResultTypeDef = TypedDict(
    "GetDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List["ModelVersionTypeDef"],
        "rules": List["RuleTypeDef"],
        "status": DetectorVersionStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "ruleExecutionMode": RuleExecutionModeType,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorsRequestRequestTypeDef = TypedDict(
    "GetDetectorsRequestRequestTypeDef",
    {
        "detectorId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetDetectorsResultTypeDef = TypedDict(
    "GetDetectorsResultTypeDef",
    {
        "detectors": List["DetectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEntityTypesRequestRequestTypeDef = TypedDict(
    "GetEntityTypesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetEntityTypesResultTypeDef = TypedDict(
    "GetEntityTypesResultTypeDef",
    {
        "entityTypes": List["EntityTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventPredictionMetadataRequestRequestTypeDef = TypedDict(
    "GetEventPredictionMetadataRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "detectorId": str,
        "detectorVersionId": str,
        "predictionTimestamp": str,
    },
)

GetEventPredictionMetadataResultTypeDef = TypedDict(
    "GetEventPredictionMetadataResultTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "entityId": str,
        "entityType": str,
        "eventTimestamp": str,
        "detectorId": str,
        "detectorVersionId": str,
        "detectorVersionStatus": str,
        "eventVariables": List["EventVariableSummaryTypeDef"],
        "rules": List["EvaluatedRuleTypeDef"],
        "ruleExecutionMode": RuleExecutionModeType,
        "outcomes": List[str],
        "evaluatedModelVersions": List["EvaluatedModelVersionTypeDef"],
        "evaluatedExternalModels": List["EvaluatedExternalModelTypeDef"],
        "predictionTimestamp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventPredictionRequestRequestTypeDef = TypedDict(
    "GetEventPredictionRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventId": str,
        "eventTypeName": str,
        "entities": Sequence["EntityTypeDef"],
        "eventTimestamp": str,
        "eventVariables": Mapping[str, str],
        "detectorVersionId": NotRequired[str],
        "externalModelEndpointDataBlobs": NotRequired[Mapping[str, "ModelEndpointDataBlobTypeDef"]],
    },
)

GetEventPredictionResultTypeDef = TypedDict(
    "GetEventPredictionResultTypeDef",
    {
        "modelScores": List["ModelScoresTypeDef"],
        "ruleResults": List["RuleResultTypeDef"],
        "externalModelOutputs": List["ExternalModelOutputsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventRequestRequestTypeDef = TypedDict(
    "GetEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
    },
)

GetEventResultTypeDef = TypedDict(
    "GetEventResultTypeDef",
    {
        "event": "EventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventTypesRequestRequestTypeDef = TypedDict(
    "GetEventTypesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetEventTypesResultTypeDef = TypedDict(
    "GetEventTypesResultTypeDef",
    {
        "eventTypes": List["EventTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExternalModelsRequestRequestTypeDef = TypedDict(
    "GetExternalModelsRequestRequestTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetExternalModelsResultTypeDef = TypedDict(
    "GetExternalModelsResultTypeDef",
    {
        "externalModels": List["ExternalModelTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKMSEncryptionKeyResultTypeDef = TypedDict(
    "GetKMSEncryptionKeyResultTypeDef",
    {
        "kmsKey": "KMSKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLabelsRequestRequestTypeDef = TypedDict(
    "GetLabelsRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetLabelsResultTypeDef = TypedDict(
    "GetLabelsResultTypeDef",
    {
        "labels": List["LabelTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelVersionRequestRequestTypeDef = TypedDict(
    "GetModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)

GetModelVersionResultTypeDef = TypedDict(
    "GetModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "ingestedEventsDetail": "IngestedEventsDetailTypeDef",
        "status": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelsRequestRequestTypeDef = TypedDict(
    "GetModelsRequestRequestTypeDef",
    {
        "modelId": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetModelsResultTypeDef = TypedDict(
    "GetModelsResultTypeDef",
    {
        "nextToken": str,
        "models": List["ModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutcomesRequestRequestTypeDef = TypedDict(
    "GetOutcomesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetOutcomesResultTypeDef = TypedDict(
    "GetOutcomesResultTypeDef",
    {
        "outcomes": List["OutcomeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRulesRequestRequestTypeDef = TypedDict(
    "GetRulesRequestRequestTypeDef",
    {
        "detectorId": str,
        "ruleId": NotRequired[str],
        "ruleVersion": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetRulesResultTypeDef = TypedDict(
    "GetRulesResultTypeDef",
    {
        "ruleDetails": List["RuleDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVariablesRequestRequestTypeDef = TypedDict(
    "GetVariablesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetVariablesResultTypeDef = TypedDict(
    "GetVariablesResultTypeDef",
    {
        "variables": List["VariableTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IngestedEventStatisticsTypeDef = TypedDict(
    "IngestedEventStatisticsTypeDef",
    {
        "numberOfEvents": NotRequired[int],
        "eventDataSizeInBytes": NotRequired[int],
        "leastRecentEvent": NotRequired[str],
        "mostRecentEvent": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
    },
)

IngestedEventsDetailTypeDef = TypedDict(
    "IngestedEventsDetailTypeDef",
    {
        "ingestedEventsTimeWindow": "IngestedEventsTimeWindowTypeDef",
    },
)

IngestedEventsTimeWindowTypeDef = TypedDict(
    "IngestedEventsTimeWindowTypeDef",
    {
        "startTime": str,
        "endTime": str,
    },
)

KMSKeyTypeDef = TypedDict(
    "KMSKeyTypeDef",
    {
        "kmsEncryptionKeyArn": NotRequired[str],
    },
)

LabelSchemaTypeDef = TypedDict(
    "LabelSchemaTypeDef",
    {
        "labelMapper": Mapping[str, Sequence[str]],
        "unlabeledEventsTreatment": NotRequired[UnlabeledEventsTreatmentType],
    },
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

ListEventPredictionsRequestRequestTypeDef = TypedDict(
    "ListEventPredictionsRequestRequestTypeDef",
    {
        "eventId": NotRequired["FilterConditionTypeDef"],
        "eventType": NotRequired["FilterConditionTypeDef"],
        "detectorId": NotRequired["FilterConditionTypeDef"],
        "detectorVersionId": NotRequired["FilterConditionTypeDef"],
        "predictionTimeRange": NotRequired["PredictionTimeRangeTypeDef"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListEventPredictionsResultTypeDef = TypedDict(
    "ListEventPredictionsResultTypeDef",
    {
        "eventPredictionSummaries": List["EventPredictionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogOddsMetricTypeDef = TypedDict(
    "LogOddsMetricTypeDef",
    {
        "variableName": str,
        "variableType": str,
        "variableImportance": float,
    },
)

MetricDataPointTypeDef = TypedDict(
    "MetricDataPointTypeDef",
    {
        "fpr": NotRequired[float],
        "precision": NotRequired[float],
        "tpr": NotRequired[float],
        "threshold": NotRequired[float],
    },
)

ModelEndpointDataBlobTypeDef = TypedDict(
    "ModelEndpointDataBlobTypeDef",
    {
        "byteBuffer": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "contentType": NotRequired[str],
    },
)

ModelInputConfigurationTypeDef = TypedDict(
    "ModelInputConfigurationTypeDef",
    {
        "useEventVariables": bool,
        "eventTypeName": NotRequired[str],
        "format": NotRequired[ModelInputDataFormatType],
        "jsonInputTemplate": NotRequired[str],
        "csvInputTemplate": NotRequired[str],
    },
)

ModelOutputConfigurationTypeDef = TypedDict(
    "ModelOutputConfigurationTypeDef",
    {
        "format": ModelOutputDataFormatType,
        "jsonKeyToVariableMap": NotRequired[Dict[str, str]],
        "csvIndexToVariableMap": NotRequired[Dict[str, str]],
    },
)

ModelScoresTypeDef = TypedDict(
    "ModelScoresTypeDef",
    {
        "modelVersion": NotRequired["ModelVersionTypeDef"],
        "scores": NotRequired[Dict[str, float]],
    },
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "modelId": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "description": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "createdTime": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

ModelVersionDetailTypeDef = TypedDict(
    "ModelVersionDetailTypeDef",
    {
        "modelId": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "modelVersionNumber": NotRequired[str],
        "status": NotRequired[str],
        "trainingDataSource": NotRequired[TrainingDataSourceEnumType],
        "trainingDataSchema": NotRequired["TrainingDataSchemaTypeDef"],
        "externalEventsDetail": NotRequired["ExternalEventsDetailTypeDef"],
        "ingestedEventsDetail": NotRequired["IngestedEventsDetailTypeDef"],
        "trainingResult": NotRequired["TrainingResultTypeDef"],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

ModelVersionEvaluationTypeDef = TypedDict(
    "ModelVersionEvaluationTypeDef",
    {
        "outputVariableName": NotRequired[str],
        "evaluationScore": NotRequired[str],
        "predictionExplanations": NotRequired["PredictionExplanationsTypeDef"],
    },
)

ModelVersionTypeDef = TypedDict(
    "ModelVersionTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "arn": NotRequired[str],
    },
)

OutcomeTypeDef = TypedDict(
    "OutcomeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

PredictionExplanationsTypeDef = TypedDict(
    "PredictionExplanationsTypeDef",
    {
        "variableImpactExplanations": NotRequired[List["VariableImpactExplanationTypeDef"]],
    },
)

PredictionTimeRangeTypeDef = TypedDict(
    "PredictionTimeRangeTypeDef",
    {
        "startTime": str,
        "endTime": str,
    },
)

PutDetectorRequestRequestTypeDef = TypedDict(
    "PutDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventTypeName": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutEntityTypeRequestRequestTypeDef = TypedDict(
    "PutEntityTypeRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutEventTypeRequestRequestTypeDef = TypedDict(
    "PutEventTypeRequestRequestTypeDef",
    {
        "name": str,
        "eventVariables": Sequence[str],
        "entityTypes": Sequence[str],
        "description": NotRequired[str],
        "labels": NotRequired[Sequence[str]],
        "eventIngestion": NotRequired[EventIngestionType],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutExternalModelRequestRequestTypeDef = TypedDict(
    "PutExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": "ModelInputConfigurationTypeDef",
        "outputConfiguration": "ModelOutputConfigurationTypeDef",
        "modelEndpointStatus": ModelEndpointStatusType,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutKMSEncryptionKeyRequestRequestTypeDef = TypedDict(
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
)

PutLabelRequestRequestTypeDef = TypedDict(
    "PutLabelRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutOutcomeRequestRequestTypeDef = TypedDict(
    "PutOutcomeRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
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

RuleDetailTypeDef = TypedDict(
    "RuleDetailTypeDef",
    {
        "ruleId": NotRequired[str],
        "description": NotRequired[str],
        "detectorId": NotRequired[str],
        "ruleVersion": NotRequired[str],
        "expression": NotRequired[str],
        "language": NotRequired[Literal["DETECTORPL"]],
        "outcomes": NotRequired[List[str]],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)

RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "ruleId": NotRequired[str],
        "outcomes": NotRequired[List[str]],
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "detectorId": str,
        "ruleId": str,
        "ruleVersion": str,
    },
)

SendEventRequestRequestTypeDef = TypedDict(
    "SendEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "eventTimestamp": str,
        "eventVariables": Mapping[str, str],
        "entities": Sequence["EntityTypeDef"],
        "assignedLabel": NotRequired[str],
        "labelTimestamp": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
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

TrainingDataSchemaTypeDef = TypedDict(
    "TrainingDataSchemaTypeDef",
    {
        "modelVariables": Sequence[str],
        "labelSchema": "LabelSchemaTypeDef",
    },
)

TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "auc": NotRequired[float],
        "metricDataPoints": NotRequired[List["MetricDataPointTypeDef"]],
    },
)

TrainingResultTypeDef = TypedDict(
    "TrainingResultTypeDef",
    {
        "dataValidationMetrics": NotRequired["DataValidationMetricsTypeDef"],
        "trainingMetrics": NotRequired["TrainingMetricsTypeDef"],
        "variableImportanceMetrics": NotRequired["VariableImportanceMetricsTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)

UpdateDetectorVersionMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
    },
)

UpdateDetectorVersionRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "externalModelEndpoints": Sequence[str],
        "rules": Sequence["RuleTypeDef"],
        "description": NotRequired[str],
        "modelVersions": NotRequired[Sequence["ModelVersionTypeDef"]],
        "ruleExecutionMode": NotRequired[RuleExecutionModeType],
    },
)

UpdateDetectorVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
    },
)

UpdateEventLabelRequestRequestTypeDef = TypedDict(
    "UpdateEventLabelRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "assignedLabel": str,
        "labelTimestamp": str,
    },
)

UpdateModelRequestRequestTypeDef = TypedDict(
    "UpdateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "description": NotRequired[str],
    },
)

UpdateModelVersionRequestRequestTypeDef = TypedDict(
    "UpdateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "majorVersionNumber": str,
        "externalEventsDetail": NotRequired["ExternalEventsDetailTypeDef"],
        "ingestedEventsDetail": NotRequired["IngestedEventsDetailTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateModelVersionResultTypeDef = TypedDict(
    "UpdateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateModelVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateModelVersionStatusRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": ModelVersionStatusType,
    },
)

UpdateRuleMetadataRequestRequestTypeDef = TypedDict(
    "UpdateRuleMetadataRequestRequestTypeDef",
    {
        "rule": "RuleTypeDef",
        "description": str,
    },
)

UpdateRuleVersionRequestRequestTypeDef = TypedDict(
    "UpdateRuleVersionRequestRequestTypeDef",
    {
        "rule": "RuleTypeDef",
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": Sequence[str],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateRuleVersionResultTypeDef = TypedDict(
    "UpdateRuleVersionResultTypeDef",
    {
        "rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVariableRequestRequestTypeDef = TypedDict(
    "UpdateVariableRequestRequestTypeDef",
    {
        "name": str,
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "variableType": NotRequired[str],
    },
)

VariableEntryTypeDef = TypedDict(
    "VariableEntryTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[str],
        "dataSource": NotRequired[str],
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "variableType": NotRequired[str],
    },
)

VariableImpactExplanationTypeDef = TypedDict(
    "VariableImpactExplanationTypeDef",
    {
        "eventVariableName": NotRequired[str],
        "relativeImpact": NotRequired[str],
        "logOddsImpact": NotRequired[float],
    },
)

VariableImportanceMetricsTypeDef = TypedDict(
    "VariableImportanceMetricsTypeDef",
    {
        "logOddsMetrics": NotRequired[List["LogOddsMetricTypeDef"]],
    },
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[DataTypeType],
        "dataSource": NotRequired[DataSourceType],
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "variableType": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
