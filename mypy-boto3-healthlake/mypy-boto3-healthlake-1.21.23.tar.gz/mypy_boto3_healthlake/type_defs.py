"""
Type annotations for healthlake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import CreateFHIRDatastoreRequestRequestTypeDef

    data: CreateFHIRDatastoreRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import CmkTypeType, DatastoreStatusType, JobStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateFHIRDatastoreRequestRequestTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DatastorePropertiesTypeDef",
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "DescribeFHIRExportJobRequestRequestTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "DescribeFHIRImportJobRequestRequestTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "KmsEncryptionConfigTypeDef",
    "ListFHIRDatastoresRequestRequestTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "ListFHIRExportJobsRequestRequestTypeDef",
    "ListFHIRExportJobsResponseTypeDef",
    "ListFHIRImportJobsRequestRequestTypeDef",
    "ListFHIRImportJobsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "SseConfigurationTypeDef",
    "StartFHIRExportJobRequestRequestTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobRequestRequestTypeDef",
    "StartFHIRImportJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

CreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "CreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreName": NotRequired[str],
        "SseConfiguration": NotRequired["SseConfigurationTypeDef"],
        "PreloadDataConfig": NotRequired["PreloadDataConfigTypeDef"],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFHIRDatastoreResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatastoreFilterTypeDef = TypedDict(
    "DatastoreFilterTypeDef",
    {
        "DatastoreName": NotRequired[str],
        "DatastoreStatus": NotRequired[DatastoreStatusType],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "CreatedAfter": NotRequired[Union[datetime, str]],
    },
)

DatastorePropertiesTypeDef = TypedDict(
    "DatastorePropertiesTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreEndpoint": str,
        "DatastoreName": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "SseConfiguration": NotRequired["SseConfigurationTypeDef"],
        "PreloadDataConfig": NotRequired["PreloadDataConfigTypeDef"],
    },
)

DeleteFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": NotRequired[str],
    },
)

DeleteFHIRDatastoreResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": NotRequired[str],
    },
)

DescribeFHIRDatastoreResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseTypeDef",
    {
        "DatastoreProperties": "DatastorePropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRExportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRExportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRExportJobResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseTypeDef",
    {
        "ExportJobProperties": "ExportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRImportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRImportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRImportJobResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseTypeDef",
    {
        "ImportJobProperties": "ImportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportJobPropertiesTypeDef = TypedDict(
    "ExportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "JobName": NotRequired[str],
        "EndTime": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "Message": NotRequired[str],
    },
)

ImportJobPropertiesTypeDef = TypedDict(
    "ImportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "JobName": NotRequired[str],
        "EndTime": NotRequired[datetime],
        "JobOutputDataConfig": NotRequired["OutputDataConfigTypeDef"],
        "DataAccessRoleArn": NotRequired[str],
        "Message": NotRequired[str],
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": NotRequired[str],
    },
)

KmsEncryptionConfigTypeDef = TypedDict(
    "KmsEncryptionConfigTypeDef",
    {
        "CmkType": CmkTypeType,
        "KmsKeyId": NotRequired[str],
    },
)

ListFHIRDatastoresRequestRequestTypeDef = TypedDict(
    "ListFHIRDatastoresRequestRequestTypeDef",
    {
        "Filter": NotRequired["DatastoreFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFHIRDatastoresResponseTypeDef = TypedDict(
    "ListFHIRDatastoresResponseTypeDef",
    {
        "DatastorePropertiesList": List["DatastorePropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFHIRExportJobsRequestRequestTypeDef = TypedDict(
    "ListFHIRExportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmittedBefore": NotRequired[Union[datetime, str]],
        "SubmittedAfter": NotRequired[Union[datetime, str]],
    },
)

ListFHIRExportJobsResponseTypeDef = TypedDict(
    "ListFHIRExportJobsResponseTypeDef",
    {
        "ExportJobPropertiesList": List["ExportJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFHIRImportJobsRequestRequestTypeDef = TypedDict(
    "ListFHIRImportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmittedBefore": NotRequired[Union[datetime, str]],
        "SubmittedAfter": NotRequired[Union[datetime, str]],
    },
)

ListFHIRImportJobsResponseTypeDef = TypedDict(
    "ListFHIRImportJobsResponseTypeDef",
    {
        "ImportJobPropertiesList": List["ImportJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Configuration": NotRequired["S3ConfigurationTypeDef"],
    },
)

PreloadDataConfigTypeDef = TypedDict(
    "PreloadDataConfigTypeDef",
    {
        "PreloadDataType": Literal["SYNTHEA"],
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

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
    },
)

SseConfigurationTypeDef = TypedDict(
    "SseConfigurationTypeDef",
    {
        "KmsEncryptionConfig": "KmsEncryptionConfigTypeDef",
    },
)

StartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "StartFHIRExportJobRequestRequestTypeDef",
    {
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
        "JobName": NotRequired[str],
    },
)

StartFHIRExportJobResponseTypeDef = TypedDict(
    "StartFHIRExportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "StartFHIRImportJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "JobOutputDataConfig": "OutputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
        "JobName": NotRequired[str],
    },
)

StartFHIRImportJobResponseTypeDef = TypedDict(
    "StartFHIRImportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
