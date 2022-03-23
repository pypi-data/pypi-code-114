"""
Type annotations for kafka service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kafka/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kafka.type_defs import BatchAssociateScramSecretRequestRequestTypeDef

    data: BatchAssociateScramSecretRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ClientBrokerType,
    ClusterStateType,
    ClusterTypeType,
    ConfigurationStateType,
    EnhancedMonitoringType,
    KafkaVersionStatusType,
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
    "BatchAssociateScramSecretRequestRequestTypeDef",
    "BatchAssociateScramSecretResponseTypeDef",
    "BatchDisassociateScramSecretRequestRequestTypeDef",
    "BatchDisassociateScramSecretResponseTypeDef",
    "BrokerEBSVolumeInfoTypeDef",
    "BrokerLogsTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "BrokerNodeInfoTypeDef",
    "BrokerSoftwareInfoTypeDef",
    "ClientAuthenticationTypeDef",
    "CloudWatchLogsTypeDef",
    "ClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "ClusterOperationStepInfoTypeDef",
    "ClusterOperationStepTypeDef",
    "ClusterTypeDef",
    "CompatibleKafkaVersionTypeDef",
    "ConfigurationInfoTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConnectivityInfoTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateClusterV2RequestRequestTypeDef",
    "CreateClusterV2ResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteConfigurationRequestRequestTypeDef",
    "DeleteConfigurationResponseTypeDef",
    "DescribeClusterOperationRequestRequestTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeClusterV2RequestRequestTypeDef",
    "DescribeClusterV2ResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "EBSStorageInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ErrorInfoTypeDef",
    "FirehoseTypeDef",
    "GetBootstrapBrokersRequestRequestTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    "GetCompatibleKafkaVersionsResponseTypeDef",
    "IamTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaVersionTypeDef",
    "ListClusterOperationsRequestRequestTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListClustersV2RequestRequestTypeDef",
    "ListClustersV2ResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListKafkaVersionsRequestRequestTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "ListNodesRequestRequestTypeDef",
    "ListNodesResponseTypeDef",
    "ListScramSecretsRequestRequestTypeDef",
    "ListScramSecretsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingInfoTypeDef",
    "MutableClusterInfoTypeDef",
    "NodeExporterInfoTypeDef",
    "NodeExporterTypeDef",
    "NodeInfoTypeDef",
    "OpenMonitoringInfoTypeDef",
    "OpenMonitoringTypeDef",
    "PaginatorConfigTypeDef",
    "PrometheusInfoTypeDef",
    "PrometheusTypeDef",
    "ProvisionedRequestTypeDef",
    "ProvisionedThroughputTypeDef",
    "ProvisionedTypeDef",
    "PublicAccessTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "RebootBrokerResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3TypeDef",
    "SaslTypeDef",
    "ScramTypeDef",
    "ServerlessClientAuthenticationTypeDef",
    "ServerlessRequestTypeDef",
    "ServerlessSaslTypeDef",
    "ServerlessTypeDef",
    "StateInfoTypeDef",
    "StorageInfoTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TlsTypeDef",
    "UnauthenticatedTypeDef",
    "UnprocessedScramSecretTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrokerCountRequestRequestTypeDef",
    "UpdateBrokerCountResponseTypeDef",
    "UpdateBrokerStorageRequestRequestTypeDef",
    "UpdateBrokerStorageResponseTypeDef",
    "UpdateBrokerTypeRequestRequestTypeDef",
    "UpdateBrokerTypeResponseTypeDef",
    "UpdateClusterConfigurationRequestRequestTypeDef",
    "UpdateClusterConfigurationResponseTypeDef",
    "UpdateClusterKafkaVersionRequestRequestTypeDef",
    "UpdateClusterKafkaVersionResponseTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateConnectivityRequestRequestTypeDef",
    "UpdateConnectivityResponseTypeDef",
    "UpdateMonitoringRequestRequestTypeDef",
    "UpdateMonitoringResponseTypeDef",
    "UpdateSecurityRequestRequestTypeDef",
    "UpdateSecurityResponseTypeDef",
    "VpcConfigTypeDef",
    "ZookeeperNodeInfoTypeDef",
)

BatchAssociateScramSecretRequestRequestTypeDef = TypedDict(
    "BatchAssociateScramSecretRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": Sequence[str],
    },
)

BatchAssociateScramSecretResponseTypeDef = TypedDict(
    "BatchAssociateScramSecretResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List["UnprocessedScramSecretTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateScramSecretRequestRequestTypeDef = TypedDict(
    "BatchDisassociateScramSecretRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": Sequence[str],
    },
)

BatchDisassociateScramSecretResponseTypeDef = TypedDict(
    "BatchDisassociateScramSecretResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List["UnprocessedScramSecretTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrokerEBSVolumeInfoTypeDef = TypedDict(
    "BrokerEBSVolumeInfoTypeDef",
    {
        "KafkaBrokerNodeId": str,
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
        "VolumeSizeGB": NotRequired[int],
    },
)

BrokerLogsTypeDef = TypedDict(
    "BrokerLogsTypeDef",
    {
        "CloudWatchLogs": NotRequired["CloudWatchLogsTypeDef"],
        "Firehose": NotRequired["FirehoseTypeDef"],
        "S3": NotRequired["S3TypeDef"],
    },
)

BrokerNodeGroupInfoTypeDef = TypedDict(
    "BrokerNodeGroupInfoTypeDef",
    {
        "ClientSubnets": Sequence[str],
        "InstanceType": str,
        "BrokerAZDistribution": NotRequired[Literal["DEFAULT"]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "StorageInfo": NotRequired["StorageInfoTypeDef"],
        "ConnectivityInfo": NotRequired["ConnectivityInfoTypeDef"],
    },
)

BrokerNodeInfoTypeDef = TypedDict(
    "BrokerNodeInfoTypeDef",
    {
        "AttachedENIId": NotRequired[str],
        "BrokerId": NotRequired[float],
        "ClientSubnet": NotRequired[str],
        "ClientVpcIpAddress": NotRequired[str],
        "CurrentBrokerSoftwareInfo": NotRequired["BrokerSoftwareInfoTypeDef"],
        "Endpoints": NotRequired[List[str]],
    },
)

BrokerSoftwareInfoTypeDef = TypedDict(
    "BrokerSoftwareInfoTypeDef",
    {
        "ConfigurationArn": NotRequired[str],
        "ConfigurationRevision": NotRequired[int],
        "KafkaVersion": NotRequired[str],
    },
)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef",
    {
        "Sasl": NotRequired["SaslTypeDef"],
        "Tls": NotRequired["TlsTypeDef"],
        "Unauthenticated": NotRequired["UnauthenticatedTypeDef"],
    },
)

CloudWatchLogsTypeDef = TypedDict(
    "CloudWatchLogsTypeDef",
    {
        "Enabled": bool,
        "LogGroup": NotRequired[str],
    },
)

ClusterInfoTypeDef = TypedDict(
    "ClusterInfoTypeDef",
    {
        "ActiveOperationArn": NotRequired[str],
        "BrokerNodeGroupInfo": NotRequired["BrokerNodeGroupInfoTypeDef"],
        "ClientAuthentication": NotRequired["ClientAuthenticationTypeDef"],
        "ClusterArn": NotRequired[str],
        "ClusterName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CurrentBrokerSoftwareInfo": NotRequired["BrokerSoftwareInfoTypeDef"],
        "CurrentVersion": NotRequired[str],
        "EncryptionInfo": NotRequired["EncryptionInfoTypeDef"],
        "EnhancedMonitoring": NotRequired[EnhancedMonitoringType],
        "OpenMonitoring": NotRequired["OpenMonitoringTypeDef"],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "NumberOfBrokerNodes": NotRequired[int],
        "State": NotRequired[ClusterStateType],
        "StateInfo": NotRequired["StateInfoTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
        "ZookeeperConnectString": NotRequired[str],
        "ZookeeperConnectStringTls": NotRequired[str],
    },
)

ClusterOperationInfoTypeDef = TypedDict(
    "ClusterOperationInfoTypeDef",
    {
        "ClientRequestId": NotRequired[str],
        "ClusterArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ErrorInfo": NotRequired["ErrorInfoTypeDef"],
        "OperationArn": NotRequired[str],
        "OperationState": NotRequired[str],
        "OperationSteps": NotRequired[List["ClusterOperationStepTypeDef"]],
        "OperationType": NotRequired[str],
        "SourceClusterInfo": NotRequired["MutableClusterInfoTypeDef"],
        "TargetClusterInfo": NotRequired["MutableClusterInfoTypeDef"],
    },
)

ClusterOperationStepInfoTypeDef = TypedDict(
    "ClusterOperationStepInfoTypeDef",
    {
        "StepStatus": NotRequired[str],
    },
)

ClusterOperationStepTypeDef = TypedDict(
    "ClusterOperationStepTypeDef",
    {
        "StepInfo": NotRequired["ClusterOperationStepInfoTypeDef"],
        "StepName": NotRequired[str],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ActiveOperationArn": NotRequired[str],
        "ClusterType": NotRequired[ClusterTypeType],
        "ClusterArn": NotRequired[str],
        "ClusterName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CurrentVersion": NotRequired[str],
        "State": NotRequired[ClusterStateType],
        "StateInfo": NotRequired["StateInfoTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
        "Provisioned": NotRequired["ProvisionedTypeDef"],
        "Serverless": NotRequired["ServerlessTypeDef"],
    },
)

CompatibleKafkaVersionTypeDef = TypedDict(
    "CompatibleKafkaVersionTypeDef",
    {
        "SourceVersion": NotRequired[str],
        "TargetVersions": NotRequired[List[str]],
    },
)

ConfigurationInfoTypeDef = TypedDict(
    "ConfigurationInfoTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

ConfigurationRevisionTypeDef = TypedDict(
    "ConfigurationRevisionTypeDef",
    {
        "CreationTime": datetime,
        "Revision": int,
        "Description": NotRequired[str],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
    },
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "PublicAccess": NotRequired["PublicAccessTypeDef"],
    },
)

CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "ClusterName": str,
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
        "ClientAuthentication": NotRequired["ClientAuthenticationTypeDef"],
        "ConfigurationInfo": NotRequired["ConfigurationInfoTypeDef"],
        "EncryptionInfo": NotRequired["EncryptionInfoTypeDef"],
        "EnhancedMonitoring": NotRequired[EnhancedMonitoringType],
        "OpenMonitoring": NotRequired["OpenMonitoringInfoTypeDef"],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterV2RequestRequestTypeDef = TypedDict(
    "CreateClusterV2RequestRequestTypeDef",
    {
        "ClusterName": str,
        "Tags": NotRequired[Mapping[str, str]],
        "Provisioned": NotRequired["ProvisionedRequestTypeDef"],
        "Serverless": NotRequired["ServerlessRequestTypeDef"],
    },
)

CreateClusterV2ResponseTypeDef = TypedDict(
    "CreateClusterV2ResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ClusterType": ClusterTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConfigurationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "ServerProperties": Union[bytes, IO[bytes], StreamingBody],
        "Description": NotRequired[str],
        "KafkaVersions": NotRequired[Sequence[str]],
    },
)

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": NotRequired[str],
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "State": ClusterStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteConfigurationResponseTypeDef = TypedDict(
    "DeleteConfigurationResponseTypeDef",
    {
        "Arn": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterOperationRequestRequestTypeDef = TypedDict(
    "DescribeClusterOperationRequestRequestTypeDef",
    {
        "ClusterOperationArn": str,
    },
)

DescribeClusterOperationResponseTypeDef = TypedDict(
    "DescribeClusterOperationResponseTypeDef",
    {
        "ClusterOperationInfo": "ClusterOperationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "ClusterInfo": "ClusterInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterV2RequestRequestTypeDef = TypedDict(
    "DescribeClusterV2RequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterV2ResponseTypeDef = TypedDict(
    "DescribeClusterV2ResponseTypeDef",
    {
        "ClusterInfo": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSStorageInfoTypeDef = TypedDict(
    "EBSStorageInfoTypeDef",
    {
        "ProvisionedThroughput": NotRequired["ProvisionedThroughputTypeDef"],
        "VolumeSize": NotRequired[int],
    },
)

EncryptionAtRestTypeDef = TypedDict(
    "EncryptionAtRestTypeDef",
    {
        "DataVolumeKMSKeyId": str,
    },
)

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {
        "ClientBroker": NotRequired[ClientBrokerType],
        "InCluster": NotRequired[bool],
    },
)

EncryptionInfoTypeDef = TypedDict(
    "EncryptionInfoTypeDef",
    {
        "EncryptionAtRest": NotRequired["EncryptionAtRestTypeDef"],
        "EncryptionInTransit": NotRequired["EncryptionInTransitTypeDef"],
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorString": NotRequired[str],
    },
)

FirehoseTypeDef = TypedDict(
    "FirehoseTypeDef",
    {
        "Enabled": bool,
        "DeliveryStream": NotRequired[str],
    },
)

GetBootstrapBrokersRequestRequestTypeDef = TypedDict(
    "GetBootstrapBrokersRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

GetBootstrapBrokersResponseTypeDef = TypedDict(
    "GetBootstrapBrokersResponseTypeDef",
    {
        "BootstrapBrokerString": str,
        "BootstrapBrokerStringTls": str,
        "BootstrapBrokerStringSaslScram": str,
        "BootstrapBrokerStringSaslIam": str,
        "BootstrapBrokerStringPublicTls": str,
        "BootstrapBrokerStringPublicSaslScram": str,
        "BootstrapBrokerStringPublicSaslIam": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCompatibleKafkaVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    {
        "ClusterArn": NotRequired[str],
    },
)

GetCompatibleKafkaVersionsResponseTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsResponseTypeDef",
    {
        "CompatibleKafkaVersions": List["CompatibleKafkaVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamTypeDef = TypedDict(
    "IamTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

JmxExporterInfoTypeDef = TypedDict(
    "JmxExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

JmxExporterTypeDef = TypedDict(
    "JmxExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

KafkaVersionTypeDef = TypedDict(
    "KafkaVersionTypeDef",
    {
        "Version": NotRequired[str],
        "Status": NotRequired[KafkaVersionStatusType],
    },
)

ListClusterOperationsRequestRequestTypeDef = TypedDict(
    "ListClusterOperationsRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListClusterOperationsResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List["ClusterOperationInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "ClusterNameFilter": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "ClusterInfoList": List["ClusterInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersV2RequestRequestTypeDef = TypedDict(
    "ListClustersV2RequestRequestTypeDef",
    {
        "ClusterNameFilter": NotRequired[str],
        "ClusterTypeFilter": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListClustersV2ResponseTypeDef = TypedDict(
    "ListClustersV2ResponseTypeDef",
    {
        "ClusterInfoList": List["ClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "ListConfigurationRevisionsRequestRequestTypeDef",
    {
        "Arn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List["ConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKafkaVersionsRequestRequestTypeDef = TypedDict(
    "ListKafkaVersionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListKafkaVersionsResponseTypeDef = TypedDict(
    "ListKafkaVersionsResponseTypeDef",
    {
        "KafkaVersions": List["KafkaVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodesRequestRequestTypeDef = TypedDict(
    "ListNodesRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInfoList": List["NodeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScramSecretsRequestRequestTypeDef = TypedDict(
    "ListScramSecretsRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListScramSecretsResponseTypeDef = TypedDict(
    "ListScramSecretsResponseTypeDef",
    {
        "NextToken": str,
        "SecretArnList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingInfoTypeDef = TypedDict(
    "LoggingInfoTypeDef",
    {
        "BrokerLogs": "BrokerLogsTypeDef",
    },
)

MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": NotRequired[List["BrokerEBSVolumeInfoTypeDef"]],
        "ConfigurationInfo": NotRequired["ConfigurationInfoTypeDef"],
        "NumberOfBrokerNodes": NotRequired[int],
        "EnhancedMonitoring": NotRequired[EnhancedMonitoringType],
        "OpenMonitoring": NotRequired["OpenMonitoringTypeDef"],
        "KafkaVersion": NotRequired[str],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "InstanceType": NotRequired[str],
        "ClientAuthentication": NotRequired["ClientAuthenticationTypeDef"],
        "EncryptionInfo": NotRequired["EncryptionInfoTypeDef"],
        "ConnectivityInfo": NotRequired["ConnectivityInfoTypeDef"],
    },
)

NodeExporterInfoTypeDef = TypedDict(
    "NodeExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeExporterTypeDef = TypedDict(
    "NodeExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeInfoTypeDef = TypedDict(
    "NodeInfoTypeDef",
    {
        "AddedToClusterTime": NotRequired[str],
        "BrokerNodeInfo": NotRequired["BrokerNodeInfoTypeDef"],
        "InstanceType": NotRequired[str],
        "NodeARN": NotRequired[str],
        "NodeType": NotRequired[Literal["BROKER"]],
        "ZookeeperNodeInfo": NotRequired["ZookeeperNodeInfoTypeDef"],
    },
)

OpenMonitoringInfoTypeDef = TypedDict(
    "OpenMonitoringInfoTypeDef",
    {
        "Prometheus": "PrometheusInfoTypeDef",
    },
)

OpenMonitoringTypeDef = TypedDict(
    "OpenMonitoringTypeDef",
    {
        "Prometheus": "PrometheusTypeDef",
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

PrometheusInfoTypeDef = TypedDict(
    "PrometheusInfoTypeDef",
    {
        "JmxExporter": NotRequired["JmxExporterInfoTypeDef"],
        "NodeExporter": NotRequired["NodeExporterInfoTypeDef"],
    },
)

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {
        "JmxExporter": NotRequired["JmxExporterTypeDef"],
        "NodeExporter": NotRequired["NodeExporterTypeDef"],
    },
)

ProvisionedRequestTypeDef = TypedDict(
    "ProvisionedRequestTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
        "ClientAuthentication": NotRequired["ClientAuthenticationTypeDef"],
        "ConfigurationInfo": NotRequired["ConfigurationInfoTypeDef"],
        "EncryptionInfo": NotRequired["EncryptionInfoTypeDef"],
        "EnhancedMonitoring": NotRequired[EnhancedMonitoringType],
        "OpenMonitoring": NotRequired["OpenMonitoringInfoTypeDef"],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
    },
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "Enabled": NotRequired[bool],
        "VolumeThroughput": NotRequired[int],
    },
)

ProvisionedTypeDef = TypedDict(
    "ProvisionedTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "CurrentBrokerSoftwareInfo": NotRequired["BrokerSoftwareInfoTypeDef"],
        "ClientAuthentication": NotRequired["ClientAuthenticationTypeDef"],
        "EncryptionInfo": NotRequired["EncryptionInfoTypeDef"],
        "EnhancedMonitoring": NotRequired[EnhancedMonitoringType],
        "OpenMonitoring": NotRequired["OpenMonitoringInfoTypeDef"],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
        "ZookeeperConnectString": NotRequired[str],
        "ZookeeperConnectStringTls": NotRequired[str],
    },
)

PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "Type": NotRequired[str],
    },
)

RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerIds": Sequence[str],
        "ClusterArn": str,
    },
)

RebootBrokerResponseTypeDef = TypedDict(
    "RebootBrokerResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
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

S3TypeDef = TypedDict(
    "S3TypeDef",
    {
        "Enabled": bool,
        "Bucket": NotRequired[str],
        "Prefix": NotRequired[str],
    },
)

SaslTypeDef = TypedDict(
    "SaslTypeDef",
    {
        "Scram": NotRequired["ScramTypeDef"],
        "Iam": NotRequired["IamTypeDef"],
    },
)

ScramTypeDef = TypedDict(
    "ScramTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

ServerlessClientAuthenticationTypeDef = TypedDict(
    "ServerlessClientAuthenticationTypeDef",
    {
        "Sasl": NotRequired["ServerlessSaslTypeDef"],
    },
)

ServerlessRequestTypeDef = TypedDict(
    "ServerlessRequestTypeDef",
    {
        "VpcConfigs": Sequence["VpcConfigTypeDef"],
        "ClientAuthentication": NotRequired["ServerlessClientAuthenticationTypeDef"],
    },
)

ServerlessSaslTypeDef = TypedDict(
    "ServerlessSaslTypeDef",
    {
        "Iam": NotRequired["IamTypeDef"],
    },
)

ServerlessTypeDef = TypedDict(
    "ServerlessTypeDef",
    {
        "VpcConfigs": List["VpcConfigTypeDef"],
        "ClientAuthentication": NotRequired["ServerlessClientAuthenticationTypeDef"],
    },
)

StateInfoTypeDef = TypedDict(
    "StateInfoTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef",
    {
        "EbsStorageInfo": NotRequired["EBSStorageInfoTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TlsTypeDef = TypedDict(
    "TlsTypeDef",
    {
        "CertificateAuthorityArnList": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)

UnauthenticatedTypeDef = TypedDict(
    "UnauthenticatedTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

UnprocessedScramSecretTypeDef = TypedDict(
    "UnprocessedScramSecretTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "SecretArn": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateBrokerCountRequestRequestTypeDef = TypedDict(
    "UpdateBrokerCountRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetNumberOfBrokerNodes": int,
    },
)

UpdateBrokerCountResponseTypeDef = TypedDict(
    "UpdateBrokerCountResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBrokerStorageRequestRequestTypeDef = TypedDict(
    "UpdateBrokerStorageRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetBrokerEBSVolumeInfo": Sequence["BrokerEBSVolumeInfoTypeDef"],
    },
)

UpdateBrokerStorageResponseTypeDef = TypedDict(
    "UpdateBrokerStorageResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBrokerTypeRequestRequestTypeDef = TypedDict(
    "UpdateBrokerTypeRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetInstanceType": str,
    },
)

UpdateBrokerTypeResponseTypeDef = TypedDict(
    "UpdateBrokerTypeResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateClusterConfigurationRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "CurrentVersion": str,
    },
)

UpdateClusterConfigurationResponseTypeDef = TypedDict(
    "UpdateClusterConfigurationResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterKafkaVersionRequestRequestTypeDef = TypedDict(
    "UpdateClusterKafkaVersionRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetKafkaVersion": str,
        "ConfigurationInfo": NotRequired["ConfigurationInfoTypeDef"],
    },
)

UpdateClusterKafkaVersionResponseTypeDef = TypedDict(
    "UpdateClusterKafkaVersionResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
        "ServerProperties": Union[bytes, IO[bytes], StreamingBody],
        "Description": NotRequired[str],
    },
)

UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectivityRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ConnectivityInfo": "ConnectivityInfoTypeDef",
        "CurrentVersion": str,
    },
)

UpdateConnectivityResponseTypeDef = TypedDict(
    "UpdateConnectivityResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMonitoringRequestRequestTypeDef = TypedDict(
    "UpdateMonitoringRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "EnhancedMonitoring": NotRequired[EnhancedMonitoringType],
        "OpenMonitoring": NotRequired["OpenMonitoringInfoTypeDef"],
        "LoggingInfo": NotRequired["LoggingInfoTypeDef"],
    },
)

UpdateMonitoringResponseTypeDef = TypedDict(
    "UpdateMonitoringResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSecurityRequestRequestTypeDef = TypedDict(
    "UpdateSecurityRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "ClientAuthentication": NotRequired["ClientAuthenticationTypeDef"],
        "EncryptionInfo": NotRequired["EncryptionInfoTypeDef"],
    },
)

UpdateSecurityResponseTypeDef = TypedDict(
    "UpdateSecurityResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

ZookeeperNodeInfoTypeDef = TypedDict(
    "ZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": NotRequired[str],
        "ClientVpcIpAddress": NotRequired[str],
        "Endpoints": NotRequired[List[str]],
        "ZookeeperId": NotRequired[float],
        "ZookeeperVersion": NotRequired[str],
    },
)
