"""
Type annotations for importexport service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_importexport/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_importexport.type_defs import ArtifactTypeDef

    data: ArtifactTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import JobTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArtifactTypeDef",
    "CancelJobInputRequestTypeDef",
    "CancelJobOutputTypeDef",
    "CreateJobInputRequestTypeDef",
    "CreateJobOutputTypeDef",
    "GetShippingLabelInputRequestTypeDef",
    "GetShippingLabelOutputTypeDef",
    "GetStatusInputRequestTypeDef",
    "GetStatusOutputTypeDef",
    "JobTypeDef",
    "ListJobsInputRequestTypeDef",
    "ListJobsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateJobInputRequestTypeDef",
    "UpdateJobOutputTypeDef",
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "Description": NotRequired[str],
        "URL": NotRequired[str],
    },
)

CancelJobInputRequestTypeDef = TypedDict(
    "CancelJobInputRequestTypeDef",
    {
        "JobId": str,
        "APIVersion": NotRequired[str],
    },
)

CancelJobOutputTypeDef = TypedDict(
    "CancelJobOutputTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobInputRequestTypeDef = TypedDict(
    "CreateJobInputRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Manifest": str,
        "ValidateOnly": bool,
        "ManifestAddendum": NotRequired[str],
        "APIVersion": NotRequired[str],
    },
)

CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetShippingLabelInputRequestTypeDef = TypedDict(
    "GetShippingLabelInputRequestTypeDef",
    {
        "jobIds": Sequence[str],
        "name": NotRequired[str],
        "company": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "country": NotRequired[str],
        "stateOrProvince": NotRequired[str],
        "city": NotRequired[str],
        "postalCode": NotRequired[str],
        "street1": NotRequired[str],
        "street2": NotRequired[str],
        "street3": NotRequired[str],
        "APIVersion": NotRequired[str],
    },
)

GetShippingLabelOutputTypeDef = TypedDict(
    "GetShippingLabelOutputTypeDef",
    {
        "ShippingLabelURL": str,
        "Warning": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStatusInputRequestTypeDef = TypedDict(
    "GetStatusInputRequestTypeDef",
    {
        "JobId": str,
        "APIVersion": NotRequired[str],
    },
)

GetStatusOutputTypeDef = TypedDict(
    "GetStatusOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "JobId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "IsCanceled": NotRequired[bool],
        "JobType": NotRequired[JobTypeType],
    },
)

ListJobsInputRequestTypeDef = TypedDict(
    "ListJobsInputRequestTypeDef",
    {
        "MaxJobs": NotRequired[int],
        "Marker": NotRequired[str],
        "APIVersion": NotRequired[str],
    },
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "IsTruncated": bool,
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

UpdateJobInputRequestTypeDef = TypedDict(
    "UpdateJobInputRequestTypeDef",
    {
        "JobId": str,
        "Manifest": str,
        "JobType": JobTypeType,
        "ValidateOnly": bool,
        "APIVersion": NotRequired[str],
    },
)

UpdateJobOutputTypeDef = TypedDict(
    "UpdateJobOutputTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
