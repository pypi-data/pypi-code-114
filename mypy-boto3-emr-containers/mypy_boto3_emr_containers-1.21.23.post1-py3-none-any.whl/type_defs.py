"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunRequestRequestTypeDef

    data: CancelJobRunRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EndpointStateType,
    FailureReasonType,
    JobRunStateType,
    PersistentAppUIType,
    VirtualClusterStateType,
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
    "CancelJobRunRequestRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CertificateTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationTypeDef",
    "ContainerInfoTypeDef",
    "ContainerProviderTypeDef",
    "CreateManagedEndpointRequestRequestTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateVirtualClusterRequestRequestTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "DeleteManagedEndpointRequestRequestTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterRequestRequestTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeManagedEndpointRequestRequestTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "DescribeVirtualClusterRequestRequestTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "EksInfoTypeDef",
    "EndpointTypeDef",
    "JobDriverTypeDef",
    "JobRunTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListManagedEndpointsRequestRequestTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersRequestRequestTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VirtualClusterTypeDef",
)

CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": NotRequired[str],
        "certificateData": NotRequired[str],
    },
)

CloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "CloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": NotRequired[str],
    },
)

ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": NotRequired[Sequence["ConfigurationTypeDef"]],
        "monitoringConfiguration": NotRequired["MonitoringConfigurationTypeDef"],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "classification": str,
        "properties": NotRequired[Mapping[str, str]],
        "configurations": NotRequired[Sequence[Dict[str, Any]]],
    },
)

ContainerInfoTypeDef = TypedDict(
    "ContainerInfoTypeDef",
    {
        "eksInfo": NotRequired["EksInfoTypeDef"],
    },
)

ContainerProviderTypeDef = TypedDict(
    "ContainerProviderTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
        "info": NotRequired["ContainerInfoTypeDef"],
    },
)

CreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "CreateManagedEndpointRequestRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "clientToken": str,
        "certificateArn": NotRequired[str],
        "configurationOverrides": NotRequired["ConfigurationOverridesTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualClusterRequestRequestTypeDef = TypedDict(
    "CreateVirtualClusterRequestRequestTypeDef",
    {
        "name": str,
        "containerProvider": "ContainerProviderTypeDef",
        "clientToken": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteManagedEndpointRequestRequestTypeDef = TypedDict(
    "DeleteManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualClusterRequestRequestTypeDef = TypedDict(
    "DeleteVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "jobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedEndpointRequestRequestTypeDef = TypedDict(
    "DescribeManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeManagedEndpointResponseTypeDef = TypedDict(
    "DescribeManagedEndpointResponseTypeDef",
    {
        "endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualClusterRequestRequestTypeDef = TypedDict(
    "DescribeVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeVirtualClusterResponseTypeDef = TypedDict(
    "DescribeVirtualClusterResponseTypeDef",
    {
        "virtualCluster": "VirtualClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EksInfoTypeDef = TypedDict(
    "EksInfoTypeDef",
    {
        "namespace": NotRequired[str],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "type": NotRequired[str],
        "state": NotRequired[EndpointStateType],
        "releaseLabel": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "certificateAuthority": NotRequired["CertificateTypeDef"],
        "configurationOverrides": NotRequired["ConfigurationOverridesTypeDef"],
        "serverUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "securityGroup": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
    },
)

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmitJobDriver": NotRequired["SparkSubmitJobDriverTypeDef"],
    },
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[JobRunStateType],
        "clientToken": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "configurationOverrides": NotRequired["ConfigurationOverridesTypeDef"],
        "jobDriver": NotRequired["JobDriverTypeDef"],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "finishedAt": NotRequired[datetime],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
    },
)

ListJobRunsRequestRequestTypeDef = TypedDict(
    "ListJobRunsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[Union[datetime, str]],
        "createdAfter": NotRequired[Union[datetime, str]],
        "name": NotRequired[str],
        "states": NotRequired[Sequence[JobRunStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List["JobRunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedEndpointsRequestRequestTypeDef = TypedDict(
    "ListManagedEndpointsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[Union[datetime, str]],
        "createdAfter": NotRequired[Union[datetime, str]],
        "types": NotRequired[Sequence[str]],
        "states": NotRequired[Sequence[EndpointStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListManagedEndpointsResponseTypeDef = TypedDict(
    "ListManagedEndpointsResponseTypeDef",
    {
        "endpoints": List["EndpointTypeDef"],
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

ListVirtualClustersRequestRequestTypeDef = TypedDict(
    "ListVirtualClustersRequestRequestTypeDef",
    {
        "containerProviderId": NotRequired[str],
        "containerProviderType": NotRequired[Literal["EKS"]],
        "createdAfter": NotRequired[Union[datetime, str]],
        "createdBefore": NotRequired[Union[datetime, str]],
        "states": NotRequired[Sequence[VirtualClusterStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListVirtualClustersResponseTypeDef = TypedDict(
    "ListVirtualClustersResponseTypeDef",
    {
        "virtualClusters": List["VirtualClusterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "persistentAppUI": NotRequired[PersistentAppUIType],
        "cloudWatchMonitoringConfiguration": NotRequired[
            "CloudWatchMonitoringConfigurationTypeDef"
        ],
        "s3MonitoringConfiguration": NotRequired["S3MonitoringConfigurationTypeDef"],
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

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
    },
)

SparkSubmitJobDriverTypeDef = TypedDict(
    "SparkSubmitJobDriverTypeDef",
    {
        "entryPoint": str,
        "entryPointArguments": NotRequired[List[str]],
        "sparkSubmitParameters": NotRequired[str],
    },
)

StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": "JobDriverTypeDef",
        "name": NotRequired[str],
        "configurationOverrides": NotRequired["ConfigurationOverridesTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[VirtualClusterStateType],
        "containerProvider": NotRequired["ContainerProviderTypeDef"],
        "createdAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
