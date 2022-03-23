"""
Type annotations for migrationhub-config service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhub_config/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_migrationhub_config.type_defs import CreateHomeRegionControlRequestRequestTypeDef

    data: CreateHomeRegionControlRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateHomeRegionControlRequestRequestTypeDef",
    "CreateHomeRegionControlResultTypeDef",
    "DescribeHomeRegionControlsRequestRequestTypeDef",
    "DescribeHomeRegionControlsResultTypeDef",
    "GetHomeRegionResultTypeDef",
    "HomeRegionControlTypeDef",
    "ResponseMetadataTypeDef",
    "TargetTypeDef",
)

CreateHomeRegionControlRequestRequestTypeDef = TypedDict(
    "CreateHomeRegionControlRequestRequestTypeDef",
    {
        "HomeRegion": str,
        "Target": "TargetTypeDef",
        "DryRun": NotRequired[bool],
    },
)

CreateHomeRegionControlResultTypeDef = TypedDict(
    "CreateHomeRegionControlResultTypeDef",
    {
        "HomeRegionControl": "HomeRegionControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHomeRegionControlsRequestRequestTypeDef = TypedDict(
    "DescribeHomeRegionControlsRequestRequestTypeDef",
    {
        "ControlId": NotRequired[str],
        "HomeRegion": NotRequired[str],
        "Target": NotRequired["TargetTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeHomeRegionControlsResultTypeDef = TypedDict(
    "DescribeHomeRegionControlsResultTypeDef",
    {
        "HomeRegionControls": List["HomeRegionControlTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHomeRegionResultTypeDef = TypedDict(
    "GetHomeRegionResultTypeDef",
    {
        "HomeRegion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HomeRegionControlTypeDef = TypedDict(
    "HomeRegionControlTypeDef",
    {
        "ControlId": NotRequired[str],
        "HomeRegion": NotRequired[str],
        "Target": NotRequired["TargetTypeDef"],
        "RequestedTime": NotRequired[datetime],
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

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Type": Literal["ACCOUNT"],
        "Id": NotRequired[str],
    },
)
