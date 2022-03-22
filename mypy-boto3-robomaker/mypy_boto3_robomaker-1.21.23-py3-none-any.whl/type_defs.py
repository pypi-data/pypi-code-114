"""
Type annotations for robomaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsRequestRequestTypeDef

    data: BatchDeleteWorldsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ArchitectureType,
    ComputeTypeType,
    DataSourceTypeType,
    DeploymentJobErrorCodeType,
    DeploymentStatusType,
    ExitBehaviorType,
    FailureBehaviorType,
    RobotDeploymentStepType,
    RobotSoftwareSuiteTypeType,
    RobotSoftwareSuiteVersionTypeType,
    RobotStatusType,
    SimulationJobBatchStatusType,
    SimulationJobErrorCodeType,
    SimulationJobStatusType,
    SimulationSoftwareSuiteTypeType,
    UploadBehaviorType,
    WorldExportJobErrorCodeType,
    WorldExportJobStatusType,
    WorldGenerationJobErrorCodeType,
    WorldGenerationJobStatusType,
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
    "BatchDeleteWorldsRequestRequestTypeDef",
    "BatchDeleteWorldsResponseTypeDef",
    "BatchDescribeSimulationJobRequestRequestTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "BatchPolicyTypeDef",
    "CancelDeploymentJobRequestRequestTypeDef",
    "CancelSimulationJobBatchRequestRequestTypeDef",
    "CancelSimulationJobRequestRequestTypeDef",
    "CancelWorldExportJobRequestRequestTypeDef",
    "CancelWorldGenerationJobRequestRequestTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateDeploymentJobRequestRequestTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotApplicationRequestRequestTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionRequestRequestTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "CreateRobotRequestRequestTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateSimulationApplicationRequestRequestTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionRequestRequestTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "CreateSimulationJobRequestRequestTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "CreateWorldExportJobRequestRequestTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "CreateWorldGenerationJobRequestRequestTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "CreateWorldTemplateRequestRequestTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteRobotApplicationRequestRequestTypeDef",
    "DeleteRobotRequestRequestTypeDef",
    "DeleteSimulationApplicationRequestRequestTypeDef",
    "DeleteWorldTemplateRequestRequestTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeregisterRobotRequestRequestTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeDeploymentJobRequestRequestTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "DescribeFleetRequestRequestTypeDef",
    "DescribeFleetResponseTypeDef",
    "DescribeRobotApplicationRequestRequestTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "DescribeRobotRequestRequestTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeSimulationApplicationRequestRequestTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "DescribeSimulationJobBatchRequestRequestTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "DescribeSimulationJobRequestRequestTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "DescribeWorldExportJobRequestRequestTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "DescribeWorldGenerationJobRequestRequestTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "DescribeWorldRequestRequestTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateRequestRequestTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "EnvironmentTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FilterTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyRequestRequestTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "LaunchConfigTypeDef",
    "ListDeploymentJobsRequestRequestTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListRobotApplicationsRequestRequestTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListRobotsRequestRequestTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationApplicationsRequestRequestTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListSimulationJobBatchesRequestRequestTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListSimulationJobsRequestRequestTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorldExportJobsRequestRequestTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsRequestRequestTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "ListWorldTemplatesRequestRequestTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsRequestRequestTypeDef",
    "ListWorldsResponseTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PaginatorConfigTypeDef",
    "PortForwardingConfigTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotRequestRequestTypeDef",
    "RegisterRobotResponseTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadataTypeDef",
    "RestartSimulationJobRequestRequestTypeDef",
    "RobotApplicationConfigTypeDef",
    "RobotApplicationSummaryTypeDef",
    "RobotDeploymentTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "RobotTypeDef",
    "S3KeyOutputTypeDef",
    "S3ObjectTypeDef",
    "SimulationApplicationConfigTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "SimulationJobRequestTypeDef",
    "SimulationJobSummaryTypeDef",
    "SimulationJobTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "SourceConfigTypeDef",
    "SourceTypeDef",
    "StartSimulationJobBatchRequestRequestTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "SyncDeploymentJobRequestRequestTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateLocationTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRobotApplicationRequestRequestTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "UpdateSimulationApplicationRequestRequestTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "UpdateWorldTemplateRequestRequestTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
    "UploadConfigurationTypeDef",
    "VPCConfigResponseTypeDef",
    "VPCConfigTypeDef",
    "WorldConfigTypeDef",
    "WorldCountTypeDef",
    "WorldExportJobSummaryTypeDef",
    "WorldFailureTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "WorldSummaryTypeDef",
)

BatchDeleteWorldsRequestRequestTypeDef = TypedDict(
    "BatchDeleteWorldsRequestRequestTypeDef",
    {
        "worlds": Sequence[str],
    },
)

BatchDeleteWorldsResponseTypeDef = TypedDict(
    "BatchDeleteWorldsResponseTypeDef",
    {
        "unprocessedWorlds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeSimulationJobRequestRequestTypeDef = TypedDict(
    "BatchDescribeSimulationJobRequestRequestTypeDef",
    {
        "jobs": Sequence[str],
    },
)

BatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List["SimulationJobTypeDef"],
        "unprocessedJobs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPolicyTypeDef = TypedDict(
    "BatchPolicyTypeDef",
    {
        "timeoutInSeconds": NotRequired[int],
        "maxConcurrency": NotRequired[int],
    },
)

CancelDeploymentJobRequestRequestTypeDef = TypedDict(
    "CancelDeploymentJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

CancelSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "CancelSimulationJobBatchRequestRequestTypeDef",
    {
        "batch": str,
    },
)

CancelSimulationJobRequestRequestTypeDef = TypedDict(
    "CancelSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

CancelWorldExportJobRequestRequestTypeDef = TypedDict(
    "CancelWorldExportJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

CancelWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "CancelWorldGenerationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

ComputeResponseTypeDef = TypedDict(
    "ComputeResponseTypeDef",
    {
        "simulationUnitLimit": NotRequired[int],
        "computeType": NotRequired[ComputeTypeType],
        "gpuUnitLimit": NotRequired[int],
    },
)

ComputeTypeDef = TypedDict(
    "ComputeTypeDef",
    {
        "simulationUnitLimit": NotRequired[int],
        "computeType": NotRequired[ComputeTypeType],
        "gpuUnitLimit": NotRequired[int],
    },
)

CreateDeploymentJobRequestRequestTypeDef = TypedDict(
    "CreateDeploymentJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
        "deploymentApplicationConfigs": Sequence["DeploymentApplicationConfigTypeDef"],
        "deploymentConfig": NotRequired["DeploymentConfigTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateDeploymentJobResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "name": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRobotApplicationRequestRequestTypeDef = TypedDict(
    "CreateRobotApplicationRequestRequestTypeDef",
    {
        "name": str,
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "sources": NotRequired[Sequence["SourceConfigTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
        "environment": NotRequired["EnvironmentTypeDef"],
    },
)

CreateRobotApplicationResponseTypeDef = TypedDict(
    "CreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRobotApplicationVersionRequestRequestTypeDef = TypedDict(
    "CreateRobotApplicationVersionRequestRequestTypeDef",
    {
        "application": str,
        "currentRevisionId": NotRequired[str],
        "s3Etags": NotRequired[Sequence[str]],
        "imageDigest": NotRequired[str],
    },
)

CreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "CreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRobotRequestRequestTypeDef = TypedDict(
    "CreateRobotRequestRequestTypeDef",
    {
        "name": str,
        "architecture": ArchitectureType,
        "greengrassGroupId": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateRobotResponseTypeDef = TypedDict(
    "CreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": ArchitectureType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "CreateSimulationApplicationRequestRequestTypeDef",
    {
        "name": str,
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "sources": NotRequired[Sequence["SourceConfigTypeDef"]],
        "renderingEngine": NotRequired["RenderingEngineTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
        "environment": NotRequired["EnvironmentTypeDef"],
    },
)

CreateSimulationApplicationResponseTypeDef = TypedDict(
    "CreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSimulationApplicationVersionRequestRequestTypeDef = TypedDict(
    "CreateSimulationApplicationVersionRequestRequestTypeDef",
    {
        "application": str,
        "currentRevisionId": NotRequired[str],
        "s3Etags": NotRequired[Sequence[str]],
        "imageDigest": NotRequired[str],
    },
)

CreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "CreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSimulationJobRequestRequestTypeDef = TypedDict(
    "CreateSimulationJobRequestRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "iamRole": str,
        "clientRequestToken": NotRequired[str],
        "outputLocation": NotRequired["OutputLocationTypeDef"],
        "loggingConfig": NotRequired["LoggingConfigTypeDef"],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "robotApplications": NotRequired[Sequence["RobotApplicationConfigTypeDef"]],
        "simulationApplications": NotRequired[Sequence["SimulationApplicationConfigTypeDef"]],
        "dataSources": NotRequired[Sequence["DataSourceConfigTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
        "vpcConfig": NotRequired["VPCConfigTypeDef"],
        "compute": NotRequired["ComputeTypeDef"],
    },
)

CreateSimulationJobResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "compute": "ComputeResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorldExportJobRequestRequestTypeDef = TypedDict(
    "CreateWorldExportJobRequestRequestTypeDef",
    {
        "worlds": Sequence[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateWorldExportJobResponseTypeDef = TypedDict(
    "CreateWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "CreateWorldGenerationJobRequestRequestTypeDef",
    {
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "clientRequestToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "worldTags": NotRequired[Mapping[str, str]],
    },
)

CreateWorldGenerationJobResponseTypeDef = TypedDict(
    "CreateWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorldTemplateRequestRequestTypeDef = TypedDict(
    "CreateWorldTemplateRequestRequestTypeDef",
    {
        "clientRequestToken": NotRequired[str],
        "name": NotRequired[str],
        "templateBody": NotRequired[str],
        "templateLocation": NotRequired["TemplateLocationTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateWorldTemplateResponseTypeDef = TypedDict(
    "CreateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "createdAt": datetime,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": Sequence[str],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "name": NotRequired[str],
        "s3Bucket": NotRequired[str],
        "s3Keys": NotRequired[List["S3KeyOutputTypeDef"]],
        "type": NotRequired[DataSourceTypeType],
        "destination": NotRequired[str],
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleet": str,
    },
)

DeleteRobotApplicationRequestRequestTypeDef = TypedDict(
    "DeleteRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)

DeleteRobotRequestRequestTypeDef = TypedDict(
    "DeleteRobotRequestRequestTypeDef",
    {
        "robot": str,
    },
)

DeleteSimulationApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)

DeleteWorldTemplateRequestRequestTypeDef = TypedDict(
    "DeleteWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
)

DeploymentApplicationConfigTypeDef = TypedDict(
    "DeploymentApplicationConfigTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": "DeploymentLaunchConfigTypeDef",
    },
)

DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": NotRequired[int],
        "failureThresholdPercentage": NotRequired[int],
        "robotDeploymentTimeoutInSeconds": NotRequired[int],
        "downloadConditionFile": NotRequired["S3ObjectTypeDef"],
    },
)

DeploymentJobTypeDef = TypedDict(
    "DeploymentJobTypeDef",
    {
        "arn": NotRequired[str],
        "fleet": NotRequired[str],
        "status": NotRequired[DeploymentStatusType],
        "deploymentApplicationConfigs": NotRequired[List["DeploymentApplicationConfigTypeDef"]],
        "deploymentConfig": NotRequired["DeploymentConfigTypeDef"],
        "failureReason": NotRequired[str],
        "failureCode": NotRequired[DeploymentJobErrorCodeType],
        "createdAt": NotRequired[datetime],
    },
)

DeploymentLaunchConfigTypeDef = TypedDict(
    "DeploymentLaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
        "preLaunchFile": NotRequired[str],
        "postLaunchFile": NotRequired[str],
        "environmentVariables": NotRequired[Mapping[str, str]],
    },
)

DeregisterRobotRequestRequestTypeDef = TypedDict(
    "DeregisterRobotRequestRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)

DeregisterRobotResponseTypeDef = TypedDict(
    "DeregisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeploymentJobRequestRequestTypeDef = TypedDict(
    "DescribeDeploymentJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeDeploymentJobResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "robotDeploymentSummary": List["RobotDeploymentTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetRequestRequestTypeDef = TypedDict(
    "DescribeFleetRequestRequestTypeDef",
    {
        "fleet": str,
    },
)

DescribeFleetResponseTypeDef = TypedDict(
    "DescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List["RobotTypeDef"],
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRobotApplicationRequestRequestTypeDef = TypedDict(
    "DescribeRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)

DescribeRobotApplicationResponseTypeDef = TypedDict(
    "DescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "environment": "EnvironmentTypeDef",
        "imageDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRobotRequestRequestTypeDef = TypedDict(
    "DescribeRobotRequestRequestTypeDef",
    {
        "robot": str,
    },
)

DescribeRobotResponseTypeDef = TypedDict(
    "DescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": RobotStatusType,
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": ArchitectureType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationApplicationRequestRequestTypeDef = TypedDict(
    "DescribeSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "applicationVersion": NotRequired[str],
    },
)

DescribeSimulationApplicationResponseTypeDef = TypedDict(
    "DescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "environment": "EnvironmentTypeDef",
        "imageDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "DescribeSimulationJobBatchRequestRequestTypeDef",
    {
        "batch": str,
    },
)

DescribeSimulationJobBatchResponseTypeDef = TypedDict(
    "DescribeSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationJobRequestRequestTypeDef = TypedDict(
    "DescribeSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeSimulationJobResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "compute": "ComputeResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldExportJobRequestRequestTypeDef = TypedDict(
    "DescribeWorldExportJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeWorldExportJobResponseTypeDef = TypedDict(
    "DescribeWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "worlds": List[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldGenerationJobRequestRequestTypeDef = TypedDict(
    "DescribeWorldGenerationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

DescribeWorldGenerationJobResponseTypeDef = TypedDict(
    "DescribeWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "finishedWorldsSummary": "FinishedWorldsSummaryTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldRequestRequestTypeDef = TypedDict(
    "DescribeWorldRequestRequestTypeDef",
    {
        "world": str,
    },
)

DescribeWorldResponseTypeDef = TypedDict(
    "DescribeWorldResponseTypeDef",
    {
        "arn": str,
        "generationJob": str,
        "template": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "worldDescriptionBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldTemplateRequestRequestTypeDef = TypedDict(
    "DescribeWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
    },
)

DescribeWorldTemplateResponseTypeDef = TypedDict(
    "DescribeWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "uri": NotRequired[str],
    },
)

FailedCreateSimulationJobRequestTypeDef = TypedDict(
    "FailedCreateSimulationJobRequestTypeDef",
    {
        "request": NotRequired["SimulationJobRequestTypeDef"],
        "failureReason": NotRequired[str],
        "failureCode": NotRequired[SimulationJobErrorCodeType],
        "failedAt": NotRequired[datetime],
    },
)

FailureSummaryTypeDef = TypedDict(
    "FailureSummaryTypeDef",
    {
        "totalFailureCount": NotRequired[int],
        "failures": NotRequired[List["WorldFailureTypeDef"]],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)

FinishedWorldsSummaryTypeDef = TypedDict(
    "FinishedWorldsSummaryTypeDef",
    {
        "finishedCount": NotRequired[int],
        "succeededWorlds": NotRequired[List[str]],
        "failureSummary": NotRequired["FailureSummaryTypeDef"],
    },
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastDeploymentStatus": NotRequired[DeploymentStatusType],
        "lastDeploymentJob": NotRequired[str],
        "lastDeploymentTime": NotRequired[datetime],
    },
)

GetWorldTemplateBodyRequestRequestTypeDef = TypedDict(
    "GetWorldTemplateBodyRequestRequestTypeDef",
    {
        "template": NotRequired[str],
        "generationJob": NotRequired[str],
    },
)

GetWorldTemplateBodyResponseTypeDef = TypedDict(
    "GetWorldTemplateBodyResponseTypeDef",
    {
        "templateBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchConfigTypeDef = TypedDict(
    "LaunchConfigTypeDef",
    {
        "packageName": NotRequired[str],
        "launchFile": NotRequired[str],
        "environmentVariables": NotRequired[Dict[str, str]],
        "portForwardingConfig": NotRequired["PortForwardingConfigTypeDef"],
        "streamUI": NotRequired[bool],
        "command": NotRequired[List[str]],
    },
)

ListDeploymentJobsRequestRequestTypeDef = TypedDict(
    "ListDeploymentJobsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List["DeploymentJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetDetails": List["FleetTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRobotApplicationsRequestRequestTypeDef = TypedDict(
    "ListRobotApplicationsRequestRequestTypeDef",
    {
        "versionQualifier": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List["RobotApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRobotsRequestRequestTypeDef = TypedDict(
    "ListRobotsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef",
    {
        "robots": List["RobotTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationApplicationsRequestRequestTypeDef = TypedDict(
    "ListSimulationApplicationsRequestRequestTypeDef",
    {
        "versionQualifier": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List["SimulationApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationJobBatchesRequestRequestTypeDef = TypedDict(
    "ListSimulationJobBatchesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseTypeDef",
    {
        "simulationJobBatchSummaries": List["SimulationJobBatchSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationJobsRequestRequestTypeDef = TypedDict(
    "ListSimulationJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListSimulationJobsResponseTypeDef = TypedDict(
    "ListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List["SimulationJobSummaryTypeDef"],
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

ListWorldExportJobsRequestRequestTypeDef = TypedDict(
    "ListWorldExportJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListWorldExportJobsResponseTypeDef = TypedDict(
    "ListWorldExportJobsResponseTypeDef",
    {
        "worldExportJobSummaries": List["WorldExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldGenerationJobsRequestRequestTypeDef = TypedDict(
    "ListWorldGenerationJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListWorldGenerationJobsResponseTypeDef = TypedDict(
    "ListWorldGenerationJobsResponseTypeDef",
    {
        "worldGenerationJobSummaries": List["WorldGenerationJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldTemplatesRequestRequestTypeDef = TypedDict(
    "ListWorldTemplatesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListWorldTemplatesResponseTypeDef = TypedDict(
    "ListWorldTemplatesResponseTypeDef",
    {
        "templateSummaries": List["TemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldsRequestRequestTypeDef = TypedDict(
    "ListWorldsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListWorldsResponseTypeDef = TypedDict(
    "ListWorldsResponseTypeDef",
    {
        "worldSummaries": List["WorldSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "recordAllRosTopics": NotRequired[bool],
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "publicIpAddress": NotRequired[str],
    },
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Prefix": NotRequired[str],
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

PortForwardingConfigTypeDef = TypedDict(
    "PortForwardingConfigTypeDef",
    {
        "portMappings": NotRequired[List["PortMappingTypeDef"]],
    },
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "jobPort": int,
        "applicationPort": int,
        "enableOnPublicIp": NotRequired[bool],
    },
)

ProgressDetailTypeDef = TypedDict(
    "ProgressDetailTypeDef",
    {
        "currentProgress": NotRequired[RobotDeploymentStepType],
        "percentDone": NotRequired[float],
        "estimatedTimeRemainingSeconds": NotRequired[int],
        "targetResource": NotRequired[str],
    },
)

RegisterRobotRequestRequestTypeDef = TypedDict(
    "RegisterRobotRequestRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)

RegisterRobotResponseTypeDef = TypedDict(
    "RegisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenderingEngineTypeDef = TypedDict(
    "RenderingEngineTypeDef",
    {
        "name": NotRequired[Literal["OGRE"]],
        "version": NotRequired[str],
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

RestartSimulationJobRequestRequestTypeDef = TypedDict(
    "RestartSimulationJobRequestRequestTypeDef",
    {
        "job": str,
    },
)

RobotApplicationConfigTypeDef = TypedDict(
    "RobotApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": "LaunchConfigTypeDef",
        "applicationVersion": NotRequired[str],
        "uploadConfigurations": NotRequired[List["UploadConfigurationTypeDef"]],
        "useDefaultUploadConfigurations": NotRequired[bool],
        "tools": NotRequired[List["ToolTypeDef"]],
        "useDefaultTools": NotRequired[bool],
    },
)

RobotApplicationSummaryTypeDef = TypedDict(
    "RobotApplicationSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "robotSoftwareSuite": NotRequired["RobotSoftwareSuiteTypeDef"],
    },
)

RobotDeploymentTypeDef = TypedDict(
    "RobotDeploymentTypeDef",
    {
        "arn": NotRequired[str],
        "deploymentStartTime": NotRequired[datetime],
        "deploymentFinishTime": NotRequired[datetime],
        "status": NotRequired[RobotStatusType],
        "progressDetail": NotRequired["ProgressDetailTypeDef"],
        "failureReason": NotRequired[str],
        "failureCode": NotRequired[DeploymentJobErrorCodeType],
    },
)

RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {
        "name": NotRequired[RobotSoftwareSuiteTypeType],
        "version": NotRequired[RobotSoftwareSuiteVersionTypeType],
    },
)

RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "fleetArn": NotRequired[str],
        "status": NotRequired[RobotStatusType],
        "greenGrassGroupId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "architecture": NotRequired[ArchitectureType],
        "lastDeploymentJob": NotRequired[str],
        "lastDeploymentTime": NotRequired[datetime],
    },
)

S3KeyOutputTypeDef = TypedDict(
    "S3KeyOutputTypeDef",
    {
        "s3Key": NotRequired[str],
        "etag": NotRequired[str],
    },
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucket": str,
        "key": str,
        "etag": NotRequired[str],
    },
)

SimulationApplicationConfigTypeDef = TypedDict(
    "SimulationApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": "LaunchConfigTypeDef",
        "applicationVersion": NotRequired[str],
        "uploadConfigurations": NotRequired[List["UploadConfigurationTypeDef"]],
        "worldConfigs": NotRequired[List["WorldConfigTypeDef"]],
        "useDefaultUploadConfigurations": NotRequired[bool],
        "tools": NotRequired[List["ToolTypeDef"]],
        "useDefaultTools": NotRequired[bool],
    },
)

SimulationApplicationSummaryTypeDef = TypedDict(
    "SimulationApplicationSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "robotSoftwareSuite": NotRequired["RobotSoftwareSuiteTypeDef"],
        "simulationSoftwareSuite": NotRequired["SimulationSoftwareSuiteTypeDef"],
    },
)

SimulationJobBatchSummaryTypeDef = TypedDict(
    "SimulationJobBatchSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[SimulationJobBatchStatusType],
        "failedRequestCount": NotRequired[int],
        "pendingRequestCount": NotRequired[int],
        "createdRequestCount": NotRequired[int],
    },
)

SimulationJobRequestTypeDef = TypedDict(
    "SimulationJobRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "outputLocation": NotRequired["OutputLocationTypeDef"],
        "loggingConfig": NotRequired["LoggingConfigTypeDef"],
        "iamRole": NotRequired[str],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "useDefaultApplications": NotRequired[bool],
        "robotApplications": NotRequired[List["RobotApplicationConfigTypeDef"]],
        "simulationApplications": NotRequired[List["SimulationApplicationConfigTypeDef"]],
        "dataSources": NotRequired[List["DataSourceConfigTypeDef"]],
        "vpcConfig": NotRequired["VPCConfigTypeDef"],
        "compute": NotRequired["ComputeTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

SimulationJobSummaryTypeDef = TypedDict(
    "SimulationJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "status": NotRequired[SimulationJobStatusType],
        "simulationApplicationNames": NotRequired[List[str]],
        "robotApplicationNames": NotRequired[List[str]],
        "dataSourceNames": NotRequired[List[str]],
        "computeType": NotRequired[ComputeTypeType],
    },
)

SimulationJobTypeDef = TypedDict(
    "SimulationJobTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[SimulationJobStatusType],
        "lastStartedAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "failureBehavior": NotRequired[FailureBehaviorType],
        "failureCode": NotRequired[SimulationJobErrorCodeType],
        "failureReason": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "outputLocation": NotRequired["OutputLocationTypeDef"],
        "loggingConfig": NotRequired["LoggingConfigTypeDef"],
        "maxJobDurationInSeconds": NotRequired[int],
        "simulationTimeMillis": NotRequired[int],
        "iamRole": NotRequired[str],
        "robotApplications": NotRequired[List["RobotApplicationConfigTypeDef"]],
        "simulationApplications": NotRequired[List["SimulationApplicationConfigTypeDef"]],
        "dataSources": NotRequired[List["DataSourceTypeDef"]],
        "tags": NotRequired[Dict[str, str]],
        "vpcConfig": NotRequired["VPCConfigResponseTypeDef"],
        "networkInterface": NotRequired["NetworkInterfaceTypeDef"],
        "compute": NotRequired["ComputeResponseTypeDef"],
    },
)

SimulationSoftwareSuiteTypeDef = TypedDict(
    "SimulationSoftwareSuiteTypeDef",
    {
        "name": NotRequired[SimulationSoftwareSuiteTypeType],
        "version": NotRequired[str],
    },
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Key": NotRequired[str],
        "architecture": NotRequired[ArchitectureType],
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Key": NotRequired[str],
        "etag": NotRequired[str],
        "architecture": NotRequired[ArchitectureType],
    },
)

StartSimulationJobBatchRequestRequestTypeDef = TypedDict(
    "StartSimulationJobBatchRequestRequestTypeDef",
    {
        "createSimulationJobRequests": Sequence["SimulationJobRequestTypeDef"],
        "clientRequestToken": NotRequired[str],
        "batchPolicy": NotRequired["BatchPolicyTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartSimulationJobBatchResponseTypeDef = TypedDict(
    "StartSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncDeploymentJobRequestRequestTypeDef = TypedDict(
    "SyncDeploymentJobRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
    },
)

SyncDeploymentJobResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
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

TemplateLocationTypeDef = TypedDict(
    "TemplateLocationTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "version": NotRequired[str],
    },
)

ToolTypeDef = TypedDict(
    "ToolTypeDef",
    {
        "name": str,
        "command": str,
        "streamUI": NotRequired[bool],
        "streamOutputToCloudWatch": NotRequired[bool],
        "exitBehavior": NotRequired[ExitBehaviorType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateRobotApplicationRequestRequestTypeDef = TypedDict(
    "UpdateRobotApplicationRequestRequestTypeDef",
    {
        "application": str,
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "sources": NotRequired[Sequence["SourceConfigTypeDef"]],
        "currentRevisionId": NotRequired[str],
        "environment": NotRequired["EnvironmentTypeDef"],
    },
)

UpdateRobotApplicationResponseTypeDef = TypedDict(
    "UpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSimulationApplicationRequestRequestTypeDef = TypedDict(
    "UpdateSimulationApplicationRequestRequestTypeDef",
    {
        "application": str,
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "sources": NotRequired[Sequence["SourceConfigTypeDef"]],
        "renderingEngine": NotRequired["RenderingEngineTypeDef"],
        "currentRevisionId": NotRequired[str],
        "environment": NotRequired["EnvironmentTypeDef"],
    },
)

UpdateSimulationApplicationResponseTypeDef = TypedDict(
    "UpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorldTemplateRequestRequestTypeDef = TypedDict(
    "UpdateWorldTemplateRequestRequestTypeDef",
    {
        "template": str,
        "name": NotRequired[str],
        "templateBody": NotRequired[str],
        "templateLocation": NotRequired["TemplateLocationTypeDef"],
    },
)

UpdateWorldTemplateResponseTypeDef = TypedDict(
    "UpdateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadConfigurationTypeDef = TypedDict(
    "UploadConfigurationTypeDef",
    {
        "name": str,
        "path": str,
        "uploadBehavior": UploadBehaviorType,
    },
)

VPCConfigResponseTypeDef = TypedDict(
    "VPCConfigResponseTypeDef",
    {
        "subnets": NotRequired[List[str]],
        "securityGroups": NotRequired[List[str]],
        "vpcId": NotRequired[str],
        "assignPublicIp": NotRequired[bool],
    },
)

VPCConfigTypeDef = TypedDict(
    "VPCConfigTypeDef",
    {
        "subnets": Sequence[str],
        "securityGroups": NotRequired[Sequence[str]],
        "assignPublicIp": NotRequired[bool],
    },
)

WorldConfigTypeDef = TypedDict(
    "WorldConfigTypeDef",
    {
        "world": NotRequired[str],
    },
)

WorldCountTypeDef = TypedDict(
    "WorldCountTypeDef",
    {
        "floorplanCount": NotRequired[int],
        "interiorCountPerFloorplan": NotRequired[int],
    },
)

WorldExportJobSummaryTypeDef = TypedDict(
    "WorldExportJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "status": NotRequired[WorldExportJobStatusType],
        "createdAt": NotRequired[datetime],
        "worlds": NotRequired[List[str]],
        "outputLocation": NotRequired["OutputLocationTypeDef"],
    },
)

WorldFailureTypeDef = TypedDict(
    "WorldFailureTypeDef",
    {
        "failureCode": NotRequired[WorldGenerationJobErrorCodeType],
        "sampleFailureReason": NotRequired[str],
        "failureCount": NotRequired[int],
    },
)

WorldGenerationJobSummaryTypeDef = TypedDict(
    "WorldGenerationJobSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "template": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[WorldGenerationJobStatusType],
        "worldCount": NotRequired["WorldCountTypeDef"],
        "succeededWorldCount": NotRequired[int],
        "failedWorldCount": NotRequired[int],
    },
)

WorldSummaryTypeDef = TypedDict(
    "WorldSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "generationJob": NotRequired[str],
        "template": NotRequired[str],
    },
)
