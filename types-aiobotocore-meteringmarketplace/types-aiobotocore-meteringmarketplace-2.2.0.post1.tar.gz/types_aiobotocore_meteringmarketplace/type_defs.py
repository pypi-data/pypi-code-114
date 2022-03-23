"""
Type annotations for meteringmarketplace service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_meteringmarketplace/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_meteringmarketplace.type_defs import BatchMeterUsageRequestRequestTypeDef

    data: BatchMeterUsageRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import UsageRecordResultStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchMeterUsageRequestRequestTypeDef",
    "BatchMeterUsageResultTypeDef",
    "MeterUsageRequestRequestTypeDef",
    "MeterUsageResultTypeDef",
    "RegisterUsageRequestRequestTypeDef",
    "RegisterUsageResultTypeDef",
    "ResolveCustomerRequestRequestTypeDef",
    "ResolveCustomerResultTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "UsageAllocationTypeDef",
    "UsageRecordResultTypeDef",
    "UsageRecordTypeDef",
)

BatchMeterUsageRequestRequestTypeDef = TypedDict(
    "BatchMeterUsageRequestRequestTypeDef",
    {
        "UsageRecords": Sequence["UsageRecordTypeDef"],
        "ProductCode": str,
    },
)

BatchMeterUsageResultTypeDef = TypedDict(
    "BatchMeterUsageResultTypeDef",
    {
        "Results": List["UsageRecordResultTypeDef"],
        "UnprocessedRecords": List["UsageRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MeterUsageRequestRequestTypeDef = TypedDict(
    "MeterUsageRequestRequestTypeDef",
    {
        "ProductCode": str,
        "Timestamp": Union[datetime, str],
        "UsageDimension": str,
        "UsageQuantity": NotRequired[int],
        "DryRun": NotRequired[bool],
        "UsageAllocations": NotRequired[Sequence["UsageAllocationTypeDef"]],
    },
)

MeterUsageResultTypeDef = TypedDict(
    "MeterUsageResultTypeDef",
    {
        "MeteringRecordId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterUsageRequestRequestTypeDef = TypedDict(
    "RegisterUsageRequestRequestTypeDef",
    {
        "ProductCode": str,
        "PublicKeyVersion": int,
        "Nonce": NotRequired[str],
    },
)

RegisterUsageResultTypeDef = TypedDict(
    "RegisterUsageResultTypeDef",
    {
        "PublicKeyRotationTimestamp": datetime,
        "Signature": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveCustomerRequestRequestTypeDef = TypedDict(
    "ResolveCustomerRequestRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)

ResolveCustomerResultTypeDef = TypedDict(
    "ResolveCustomerResultTypeDef",
    {
        "CustomerIdentifier": str,
        "ProductCode": str,
        "CustomerAWSAccountId": str,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UsageAllocationTypeDef = TypedDict(
    "UsageAllocationTypeDef",
    {
        "AllocatedUsageQuantity": int,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UsageRecordResultTypeDef = TypedDict(
    "UsageRecordResultTypeDef",
    {
        "UsageRecord": NotRequired["UsageRecordTypeDef"],
        "MeteringRecordId": NotRequired[str],
        "Status": NotRequired[UsageRecordResultStatusType],
    },
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "Timestamp": Union[datetime, str],
        "CustomerIdentifier": str,
        "Dimension": str,
        "Quantity": NotRequired[int],
        "UsageAllocations": NotRequired[Sequence["UsageAllocationTypeDef"]],
    },
)
