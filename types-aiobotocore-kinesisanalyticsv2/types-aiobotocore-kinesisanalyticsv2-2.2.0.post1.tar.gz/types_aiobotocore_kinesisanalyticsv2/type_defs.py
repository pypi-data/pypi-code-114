"""
Type annotations for kinesisanalyticsv2 service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisanalyticsv2/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kinesisanalyticsv2.type_defs import AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef

    data: AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ApplicationModeType,
    ApplicationRestoreTypeType,
    ApplicationStatusType,
    ArtifactTypeType,
    CodeContentTypeType,
    ConfigurationTypeType,
    InputStartingPositionType,
    LogLevelType,
    MetricsLevelType,
    RecordFormatTypeType,
    RuntimeEnvironmentType,
    SnapshotStatusType,
    UrlTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    "AddApplicationInputRequestRequestTypeDef",
    "AddApplicationInputResponseTypeDef",
    "AddApplicationOutputRequestRequestTypeDef",
    "AddApplicationOutputResponseTypeDef",
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    "AddApplicationReferenceDataSourceResponseTypeDef",
    "AddApplicationVpcConfigurationRequestRequestTypeDef",
    "AddApplicationVpcConfigurationResponseTypeDef",
    "ApplicationCodeConfigurationDescriptionTypeDef",
    "ApplicationCodeConfigurationTypeDef",
    "ApplicationCodeConfigurationUpdateTypeDef",
    "ApplicationConfigurationDescriptionTypeDef",
    "ApplicationConfigurationTypeDef",
    "ApplicationConfigurationUpdateTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    "ApplicationRestoreConfigurationTypeDef",
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationTypeDef",
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationVersionSummaryTypeDef",
    "CSVMappingParametersTypeDef",
    "CatalogConfigurationDescriptionTypeDef",
    "CatalogConfigurationTypeDef",
    "CatalogConfigurationUpdateTypeDef",
    "CheckpointConfigurationDescriptionTypeDef",
    "CheckpointConfigurationTypeDef",
    "CheckpointConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CodeContentDescriptionTypeDef",
    "CodeContentTypeDef",
    "CodeContentUpdateTypeDef",
    "CreateApplicationPresignedUrlRequestRequestTypeDef",
    "CreateApplicationPresignedUrlResponseTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateApplicationSnapshotRequestRequestTypeDef",
    "CustomArtifactConfigurationDescriptionTypeDef",
    "CustomArtifactConfigurationTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    "DeleteApplicationOutputRequestRequestTypeDef",
    "DeleteApplicationOutputResponseTypeDef",
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteApplicationSnapshotRequestRequestTypeDef",
    "DeleteApplicationVpcConfigurationRequestRequestTypeDef",
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    "DeployAsApplicationConfigurationTypeDef",
    "DeployAsApplicationConfigurationUpdateTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeApplicationSnapshotRequestRequestTypeDef",
    "DescribeApplicationSnapshotResponseTypeDef",
    "DescribeApplicationVersionRequestRequestTypeDef",
    "DescribeApplicationVersionResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaRequestRequestTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "EnvironmentPropertiesTypeDef",
    "EnvironmentPropertyDescriptionsTypeDef",
    "EnvironmentPropertyUpdatesTypeDef",
    "FlinkApplicationConfigurationDescriptionTypeDef",
    "FlinkApplicationConfigurationTypeDef",
    "FlinkApplicationConfigurationUpdateTypeDef",
    "FlinkRunConfigurationTypeDef",
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    "GlueDataCatalogConfigurationTypeDef",
    "GlueDataCatalogConfigurationUpdateTypeDef",
    "InputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismTypeDef",
    "InputParallelismUpdateTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "InputSchemaUpdateTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "InputTypeDef",
    "InputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationSnapshotsRequestRequestTypeDef",
    "ListApplicationSnapshotsResponseTypeDef",
    "ListApplicationVersionsRequestRequestTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "MavenReferenceTypeDef",
    "MonitoringConfigurationDescriptionTypeDef",
    "MonitoringConfigurationTypeDef",
    "MonitoringConfigurationUpdateTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelismConfigurationDescriptionTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParallelismConfigurationUpdateTypeDef",
    "PropertyGroupTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackApplicationRequestRequestTypeDef",
    "RollbackApplicationResponseTypeDef",
    "RunConfigurationDescriptionTypeDef",
    "RunConfigurationTypeDef",
    "RunConfigurationUpdateTypeDef",
    "S3ApplicationCodeLocationDescriptionTypeDef",
    "S3ConfigurationTypeDef",
    "S3ContentBaseLocationDescriptionTypeDef",
    "S3ContentBaseLocationTypeDef",
    "S3ContentBaseLocationUpdateTypeDef",
    "S3ContentLocationTypeDef",
    "S3ContentLocationUpdateTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SnapshotDetailsTypeDef",
    "SourceSchemaTypeDef",
    "SqlApplicationConfigurationDescriptionTypeDef",
    "SqlApplicationConfigurationTypeDef",
    "SqlApplicationConfigurationUpdateTypeDef",
    "SqlRunConfigurationTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef",
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUpdateTypeDef",
    "ZeppelinApplicationConfigurationDescriptionTypeDef",
    "ZeppelinApplicationConfigurationTypeDef",
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    "ZeppelinMonitoringConfigurationTypeDef",
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
)

AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CloudWatchLoggingOption": "CloudWatchLoggingOptionTypeDef",
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)

AddApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfiguration": "InputProcessingConfigurationTypeDef",
    },
)

AddApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfigurationDescription": "InputProcessingConfigurationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddApplicationInputRequestRequestTypeDef = TypedDict(
    "AddApplicationInputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Input": "InputTypeDef",
    },
)

AddApplicationInputResponseTypeDef = TypedDict(
    "AddApplicationInputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputDescriptions": List["InputDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddApplicationOutputRequestRequestTypeDef = TypedDict(
    "AddApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Output": "OutputTypeDef",
    },
)

AddApplicationOutputResponseTypeDef = TypedDict(
    "AddApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "OutputDescriptions": List["OutputDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceDataSource": "ReferenceDataSourceTypeDef",
    },
)

AddApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ReferenceDataSourceDescriptions": List["ReferenceDataSourceDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddApplicationVpcConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationVpcConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)

AddApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "AddApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentType": CodeContentTypeType,
        "CodeContentDescription": NotRequired["CodeContentDescriptionTypeDef"],
    },
)

ApplicationCodeConfigurationTypeDef = TypedDict(
    "ApplicationCodeConfigurationTypeDef",
    {
        "CodeContentType": CodeContentTypeType,
        "CodeContent": NotRequired["CodeContentTypeDef"],
    },
)

ApplicationCodeConfigurationUpdateTypeDef = TypedDict(
    "ApplicationCodeConfigurationUpdateTypeDef",
    {
        "CodeContentTypeUpdate": NotRequired[CodeContentTypeType],
        "CodeContentUpdate": NotRequired["CodeContentUpdateTypeDef"],
    },
)

ApplicationConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": NotRequired[
            "SqlApplicationConfigurationDescriptionTypeDef"
        ],
        "ApplicationCodeConfigurationDescription": NotRequired[
            "ApplicationCodeConfigurationDescriptionTypeDef"
        ],
        "RunConfigurationDescription": NotRequired["RunConfigurationDescriptionTypeDef"],
        "FlinkApplicationConfigurationDescription": NotRequired[
            "FlinkApplicationConfigurationDescriptionTypeDef"
        ],
        "EnvironmentPropertyDescriptions": NotRequired["EnvironmentPropertyDescriptionsTypeDef"],
        "ApplicationSnapshotConfigurationDescription": NotRequired[
            "ApplicationSnapshotConfigurationDescriptionTypeDef"
        ],
        "VpcConfigurationDescriptions": NotRequired[List["VpcConfigurationDescriptionTypeDef"]],
        "ZeppelinApplicationConfigurationDescription": NotRequired[
            "ZeppelinApplicationConfigurationDescriptionTypeDef"
        ],
    },
)

ApplicationConfigurationTypeDef = TypedDict(
    "ApplicationConfigurationTypeDef",
    {
        "SqlApplicationConfiguration": NotRequired["SqlApplicationConfigurationTypeDef"],
        "FlinkApplicationConfiguration": NotRequired["FlinkApplicationConfigurationTypeDef"],
        "EnvironmentProperties": NotRequired["EnvironmentPropertiesTypeDef"],
        "ApplicationCodeConfiguration": NotRequired["ApplicationCodeConfigurationTypeDef"],
        "ApplicationSnapshotConfiguration": NotRequired["ApplicationSnapshotConfigurationTypeDef"],
        "VpcConfigurations": NotRequired[Sequence["VpcConfigurationTypeDef"]],
        "ZeppelinApplicationConfiguration": NotRequired["ZeppelinApplicationConfigurationTypeDef"],
    },
)

ApplicationConfigurationUpdateTypeDef = TypedDict(
    "ApplicationConfigurationUpdateTypeDef",
    {
        "SqlApplicationConfigurationUpdate": NotRequired[
            "SqlApplicationConfigurationUpdateTypeDef"
        ],
        "ApplicationCodeConfigurationUpdate": NotRequired[
            "ApplicationCodeConfigurationUpdateTypeDef"
        ],
        "FlinkApplicationConfigurationUpdate": NotRequired[
            "FlinkApplicationConfigurationUpdateTypeDef"
        ],
        "EnvironmentPropertyUpdates": NotRequired["EnvironmentPropertyUpdatesTypeDef"],
        "ApplicationSnapshotConfigurationUpdate": NotRequired[
            "ApplicationSnapshotConfigurationUpdateTypeDef"
        ],
        "VpcConfigurationUpdates": NotRequired[Sequence["VpcConfigurationUpdateTypeDef"]],
        "ZeppelinApplicationConfigurationUpdate": NotRequired[
            "ZeppelinApplicationConfigurationUpdateTypeDef"
        ],
    },
)

ApplicationDetailTypeDef = TypedDict(
    "ApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationName": str,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "ApplicationDescription": NotRequired[str],
        "ServiceExecutionRole": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "ApplicationConfigurationDescription": NotRequired[
            "ApplicationConfigurationDescriptionTypeDef"
        ],
        "CloudWatchLoggingOptionDescriptions": NotRequired[
            List["CloudWatchLoggingOptionDescriptionTypeDef"]
        ],
        "ApplicationMaintenanceConfigurationDescription": NotRequired[
            "ApplicationMaintenanceConfigurationDescriptionTypeDef"
        ],
        "ApplicationVersionUpdatedFrom": NotRequired[int],
        "ApplicationVersionRolledBackFrom": NotRequired[int],
        "ConditionalToken": NotRequired[str],
        "ApplicationVersionRolledBackTo": NotRequired[int],
        "ApplicationMode": NotRequired[ApplicationModeType],
    },
)

ApplicationMaintenanceConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    {
        "ApplicationMaintenanceWindowStartTime": str,
        "ApplicationMaintenanceWindowEndTime": str,
    },
)

ApplicationMaintenanceConfigurationUpdateTypeDef = TypedDict(
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    {
        "ApplicationMaintenanceWindowStartTimeUpdate": str,
    },
)

ApplicationRestoreConfigurationTypeDef = TypedDict(
    "ApplicationRestoreConfigurationTypeDef",
    {
        "ApplicationRestoreType": ApplicationRestoreTypeType,
        "SnapshotName": NotRequired[str],
    },
)

ApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    {
        "SnapshotsEnabled": bool,
    },
)

ApplicationSnapshotConfigurationTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationTypeDef",
    {
        "SnapshotsEnabled": bool,
    },
)

ApplicationSnapshotConfigurationUpdateTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    {
        "SnapshotsEnabledUpdate": bool,
    },
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ApplicationMode": NotRequired[ApplicationModeType],
    },
)

ApplicationVersionSummaryTypeDef = TypedDict(
    "ApplicationVersionSummaryTypeDef",
    {
        "ApplicationVersionId": int,
        "ApplicationStatus": ApplicationStatusType,
    },
)

CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)

CatalogConfigurationDescriptionTypeDef = TypedDict(
    "CatalogConfigurationDescriptionTypeDef",
    {
        "GlueDataCatalogConfigurationDescription": "GlueDataCatalogConfigurationDescriptionTypeDef",
    },
)

CatalogConfigurationTypeDef = TypedDict(
    "CatalogConfigurationTypeDef",
    {
        "GlueDataCatalogConfiguration": "GlueDataCatalogConfigurationTypeDef",
    },
)

CatalogConfigurationUpdateTypeDef = TypedDict(
    "CatalogConfigurationUpdateTypeDef",
    {
        "GlueDataCatalogConfigurationUpdate": "GlueDataCatalogConfigurationUpdateTypeDef",
    },
)

CheckpointConfigurationDescriptionTypeDef = TypedDict(
    "CheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": NotRequired[ConfigurationTypeType],
        "CheckpointingEnabled": NotRequired[bool],
        "CheckpointInterval": NotRequired[int],
        "MinPauseBetweenCheckpoints": NotRequired[int],
    },
)

CheckpointConfigurationTypeDef = TypedDict(
    "CheckpointConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "CheckpointingEnabled": NotRequired[bool],
        "CheckpointInterval": NotRequired[int],
        "MinPauseBetweenCheckpoints": NotRequired[int],
    },
)

CheckpointConfigurationUpdateTypeDef = TypedDict(
    "CheckpointConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": NotRequired[ConfigurationTypeType],
        "CheckpointingEnabledUpdate": NotRequired[bool],
        "CheckpointIntervalUpdate": NotRequired[int],
        "MinPauseBetweenCheckpointsUpdate": NotRequired[int],
    },
)

CloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
        "CloudWatchLoggingOptionId": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)

CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
    },
)

CloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "CloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
        "LogStreamARNUpdate": NotRequired[str],
    },
)

CodeContentDescriptionTypeDef = TypedDict(
    "CodeContentDescriptionTypeDef",
    {
        "TextContent": NotRequired[str],
        "CodeMD5": NotRequired[str],
        "CodeSize": NotRequired[int],
        "S3ApplicationCodeLocationDescription": NotRequired[
            "S3ApplicationCodeLocationDescriptionTypeDef"
        ],
    },
)

CodeContentTypeDef = TypedDict(
    "CodeContentTypeDef",
    {
        "TextContent": NotRequired[str],
        "ZipFileContent": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3ContentLocation": NotRequired["S3ContentLocationTypeDef"],
    },
)

CodeContentUpdateTypeDef = TypedDict(
    "CodeContentUpdateTypeDef",
    {
        "TextContentUpdate": NotRequired[str],
        "ZipFileContentUpdate": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3ContentLocationUpdate": NotRequired["S3ContentLocationUpdateTypeDef"],
    },
)

CreateApplicationPresignedUrlRequestRequestTypeDef = TypedDict(
    "CreateApplicationPresignedUrlRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "UrlType": UrlTypeType,
        "SessionExpirationDurationInSeconds": NotRequired[int],
    },
)

CreateApplicationPresignedUrlResponseTypeDef = TypedDict(
    "CreateApplicationPresignedUrlResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ServiceExecutionRole": str,
        "ApplicationDescription": NotRequired[str],
        "ApplicationConfiguration": NotRequired["ApplicationConfigurationTypeDef"],
        "CloudWatchLoggingOptions": NotRequired[Sequence["CloudWatchLoggingOptionTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ApplicationMode": NotRequired[ApplicationModeType],
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApplicationSnapshotRequestRequestTypeDef = TypedDict(
    "CreateApplicationSnapshotRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "SnapshotName": str,
    },
)

CustomArtifactConfigurationDescriptionTypeDef = TypedDict(
    "CustomArtifactConfigurationDescriptionTypeDef",
    {
        "ArtifactType": NotRequired[ArtifactTypeType],
        "S3ContentLocationDescription": NotRequired["S3ContentLocationTypeDef"],
        "MavenReferenceDescription": NotRequired["MavenReferenceTypeDef"],
    },
)

CustomArtifactConfigurationTypeDef = TypedDict(
    "CustomArtifactConfigurationTypeDef",
    {
        "ArtifactType": ArtifactTypeType,
        "S3ContentLocation": NotRequired["S3ContentLocationTypeDef"],
        "MavenReference": NotRequired["MavenReferenceTypeDef"],
    },
)

DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CloudWatchLoggingOptionId": str,
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)

DeleteApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
    },
)

DeleteApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationOutputRequestRequestTypeDef = TypedDict(
    "DeleteApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "OutputId": str,
    },
)

DeleteApplicationOutputResponseTypeDef = TypedDict(
    "DeleteApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceId": str,
    },
)

DeleteApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CreateTimestamp": Union[datetime, str],
    },
)

DeleteApplicationSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteApplicationSnapshotRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "SnapshotName": str,
        "SnapshotCreationTimestamp": Union[datetime, str],
    },
)

DeleteApplicationVpcConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationVpcConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "VpcConfigurationId": str,
        "CurrentApplicationVersionId": NotRequired[int],
        "ConditionalToken": NotRequired[str],
    },
)

DeleteApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeployAsApplicationConfigurationDescriptionTypeDef = TypedDict(
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    {
        "S3ContentLocationDescription": "S3ContentBaseLocationDescriptionTypeDef",
    },
)

DeployAsApplicationConfigurationTypeDef = TypedDict(
    "DeployAsApplicationConfigurationTypeDef",
    {
        "S3ContentLocation": "S3ContentBaseLocationTypeDef",
    },
)

DeployAsApplicationConfigurationUpdateTypeDef = TypedDict(
    "DeployAsApplicationConfigurationUpdateTypeDef",
    {
        "S3ContentLocationUpdate": NotRequired["S3ContentBaseLocationUpdateTypeDef"],
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "IncludeAdditionalDetails": NotRequired[bool],
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationSnapshotRequestRequestTypeDef = TypedDict(
    "DescribeApplicationSnapshotRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "SnapshotName": str,
    },
)

DescribeApplicationSnapshotResponseTypeDef = TypedDict(
    "DescribeApplicationSnapshotResponseTypeDef",
    {
        "SnapshotDetails": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationVersionRequestRequestTypeDef = TypedDict(
    "DescribeApplicationVersionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "ApplicationVersionId": int,
    },
)

DescribeApplicationVersionResponseTypeDef = TypedDict(
    "DescribeApplicationVersionResponseTypeDef",
    {
        "ApplicationVersionDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)

DiscoverInputSchemaRequestRequestTypeDef = TypedDict(
    "DiscoverInputSchemaRequestRequestTypeDef",
    {
        "ServiceExecutionRole": str,
        "ResourceARN": NotRequired[str],
        "InputStartingPositionConfiguration": NotRequired[
            "InputStartingPositionConfigurationTypeDef"
        ],
        "S3Configuration": NotRequired["S3ConfigurationTypeDef"],
        "InputProcessingConfiguration": NotRequired["InputProcessingConfigurationTypeDef"],
    },
)

DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": "SourceSchemaTypeDef",
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentPropertiesTypeDef = TypedDict(
    "EnvironmentPropertiesTypeDef",
    {
        "PropertyGroups": Sequence["PropertyGroupTypeDef"],
    },
)

EnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "EnvironmentPropertyDescriptionsTypeDef",
    {
        "PropertyGroupDescriptions": NotRequired[List["PropertyGroupTypeDef"]],
    },
)

EnvironmentPropertyUpdatesTypeDef = TypedDict(
    "EnvironmentPropertyUpdatesTypeDef",
    {
        "PropertyGroups": Sequence["PropertyGroupTypeDef"],
    },
)

FlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "FlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": NotRequired[
            "CheckpointConfigurationDescriptionTypeDef"
        ],
        "MonitoringConfigurationDescription": NotRequired[
            "MonitoringConfigurationDescriptionTypeDef"
        ],
        "ParallelismConfigurationDescription": NotRequired[
            "ParallelismConfigurationDescriptionTypeDef"
        ],
        "JobPlanDescription": NotRequired[str],
    },
)

FlinkApplicationConfigurationTypeDef = TypedDict(
    "FlinkApplicationConfigurationTypeDef",
    {
        "CheckpointConfiguration": NotRequired["CheckpointConfigurationTypeDef"],
        "MonitoringConfiguration": NotRequired["MonitoringConfigurationTypeDef"],
        "ParallelismConfiguration": NotRequired["ParallelismConfigurationTypeDef"],
    },
)

FlinkApplicationConfigurationUpdateTypeDef = TypedDict(
    "FlinkApplicationConfigurationUpdateTypeDef",
    {
        "CheckpointConfigurationUpdate": NotRequired["CheckpointConfigurationUpdateTypeDef"],
        "MonitoringConfigurationUpdate": NotRequired["MonitoringConfigurationUpdateTypeDef"],
        "ParallelismConfigurationUpdate": NotRequired["ParallelismConfigurationUpdateTypeDef"],
    },
)

FlinkRunConfigurationTypeDef = TypedDict(
    "FlinkRunConfigurationTypeDef",
    {
        "AllowNonRestoredState": NotRequired[bool],
    },
)

GlueDataCatalogConfigurationDescriptionTypeDef = TypedDict(
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    {
        "DatabaseARN": str,
    },
)

GlueDataCatalogConfigurationTypeDef = TypedDict(
    "GlueDataCatalogConfigurationTypeDef",
    {
        "DatabaseARN": str,
    },
)

GlueDataCatalogConfigurationUpdateTypeDef = TypedDict(
    "GlueDataCatalogConfigurationUpdateTypeDef",
    {
        "DatabaseARNUpdate": str,
    },
)

InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": NotRequired[str],
        "NamePrefix": NotRequired[str],
        "InAppStreamNames": NotRequired[List[str]],
        "InputProcessingConfigurationDescription": NotRequired[
            "InputProcessingConfigurationDescriptionTypeDef"
        ],
        "KinesisStreamsInputDescription": NotRequired["KinesisStreamsInputDescriptionTypeDef"],
        "KinesisFirehoseInputDescription": NotRequired["KinesisFirehoseInputDescriptionTypeDef"],
        "InputSchema": NotRequired["SourceSchemaTypeDef"],
        "InputParallelism": NotRequired["InputParallelismTypeDef"],
        "InputStartingPositionConfiguration": NotRequired[
            "InputStartingPositionConfigurationTypeDef"
        ],
    },
)

InputLambdaProcessorDescriptionTypeDef = TypedDict(
    "InputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)

InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
    },
)

InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": NotRequired[int],
    },
)

InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": int,
    },
)

InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": NotRequired["InputLambdaProcessorDescriptionTypeDef"],
    },
)

InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": "InputLambdaProcessorTypeDef",
    },
)

InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": "InputLambdaProcessorUpdateTypeDef",
    },
)

InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": NotRequired["RecordFormatTypeDef"],
        "RecordEncodingUpdate": NotRequired[str],
        "RecordColumnUpdates": NotRequired[Sequence["RecordColumnTypeDef"]],
    },
)

InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": NotRequired[InputStartingPositionType],
    },
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": "SourceSchemaTypeDef",
        "InputProcessingConfiguration": NotRequired["InputProcessingConfigurationTypeDef"],
        "KinesisStreamsInput": NotRequired["KinesisStreamsInputTypeDef"],
        "KinesisFirehoseInput": NotRequired["KinesisFirehoseInputTypeDef"],
        "InputParallelism": NotRequired["InputParallelismTypeDef"],
    },
)

InputUpdateTypeDef = TypedDict(
    "InputUpdateTypeDef",
    {
        "InputId": str,
        "NamePrefixUpdate": NotRequired[str],
        "InputProcessingConfigurationUpdate": NotRequired[
            "InputProcessingConfigurationUpdateTypeDef"
        ],
        "KinesisStreamsInputUpdate": NotRequired["KinesisStreamsInputUpdateTypeDef"],
        "KinesisFirehoseInputUpdate": NotRequired["KinesisFirehoseInputUpdateTypeDef"],
        "InputSchemaUpdate": NotRequired["InputSchemaUpdateTypeDef"],
        "InputParallelismUpdate": NotRequired["InputParallelismUpdateTypeDef"],
    },
)

JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)

KinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)

KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
    },
)

KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

KinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)

KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
    },
)

KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

KinesisStreamsInputDescriptionTypeDef = TypedDict(
    "KinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)

KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
    },
)

KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

KinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "KinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)

KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
    },
)

KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

LambdaOutputDescriptionTypeDef = TypedDict(
    "LambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": NotRequired[str],
    },
)

LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
    },
)

LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

ListApplicationSnapshotsRequestRequestTypeDef = TypedDict(
    "ListApplicationSnapshotsRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationSnapshotsResponseTypeDef = TypedDict(
    "ListApplicationSnapshotsResponseTypeDef",
    {
        "SnapshotSummaries": List["SnapshotDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "ListApplicationVersionsRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {
        "ApplicationVersionSummaries": List["ApplicationVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": NotRequired["JSONMappingParametersTypeDef"],
        "CSVMappingParameters": NotRequired["CSVMappingParametersTypeDef"],
    },
)

MavenReferenceTypeDef = TypedDict(
    "MavenReferenceTypeDef",
    {
        "GroupId": str,
        "ArtifactId": str,
        "Version": str,
    },
)

MonitoringConfigurationDescriptionTypeDef = TypedDict(
    "MonitoringConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": NotRequired[ConfigurationTypeType],
        "MetricsLevel": NotRequired[MetricsLevelType],
        "LogLevel": NotRequired[LogLevelType],
    },
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "MetricsLevel": NotRequired[MetricsLevelType],
        "LogLevel": NotRequired[LogLevelType],
    },
)

MonitoringConfigurationUpdateTypeDef = TypedDict(
    "MonitoringConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": NotRequired[ConfigurationTypeType],
        "MetricsLevelUpdate": NotRequired[MetricsLevelType],
        "LogLevelUpdate": NotRequired[LogLevelType],
    },
)

OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": NotRequired[str],
        "Name": NotRequired[str],
        "KinesisStreamsOutputDescription": NotRequired["KinesisStreamsOutputDescriptionTypeDef"],
        "KinesisFirehoseOutputDescription": NotRequired["KinesisFirehoseOutputDescriptionTypeDef"],
        "LambdaOutputDescription": NotRequired["LambdaOutputDescriptionTypeDef"],
        "DestinationSchema": NotRequired["DestinationSchemaTypeDef"],
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": "DestinationSchemaTypeDef",
        "KinesisStreamsOutput": NotRequired["KinesisStreamsOutputTypeDef"],
        "KinesisFirehoseOutput": NotRequired["KinesisFirehoseOutputTypeDef"],
        "LambdaOutput": NotRequired["LambdaOutputTypeDef"],
    },
)

OutputUpdateTypeDef = TypedDict(
    "OutputUpdateTypeDef",
    {
        "OutputId": str,
        "NameUpdate": NotRequired[str],
        "KinesisStreamsOutputUpdate": NotRequired["KinesisStreamsOutputUpdateTypeDef"],
        "KinesisFirehoseOutputUpdate": NotRequired["KinesisFirehoseOutputUpdateTypeDef"],
        "LambdaOutputUpdate": NotRequired["LambdaOutputUpdateTypeDef"],
        "DestinationSchemaUpdate": NotRequired["DestinationSchemaTypeDef"],
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

ParallelismConfigurationDescriptionTypeDef = TypedDict(
    "ParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": NotRequired[ConfigurationTypeType],
        "Parallelism": NotRequired[int],
        "ParallelismPerKPU": NotRequired[int],
        "CurrentParallelism": NotRequired[int],
        "AutoScalingEnabled": NotRequired[bool],
    },
)

ParallelismConfigurationTypeDef = TypedDict(
    "ParallelismConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "Parallelism": NotRequired[int],
        "ParallelismPerKPU": NotRequired[int],
        "AutoScalingEnabled": NotRequired[bool],
    },
)

ParallelismConfigurationUpdateTypeDef = TypedDict(
    "ParallelismConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": NotRequired[ConfigurationTypeType],
        "ParallelismUpdate": NotRequired[int],
        "ParallelismPerKPUUpdate": NotRequired[int],
        "AutoScalingEnabledUpdate": NotRequired[bool],
    },
)

PropertyGroupTypeDef = TypedDict(
    "PropertyGroupTypeDef",
    {
        "PropertyGroupId": str,
        "PropertyMap": Mapping[str, str],
    },
)

RecordColumnTypeDef = TypedDict(
    "RecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
        "Mapping": NotRequired[str],
    },
)

RecordFormatTypeDef = TypedDict(
    "RecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
        "MappingParameters": NotRequired["MappingParametersTypeDef"],
    },
)

ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "ReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": "S3ReferenceDataSourceDescriptionTypeDef",
        "ReferenceSchema": NotRequired["SourceSchemaTypeDef"],
    },
)

ReferenceDataSourceTypeDef = TypedDict(
    "ReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": "SourceSchemaTypeDef",
        "S3ReferenceDataSource": NotRequired["S3ReferenceDataSourceTypeDef"],
    },
)

ReferenceDataSourceUpdateTypeDef = TypedDict(
    "ReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
        "TableNameUpdate": NotRequired[str],
        "S3ReferenceDataSourceUpdate": NotRequired["S3ReferenceDataSourceUpdateTypeDef"],
        "ReferenceSchemaUpdate": NotRequired["SourceSchemaTypeDef"],
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

RollbackApplicationRequestRequestTypeDef = TypedDict(
    "RollbackApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
    },
)

RollbackApplicationResponseTypeDef = TypedDict(
    "RollbackApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RunConfigurationDescriptionTypeDef = TypedDict(
    "RunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": NotRequired[
            "ApplicationRestoreConfigurationTypeDef"
        ],
        "FlinkRunConfigurationDescription": NotRequired["FlinkRunConfigurationTypeDef"],
    },
)

RunConfigurationTypeDef = TypedDict(
    "RunConfigurationTypeDef",
    {
        "FlinkRunConfiguration": NotRequired["FlinkRunConfigurationTypeDef"],
        "SqlRunConfigurations": NotRequired[Sequence["SqlRunConfigurationTypeDef"]],
        "ApplicationRestoreConfiguration": NotRequired["ApplicationRestoreConfigurationTypeDef"],
    },
)

RunConfigurationUpdateTypeDef = TypedDict(
    "RunConfigurationUpdateTypeDef",
    {
        "FlinkRunConfiguration": NotRequired["FlinkRunConfigurationTypeDef"],
        "ApplicationRestoreConfiguration": NotRequired["ApplicationRestoreConfigurationTypeDef"],
    },
)

S3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "S3ApplicationCodeLocationDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ObjectVersion": NotRequired[str],
    },
)

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
)

S3ContentBaseLocationDescriptionTypeDef = TypedDict(
    "S3ContentBaseLocationDescriptionTypeDef",
    {
        "BucketARN": str,
        "BasePath": NotRequired[str],
    },
)

S3ContentBaseLocationTypeDef = TypedDict(
    "S3ContentBaseLocationTypeDef",
    {
        "BucketARN": str,
        "BasePath": NotRequired[str],
    },
)

S3ContentBaseLocationUpdateTypeDef = TypedDict(
    "S3ContentBaseLocationUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "BasePathUpdate": NotRequired[str],
    },
)

S3ContentLocationTypeDef = TypedDict(
    "S3ContentLocationTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ObjectVersion": NotRequired[str],
    },
)

S3ContentLocationUpdateTypeDef = TypedDict(
    "S3ContentLocationUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "FileKeyUpdate": NotRequired[str],
        "ObjectVersionUpdate": NotRequired[str],
    },
)

S3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "S3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": NotRequired[str],
    },
)

S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": NotRequired[str],
        "FileKey": NotRequired[str],
    },
)

S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "FileKeyUpdate": NotRequired[str],
    },
)

SnapshotDetailsTypeDef = TypedDict(
    "SnapshotDetailsTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": SnapshotStatusType,
        "ApplicationVersionId": int,
        "SnapshotCreationTimestamp": NotRequired[datetime],
    },
)

SourceSchemaTypeDef = TypedDict(
    "SourceSchemaTypeDef",
    {
        "RecordFormat": "RecordFormatTypeDef",
        "RecordColumns": Sequence["RecordColumnTypeDef"],
        "RecordEncoding": NotRequired[str],
    },
)

SqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "SqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": NotRequired[List["InputDescriptionTypeDef"]],
        "OutputDescriptions": NotRequired[List["OutputDescriptionTypeDef"]],
        "ReferenceDataSourceDescriptions": NotRequired[
            List["ReferenceDataSourceDescriptionTypeDef"]
        ],
    },
)

SqlApplicationConfigurationTypeDef = TypedDict(
    "SqlApplicationConfigurationTypeDef",
    {
        "Inputs": NotRequired[Sequence["InputTypeDef"]],
        "Outputs": NotRequired[Sequence["OutputTypeDef"]],
        "ReferenceDataSources": NotRequired[Sequence["ReferenceDataSourceTypeDef"]],
    },
)

SqlApplicationConfigurationUpdateTypeDef = TypedDict(
    "SqlApplicationConfigurationUpdateTypeDef",
    {
        "InputUpdates": NotRequired[Sequence["InputUpdateTypeDef"]],
        "OutputUpdates": NotRequired[Sequence["OutputUpdateTypeDef"]],
        "ReferenceDataSourceUpdates": NotRequired[Sequence["ReferenceDataSourceUpdateTypeDef"]],
    },
)

SqlRunConfigurationTypeDef = TypedDict(
    "SqlRunConfigurationTypeDef",
    {
        "InputId": str,
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
)

StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "RunConfiguration": NotRequired["RunConfigurationTypeDef"],
    },
)

StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "Force": NotRequired[bool],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationMaintenanceConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "ApplicationMaintenanceConfigurationUpdate": (
            "ApplicationMaintenanceConfigurationUpdateTypeDef"
        ),
    },
)

UpdateApplicationMaintenanceConfigurationResponseTypeDef = TypedDict(
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationMaintenanceConfigurationDescription": (
            "ApplicationMaintenanceConfigurationDescriptionTypeDef"
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": NotRequired[int],
        "ApplicationConfigurationUpdate": NotRequired["ApplicationConfigurationUpdateTypeDef"],
        "ServiceExecutionRoleUpdate": NotRequired[str],
        "RunConfigurationUpdate": NotRequired["RunConfigurationUpdateTypeDef"],
        "CloudWatchLoggingOptionUpdates": NotRequired[
            Sequence["CloudWatchLoggingOptionUpdateTypeDef"]
        ],
        "ConditionalToken": NotRequired[str],
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "VpcConfigurationId": str,
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
)

VpcConfigurationUpdateTypeDef = TypedDict(
    "VpcConfigurationUpdateTypeDef",
    {
        "VpcConfigurationId": str,
        "SubnetIdUpdates": NotRequired[Sequence[str]],
        "SecurityGroupIdUpdates": NotRequired[Sequence[str]],
    },
)

ZeppelinApplicationConfigurationDescriptionTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationDescriptionTypeDef",
    {
        "MonitoringConfigurationDescription": "ZeppelinMonitoringConfigurationDescriptionTypeDef",
        "CatalogConfigurationDescription": NotRequired["CatalogConfigurationDescriptionTypeDef"],
        "DeployAsApplicationConfigurationDescription": NotRequired[
            "DeployAsApplicationConfigurationDescriptionTypeDef"
        ],
        "CustomArtifactsConfigurationDescription": NotRequired[
            List["CustomArtifactConfigurationDescriptionTypeDef"]
        ],
    },
)

ZeppelinApplicationConfigurationTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationTypeDef",
    {
        "MonitoringConfiguration": NotRequired["ZeppelinMonitoringConfigurationTypeDef"],
        "CatalogConfiguration": NotRequired["CatalogConfigurationTypeDef"],
        "DeployAsApplicationConfiguration": NotRequired["DeployAsApplicationConfigurationTypeDef"],
        "CustomArtifactsConfiguration": NotRequired[Sequence["CustomArtifactConfigurationTypeDef"]],
    },
)

ZeppelinApplicationConfigurationUpdateTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    {
        "MonitoringConfigurationUpdate": NotRequired[
            "ZeppelinMonitoringConfigurationUpdateTypeDef"
        ],
        "CatalogConfigurationUpdate": NotRequired["CatalogConfigurationUpdateTypeDef"],
        "DeployAsApplicationConfigurationUpdate": NotRequired[
            "DeployAsApplicationConfigurationUpdateTypeDef"
        ],
        "CustomArtifactsConfigurationUpdate": NotRequired[
            Sequence["CustomArtifactConfigurationTypeDef"]
        ],
    },
)

ZeppelinMonitoringConfigurationDescriptionTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    {
        "LogLevel": NotRequired[LogLevelType],
    },
)

ZeppelinMonitoringConfigurationTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationTypeDef",
    {
        "LogLevel": LogLevelType,
    },
)

ZeppelinMonitoringConfigurationUpdateTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
    {
        "LogLevelUpdate": LogLevelType,
    },
)
