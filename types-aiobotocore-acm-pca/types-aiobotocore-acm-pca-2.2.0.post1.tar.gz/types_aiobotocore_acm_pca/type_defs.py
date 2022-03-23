"""
Type annotations for acm-pca service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_acm_pca/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_acm_pca.type_defs import ASN1SubjectTypeDef

    data: ASN1SubjectTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AccessMethodTypeType,
    ActionTypeType,
    AuditReportResponseFormatType,
    AuditReportStatusType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
    ExtendedKeyUsageTypeType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyStorageSecurityStandardType,
    ResourceOwnerType,
    RevocationReasonType,
    S3ObjectAclType,
    SigningAlgorithmType,
    ValidityPeriodTypeType,
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
    "ASN1SubjectTypeDef",
    "AccessDescriptionTypeDef",
    "AccessMethodTypeDef",
    "ApiPassthroughTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityRequestRequestTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "CreatePermissionRequestRequestTypeDef",
    "CrlConfigurationTypeDef",
    "CsrExtensionsTypeDef",
    "CustomAttributeTypeDef",
    "CustomExtensionTypeDef",
    "DeleteCertificateAuthorityRequestRequestTypeDef",
    "DeletePermissionRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "ExtensionsTypeDef",
    "GeneralNameTypeDef",
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateRequestRequestTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "ImportCertificateAuthorityCertificateRequestRequestTypeDef",
    "IssueCertificateRequestRequestTypeDef",
    "IssueCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "OcspConfigurationTypeDef",
    "OtherNameTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PolicyInformationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "PutPolicyRequestRequestTypeDef",
    "QualifierTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    "RevocationConfigurationTypeDef",
    "RevokeCertificateRequestRequestTypeDef",
    "TagCertificateAuthorityRequestRequestTypeDef",
    "TagTypeDef",
    "UntagCertificateAuthorityRequestRequestTypeDef",
    "UpdateCertificateAuthorityRequestRequestTypeDef",
    "ValidityTypeDef",
    "WaiterConfigTypeDef",
)

ASN1SubjectTypeDef = TypedDict(
    "ASN1SubjectTypeDef",
    {
        "Country": NotRequired[str],
        "Organization": NotRequired[str],
        "OrganizationalUnit": NotRequired[str],
        "DistinguishedNameQualifier": NotRequired[str],
        "State": NotRequired[str],
        "CommonName": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Locality": NotRequired[str],
        "Title": NotRequired[str],
        "Surname": NotRequired[str],
        "GivenName": NotRequired[str],
        "Initials": NotRequired[str],
        "Pseudonym": NotRequired[str],
        "GenerationQualifier": NotRequired[str],
        "CustomAttributes": NotRequired[Sequence["CustomAttributeTypeDef"]],
    },
)

AccessDescriptionTypeDef = TypedDict(
    "AccessDescriptionTypeDef",
    {
        "AccessMethod": "AccessMethodTypeDef",
        "AccessLocation": "GeneralNameTypeDef",
    },
)

AccessMethodTypeDef = TypedDict(
    "AccessMethodTypeDef",
    {
        "CustomObjectIdentifier": NotRequired[str],
        "AccessMethodType": NotRequired[AccessMethodTypeType],
    },
)

ApiPassthroughTypeDef = TypedDict(
    "ApiPassthroughTypeDef",
    {
        "Extensions": NotRequired["ExtensionsTypeDef"],
        "Subject": NotRequired["ASN1SubjectTypeDef"],
    },
)

CertificateAuthorityConfigurationTypeDef = TypedDict(
    "CertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": "ASN1SubjectTypeDef",
        "CsrExtensions": NotRequired["CsrExtensionsTypeDef"],
    },
)

CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": NotRequired[str],
        "OwnerAccount": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastStateChangeAt": NotRequired[datetime],
        "Type": NotRequired[CertificateAuthorityTypeType],
        "Serial": NotRequired[str],
        "Status": NotRequired[CertificateAuthorityStatusType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "FailureReason": NotRequired[FailureReasonType],
        "CertificateAuthorityConfiguration": NotRequired[
            "CertificateAuthorityConfigurationTypeDef"
        ],
        "RevocationConfiguration": NotRequired["RevocationConfigurationTypeDef"],
        "RestorableUntil": NotRequired[datetime],
        "KeyStorageSecurityStandard": NotRequired[KeyStorageSecurityStandardType],
    },
)

CreateCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "S3BucketName": str,
        "AuditReportResponseFormat": AuditReportResponseFormatType,
    },
)

CreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportId": str,
        "S3Key": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "CertificateAuthorityType": CertificateAuthorityTypeType,
        "RevocationConfiguration": NotRequired["RevocationConfigurationTypeDef"],
        "IdempotencyToken": NotRequired[str],
        "KeyStorageSecurityStandard": NotRequired[KeyStorageSecurityStandardType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePermissionRequestRequestTypeDef = TypedDict(
    "CreatePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "Actions": Sequence[ActionTypeType],
        "SourceAccount": NotRequired[str],
    },
)

CrlConfigurationTypeDef = TypedDict(
    "CrlConfigurationTypeDef",
    {
        "Enabled": bool,
        "ExpirationInDays": NotRequired[int],
        "CustomCname": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3ObjectAcl": NotRequired[S3ObjectAclType],
    },
)

CsrExtensionsTypeDef = TypedDict(
    "CsrExtensionsTypeDef",
    {
        "KeyUsage": NotRequired["KeyUsageTypeDef"],
        "SubjectInformationAccess": NotRequired[Sequence["AccessDescriptionTypeDef"]],
    },
)

CustomAttributeTypeDef = TypedDict(
    "CustomAttributeTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
    },
)

CustomExtensionTypeDef = TypedDict(
    "CustomExtensionTypeDef",
    {
        "ObjectIdentifier": str,
        "Value": str,
        "Critical": NotRequired[bool],
    },
)

DeleteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DeleteCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "PermanentDeletionTimeInDays": NotRequired[int],
    },
)

DeletePermissionRequestRequestTypeDef = TypedDict(
    "DeletePermissionRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "SourceAccount": NotRequired[str],
    },
)

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeCertificateAuthorityAuditReportRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
    },
)

DescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": AuditReportStatusType,
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

DescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityResponseTypeDef",
    {
        "CertificateAuthority": "CertificateAuthorityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdiPartyNameTypeDef = TypedDict(
    "EdiPartyNameTypeDef",
    {
        "PartyName": str,
        "NameAssigner": NotRequired[str],
    },
)

ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "ExtendedKeyUsageType": NotRequired[ExtendedKeyUsageTypeType],
        "ExtendedKeyUsageObjectIdentifier": NotRequired[str],
    },
)

ExtensionsTypeDef = TypedDict(
    "ExtensionsTypeDef",
    {
        "CertificatePolicies": NotRequired[Sequence["PolicyInformationTypeDef"]],
        "ExtendedKeyUsage": NotRequired[Sequence["ExtendedKeyUsageTypeDef"]],
        "KeyUsage": NotRequired["KeyUsageTypeDef"],
        "SubjectAlternativeNames": NotRequired[Sequence["GeneralNameTypeDef"]],
        "CustomExtensions": NotRequired[Sequence["CustomExtensionTypeDef"]],
    },
)

GeneralNameTypeDef = TypedDict(
    "GeneralNameTypeDef",
    {
        "OtherName": NotRequired["OtherNameTypeDef"],
        "Rfc822Name": NotRequired[str],
        "DnsName": NotRequired[str],
        "DirectoryName": NotRequired["ASN1SubjectTypeDef"],
        "EdiPartyName": NotRequired["EdiPartyNameTypeDef"],
        "UniformResourceIdentifier": NotRequired[str],
        "IpAddress": NotRequired[str],
        "RegisteredId": NotRequired[str],
    },
)

GetCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateAuthorityCsrRequestRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCsrRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCsrResponseTypeDef",
    {
        "Csr": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
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

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportCertificateAuthorityCertificateRequestRequestTypeDef = TypedDict(
    "ImportCertificateAuthorityCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Certificate": Union[bytes, IO[bytes], StreamingBody],
        "CertificateChain": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

IssueCertificateRequestRequestTypeDef = TypedDict(
    "IssueCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Csr": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmType,
        "Validity": "ValidityTypeDef",
        "ApiPassthrough": NotRequired["ApiPassthroughTypeDef"],
        "TemplateArn": NotRequired[str],
        "ValidityNotBefore": NotRequired["ValidityTypeDef"],
        "IdempotencyToken": NotRequired[str],
    },
)

IssueCertificateResponseTypeDef = TypedDict(
    "IssueCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "DigitalSignature": NotRequired[bool],
        "NonRepudiation": NotRequired[bool],
        "KeyEncipherment": NotRequired[bool],
        "DataEncipherment": NotRequired[bool],
        "KeyAgreement": NotRequired[bool],
        "KeyCertSign": NotRequired[bool],
        "CRLSign": NotRequired[bool],
        "EncipherOnly": NotRequired[bool],
        "DecipherOnly": NotRequired[bool],
    },
)

ListCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceOwner": NotRequired[ResourceOwnerType],
    },
)

ListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List["CertificateAuthorityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OcspConfigurationTypeDef = TypedDict(
    "OcspConfigurationTypeDef",
    {
        "Enabled": bool,
        "OcspCustomCname": NotRequired[str],
    },
)

OtherNameTypeDef = TypedDict(
    "OtherNameTypeDef",
    {
        "TypeId": str,
        "Value": str,
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "CertificateAuthorityArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Principal": NotRequired[str],
        "SourceAccount": NotRequired[str],
        "Actions": NotRequired[List[ActionTypeType]],
        "Policy": NotRequired[str],
    },
)

PolicyInformationTypeDef = TypedDict(
    "PolicyInformationTypeDef",
    {
        "CertPolicyId": str,
        "PolicyQualifiers": NotRequired[Sequence["PolicyQualifierInfoTypeDef"]],
    },
)

PolicyQualifierInfoTypeDef = TypedDict(
    "PolicyQualifierInfoTypeDef",
    {
        "PolicyQualifierId": Literal["CPS"],
        "Qualifier": "QualifierTypeDef",
    },
)

PutPolicyRequestRequestTypeDef = TypedDict(
    "PutPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

QualifierTypeDef = TypedDict(
    "QualifierTypeDef",
    {
        "CpsUri": str,
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

RestoreCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "RestoreCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

RevocationConfigurationTypeDef = TypedDict(
    "RevocationConfigurationTypeDef",
    {
        "CrlConfiguration": NotRequired["CrlConfigurationTypeDef"],
        "OcspConfiguration": NotRequired["OcspConfigurationTypeDef"],
    },
)

RevokeCertificateRequestRequestTypeDef = TypedDict(
    "RevokeCertificateRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateSerial": str,
        "RevocationReason": RevocationReasonType,
    },
)

TagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "TagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

UntagCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "UntagCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

UpdateCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "UpdateCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "RevocationConfiguration": NotRequired["RevocationConfigurationTypeDef"],
        "Status": NotRequired[CertificateAuthorityStatusType],
    },
)

ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {
        "Value": int,
        "Type": ValidityPeriodTypeType,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
