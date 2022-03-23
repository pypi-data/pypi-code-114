"""
Type annotations for snow-device-management service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_snow_device_management/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_snow_device_management.type_defs import CancelTaskInputRequestTypeDef

    data: CancelTaskInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AttachmentStatusType,
    ExecutionStateType,
    InstanceStateNameType,
    IpAddressAssignmentType,
    PhysicalConnectorTypeType,
    TaskStateType,
    UnlockStateType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelTaskInputRequestTypeDef",
    "CancelTaskOutputTypeDef",
    "CapacityTypeDef",
    "CommandTypeDef",
    "CpuOptionsTypeDef",
    "CreateTaskInputRequestTypeDef",
    "CreateTaskOutputTypeDef",
    "DescribeDeviceEc2InputRequestTypeDef",
    "DescribeDeviceEc2OutputTypeDef",
    "DescribeDeviceInputRequestTypeDef",
    "DescribeDeviceOutputTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeTaskInputRequestTypeDef",
    "DescribeTaskOutputTypeDef",
    "DeviceSummaryTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "ExecutionSummaryTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceStateTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListDeviceResourcesInputRequestTypeDef",
    "ListDeviceResourcesOutputTypeDef",
    "ListDevicesInputRequestTypeDef",
    "ListDevicesOutputTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTasksInputRequestTypeDef",
    "ListTasksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PhysicalNetworkInterfaceTypeDef",
    "ResourceSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SoftwareInformationTypeDef",
    "TagResourceInputRequestTypeDef",
    "TaskSummaryTypeDef",
    "UntagResourceInputRequestTypeDef",
)

CancelTaskInputRequestTypeDef = TypedDict(
    "CancelTaskInputRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelTaskOutputTypeDef = TypedDict(
    "CancelTaskOutputTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "available": NotRequired[int],
        "name": NotRequired[str],
        "total": NotRequired[int],
        "unit": NotRequired[str],
        "used": NotRequired[int],
    },
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "reboot": NotRequired[Mapping[str, Any]],
        "unlock": NotRequired[Mapping[str, Any]],
    },
)

CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "coreCount": NotRequired[int],
        "threadsPerCore": NotRequired[int],
    },
)

CreateTaskInputRequestTypeDef = TypedDict(
    "CreateTaskInputRequestTypeDef",
    {
        "command": "CommandTypeDef",
        "targets": Sequence[str],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateTaskOutputTypeDef = TypedDict(
    "CreateTaskOutputTypeDef",
    {
        "taskArn": str,
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceEc2InputRequestTypeDef = TypedDict(
    "DescribeDeviceEc2InputRequestTypeDef",
    {
        "instanceIds": Sequence[str],
        "managedDeviceId": str,
    },
)

DescribeDeviceEc2OutputTypeDef = TypedDict(
    "DescribeDeviceEc2OutputTypeDef",
    {
        "instances": List["InstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceInputRequestTypeDef = TypedDict(
    "DescribeDeviceInputRequestTypeDef",
    {
        "managedDeviceId": str,
    },
)

DescribeDeviceOutputTypeDef = TypedDict(
    "DescribeDeviceOutputTypeDef",
    {
        "associatedWithJob": str,
        "deviceCapacities": List["CapacityTypeDef"],
        "deviceState": UnlockStateType,
        "deviceType": str,
        "lastReachedOutAt": datetime,
        "lastUpdatedAt": datetime,
        "managedDeviceArn": str,
        "managedDeviceId": str,
        "physicalNetworkInterfaces": List["PhysicalNetworkInterfaceTypeDef"],
        "software": "SoftwareInformationTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "managedDeviceId": str,
        "taskId": str,
    },
)

DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionId": str,
        "lastUpdatedAt": datetime,
        "managedDeviceId": str,
        "startedAt": datetime,
        "state": ExecutionStateType,
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskInputRequestTypeDef = TypedDict(
    "DescribeTaskInputRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeTaskOutputTypeDef = TypedDict(
    "DescribeTaskOutputTypeDef",
    {
        "completedAt": datetime,
        "createdAt": datetime,
        "description": str,
        "lastUpdatedAt": datetime,
        "state": TaskStateType,
        "tags": Dict[str, str],
        "targets": List[str],
        "taskArn": str,
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "associatedWithJob": NotRequired[str],
        "managedDeviceArn": NotRequired[str],
        "managedDeviceId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "attachTime": NotRequired[datetime],
        "deleteOnTermination": NotRequired[bool],
        "status": NotRequired[AttachmentStatusType],
        "volumeId": NotRequired[str],
    },
)

ExecutionSummaryTypeDef = TypedDict(
    "ExecutionSummaryTypeDef",
    {
        "executionId": NotRequired[str],
        "managedDeviceId": NotRequired[str],
        "state": NotRequired[ExecutionStateType],
        "taskId": NotRequired[str],
    },
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": NotRequired[str],
        "ebs": NotRequired["EbsInstanceBlockDeviceTypeDef"],
    },
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": NotRequired[int],
        "name": NotRequired[InstanceStateNameType],
    },
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "instance": NotRequired["InstanceTypeDef"],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "amiLaunchIndex": NotRequired[int],
        "blockDeviceMappings": NotRequired[List["InstanceBlockDeviceMappingTypeDef"]],
        "cpuOptions": NotRequired["CpuOptionsTypeDef"],
        "createdAt": NotRequired[datetime],
        "imageId": NotRequired[str],
        "instanceId": NotRequired[str],
        "instanceType": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "publicIpAddress": NotRequired[str],
        "rootDeviceName": NotRequired[str],
        "securityGroups": NotRequired[List["SecurityGroupIdentifierTypeDef"]],
        "state": NotRequired["InstanceStateTypeDef"],
        "updatedAt": NotRequired[datetime],
    },
)

ListDeviceResourcesInputRequestTypeDef = TypedDict(
    "ListDeviceResourcesInputRequestTypeDef",
    {
        "managedDeviceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "type": NotRequired[str],
    },
)

ListDeviceResourcesOutputTypeDef = TypedDict(
    "ListDeviceResourcesOutputTypeDef",
    {
        "nextToken": str,
        "resources": List["ResourceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesInputRequestTypeDef = TypedDict(
    "ListDevicesInputRequestTypeDef",
    {
        "jobId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListDevicesOutputTypeDef = TypedDict(
    "ListDevicesOutputTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExecutionsInputRequestTypeDef = TypedDict(
    "ListExecutionsInputRequestTypeDef",
    {
        "taskId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "state": NotRequired[ExecutionStateType],
    },
)

ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List["ExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksInputRequestTypeDef = TypedDict(
    "ListTasksInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "state": NotRequired[TaskStateType],
    },
)

ListTasksOutputTypeDef = TypedDict(
    "ListTasksOutputTypeDef",
    {
        "nextToken": str,
        "tasks": List["TaskSummaryTypeDef"],
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

PhysicalNetworkInterfaceTypeDef = TypedDict(
    "PhysicalNetworkInterfaceTypeDef",
    {
        "defaultGateway": NotRequired[str],
        "ipAddress": NotRequired[str],
        "ipAddressAssignment": NotRequired[IpAddressAssignmentType],
        "macAddress": NotRequired[str],
        "netmask": NotRequired[str],
        "physicalConnectorType": NotRequired[PhysicalConnectorTypeType],
        "physicalNetworkInterfaceId": NotRequired[str],
    },
)

ResourceSummaryTypeDef = TypedDict(
    "ResourceSummaryTypeDef",
    {
        "resourceType": str,
        "arn": NotRequired[str],
        "id": NotRequired[str],
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

SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "groupId": NotRequired[str],
        "groupName": NotRequired[str],
    },
)

SoftwareInformationTypeDef = TypedDict(
    "SoftwareInformationTypeDef",
    {
        "installState": NotRequired[str],
        "installedVersion": NotRequired[str],
        "installingVersion": NotRequired[str],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TaskSummaryTypeDef = TypedDict(
    "TaskSummaryTypeDef",
    {
        "taskId": str,
        "state": NotRequired[TaskStateType],
        "tags": NotRequired[Dict[str, str]],
        "taskArn": NotRequired[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
