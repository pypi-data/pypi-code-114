"""
Type annotations for backup-gateway service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_backup_gateway/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_backup_gateway.type_defs import AssociateGatewayToServerInputRequestTypeDef

    data: AssociateGatewayToServerInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import HypervisorStateType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateGatewayToServerInputRequestTypeDef",
    "AssociateGatewayToServerOutputTypeDef",
    "CreateGatewayInputRequestTypeDef",
    "CreateGatewayOutputTypeDef",
    "DeleteGatewayInputRequestTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteHypervisorInputRequestTypeDef",
    "DeleteHypervisorOutputTypeDef",
    "DisassociateGatewayFromServerInputRequestTypeDef",
    "DisassociateGatewayFromServerOutputTypeDef",
    "GatewayTypeDef",
    "HypervisorTypeDef",
    "ImportHypervisorConfigurationInputRequestTypeDef",
    "ImportHypervisorConfigurationOutputTypeDef",
    "ListGatewaysInputRequestTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListHypervisorsInputRequestTypeDef",
    "ListHypervisorsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualMachinesInputRequestTypeDef",
    "ListVirtualMachinesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutMaintenanceStartTimeInputRequestTypeDef",
    "PutMaintenanceStartTimeOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagResourceOutputTypeDef",
    "TagTypeDef",
    "TestHypervisorConfigurationInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagResourceOutputTypeDef",
    "UpdateGatewayInformationInputRequestTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateHypervisorInputRequestTypeDef",
    "UpdateHypervisorOutputTypeDef",
    "VirtualMachineTypeDef",
)

AssociateGatewayToServerInputRequestTypeDef = TypedDict(
    "AssociateGatewayToServerInputRequestTypeDef",
    {
        "GatewayArn": str,
        "ServerArn": str,
    },
)

AssociateGatewayToServerOutputTypeDef = TypedDict(
    "AssociateGatewayToServerOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGatewayInputRequestTypeDef = TypedDict(
    "CreateGatewayInputRequestTypeDef",
    {
        "ActivationKey": str,
        "GatewayDisplayName": str,
        "GatewayType": Literal["BACKUP_VM"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGatewayOutputTypeDef = TypedDict(
    "CreateGatewayOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayInputRequestTypeDef = TypedDict(
    "DeleteGatewayInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHypervisorInputRequestTypeDef = TypedDict(
    "DeleteHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)

DeleteHypervisorOutputTypeDef = TypedDict(
    "DeleteHypervisorOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateGatewayFromServerInputRequestTypeDef = TypedDict(
    "DisassociateGatewayFromServerInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

DisassociateGatewayFromServerOutputTypeDef = TypedDict(
    "DisassociateGatewayFromServerOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {
        "GatewayArn": NotRequired[str],
        "GatewayDisplayName": NotRequired[str],
        "GatewayType": NotRequired[Literal["BACKUP_VM"]],
        "HypervisorId": NotRequired[str],
        "LastSeenTime": NotRequired[datetime],
    },
)

HypervisorTypeDef = TypedDict(
    "HypervisorTypeDef",
    {
        "Host": NotRequired[str],
        "HypervisorArn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[HypervisorStateType],
    },
)

ImportHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "ImportHypervisorConfigurationInputRequestTypeDef",
    {
        "Host": str,
        "Name": str,
        "KmsKeyArn": NotRequired[str],
        "Password": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Username": NotRequired[str],
    },
)

ImportHypervisorConfigurationOutputTypeDef = TypedDict(
    "ImportHypervisorConfigurationOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysInputRequestTypeDef = TypedDict(
    "ListGatewaysInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List["GatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHypervisorsInputRequestTypeDef = TypedDict(
    "ListHypervisorsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListHypervisorsOutputTypeDef = TypedDict(
    "ListHypervisorsOutputTypeDef",
    {
        "Hypervisors": List["HypervisorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualMachinesInputRequestTypeDef = TypedDict(
    "ListVirtualMachinesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListVirtualMachinesOutputTypeDef = TypedDict(
    "ListVirtualMachinesOutputTypeDef",
    {
        "NextToken": str,
        "VirtualMachines": List["VirtualMachineTypeDef"],
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

PutMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "PutMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayArn": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfMonth": NotRequired[int],
        "DayOfWeek": NotRequired[int],
    },
)

PutMaintenanceStartTimeOutputTypeDef = TypedDict(
    "PutMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayArn": str,
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagResourceOutputTypeDef = TypedDict(
    "TagResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "TestHypervisorConfigurationInputRequestTypeDef",
    {
        "GatewayArn": str,
        "Host": str,
        "Password": NotRequired[str],
        "Username": NotRequired[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UntagResourceOutputTypeDef = TypedDict(
    "UntagResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "UpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayArn": str,
        "GatewayDisplayName": NotRequired[str],
    },
)

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateHypervisorInputRequestTypeDef = TypedDict(
    "UpdateHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
        "Host": NotRequired[str],
        "Password": NotRequired[str],
        "Username": NotRequired[str],
    },
)

UpdateHypervisorOutputTypeDef = TypedDict(
    "UpdateHypervisorOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualMachineTypeDef = TypedDict(
    "VirtualMachineTypeDef",
    {
        "HostName": NotRequired[str],
        "HypervisorId": NotRequired[str],
        "LastBackupDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "Path": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
