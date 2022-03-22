"""
Type annotations for acm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_acm.type_defs import AddTagsToCertificateRequestRequestTypeDef

    data: AddTagsToCertificateRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    CertificateStatusType,
    CertificateTransparencyLoggingPreferenceType,
    CertificateTypeType,
    DomainStatusType,
    ExtendedKeyUsageNameType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyUsageNameType,
    RenewalEligibilityType,
    RenewalStatusType,
    RevocationReasonType,
    ValidationMethodType,
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
    "AddTagsToCertificateRequestRequestTypeDef",
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "DomainValidationTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "ExportCertificateRequestRequestTypeDef",
    "ExportCertificateResponseTypeDef",
    "ExtendedKeyUsageTypeDef",
    "FiltersTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetCertificateRequestRequestTypeDef",
    "GetCertificateResponseTypeDef",
    "ImportCertificateRequestRequestTypeDef",
    "ImportCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateRequestRequestTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountConfigurationRequestRequestTypeDef",
    "RemoveTagsFromCertificateRequestRequestTypeDef",
    "RenewCertificateRequestRequestTypeDef",
    "RenewalSummaryTypeDef",
    "RequestCertificateRequestRequestTypeDef",
    "RequestCertificateResponseTypeDef",
    "ResendValidationEmailRequestRequestTypeDef",
    "ResourceRecordTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "UpdateCertificateOptionsRequestRequestTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToCertificateRequestRequestTypeDef = TypedDict(
    "AddTagsToCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

CertificateDetailTypeDef = TypedDict(
    "CertificateDetailTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DomainName": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[List[str]],
        "DomainValidationOptions": NotRequired[List["DomainValidationTypeDef"]],
        "Serial": NotRequired[str],
        "Subject": NotRequired[str],
        "Issuer": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "IssuedAt": NotRequired[datetime],
        "ImportedAt": NotRequired[datetime],
        "Status": NotRequired[CertificateStatusType],
        "RevokedAt": NotRequired[datetime],
        "RevocationReason": NotRequired[RevocationReasonType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "KeyAlgorithm": NotRequired[KeyAlgorithmType],
        "SignatureAlgorithm": NotRequired[str],
        "InUseBy": NotRequired[List[str]],
        "FailureReason": NotRequired[FailureReasonType],
        "Type": NotRequired[CertificateTypeType],
        "RenewalSummary": NotRequired["RenewalSummaryTypeDef"],
        "KeyUsages": NotRequired[List["KeyUsageTypeDef"]],
        "ExtendedKeyUsages": NotRequired[List["ExtendedKeyUsageTypeDef"]],
        "CertificateAuthorityArn": NotRequired[str],
        "RenewalEligibility": NotRequired[RenewalEligibilityType],
        "Options": NotRequired["CertificateOptionsTypeDef"],
    },
)

CertificateOptionsTypeDef = TypedDict(
    "CertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": NotRequired[
            CertificateTransparencyLoggingPreferenceType
        ],
    },
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DomainName": NotRequired[str],
    },
)

DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "Certificate": "CertificateDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainValidationOptionTypeDef = TypedDict(
    "DomainValidationOptionTypeDef",
    {
        "DomainName": str,
        "ValidationDomain": str,
    },
)

DomainValidationTypeDef = TypedDict(
    "DomainValidationTypeDef",
    {
        "DomainName": str,
        "ValidationEmails": NotRequired[List[str]],
        "ValidationDomain": NotRequired[str],
        "ValidationStatus": NotRequired[DomainStatusType],
        "ResourceRecord": NotRequired["ResourceRecordTypeDef"],
        "ValidationMethod": NotRequired[ValidationMethodType],
    },
)

ExpiryEventsConfigurationTypeDef = TypedDict(
    "ExpiryEventsConfigurationTypeDef",
    {
        "DaysBeforeExpiry": NotRequired[int],
    },
)

ExportCertificateRequestRequestTypeDef = TypedDict(
    "ExportCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Passphrase": Union[bytes, IO[bytes], StreamingBody],
    },
)

ExportCertificateResponseTypeDef = TypedDict(
    "ExportCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "PrivateKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "Name": NotRequired[ExtendedKeyUsageNameType],
        "OID": NotRequired[str],
    },
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "extendedKeyUsage": NotRequired[Sequence[ExtendedKeyUsageNameType]],
        "keyUsage": NotRequired[Sequence[KeyUsageNameType]],
        "keyTypes": NotRequired[Sequence[KeyAlgorithmType]],
    },
)

GetAccountConfigurationResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseTypeDef",
    {
        "ExpiryEvents": "ExpiryEventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportCertificateRequestRequestTypeDef = TypedDict(
    "ImportCertificateRequestRequestTypeDef",
    {
        "Certificate": Union[bytes, IO[bytes], StreamingBody],
        "PrivateKey": Union[bytes, IO[bytes], StreamingBody],
        "CertificateArn": NotRequired[str],
        "CertificateChain": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "Name": NotRequired[KeyUsageNameType],
    },
)

ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "CertificateStatuses": NotRequired[Sequence[CertificateStatusType]],
        "Includes": NotRequired["FiltersTypeDef"],
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificateSummaryList": List["CertificateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForCertificateRequestRequestTypeDef = TypedDict(
    "ListTagsForCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

ListTagsForCertificateResponseTypeDef = TypedDict(
    "ListTagsForCertificateResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

PutAccountConfigurationRequestRequestTypeDef = TypedDict(
    "PutAccountConfigurationRequestRequestTypeDef",
    {
        "IdempotencyToken": str,
        "ExpiryEvents": NotRequired["ExpiryEventsConfigurationTypeDef"],
    },
)

RemoveTagsFromCertificateRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

RenewCertificateRequestRequestTypeDef = TypedDict(
    "RenewCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "RenewalStatus": RenewalStatusType,
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "UpdatedAt": datetime,
        "RenewalStatusReason": NotRequired[FailureReasonType],
    },
)

RequestCertificateRequestRequestTypeDef = TypedDict(
    "RequestCertificateRequestRequestTypeDef",
    {
        "DomainName": str,
        "ValidationMethod": NotRequired[ValidationMethodType],
        "SubjectAlternativeNames": NotRequired[Sequence[str]],
        "IdempotencyToken": NotRequired[str],
        "DomainValidationOptions": NotRequired[Sequence["DomainValidationOptionTypeDef"]],
        "Options": NotRequired["CertificateOptionsTypeDef"],
        "CertificateAuthorityArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

RequestCertificateResponseTypeDef = TypedDict(
    "RequestCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResendValidationEmailRequestRequestTypeDef = TypedDict(
    "ResendValidationEmailRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Domain": str,
        "ValidationDomain": str,
    },
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Name": str,
        "Type": Literal["CNAME"],
        "Value": str,
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
        "Value": NotRequired[str],
    },
)

UpdateCertificateOptionsRequestRequestTypeDef = TypedDict(
    "UpdateCertificateOptionsRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Options": "CertificateOptionsTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
