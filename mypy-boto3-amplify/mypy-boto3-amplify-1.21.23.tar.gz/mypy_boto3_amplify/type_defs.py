"""
Type annotations for amplify service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplify.type_defs import AppTypeDef

    data: AppTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    DomainStatusType,
    JobStatusType,
    JobTypeType,
    PlatformType,
    RepositoryCloneMethodType,
    StageType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppTypeDef",
    "ArtifactTypeDef",
    "AutoBranchCreationConfigTypeDef",
    "BackendEnvironmentTypeDef",
    "BranchTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResultTypeDef",
    "CreateBackendEnvironmentRequestRequestTypeDef",
    "CreateBackendEnvironmentResultTypeDef",
    "CreateBranchRequestRequestTypeDef",
    "CreateBranchResultTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateDomainAssociationRequestRequestTypeDef",
    "CreateDomainAssociationResultTypeDef",
    "CreateWebhookRequestRequestTypeDef",
    "CreateWebhookResultTypeDef",
    "CustomRuleTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppResultTypeDef",
    "DeleteBackendEnvironmentRequestRequestTypeDef",
    "DeleteBackendEnvironmentResultTypeDef",
    "DeleteBranchRequestRequestTypeDef",
    "DeleteBranchResultTypeDef",
    "DeleteDomainAssociationRequestRequestTypeDef",
    "DeleteDomainAssociationResultTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobResultTypeDef",
    "DeleteWebhookRequestRequestTypeDef",
    "DeleteWebhookResultTypeDef",
    "DomainAssociationTypeDef",
    "GenerateAccessLogsRequestRequestTypeDef",
    "GenerateAccessLogsResultTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppResultTypeDef",
    "GetArtifactUrlRequestRequestTypeDef",
    "GetArtifactUrlResultTypeDef",
    "GetBackendEnvironmentRequestRequestTypeDef",
    "GetBackendEnvironmentResultTypeDef",
    "GetBranchRequestRequestTypeDef",
    "GetBranchResultTypeDef",
    "GetDomainAssociationRequestRequestTypeDef",
    "GetDomainAssociationResultTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResultTypeDef",
    "GetWebhookRequestRequestTypeDef",
    "GetWebhookResultTypeDef",
    "JobSummaryTypeDef",
    "JobTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResultTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListArtifactsResultTypeDef",
    "ListBackendEnvironmentsRequestRequestTypeDef",
    "ListBackendEnvironmentsResultTypeDef",
    "ListBranchesRequestRequestTypeDef",
    "ListBranchesResultTypeDef",
    "ListDomainAssociationsRequestRequestTypeDef",
    "ListDomainAssociationsResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebhooksRequestRequestTypeDef",
    "ListWebhooksResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProductionBranchTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StartDeploymentResultTypeDef",
    "StartJobRequestRequestTypeDef",
    "StartJobResultTypeDef",
    "StepTypeDef",
    "StopJobRequestRequestTypeDef",
    "StopJobResultTypeDef",
    "SubDomainSettingTypeDef",
    "SubDomainTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateAppResultTypeDef",
    "UpdateBranchRequestRequestTypeDef",
    "UpdateBranchResultTypeDef",
    "UpdateDomainAssociationRequestRequestTypeDef",
    "UpdateDomainAssociationResultTypeDef",
    "UpdateWebhookRequestRequestTypeDef",
    "UpdateWebhookResultTypeDef",
    "WebhookTypeDef",
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "description": str,
        "repository": str,
        "platform": PlatformType,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "tags": NotRequired[Dict[str, str]],
        "iamServiceRoleArn": NotRequired[str],
        "enableBranchAutoDeletion": NotRequired[bool],
        "basicAuthCredentials": NotRequired[str],
        "customRules": NotRequired[List["CustomRuleTypeDef"]],
        "productionBranch": NotRequired["ProductionBranchTypeDef"],
        "buildSpec": NotRequired[str],
        "customHeaders": NotRequired[str],
        "enableAutoBranchCreation": NotRequired[bool],
        "autoBranchCreationPatterns": NotRequired[List[str]],
        "autoBranchCreationConfig": NotRequired["AutoBranchCreationConfigTypeDef"],
        "repositoryCloneMethod": NotRequired[RepositoryCloneMethodType],
    },
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "artifactFileName": str,
        "artifactId": str,
    },
)

AutoBranchCreationConfigTypeDef = TypedDict(
    "AutoBranchCreationConfigTypeDef",
    {
        "stage": NotRequired[StageType],
        "framework": NotRequired[str],
        "enableAutoBuild": NotRequired[bool],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "basicAuthCredentials": NotRequired[str],
        "enableBasicAuth": NotRequired[bool],
        "enablePerformanceMode": NotRequired[bool],
        "buildSpec": NotRequired[str],
        "enablePullRequestPreview": NotRequired[bool],
        "pullRequestEnvironmentName": NotRequired[str],
    },
)

BackendEnvironmentTypeDef = TypedDict(
    "BackendEnvironmentTypeDef",
    {
        "backendEnvironmentArn": str,
        "environmentName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "stackName": NotRequired[str],
        "deploymentArtifacts": NotRequired[str],
    },
)

BranchTypeDef = TypedDict(
    "BranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "stage": StageType,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "ttl": str,
        "enablePullRequestPreview": bool,
        "tags": NotRequired[Dict[str, str]],
        "enablePerformanceMode": NotRequired[bool],
        "thumbnailUrl": NotRequired[str],
        "basicAuthCredentials": NotRequired[str],
        "buildSpec": NotRequired[str],
        "associatedResources": NotRequired[List[str]],
        "pullRequestEnvironmentName": NotRequired[str],
        "destinationBranch": NotRequired[str],
        "sourceBranch": NotRequired[str],
        "backendEnvironmentArn": NotRequired[str],
    },
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "repository": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "iamServiceRoleArn": NotRequired[str],
        "oauthToken": NotRequired[str],
        "accessToken": NotRequired[str],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "enableBranchAutoBuild": NotRequired[bool],
        "enableBranchAutoDeletion": NotRequired[bool],
        "enableBasicAuth": NotRequired[bool],
        "basicAuthCredentials": NotRequired[str],
        "customRules": NotRequired[Sequence["CustomRuleTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
        "buildSpec": NotRequired[str],
        "customHeaders": NotRequired[str],
        "enableAutoBranchCreation": NotRequired[bool],
        "autoBranchCreationPatterns": NotRequired[Sequence[str]],
        "autoBranchCreationConfig": NotRequired["AutoBranchCreationConfigTypeDef"],
    },
)

CreateAppResultTypeDef = TypedDict(
    "CreateAppResultTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateBackendEnvironmentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "stackName": NotRequired[str],
        "deploymentArtifacts": NotRequired[str],
    },
)

CreateBackendEnvironmentResultTypeDef = TypedDict(
    "CreateBackendEnvironmentResultTypeDef",
    {
        "backendEnvironment": "BackendEnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBranchRequestRequestTypeDef = TypedDict(
    "CreateBranchRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "description": NotRequired[str],
        "stage": NotRequired[StageType],
        "framework": NotRequired[str],
        "enableNotification": NotRequired[bool],
        "enableAutoBuild": NotRequired[bool],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "basicAuthCredentials": NotRequired[str],
        "enableBasicAuth": NotRequired[bool],
        "enablePerformanceMode": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
        "buildSpec": NotRequired[str],
        "ttl": NotRequired[str],
        "displayName": NotRequired[str],
        "enablePullRequestPreview": NotRequired[bool],
        "pullRequestEnvironmentName": NotRequired[str],
        "backendEnvironmentArn": NotRequired[str],
    },
)

CreateBranchResultTypeDef = TypedDict(
    "CreateBranchResultTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "fileMap": NotRequired[Mapping[str, str]],
    },
)

CreateDeploymentResultTypeDef = TypedDict(
    "CreateDeploymentResultTypeDef",
    {
        "jobId": str,
        "fileUploadUrls": Dict[str, str],
        "zipUploadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainAssociationRequestRequestTypeDef = TypedDict(
    "CreateDomainAssociationRequestRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
        "subDomainSettings": Sequence["SubDomainSettingTypeDef"],
        "enableAutoSubDomain": NotRequired[bool],
        "autoSubDomainCreationPatterns": NotRequired[Sequence[str]],
        "autoSubDomainIAMRole": NotRequired[str],
    },
)

CreateDomainAssociationResultTypeDef = TypedDict(
    "CreateDomainAssociationResultTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebhookRequestRequestTypeDef = TypedDict(
    "CreateWebhookRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "description": NotRequired[str],
    },
)

CreateWebhookResultTypeDef = TypedDict(
    "CreateWebhookResultTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomRuleTypeDef = TypedDict(
    "CustomRuleTypeDef",
    {
        "source": str,
        "target": str,
        "status": NotRequired[str],
        "condition": NotRequired[str],
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "appId": str,
    },
)

DeleteAppResultTypeDef = TypedDict(
    "DeleteAppResultTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteBackendEnvironmentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

DeleteBackendEnvironmentResultTypeDef = TypedDict(
    "DeleteBackendEnvironmentResultTypeDef",
    {
        "backendEnvironment": "BackendEnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBranchRequestRequestTypeDef = TypedDict(
    "DeleteBranchRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)

DeleteBranchResultTypeDef = TypedDict(
    "DeleteBranchResultTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainAssociationRequestRequestTypeDef = TypedDict(
    "DeleteDomainAssociationRequestRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
    },
)

DeleteDomainAssociationResultTypeDef = TypedDict(
    "DeleteDomainAssociationResultTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)

DeleteJobResultTypeDef = TypedDict(
    "DeleteJobResultTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebhookRequestRequestTypeDef = TypedDict(
    "DeleteWebhookRequestRequestTypeDef",
    {
        "webhookId": str,
    },
)

DeleteWebhookResultTypeDef = TypedDict(
    "DeleteWebhookResultTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainAssociationTypeDef = TypedDict(
    "DomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": DomainStatusType,
        "statusReason": str,
        "subDomains": List["SubDomainTypeDef"],
        "autoSubDomainCreationPatterns": NotRequired[List[str]],
        "autoSubDomainIAMRole": NotRequired[str],
        "certificateVerificationDNSRecord": NotRequired[str],
    },
)

GenerateAccessLogsRequestRequestTypeDef = TypedDict(
    "GenerateAccessLogsRequestRequestTypeDef",
    {
        "domainName": str,
        "appId": str,
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
    },
)

GenerateAccessLogsResultTypeDef = TypedDict(
    "GenerateAccessLogsResultTypeDef",
    {
        "logUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppResultTypeDef = TypedDict(
    "GetAppResultTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArtifactUrlRequestRequestTypeDef = TypedDict(
    "GetArtifactUrlRequestRequestTypeDef",
    {
        "artifactId": str,
    },
)

GetArtifactUrlResultTypeDef = TypedDict(
    "GetArtifactUrlResultTypeDef",
    {
        "artifactId": str,
        "artifactUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendEnvironmentRequestRequestTypeDef = TypedDict(
    "GetBackendEnvironmentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

GetBackendEnvironmentResultTypeDef = TypedDict(
    "GetBackendEnvironmentResultTypeDef",
    {
        "backendEnvironment": "BackendEnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBranchRequestRequestTypeDef = TypedDict(
    "GetBranchRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)

GetBranchResultTypeDef = TypedDict(
    "GetBranchResultTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainAssociationRequestRequestTypeDef = TypedDict(
    "GetDomainAssociationRequestRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
    },
)

GetDomainAssociationResultTypeDef = TypedDict(
    "GetDomainAssociationResultTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)

GetJobResultTypeDef = TypedDict(
    "GetJobResultTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebhookRequestRequestTypeDef = TypedDict(
    "GetWebhookRequestRequestTypeDef",
    {
        "webhookId": str,
    },
)

GetWebhookResultTypeDef = TypedDict(
    "GetWebhookResultTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": JobStatusType,
        "jobType": JobTypeType,
        "endTime": NotRequired[datetime],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "summary": "JobSummaryTypeDef",
        "steps": List["StepTypeDef"],
    },
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAppsResultTypeDef = TypedDict(
    "ListAppsResultTypeDef",
    {
        "apps": List["AppTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {
        "artifacts": List["ArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackendEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListBackendEnvironmentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListBackendEnvironmentsResultTypeDef = TypedDict(
    "ListBackendEnvironmentsResultTypeDef",
    {
        "backendEnvironments": List["BackendEnvironmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBranchesRequestRequestTypeDef = TypedDict(
    "ListBranchesRequestRequestTypeDef",
    {
        "appId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListBranchesResultTypeDef = TypedDict(
    "ListBranchesResultTypeDef",
    {
        "branches": List["BranchTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainAssociationsRequestRequestTypeDef = TypedDict(
    "ListDomainAssociationsRequestRequestTypeDef",
    {
        "appId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDomainAssociationsResultTypeDef = TypedDict(
    "ListDomainAssociationsResultTypeDef",
    {
        "domainAssociations": List["DomainAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "jobSummaries": List["JobSummaryTypeDef"],
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

ListWebhooksRequestRequestTypeDef = TypedDict(
    "ListWebhooksRequestRequestTypeDef",
    {
        "appId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListWebhooksResultTypeDef = TypedDict(
    "ListWebhooksResultTypeDef",
    {
        "webhooks": List["WebhookTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ProductionBranchTypeDef = TypedDict(
    "ProductionBranchTypeDef",
    {
        "lastDeployTime": NotRequired[datetime],
        "status": NotRequired[str],
        "thumbnailUrl": NotRequired[str],
        "branchName": NotRequired[str],
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

StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": NotRequired[str],
        "sourceUrl": NotRequired[str],
    },
)

StartDeploymentResultTypeDef = TypedDict(
    "StartDeploymentResultTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRequestRequestTypeDef = TypedDict(
    "StartJobRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobType": JobTypeType,
        "jobId": NotRequired[str],
        "jobReason": NotRequired[str],
        "commitId": NotRequired[str],
        "commitMessage": NotRequired[str],
        "commitTime": NotRequired[Union[datetime, str]],
    },
)

StartJobResultTypeDef = TypedDict(
    "StartJobResultTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "stepName": str,
        "startTime": datetime,
        "status": JobStatusType,
        "endTime": datetime,
        "logUrl": NotRequired[str],
        "artifactsUrl": NotRequired[str],
        "testArtifactsUrl": NotRequired[str],
        "testConfigUrl": NotRequired[str],
        "screenshots": NotRequired[Dict[str, str]],
        "statusReason": NotRequired[str],
        "context": NotRequired[str],
    },
)

StopJobRequestRequestTypeDef = TypedDict(
    "StopJobRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)

StopJobResultTypeDef = TypedDict(
    "StopJobResultTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubDomainSettingTypeDef = TypedDict(
    "SubDomainSettingTypeDef",
    {
        "prefix": str,
        "branchName": str,
    },
)

SubDomainTypeDef = TypedDict(
    "SubDomainTypeDef",
    {
        "subDomainSetting": "SubDomainSettingTypeDef",
        "verified": bool,
        "dnsRecord": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "appId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "iamServiceRoleArn": NotRequired[str],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "enableBranchAutoBuild": NotRequired[bool],
        "enableBranchAutoDeletion": NotRequired[bool],
        "enableBasicAuth": NotRequired[bool],
        "basicAuthCredentials": NotRequired[str],
        "customRules": NotRequired[Sequence["CustomRuleTypeDef"]],
        "buildSpec": NotRequired[str],
        "customHeaders": NotRequired[str],
        "enableAutoBranchCreation": NotRequired[bool],
        "autoBranchCreationPatterns": NotRequired[Sequence[str]],
        "autoBranchCreationConfig": NotRequired["AutoBranchCreationConfigTypeDef"],
        "repository": NotRequired[str],
        "oauthToken": NotRequired[str],
        "accessToken": NotRequired[str],
    },
)

UpdateAppResultTypeDef = TypedDict(
    "UpdateAppResultTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBranchRequestRequestTypeDef = TypedDict(
    "UpdateBranchRequestRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "description": NotRequired[str],
        "framework": NotRequired[str],
        "stage": NotRequired[StageType],
        "enableNotification": NotRequired[bool],
        "enableAutoBuild": NotRequired[bool],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "basicAuthCredentials": NotRequired[str],
        "enableBasicAuth": NotRequired[bool],
        "enablePerformanceMode": NotRequired[bool],
        "buildSpec": NotRequired[str],
        "ttl": NotRequired[str],
        "displayName": NotRequired[str],
        "enablePullRequestPreview": NotRequired[bool],
        "pullRequestEnvironmentName": NotRequired[str],
        "backendEnvironmentArn": NotRequired[str],
    },
)

UpdateBranchResultTypeDef = TypedDict(
    "UpdateBranchResultTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainAssociationRequestRequestTypeDef = TypedDict(
    "UpdateDomainAssociationRequestRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
        "enableAutoSubDomain": NotRequired[bool],
        "subDomainSettings": NotRequired[Sequence["SubDomainSettingTypeDef"]],
        "autoSubDomainCreationPatterns": NotRequired[Sequence[str]],
        "autoSubDomainIAMRole": NotRequired[str],
    },
)

UpdateDomainAssociationResultTypeDef = TypedDict(
    "UpdateDomainAssociationResultTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWebhookRequestRequestTypeDef = TypedDict(
    "UpdateWebhookRequestRequestTypeDef",
    {
        "webhookId": str,
        "branchName": NotRequired[str],
        "description": NotRequired[str],
    },
)

UpdateWebhookResultTypeDef = TypedDict(
    "UpdateWebhookResultTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
