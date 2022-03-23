"""
Type annotations for codepipeline service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_codepipeline/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActionCategoryType,
    ActionConfigurationPropertyTypeType,
    ActionExecutionStatusType,
    ActionOwnerType,
    ApprovalStatusType,
    ExecutorTypeType,
    FailureTypeType,
    JobStatusType,
    PipelineExecutionStatusType,
    StageExecutionStatusType,
    StageTransitionTypeType,
    TriggerTypeType,
    WebhookAuthenticationTypeType,
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
    "AWSSessionCredentialsTypeDef",
    "AcknowledgeJobInputRequestTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionDeclarationTypeDef",
    "ActionExecutionDetailTypeDef",
    "ActionExecutionFilterTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionTypeDef",
    "ActionStateTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeDeclarationTypeDef",
    "ActionTypeExecutorTypeDef",
    "ActionTypeIdTypeDef",
    "ActionTypeIdentifierTypeDef",
    "ActionTypePermissionsTypeDef",
    "ActionTypePropertyTypeDef",
    "ActionTypeSettingsTypeDef",
    "ActionTypeTypeDef",
    "ActionTypeUrlsTypeDef",
    "ApprovalResultTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactDetailsTypeDef",
    "ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "ArtifactStoreTypeDef",
    "ArtifactTypeDef",
    "BlockerDeclarationTypeDef",
    "CreateCustomActionTypeInputRequestTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "CreatePipelineOutputTypeDef",
    "CurrentRevisionTypeDef",
    "DeleteCustomActionTypeInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "DeleteWebhookInputRequestTypeDef",
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    "DisableStageTransitionInputRequestTypeDef",
    "EnableStageTransitionInputRequestTypeDef",
    "EncryptionKeyTypeDef",
    "ErrorDetailsTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "ExecutorConfigurationTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeInputRequestTypeDef",
    "GetActionTypeOutputTypeDef",
    "GetJobDetailsInputRequestTypeDef",
    "GetJobDetailsOutputTypeDef",
    "GetPipelineExecutionInputRequestTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "GetPipelineInputRequestTypeDef",
    "GetPipelineOutputTypeDef",
    "GetPipelineStateInputRequestTypeDef",
    "GetPipelineStateOutputTypeDef",
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
    "InputArtifactTypeDef",
    "JobDataTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "ListActionExecutionsInputRequestTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "ListActionTypesInputRequestTypeDef",
    "ListActionTypesOutputTypeDef",
    "ListPipelineExecutionsInputRequestTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "ListPipelinesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWebhookItemTypeDef",
    "ListWebhooksInputRequestTypeDef",
    "ListWebhooksOutputTypeDef",
    "OutputArtifactTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineContextTypeDef",
    "PipelineDeclarationTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineMetadataTypeDef",
    "PipelineSummaryTypeDef",
    "PollForJobsInputRequestTypeDef",
    "PollForJobsOutputTypeDef",
    "PollForThirdPartyJobsInputRequestTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "PutActionRevisionInputRequestTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultInputRequestTypeDef",
    "PutApprovalResultOutputTypeDef",
    "PutJobFailureResultInputRequestTypeDef",
    "PutJobSuccessResultInputRequestTypeDef",
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    "PutThirdPartyJobSuccessResultInputRequestTypeDef",
    "PutWebhookInputRequestTypeDef",
    "PutWebhookOutputTypeDef",
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStageExecutionInputRequestTypeDef",
    "RetryStageExecutionOutputTypeDef",
    "S3ArtifactLocationTypeDef",
    "S3LocationTypeDef",
    "SourceRevisionTypeDef",
    "StageContextTypeDef",
    "StageDeclarationTypeDef",
    "StageExecutionTypeDef",
    "StageStateTypeDef",
    "StartPipelineExecutionInputRequestTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopExecutionTriggerTypeDef",
    "StopPipelineExecutionInputRequestTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "ThirdPartyJobTypeDef",
    "TransitionStateTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateActionTypeInputRequestTypeDef",
    "UpdatePipelineInputRequestTypeDef",
    "UpdatePipelineOutputTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookDefinitionTypeDef",
    "WebhookFilterRuleTypeDef",
)

AWSSessionCredentialsTypeDef = TypedDict(
    "AWSSessionCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
)

AcknowledgeJobInputRequestTypeDef = TypedDict(
    "AcknowledgeJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
    },
)

AcknowledgeJobOutputTypeDef = TypedDict(
    "AcknowledgeJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcknowledgeThirdPartyJobInputRequestTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
        "clientToken": str,
    },
)

AcknowledgeThirdPartyJobOutputTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActionConfigurationPropertyTypeDef = TypedDict(
    "ActionConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
        "type": NotRequired[ActionConfigurationPropertyTypeType],
    },
)

ActionConfigurationTypeDef = TypedDict(
    "ActionConfigurationTypeDef",
    {
        "configuration": NotRequired[Dict[str, str]],
    },
)

ActionContextTypeDef = TypedDict(
    "ActionContextTypeDef",
    {
        "name": NotRequired[str],
        "actionExecutionId": NotRequired[str],
    },
)

ActionDeclarationTypeDef = TypedDict(
    "ActionDeclarationTypeDef",
    {
        "name": str,
        "actionTypeId": "ActionTypeIdTypeDef",
        "runOrder": NotRequired[int],
        "configuration": NotRequired[Mapping[str, str]],
        "outputArtifacts": NotRequired[Sequence["OutputArtifactTypeDef"]],
        "inputArtifacts": NotRequired[Sequence["InputArtifactTypeDef"]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "namespace": NotRequired[str],
    },
)

ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "actionExecutionId": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "stageName": NotRequired[str],
        "actionName": NotRequired[str],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[ActionExecutionStatusType],
        "input": NotRequired["ActionExecutionInputTypeDef"],
        "output": NotRequired["ActionExecutionOutputTypeDef"],
    },
)

ActionExecutionFilterTypeDef = TypedDict(
    "ActionExecutionFilterTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
    },
)

ActionExecutionInputTypeDef = TypedDict(
    "ActionExecutionInputTypeDef",
    {
        "actionTypeId": NotRequired["ActionTypeIdTypeDef"],
        "configuration": NotRequired[Dict[str, str]],
        "resolvedConfiguration": NotRequired[Dict[str, str]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "inputArtifacts": NotRequired[List["ArtifactDetailTypeDef"]],
        "namespace": NotRequired[str],
    },
)

ActionExecutionOutputTypeDef = TypedDict(
    "ActionExecutionOutputTypeDef",
    {
        "outputArtifacts": NotRequired[List["ArtifactDetailTypeDef"]],
        "executionResult": NotRequired["ActionExecutionResultTypeDef"],
        "outputVariables": NotRequired[Dict[str, str]],
    },
)

ActionExecutionResultTypeDef = TypedDict(
    "ActionExecutionResultTypeDef",
    {
        "externalExecutionId": NotRequired[str],
        "externalExecutionSummary": NotRequired[str],
        "externalExecutionUrl": NotRequired[str],
    },
)

ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "actionExecutionId": NotRequired[str],
        "status": NotRequired[ActionExecutionStatusType],
        "summary": NotRequired[str],
        "lastStatusChange": NotRequired[datetime],
        "token": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "externalExecutionId": NotRequired[str],
        "externalExecutionUrl": NotRequired[str],
        "percentComplete": NotRequired[int],
        "errorDetails": NotRequired["ErrorDetailsTypeDef"],
    },
)

ActionRevisionTypeDef = TypedDict(
    "ActionRevisionTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": datetime,
    },
)

ActionStateTypeDef = TypedDict(
    "ActionStateTypeDef",
    {
        "actionName": NotRequired[str],
        "currentRevision": NotRequired["ActionRevisionTypeDef"],
        "latestExecution": NotRequired["ActionExecutionTypeDef"],
        "entityUrl": NotRequired[str],
        "revisionUrl": NotRequired[str],
    },
)

ActionTypeArtifactDetailsTypeDef = TypedDict(
    "ActionTypeArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

ActionTypeDeclarationTypeDef = TypedDict(
    "ActionTypeDeclarationTypeDef",
    {
        "executor": "ActionTypeExecutorTypeDef",
        "id": "ActionTypeIdentifierTypeDef",
        "inputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
        "outputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
        "description": NotRequired[str],
        "permissions": NotRequired["ActionTypePermissionsTypeDef"],
        "properties": NotRequired[List["ActionTypePropertyTypeDef"]],
        "urls": NotRequired["ActionTypeUrlsTypeDef"],
    },
)

ActionTypeExecutorTypeDef = TypedDict(
    "ActionTypeExecutorTypeDef",
    {
        "configuration": "ExecutorConfigurationTypeDef",
        "type": ExecutorTypeType,
        "policyStatementsTemplate": NotRequired[str],
        "jobTimeout": NotRequired[int],
    },
)

ActionTypeIdTypeDef = TypedDict(
    "ActionTypeIdTypeDef",
    {
        "category": ActionCategoryType,
        "owner": ActionOwnerType,
        "provider": str,
        "version": str,
    },
)

ActionTypeIdentifierTypeDef = TypedDict(
    "ActionTypeIdentifierTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

ActionTypePermissionsTypeDef = TypedDict(
    "ActionTypePermissionsTypeDef",
    {
        "allowedAccounts": List[str],
    },
)

ActionTypePropertyTypeDef = TypedDict(
    "ActionTypePropertyTypeDef",
    {
        "name": str,
        "optional": bool,
        "key": bool,
        "noEcho": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
    },
)

ActionTypeSettingsTypeDef = TypedDict(
    "ActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": NotRequired[str],
        "entityUrlTemplate": NotRequired[str],
        "executionUrlTemplate": NotRequired[str],
        "revisionUrlTemplate": NotRequired[str],
    },
)

ActionTypeTypeDef = TypedDict(
    "ActionTypeTypeDef",
    {
        "id": "ActionTypeIdTypeDef",
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
        "settings": NotRequired["ActionTypeSettingsTypeDef"],
        "actionConfigurationProperties": NotRequired[List["ActionConfigurationPropertyTypeDef"]],
    },
)

ActionTypeUrlsTypeDef = TypedDict(
    "ActionTypeUrlsTypeDef",
    {
        "configurationUrl": NotRequired[str],
        "entityUrlTemplate": NotRequired[str],
        "executionUrlTemplate": NotRequired[str],
        "revisionUrlTemplate": NotRequired[str],
    },
)

ApprovalResultTypeDef = TypedDict(
    "ApprovalResultTypeDef",
    {
        "summary": str,
        "status": ApprovalStatusType,
    },
)

ArtifactDetailTypeDef = TypedDict(
    "ArtifactDetailTypeDef",
    {
        "name": NotRequired[str],
        "s3location": NotRequired["S3LocationTypeDef"],
    },
)

ArtifactDetailsTypeDef = TypedDict(
    "ArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {
        "type": NotRequired[Literal["S3"]],
        "s3Location": NotRequired["S3ArtifactLocationTypeDef"],
    },
)

ArtifactRevisionTypeDef = TypedDict(
    "ArtifactRevisionTypeDef",
    {
        "name": NotRequired[str],
        "revisionId": NotRequired[str],
        "revisionChangeIdentifier": NotRequired[str],
        "revisionSummary": NotRequired[str],
        "created": NotRequired[datetime],
        "revisionUrl": NotRequired[str],
    },
)

ArtifactStoreTypeDef = TypedDict(
    "ArtifactStoreTypeDef",
    {
        "type": Literal["S3"],
        "location": str,
        "encryptionKey": NotRequired["EncryptionKeyTypeDef"],
    },
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "name": NotRequired[str],
        "revision": NotRequired[str],
        "location": NotRequired["ArtifactLocationTypeDef"],
    },
)

BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef",
    {
        "name": str,
        "type": Literal["Schedule"],
    },
)

CreateCustomActionTypeInputRequestTypeDef = TypedDict(
    "CreateCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
        "settings": NotRequired["ActionTypeSettingsTypeDef"],
        "configurationProperties": NotRequired[Sequence["ActionConfigurationPropertyTypeDef"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCustomActionTypeOutputTypeDef = TypedDict(
    "CreateCustomActionTypeOutputTypeDef",
    {
        "actionType": "ActionTypeTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePipelineInputRequestTypeDef = TypedDict(
    "CreatePipelineInputRequestTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CurrentRevisionTypeDef = TypedDict(
    "CurrentRevisionTypeDef",
    {
        "revision": str,
        "changeIdentifier": str,
        "created": NotRequired[Union[datetime, str]],
        "revisionSummary": NotRequired[str],
    },
)

DeleteCustomActionTypeInputRequestTypeDef = TypedDict(
    "DeleteCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
    },
)

DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteWebhookInputRequestTypeDef = TypedDict(
    "DeleteWebhookInputRequestTypeDef",
    {
        "name": str,
    },
)

DeregisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": NotRequired[str],
    },
)

DisableStageTransitionInputRequestTypeDef = TypedDict(
    "DisableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
        "reason": str,
    },
)

EnableStageTransitionInputRequestTypeDef = TypedDict(
    "EnableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
    },
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "id": str,
        "type": Literal["KMS"],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "summary": NotRequired[str],
        "externalExecutionId": NotRequired[str],
        "percentComplete": NotRequired[int],
    },
)

ExecutionTriggerTypeDef = TypedDict(
    "ExecutionTriggerTypeDef",
    {
        "triggerType": NotRequired[TriggerTypeType],
        "triggerDetail": NotRequired[str],
    },
)

ExecutorConfigurationTypeDef = TypedDict(
    "ExecutorConfigurationTypeDef",
    {
        "lambdaExecutorConfiguration": NotRequired["LambdaExecutorConfigurationTypeDef"],
        "jobWorkerExecutorConfiguration": NotRequired["JobWorkerExecutorConfigurationTypeDef"],
    },
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "type": FailureTypeType,
        "message": str,
        "externalExecutionId": NotRequired[str],
    },
)

GetActionTypeInputRequestTypeDef = TypedDict(
    "GetActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

GetActionTypeOutputTypeDef = TypedDict(
    "GetActionTypeOutputTypeDef",
    {
        "actionType": "ActionTypeDeclarationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobDetailsInputRequestTypeDef = TypedDict(
    "GetJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
    },
)

GetJobDetailsOutputTypeDef = TypedDict(
    "GetJobDetailsOutputTypeDef",
    {
        "jobDetails": "JobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineExecutionInputRequestTypeDef = TypedDict(
    "GetPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)

GetPipelineExecutionOutputTypeDef = TypedDict(
    "GetPipelineExecutionOutputTypeDef",
    {
        "pipelineExecution": "PipelineExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineInputRequestTypeDef = TypedDict(
    "GetPipelineInputRequestTypeDef",
    {
        "name": str,
        "version": NotRequired[int],
    },
)

GetPipelineOutputTypeDef = TypedDict(
    "GetPipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "metadata": "PipelineMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineStateInputRequestTypeDef = TypedDict(
    "GetPipelineStateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetPipelineStateOutputTypeDef = TypedDict(
    "GetPipelineStateOutputTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List["StageStateTypeDef"],
        "created": datetime,
        "updated": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThirdPartyJobDetailsInputRequestTypeDef = TypedDict(
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)

GetThirdPartyJobDetailsOutputTypeDef = TypedDict(
    "GetThirdPartyJobDetailsOutputTypeDef",
    {
        "jobDetails": "ThirdPartyJobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputArtifactTypeDef = TypedDict(
    "InputArtifactTypeDef",
    {
        "name": str,
    },
)

JobDataTypeDef = TypedDict(
    "JobDataTypeDef",
    {
        "actionTypeId": NotRequired["ActionTypeIdTypeDef"],
        "actionConfiguration": NotRequired["ActionConfigurationTypeDef"],
        "pipelineContext": NotRequired["PipelineContextTypeDef"],
        "inputArtifacts": NotRequired[List["ArtifactTypeDef"]],
        "outputArtifacts": NotRequired[List["ArtifactTypeDef"]],
        "artifactCredentials": NotRequired["AWSSessionCredentialsTypeDef"],
        "continuationToken": NotRequired[str],
        "encryptionKey": NotRequired["EncryptionKeyTypeDef"],
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired["JobDataTypeDef"],
        "accountId": NotRequired[str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired["JobDataTypeDef"],
        "nonce": NotRequired[str],
        "accountId": NotRequired[str],
    },
)

JobWorkerExecutorConfigurationTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationTypeDef",
    {
        "pollingAccounts": NotRequired[List[str]],
        "pollingServicePrincipals": NotRequired[List[str]],
    },
)

LambdaExecutorConfigurationTypeDef = TypedDict(
    "LambdaExecutorConfigurationTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

ListActionExecutionsInputRequestTypeDef = TypedDict(
    "ListActionExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired["ActionExecutionFilterTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListActionExecutionsOutputTypeDef = TypedDict(
    "ListActionExecutionsOutputTypeDef",
    {
        "actionExecutionDetails": List["ActionExecutionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListActionTypesInputRequestTypeDef = TypedDict(
    "ListActionTypesInputRequestTypeDef",
    {
        "actionOwnerFilter": NotRequired[ActionOwnerType],
        "nextToken": NotRequired[str],
        "regionFilter": NotRequired[str],
    },
)

ListActionTypesOutputTypeDef = TypedDict(
    "ListActionTypesOutputTypeDef",
    {
        "actionTypes": List["ActionTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineExecutionsInputRequestTypeDef = TypedDict(
    "ListPipelineExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListPipelineExecutionsOutputTypeDef = TypedDict(
    "ListPipelineExecutionsOutputTypeDef",
    {
        "pipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelines": List["PipelineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWebhookItemTypeDef = TypedDict(
    "ListWebhookItemTypeDef",
    {
        "definition": "WebhookDefinitionTypeDef",
        "url": str,
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[str],
        "lastTriggered": NotRequired[datetime],
        "arn": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
    },
)

ListWebhooksInputRequestTypeDef = TypedDict(
    "ListWebhooksInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWebhooksOutputTypeDef = TypedDict(
    "ListWebhooksOutputTypeDef",
    {
        "webhooks": List["ListWebhookItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputArtifactTypeDef = TypedDict(
    "OutputArtifactTypeDef",
    {
        "name": str,
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

PipelineContextTypeDef = TypedDict(
    "PipelineContextTypeDef",
    {
        "pipelineName": NotRequired[str],
        "stage": NotRequired["StageContextTypeDef"],
        "action": NotRequired["ActionContextTypeDef"],
        "pipelineArn": NotRequired[str],
        "pipelineExecutionId": NotRequired[str],
    },
)

PipelineDeclarationTypeDef = TypedDict(
    "PipelineDeclarationTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": Sequence["StageDeclarationTypeDef"],
        "artifactStore": NotRequired["ArtifactStoreTypeDef"],
        "artifactStores": NotRequired[Mapping[str, "ArtifactStoreTypeDef"]],
        "version": NotRequired[int],
    },
)

PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "status": NotRequired[PipelineExecutionStatusType],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "sourceRevisions": NotRequired[List["SourceRevisionTypeDef"]],
        "trigger": NotRequired["ExecutionTriggerTypeDef"],
        "stopTrigger": NotRequired["StopExecutionTriggerTypeDef"],
    },
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "pipelineName": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "pipelineExecutionId": NotRequired[str],
        "status": NotRequired[PipelineExecutionStatusType],
        "statusSummary": NotRequired[str],
        "artifactRevisions": NotRequired[List["ArtifactRevisionTypeDef"]],
    },
)

PipelineMetadataTypeDef = TypedDict(
    "PipelineMetadataTypeDef",
    {
        "pipelineArn": NotRequired[str],
        "created": NotRequired[datetime],
        "updated": NotRequired[datetime],
    },
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "name": NotRequired[str],
        "version": NotRequired[int],
        "created": NotRequired[datetime],
        "updated": NotRequired[datetime],
    },
)

PollForJobsInputRequestTypeDef = TypedDict(
    "PollForJobsInputRequestTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "maxBatchSize": NotRequired[int],
        "queryParam": NotRequired[Mapping[str, str]],
    },
)

PollForJobsOutputTypeDef = TypedDict(
    "PollForJobsOutputTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PollForThirdPartyJobsInputRequestTypeDef = TypedDict(
    "PollForThirdPartyJobsInputRequestTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "maxBatchSize": NotRequired[int],
    },
)

PollForThirdPartyJobsOutputTypeDef = TypedDict(
    "PollForThirdPartyJobsOutputTypeDef",
    {
        "jobs": List["ThirdPartyJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutActionRevisionInputRequestTypeDef = TypedDict(
    "PutActionRevisionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "actionRevision": "ActionRevisionTypeDef",
    },
)

PutActionRevisionOutputTypeDef = TypedDict(
    "PutActionRevisionOutputTypeDef",
    {
        "newRevision": bool,
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutApprovalResultInputRequestTypeDef = TypedDict(
    "PutApprovalResultInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "result": "ApprovalResultTypeDef",
        "token": str,
    },
)

PutApprovalResultOutputTypeDef = TypedDict(
    "PutApprovalResultOutputTypeDef",
    {
        "approvedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutJobFailureResultInputRequestTypeDef = TypedDict(
    "PutJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "failureDetails": "FailureDetailsTypeDef",
    },
)

PutJobSuccessResultInputRequestTypeDef = TypedDict(
    "PutJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
        "currentRevision": NotRequired["CurrentRevisionTypeDef"],
        "continuationToken": NotRequired[str],
        "executionDetails": NotRequired["ExecutionDetailsTypeDef"],
        "outputVariables": NotRequired[Mapping[str, str]],
    },
)

PutThirdPartyJobFailureResultInputRequestTypeDef = TypedDict(
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "failureDetails": "FailureDetailsTypeDef",
    },
)

PutThirdPartyJobSuccessResultInputRequestTypeDef = TypedDict(
    "PutThirdPartyJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "currentRevision": NotRequired["CurrentRevisionTypeDef"],
        "continuationToken": NotRequired[str],
        "executionDetails": NotRequired["ExecutionDetailsTypeDef"],
    },
)

PutWebhookInputRequestTypeDef = TypedDict(
    "PutWebhookInputRequestTypeDef",
    {
        "webhook": "WebhookDefinitionTypeDef",
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutWebhookOutputTypeDef = TypedDict(
    "PutWebhookOutputTypeDef",
    {
        "webhook": "ListWebhookItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": NotRequired[str],
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

RetryStageExecutionInputRequestTypeDef = TypedDict(
    "RetryStageExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "pipelineExecutionId": str,
        "retryMode": Literal["FAILED_ACTIONS"],
    },
)

RetryStageExecutionOutputTypeDef = TypedDict(
    "RetryStageExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ArtifactLocationTypeDef = TypedDict(
    "S3ArtifactLocationTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
    },
)

SourceRevisionTypeDef = TypedDict(
    "SourceRevisionTypeDef",
    {
        "actionName": str,
        "revisionId": NotRequired[str],
        "revisionSummary": NotRequired[str],
        "revisionUrl": NotRequired[str],
    },
)

StageContextTypeDef = TypedDict(
    "StageContextTypeDef",
    {
        "name": NotRequired[str],
    },
)

StageDeclarationTypeDef = TypedDict(
    "StageDeclarationTypeDef",
    {
        "name": str,
        "actions": Sequence["ActionDeclarationTypeDef"],
        "blockers": NotRequired[Sequence["BlockerDeclarationTypeDef"]],
    },
)

StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": StageExecutionStatusType,
    },
)

StageStateTypeDef = TypedDict(
    "StageStateTypeDef",
    {
        "stageName": NotRequired[str],
        "inboundExecution": NotRequired["StageExecutionTypeDef"],
        "inboundTransitionState": NotRequired["TransitionStateTypeDef"],
        "actionStates": NotRequired[List["ActionStateTypeDef"]],
        "latestExecution": NotRequired["StageExecutionTypeDef"],
    },
)

StartPipelineExecutionInputRequestTypeDef = TypedDict(
    "StartPipelineExecutionInputRequestTypeDef",
    {
        "name": str,
        "clientRequestToken": NotRequired[str],
    },
)

StartPipelineExecutionOutputTypeDef = TypedDict(
    "StartPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExecutionTriggerTypeDef = TypedDict(
    "StopExecutionTriggerTypeDef",
    {
        "reason": NotRequired[str],
    },
)

StopPipelineExecutionInputRequestTypeDef = TypedDict(
    "StopPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
        "abandon": NotRequired[bool],
        "reason": NotRequired[str],
    },
)

StopPipelineExecutionOutputTypeDef = TypedDict(
    "StopPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
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
        "key": str,
        "value": str,
    },
)

ThirdPartyJobDataTypeDef = TypedDict(
    "ThirdPartyJobDataTypeDef",
    {
        "actionTypeId": NotRequired["ActionTypeIdTypeDef"],
        "actionConfiguration": NotRequired["ActionConfigurationTypeDef"],
        "pipelineContext": NotRequired["PipelineContextTypeDef"],
        "inputArtifacts": NotRequired[List["ArtifactTypeDef"]],
        "outputArtifacts": NotRequired[List["ArtifactTypeDef"]],
        "artifactCredentials": NotRequired["AWSSessionCredentialsTypeDef"],
        "continuationToken": NotRequired[str],
        "encryptionKey": NotRequired["EncryptionKeyTypeDef"],
    },
)

ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired["ThirdPartyJobDataTypeDef"],
        "nonce": NotRequired[str],
    },
)

ThirdPartyJobTypeDef = TypedDict(
    "ThirdPartyJobTypeDef",
    {
        "clientId": NotRequired[str],
        "jobId": NotRequired[str],
    },
)

TransitionStateTypeDef = TypedDict(
    "TransitionStateTypeDef",
    {
        "enabled": NotRequired[bool],
        "lastChangedBy": NotRequired[str],
        "lastChangedAt": NotRequired[datetime],
        "disabledReason": NotRequired[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateActionTypeInputRequestTypeDef = TypedDict(
    "UpdateActionTypeInputRequestTypeDef",
    {
        "actionType": "ActionTypeDeclarationTypeDef",
    },
)

UpdatePipelineInputRequestTypeDef = TypedDict(
    "UpdatePipelineInputRequestTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
    },
)

UpdatePipelineOutputTypeDef = TypedDict(
    "UpdatePipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WebhookAuthConfigurationTypeDef = TypedDict(
    "WebhookAuthConfigurationTypeDef",
    {
        "AllowedIPRange": NotRequired[str],
        "SecretToken": NotRequired[str],
    },
)

WebhookDefinitionTypeDef = TypedDict(
    "WebhookDefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List["WebhookFilterRuleTypeDef"],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": "WebhookAuthConfigurationTypeDef",
    },
)

WebhookFilterRuleTypeDef = TypedDict(
    "WebhookFilterRuleTypeDef",
    {
        "jsonPath": str,
        "matchEquals": NotRequired[str],
    },
)
