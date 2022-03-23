"""
Type annotations for iot1click-devices service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_iot1click_devices/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_iot1click_devices.type_defs import ClaimDevicesByClaimCodeRequestRequestTypeDef

    data: ClaimDevicesByClaimCodeRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    "ClaimDevicesByClaimCodeResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DeviceDescriptionTypeDef",
    "DeviceEventTypeDef",
    "DeviceMethodTypeDef",
    "DeviceTypeDef",
    "FinalizeDeviceClaimRequestRequestTypeDef",
    "FinalizeDeviceClaimResponseTypeDef",
    "GetDeviceMethodsRequestRequestTypeDef",
    "GetDeviceMethodsResponseTypeDef",
    "InitiateDeviceClaimRequestRequestTypeDef",
    "InitiateDeviceClaimResponseTypeDef",
    "InvokeDeviceMethodRequestRequestTypeDef",
    "InvokeDeviceMethodResponseTypeDef",
    "ListDeviceEventsRequestRequestTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnclaimDeviceRequestRequestTypeDef",
    "UnclaimDeviceResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceStateRequestRequestTypeDef",
)

ClaimDevicesByClaimCodeRequestRequestTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    {
        "ClaimCode": str,
    },
)

ClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeResponseTypeDef",
    {
        "ClaimCode": str,
        "Total": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceDescription": "DeviceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
        "DeviceId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "RemainingLife": NotRequired[float],
        "Type": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {
        "Device": NotRequired["DeviceTypeDef"],
        "StdEvent": NotRequired[str],
    },
)

DeviceMethodTypeDef = TypedDict(
    "DeviceMethodTypeDef",
    {
        "DeviceType": NotRequired[str],
        "MethodName": NotRequired[str],
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Attributes": NotRequired[Dict[str, Any]],
        "DeviceId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

FinalizeDeviceClaimRequestRequestTypeDef = TypedDict(
    "FinalizeDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

FinalizeDeviceClaimResponseTypeDef = TypedDict(
    "FinalizeDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceMethodsRequestRequestTypeDef = TypedDict(
    "GetDeviceMethodsRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

GetDeviceMethodsResponseTypeDef = TypedDict(
    "GetDeviceMethodsResponseTypeDef",
    {
        "DeviceMethods": List["DeviceMethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiateDeviceClaimRequestRequestTypeDef = TypedDict(
    "InitiateDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

InitiateDeviceClaimResponseTypeDef = TypedDict(
    "InitiateDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvokeDeviceMethodRequestRequestTypeDef = TypedDict(
    "InvokeDeviceMethodRequestRequestTypeDef",
    {
        "DeviceId": str,
        "DeviceMethod": NotRequired["DeviceMethodTypeDef"],
        "DeviceMethodParameters": NotRequired[str],
    },
)

InvokeDeviceMethodResponseTypeDef = TypedDict(
    "InvokeDeviceMethodResponseTypeDef",
    {
        "DeviceMethodResponse": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceEventsRequestRequestTypeDef = TypedDict(
    "ListDeviceEventsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": Union[datetime, str],
        "ToTimeStamp": Union[datetime, str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {
        "Events": List["DeviceEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceDescriptionTypeDef"],
        "NextToken": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UnclaimDeviceRequestRequestTypeDef = TypedDict(
    "UnclaimDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)

UnclaimDeviceResponseTypeDef = TypedDict(
    "UnclaimDeviceResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDeviceStateRequestRequestTypeDef = TypedDict(
    "UpdateDeviceStateRequestRequestTypeDef",
    {
        "DeviceId": str,
        "Enabled": NotRequired[bool],
    },
)
