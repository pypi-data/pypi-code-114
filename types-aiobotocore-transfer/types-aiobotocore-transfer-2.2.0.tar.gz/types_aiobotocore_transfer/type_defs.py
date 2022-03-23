"""
Type annotations for transfer service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_transfer/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_transfer.type_defs import CopyStepDetailsTypeDef

    data: CopyStepDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    CustomStepStatusType,
    DomainType,
    EndpointTypeType,
    ExecutionErrorTypeType,
    ExecutionStatusType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    OverwriteExistingType,
    ProtocolType,
    StateType,
    TlsSessionResumptionModeType,
    WorkflowStepTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CopyStepDetailsTypeDef",
    "CreateAccessRequestRequestTypeDef",
    "CreateAccessResponseTypeDef",
    "CreateServerRequestRequestTypeDef",
    "CreateServerResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CustomStepDetailsTypeDef",
    "DeleteAccessRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "DeleteSshPublicKeyRequestRequestTypeDef",
    "DeleteStepDetailsTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DescribeAccessRequestRequestTypeDef",
    "DescribeAccessResponseTypeDef",
    "DescribeExecutionRequestRequestTypeDef",
    "DescribeExecutionResponseTypeDef",
    "DescribeSecurityPolicyRequestRequestTypeDef",
    "DescribeSecurityPolicyResponseTypeDef",
    "DescribeServerRequestRequestTypeDef",
    "DescribeServerResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "DescribeWorkflowRequestRequestTypeDef",
    "DescribeWorkflowResponseTypeDef",
    "DescribedAccessTypeDef",
    "DescribedExecutionTypeDef",
    "DescribedSecurityPolicyTypeDef",
    "DescribedServerTypeDef",
    "DescribedUserTypeDef",
    "DescribedWorkflowTypeDef",
    "EfsFileLocationTypeDef",
    "EndpointDetailsTypeDef",
    "ExecutionErrorTypeDef",
    "ExecutionResultsTypeDef",
    "ExecutionStepResultTypeDef",
    "FileLocationTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ImportSshPublicKeyRequestRequestTypeDef",
    "ImportSshPublicKeyResponseTypeDef",
    "InputFileLocationTypeDef",
    "ListAccessesRequestRequestTypeDef",
    "ListAccessesResponseTypeDef",
    "ListExecutionsRequestRequestTypeDef",
    "ListExecutionsResponseTypeDef",
    "ListSecurityPoliciesRequestRequestTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "ListServersRequestRequestTypeDef",
    "ListServersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "ListedAccessTypeDef",
    "ListedExecutionTypeDef",
    "ListedServerTypeDef",
    "ListedUserTypeDef",
    "ListedWorkflowTypeDef",
    "LoggingConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PosixProfileTypeDef",
    "ProtocolDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "S3FileLocationTypeDef",
    "S3InputFileLocationTypeDef",
    "S3TagTypeDef",
    "SendWorkflowStepStateRequestRequestTypeDef",
    "ServiceMetadataTypeDef",
    "SshPublicKeyTypeDef",
    "StartServerRequestRequestTypeDef",
    "StopServerRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagStepDetailsTypeDef",
    "TagTypeDef",
    "TestIdentityProviderRequestRequestTypeDef",
    "TestIdentityProviderResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessRequestRequestTypeDef",
    "UpdateAccessResponseTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "UpdateServerResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserDetailsTypeDef",
    "WaiterConfigTypeDef",
    "WorkflowDetailTypeDef",
    "WorkflowDetailsTypeDef",
    "WorkflowStepTypeDef",
)

CopyStepDetailsTypeDef = TypedDict(
    "CopyStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "DestinationFileLocation": NotRequired["InputFileLocationTypeDef"],
        "OverwriteExisting": NotRequired[OverwriteExistingType],
        "SourceFileLocation": NotRequired[str],
    },
)

CreateAccessRequestRequestTypeDef = TypedDict(
    "CreateAccessRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "ExternalId": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence["HomeDirectoryMapEntryTypeDef"]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
    },
)

CreateAccessResponseTypeDef = TypedDict(
    "CreateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServerRequestRequestTypeDef = TypedDict(
    "CreateServerRequestRequestTypeDef",
    {
        "Certificate": NotRequired[str],
        "Domain": NotRequired[DomainType],
        "EndpointDetails": NotRequired["EndpointDetailsTypeDef"],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostKey": NotRequired[str],
        "IdentityProviderDetails": NotRequired["IdentityProviderDetailsTypeDef"],
        "IdentityProviderType": NotRequired[IdentityProviderTypeType],
        "LoggingRole": NotRequired[str],
        "PostAuthenticationLoginBanner": NotRequired[str],
        "PreAuthenticationLoginBanner": NotRequired[str],
        "Protocols": NotRequired[Sequence[ProtocolType]],
        "ProtocolDetails": NotRequired["ProtocolDetailsTypeDef"],
        "SecurityPolicyName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "WorkflowDetails": NotRequired["WorkflowDetailsTypeDef"],
    },
)

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "UserName": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence["HomeDirectoryMapEntryTypeDef"]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
        "SshPublicKeyBody": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkflowRequestRequestTypeDef = TypedDict(
    "CreateWorkflowRequestRequestTypeDef",
    {
        "Steps": Sequence["WorkflowStepTypeDef"],
        "Description": NotRequired[str],
        "OnExceptionSteps": NotRequired[Sequence["WorkflowStepTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomStepDetailsTypeDef = TypedDict(
    "CustomStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Target": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
        "SourceFileLocation": NotRequired[str],
    },
)

DeleteAccessRequestRequestTypeDef = TypedDict(
    "DeleteAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

DeleteSshPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
    },
)

DeleteStepDetailsTypeDef = TypedDict(
    "DeleteStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "SourceFileLocation": NotRequired[str],
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)

DescribeAccessRequestRequestTypeDef = TypedDict(
    "DescribeAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DescribeAccessResponseTypeDef = TypedDict(
    "DescribeAccessResponseTypeDef",
    {
        "ServerId": str,
        "Access": "DescribedAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionRequestRequestTypeDef = TypedDict(
    "DescribeExecutionRequestRequestTypeDef",
    {
        "ExecutionId": str,
        "WorkflowId": str,
    },
)

DescribeExecutionResponseTypeDef = TypedDict(
    "DescribeExecutionResponseTypeDef",
    {
        "WorkflowId": str,
        "Execution": "DescribedExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityPolicyRequestRequestTypeDef = TypedDict(
    "DescribeSecurityPolicyRequestRequestTypeDef",
    {
        "SecurityPolicyName": str,
    },
)

DescribeSecurityPolicyResponseTypeDef = TypedDict(
    "DescribeSecurityPolicyResponseTypeDef",
    {
        "SecurityPolicy": "DescribedSecurityPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServerRequestRequestTypeDef = TypedDict(
    "DescribeServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

DescribeServerResponseTypeDef = TypedDict(
    "DescribeServerResponseTypeDef",
    {
        "Server": "DescribedServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "ServerId": str,
        "User": "DescribedUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkflowRequestRequestTypeDef = TypedDict(
    "DescribeWorkflowRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)

DescribeWorkflowResponseTypeDef = TypedDict(
    "DescribeWorkflowResponseTypeDef",
    {
        "Workflow": "DescribedWorkflowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribedAccessTypeDef = TypedDict(
    "DescribedAccessTypeDef",
    {
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryMappings": NotRequired[List["HomeDirectoryMapEntryTypeDef"]],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
        "Role": NotRequired[str],
        "ExternalId": NotRequired[str],
    },
)

DescribedExecutionTypeDef = TypedDict(
    "DescribedExecutionTypeDef",
    {
        "ExecutionId": NotRequired[str],
        "InitialFileLocation": NotRequired["FileLocationTypeDef"],
        "ServiceMetadata": NotRequired["ServiceMetadataTypeDef"],
        "ExecutionRole": NotRequired[str],
        "LoggingConfiguration": NotRequired["LoggingConfigurationTypeDef"],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
        "Status": NotRequired[ExecutionStatusType],
        "Results": NotRequired["ExecutionResultsTypeDef"],
    },
)

DescribedSecurityPolicyTypeDef = TypedDict(
    "DescribedSecurityPolicyTypeDef",
    {
        "SecurityPolicyName": str,
        "Fips": NotRequired[bool],
        "SshCiphers": NotRequired[List[str]],
        "SshKexs": NotRequired[List[str]],
        "SshMacs": NotRequired[List[str]],
        "TlsCiphers": NotRequired[List[str]],
    },
)

DescribedServerTypeDef = TypedDict(
    "DescribedServerTypeDef",
    {
        "Arn": str,
        "Certificate": NotRequired[str],
        "ProtocolDetails": NotRequired["ProtocolDetailsTypeDef"],
        "Domain": NotRequired[DomainType],
        "EndpointDetails": NotRequired["EndpointDetailsTypeDef"],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostKeyFingerprint": NotRequired[str],
        "IdentityProviderDetails": NotRequired["IdentityProviderDetailsTypeDef"],
        "IdentityProviderType": NotRequired[IdentityProviderTypeType],
        "LoggingRole": NotRequired[str],
        "PostAuthenticationLoginBanner": NotRequired[str],
        "PreAuthenticationLoginBanner": NotRequired[str],
        "Protocols": NotRequired[List[ProtocolType]],
        "SecurityPolicyName": NotRequired[str],
        "ServerId": NotRequired[str],
        "State": NotRequired[StateType],
        "Tags": NotRequired[List["TagTypeDef"]],
        "UserCount": NotRequired[int],
        "WorkflowDetails": NotRequired["WorkflowDetailsTypeDef"],
    },
)

DescribedUserTypeDef = TypedDict(
    "DescribedUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryMappings": NotRequired[List["HomeDirectoryMapEntryTypeDef"]],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
        "Role": NotRequired[str],
        "SshPublicKeys": NotRequired[List["SshPublicKeyTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
        "UserName": NotRequired[str],
    },
)

DescribedWorkflowTypeDef = TypedDict(
    "DescribedWorkflowTypeDef",
    {
        "Arn": str,
        "Description": NotRequired[str],
        "Steps": NotRequired[List["WorkflowStepTypeDef"]],
        "OnExceptionSteps": NotRequired[List["WorkflowStepTypeDef"]],
        "WorkflowId": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

EfsFileLocationTypeDef = TypedDict(
    "EfsFileLocationTypeDef",
    {
        "FileSystemId": NotRequired[str],
        "Path": NotRequired[str],
    },
)

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "AddressAllocationIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VpcEndpointId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

ExecutionErrorTypeDef = TypedDict(
    "ExecutionErrorTypeDef",
    {
        "Type": ExecutionErrorTypeType,
        "Message": str,
    },
)

ExecutionResultsTypeDef = TypedDict(
    "ExecutionResultsTypeDef",
    {
        "Steps": NotRequired[List["ExecutionStepResultTypeDef"]],
        "OnExceptionSteps": NotRequired[List["ExecutionStepResultTypeDef"]],
    },
)

ExecutionStepResultTypeDef = TypedDict(
    "ExecutionStepResultTypeDef",
    {
        "StepType": NotRequired[WorkflowStepTypeType],
        "Outputs": NotRequired[str],
        "Error": NotRequired["ExecutionErrorTypeDef"],
    },
)

FileLocationTypeDef = TypedDict(
    "FileLocationTypeDef",
    {
        "S3FileLocation": NotRequired["S3FileLocationTypeDef"],
        "EfsFileLocation": NotRequired["EfsFileLocationTypeDef"],
    },
)

HomeDirectoryMapEntryTypeDef = TypedDict(
    "HomeDirectoryMapEntryTypeDef",
    {
        "Entry": str,
        "Target": str,
    },
)

IdentityProviderDetailsTypeDef = TypedDict(
    "IdentityProviderDetailsTypeDef",
    {
        "Url": NotRequired[str],
        "InvocationRole": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "Function": NotRequired[str],
    },
)

ImportSshPublicKeyRequestRequestTypeDef = TypedDict(
    "ImportSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyBody": str,
        "UserName": str,
    },
)

ImportSshPublicKeyResponseTypeDef = TypedDict(
    "ImportSshPublicKeyResponseTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputFileLocationTypeDef = TypedDict(
    "InputFileLocationTypeDef",
    {
        "S3FileLocation": NotRequired["S3InputFileLocationTypeDef"],
        "EfsFileLocation": NotRequired["EfsFileLocationTypeDef"],
    },
)

ListAccessesRequestRequestTypeDef = TypedDict(
    "ListAccessesRequestRequestTypeDef",
    {
        "ServerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAccessesResponseTypeDef = TypedDict(
    "ListAccessesResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Accesses": List["ListedAccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExecutionsRequestRequestTypeDef = TypedDict(
    "ListExecutionsRequestRequestTypeDef",
    {
        "WorkflowId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListExecutionsResponseTypeDef = TypedDict(
    "ListExecutionsResponseTypeDef",
    {
        "NextToken": str,
        "WorkflowId": str,
        "Executions": List["ListedExecutionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityPoliciesRequestRequestTypeDef = TypedDict(
    "ListSecurityPoliciesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSecurityPoliciesResponseTypeDef = TypedDict(
    "ListSecurityPoliciesResponseTypeDef",
    {
        "NextToken": str,
        "SecurityPolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "NextToken": str,
        "Servers": List["ListedServerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Arn": str,
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "ServerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Users": List["ListedUserTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "NextToken": str,
        "Workflows": List["ListedWorkflowTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListedAccessTypeDef = TypedDict(
    "ListedAccessTypeDef",
    {
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Role": NotRequired[str],
        "ExternalId": NotRequired[str],
    },
)

ListedExecutionTypeDef = TypedDict(
    "ListedExecutionTypeDef",
    {
        "ExecutionId": NotRequired[str],
        "InitialFileLocation": NotRequired["FileLocationTypeDef"],
        "ServiceMetadata": NotRequired["ServiceMetadataTypeDef"],
        "Status": NotRequired[ExecutionStatusType],
    },
)

ListedServerTypeDef = TypedDict(
    "ListedServerTypeDef",
    {
        "Arn": str,
        "Domain": NotRequired[DomainType],
        "IdentityProviderType": NotRequired[IdentityProviderTypeType],
        "EndpointType": NotRequired[EndpointTypeType],
        "LoggingRole": NotRequired[str],
        "ServerId": NotRequired[str],
        "State": NotRequired[StateType],
        "UserCount": NotRequired[int],
    },
)

ListedUserTypeDef = TypedDict(
    "ListedUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Role": NotRequired[str],
        "SshPublicKeyCount": NotRequired[int],
        "UserName": NotRequired[str],
    },
)

ListedWorkflowTypeDef = TypedDict(
    "ListedWorkflowTypeDef",
    {
        "WorkflowId": NotRequired[str],
        "Description": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LoggingRole": NotRequired[str],
        "LogGroupName": NotRequired[str],
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

PosixProfileTypeDef = TypedDict(
    "PosixProfileTypeDef",
    {
        "Uid": int,
        "Gid": int,
        "SecondaryGids": NotRequired[Sequence[int]],
    },
)

ProtocolDetailsTypeDef = TypedDict(
    "ProtocolDetailsTypeDef",
    {
        "PassiveIp": NotRequired[str],
        "TlsSessionResumptionMode": NotRequired[TlsSessionResumptionModeType],
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

S3FileLocationTypeDef = TypedDict(
    "S3FileLocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
        "VersionId": NotRequired[str],
        "Etag": NotRequired[str],
    },
)

S3InputFileLocationTypeDef = TypedDict(
    "S3InputFileLocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)

S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SendWorkflowStepStateRequestRequestTypeDef = TypedDict(
    "SendWorkflowStepStateRequestRequestTypeDef",
    {
        "WorkflowId": str,
        "ExecutionId": str,
        "Token": str,
        "Status": CustomStepStatusType,
    },
)

ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "UserDetails": "UserDetailsTypeDef",
    },
)

SshPublicKeyTypeDef = TypedDict(
    "SshPublicKeyTypeDef",
    {
        "DateImported": datetime,
        "SshPublicKeyBody": str,
        "SshPublicKeyId": str,
    },
)

StartServerRequestRequestTypeDef = TypedDict(
    "StartServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

StopServerRequestRequestTypeDef = TypedDict(
    "StopServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagStepDetailsTypeDef = TypedDict(
    "TagStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Tags": NotRequired[Sequence["S3TagTypeDef"]],
        "SourceFileLocation": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestIdentityProviderRequestRequestTypeDef = TypedDict(
    "TestIdentityProviderRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ServerProtocol": NotRequired[ProtocolType],
        "SourceIp": NotRequired[str],
        "UserPassword": NotRequired[str],
    },
)

TestIdentityProviderResponseTypeDef = TypedDict(
    "TestIdentityProviderResponseTypeDef",
    {
        "Response": str,
        "StatusCode": int,
        "Message": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAccessRequestRequestTypeDef = TypedDict(
    "UpdateAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence["HomeDirectoryMapEntryTypeDef"]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
        "Role": NotRequired[str],
    },
)

UpdateAccessResponseTypeDef = TypedDict(
    "UpdateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServerRequestRequestTypeDef = TypedDict(
    "UpdateServerRequestRequestTypeDef",
    {
        "ServerId": str,
        "Certificate": NotRequired[str],
        "ProtocolDetails": NotRequired["ProtocolDetailsTypeDef"],
        "EndpointDetails": NotRequired["EndpointDetailsTypeDef"],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostKey": NotRequired[str],
        "IdentityProviderDetails": NotRequired["IdentityProviderDetailsTypeDef"],
        "LoggingRole": NotRequired[str],
        "PostAuthenticationLoginBanner": NotRequired[str],
        "PreAuthenticationLoginBanner": NotRequired[str],
        "Protocols": NotRequired[Sequence[ProtocolType]],
        "SecurityPolicyName": NotRequired[str],
        "WorkflowDetails": NotRequired["WorkflowDetailsTypeDef"],
    },
)

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence["HomeDirectoryMapEntryTypeDef"]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired["PosixProfileTypeDef"],
        "Role": NotRequired[str],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "UserName": str,
        "ServerId": str,
        "SessionId": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WorkflowDetailTypeDef = TypedDict(
    "WorkflowDetailTypeDef",
    {
        "WorkflowId": str,
        "ExecutionRole": str,
    },
)

WorkflowDetailsTypeDef = TypedDict(
    "WorkflowDetailsTypeDef",
    {
        "OnUpload": Sequence["WorkflowDetailTypeDef"],
    },
)

WorkflowStepTypeDef = TypedDict(
    "WorkflowStepTypeDef",
    {
        "Type": NotRequired[WorkflowStepTypeType],
        "CopyStepDetails": NotRequired["CopyStepDetailsTypeDef"],
        "CustomStepDetails": NotRequired["CustomStepDetailsTypeDef"],
        "DeleteStepDetails": NotRequired["DeleteStepDetailsTypeDef"],
        "TagStepDetails": NotRequired["TagStepDetailsTypeDef"],
    },
)
