"""
Type annotations for applicationcostprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_applicationcostprofiler.type_defs import DeleteReportDefinitionRequestRequestTypeDef

    data: DeleteReportDefinitionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from typing_extensions import NotRequired

from .literals import FormatType, ReportFrequencyType, S3BucketRegionType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteReportDefinitionRequestRequestTypeDef",
    "DeleteReportDefinitionResultTypeDef",
    "GetReportDefinitionRequestRequestTypeDef",
    "GetReportDefinitionResultTypeDef",
    "ImportApplicationUsageRequestRequestTypeDef",
    "ImportApplicationUsageResultTypeDef",
    "ListReportDefinitionsRequestRequestTypeDef",
    "ListReportDefinitionsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutReportDefinitionRequestRequestTypeDef",
    "PutReportDefinitionResultTypeDef",
    "ReportDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SourceS3LocationTypeDef",
    "UpdateReportDefinitionRequestRequestTypeDef",
    "UpdateReportDefinitionResultTypeDef",
)

DeleteReportDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
    },
)

DeleteReportDefinitionResultTypeDef = TypedDict(
    "DeleteReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReportDefinitionRequestRequestTypeDef = TypedDict(
    "GetReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
    },
)

GetReportDefinitionResultTypeDef = TypedDict(
    "GetReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
        "createdAt": datetime,
        "lastUpdated": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportApplicationUsageRequestRequestTypeDef = TypedDict(
    "ImportApplicationUsageRequestRequestTypeDef",
    {
        "sourceS3Location": "SourceS3LocationTypeDef",
    },
)

ImportApplicationUsageResultTypeDef = TypedDict(
    "ImportApplicationUsageResultTypeDef",
    {
        "importId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportDefinitionsRequestRequestTypeDef = TypedDict(
    "ListReportDefinitionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListReportDefinitionsResultTypeDef = TypedDict(
    "ListReportDefinitionsResultTypeDef",
    {
        "reportDefinitions": List["ReportDefinitionTypeDef"],
        "nextToken": str,
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

PutReportDefinitionRequestRequestTypeDef = TypedDict(
    "PutReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
    },
)

PutReportDefinitionResultTypeDef = TypedDict(
    "PutReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportDefinitionTypeDef = TypedDict(
    "ReportDefinitionTypeDef",
    {
        "reportId": NotRequired[str],
        "reportDescription": NotRequired[str],
        "reportFrequency": NotRequired[ReportFrequencyType],
        "format": NotRequired[FormatType],
        "destinationS3Location": NotRequired["S3LocationTypeDef"],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
)

SourceS3LocationTypeDef = TypedDict(
    "SourceS3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "region": NotRequired[S3BucketRegionType],
    },
)

UpdateReportDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
    },
)

UpdateReportDefinitionResultTypeDef = TypedDict(
    "UpdateReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
