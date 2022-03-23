"""
Type annotations for datasync service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_datasync/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_datasync.type_defs import AgentListEntryTypeDef

    data: AgentListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AgentStatusType,
    AtimeType,
    EndpointTypeType,
    GidType,
    HdfsAuthenticationTypeType,
    HdfsDataTransferProtectionType,
    HdfsRpcProtectionType,
    LocationFilterNameType,
    LogLevelType,
    MtimeType,
    NfsVersionType,
    ObjectStorageServerProtocolType,
    OperatorType,
    OverwriteModeType,
    PhaseStatusType,
    PosixPermissionsType,
    PreserveDeletedFilesType,
    PreserveDevicesType,
    S3StorageClassType,
    SmbSecurityDescriptorCopyFlagsType,
    SmbVersionType,
    TaskExecutionStatusType,
    TaskFilterNameType,
    TaskQueueingType,
    TaskStatusType,
    TransferModeType,
    UidType,
    VerifyModeType,
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
    "AgentListEntryTypeDef",
    "CancelTaskExecutionRequestRequestTypeDef",
    "CreateAgentRequestRequestTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateLocationEfsRequestRequestTypeDef",
    "CreateLocationEfsResponseTypeDef",
    "CreateLocationFsxLustreRequestRequestTypeDef",
    "CreateLocationFsxLustreResponseTypeDef",
    "CreateLocationFsxWindowsRequestRequestTypeDef",
    "CreateLocationFsxWindowsResponseTypeDef",
    "CreateLocationHdfsRequestRequestTypeDef",
    "CreateLocationHdfsResponseTypeDef",
    "CreateLocationNfsRequestRequestTypeDef",
    "CreateLocationNfsResponseTypeDef",
    "CreateLocationObjectStorageRequestRequestTypeDef",
    "CreateLocationObjectStorageResponseTypeDef",
    "CreateLocationS3RequestRequestTypeDef",
    "CreateLocationS3ResponseTypeDef",
    "CreateLocationSmbRequestRequestTypeDef",
    "CreateLocationSmbResponseTypeDef",
    "CreateTaskRequestRequestTypeDef",
    "CreateTaskResponseTypeDef",
    "DeleteAgentRequestRequestTypeDef",
    "DeleteLocationRequestRequestTypeDef",
    "DeleteTaskRequestRequestTypeDef",
    "DescribeAgentRequestRequestTypeDef",
    "DescribeAgentResponseTypeDef",
    "DescribeLocationEfsRequestRequestTypeDef",
    "DescribeLocationEfsResponseTypeDef",
    "DescribeLocationFsxLustreRequestRequestTypeDef",
    "DescribeLocationFsxLustreResponseTypeDef",
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    "DescribeLocationFsxWindowsResponseTypeDef",
    "DescribeLocationHdfsRequestRequestTypeDef",
    "DescribeLocationHdfsResponseTypeDef",
    "DescribeLocationNfsRequestRequestTypeDef",
    "DescribeLocationNfsResponseTypeDef",
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    "DescribeLocationObjectStorageResponseTypeDef",
    "DescribeLocationS3RequestRequestTypeDef",
    "DescribeLocationS3ResponseTypeDef",
    "DescribeLocationSmbRequestRequestTypeDef",
    "DescribeLocationSmbResponseTypeDef",
    "DescribeTaskExecutionRequestRequestTypeDef",
    "DescribeTaskExecutionResponseTypeDef",
    "DescribeTaskRequestRequestTypeDef",
    "DescribeTaskResponseTypeDef",
    "Ec2ConfigTypeDef",
    "FilterRuleTypeDef",
    "HdfsNameNodeTypeDef",
    "ListAgentsRequestRequestTypeDef",
    "ListAgentsResponseTypeDef",
    "ListLocationsRequestRequestTypeDef",
    "ListLocationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsRequestRequestTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListTasksResponseTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "OptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateLinkConfigTypeDef",
    "QopConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "StartTaskExecutionRequestRequestTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "TagListEntryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "TaskScheduleTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentRequestRequestTypeDef",
    "UpdateLocationHdfsRequestRequestTypeDef",
    "UpdateLocationNfsRequestRequestTypeDef",
    "UpdateLocationObjectStorageRequestRequestTypeDef",
    "UpdateLocationSmbRequestRequestTypeDef",
    "UpdateTaskExecutionRequestRequestTypeDef",
    "UpdateTaskRequestRequestTypeDef",
)

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef",
    {
        "AgentArn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[AgentStatusType],
    },
)

CancelTaskExecutionRequestRequestTypeDef = TypedDict(
    "CancelTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

CreateAgentRequestRequestTypeDef = TypedDict(
    "CreateAgentRequestRequestTypeDef",
    {
        "ActivationKey": str,
        "AgentName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
        "VpcEndpointId": NotRequired[str],
        "SubnetArns": NotRequired[Sequence[str]],
        "SecurityGroupArns": NotRequired[Sequence[str]],
    },
)

CreateAgentResponseTypeDef = TypedDict(
    "CreateAgentResponseTypeDef",
    {
        "AgentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationEfsRequestRequestTypeDef = TypedDict(
    "CreateLocationEfsRequestRequestTypeDef",
    {
        "EfsFilesystemArn": str,
        "Ec2Config": "Ec2ConfigTypeDef",
        "Subdirectory": NotRequired[str],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationEfsResponseTypeDef = TypedDict(
    "CreateLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "CreateLocationFsxLustreRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": Sequence[str],
        "Subdirectory": NotRequired[str],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationFsxLustreResponseTypeDef = TypedDict(
    "CreateLocationFsxLustreResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "CreateLocationFsxWindowsRequestRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": Sequence[str],
        "User": str,
        "Password": str,
        "Subdirectory": NotRequired[str],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
        "Domain": NotRequired[str],
    },
)

CreateLocationFsxWindowsResponseTypeDef = TypedDict(
    "CreateLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationHdfsRequestRequestTypeDef = TypedDict(
    "CreateLocationHdfsRequestRequestTypeDef",
    {
        "NameNodes": Sequence["HdfsNameNodeTypeDef"],
        "AuthenticationType": HdfsAuthenticationTypeType,
        "AgentArns": Sequence[str],
        "Subdirectory": NotRequired[str],
        "BlockSize": NotRequired[int],
        "ReplicationFactor": NotRequired[int],
        "KmsKeyProviderUri": NotRequired[str],
        "QopConfiguration": NotRequired["QopConfigurationTypeDef"],
        "SimpleUser": NotRequired[str],
        "KerberosPrincipal": NotRequired[str],
        "KerberosKeytab": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "KerberosKrb5Conf": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationHdfsResponseTypeDef = TypedDict(
    "CreateLocationHdfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationNfsRequestRequestTypeDef = TypedDict(
    "CreateLocationNfsRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": NotRequired["NfsMountOptionsTypeDef"],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationNfsResponseTypeDef = TypedDict(
    "CreateLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "CreateLocationObjectStorageRequestRequestTypeDef",
    {
        "ServerHostname": str,
        "BucketName": str,
        "AgentArns": Sequence[str],
        "ServerPort": NotRequired[int],
        "ServerProtocol": NotRequired[ObjectStorageServerProtocolType],
        "Subdirectory": NotRequired[str],
        "AccessKey": NotRequired[str],
        "SecretKey": NotRequired[str],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationObjectStorageResponseTypeDef = TypedDict(
    "CreateLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationS3RequestRequestTypeDef = TypedDict(
    "CreateLocationS3RequestRequestTypeDef",
    {
        "S3BucketArn": str,
        "S3Config": "S3ConfigTypeDef",
        "Subdirectory": NotRequired[str],
        "S3StorageClass": NotRequired[S3StorageClassType],
        "AgentArns": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationS3ResponseTypeDef = TypedDict(
    "CreateLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLocationSmbRequestRequestTypeDef = TypedDict(
    "CreateLocationSmbRequestRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "User": str,
        "Password": str,
        "AgentArns": Sequence[str],
        "Domain": NotRequired[str],
        "MountOptions": NotRequired["SmbMountOptionsTypeDef"],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
    },
)

CreateLocationSmbResponseTypeDef = TypedDict(
    "CreateLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTaskRequestRequestTypeDef = TypedDict(
    "CreateTaskRequestRequestTypeDef",
    {
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": NotRequired[str],
        "Name": NotRequired[str],
        "Options": NotRequired["OptionsTypeDef"],
        "Excludes": NotRequired[Sequence["FilterRuleTypeDef"]],
        "Schedule": NotRequired["TaskScheduleTypeDef"],
        "Tags": NotRequired[Sequence["TagListEntryTypeDef"]],
        "Includes": NotRequired[Sequence["FilterRuleTypeDef"]],
    },
)

CreateTaskResponseTypeDef = TypedDict(
    "CreateTaskResponseTypeDef",
    {
        "TaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAgentRequestRequestTypeDef = TypedDict(
    "DeleteAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DeleteLocationRequestRequestTypeDef = TypedDict(
    "DeleteLocationRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DeleteTaskRequestRequestTypeDef = TypedDict(
    "DeleteTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeAgentRequestRequestTypeDef = TypedDict(
    "DescribeAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DescribeAgentResponseTypeDef = TypedDict(
    "DescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": EndpointTypeType,
        "PrivateLinkConfig": "PrivateLinkConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationEfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationEfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationEfsResponseTypeDef = TypedDict(
    "DescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": "Ec2ConfigTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxLustreRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxLustreRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxLustreResponseTypeDef = TypedDict(
    "DescribeLocationFsxLustreResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxWindowsRequestRequestTypeDef = TypedDict(
    "DescribeLocationFsxWindowsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxWindowsResponseTypeDef = TypedDict(
    "DescribeLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "User": str,
        "Domain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationHdfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationHdfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationHdfsResponseTypeDef = TypedDict(
    "DescribeLocationHdfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "NameNodes": List["HdfsNameNodeTypeDef"],
        "BlockSize": int,
        "ReplicationFactor": int,
        "KmsKeyProviderUri": str,
        "QopConfiguration": "QopConfigurationTypeDef",
        "AuthenticationType": HdfsAuthenticationTypeType,
        "SimpleUser": str,
        "KerberosPrincipal": str,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationNfsRequestRequestTypeDef = TypedDict(
    "DescribeLocationNfsRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationNfsResponseTypeDef = TypedDict(
    "DescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": "NfsMountOptionsTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "DescribeLocationObjectStorageRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationObjectStorageResponseTypeDef = TypedDict(
    "DescribeLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AccessKey": str,
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationS3RequestRequestTypeDef = TypedDict(
    "DescribeLocationS3RequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationS3ResponseTypeDef = TypedDict(
    "DescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": S3StorageClassType,
        "S3Config": "S3ConfigTypeDef",
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationSmbRequestRequestTypeDef = TypedDict(
    "DescribeLocationSmbRequestRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationSmbResponseTypeDef = TypedDict(
    "DescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskExecutionRequestRequestTypeDef = TypedDict(
    "DescribeTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

DescribeTaskExecutionResponseTypeDef = TypedDict(
    "DescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Includes": List["FilterRuleTypeDef"],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": "TaskExecutionResultDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskRequestRequestTypeDef = TypedDict(
    "DescribeTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeTaskResponseTypeDef = TypedDict(
    "DescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
        "Includes": List["FilterRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ec2ConfigTypeDef = TypedDict(
    "Ec2ConfigTypeDef",
    {
        "SubnetArn": str,
        "SecurityGroupArns": Sequence[str],
    },
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "FilterType": NotRequired[Literal["SIMPLE_PATTERN"]],
        "Value": NotRequired[str],
    },
)

HdfsNameNodeTypeDef = TypedDict(
    "HdfsNameNodeTypeDef",
    {
        "Hostname": str,
        "Port": int,
    },
)

ListAgentsRequestRequestTypeDef = TypedDict(
    "ListAgentsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {
        "Agents": List["AgentListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocationsRequestRequestTypeDef = TypedDict(
    "ListLocationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["LocationFilterTypeDef"]],
    },
)

ListLocationsResponseTypeDef = TypedDict(
    "ListLocationsResponseTypeDef",
    {
        "Locations": List["LocationListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskExecutionsRequestRequestTypeDef = TypedDict(
    "ListTaskExecutionsRequestRequestTypeDef",
    {
        "TaskArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTaskExecutionsResponseTypeDef = TypedDict(
    "ListTaskExecutionsResponseTypeDef",
    {
        "TaskExecutions": List["TaskExecutionListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["TaskFilterTypeDef"]],
    },
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "Tasks": List["TaskListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationFilterTypeDef = TypedDict(
    "LocationFilterTypeDef",
    {
        "Name": LocationFilterNameType,
        "Values": Sequence[str],
        "Operator": OperatorType,
    },
)

LocationListEntryTypeDef = TypedDict(
    "LocationListEntryTypeDef",
    {
        "LocationArn": NotRequired[str],
        "LocationUri": NotRequired[str],
    },
)

NfsMountOptionsTypeDef = TypedDict(
    "NfsMountOptionsTypeDef",
    {
        "Version": NotRequired[NfsVersionType],
    },
)

OnPremConfigTypeDef = TypedDict(
    "OnPremConfigTypeDef",
    {
        "AgentArns": Sequence[str],
    },
)

OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "VerifyMode": NotRequired[VerifyModeType],
        "OverwriteMode": NotRequired[OverwriteModeType],
        "Atime": NotRequired[AtimeType],
        "Mtime": NotRequired[MtimeType],
        "Uid": NotRequired[UidType],
        "Gid": NotRequired[GidType],
        "PreserveDeletedFiles": NotRequired[PreserveDeletedFilesType],
        "PreserveDevices": NotRequired[PreserveDevicesType],
        "PosixPermissions": NotRequired[PosixPermissionsType],
        "BytesPerSecond": NotRequired[int],
        "TaskQueueing": NotRequired[TaskQueueingType],
        "LogLevel": NotRequired[LogLevelType],
        "TransferMode": NotRequired[TransferModeType],
        "SecurityDescriptorCopyFlags": NotRequired[SmbSecurityDescriptorCopyFlagsType],
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

PrivateLinkConfigTypeDef = TypedDict(
    "PrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": NotRequired[str],
        "PrivateLinkEndpoint": NotRequired[str],
        "SubnetArns": NotRequired[List[str]],
        "SecurityGroupArns": NotRequired[List[str]],
    },
)

QopConfigurationTypeDef = TypedDict(
    "QopConfigurationTypeDef",
    {
        "RpcProtection": NotRequired[HdfsRpcProtectionType],
        "DataTransferProtection": NotRequired[HdfsDataTransferProtectionType],
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

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketAccessRoleArn": str,
    },
)

SmbMountOptionsTypeDef = TypedDict(
    "SmbMountOptionsTypeDef",
    {
        "Version": NotRequired[SmbVersionType],
    },
)

StartTaskExecutionRequestRequestTypeDef = TypedDict(
    "StartTaskExecutionRequestRequestTypeDef",
    {
        "TaskArn": str,
        "OverrideOptions": NotRequired["OptionsTypeDef"],
        "Includes": NotRequired[Sequence["FilterRuleTypeDef"]],
        "Excludes": NotRequired[Sequence["FilterRuleTypeDef"]],
    },
)

StartTaskExecutionResponseTypeDef = TypedDict(
    "StartTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagListEntryTypeDef = TypedDict(
    "TagListEntryTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagListEntryTypeDef"],
    },
)

TaskExecutionListEntryTypeDef = TypedDict(
    "TaskExecutionListEntryTypeDef",
    {
        "TaskExecutionArn": NotRequired[str],
        "Status": NotRequired[TaskExecutionStatusType],
    },
)

TaskExecutionResultDetailTypeDef = TypedDict(
    "TaskExecutionResultDetailTypeDef",
    {
        "PrepareDuration": NotRequired[int],
        "PrepareStatus": NotRequired[PhaseStatusType],
        "TotalDuration": NotRequired[int],
        "TransferDuration": NotRequired[int],
        "TransferStatus": NotRequired[PhaseStatusType],
        "VerifyDuration": NotRequired[int],
        "VerifyStatus": NotRequired[PhaseStatusType],
        "ErrorCode": NotRequired[str],
        "ErrorDetail": NotRequired[str],
    },
)

TaskFilterTypeDef = TypedDict(
    "TaskFilterTypeDef",
    {
        "Name": TaskFilterNameType,
        "Values": Sequence[str],
        "Operator": OperatorType,
    },
)

TaskListEntryTypeDef = TypedDict(
    "TaskListEntryTypeDef",
    {
        "TaskArn": NotRequired[str],
        "Status": NotRequired[TaskStatusType],
        "Name": NotRequired[str],
    },
)

TaskScheduleTypeDef = TypedDict(
    "TaskScheduleTypeDef",
    {
        "ScheduleExpression": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Keys": Sequence[str],
    },
)

UpdateAgentRequestRequestTypeDef = TypedDict(
    "UpdateAgentRequestRequestTypeDef",
    {
        "AgentArn": str,
        "Name": NotRequired[str],
    },
)

UpdateLocationHdfsRequestRequestTypeDef = TypedDict(
    "UpdateLocationHdfsRequestRequestTypeDef",
    {
        "LocationArn": str,
        "Subdirectory": NotRequired[str],
        "NameNodes": NotRequired[Sequence["HdfsNameNodeTypeDef"]],
        "BlockSize": NotRequired[int],
        "ReplicationFactor": NotRequired[int],
        "KmsKeyProviderUri": NotRequired[str],
        "QopConfiguration": NotRequired["QopConfigurationTypeDef"],
        "AuthenticationType": NotRequired[HdfsAuthenticationTypeType],
        "SimpleUser": NotRequired[str],
        "KerberosPrincipal": NotRequired[str],
        "KerberosKeytab": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "KerberosKrb5Conf": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "AgentArns": NotRequired[Sequence[str]],
    },
)

UpdateLocationNfsRequestRequestTypeDef = TypedDict(
    "UpdateLocationNfsRequestRequestTypeDef",
    {
        "LocationArn": str,
        "Subdirectory": NotRequired[str],
        "OnPremConfig": NotRequired["OnPremConfigTypeDef"],
        "MountOptions": NotRequired["NfsMountOptionsTypeDef"],
    },
)

UpdateLocationObjectStorageRequestRequestTypeDef = TypedDict(
    "UpdateLocationObjectStorageRequestRequestTypeDef",
    {
        "LocationArn": str,
        "ServerPort": NotRequired[int],
        "ServerProtocol": NotRequired[ObjectStorageServerProtocolType],
        "Subdirectory": NotRequired[str],
        "AccessKey": NotRequired[str],
        "SecretKey": NotRequired[str],
        "AgentArns": NotRequired[Sequence[str]],
    },
)

UpdateLocationSmbRequestRequestTypeDef = TypedDict(
    "UpdateLocationSmbRequestRequestTypeDef",
    {
        "LocationArn": str,
        "Subdirectory": NotRequired[str],
        "User": NotRequired[str],
        "Domain": NotRequired[str],
        "Password": NotRequired[str],
        "AgentArns": NotRequired[Sequence[str]],
        "MountOptions": NotRequired["SmbMountOptionsTypeDef"],
    },
)

UpdateTaskExecutionRequestRequestTypeDef = TypedDict(
    "UpdateTaskExecutionRequestRequestTypeDef",
    {
        "TaskExecutionArn": str,
        "Options": "OptionsTypeDef",
    },
)

UpdateTaskRequestRequestTypeDef = TypedDict(
    "UpdateTaskRequestRequestTypeDef",
    {
        "TaskArn": str,
        "Options": NotRequired["OptionsTypeDef"],
        "Excludes": NotRequired[Sequence["FilterRuleTypeDef"]],
        "Schedule": NotRequired["TaskScheduleTypeDef"],
        "Name": NotRequired[str],
        "CloudWatchLogGroupArn": NotRequired[str],
        "Includes": NotRequired[Sequence["FilterRuleTypeDef"]],
    },
)
