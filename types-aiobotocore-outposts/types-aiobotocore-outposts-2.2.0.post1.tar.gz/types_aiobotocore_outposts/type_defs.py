"""
Type annotations for outposts service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_outposts/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_outposts.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AddressTypeType,
    CatalogItemClassType,
    CatalogItemStatusType,
    FiberOpticCableTypeType,
    LineItemStatusType,
    MaximumSupportedWeightLbsType,
    OpticalStandardType,
    OrderStatusType,
    OrderTypeType,
    PaymentOptionType,
    PowerConnectorType,
    PowerDrawKvaType,
    PowerFeedDropType,
    PowerPhaseType,
    SupportedHardwareTypeType,
    SupportedStorageEnumType,
    UplinkCountType,
    UplinkGbpsType,
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
    "AddressTypeDef",
    "CancelOrderInputRequestTypeDef",
    "CatalogItemTypeDef",
    "CreateOrderInputRequestTypeDef",
    "CreateOrderOutputTypeDef",
    "CreateOutpostInputRequestTypeDef",
    "CreateOutpostOutputTypeDef",
    "CreateSiteInputRequestTypeDef",
    "CreateSiteOutputTypeDef",
    "DeleteOutpostInputRequestTypeDef",
    "DeleteSiteInputRequestTypeDef",
    "EC2CapacityTypeDef",
    "GetCatalogItemInputRequestTypeDef",
    "GetCatalogItemOutputTypeDef",
    "GetOrderInputRequestTypeDef",
    "GetOrderOutputTypeDef",
    "GetOutpostInputRequestTypeDef",
    "GetOutpostInstanceTypesInputRequestTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "GetSiteAddressInputRequestTypeDef",
    "GetSiteAddressOutputTypeDef",
    "GetSiteInputRequestTypeDef",
    "GetSiteOutputTypeDef",
    "InstanceTypeItemTypeDef",
    "LineItemRequestTypeDef",
    "LineItemTypeDef",
    "ListCatalogItemsInputRequestTypeDef",
    "ListCatalogItemsOutputTypeDef",
    "ListOrdersInputRequestTypeDef",
    "ListOrdersOutputTypeDef",
    "ListOutpostsInputRequestTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesInputRequestTypeDef",
    "ListSitesOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OrderSummaryTypeDef",
    "OrderTypeDef",
    "OutpostTypeDef",
    "RackPhysicalPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "SiteTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOutpostInputRequestTypeDef",
    "UpdateOutpostOutputTypeDef",
    "UpdateSiteAddressInputRequestTypeDef",
    "UpdateSiteAddressOutputTypeDef",
    "UpdateSiteInputRequestTypeDef",
    "UpdateSiteOutputTypeDef",
    "UpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "StateOrRegion": str,
        "PostalCode": str,
        "CountryCode": str,
        "ContactName": NotRequired[str],
        "ContactPhoneNumber": NotRequired[str],
        "AddressLine2": NotRequired[str],
        "AddressLine3": NotRequired[str],
        "DistrictOrCounty": NotRequired[str],
        "Municipality": NotRequired[str],
    },
)

CancelOrderInputRequestTypeDef = TypedDict(
    "CancelOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)

CatalogItemTypeDef = TypedDict(
    "CatalogItemTypeDef",
    {
        "CatalogItemId": NotRequired[str],
        "ItemStatus": NotRequired[CatalogItemStatusType],
        "EC2Capacities": NotRequired[List["EC2CapacityTypeDef"]],
        "PowerKva": NotRequired[float],
        "WeightLbs": NotRequired[int],
        "SupportedUplinkGbps": NotRequired[List[int]],
        "SupportedStorage": NotRequired[List[SupportedStorageEnumType]],
    },
)

CreateOrderInputRequestTypeDef = TypedDict(
    "CreateOrderInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "LineItems": Sequence["LineItemRequestTypeDef"],
        "PaymentOption": PaymentOptionType,
        "PaymentTerm": NotRequired[Literal["THREE_YEARS"]],
    },
)

CreateOrderOutputTypeDef = TypedDict(
    "CreateOrderOutputTypeDef",
    {
        "Order": "OrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOutpostInputRequestTypeDef = TypedDict(
    "CreateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "SiteId": str,
        "Description": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "SupportedHardwareType": NotRequired[SupportedHardwareTypeType],
    },
)

CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSiteInputRequestTypeDef = TypedDict(
    "CreateSiteInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Notes": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "OperatingAddress": NotRequired["AddressTypeDef"],
        "ShippingAddress": NotRequired["AddressTypeDef"],
        "RackPhysicalProperties": NotRequired["RackPhysicalPropertiesTypeDef"],
    },
)

CreateSiteOutputTypeDef = TypedDict(
    "CreateSiteOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutpostInputRequestTypeDef = TypedDict(
    "DeleteOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

DeleteSiteInputRequestTypeDef = TypedDict(
    "DeleteSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

EC2CapacityTypeDef = TypedDict(
    "EC2CapacityTypeDef",
    {
        "Family": NotRequired[str],
        "MaxSize": NotRequired[str],
        "Quantity": NotRequired[str],
    },
)

GetCatalogItemInputRequestTypeDef = TypedDict(
    "GetCatalogItemInputRequestTypeDef",
    {
        "CatalogItemId": str,
    },
)

GetCatalogItemOutputTypeDef = TypedDict(
    "GetCatalogItemOutputTypeDef",
    {
        "CatalogItem": "CatalogItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrderInputRequestTypeDef = TypedDict(
    "GetOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)

GetOrderOutputTypeDef = TypedDict(
    "GetOrderOutputTypeDef",
    {
        "Order": "OrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutpostInputRequestTypeDef = TypedDict(
    "GetOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

GetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "GetOutpostInstanceTypesInputRequestTypeDef",
    {
        "OutpostId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteAddressInputRequestTypeDef = TypedDict(
    "GetSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
    },
)

GetSiteAddressOutputTypeDef = TypedDict(
    "GetSiteAddressOutputTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteInputRequestTypeDef = TypedDict(
    "GetSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

GetSiteOutputTypeDef = TypedDict(
    "GetSiteOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeItemTypeDef = TypedDict(
    "InstanceTypeItemTypeDef",
    {
        "InstanceType": NotRequired[str],
    },
)

LineItemRequestTypeDef = TypedDict(
    "LineItemRequestTypeDef",
    {
        "CatalogItemId": NotRequired[str],
        "Quantity": NotRequired[int],
    },
)

LineItemTypeDef = TypedDict(
    "LineItemTypeDef",
    {
        "CatalogItemId": NotRequired[str],
        "LineItemId": NotRequired[str],
        "Quantity": NotRequired[int],
        "Status": NotRequired[LineItemStatusType],
    },
)

ListCatalogItemsInputRequestTypeDef = TypedDict(
    "ListCatalogItemsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ItemClassFilter": NotRequired[Sequence[CatalogItemClassType]],
        "SupportedStorageFilter": NotRequired[Sequence[SupportedStorageEnumType]],
        "EC2FamilyFilter": NotRequired[Sequence[str]],
    },
)

ListCatalogItemsOutputTypeDef = TypedDict(
    "ListCatalogItemsOutputTypeDef",
    {
        "CatalogItems": List["CatalogItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrdersInputRequestTypeDef = TypedDict(
    "ListOrdersInputRequestTypeDef",
    {
        "OutpostIdentifierFilter": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListOrdersOutputTypeDef = TypedDict(
    "ListOrdersOutputTypeDef",
    {
        "Orders": List["OrderSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutpostsInputRequestTypeDef = TypedDict(
    "ListOutpostsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "LifeCycleStatusFilter": NotRequired[Sequence[str]],
        "AvailabilityZoneFilter": NotRequired[Sequence[str]],
        "AvailabilityZoneIdFilter": NotRequired[Sequence[str]],
    },
)

ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef",
    {
        "Outposts": List["OutpostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSitesInputRequestTypeDef = TypedDict(
    "ListSitesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "OperatingAddressCountryCodeFilter": NotRequired[Sequence[str]],
        "OperatingAddressStateOrRegionFilter": NotRequired[Sequence[str]],
        "OperatingAddressCityFilter": NotRequired[Sequence[str]],
    },
)

ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef",
    {
        "Sites": List["SiteTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderSummaryTypeDef = TypedDict(
    "OrderSummaryTypeDef",
    {
        "OutpostId": NotRequired[str],
        "OrderId": NotRequired[str],
        "OrderType": NotRequired[OrderTypeType],
        "Status": NotRequired[OrderStatusType],
        "LineItemCountsByStatus": NotRequired[Dict[LineItemStatusType, int]],
        "OrderSubmissionDate": NotRequired[datetime],
        "OrderFulfilledDate": NotRequired[datetime],
    },
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "OutpostId": NotRequired[str],
        "OrderId": NotRequired[str],
        "Status": NotRequired[OrderStatusType],
        "LineItems": NotRequired[List["LineItemTypeDef"]],
        "PaymentOption": NotRequired[PaymentOptionType],
        "OrderSubmissionDate": NotRequired[datetime],
        "OrderFulfilledDate": NotRequired[datetime],
    },
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "SiteId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LifeCycleStatus": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "SiteArn": NotRequired[str],
        "SupportedHardwareType": NotRequired[SupportedHardwareTypeType],
    },
)

RackPhysicalPropertiesTypeDef = TypedDict(
    "RackPhysicalPropertiesTypeDef",
    {
        "PowerDrawKva": NotRequired[PowerDrawKvaType],
        "PowerPhase": NotRequired[PowerPhaseType],
        "PowerConnector": NotRequired[PowerConnectorType],
        "PowerFeedDrop": NotRequired[PowerFeedDropType],
        "UplinkGbps": NotRequired[UplinkGbpsType],
        "UplinkCount": NotRequired[UplinkCountType],
        "FiberOpticCableType": NotRequired[FiberOpticCableTypeType],
        "OpticalStandard": NotRequired[OpticalStandardType],
        "MaximumSupportedWeightLbs": NotRequired[MaximumSupportedWeightLbsType],
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

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": NotRequired[str],
        "AccountId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "SiteArn": NotRequired[str],
        "Notes": NotRequired[str],
        "OperatingAddressCountryCode": NotRequired[str],
        "OperatingAddressStateOrRegion": NotRequired[str],
        "OperatingAddressCity": NotRequired[str],
        "RackPhysicalProperties": NotRequired["RackPhysicalPropertiesTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateOutpostInputRequestTypeDef = TypedDict(
    "UpdateOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SupportedHardwareType": NotRequired[SupportedHardwareTypeType],
    },
)

UpdateOutpostOutputTypeDef = TypedDict(
    "UpdateOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSiteAddressInputRequestTypeDef = TypedDict(
    "UpdateSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": "AddressTypeDef",
    },
)

UpdateSiteAddressOutputTypeDef = TypedDict(
    "UpdateSiteAddressOutputTypeDef",
    {
        "AddressType": AddressTypeType,
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSiteInputRequestTypeDef = TypedDict(
    "UpdateSiteInputRequestTypeDef",
    {
        "SiteId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Notes": NotRequired[str],
    },
)

UpdateSiteOutputTypeDef = TypedDict(
    "UpdateSiteOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSiteRackPhysicalPropertiesInputRequestTypeDef = TypedDict(
    "UpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    {
        "SiteId": str,
        "PowerDrawKva": NotRequired[PowerDrawKvaType],
        "PowerPhase": NotRequired[PowerPhaseType],
        "PowerConnector": NotRequired[PowerConnectorType],
        "PowerFeedDrop": NotRequired[PowerFeedDropType],
        "UplinkGbps": NotRequired[UplinkGbpsType],
        "UplinkCount": NotRequired[UplinkCountType],
        "FiberOpticCableType": NotRequired[FiberOpticCableTypeType],
        "OpticalStandard": NotRequired[OpticalStandardType],
        "MaximumSupportedWeightLbs": NotRequired[MaximumSupportedWeightLbsType],
    },
)

UpdateSiteRackPhysicalPropertiesOutputTypeDef = TypedDict(
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
