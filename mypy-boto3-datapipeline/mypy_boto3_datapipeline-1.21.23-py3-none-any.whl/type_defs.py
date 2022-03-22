"""
Type annotations for datapipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datapipeline.type_defs import ActivatePipelineInputRequestTypeDef

    data: ActivatePipelineInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import OperatorTypeType, TaskStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivatePipelineInputRequestTypeDef",
    "AddTagsInputRequestTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "CreatePipelineOutputTypeDef",
    "DeactivatePipelineInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "DescribeObjectsInputRequestTypeDef",
    "DescribeObjectsOutputTypeDef",
    "DescribePipelinesInputRequestTypeDef",
    "DescribePipelinesOutputTypeDef",
    "EvaluateExpressionInputRequestTypeDef",
    "EvaluateExpressionOutputTypeDef",
    "FieldTypeDef",
    "GetPipelineDefinitionInputRequestTypeDef",
    "GetPipelineDefinitionOutputTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "ListPipelinesOutputTypeDef",
    "OperatorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterAttributeTypeDef",
    "ParameterObjectTypeDef",
    "ParameterValueTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineIdNameTypeDef",
    "PipelineObjectTypeDef",
    "PollForTaskInputRequestTypeDef",
    "PollForTaskOutputTypeDef",
    "PutPipelineDefinitionInputRequestTypeDef",
    "PutPipelineDefinitionOutputTypeDef",
    "QueryObjectsInputRequestTypeDef",
    "QueryObjectsOutputTypeDef",
    "QueryTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ReportTaskProgressInputRequestTypeDef",
    "ReportTaskProgressOutputTypeDef",
    "ReportTaskRunnerHeartbeatInputRequestTypeDef",
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SelectorTypeDef",
    "SetStatusInputRequestTypeDef",
    "SetTaskStatusInputRequestTypeDef",
    "TagTypeDef",
    "TaskObjectTypeDef",
    "ValidatePipelineDefinitionInputRequestTypeDef",
    "ValidatePipelineDefinitionOutputTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
)

ActivatePipelineInputRequestTypeDef = TypedDict(
    "ActivatePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
        "parameterValues": NotRequired[Sequence["ParameterValueTypeDef"]],
        "startTimestamp": NotRequired[Union[datetime, str]],
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "pipelineId": str,
        "tags": Sequence["TagTypeDef"],
    },
)

CreatePipelineInputRequestTypeDef = TypedDict(
    "CreatePipelineInputRequestTypeDef",
    {
        "name": str,
        "uniqueId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipelineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivatePipelineInputRequestTypeDef = TypedDict(
    "DeactivatePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
        "cancelActive": NotRequired[bool],
    },
)

DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "pipelineId": str,
    },
)

DescribeObjectsInputRequestTypeDef = TypedDict(
    "DescribeObjectsInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectIds": Sequence[str],
        "evaluateExpressions": NotRequired[bool],
        "marker": NotRequired[str],
    },
)

DescribeObjectsOutputTypeDef = TypedDict(
    "DescribeObjectsOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelinesInputRequestTypeDef = TypedDict(
    "DescribePipelinesInputRequestTypeDef",
    {
        "pipelineIds": Sequence[str],
    },
)

DescribePipelinesOutputTypeDef = TypedDict(
    "DescribePipelinesOutputTypeDef",
    {
        "pipelineDescriptionList": List["PipelineDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluateExpressionInputRequestTypeDef = TypedDict(
    "EvaluateExpressionInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectId": str,
        "expression": str,
    },
)

EvaluateExpressionOutputTypeDef = TypedDict(
    "EvaluateExpressionOutputTypeDef",
    {
        "evaluatedExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "key": str,
        "stringValue": NotRequired[str],
        "refValue": NotRequired[str],
    },
)

GetPipelineDefinitionInputRequestTypeDef = TypedDict(
    "GetPipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "version": NotRequired[str],
    },
)

GetPipelineDefinitionOutputTypeDef = TypedDict(
    "GetPipelineDefinitionOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "document": NotRequired[str],
        "signature": NotRequired[str],
    },
)

ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "marker": NotRequired[str],
    },
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelineIdList": List["PipelineIdNameTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperatorTypeDef = TypedDict(
    "OperatorTypeDef",
    {
        "type": NotRequired[OperatorTypeType],
        "values": NotRequired[Sequence[str]],
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

ParameterAttributeTypeDef = TypedDict(
    "ParameterAttributeTypeDef",
    {
        "key": str,
        "stringValue": str,
    },
)

ParameterObjectTypeDef = TypedDict(
    "ParameterObjectTypeDef",
    {
        "id": str,
        "attributes": List["ParameterAttributeTypeDef"],
    },
)

ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "id": str,
        "stringValue": str,
    },
)

PipelineDescriptionTypeDef = TypedDict(
    "PipelineDescriptionTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List["FieldTypeDef"],
        "description": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

PipelineIdNameTypeDef = TypedDict(
    "PipelineIdNameTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)

PipelineObjectTypeDef = TypedDict(
    "PipelineObjectTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List["FieldTypeDef"],
    },
)

PollForTaskInputRequestTypeDef = TypedDict(
    "PollForTaskInputRequestTypeDef",
    {
        "workerGroup": str,
        "hostname": NotRequired[str],
        "instanceIdentity": NotRequired["InstanceIdentityTypeDef"],
    },
)

PollForTaskOutputTypeDef = TypedDict(
    "PollForTaskOutputTypeDef",
    {
        "taskObject": "TaskObjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPipelineDefinitionInputRequestTypeDef = TypedDict(
    "PutPipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": Sequence["PipelineObjectTypeDef"],
        "parameterObjects": NotRequired[Sequence["ParameterObjectTypeDef"]],
        "parameterValues": NotRequired[Sequence["ParameterValueTypeDef"]],
    },
)

PutPipelineDefinitionOutputTypeDef = TypedDict(
    "PutPipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryObjectsInputRequestTypeDef = TypedDict(
    "QueryObjectsInputRequestTypeDef",
    {
        "pipelineId": str,
        "sphere": str,
        "query": NotRequired["QueryTypeDef"],
        "marker": NotRequired[str],
        "limit": NotRequired[int],
    },
)

QueryObjectsOutputTypeDef = TypedDict(
    "QueryObjectsOutputTypeDef",
    {
        "ids": List[str],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "selectors": NotRequired[Sequence["SelectorTypeDef"]],
    },
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "pipelineId": str,
        "tagKeys": Sequence[str],
    },
)

ReportTaskProgressInputRequestTypeDef = TypedDict(
    "ReportTaskProgressInputRequestTypeDef",
    {
        "taskId": str,
        "fields": NotRequired[Sequence["FieldTypeDef"]],
    },
)

ReportTaskProgressOutputTypeDef = TypedDict(
    "ReportTaskProgressOutputTypeDef",
    {
        "canceled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportTaskRunnerHeartbeatInputRequestTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatInputRequestTypeDef",
    {
        "taskrunnerId": str,
        "workerGroup": NotRequired[str],
        "hostname": NotRequired[str],
    },
)

ReportTaskRunnerHeartbeatOutputTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    {
        "terminate": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "fieldName": NotRequired[str],
        "operator": NotRequired["OperatorTypeDef"],
    },
)

SetStatusInputRequestTypeDef = TypedDict(
    "SetStatusInputRequestTypeDef",
    {
        "pipelineId": str,
        "objectIds": Sequence[str],
        "status": str,
    },
)

SetTaskStatusInputRequestTypeDef = TypedDict(
    "SetTaskStatusInputRequestTypeDef",
    {
        "taskId": str,
        "taskStatus": TaskStatusType,
        "errorId": NotRequired[str],
        "errorMessage": NotRequired[str],
        "errorStackTrace": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TaskObjectTypeDef = TypedDict(
    "TaskObjectTypeDef",
    {
        "taskId": NotRequired[str],
        "pipelineId": NotRequired[str],
        "attemptId": NotRequired[str],
        "objects": NotRequired[Dict[str, "PipelineObjectTypeDef"]],
    },
)

ValidatePipelineDefinitionInputRequestTypeDef = TypedDict(
    "ValidatePipelineDefinitionInputRequestTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": Sequence["PipelineObjectTypeDef"],
        "parameterObjects": NotRequired[Sequence["ParameterObjectTypeDef"]],
        "parameterValues": NotRequired[Sequence["ParameterValueTypeDef"]],
    },
)

ValidatePipelineDefinitionOutputTypeDef = TypedDict(
    "ValidatePipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "id": NotRequired[str],
        "errors": NotRequired[List[str]],
    },
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "id": NotRequired[str],
        "warnings": NotRequired[List[str]],
    },
)
