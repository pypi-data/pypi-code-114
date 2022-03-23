"""
Type annotations for migrationhubstrategy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.type_defs import AntipatternSeveritySummaryTypeDef

    data: AntipatternSeveritySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AntipatternReportStatusType,
    ApplicationComponentCriteriaType,
    AppTypeType,
    AssessmentStatusType,
    AwsManagedTargetDestinationType,
    CollectorHealthType,
    DatabaseManagementPreferenceType,
    DataSourceTypeType,
    HeterogeneousTargetDatabaseEngineType,
    ImportFileTaskStatusType,
    InclusionStatusType,
    NoPreferenceTargetDestinationType,
    OSTypeType,
    OutputFormatType,
    RecommendationReportStatusType,
    ResourceSubTypeType,
    RunTimeAssessmentStatusType,
    SelfManageTargetDestinationType,
    ServerCriteriaType,
    ServerOsTypeType,
    SeverityType,
    SortOrderType,
    SrcCodeOrDbAnalysisStatusType,
    StrategyRecommendationType,
    StrategyType,
    TargetDatabaseEngineType,
    TargetDestinationType,
    TransformationToolNameType,
    VersionControlType,
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
    "AntipatternSeveritySummaryTypeDef",
    "ApplicationComponentDetailTypeDef",
    "ApplicationComponentStrategyTypeDef",
    "ApplicationComponentSummaryTypeDef",
    "ApplicationPreferencesTypeDef",
    "AssessmentSummaryTypeDef",
    "AssociatedApplicationTypeDef",
    "AwsManagedResourcesTypeDef",
    "BusinessGoalsTypeDef",
    "CollectorTypeDef",
    "DataCollectionDetailsTypeDef",
    "DatabaseConfigDetailTypeDef",
    "DatabaseMigrationPreferenceTypeDef",
    "DatabasePreferencesTypeDef",
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    "GetApplicationComponentDetailsResponseTypeDef",
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    "GetApplicationComponentStrategiesResponseTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetImportFileTaskRequestRequestTypeDef",
    "GetImportFileTaskResponseTypeDef",
    "GetPortfolioPreferencesResponseTypeDef",
    "GetPortfolioSummaryResponseTypeDef",
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    "GetRecommendationReportDetailsResponseTypeDef",
    "GetServerDetailsRequestRequestTypeDef",
    "GetServerDetailsResponseTypeDef",
    "GetServerStrategiesRequestRequestTypeDef",
    "GetServerStrategiesResponseTypeDef",
    "GroupTypeDef",
    "HeterogeneousTypeDef",
    "HomogeneousTypeDef",
    "ImportFileTaskInformationTypeDef",
    "ListApplicationComponentsRequestRequestTypeDef",
    "ListApplicationComponentsResponseTypeDef",
    "ListCollectorsRequestRequestTypeDef",
    "ListCollectorsResponseTypeDef",
    "ListImportFileTaskRequestRequestTypeDef",
    "ListImportFileTaskResponseTypeDef",
    "ListServersRequestRequestTypeDef",
    "ListServersResponseTypeDef",
    "ManagementPreferenceTypeDef",
    "NetworkInfoTypeDef",
    "NoDatabaseMigrationPreferenceTypeDef",
    "NoManagementPreferenceTypeDef",
    "OSInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PrioritizeBusinessGoalsTypeDef",
    "PutPortfolioPreferencesRequestRequestTypeDef",
    "RecommendationReportDetailsTypeDef",
    "RecommendationSetTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "SelfManageResourcesTypeDef",
    "ServerDetailTypeDef",
    "ServerStrategyTypeDef",
    "ServerSummaryTypeDef",
    "SourceCodeRepositoryTypeDef",
    "SourceCodeTypeDef",
    "StartAssessmentRequestRequestTypeDef",
    "StartAssessmentResponseTypeDef",
    "StartImportFileTaskRequestRequestTypeDef",
    "StartImportFileTaskResponseTypeDef",
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    "StartRecommendationReportGenerationResponseTypeDef",
    "StopAssessmentRequestRequestTypeDef",
    "StrategyOptionTypeDef",
    "StrategySummaryTypeDef",
    "SystemInfoTypeDef",
    "TransformationToolTypeDef",
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    "UpdateServerConfigRequestRequestTypeDef",
)

AntipatternSeveritySummaryTypeDef = TypedDict(
    "AntipatternSeveritySummaryTypeDef",
    {
        "count": NotRequired[int],
        "severity": NotRequired[SeverityType],
    },
)

ApplicationComponentDetailTypeDef = TypedDict(
    "ApplicationComponentDetailTypeDef",
    {
        "analysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
        "antipatternReportS3Object": NotRequired["S3ObjectTypeDef"],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "appType": NotRequired[AppTypeType],
        "associatedServerId": NotRequired[str],
        "databaseConfigDetail": NotRequired["DatabaseConfigDetailTypeDef"],
        "id": NotRequired[str],
        "inclusionStatus": NotRequired[InclusionStatusType],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List["AntipatternSeveritySummaryTypeDef"]],
        "moreServerAssociationExists": NotRequired[bool],
        "name": NotRequired[str],
        "osDriver": NotRequired[str],
        "osVersion": NotRequired[str],
        "recommendationSet": NotRequired["RecommendationSetTypeDef"],
        "resourceSubType": NotRequired[ResourceSubTypeType],
        "sourceCodeRepositories": NotRequired[List["SourceCodeRepositoryTypeDef"]],
        "statusMessage": NotRequired[str],
    },
)

ApplicationComponentStrategyTypeDef = TypedDict(
    "ApplicationComponentStrategyTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "recommendation": NotRequired["RecommendationSetTypeDef"],
        "status": NotRequired[StrategyRecommendationType],
    },
)

ApplicationComponentSummaryTypeDef = TypedDict(
    "ApplicationComponentSummaryTypeDef",
    {
        "appType": NotRequired[AppTypeType],
        "count": NotRequired[int],
    },
)

ApplicationPreferencesTypeDef = TypedDict(
    "ApplicationPreferencesTypeDef",
    {
        "managementPreference": NotRequired["ManagementPreferenceTypeDef"],
    },
)

AssessmentSummaryTypeDef = TypedDict(
    "AssessmentSummaryTypeDef",
    {
        "antipatternReportS3Object": NotRequired["S3ObjectTypeDef"],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List["AntipatternSeveritySummaryTypeDef"]],
        "listApplicationComponentStrategySummary": NotRequired[List["StrategySummaryTypeDef"]],
        "listApplicationComponentSummary": NotRequired[List["ApplicationComponentSummaryTypeDef"]],
        "listServerStrategySummary": NotRequired[List["StrategySummaryTypeDef"]],
        "listServerSummary": NotRequired[List["ServerSummaryTypeDef"]],
    },
)

AssociatedApplicationTypeDef = TypedDict(
    "AssociatedApplicationTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)

AwsManagedResourcesTypeDef = TypedDict(
    "AwsManagedResourcesTypeDef",
    {
        "targetDestination": List[AwsManagedTargetDestinationType],
    },
)

BusinessGoalsTypeDef = TypedDict(
    "BusinessGoalsTypeDef",
    {
        "licenseCostReduction": NotRequired[int],
        "modernizeInfrastructureWithCloudNativeTechnologies": NotRequired[int],
        "reduceOperationalOverheadWithManagedServices": NotRequired[int],
        "speedOfMigration": NotRequired[int],
    },
)

CollectorTypeDef = TypedDict(
    "CollectorTypeDef",
    {
        "collectorHealth": NotRequired[CollectorHealthType],
        "collectorId": NotRequired[str],
        "collectorVersion": NotRequired[str],
        "hostName": NotRequired[str],
        "ipAddress": NotRequired[str],
        "lastActivityTimeStamp": NotRequired[str],
        "registeredTimeStamp": NotRequired[str],
    },
)

DataCollectionDetailsTypeDef = TypedDict(
    "DataCollectionDetailsTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "failed": NotRequired[int],
        "inProgress": NotRequired[int],
        "servers": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[AssessmentStatusType],
        "success": NotRequired[int],
    },
)

DatabaseConfigDetailTypeDef = TypedDict(
    "DatabaseConfigDetailTypeDef",
    {
        "secretName": NotRequired[str],
    },
)

DatabaseMigrationPreferenceTypeDef = TypedDict(
    "DatabaseMigrationPreferenceTypeDef",
    {
        "heterogeneous": NotRequired["HeterogeneousTypeDef"],
        "homogeneous": NotRequired["HomogeneousTypeDef"],
        "noPreference": NotRequired["NoDatabaseMigrationPreferenceTypeDef"],
    },
)

DatabasePreferencesTypeDef = TypedDict(
    "DatabasePreferencesTypeDef",
    {
        "databaseManagementPreference": NotRequired[DatabaseManagementPreferenceType],
        "databaseMigrationPreference": NotRequired["DatabaseMigrationPreferenceTypeDef"],
    },
)

GetApplicationComponentDetailsRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)

GetApplicationComponentDetailsResponseTypeDef = TypedDict(
    "GetApplicationComponentDetailsResponseTypeDef",
    {
        "applicationComponentDetail": "ApplicationComponentDetailTypeDef",
        "associatedApplications": List["AssociatedApplicationTypeDef"],
        "associatedServerIds": List[str],
        "moreApplicationResource": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationComponentStrategiesRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)

GetApplicationComponentStrategiesResponseTypeDef = TypedDict(
    "GetApplicationComponentStrategiesResponseTypeDef",
    {
        "applicationComponentStrategies": List["ApplicationComponentStrategyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "dataCollectionDetails": "DataCollectionDetailsTypeDef",
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportFileTaskRequestRequestTypeDef = TypedDict(
    "GetImportFileTaskRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetImportFileTaskResponseTypeDef = TypedDict(
    "GetImportFileTaskResponseTypeDef",
    {
        "completionTime": datetime,
        "id": str,
        "importName": str,
        "inputS3Bucket": str,
        "inputS3Key": str,
        "numberOfRecordsFailed": int,
        "numberOfRecordsSuccess": int,
        "startTime": datetime,
        "status": ImportFileTaskStatusType,
        "statusReportS3Bucket": str,
        "statusReportS3Key": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortfolioPreferencesResponseTypeDef = TypedDict(
    "GetPortfolioPreferencesResponseTypeDef",
    {
        "applicationPreferences": "ApplicationPreferencesTypeDef",
        "databasePreferences": "DatabasePreferencesTypeDef",
        "prioritizeBusinessGoals": "PrioritizeBusinessGoalsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortfolioSummaryResponseTypeDef = TypedDict(
    "GetPortfolioSummaryResponseTypeDef",
    {
        "assessmentSummary": "AssessmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationReportDetailsRequestRequestTypeDef = TypedDict(
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetRecommendationReportDetailsResponseTypeDef = TypedDict(
    "GetRecommendationReportDetailsResponseTypeDef",
    {
        "id": str,
        "recommendationReportDetails": "RecommendationReportDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerDetailsRequestRequestTypeDef = TypedDict(
    "GetServerDetailsRequestRequestTypeDef",
    {
        "serverId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetServerDetailsResponseTypeDef = TypedDict(
    "GetServerDetailsResponseTypeDef",
    {
        "associatedApplications": List["AssociatedApplicationTypeDef"],
        "nextToken": str,
        "serverDetail": "ServerDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerStrategiesRequestRequestTypeDef = TypedDict(
    "GetServerStrategiesRequestRequestTypeDef",
    {
        "serverId": str,
    },
)

GetServerStrategiesResponseTypeDef = TypedDict(
    "GetServerStrategiesResponseTypeDef",
    {
        "serverStrategies": List["ServerStrategyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "name": NotRequired[Literal["ExternalId"]],
        "value": NotRequired[str],
    },
)

HeterogeneousTypeDef = TypedDict(
    "HeterogeneousTypeDef",
    {
        "targetDatabaseEngine": List[HeterogeneousTargetDatabaseEngineType],
    },
)

HomogeneousTypeDef = TypedDict(
    "HomogeneousTypeDef",
    {
        "targetDatabaseEngine": NotRequired[List[Literal["None specified"]]],
    },
)

ImportFileTaskInformationTypeDef = TypedDict(
    "ImportFileTaskInformationTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "id": NotRequired[str],
        "importName": NotRequired[str],
        "inputS3Bucket": NotRequired[str],
        "inputS3Key": NotRequired[str],
        "numberOfRecordsFailed": NotRequired[int],
        "numberOfRecordsSuccess": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ImportFileTaskStatusType],
        "statusReportS3Bucket": NotRequired[str],
        "statusReportS3Key": NotRequired[str],
    },
)

ListApplicationComponentsRequestRequestTypeDef = TypedDict(
    "ListApplicationComponentsRequestRequestTypeDef",
    {
        "applicationComponentCriteria": NotRequired[ApplicationComponentCriteriaType],
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence["GroupTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortOrderType],
    },
)

ListApplicationComponentsResponseTypeDef = TypedDict(
    "ListApplicationComponentsResponseTypeDef",
    {
        "applicationComponentInfos": List["ApplicationComponentDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCollectorsRequestRequestTypeDef = TypedDict(
    "ListCollectorsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListCollectorsResponseTypeDef = TypedDict(
    "ListCollectorsResponseTypeDef",
    {
        "Collectors": List["CollectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportFileTaskRequestRequestTypeDef = TypedDict(
    "ListImportFileTaskRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListImportFileTaskResponseTypeDef = TypedDict(
    "ListImportFileTaskResponseTypeDef",
    {
        "nextToken": str,
        "taskInfos": List["ImportFileTaskInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence["GroupTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serverCriteria": NotRequired[ServerCriteriaType],
        "sort": NotRequired[SortOrderType],
    },
)

ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "nextToken": str,
        "serverInfos": List["ServerDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagementPreferenceTypeDef = TypedDict(
    "ManagementPreferenceTypeDef",
    {
        "awsManagedResources": NotRequired["AwsManagedResourcesTypeDef"],
        "noPreference": NotRequired["NoManagementPreferenceTypeDef"],
        "selfManageResources": NotRequired["SelfManageResourcesTypeDef"],
    },
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "interfaceName": str,
        "ipAddress": str,
        "macAddress": str,
        "netMask": str,
    },
)

NoDatabaseMigrationPreferenceTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceTypeDef",
    {
        "targetDatabaseEngine": List[TargetDatabaseEngineType],
    },
)

NoManagementPreferenceTypeDef = TypedDict(
    "NoManagementPreferenceTypeDef",
    {
        "targetDestination": List[NoPreferenceTargetDestinationType],
    },
)

OSInfoTypeDef = TypedDict(
    "OSInfoTypeDef",
    {
        "type": NotRequired[OSTypeType],
        "version": NotRequired[str],
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

PrioritizeBusinessGoalsTypeDef = TypedDict(
    "PrioritizeBusinessGoalsTypeDef",
    {
        "businessGoals": NotRequired["BusinessGoalsTypeDef"],
    },
)

PutPortfolioPreferencesRequestRequestTypeDef = TypedDict(
    "PutPortfolioPreferencesRequestRequestTypeDef",
    {
        "applicationPreferences": NotRequired["ApplicationPreferencesTypeDef"],
        "databasePreferences": NotRequired["DatabasePreferencesTypeDef"],
        "prioritizeBusinessGoals": NotRequired["PrioritizeBusinessGoalsTypeDef"],
    },
)

RecommendationReportDetailsTypeDef = TypedDict(
    "RecommendationReportDetailsTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "s3Bucket": NotRequired[str],
        "s3Keys": NotRequired[List[str]],
        "startTime": NotRequired[datetime],
        "status": NotRequired[RecommendationReportStatusType],
        "statusMessage": NotRequired[str],
    },
)

RecommendationSetTypeDef = TypedDict(
    "RecommendationSetTypeDef",
    {
        "strategy": NotRequired[StrategyType],
        "targetDestination": NotRequired[TargetDestinationType],
        "transformationTool": NotRequired["TransformationToolTypeDef"],
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

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3key": NotRequired[str],
    },
)

SelfManageResourcesTypeDef = TypedDict(
    "SelfManageResourcesTypeDef",
    {
        "targetDestination": List[SelfManageTargetDestinationType],
    },
)

ServerDetailTypeDef = TypedDict(
    "ServerDetailTypeDef",
    {
        "antipatternReportS3Object": NotRequired["S3ObjectTypeDef"],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "applicationComponentStrategySummary": NotRequired[List["StrategySummaryTypeDef"]],
        "dataCollectionStatus": NotRequired[RunTimeAssessmentStatusType],
        "id": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List["AntipatternSeveritySummaryTypeDef"]],
        "name": NotRequired[str],
        "recommendationSet": NotRequired["RecommendationSetTypeDef"],
        "serverType": NotRequired[str],
        "statusMessage": NotRequired[str],
        "systemInfo": NotRequired["SystemInfoTypeDef"],
    },
)

ServerStrategyTypeDef = TypedDict(
    "ServerStrategyTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "numberOfApplicationComponents": NotRequired[int],
        "recommendation": NotRequired["RecommendationSetTypeDef"],
        "status": NotRequired[StrategyRecommendationType],
    },
)

ServerSummaryTypeDef = TypedDict(
    "ServerSummaryTypeDef",
    {
        "ServerOsType": NotRequired[ServerOsTypeType],
        "count": NotRequired[int],
    },
)

SourceCodeRepositoryTypeDef = TypedDict(
    "SourceCodeRepositoryTypeDef",
    {
        "branch": NotRequired[str],
        "repository": NotRequired[str],
        "versionControlType": NotRequired[str],
    },
)

SourceCodeTypeDef = TypedDict(
    "SourceCodeTypeDef",
    {
        "location": NotRequired[str],
        "sourceVersion": NotRequired[str],
        "versionControl": NotRequired[VersionControlType],
    },
)

StartAssessmentRequestRequestTypeDef = TypedDict(
    "StartAssessmentRequestRequestTypeDef",
    {
        "s3bucketForAnalysisData": NotRequired[str],
        "s3bucketForReportData": NotRequired[str],
    },
)

StartAssessmentResponseTypeDef = TypedDict(
    "StartAssessmentResponseTypeDef",
    {
        "assessmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportFileTaskRequestRequestTypeDef = TypedDict(
    "StartImportFileTaskRequestRequestTypeDef",
    {
        "S3Bucket": str,
        "name": str,
        "s3key": str,
        "dataSourceType": NotRequired[DataSourceTypeType],
        "groupId": NotRequired[Sequence["GroupTypeDef"]],
        "s3bucketForReportData": NotRequired[str],
    },
)

StartImportFileTaskResponseTypeDef = TypedDict(
    "StartImportFileTaskResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRecommendationReportGenerationRequestRequestTypeDef = TypedDict(
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    {
        "groupIdFilter": NotRequired[Sequence["GroupTypeDef"]],
        "outputFormat": NotRequired[OutputFormatType],
    },
)

StartRecommendationReportGenerationResponseTypeDef = TypedDict(
    "StartRecommendationReportGenerationResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAssessmentRequestRequestTypeDef = TypedDict(
    "StopAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

StrategyOptionTypeDef = TypedDict(
    "StrategyOptionTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "strategy": NotRequired[StrategyType],
        "targetDestination": NotRequired[TargetDestinationType],
        "toolName": NotRequired[TransformationToolNameType],
    },
)

StrategySummaryTypeDef = TypedDict(
    "StrategySummaryTypeDef",
    {
        "count": NotRequired[int],
        "strategy": NotRequired[StrategyType],
    },
)

SystemInfoTypeDef = TypedDict(
    "SystemInfoTypeDef",
    {
        "cpuArchitecture": NotRequired[str],
        "fileSystemType": NotRequired[str],
        "networkInfoList": NotRequired[List["NetworkInfoTypeDef"]],
        "osInfo": NotRequired["OSInfoTypeDef"],
    },
)

TransformationToolTypeDef = TypedDict(
    "TransformationToolTypeDef",
    {
        "description": NotRequired[str],
        "name": NotRequired[TransformationToolNameType],
        "tranformationToolInstallationLink": NotRequired[str],
    },
)

UpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "applicationComponentId": str,
        "inclusionStatus": NotRequired[InclusionStatusType],
        "secretsManagerKey": NotRequired[str],
        "sourceCodeList": NotRequired[Sequence["SourceCodeTypeDef"]],
        "strategyOption": NotRequired["StrategyOptionTypeDef"],
    },
)

UpdateServerConfigRequestRequestTypeDef = TypedDict(
    "UpdateServerConfigRequestRequestTypeDef",
    {
        "serverId": str,
        "strategyOption": NotRequired["StrategyOptionTypeDef"],
    },
)
