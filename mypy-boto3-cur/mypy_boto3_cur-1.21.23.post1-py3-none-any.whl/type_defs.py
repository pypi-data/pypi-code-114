"""
Type annotations for cur service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cur.type_defs import DeleteReportDefinitionRequestRequestTypeDef

    data: DeleteReportDefinitionRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from typing_extensions import NotRequired

from .literals import (
    AdditionalArtifactType,
    AWSRegionType,
    CompressionFormatType,
    ReportFormatType,
    ReportVersioningType,
    TimeUnitType,
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
    "DeleteReportDefinitionRequestRequestTypeDef",
    "DeleteReportDefinitionResponseTypeDef",
    "DescribeReportDefinitionsRequestRequestTypeDef",
    "DescribeReportDefinitionsResponseTypeDef",
    "ModifyReportDefinitionRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutReportDefinitionRequestRequestTypeDef",
    "ReportDefinitionTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteReportDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteReportDefinitionRequestRequestTypeDef",
    {
        "ReportName": NotRequired[str],
    },
)

DeleteReportDefinitionResponseTypeDef = TypedDict(
    "DeleteReportDefinitionResponseTypeDef",
    {
        "ResponseMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReportDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeReportDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeReportDefinitionsResponseTypeDef = TypedDict(
    "DescribeReportDefinitionsResponseTypeDef",
    {
        "ReportDefinitions": List["ReportDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReportDefinitionRequestRequestTypeDef = TypedDict(
    "ModifyReportDefinitionRequestRequestTypeDef",
    {
        "ReportName": str,
        "ReportDefinition": "ReportDefinitionTypeDef",
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

PutReportDefinitionRequestRequestTypeDef = TypedDict(
    "PutReportDefinitionRequestRequestTypeDef",
    {
        "ReportDefinition": "ReportDefinitionTypeDef",
    },
)

ReportDefinitionTypeDef = TypedDict(
    "ReportDefinitionTypeDef",
    {
        "ReportName": str,
        "TimeUnit": TimeUnitType,
        "Format": ReportFormatType,
        "Compression": CompressionFormatType,
        "AdditionalSchemaElements": List[Literal["RESOURCES"]],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": AWSRegionType,
        "AdditionalArtifacts": NotRequired[List[AdditionalArtifactType]],
        "RefreshClosedReports": NotRequired[bool],
        "ReportVersioning": NotRequired[ReportVersioningType],
        "BillingViewArn": NotRequired[str],
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
