"""
Type annotations for license-manager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantRequestRequestTypeDef

    data: AcceptGrantRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AllowedOperationType,
    CheckoutTypeType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
    LicenseConfigurationStatusType,
    LicenseConversionTaskStatusType,
    LicenseCountingTypeType,
    LicenseDeletionStatusType,
    LicenseStatusType,
    ReceivedStatusType,
    RenewTypeType,
    ReportFrequencyTypeType,
    ReportTypeType,
    ResourceTypeType,
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
    "AcceptGrantRequestRequestTypeDef",
    "AcceptGrantResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckInLicenseRequestRequestTypeDef",
    "CheckoutBorrowLicenseRequestRequestTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseRequestRequestTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionRequestRequestTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationRequestRequestTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseConversionTaskForResourceRequestRequestTypeDef",
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    "CreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    "CreateLicenseRequestRequestTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionRequestRequestTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "DatetimeRangeTypeDef",
    "DeleteGrantRequestRequestTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    "DeleteLicenseRequestRequestTypeDef",
    "DeleteLicenseResponseTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionRequestRequestTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenRequestRequestTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantRequestRequestTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseConfigurationRequestRequestTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseConversionTaskRequestRequestTypeDef",
    "GetLicenseConversionTaskResponseTypeDef",
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    "GetLicenseRequestRequestTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageRequestRequestTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "InventoryFilterTypeDef",
    "IssuerDetailsTypeDef",
    "IssuerTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseConversionContextTypeDef",
    "LicenseConversionTaskTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListDistributedGrantsRequestRequestTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseConfigurationsRequestRequestTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseConversionTasksRequestRequestTypeDef",
    "ListLicenseConversionTasksResponseTypeDef",
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    "ListLicenseSpecificationsForResourceRequestRequestTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListLicenseVersionsRequestRequestTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesRequestRequestTypeDef",
    "ListLicensesResponseTypeDef",
    "ListReceivedGrantsRequestRequestTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListReceivedLicensesRequestRequestTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "ListResourceInventoryRequestRequestTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTokensRequestRequestTypeDef",
    "ListTokensResponseTypeDef",
    "ListUsageForLicenseConfigurationRequestRequestTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "RejectGrantRequestRequestTypeDef",
    "RejectGrantResponseTypeDef",
    "ReportContextTypeDef",
    "ReportFrequencyTypeDef",
    "ReportGeneratorTypeDef",
    "ResourceInventoryTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLicenseConfigurationRequestRequestTypeDef",
    "UpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "UpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
)

AcceptGrantRequestRequestTypeDef = TypedDict(
    "AcceptGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)

AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef",
    {
        "LastRunTime": NotRequired[datetime],
    },
)

BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef",
    {
        "AllowEarlyCheckIn": bool,
        "MaxTimeToLiveInMinutes": int,
    },
)

CheckInLicenseRequestRequestTypeDef = TypedDict(
    "CheckInLicenseRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Beneficiary": NotRequired[str],
    },
)

CheckoutBorrowLicenseRequestRequestTypeDef = TypedDict(
    "CheckoutBorrowLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Entitlements": Sequence["EntitlementDataTypeDef"],
        "DigitalSignatureMethod": Literal["JWT_PS384"],
        "ClientToken": str,
        "NodeId": NotRequired[str],
        "CheckoutMetadata": NotRequired[Sequence["MetadataTypeDef"]],
    },
)

CheckoutBorrowLicenseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CheckoutLicenseRequestRequestTypeDef = TypedDict(
    "CheckoutLicenseRequestRequestTypeDef",
    {
        "ProductSKU": str,
        "CheckoutType": CheckoutTypeType,
        "KeyFingerprint": str,
        "Entitlements": Sequence["EntitlementDataTypeDef"],
        "ClientToken": str,
        "Beneficiary": NotRequired[str],
        "NodeId": NotRequired[str],
    },
)

CheckoutLicenseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseTypeDef",
    {
        "CheckoutType": CheckoutTypeType,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
        "LicenseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "ConsumedLicenses": NotRequired[int],
    },
)

ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": NotRequired[RenewTypeType],
        "ProvisionalConfiguration": NotRequired["ProvisionalConfigurationTypeDef"],
        "BorrowConfiguration": NotRequired["BorrowConfigurationTypeDef"],
    },
)

CreateGrantRequestRequestTypeDef = TypedDict(
    "CreateGrantRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantName": str,
        "LicenseArn": str,
        "Principals": Sequence[str],
        "HomeRegion": str,
        "AllowedOperations": Sequence[AllowedOperationType],
    },
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGrantVersionRequestRequestTypeDef = TypedDict(
    "CreateGrantVersionRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantArn": str,
        "GrantName": NotRequired[str],
        "AllowedOperations": NotRequired[Sequence[AllowedOperationType]],
        "Status": NotRequired[GrantStatusType],
        "StatusReason": NotRequired[str],
        "SourceVersion": NotRequired[str],
    },
)

CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "CreateLicenseConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "Description": NotRequired[str],
        "LicenseCount": NotRequired[int],
        "LicenseCountHardLimit": NotRequired[bool],
        "LicenseRules": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DisassociateWhenNotFound": NotRequired[bool],
        "ProductInformationList": NotRequired[Sequence["ProductInformationTypeDef"]],
    },
)

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLicenseConversionTaskForResourceRequestRequestTypeDef = TypedDict(
    "CreateLicenseConversionTaskForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "SourceLicenseContext": "LicenseConversionContextTypeDef",
        "DestinationLicenseContext": "LicenseConversionContextTypeDef",
    },
)

CreateLicenseConversionTaskForResourceResponseTypeDef = TypedDict(
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "ClientToken": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLicenseRequestRequestTypeDef = TypedDict(
    "CreateLicenseRequestRequestTypeDef",
    {
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerTypeDef",
        "HomeRegion": str,
        "Validity": "DatetimeRangeTypeDef",
        "Entitlements": Sequence["EntitlementTypeDef"],
        "Beneficiary": str,
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "ClientToken": str,
        "LicenseMetadata": NotRequired[Sequence["MetadataTypeDef"]],
    },
)

CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": LicenseStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLicenseVersionRequestRequestTypeDef = TypedDict(
    "CreateLicenseVersionRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "Issuer": "IssuerTypeDef",
        "HomeRegion": str,
        "Validity": "DatetimeRangeTypeDef",
        "Entitlements": Sequence["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "Status": LicenseStatusType,
        "ClientToken": str,
        "LicenseMetadata": NotRequired[Sequence["MetadataTypeDef"]],
        "SourceVersion": NotRequired[str],
    },
)

CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": LicenseStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "ClientToken": str,
        "RoleArns": NotRequired[Sequence[str]],
        "ExpirationInDays": NotRequired[int],
        "TokenProperties": NotRequired[Sequence[str]],
    },
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "TokenId": str,
        "TokenType": Literal["REFRESH_TOKEN"],
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatetimeRangeTypeDef = TypedDict(
    "DatetimeRangeTypeDef",
    {
        "Begin": str,
        "End": NotRequired[str],
    },
)

DeleteGrantRequestRequestTypeDef = TypedDict(
    "DeleteGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
        "Version": str,
        "StatusReason": NotRequired[str],
    },
)

DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

DeleteLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

DeleteLicenseRequestRequestTypeDef = TypedDict(
    "DeleteLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "SourceVersion": str,
    },
)

DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {
        "Status": LicenseDeletionStatusType,
        "DeletionDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "TokenId": str,
    },
)

EntitlementDataTypeDef = TypedDict(
    "EntitlementDataTypeDef",
    {
        "Name": str,
        "Unit": EntitlementDataUnitType,
        "Value": NotRequired[str],
    },
)

EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "Name": str,
        "Unit": EntitlementUnitType,
        "Value": NotRequired[str],
        "MaxCount": NotRequired[int],
        "Overage": NotRequired[bool],
        "AllowCheckIn": NotRequired[bool],
    },
)

EntitlementUsageTypeDef = TypedDict(
    "EntitlementUsageTypeDef",
    {
        "Name": str,
        "ConsumedValue": str,
        "Unit": EntitlementDataUnitType,
        "MaxCount": NotRequired[str],
    },
)

ExtendLicenseConsumptionRequestRequestTypeDef = TypedDict(
    "ExtendLicenseConsumptionRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
        "DryRun": NotRequired[bool],
    },
)

ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Expiration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

GetAccessTokenRequestRequestTypeDef = TypedDict(
    "GetAccessTokenRequestRequestTypeDef",
    {
        "Token": str,
        "TokenProperties": NotRequired[Sequence[str]],
    },
)

GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef",
    {
        "AccessToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGrantRequestRequestTypeDef = TypedDict(
    "GetGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
        "Version": NotRequired[str],
    },
)

GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef",
    {
        "Grant": "GrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "GetLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
        "DisassociateWhenNotFound": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseConversionTaskRequestRequestTypeDef = TypedDict(
    "GetLicenseConversionTaskRequestRequestTypeDef",
    {
        "LicenseConversionTaskId": str,
    },
)

GetLicenseConversionTaskResponseTypeDef = TypedDict(
    "GetLicenseConversionTaskResponseTypeDef",
    {
        "LicenseConversionTaskId": str,
        "ResourceArn": str,
        "SourceLicenseContext": "LicenseConversionContextTypeDef",
        "DestinationLicenseContext": "LicenseConversionContextTypeDef",
        "StatusMessage": str,
        "Status": LicenseConversionTaskStatusType,
        "StartTime": datetime,
        "LicenseConversionTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

GetLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    {
        "ReportGenerator": "ReportGeneratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseRequestRequestTypeDef = TypedDict(
    "GetLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Version": NotRequired[str],
    },
)

GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef",
    {
        "License": "LicenseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseUsageRequestRequestTypeDef = TypedDict(
    "GetLicenseUsageRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)

GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef",
    {
        "LicenseUsage": "LicenseUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": GrantStatusType,
        "Version": str,
        "GrantedOperations": List[AllowedOperationType],
        "StatusReason": NotRequired[str],
    },
)

GrantedLicenseTypeDef = TypedDict(
    "GrantedLicenseTypeDef",
    {
        "LicenseArn": NotRequired[str],
        "LicenseName": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProductSKU": NotRequired[str],
        "Issuer": NotRequired["IssuerDetailsTypeDef"],
        "HomeRegion": NotRequired[str],
        "Status": NotRequired[LicenseStatusType],
        "Validity": NotRequired["DatetimeRangeTypeDef"],
        "Beneficiary": NotRequired[str],
        "Entitlements": NotRequired[List["EntitlementTypeDef"]],
        "ConsumptionConfiguration": NotRequired["ConsumptionConfigurationTypeDef"],
        "LicenseMetadata": NotRequired[List["MetadataTypeDef"]],
        "CreateTime": NotRequired[str],
        "Version": NotRequired[str],
        "ReceivedMetadata": NotRequired["ReceivedMetadataTypeDef"],
    },
)

InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Name": str,
        "Condition": InventoryFilterConditionType,
        "Value": NotRequired[str],
    },
)

IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "SignKey": NotRequired[str],
        "KeyFingerprint": NotRequired[str],
    },
)

IssuerTypeDef = TypedDict(
    "IssuerTypeDef",
    {
        "Name": str,
        "SignKey": NotRequired[str],
    },
)

LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceOwnerId": NotRequired[str],
        "AssociationTime": NotRequired[datetime],
        "AmiAssociationScope": NotRequired[str],
    },
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": NotRequired[str],
        "LicenseConfigurationArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LicenseCountingType": NotRequired[LicenseCountingTypeType],
        "LicenseRules": NotRequired[List[str]],
        "LicenseCount": NotRequired[int],
        "LicenseCountHardLimit": NotRequired[bool],
        "DisassociateWhenNotFound": NotRequired[bool],
        "ConsumedLicenses": NotRequired[int],
        "Status": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "ConsumedLicenseSummaryList": NotRequired[List["ConsumedLicenseSummaryTypeDef"]],
        "ManagedResourceSummaryList": NotRequired[List["ManagedResourceSummaryTypeDef"]],
        "ProductInformationList": NotRequired[List["ProductInformationTypeDef"]],
        "AutomatedDiscoveryInformation": NotRequired["AutomatedDiscoveryInformationTypeDef"],
    },
)

LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceStatus": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "AssociationTime": NotRequired[datetime],
        "ConsumedLicenses": NotRequired[int],
    },
)

LicenseConversionContextTypeDef = TypedDict(
    "LicenseConversionContextTypeDef",
    {
        "UsageOperation": NotRequired[str],
    },
)

LicenseConversionTaskTypeDef = TypedDict(
    "LicenseConversionTaskTypeDef",
    {
        "LicenseConversionTaskId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "SourceLicenseContext": NotRequired["LicenseConversionContextTypeDef"],
        "DestinationLicenseContext": NotRequired["LicenseConversionContextTypeDef"],
        "Status": NotRequired[LicenseConversionTaskStatusType],
        "StatusMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "LicenseConversionTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

LicenseOperationFailureTypeDef = TypedDict(
    "LicenseOperationFailureTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ErrorMessage": NotRequired[str],
        "FailureTime": NotRequired[datetime],
        "OperationName": NotRequired[str],
        "ResourceOwnerId": NotRequired[str],
        "OperationRequestedBy": NotRequired[str],
        "MetadataList": NotRequired[List["MetadataTypeDef"]],
    },
)

LicenseSpecificationTypeDef = TypedDict(
    "LicenseSpecificationTypeDef",
    {
        "LicenseConfigurationArn": str,
        "AmiAssociationScope": NotRequired[str],
    },
)

LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "LicenseArn": NotRequired[str],
        "LicenseName": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProductSKU": NotRequired[str],
        "Issuer": NotRequired["IssuerDetailsTypeDef"],
        "HomeRegion": NotRequired[str],
        "Status": NotRequired[LicenseStatusType],
        "Validity": NotRequired["DatetimeRangeTypeDef"],
        "Beneficiary": NotRequired[str],
        "Entitlements": NotRequired[List["EntitlementTypeDef"]],
        "ConsumptionConfiguration": NotRequired["ConsumptionConfigurationTypeDef"],
        "LicenseMetadata": NotRequired[List["MetadataTypeDef"]],
        "CreateTime": NotRequired[str],
        "Version": NotRequired[str],
    },
)

LicenseUsageTypeDef = TypedDict(
    "LicenseUsageTypeDef",
    {
        "EntitlementUsages": NotRequired[List["EntitlementUsageTypeDef"]],
    },
)

ListAssociationsForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributedGrantsRequestRequestTypeDef = TypedDict(
    "ListDistributedGrantsRequestRequestTypeDef",
    {
        "GrantArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List["LicenseOperationFailureTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List["LicenseConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseConversionTasksRequestRequestTypeDef = TypedDict(
    "ListLicenseConversionTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListLicenseConversionTasksResponseTypeDef = TypedDict(
    "ListLicenseConversionTasksResponseTypeDef",
    {
        "LicenseConversionTasks": List["LicenseConversionTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseManagerReportGeneratorsRequestRequestTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLicenseManagerReportGeneratorsResponseTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    {
        "ReportGenerators": List["ReportGeneratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List["LicenseSpecificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseVersionsRequestRequestTypeDef = TypedDict(
    "ListLicenseVersionsRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicensesRequestRequestTypeDef = TypedDict(
    "ListLicensesRequestRequestTypeDef",
    {
        "LicenseArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedGrantsRequestRequestTypeDef = TypedDict(
    "ListReceivedGrantsRequestRequestTypeDef",
    {
        "GrantArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedLicensesRequestRequestTypeDef = TypedDict(
    "ListReceivedLicensesRequestRequestTypeDef",
    {
        "LicenseArns": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {
        "Licenses": List["GrantedLicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceInventoryRequestRequestTypeDef = TypedDict(
    "ListResourceInventoryRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["InventoryFilterTypeDef"]],
    },
)

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List["ResourceInventoryTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTokensRequestRequestTypeDef = TypedDict(
    "ListTokensRequestRequestTypeDef",
    {
        "TokenIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef",
    {
        "Tokens": List["TokenDataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsageForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
    },
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "AssociationCount": NotRequired[int],
    },
)

MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "EnableIntegration": bool,
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

ProductInformationFilterTypeDef = TypedDict(
    "ProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
        "ProductInformationFilterValue": NotRequired[Sequence[str]],
    },
)

ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": Sequence["ProductInformationFilterTypeDef"],
    },
)

ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef",
    {
        "MaxTimeToLiveInMinutes": int,
    },
)

ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {
        "ReceivedStatus": NotRequired[ReceivedStatusType],
        "ReceivedStatusReason": NotRequired[str],
        "AllowedOperations": NotRequired[List[AllowedOperationType]],
    },
)

RejectGrantRequestRequestTypeDef = TypedDict(
    "RejectGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)

RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportContextTypeDef = TypedDict(
    "ReportContextTypeDef",
    {
        "licenseConfigurationArns": Sequence[str],
    },
)

ReportFrequencyTypeDef = TypedDict(
    "ReportFrequencyTypeDef",
    {
        "value": NotRequired[int],
        "period": NotRequired[ReportFrequencyTypeType],
    },
)

ReportGeneratorTypeDef = TypedDict(
    "ReportGeneratorTypeDef",
    {
        "ReportGeneratorName": NotRequired[str],
        "ReportType": NotRequired[List[ReportTypeType]],
        "ReportContext": NotRequired["ReportContextTypeDef"],
        "ReportFrequency": NotRequired["ReportFrequencyTypeDef"],
        "LicenseManagerReportGeneratorArn": NotRequired[str],
        "LastRunStatus": NotRequired[str],
        "LastRunFailureReason": NotRequired[str],
        "LastReportGenerationTime": NotRequired[str],
        "ReportCreatorAccount": NotRequired[str],
        "Description": NotRequired[str],
        "S3Location": NotRequired["S3LocationTypeDef"],
        "CreateTime": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceArn": NotRequired[str],
        "Platform": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "ResourceOwningAccountId": NotRequired[str],
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
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TokenDataTypeDef = TypedDict(
    "TokenDataTypeDef",
    {
        "TokenId": NotRequired[str],
        "TokenType": NotRequired[str],
        "LicenseArn": NotRequired[str],
        "ExpirationTime": NotRequired[str],
        "TokenProperties": NotRequired[List[str]],
        "RoleArns": NotRequired[List[str]],
        "Status": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
        "LicenseConfigurationStatus": NotRequired[LicenseConfigurationStatusType],
        "LicenseRules": NotRequired[Sequence[str]],
        "LicenseCount": NotRequired[int],
        "LicenseCountHardLimit": NotRequired[bool],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ProductInformationList": NotRequired[Sequence["ProductInformationTypeDef"]],
        "DisassociateWhenNotFound": NotRequired[bool],
    },
)

UpdateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "UpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "ClientToken": str,
        "Description": NotRequired[str],
    },
)

UpdateLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "UpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "AddLicenseSpecifications": NotRequired[Sequence["LicenseSpecificationTypeDef"]],
        "RemoveLicenseSpecifications": NotRequired[Sequence["LicenseSpecificationTypeDef"]],
    },
)

UpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingsRequestRequestTypeDef",
    {
        "S3BucketArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "OrganizationConfiguration": NotRequired["OrganizationConfigurationTypeDef"],
        "EnableCrossAccountsDiscovery": NotRequired[bool],
    },
)
