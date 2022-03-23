"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_marketplacecommerceanalytics/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_marketplacecommerceanalytics.type_defs import GenerateDataSetRequestRequestTypeDef

    data: GenerateDataSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, Mapping, Union

from typing_extensions import NotRequired

from .literals import DataSetTypeType, SupportDataSetTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GenerateDataSetRequestRequestTypeDef",
    "GenerateDataSetResultTypeDef",
    "ResponseMetadataTypeDef",
    "StartSupportDataExportRequestRequestTypeDef",
    "StartSupportDataExportResultTypeDef",
)

GenerateDataSetRequestRequestTypeDef = TypedDict(
    "GenerateDataSetRequestRequestTypeDef",
    {
        "dataSetType": DataSetTypeType,
        "dataSetPublicationDate": Union[datetime, str],
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
        "destinationS3Prefix": NotRequired[str],
        "customerDefinedValues": NotRequired[Mapping[str, str]],
    },
)

GenerateDataSetResultTypeDef = TypedDict(
    "GenerateDataSetResultTypeDef",
    {
        "dataSetRequestId": str,
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

StartSupportDataExportRequestRequestTypeDef = TypedDict(
    "StartSupportDataExportRequestRequestTypeDef",
    {
        "dataSetType": SupportDataSetTypeType,
        "fromDate": Union[datetime, str],
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
        "destinationS3Prefix": NotRequired[str],
        "customerDefinedValues": NotRequired[Mapping[str, str]],
    },
)

StartSupportDataExportResultTypeDef = TypedDict(
    "StartSupportDataExportResultTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
