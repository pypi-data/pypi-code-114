"""
Type annotations for kafkaconnect service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kafkaconnect/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kafkaconnect.type_defs import ApacheKafkaClusterDescriptionTypeDef

    data: ApacheKafkaClusterDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ConnectorStateType,
    CustomPluginContentTypeType,
    CustomPluginStateType,
    KafkaClusterClientAuthenticationTypeType,
    KafkaClusterEncryptionInTransitTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApacheKafkaClusterDescriptionTypeDef",
    "ApacheKafkaClusterTypeDef",
    "AutoScalingDescriptionTypeDef",
    "AutoScalingTypeDef",
    "AutoScalingUpdateTypeDef",
    "CapacityDescriptionTypeDef",
    "CapacityTypeDef",
    "CapacityUpdateTypeDef",
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    "CloudWatchLogsLogDeliveryTypeDef",
    "ConnectorSummaryTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateCustomPluginRequestRequestTypeDef",
    "CreateCustomPluginResponseTypeDef",
    "CreateWorkerConfigurationRequestRequestTypeDef",
    "CreateWorkerConfigurationResponseTypeDef",
    "CustomPluginDescriptionTypeDef",
    "CustomPluginFileDescriptionTypeDef",
    "CustomPluginLocationDescriptionTypeDef",
    "CustomPluginLocationTypeDef",
    "CustomPluginRevisionSummaryTypeDef",
    "CustomPluginSummaryTypeDef",
    "CustomPluginTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteConnectorResponseTypeDef",
    "DeleteCustomPluginRequestRequestTypeDef",
    "DeleteCustomPluginResponseTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeCustomPluginRequestRequestTypeDef",
    "DescribeCustomPluginResponseTypeDef",
    "DescribeWorkerConfigurationRequestRequestTypeDef",
    "DescribeWorkerConfigurationResponseTypeDef",
    "FirehoseLogDeliveryDescriptionTypeDef",
    "FirehoseLogDeliveryTypeDef",
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    "KafkaClusterClientAuthenticationTypeDef",
    "KafkaClusterDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitTypeDef",
    "KafkaClusterTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListCustomPluginsRequestRequestTypeDef",
    "ListCustomPluginsResponseTypeDef",
    "ListWorkerConfigurationsRequestRequestTypeDef",
    "ListWorkerConfigurationsResponseTypeDef",
    "LogDeliveryDescriptionTypeDef",
    "LogDeliveryTypeDef",
    "PaginatorConfigTypeDef",
    "PluginDescriptionTypeDef",
    "PluginTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "ProvisionedCapacityTypeDef",
    "ProvisionedCapacityUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationDescriptionTypeDef",
    "S3LocationTypeDef",
    "S3LogDeliveryDescriptionTypeDef",
    "S3LogDeliveryTypeDef",
    "ScaleInPolicyDescriptionTypeDef",
    "ScaleInPolicyTypeDef",
    "ScaleInPolicyUpdateTypeDef",
    "ScaleOutPolicyDescriptionTypeDef",
    "ScaleOutPolicyTypeDef",
    "ScaleOutPolicyUpdateTypeDef",
    "StateDescriptionTypeDef",
    "UpdateConnectorRequestRequestTypeDef",
    "UpdateConnectorResponseTypeDef",
    "VpcDescriptionTypeDef",
    "VpcTypeDef",
    "WorkerConfigurationDescriptionTypeDef",
    "WorkerConfigurationRevisionDescriptionTypeDef",
    "WorkerConfigurationRevisionSummaryTypeDef",
    "WorkerConfigurationSummaryTypeDef",
    "WorkerConfigurationTypeDef",
    "WorkerLogDeliveryDescriptionTypeDef",
    "WorkerLogDeliveryTypeDef",
)

ApacheKafkaClusterDescriptionTypeDef = TypedDict(
    "ApacheKafkaClusterDescriptionTypeDef",
    {
        "bootstrapServers": NotRequired[str],
        "vpc": NotRequired["VpcDescriptionTypeDef"],
    },
)

ApacheKafkaClusterTypeDef = TypedDict(
    "ApacheKafkaClusterTypeDef",
    {
        "bootstrapServers": str,
        "vpc": "VpcTypeDef",
    },
)

AutoScalingDescriptionTypeDef = TypedDict(
    "AutoScalingDescriptionTypeDef",
    {
        "maxWorkerCount": NotRequired[int],
        "mcuCount": NotRequired[int],
        "minWorkerCount": NotRequired[int],
        "scaleInPolicy": NotRequired["ScaleInPolicyDescriptionTypeDef"],
        "scaleOutPolicy": NotRequired["ScaleOutPolicyDescriptionTypeDef"],
    },
)

AutoScalingTypeDef = TypedDict(
    "AutoScalingTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
        "scaleInPolicy": NotRequired["ScaleInPolicyTypeDef"],
        "scaleOutPolicy": NotRequired["ScaleOutPolicyTypeDef"],
    },
)

AutoScalingUpdateTypeDef = TypedDict(
    "AutoScalingUpdateTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
        "scaleInPolicy": "ScaleInPolicyUpdateTypeDef",
        "scaleOutPolicy": "ScaleOutPolicyUpdateTypeDef",
    },
)

CapacityDescriptionTypeDef = TypedDict(
    "CapacityDescriptionTypeDef",
    {
        "autoScaling": NotRequired["AutoScalingDescriptionTypeDef"],
        "provisionedCapacity": NotRequired["ProvisionedCapacityDescriptionTypeDef"],
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "autoScaling": NotRequired["AutoScalingTypeDef"],
        "provisionedCapacity": NotRequired["ProvisionedCapacityTypeDef"],
    },
)

CapacityUpdateTypeDef = TypedDict(
    "CapacityUpdateTypeDef",
    {
        "autoScaling": NotRequired["AutoScalingUpdateTypeDef"],
        "provisionedCapacity": NotRequired["ProvisionedCapacityUpdateTypeDef"],
    },
)

CloudWatchLogsLogDeliveryDescriptionTypeDef = TypedDict(
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    {
        "enabled": NotRequired[bool],
        "logGroup": NotRequired[str],
    },
)

CloudWatchLogsLogDeliveryTypeDef = TypedDict(
    "CloudWatchLogsLogDeliveryTypeDef",
    {
        "enabled": bool,
        "logGroup": NotRequired[str],
    },
)

ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "capacity": NotRequired["CapacityDescriptionTypeDef"],
        "connectorArn": NotRequired[str],
        "connectorDescription": NotRequired[str],
        "connectorName": NotRequired[str],
        "connectorState": NotRequired[ConnectorStateType],
        "creationTime": NotRequired[datetime],
        "currentVersion": NotRequired[str],
        "kafkaCluster": NotRequired["KafkaClusterDescriptionTypeDef"],
        "kafkaClusterClientAuthentication": NotRequired[
            "KafkaClusterClientAuthenticationDescriptionTypeDef"
        ],
        "kafkaClusterEncryptionInTransit": NotRequired[
            "KafkaClusterEncryptionInTransitDescriptionTypeDef"
        ],
        "kafkaConnectVersion": NotRequired[str],
        "logDelivery": NotRequired["LogDeliveryDescriptionTypeDef"],
        "plugins": NotRequired[List["PluginDescriptionTypeDef"]],
        "serviceExecutionRoleArn": NotRequired[str],
        "workerConfiguration": NotRequired["WorkerConfigurationDescriptionTypeDef"],
    },
)

CreateConnectorRequestRequestTypeDef = TypedDict(
    "CreateConnectorRequestRequestTypeDef",
    {
        "capacity": "CapacityTypeDef",
        "connectorConfiguration": Mapping[str, str],
        "connectorName": str,
        "kafkaCluster": "KafkaClusterTypeDef",
        "kafkaClusterClientAuthentication": "KafkaClusterClientAuthenticationTypeDef",
        "kafkaClusterEncryptionInTransit": "KafkaClusterEncryptionInTransitTypeDef",
        "kafkaConnectVersion": str,
        "plugins": Sequence["PluginTypeDef"],
        "serviceExecutionRoleArn": str,
        "connectorDescription": NotRequired[str],
        "logDelivery": NotRequired["LogDeliveryTypeDef"],
        "workerConfiguration": NotRequired["WorkerConfigurationTypeDef"],
    },
)

CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomPluginRequestRequestTypeDef = TypedDict(
    "CreateCustomPluginRequestRequestTypeDef",
    {
        "contentType": CustomPluginContentTypeType,
        "location": "CustomPluginLocationTypeDef",
        "name": str,
        "description": NotRequired[str],
    },
)

CreateCustomPluginResponseTypeDef = TypedDict(
    "CreateCustomPluginResponseTypeDef",
    {
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "name": str,
        "revision": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "CreateWorkerConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "propertiesFileContent": str,
        "description": NotRequired[str],
    },
)

CreateWorkerConfigurationResponseTypeDef = TypedDict(
    "CreateWorkerConfigurationResponseTypeDef",
    {
        "creationTime": datetime,
        "latestRevision": "WorkerConfigurationRevisionSummaryTypeDef",
        "name": str,
        "workerConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomPluginDescriptionTypeDef = TypedDict(
    "CustomPluginDescriptionTypeDef",
    {
        "customPluginArn": NotRequired[str],
        "revision": NotRequired[int],
    },
)

CustomPluginFileDescriptionTypeDef = TypedDict(
    "CustomPluginFileDescriptionTypeDef",
    {
        "fileMd5": NotRequired[str],
        "fileSize": NotRequired[int],
    },
)

CustomPluginLocationDescriptionTypeDef = TypedDict(
    "CustomPluginLocationDescriptionTypeDef",
    {
        "s3Location": NotRequired["S3LocationDescriptionTypeDef"],
    },
)

CustomPluginLocationTypeDef = TypedDict(
    "CustomPluginLocationTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
)

CustomPluginRevisionSummaryTypeDef = TypedDict(
    "CustomPluginRevisionSummaryTypeDef",
    {
        "contentType": NotRequired[CustomPluginContentTypeType],
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "fileDescription": NotRequired["CustomPluginFileDescriptionTypeDef"],
        "location": NotRequired["CustomPluginLocationDescriptionTypeDef"],
        "revision": NotRequired[int],
    },
)

CustomPluginSummaryTypeDef = TypedDict(
    "CustomPluginSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "customPluginArn": NotRequired[str],
        "customPluginState": NotRequired[CustomPluginStateType],
        "description": NotRequired[str],
        "latestRevision": NotRequired["CustomPluginRevisionSummaryTypeDef"],
        "name": NotRequired[str],
    },
)

CustomPluginTypeDef = TypedDict(
    "CustomPluginTypeDef",
    {
        "customPluginArn": str,
        "revision": int,
    },
)

DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "connectorArn": str,
        "currentVersion": NotRequired[str],
    },
)

DeleteConnectorResponseTypeDef = TypedDict(
    "DeleteConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomPluginRequestRequestTypeDef = TypedDict(
    "DeleteCustomPluginRequestRequestTypeDef",
    {
        "customPluginArn": str,
    },
)

DeleteCustomPluginResponseTypeDef = TypedDict(
    "DeleteCustomPluginResponseTypeDef",
    {
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "connectorArn": str,
    },
)

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "capacity": "CapacityDescriptionTypeDef",
        "connectorArn": str,
        "connectorConfiguration": Dict[str, str],
        "connectorDescription": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "creationTime": datetime,
        "currentVersion": str,
        "kafkaCluster": "KafkaClusterDescriptionTypeDef",
        "kafkaClusterClientAuthentication": "KafkaClusterClientAuthenticationDescriptionTypeDef",
        "kafkaClusterEncryptionInTransit": "KafkaClusterEncryptionInTransitDescriptionTypeDef",
        "kafkaConnectVersion": str,
        "logDelivery": "LogDeliveryDescriptionTypeDef",
        "plugins": List["PluginDescriptionTypeDef"],
        "serviceExecutionRoleArn": str,
        "stateDescription": "StateDescriptionTypeDef",
        "workerConfiguration": "WorkerConfigurationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomPluginRequestRequestTypeDef = TypedDict(
    "DescribeCustomPluginRequestRequestTypeDef",
    {
        "customPluginArn": str,
    },
)

DescribeCustomPluginResponseTypeDef = TypedDict(
    "DescribeCustomPluginResponseTypeDef",
    {
        "creationTime": datetime,
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "description": str,
        "latestRevision": "CustomPluginRevisionSummaryTypeDef",
        "name": str,
        "stateDescription": "StateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeWorkerConfigurationRequestRequestTypeDef",
    {
        "workerConfigurationArn": str,
    },
)

DescribeWorkerConfigurationResponseTypeDef = TypedDict(
    "DescribeWorkerConfigurationResponseTypeDef",
    {
        "creationTime": datetime,
        "description": str,
        "latestRevision": "WorkerConfigurationRevisionDescriptionTypeDef",
        "name": str,
        "workerConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FirehoseLogDeliveryDescriptionTypeDef = TypedDict(
    "FirehoseLogDeliveryDescriptionTypeDef",
    {
        "deliveryStream": NotRequired[str],
        "enabled": NotRequired[bool],
    },
)

FirehoseLogDeliveryTypeDef = TypedDict(
    "FirehoseLogDeliveryTypeDef",
    {
        "enabled": bool,
        "deliveryStream": NotRequired[str],
    },
)

KafkaClusterClientAuthenticationDescriptionTypeDef = TypedDict(
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    {
        "authenticationType": NotRequired[KafkaClusterClientAuthenticationTypeType],
    },
)

KafkaClusterClientAuthenticationTypeDef = TypedDict(
    "KafkaClusterClientAuthenticationTypeDef",
    {
        "authenticationType": KafkaClusterClientAuthenticationTypeType,
    },
)

KafkaClusterDescriptionTypeDef = TypedDict(
    "KafkaClusterDescriptionTypeDef",
    {
        "apacheKafkaCluster": NotRequired["ApacheKafkaClusterDescriptionTypeDef"],
    },
)

KafkaClusterEncryptionInTransitDescriptionTypeDef = TypedDict(
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    {
        "encryptionType": NotRequired[KafkaClusterEncryptionInTransitTypeType],
    },
)

KafkaClusterEncryptionInTransitTypeDef = TypedDict(
    "KafkaClusterEncryptionInTransitTypeDef",
    {
        "encryptionType": KafkaClusterEncryptionInTransitTypeType,
    },
)

KafkaClusterTypeDef = TypedDict(
    "KafkaClusterTypeDef",
    {
        "apacheKafkaCluster": "ApacheKafkaClusterTypeDef",
    },
)

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "connectorNamePrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List["ConnectorSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomPluginsRequestRequestTypeDef = TypedDict(
    "ListCustomPluginsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListCustomPluginsResponseTypeDef = TypedDict(
    "ListCustomPluginsResponseTypeDef",
    {
        "customPlugins": List["CustomPluginSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkerConfigurationsRequestRequestTypeDef = TypedDict(
    "ListWorkerConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListWorkerConfigurationsResponseTypeDef = TypedDict(
    "ListWorkerConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "workerConfigurations": List["WorkerConfigurationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDeliveryDescriptionTypeDef = TypedDict(
    "LogDeliveryDescriptionTypeDef",
    {
        "workerLogDelivery": NotRequired["WorkerLogDeliveryDescriptionTypeDef"],
    },
)

LogDeliveryTypeDef = TypedDict(
    "LogDeliveryTypeDef",
    {
        "workerLogDelivery": "WorkerLogDeliveryTypeDef",
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

PluginDescriptionTypeDef = TypedDict(
    "PluginDescriptionTypeDef",
    {
        "customPlugin": NotRequired["CustomPluginDescriptionTypeDef"],
    },
)

PluginTypeDef = TypedDict(
    "PluginTypeDef",
    {
        "customPlugin": "CustomPluginTypeDef",
    },
)

ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "mcuCount": NotRequired[int],
        "workerCount": NotRequired[int],
    },
)

ProvisionedCapacityTypeDef = TypedDict(
    "ProvisionedCapacityTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
    },
)

ProvisionedCapacityUpdateTypeDef = TypedDict(
    "ProvisionedCapacityUpdateTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
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

S3LocationDescriptionTypeDef = TypedDict(
    "S3LocationDescriptionTypeDef",
    {
        "bucketArn": NotRequired[str],
        "fileKey": NotRequired[str],
        "objectVersion": NotRequired[str],
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketArn": str,
        "fileKey": str,
        "objectVersion": NotRequired[str],
    },
)

S3LogDeliveryDescriptionTypeDef = TypedDict(
    "S3LogDeliveryDescriptionTypeDef",
    {
        "bucket": NotRequired[str],
        "enabled": NotRequired[bool],
        "prefix": NotRequired[str],
    },
)

S3LogDeliveryTypeDef = TypedDict(
    "S3LogDeliveryTypeDef",
    {
        "enabled": bool,
        "bucket": NotRequired[str],
        "prefix": NotRequired[str],
    },
)

ScaleInPolicyDescriptionTypeDef = TypedDict(
    "ScaleInPolicyDescriptionTypeDef",
    {
        "cpuUtilizationPercentage": NotRequired[int],
    },
)

ScaleInPolicyTypeDef = TypedDict(
    "ScaleInPolicyTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

ScaleInPolicyUpdateTypeDef = TypedDict(
    "ScaleInPolicyUpdateTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

ScaleOutPolicyDescriptionTypeDef = TypedDict(
    "ScaleOutPolicyDescriptionTypeDef",
    {
        "cpuUtilizationPercentage": NotRequired[int],
    },
)

ScaleOutPolicyTypeDef = TypedDict(
    "ScaleOutPolicyTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

ScaleOutPolicyUpdateTypeDef = TypedDict(
    "ScaleOutPolicyUpdateTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

StateDescriptionTypeDef = TypedDict(
    "StateDescriptionTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

UpdateConnectorRequestRequestTypeDef = TypedDict(
    "UpdateConnectorRequestRequestTypeDef",
    {
        "capacity": "CapacityUpdateTypeDef",
        "connectorArn": str,
        "currentVersion": str,
    },
)

UpdateConnectorResponseTypeDef = TypedDict(
    "UpdateConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcDescriptionTypeDef = TypedDict(
    "VpcDescriptionTypeDef",
    {
        "securityGroups": NotRequired[List[str]],
        "subnets": NotRequired[List[str]],
    },
)

VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "subnets": Sequence[str],
        "securityGroups": NotRequired[Sequence[str]],
    },
)

WorkerConfigurationDescriptionTypeDef = TypedDict(
    "WorkerConfigurationDescriptionTypeDef",
    {
        "revision": NotRequired[int],
        "workerConfigurationArn": NotRequired[str],
    },
)

WorkerConfigurationRevisionDescriptionTypeDef = TypedDict(
    "WorkerConfigurationRevisionDescriptionTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "propertiesFileContent": NotRequired[str],
        "revision": NotRequired[int],
    },
)

WorkerConfigurationRevisionSummaryTypeDef = TypedDict(
    "WorkerConfigurationRevisionSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "revision": NotRequired[int],
    },
)

WorkerConfigurationSummaryTypeDef = TypedDict(
    "WorkerConfigurationSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "description": NotRequired[str],
        "latestRevision": NotRequired["WorkerConfigurationRevisionSummaryTypeDef"],
        "name": NotRequired[str],
        "workerConfigurationArn": NotRequired[str],
    },
)

WorkerConfigurationTypeDef = TypedDict(
    "WorkerConfigurationTypeDef",
    {
        "revision": int,
        "workerConfigurationArn": str,
    },
)

WorkerLogDeliveryDescriptionTypeDef = TypedDict(
    "WorkerLogDeliveryDescriptionTypeDef",
    {
        "cloudWatchLogs": NotRequired["CloudWatchLogsLogDeliveryDescriptionTypeDef"],
        "firehose": NotRequired["FirehoseLogDeliveryDescriptionTypeDef"],
        "s3": NotRequired["S3LogDeliveryDescriptionTypeDef"],
    },
)

WorkerLogDeliveryTypeDef = TypedDict(
    "WorkerLogDeliveryTypeDef",
    {
        "cloudWatchLogs": NotRequired["CloudWatchLogsLogDeliveryTypeDef"],
        "firehose": NotRequired["FirehoseLogDeliveryTypeDef"],
        "s3": NotRequired["S3LogDeliveryTypeDef"],
    },
)
