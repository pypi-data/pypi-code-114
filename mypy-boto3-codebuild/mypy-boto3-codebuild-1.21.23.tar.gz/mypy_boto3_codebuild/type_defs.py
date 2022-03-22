"""
Type annotations for codebuild service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchDeleteBuildsInputRequestTypeDef

    data: BatchDeleteBuildsInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ArtifactNamespaceType,
    ArtifactPackagingType,
    ArtifactsTypeType,
    AuthTypeType,
    BatchReportModeTypeType,
    BucketOwnerAccessType,
    BuildBatchPhaseTypeType,
    BuildPhaseTypeType,
    CacheModeType,
    CacheTypeType,
    ComputeTypeType,
    EnvironmentTypeType,
    EnvironmentVariableTypeType,
    ImagePullCredentialsTypeType,
    LanguageTypeType,
    LogsConfigStatusTypeType,
    PlatformTypeType,
    ProjectSortByTypeType,
    ProjectVisibilityTypeType,
    ReportCodeCoverageSortByTypeType,
    ReportExportConfigTypeType,
    ReportGroupSortByTypeType,
    ReportGroupStatusTypeType,
    ReportGroupTrendFieldTypeType,
    ReportPackagingTypeType,
    ReportStatusTypeType,
    ReportTypeType,
    RetryBuildBatchTypeType,
    ServerTypeType,
    SharedResourceSortByTypeType,
    SortOrderTypeType,
    SourceTypeType,
    StatusTypeType,
    WebhookBuildTypeType,
    WebhookFilterTypeType,
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
    "BatchDeleteBuildsInputRequestTypeDef",
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesInputRequestTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsInputRequestTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetProjectsInputRequestTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsInputRequestTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsInputRequestTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchFilterTypeDef",
    "BuildBatchPhaseTypeDef",
    "BuildBatchTypeDef",
    "BuildGroupTypeDef",
    "BuildNotDeletedTypeDef",
    "BuildPhaseTypeDef",
    "BuildStatusConfigTypeDef",
    "BuildSummaryTypeDef",
    "BuildTypeDef",
    "CloudWatchLogsConfigTypeDef",
    "CodeCoverageReportSummaryTypeDef",
    "CodeCoverageTypeDef",
    "CreateProjectInputRequestTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateReportGroupInputRequestTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookInputRequestTypeDef",
    "CreateWebhookOutputTypeDef",
    "DebugSessionTypeDef",
    "DeleteBuildBatchInputRequestTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteReportGroupInputRequestTypeDef",
    "DeleteReportInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteSourceCredentialsInputRequestTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DeleteWebhookInputRequestTypeDef",
    "DescribeCodeCoveragesInputRequestTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesInputRequestTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GetReportGroupTrendInputRequestTypeDef",
    "GetReportGroupTrendOutputTypeDef",
    "GetResourcePolicyInputRequestTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GitSubmodulesConfigTypeDef",
    "ImportSourceCredentialsInputRequestTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "InvalidateProjectCacheInputRequestTypeDef",
    "ListBuildBatchesForProjectInputRequestTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesInputRequestTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectInputRequestTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsInputRequestTypeDef",
    "ListBuildsOutputTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsInputRequestTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ListReportsForReportGroupInputRequestTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsInputRequestTypeDef",
    "ListReportsOutputTypeDef",
    "ListSharedProjectsInputRequestTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsInputRequestTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "ListSourceCredentialsOutputTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PhaseContextTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectBadgeTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ProjectCacheTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectSourceTypeDef",
    "ProjectSourceVersionTypeDef",
    "ProjectTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportFilterTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ReportWithRawDataTypeDef",
    "ResolvedArtifactTypeDef",
    "ResponseMetadataTypeDef",
    "RetryBuildBatchInputRequestTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildInputRequestTypeDef",
    "RetryBuildOutputTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "StartBuildBatchInputRequestTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildInputRequestTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildBatchInputRequestTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildInputRequestTypeDef",
    "StopBuildOutputTypeDef",
    "TagTypeDef",
    "TestCaseFilterTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateProjectVisibilityInputRequestTypeDef",
    "UpdateProjectVisibilityOutputTypeDef",
    "UpdateReportGroupInputRequestTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookInputRequestTypeDef",
    "UpdateWebhookOutputTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
)

BatchDeleteBuildsInputRequestTypeDef = TypedDict(
    "BatchDeleteBuildsInputRequestTypeDef",
    {
        "ids": Sequence[str],
    },
)

BatchDeleteBuildsOutputTypeDef = TypedDict(
    "BatchDeleteBuildsOutputTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildBatchesInputRequestTypeDef = TypedDict(
    "BatchGetBuildBatchesInputRequestTypeDef",
    {
        "ids": Sequence[str],
    },
)

BatchGetBuildBatchesOutputTypeDef = TypedDict(
    "BatchGetBuildBatchesOutputTypeDef",
    {
        "buildBatches": List["BuildBatchTypeDef"],
        "buildBatchesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildsInputRequestTypeDef = TypedDict(
    "BatchGetBuildsInputRequestTypeDef",
    {
        "ids": Sequence[str],
    },
)

BatchGetBuildsOutputTypeDef = TypedDict(
    "BatchGetBuildsOutputTypeDef",
    {
        "builds": List["BuildTypeDef"],
        "buildsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetProjectsInputRequestTypeDef = TypedDict(
    "BatchGetProjectsInputRequestTypeDef",
    {
        "names": Sequence[str],
    },
)

BatchGetProjectsOutputTypeDef = TypedDict(
    "BatchGetProjectsOutputTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "projectsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportGroupsInputRequestTypeDef = TypedDict(
    "BatchGetReportGroupsInputRequestTypeDef",
    {
        "reportGroupArns": Sequence[str],
    },
)

BatchGetReportGroupsOutputTypeDef = TypedDict(
    "BatchGetReportGroupsOutputTypeDef",
    {
        "reportGroups": List["ReportGroupTypeDef"],
        "reportGroupsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportsInputRequestTypeDef = TypedDict(
    "BatchGetReportsInputRequestTypeDef",
    {
        "reportArns": Sequence[str],
    },
)

BatchGetReportsOutputTypeDef = TypedDict(
    "BatchGetReportsOutputTypeDef",
    {
        "reports": List["ReportTypeDef"],
        "reportsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchRestrictionsTypeDef = TypedDict(
    "BatchRestrictionsTypeDef",
    {
        "maximumBuildsAllowed": NotRequired[int],
        "computeTypesAllowed": NotRequired[List[str]],
    },
)

BuildArtifactsTypeDef = TypedDict(
    "BuildArtifactsTypeDef",
    {
        "location": NotRequired[str],
        "sha256sum": NotRequired[str],
        "md5sum": NotRequired[str],
        "overrideArtifactName": NotRequired[bool],
        "encryptionDisabled": NotRequired[bool],
        "artifactIdentifier": NotRequired[str],
        "bucketOwnerAccess": NotRequired[BucketOwnerAccessType],
    },
)

BuildBatchFilterTypeDef = TypedDict(
    "BuildBatchFilterTypeDef",
    {
        "status": NotRequired[StatusTypeType],
    },
)

BuildBatchPhaseTypeDef = TypedDict(
    "BuildBatchPhaseTypeDef",
    {
        "phaseType": NotRequired[BuildBatchPhaseTypeType],
        "phaseStatus": NotRequired[StatusTypeType],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "durationInSeconds": NotRequired[int],
        "contexts": NotRequired[List["PhaseContextTypeDef"]],
    },
)

BuildBatchTypeDef = TypedDict(
    "BuildBatchTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "currentPhase": NotRequired[str],
        "buildBatchStatus": NotRequired[StatusTypeType],
        "sourceVersion": NotRequired[str],
        "resolvedSourceVersion": NotRequired[str],
        "projectName": NotRequired[str],
        "phases": NotRequired[List["BuildBatchPhaseTypeDef"]],
        "source": NotRequired["ProjectSourceTypeDef"],
        "secondarySources": NotRequired[List["ProjectSourceTypeDef"]],
        "secondarySourceVersions": NotRequired[List["ProjectSourceVersionTypeDef"]],
        "artifacts": NotRequired["BuildArtifactsTypeDef"],
        "secondaryArtifacts": NotRequired[List["BuildArtifactsTypeDef"]],
        "cache": NotRequired["ProjectCacheTypeDef"],
        "environment": NotRequired["ProjectEnvironmentTypeDef"],
        "serviceRole": NotRequired[str],
        "logConfig": NotRequired["LogsConfigTypeDef"],
        "buildTimeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "complete": NotRequired[bool],
        "initiator": NotRequired[str],
        "vpcConfig": NotRequired["VpcConfigTypeDef"],
        "encryptionKey": NotRequired[str],
        "buildBatchNumber": NotRequired[int],
        "fileSystemLocations": NotRequired[List["ProjectFileSystemLocationTypeDef"]],
        "buildBatchConfig": NotRequired["ProjectBuildBatchConfigTypeDef"],
        "buildGroups": NotRequired[List["BuildGroupTypeDef"]],
        "debugSessionEnabled": NotRequired[bool],
    },
)

BuildGroupTypeDef = TypedDict(
    "BuildGroupTypeDef",
    {
        "identifier": NotRequired[str],
        "dependsOn": NotRequired[List[str]],
        "ignoreFailure": NotRequired[bool],
        "currentBuildSummary": NotRequired["BuildSummaryTypeDef"],
        "priorBuildSummaryList": NotRequired[List["BuildSummaryTypeDef"]],
    },
)

BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef",
    {
        "id": NotRequired[str],
        "statusCode": NotRequired[str],
    },
)

BuildPhaseTypeDef = TypedDict(
    "BuildPhaseTypeDef",
    {
        "phaseType": NotRequired[BuildPhaseTypeType],
        "phaseStatus": NotRequired[StatusTypeType],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "durationInSeconds": NotRequired[int],
        "contexts": NotRequired[List["PhaseContextTypeDef"]],
    },
)

BuildStatusConfigTypeDef = TypedDict(
    "BuildStatusConfigTypeDef",
    {
        "context": NotRequired[str],
        "targetUrl": NotRequired[str],
    },
)

BuildSummaryTypeDef = TypedDict(
    "BuildSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "requestedOn": NotRequired[datetime],
        "buildStatus": NotRequired[StatusTypeType],
        "primaryArtifact": NotRequired["ResolvedArtifactTypeDef"],
        "secondaryArtifacts": NotRequired[List["ResolvedArtifactTypeDef"]],
    },
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "buildNumber": NotRequired[int],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "currentPhase": NotRequired[str],
        "buildStatus": NotRequired[StatusTypeType],
        "sourceVersion": NotRequired[str],
        "resolvedSourceVersion": NotRequired[str],
        "projectName": NotRequired[str],
        "phases": NotRequired[List["BuildPhaseTypeDef"]],
        "source": NotRequired["ProjectSourceTypeDef"],
        "secondarySources": NotRequired[List["ProjectSourceTypeDef"]],
        "secondarySourceVersions": NotRequired[List["ProjectSourceVersionTypeDef"]],
        "artifacts": NotRequired["BuildArtifactsTypeDef"],
        "secondaryArtifacts": NotRequired[List["BuildArtifactsTypeDef"]],
        "cache": NotRequired["ProjectCacheTypeDef"],
        "environment": NotRequired["ProjectEnvironmentTypeDef"],
        "serviceRole": NotRequired[str],
        "logs": NotRequired["LogsLocationTypeDef"],
        "timeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "buildComplete": NotRequired[bool],
        "initiator": NotRequired[str],
        "vpcConfig": NotRequired["VpcConfigTypeDef"],
        "networkInterface": NotRequired["NetworkInterfaceTypeDef"],
        "encryptionKey": NotRequired[str],
        "exportedEnvironmentVariables": NotRequired[List["ExportedEnvironmentVariableTypeDef"]],
        "reportArns": NotRequired[List[str]],
        "fileSystemLocations": NotRequired[List["ProjectFileSystemLocationTypeDef"]],
        "debugSession": NotRequired["DebugSessionTypeDef"],
        "buildBatchArn": NotRequired[str],
    },
)

CloudWatchLogsConfigTypeDef = TypedDict(
    "CloudWatchLogsConfigTypeDef",
    {
        "status": LogsConfigStatusTypeType,
        "groupName": NotRequired[str],
        "streamName": NotRequired[str],
    },
)

CodeCoverageReportSummaryTypeDef = TypedDict(
    "CodeCoverageReportSummaryTypeDef",
    {
        "lineCoveragePercentage": NotRequired[float],
        "linesCovered": NotRequired[int],
        "linesMissed": NotRequired[int],
        "branchCoveragePercentage": NotRequired[float],
        "branchesCovered": NotRequired[int],
        "branchesMissed": NotRequired[int],
    },
)

CodeCoverageTypeDef = TypedDict(
    "CodeCoverageTypeDef",
    {
        "id": NotRequired[str],
        "reportARN": NotRequired[str],
        "filePath": NotRequired[str],
        "lineCoveragePercentage": NotRequired[float],
        "linesCovered": NotRequired[int],
        "linesMissed": NotRequired[int],
        "branchCoveragePercentage": NotRequired[float],
        "branchesCovered": NotRequired[int],
        "branchesMissed": NotRequired[int],
        "expired": NotRequired[datetime],
    },
)

CreateProjectInputRequestTypeDef = TypedDict(
    "CreateProjectInputRequestTypeDef",
    {
        "name": str,
        "source": "ProjectSourceTypeDef",
        "artifacts": "ProjectArtifactsTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "description": NotRequired[str],
        "secondarySources": NotRequired[Sequence["ProjectSourceTypeDef"]],
        "sourceVersion": NotRequired[str],
        "secondarySourceVersions": NotRequired[Sequence["ProjectSourceVersionTypeDef"]],
        "secondaryArtifacts": NotRequired[Sequence["ProjectArtifactsTypeDef"]],
        "cache": NotRequired["ProjectCacheTypeDef"],
        "timeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "encryptionKey": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "vpcConfig": NotRequired["VpcConfigTypeDef"],
        "badgeEnabled": NotRequired[bool],
        "logsConfig": NotRequired["LogsConfigTypeDef"],
        "fileSystemLocations": NotRequired[Sequence["ProjectFileSystemLocationTypeDef"]],
        "buildBatchConfig": NotRequired["ProjectBuildBatchConfigTypeDef"],
        "concurrentBuildLimit": NotRequired[int],
    },
)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReportGroupInputRequestTypeDef = TypedDict(
    "CreateReportGroupInputRequestTypeDef",
    {
        "name": str,
        "type": ReportTypeType,
        "exportConfig": "ReportExportConfigTypeDef",
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateReportGroupOutputTypeDef = TypedDict(
    "CreateReportGroupOutputTypeDef",
    {
        "reportGroup": "ReportGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebhookInputRequestTypeDef = TypedDict(
    "CreateWebhookInputRequestTypeDef",
    {
        "projectName": str,
        "branchFilter": NotRequired[str],
        "filterGroups": NotRequired[Sequence[Sequence["WebhookFilterTypeDef"]]],
        "buildType": NotRequired[WebhookBuildTypeType],
    },
)

CreateWebhookOutputTypeDef = TypedDict(
    "CreateWebhookOutputTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DebugSessionTypeDef = TypedDict(
    "DebugSessionTypeDef",
    {
        "sessionEnabled": NotRequired[bool],
        "sessionTarget": NotRequired[str],
    },
)

DeleteBuildBatchInputRequestTypeDef = TypedDict(
    "DeleteBuildBatchInputRequestTypeDef",
    {
        "id": str,
    },
)

DeleteBuildBatchOutputTypeDef = TypedDict(
    "DeleteBuildBatchOutputTypeDef",
    {
        "statusCode": str,
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteReportGroupInputRequestTypeDef = TypedDict(
    "DeleteReportGroupInputRequestTypeDef",
    {
        "arn": str,
        "deleteReports": NotRequired[bool],
    },
)

DeleteReportInputRequestTypeDef = TypedDict(
    "DeleteReportInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DeleteSourceCredentialsInputRequestTypeDef = TypedDict(
    "DeleteSourceCredentialsInputRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteSourceCredentialsOutputTypeDef = TypedDict(
    "DeleteSourceCredentialsOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebhookInputRequestTypeDef = TypedDict(
    "DeleteWebhookInputRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribeCodeCoveragesInputRequestTypeDef = TypedDict(
    "DescribeCodeCoveragesInputRequestTypeDef",
    {
        "reportArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "sortOrder": NotRequired[SortOrderTypeType],
        "sortBy": NotRequired[ReportCodeCoverageSortByTypeType],
        "minLineCoveragePercentage": NotRequired[float],
        "maxLineCoveragePercentage": NotRequired[float],
    },
)

DescribeCodeCoveragesOutputTypeDef = TypedDict(
    "DescribeCodeCoveragesOutputTypeDef",
    {
        "nextToken": str,
        "codeCoverages": List["CodeCoverageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestCasesInputRequestTypeDef = TypedDict(
    "DescribeTestCasesInputRequestTypeDef",
    {
        "reportArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired["TestCaseFilterTypeDef"],
    },
)

DescribeTestCasesOutputTypeDef = TypedDict(
    "DescribeTestCasesOutputTypeDef",
    {
        "nextToken": str,
        "testCases": List["TestCaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentImageTypeDef = TypedDict(
    "EnvironmentImageTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "versions": NotRequired[List[str]],
    },
)

EnvironmentLanguageTypeDef = TypedDict(
    "EnvironmentLanguageTypeDef",
    {
        "language": NotRequired[LanguageTypeType],
        "images": NotRequired[List["EnvironmentImageTypeDef"]],
    },
)

EnvironmentPlatformTypeDef = TypedDict(
    "EnvironmentPlatformTypeDef",
    {
        "platform": NotRequired[PlatformTypeType],
        "languages": NotRequired[List["EnvironmentLanguageTypeDef"]],
    },
)

EnvironmentVariableTypeDef = TypedDict(
    "EnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
        "type": NotRequired[EnvironmentVariableTypeType],
    },
)

ExportedEnvironmentVariableTypeDef = TypedDict(
    "ExportedEnvironmentVariableTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)

GetReportGroupTrendInputRequestTypeDef = TypedDict(
    "GetReportGroupTrendInputRequestTypeDef",
    {
        "reportGroupArn": str,
        "trendField": ReportGroupTrendFieldTypeType,
        "numOfReports": NotRequired[int],
    },
)

GetReportGroupTrendOutputTypeDef = TypedDict(
    "GetReportGroupTrendOutputTypeDef",
    {
        "stats": "ReportGroupTrendStatsTypeDef",
        "rawData": List["ReportWithRawDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyInputRequestTypeDef = TypedDict(
    "GetResourcePolicyInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
    {
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitSubmodulesConfigTypeDef = TypedDict(
    "GitSubmodulesConfigTypeDef",
    {
        "fetchSubmodules": bool,
    },
)

ImportSourceCredentialsInputRequestTypeDef = TypedDict(
    "ImportSourceCredentialsInputRequestTypeDef",
    {
        "token": str,
        "serverType": ServerTypeType,
        "authType": AuthTypeType,
        "username": NotRequired[str],
        "shouldOverwrite": NotRequired[bool],
    },
)

ImportSourceCredentialsOutputTypeDef = TypedDict(
    "ImportSourceCredentialsOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvalidateProjectCacheInputRequestTypeDef = TypedDict(
    "InvalidateProjectCacheInputRequestTypeDef",
    {
        "projectName": str,
    },
)

ListBuildBatchesForProjectInputRequestTypeDef = TypedDict(
    "ListBuildBatchesForProjectInputRequestTypeDef",
    {
        "projectName": NotRequired[str],
        "filter": NotRequired["BuildBatchFilterTypeDef"],
        "maxResults": NotRequired[int],
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)

ListBuildBatchesForProjectOutputTypeDef = TypedDict(
    "ListBuildBatchesForProjectOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildBatchesInputRequestTypeDef = TypedDict(
    "ListBuildBatchesInputRequestTypeDef",
    {
        "filter": NotRequired["BuildBatchFilterTypeDef"],
        "maxResults": NotRequired[int],
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)

ListBuildBatchesOutputTypeDef = TypedDict(
    "ListBuildBatchesOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsForProjectInputRequestTypeDef = TypedDict(
    "ListBuildsForProjectInputRequestTypeDef",
    {
        "projectName": str,
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)

ListBuildsForProjectOutputTypeDef = TypedDict(
    "ListBuildsForProjectOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsInputRequestTypeDef = TypedDict(
    "ListBuildsInputRequestTypeDef",
    {
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCuratedEnvironmentImagesOutputTypeDef = TypedDict(
    "ListCuratedEnvironmentImagesOutputTypeDef",
    {
        "platforms": List["EnvironmentPlatformTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "sortBy": NotRequired[ProjectSortByTypeType],
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportGroupsInputRequestTypeDef = TypedDict(
    "ListReportGroupsInputRequestTypeDef",
    {
        "sortOrder": NotRequired[SortOrderTypeType],
        "sortBy": NotRequired[ReportGroupSortByTypeType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListReportGroupsOutputTypeDef = TypedDict(
    "ListReportGroupsOutputTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsForReportGroupInputRequestTypeDef = TypedDict(
    "ListReportsForReportGroupInputRequestTypeDef",
    {
        "reportGroupArn": str,
        "nextToken": NotRequired[str],
        "sortOrder": NotRequired[SortOrderTypeType],
        "maxResults": NotRequired[int],
        "filter": NotRequired["ReportFilterTypeDef"],
    },
)

ListReportsForReportGroupOutputTypeDef = TypedDict(
    "ListReportsForReportGroupOutputTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsInputRequestTypeDef = TypedDict(
    "ListReportsInputRequestTypeDef",
    {
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired["ReportFilterTypeDef"],
    },
)

ListReportsOutputTypeDef = TypedDict(
    "ListReportsOutputTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedProjectsInputRequestTypeDef = TypedDict(
    "ListSharedProjectsInputRequestTypeDef",
    {
        "sortBy": NotRequired[SharedResourceSortByTypeType],
        "sortOrder": NotRequired[SortOrderTypeType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSharedProjectsOutputTypeDef = TypedDict(
    "ListSharedProjectsOutputTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedReportGroupsInputRequestTypeDef = TypedDict(
    "ListSharedReportGroupsInputRequestTypeDef",
    {
        "sortOrder": NotRequired[SortOrderTypeType],
        "sortBy": NotRequired[SharedResourceSortByTypeType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListSharedReportGroupsOutputTypeDef = TypedDict(
    "ListSharedReportGroupsOutputTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSourceCredentialsOutputTypeDef = TypedDict(
    "ListSourceCredentialsOutputTypeDef",
    {
        "sourceCredentialsInfos": List["SourceCredentialsInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogsConfigTypeDef = TypedDict(
    "LogsConfigTypeDef",
    {
        "cloudWatchLogs": NotRequired["CloudWatchLogsConfigTypeDef"],
        "s3Logs": NotRequired["S3LogsConfigTypeDef"],
    },
)

LogsLocationTypeDef = TypedDict(
    "LogsLocationTypeDef",
    {
        "groupName": NotRequired[str],
        "streamName": NotRequired[str],
        "deepLink": NotRequired[str],
        "s3DeepLink": NotRequired[str],
        "cloudWatchLogsArn": NotRequired[str],
        "s3LogsArn": NotRequired[str],
        "cloudWatchLogs": NotRequired["CloudWatchLogsConfigTypeDef"],
        "s3Logs": NotRequired["S3LogsConfigTypeDef"],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "subnetId": NotRequired[str],
        "networkInterfaceId": NotRequired[str],
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

PhaseContextTypeDef = TypedDict(
    "PhaseContextTypeDef",
    {
        "statusCode": NotRequired[str],
        "message": NotRequired[str],
    },
)

ProjectArtifactsTypeDef = TypedDict(
    "ProjectArtifactsTypeDef",
    {
        "type": ArtifactsTypeType,
        "location": NotRequired[str],
        "path": NotRequired[str],
        "namespaceType": NotRequired[ArtifactNamespaceType],
        "name": NotRequired[str],
        "packaging": NotRequired[ArtifactPackagingType],
        "overrideArtifactName": NotRequired[bool],
        "encryptionDisabled": NotRequired[bool],
        "artifactIdentifier": NotRequired[str],
        "bucketOwnerAccess": NotRequired[BucketOwnerAccessType],
    },
)

ProjectBadgeTypeDef = TypedDict(
    "ProjectBadgeTypeDef",
    {
        "badgeEnabled": NotRequired[bool],
        "badgeRequestUrl": NotRequired[str],
    },
)

ProjectBuildBatchConfigTypeDef = TypedDict(
    "ProjectBuildBatchConfigTypeDef",
    {
        "serviceRole": NotRequired[str],
        "combineArtifacts": NotRequired[bool],
        "restrictions": NotRequired["BatchRestrictionsTypeDef"],
        "timeoutInMins": NotRequired[int],
        "batchReportMode": NotRequired[BatchReportModeTypeType],
    },
)

ProjectCacheTypeDef = TypedDict(
    "ProjectCacheTypeDef",
    {
        "type": CacheTypeType,
        "location": NotRequired[str],
        "modes": NotRequired[List[CacheModeType]],
    },
)

ProjectEnvironmentTypeDef = TypedDict(
    "ProjectEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "image": str,
        "computeType": ComputeTypeType,
        "environmentVariables": NotRequired[List["EnvironmentVariableTypeDef"]],
        "privilegedMode": NotRequired[bool],
        "certificate": NotRequired[str],
        "registryCredential": NotRequired["RegistryCredentialTypeDef"],
        "imagePullCredentialsType": NotRequired[ImagePullCredentialsTypeType],
    },
)

ProjectFileSystemLocationTypeDef = TypedDict(
    "ProjectFileSystemLocationTypeDef",
    {
        "type": NotRequired[Literal["EFS"]],
        "location": NotRequired[str],
        "mountPoint": NotRequired[str],
        "identifier": NotRequired[str],
        "mountOptions": NotRequired[str],
    },
)

ProjectSourceTypeDef = TypedDict(
    "ProjectSourceTypeDef",
    {
        "type": SourceTypeType,
        "location": NotRequired[str],
        "gitCloneDepth": NotRequired[int],
        "gitSubmodulesConfig": NotRequired["GitSubmodulesConfigTypeDef"],
        "buildspec": NotRequired[str],
        "auth": NotRequired["SourceAuthTypeDef"],
        "reportBuildStatus": NotRequired[bool],
        "buildStatusConfig": NotRequired["BuildStatusConfigTypeDef"],
        "insecureSsl": NotRequired[bool],
        "sourceIdentifier": NotRequired[str],
    },
)

ProjectSourceVersionTypeDef = TypedDict(
    "ProjectSourceVersionTypeDef",
    {
        "sourceIdentifier": str,
        "sourceVersion": str,
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "source": NotRequired["ProjectSourceTypeDef"],
        "secondarySources": NotRequired[List["ProjectSourceTypeDef"]],
        "sourceVersion": NotRequired[str],
        "secondarySourceVersions": NotRequired[List["ProjectSourceVersionTypeDef"]],
        "artifacts": NotRequired["ProjectArtifactsTypeDef"],
        "secondaryArtifacts": NotRequired[List["ProjectArtifactsTypeDef"]],
        "cache": NotRequired["ProjectCacheTypeDef"],
        "environment": NotRequired["ProjectEnvironmentTypeDef"],
        "serviceRole": NotRequired[str],
        "timeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "encryptionKey": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
        "created": NotRequired[datetime],
        "lastModified": NotRequired[datetime],
        "webhook": NotRequired["WebhookTypeDef"],
        "vpcConfig": NotRequired["VpcConfigTypeDef"],
        "badge": NotRequired["ProjectBadgeTypeDef"],
        "logsConfig": NotRequired["LogsConfigTypeDef"],
        "fileSystemLocations": NotRequired[List["ProjectFileSystemLocationTypeDef"]],
        "buildBatchConfig": NotRequired["ProjectBuildBatchConfigTypeDef"],
        "concurrentBuildLimit": NotRequired[int],
        "projectVisibility": NotRequired[ProjectVisibilityTypeType],
        "publicProjectAlias": NotRequired[str],
        "resourceAccessRole": NotRequired[str],
    },
)

PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistryCredentialTypeDef = TypedDict(
    "RegistryCredentialTypeDef",
    {
        "credential": str,
        "credentialProvider": Literal["SECRETS_MANAGER"],
    },
)

ReportExportConfigTypeDef = TypedDict(
    "ReportExportConfigTypeDef",
    {
        "exportConfigType": NotRequired[ReportExportConfigTypeType],
        "s3Destination": NotRequired["S3ReportExportConfigTypeDef"],
    },
)

ReportFilterTypeDef = TypedDict(
    "ReportFilterTypeDef",
    {
        "status": NotRequired[ReportStatusTypeType],
    },
)

ReportGroupTrendStatsTypeDef = TypedDict(
    "ReportGroupTrendStatsTypeDef",
    {
        "average": NotRequired[str],
        "max": NotRequired[str],
        "min": NotRequired[str],
    },
)

ReportGroupTypeDef = TypedDict(
    "ReportGroupTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ReportTypeType],
        "exportConfig": NotRequired["ReportExportConfigTypeDef"],
        "created": NotRequired[datetime],
        "lastModified": NotRequired[datetime],
        "tags": NotRequired[List["TagTypeDef"]],
        "status": NotRequired[ReportGroupStatusTypeType],
    },
)

ReportTypeDef = TypedDict(
    "ReportTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[ReportTypeType],
        "name": NotRequired[str],
        "reportGroupArn": NotRequired[str],
        "executionId": NotRequired[str],
        "status": NotRequired[ReportStatusTypeType],
        "created": NotRequired[datetime],
        "expired": NotRequired[datetime],
        "exportConfig": NotRequired["ReportExportConfigTypeDef"],
        "truncated": NotRequired[bool],
        "testSummary": NotRequired["TestReportSummaryTypeDef"],
        "codeCoverageSummary": NotRequired["CodeCoverageReportSummaryTypeDef"],
    },
)

ReportWithRawDataTypeDef = TypedDict(
    "ReportWithRawDataTypeDef",
    {
        "reportArn": NotRequired[str],
        "data": NotRequired[str],
    },
)

ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {
        "type": NotRequired[ArtifactsTypeType],
        "location": NotRequired[str],
        "identifier": NotRequired[str],
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

RetryBuildBatchInputRequestTypeDef = TypedDict(
    "RetryBuildBatchInputRequestTypeDef",
    {
        "id": NotRequired[str],
        "idempotencyToken": NotRequired[str],
        "retryType": NotRequired[RetryBuildBatchTypeType],
    },
)

RetryBuildBatchOutputTypeDef = TypedDict(
    "RetryBuildBatchOutputTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryBuildInputRequestTypeDef = TypedDict(
    "RetryBuildInputRequestTypeDef",
    {
        "id": NotRequired[str],
        "idempotencyToken": NotRequired[str],
    },
)

RetryBuildOutputTypeDef = TypedDict(
    "RetryBuildOutputTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3LogsConfigTypeDef = TypedDict(
    "S3LogsConfigTypeDef",
    {
        "status": LogsConfigStatusTypeType,
        "location": NotRequired[str],
        "encryptionDisabled": NotRequired[bool],
        "bucketOwnerAccess": NotRequired[BucketOwnerAccessType],
    },
)

S3ReportExportConfigTypeDef = TypedDict(
    "S3ReportExportConfigTypeDef",
    {
        "bucket": NotRequired[str],
        "bucketOwner": NotRequired[str],
        "path": NotRequired[str],
        "packaging": NotRequired[ReportPackagingTypeType],
        "encryptionKey": NotRequired[str],
        "encryptionDisabled": NotRequired[bool],
    },
)

SourceAuthTypeDef = TypedDict(
    "SourceAuthTypeDef",
    {
        "type": Literal["OAUTH"],
        "resource": NotRequired[str],
    },
)

SourceCredentialsInfoTypeDef = TypedDict(
    "SourceCredentialsInfoTypeDef",
    {
        "arn": NotRequired[str],
        "serverType": NotRequired[ServerTypeType],
        "authType": NotRequired[AuthTypeType],
    },
)

StartBuildBatchInputRequestTypeDef = TypedDict(
    "StartBuildBatchInputRequestTypeDef",
    {
        "projectName": str,
        "secondarySourcesOverride": NotRequired[Sequence["ProjectSourceTypeDef"]],
        "secondarySourcesVersionOverride": NotRequired[Sequence["ProjectSourceVersionTypeDef"]],
        "sourceVersion": NotRequired[str],
        "artifactsOverride": NotRequired["ProjectArtifactsTypeDef"],
        "secondaryArtifactsOverride": NotRequired[Sequence["ProjectArtifactsTypeDef"]],
        "environmentVariablesOverride": NotRequired[Sequence["EnvironmentVariableTypeDef"]],
        "sourceTypeOverride": NotRequired[SourceTypeType],
        "sourceLocationOverride": NotRequired[str],
        "sourceAuthOverride": NotRequired["SourceAuthTypeDef"],
        "gitCloneDepthOverride": NotRequired[int],
        "gitSubmodulesConfigOverride": NotRequired["GitSubmodulesConfigTypeDef"],
        "buildspecOverride": NotRequired[str],
        "insecureSslOverride": NotRequired[bool],
        "reportBuildBatchStatusOverride": NotRequired[bool],
        "environmentTypeOverride": NotRequired[EnvironmentTypeType],
        "imageOverride": NotRequired[str],
        "computeTypeOverride": NotRequired[ComputeTypeType],
        "certificateOverride": NotRequired[str],
        "cacheOverride": NotRequired["ProjectCacheTypeDef"],
        "serviceRoleOverride": NotRequired[str],
        "privilegedModeOverride": NotRequired[bool],
        "buildTimeoutInMinutesOverride": NotRequired[int],
        "queuedTimeoutInMinutesOverride": NotRequired[int],
        "encryptionKeyOverride": NotRequired[str],
        "idempotencyToken": NotRequired[str],
        "logsConfigOverride": NotRequired["LogsConfigTypeDef"],
        "registryCredentialOverride": NotRequired["RegistryCredentialTypeDef"],
        "imagePullCredentialsTypeOverride": NotRequired[ImagePullCredentialsTypeType],
        "buildBatchConfigOverride": NotRequired["ProjectBuildBatchConfigTypeDef"],
        "debugSessionEnabled": NotRequired[bool],
    },
)

StartBuildBatchOutputTypeDef = TypedDict(
    "StartBuildBatchOutputTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartBuildInputRequestTypeDef = TypedDict(
    "StartBuildInputRequestTypeDef",
    {
        "projectName": str,
        "secondarySourcesOverride": NotRequired[Sequence["ProjectSourceTypeDef"]],
        "secondarySourcesVersionOverride": NotRequired[Sequence["ProjectSourceVersionTypeDef"]],
        "sourceVersion": NotRequired[str],
        "artifactsOverride": NotRequired["ProjectArtifactsTypeDef"],
        "secondaryArtifactsOverride": NotRequired[Sequence["ProjectArtifactsTypeDef"]],
        "environmentVariablesOverride": NotRequired[Sequence["EnvironmentVariableTypeDef"]],
        "sourceTypeOverride": NotRequired[SourceTypeType],
        "sourceLocationOverride": NotRequired[str],
        "sourceAuthOverride": NotRequired["SourceAuthTypeDef"],
        "gitCloneDepthOverride": NotRequired[int],
        "gitSubmodulesConfigOverride": NotRequired["GitSubmodulesConfigTypeDef"],
        "buildspecOverride": NotRequired[str],
        "insecureSslOverride": NotRequired[bool],
        "reportBuildStatusOverride": NotRequired[bool],
        "buildStatusConfigOverride": NotRequired["BuildStatusConfigTypeDef"],
        "environmentTypeOverride": NotRequired[EnvironmentTypeType],
        "imageOverride": NotRequired[str],
        "computeTypeOverride": NotRequired[ComputeTypeType],
        "certificateOverride": NotRequired[str],
        "cacheOverride": NotRequired["ProjectCacheTypeDef"],
        "serviceRoleOverride": NotRequired[str],
        "privilegedModeOverride": NotRequired[bool],
        "timeoutInMinutesOverride": NotRequired[int],
        "queuedTimeoutInMinutesOverride": NotRequired[int],
        "encryptionKeyOverride": NotRequired[str],
        "idempotencyToken": NotRequired[str],
        "logsConfigOverride": NotRequired["LogsConfigTypeDef"],
        "registryCredentialOverride": NotRequired["RegistryCredentialTypeDef"],
        "imagePullCredentialsTypeOverride": NotRequired[ImagePullCredentialsTypeType],
        "debugSessionEnabled": NotRequired[bool],
    },
)

StartBuildOutputTypeDef = TypedDict(
    "StartBuildOutputTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildBatchInputRequestTypeDef = TypedDict(
    "StopBuildBatchInputRequestTypeDef",
    {
        "id": str,
    },
)

StopBuildBatchOutputTypeDef = TypedDict(
    "StopBuildBatchOutputTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildInputRequestTypeDef = TypedDict(
    "StopBuildInputRequestTypeDef",
    {
        "id": str,
    },
)

StopBuildOutputTypeDef = TypedDict(
    "StopBuildOutputTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

TestCaseFilterTypeDef = TypedDict(
    "TestCaseFilterTypeDef",
    {
        "status": NotRequired[str],
        "keyword": NotRequired[str],
    },
)

TestCaseTypeDef = TypedDict(
    "TestCaseTypeDef",
    {
        "reportArn": NotRequired[str],
        "testRawDataPath": NotRequired[str],
        "prefix": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[str],
        "durationInNanoSeconds": NotRequired[int],
        "message": NotRequired[str],
        "expired": NotRequired[datetime],
    },
)

TestReportSummaryTypeDef = TypedDict(
    "TestReportSummaryTypeDef",
    {
        "total": int,
        "statusCounts": Dict[str, int],
        "durationInNanoSeconds": int,
    },
)

UpdateProjectInputRequestTypeDef = TypedDict(
    "UpdateProjectInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "source": NotRequired["ProjectSourceTypeDef"],
        "secondarySources": NotRequired[Sequence["ProjectSourceTypeDef"]],
        "sourceVersion": NotRequired[str],
        "secondarySourceVersions": NotRequired[Sequence["ProjectSourceVersionTypeDef"]],
        "artifacts": NotRequired["ProjectArtifactsTypeDef"],
        "secondaryArtifacts": NotRequired[Sequence["ProjectArtifactsTypeDef"]],
        "cache": NotRequired["ProjectCacheTypeDef"],
        "environment": NotRequired["ProjectEnvironmentTypeDef"],
        "serviceRole": NotRequired[str],
        "timeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "encryptionKey": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "vpcConfig": NotRequired["VpcConfigTypeDef"],
        "badgeEnabled": NotRequired[bool],
        "logsConfig": NotRequired["LogsConfigTypeDef"],
        "fileSystemLocations": NotRequired[Sequence["ProjectFileSystemLocationTypeDef"]],
        "buildBatchConfig": NotRequired["ProjectBuildBatchConfigTypeDef"],
        "concurrentBuildLimit": NotRequired[int],
    },
)

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectVisibilityInputRequestTypeDef = TypedDict(
    "UpdateProjectVisibilityInputRequestTypeDef",
    {
        "projectArn": str,
        "projectVisibility": ProjectVisibilityTypeType,
        "resourceAccessRole": NotRequired[str],
    },
)

UpdateProjectVisibilityOutputTypeDef = TypedDict(
    "UpdateProjectVisibilityOutputTypeDef",
    {
        "projectArn": str,
        "publicProjectAlias": str,
        "projectVisibility": ProjectVisibilityTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReportGroupInputRequestTypeDef = TypedDict(
    "UpdateReportGroupInputRequestTypeDef",
    {
        "arn": str,
        "exportConfig": NotRequired["ReportExportConfigTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UpdateReportGroupOutputTypeDef = TypedDict(
    "UpdateReportGroupOutputTypeDef",
    {
        "reportGroup": "ReportGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWebhookInputRequestTypeDef = TypedDict(
    "UpdateWebhookInputRequestTypeDef",
    {
        "projectName": str,
        "branchFilter": NotRequired[str],
        "rotateSecret": NotRequired[bool],
        "filterGroups": NotRequired[Sequence[Sequence["WebhookFilterTypeDef"]]],
        "buildType": NotRequired[WebhookBuildTypeType],
    },
)

UpdateWebhookOutputTypeDef = TypedDict(
    "UpdateWebhookOutputTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "vpcId": NotRequired[str],
        "subnets": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
    },
)

WebhookFilterTypeDef = TypedDict(
    "WebhookFilterTypeDef",
    {
        "type": WebhookFilterTypeType,
        "pattern": str,
        "excludeMatchedPattern": NotRequired[bool],
    },
)

WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "url": NotRequired[str],
        "payloadUrl": NotRequired[str],
        "secret": NotRequired[str],
        "branchFilter": NotRequired[str],
        "filterGroups": NotRequired[List[List["WebhookFilterTypeDef"]]],
        "buildType": NotRequired[WebhookBuildTypeType],
        "lastModifiedSecret": NotRequired[datetime],
    },
)
