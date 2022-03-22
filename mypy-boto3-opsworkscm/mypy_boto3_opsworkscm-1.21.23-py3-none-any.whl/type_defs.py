"""
Type annotations for opsworkscm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    BackupStatusType,
    BackupTypeType,
    MaintenanceStatusType,
    NodeAssociationStatusType,
    ServerStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAttributeTypeDef",
    "AssociateNodeRequestRequestTypeDef",
    "AssociateNodeResponseTypeDef",
    "BackupTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateServerRequestRequestTypeDef",
    "CreateServerResponseTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusRequestRequestTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DescribeServersRequestRequestTypeDef",
    "DescribeServersResponseTypeDef",
    "DisassociateNodeRequestRequestTypeDef",
    "DisassociateNodeResponseTypeDef",
    "EngineAttributeTypeDef",
    "ExportServerEngineAttributeRequestRequestTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreServerRequestRequestTypeDef",
    "RestoreServerResponseTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "StartMaintenanceRequestRequestTypeDef",
    "StartMaintenanceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateServerEngineAttributesRequestRequestTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "UpdateServerResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Maximum": NotRequired[int],
        "Used": NotRequired[int],
    },
)

AssociateNodeRequestRequestTypeDef = TypedDict(
    "AssociateNodeRequestRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
        "EngineAttributes": Sequence["EngineAttributeTypeDef"],
    },
)

AssociateNodeResponseTypeDef = TypedDict(
    "AssociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupArn": NotRequired[str],
        "BackupId": NotRequired[str],
        "BackupType": NotRequired[BackupTypeType],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineModel": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "InstanceProfileArn": NotRequired[str],
        "InstanceType": NotRequired[str],
        "KeyPair": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "S3DataSize": NotRequired[int],
        "S3DataUrl": NotRequired[str],
        "S3LogUrl": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "ServerName": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "Status": NotRequired[BackupStatusType],
        "StatusDescription": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "ToolsVersion": NotRequired[str],
        "UserArn": NotRequired[str],
    },
)

CreateBackupRequestRequestTypeDef = TypedDict(
    "CreateBackupRequestRequestTypeDef",
    {
        "ServerName": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServerRequestRequestTypeDef = TypedDict(
    "CreateServerRequestRequestTypeDef",
    {
        "Engine": str,
        "ServerName": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "ServiceRoleArn": str,
        "AssociatePublicIpAddress": NotRequired[bool],
        "CustomDomain": NotRequired[str],
        "CustomCertificate": NotRequired[str],
        "CustomPrivateKey": NotRequired[str],
        "DisableAutomatedBackup": NotRequired[bool],
        "EngineModel": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EngineAttributes": NotRequired[Sequence["EngineAttributeTypeDef"]],
        "BackupRetentionCount": NotRequired[int],
        "KeyPair": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "BackupId": NotRequired[str],
    },
)

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)

DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerName": str,
    },
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "Attributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "BackupId": NotRequired[str],
        "ServerName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "ServerName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "ServerEvents": List["ServerEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodeAssociationStatusRequestRequestTypeDef = TypedDict(
    "DescribeNodeAssociationStatusRequestRequestTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ServerName": str,
    },
)

DescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "DescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": NodeAssociationStatusType,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServersRequestRequestTypeDef = TypedDict(
    "DescribeServersRequestRequestTypeDef",
    {
        "ServerName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeServersResponseTypeDef = TypedDict(
    "DescribeServersResponseTypeDef",
    {
        "Servers": List["ServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateNodeRequestRequestTypeDef = TypedDict(
    "DisassociateNodeRequestRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
        "EngineAttributes": NotRequired[Sequence["EngineAttributeTypeDef"]],
    },
)

DisassociateNodeResponseTypeDef = TypedDict(
    "DisassociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EngineAttributeTypeDef = TypedDict(
    "EngineAttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

ExportServerEngineAttributeRequestRequestTypeDef = TypedDict(
    "ExportServerEngineAttributeRequestRequestTypeDef",
    {
        "ExportAttributeName": str,
        "ServerName": str,
        "InputAttributes": NotRequired[Sequence["EngineAttributeTypeDef"]],
    },
)

ExportServerEngineAttributeResponseTypeDef = TypedDict(
    "ExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": "EngineAttributeTypeDef",
        "ServerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
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

RestoreServerRequestRequestTypeDef = TypedDict(
    "RestoreServerRequestRequestTypeDef",
    {
        "BackupId": str,
        "ServerName": str,
        "InstanceType": NotRequired[str],
        "KeyPair": NotRequired[str],
    },
)

RestoreServerResponseTypeDef = TypedDict(
    "RestoreServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerEventTypeDef = TypedDict(
    "ServerEventTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "ServerName": NotRequired[str],
        "Message": NotRequired[str],
        "LogUrl": NotRequired[str],
    },
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BackupRetentionCount": NotRequired[int],
        "ServerName": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "CloudFormationStackArn": NotRequired[str],
        "CustomDomain": NotRequired[str],
        "DisableAutomatedBackup": NotRequired[bool],
        "Endpoint": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineModel": NotRequired[str],
        "EngineAttributes": NotRequired[List["EngineAttributeTypeDef"]],
        "EngineVersion": NotRequired[str],
        "InstanceProfileArn": NotRequired[str],
        "InstanceType": NotRequired[str],
        "KeyPair": NotRequired[str],
        "MaintenanceStatus": NotRequired[MaintenanceStatusType],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "ServiceRoleArn": NotRequired[str],
        "Status": NotRequired[ServerStatusType],
        "StatusReason": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "ServerArn": NotRequired[str],
    },
)

StartMaintenanceRequestRequestTypeDef = TypedDict(
    "StartMaintenanceRequestRequestTypeDef",
    {
        "ServerName": str,
        "EngineAttributes": NotRequired[Sequence["EngineAttributeTypeDef"]],
    },
)

StartMaintenanceResponseTypeDef = TypedDict(
    "StartMaintenanceResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateServerEngineAttributesRequestRequestTypeDef = TypedDict(
    "UpdateServerEngineAttributesRequestRequestTypeDef",
    {
        "ServerName": str,
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)

UpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "UpdateServerEngineAttributesResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServerRequestRequestTypeDef = TypedDict(
    "UpdateServerRequestRequestTypeDef",
    {
        "ServerName": str,
        "DisableAutomatedBackup": NotRequired[bool],
        "BackupRetentionCount": NotRequired[int],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
    },
)

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
