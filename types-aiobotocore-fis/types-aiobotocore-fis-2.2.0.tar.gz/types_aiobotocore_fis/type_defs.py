"""
Type annotations for fis service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_fis/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_fis.type_defs import ActionParameterTypeDef

    data: ActionParameterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import ExperimentActionStatusType, ExperimentStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionParameterTypeDef",
    "ActionSummaryTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "CreateExperimentTemplateActionInputTypeDef",
    "CreateExperimentTemplateLogConfigurationInputTypeDef",
    "CreateExperimentTemplateRequestRequestTypeDef",
    "CreateExperimentTemplateResponseTypeDef",
    "CreateExperimentTemplateStopConditionInputTypeDef",
    "CreateExperimentTemplateTargetInputTypeDef",
    "DeleteExperimentTemplateRequestRequestTypeDef",
    "DeleteExperimentTemplateResponseTypeDef",
    "ExperimentActionStateTypeDef",
    "ExperimentActionTypeDef",
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentLogConfigurationTypeDef",
    "ExperimentS3LogConfigurationTypeDef",
    "ExperimentStateTypeDef",
    "ExperimentStopConditionTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTargetFilterTypeDef",
    "ExperimentTargetTypeDef",
    "ExperimentTemplateActionTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentTemplateLogConfigurationTypeDef",
    "ExperimentTemplateS3LogConfigurationInputTypeDef",
    "ExperimentTemplateS3LogConfigurationTypeDef",
    "ExperimentTemplateStopConditionTypeDef",
    "ExperimentTemplateSummaryTypeDef",
    "ExperimentTemplateTargetFilterTypeDef",
    "ExperimentTemplateTargetInputFilterTypeDef",
    "ExperimentTemplateTargetTypeDef",
    "ExperimentTemplateTypeDef",
    "ExperimentTypeDef",
    "GetActionRequestRequestTypeDef",
    "GetActionResponseTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetExperimentResponseTypeDef",
    "GetExperimentTemplateRequestRequestTypeDef",
    "GetExperimentTemplateResponseTypeDef",
    "GetTargetResourceTypeRequestRequestTypeDef",
    "GetTargetResourceTypeResponseTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListActionsResponseTypeDef",
    "ListExperimentTemplatesRequestRequestTypeDef",
    "ListExperimentTemplatesResponseTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetResourceTypesRequestRequestTypeDef",
    "ListTargetResourceTypesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "StopExperimentResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetResourceTypeParameterTypeDef",
    "TargetResourceTypeSummaryTypeDef",
    "TargetResourceTypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExperimentTemplateActionInputItemTypeDef",
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    "UpdateExperimentTemplateRequestRequestTypeDef",
    "UpdateExperimentTemplateResponseTypeDef",
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    "UpdateExperimentTemplateTargetInputTypeDef",
)

ActionParameterTypeDef = TypedDict(
    "ActionParameterTypeDef",
    {
        "description": NotRequired[str],
        "required": NotRequired[bool],
    },
)

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "targets": NotRequired[Dict[str, "ActionTargetTypeDef"]],
        "tags": NotRequired[Dict[str, str]],
    },
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "resourceType": NotRequired[str],
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, "ActionParameterTypeDef"]],
        "targets": NotRequired[Dict[str, "ActionTargetTypeDef"]],
        "tags": NotRequired[Dict[str, str]],
    },
)

CreateExperimentTemplateActionInputTypeDef = TypedDict(
    "CreateExperimentTemplateActionInputTypeDef",
    {
        "actionId": str,
        "description": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
        "targets": NotRequired[Mapping[str, str]],
        "startAfter": NotRequired[Sequence[str]],
    },
)

CreateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "CreateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "logSchemaVersion": int,
        "cloudWatchLogsConfiguration": NotRequired[
            "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef"
        ],
        "s3Configuration": NotRequired["ExperimentTemplateS3LogConfigurationInputTypeDef"],
    },
)

CreateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "CreateExperimentTemplateRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "stopConditions": Sequence["CreateExperimentTemplateStopConditionInputTypeDef"],
        "actions": Mapping[str, "CreateExperimentTemplateActionInputTypeDef"],
        "roleArn": str,
        "targets": NotRequired[Mapping[str, "CreateExperimentTemplateTargetInputTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
        "logConfiguration": NotRequired["CreateExperimentTemplateLogConfigurationInputTypeDef"],
    },
)

CreateExperimentTemplateResponseTypeDef = TypedDict(
    "CreateExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "CreateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
        "value": NotRequired[str],
    },
)

CreateExperimentTemplateTargetInputTypeDef = TypedDict(
    "CreateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
        "resourceArns": NotRequired[Sequence[str]],
        "resourceTags": NotRequired[Mapping[str, str]],
        "filters": NotRequired[Sequence["ExperimentTemplateTargetInputFilterTypeDef"]],
        "parameters": NotRequired[Mapping[str, str]],
    },
)

DeleteExperimentTemplateRequestRequestTypeDef = TypedDict(
    "DeleteExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteExperimentTemplateResponseTypeDef = TypedDict(
    "DeleteExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExperimentActionStateTypeDef = TypedDict(
    "ExperimentActionStateTypeDef",
    {
        "status": NotRequired[ExperimentActionStatusType],
        "reason": NotRequired[str],
    },
)

ExperimentActionTypeDef = TypedDict(
    "ExperimentActionTypeDef",
    {
        "actionId": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
        "targets": NotRequired[Dict[str, str]],
        "startAfter": NotRequired[List[str]],
        "state": NotRequired["ExperimentActionStateTypeDef"],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)

ExperimentCloudWatchLogsLogConfigurationTypeDef = TypedDict(
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    {
        "logGroupArn": NotRequired[str],
    },
)

ExperimentLogConfigurationTypeDef = TypedDict(
    "ExperimentLogConfigurationTypeDef",
    {
        "cloudWatchLogsConfiguration": NotRequired[
            "ExperimentCloudWatchLogsLogConfigurationTypeDef"
        ],
        "s3Configuration": NotRequired["ExperimentS3LogConfigurationTypeDef"],
        "logSchemaVersion": NotRequired[int],
    },
)

ExperimentS3LogConfigurationTypeDef = TypedDict(
    "ExperimentS3LogConfigurationTypeDef",
    {
        "bucketName": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

ExperimentStateTypeDef = TypedDict(
    "ExperimentStateTypeDef",
    {
        "status": NotRequired[ExperimentStatusType],
        "reason": NotRequired[str],
    },
)

ExperimentStopConditionTypeDef = TypedDict(
    "ExperimentStopConditionTypeDef",
    {
        "source": NotRequired[str],
        "value": NotRequired[str],
    },
)

ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "id": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
        "state": NotRequired["ExperimentStateTypeDef"],
        "creationTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

ExperimentTargetFilterTypeDef = TypedDict(
    "ExperimentTargetFilterTypeDef",
    {
        "path": NotRequired[str],
        "values": NotRequired[List[str]],
    },
)

ExperimentTargetTypeDef = TypedDict(
    "ExperimentTargetTypeDef",
    {
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[List[str]],
        "resourceTags": NotRequired[Dict[str, str]],
        "filters": NotRequired[List["ExperimentTargetFilterTypeDef"]],
        "selectionMode": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
    },
)

ExperimentTemplateActionTypeDef = TypedDict(
    "ExperimentTemplateActionTypeDef",
    {
        "actionId": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
        "targets": NotRequired[Dict[str, str]],
        "startAfter": NotRequired[List[str]],
    },
)

ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef = TypedDict(
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    {
        "logGroupArn": str,
    },
)

ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    {
        "logGroupArn": NotRequired[str],
    },
)

ExperimentTemplateLogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateLogConfigurationTypeDef",
    {
        "cloudWatchLogsConfiguration": NotRequired[
            "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef"
        ],
        "s3Configuration": NotRequired["ExperimentTemplateS3LogConfigurationTypeDef"],
        "logSchemaVersion": NotRequired[int],
    },
)

ExperimentTemplateS3LogConfigurationInputTypeDef = TypedDict(
    "ExperimentTemplateS3LogConfigurationInputTypeDef",
    {
        "bucketName": str,
        "prefix": NotRequired[str],
    },
)

ExperimentTemplateS3LogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateS3LogConfigurationTypeDef",
    {
        "bucketName": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

ExperimentTemplateStopConditionTypeDef = TypedDict(
    "ExperimentTemplateStopConditionTypeDef",
    {
        "source": NotRequired[str],
        "value": NotRequired[str],
    },
)

ExperimentTemplateSummaryTypeDef = TypedDict(
    "ExperimentTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

ExperimentTemplateTargetFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetFilterTypeDef",
    {
        "path": NotRequired[str],
        "values": NotRequired[List[str]],
    },
)

ExperimentTemplateTargetInputFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetInputFilterTypeDef",
    {
        "path": str,
        "values": Sequence[str],
    },
)

ExperimentTemplateTargetTypeDef = TypedDict(
    "ExperimentTemplateTargetTypeDef",
    {
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[List[str]],
        "resourceTags": NotRequired[Dict[str, str]],
        "filters": NotRequired[List["ExperimentTemplateTargetFilterTypeDef"]],
        "selectionMode": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
    },
)

ExperimentTemplateTypeDef = TypedDict(
    "ExperimentTemplateTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "targets": NotRequired[Dict[str, "ExperimentTemplateTargetTypeDef"]],
        "actions": NotRequired[Dict[str, "ExperimentTemplateActionTypeDef"]],
        "stopConditions": NotRequired[List["ExperimentTemplateStopConditionTypeDef"]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "logConfiguration": NotRequired["ExperimentTemplateLogConfigurationTypeDef"],
    },
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "id": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
        "roleArn": NotRequired[str],
        "state": NotRequired["ExperimentStateTypeDef"],
        "targets": NotRequired[Dict[str, "ExperimentTargetTypeDef"]],
        "actions": NotRequired[Dict[str, "ExperimentActionTypeDef"]],
        "stopConditions": NotRequired[List["ExperimentStopConditionTypeDef"]],
        "creationTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "logConfiguration": NotRequired["ExperimentLogConfigurationTypeDef"],
    },
)

GetActionRequestRequestTypeDef = TypedDict(
    "GetActionRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetActionResponseTypeDef = TypedDict(
    "GetActionResponseTypeDef",
    {
        "action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentTemplateRequestRequestTypeDef = TypedDict(
    "GetExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetExperimentTemplateResponseTypeDef = TypedDict(
    "GetExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTargetResourceTypeRequestRequestTypeDef = TypedDict(
    "GetTargetResourceTypeRequestRequestTypeDef",
    {
        "resourceType": str,
    },
)

GetTargetResourceTypeResponseTypeDef = TypedDict(
    "GetTargetResourceTypeResponseTypeDef",
    {
        "targetResourceType": "TargetResourceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "actions": List["ActionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentTemplatesRequestRequestTypeDef = TypedDict(
    "ListExperimentTemplatesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListExperimentTemplatesResponseTypeDef = TypedDict(
    "ListExperimentTemplatesResponseTypeDef",
    {
        "experimentTemplates": List["ExperimentTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List["ExperimentSummaryTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetResourceTypesRequestRequestTypeDef = TypedDict(
    "ListTargetResourceTypesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTargetResourceTypesResponseTypeDef = TypedDict(
    "ListTargetResourceTypesResponseTypeDef",
    {
        "targetResourceTypes": List["TargetResourceTypeSummaryTypeDef"],
        "nextToken": str,
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

StartExperimentRequestRequestTypeDef = TypedDict(
    "StartExperimentRequestRequestTypeDef",
    {
        "clientToken": str,
        "experimentTemplateId": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExperimentRequestRequestTypeDef = TypedDict(
    "StopExperimentRequestRequestTypeDef",
    {
        "id": str,
    },
)

StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
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

TargetResourceTypeParameterTypeDef = TypedDict(
    "TargetResourceTypeParameterTypeDef",
    {
        "description": NotRequired[str],
        "required": NotRequired[bool],
    },
)

TargetResourceTypeSummaryTypeDef = TypedDict(
    "TargetResourceTypeSummaryTypeDef",
    {
        "resourceType": NotRequired[str],
        "description": NotRequired[str],
    },
)

TargetResourceTypeTypeDef = TypedDict(
    "TargetResourceTypeTypeDef",
    {
        "resourceType": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, "TargetResourceTypeParameterTypeDef"]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": NotRequired[Sequence[str]],
    },
)

UpdateExperimentTemplateActionInputItemTypeDef = TypedDict(
    "UpdateExperimentTemplateActionInputItemTypeDef",
    {
        "actionId": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
        "targets": NotRequired[Mapping[str, str]],
        "startAfter": NotRequired[Sequence[str]],
    },
)

UpdateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "cloudWatchLogsConfiguration": NotRequired[
            "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef"
        ],
        "s3Configuration": NotRequired["ExperimentTemplateS3LogConfigurationInputTypeDef"],
        "logSchemaVersion": NotRequired[int],
    },
)

UpdateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "UpdateExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
        "description": NotRequired[str],
        "stopConditions": NotRequired[
            Sequence["UpdateExperimentTemplateStopConditionInputTypeDef"]
        ],
        "targets": NotRequired[Mapping[str, "UpdateExperimentTemplateTargetInputTypeDef"]],
        "actions": NotRequired[Mapping[str, "UpdateExperimentTemplateActionInputItemTypeDef"]],
        "roleArn": NotRequired[str],
        "logConfiguration": NotRequired["UpdateExperimentTemplateLogConfigurationInputTypeDef"],
    },
)

UpdateExperimentTemplateResponseTypeDef = TypedDict(
    "UpdateExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
        "value": NotRequired[str],
    },
)

UpdateExperimentTemplateTargetInputTypeDef = TypedDict(
    "UpdateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
        "resourceArns": NotRequired[Sequence[str]],
        "resourceTags": NotRequired[Mapping[str, str]],
        "filters": NotRequired[Sequence["ExperimentTemplateTargetInputFilterTypeDef"]],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
