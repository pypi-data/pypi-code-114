"""
Type annotations for servicediscovery service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_servicediscovery/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_servicediscovery.type_defs import CreateHttpNamespaceRequestRequestTypeDef

    data: CreateHttpNamespaceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    CustomHealthStatusType,
    FilterConditionType,
    HealthCheckTypeType,
    HealthStatusFilterType,
    HealthStatusType,
    NamespaceTypeType,
    OperationFilterNameType,
    OperationStatusType,
    OperationTargetTypeType,
    OperationTypeType,
    RecordTypeType,
    RoutingPolicyType,
    ServiceTypeType,
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
    "CreateHttpNamespaceRequestRequestTypeDef",
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceRequestRequestTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceRequestRequestTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeregisterInstanceRequestRequestTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesRequestRequestTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "GetInstanceRequestRequestTypeDef",
    "GetInstanceResponseTypeDef",
    "GetInstancesHealthStatusRequestRequestTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "GetNamespaceRequestRequestTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetOperationRequestRequestTypeDef",
    "GetOperationResponseTypeDef",
    "GetServiceRequestRequestTypeDef",
    "GetServiceResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpNamespaceChangeTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NamespaceFilterTypeDef",
    "NamespacePropertiesTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "OperationFilterTypeDef",
    "OperationSummaryTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateDnsNamespaceChangeTypeDef",
    "PrivateDnsNamespacePropertiesChangeTypeDef",
    "PrivateDnsNamespacePropertiesTypeDef",
    "PrivateDnsPropertiesMutableChangeTypeDef",
    "PrivateDnsPropertiesMutableTypeDef",
    "PublicDnsNamespaceChangeTypeDef",
    "PublicDnsNamespacePropertiesChangeTypeDef",
    "PublicDnsNamespacePropertiesTypeDef",
    "PublicDnsPropertiesMutableChangeTypeDef",
    "PublicDnsPropertiesMutableTypeDef",
    "RegisterInstanceRequestRequestTypeDef",
    "RegisterInstanceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SOAChangeTypeDef",
    "SOATypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateHttpNamespaceRequestRequestTypeDef",
    "UpdateHttpNamespaceResponseTypeDef",
    "UpdateInstanceCustomHealthStatusRequestRequestTypeDef",
    "UpdatePrivateDnsNamespaceRequestRequestTypeDef",
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    "UpdatePublicDnsNamespaceRequestRequestTypeDef",
    "UpdatePublicDnsNamespaceResponseTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
)

CreateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "CreateHttpNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateHttpNamespaceResponseTypeDef = TypedDict(
    "CreateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "Vpc": str,
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Properties": NotRequired["PrivateDnsNamespacePropertiesTypeDef"],
    },
)

CreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "CreatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Properties": NotRequired["PublicDnsNamespacePropertiesTypeDef"],
    },
)

CreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "Name": str,
        "NamespaceId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "DnsConfig": NotRequired["DnsConfigTypeDef"],
        "HealthCheckConfig": NotRequired["HealthCheckConfigTypeDef"],
        "HealthCheckCustomConfig": NotRequired["HealthCheckCustomConfigTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Type": NotRequired[Literal["HTTP"]],
    },
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeregisterInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)

DeregisterInstanceResponseTypeDef = TypedDict(
    "DeregisterInstanceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscoverInstancesRequestRequestTypeDef = TypedDict(
    "DiscoverInstancesRequestRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
        "MaxResults": NotRequired[int],
        "QueryParameters": NotRequired[Mapping[str, str]],
        "OptionalParameters": NotRequired[Mapping[str, str]],
        "HealthStatus": NotRequired[HealthStatusFilterType],
    },
)

DiscoverInstancesResponseTypeDef = TypedDict(
    "DiscoverInstancesResponseTypeDef",
    {
        "Instances": List["HttpInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsConfigChangeTypeDef = TypedDict(
    "DnsConfigChangeTypeDef",
    {
        "DnsRecords": Sequence["DnsRecordTypeDef"],
    },
)

DnsConfigTypeDef = TypedDict(
    "DnsConfigTypeDef",
    {
        "DnsRecords": Sequence["DnsRecordTypeDef"],
        "NamespaceId": NotRequired[str],
        "RoutingPolicy": NotRequired[RoutingPolicyType],
    },
)

DnsPropertiesTypeDef = TypedDict(
    "DnsPropertiesTypeDef",
    {
        "HostedZoneId": NotRequired[str],
        "SOA": NotRequired["SOATypeDef"],
    },
)

DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": RecordTypeType,
        "TTL": int,
    },
)

GetInstanceRequestRequestTypeDef = TypedDict(
    "GetInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)

GetInstanceResponseTypeDef = TypedDict(
    "GetInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancesHealthStatusRequestRequestTypeDef = TypedDict(
    "GetInstancesHealthStatusRequestRequestTypeDef",
    {
        "ServiceId": str,
        "Instances": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetInstancesHealthStatusResponseTypeDef = TypedDict(
    "GetInstancesHealthStatusResponseTypeDef",
    {
        "Status": Dict[str, HealthStatusType],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamespaceRequestRequestTypeDef = TypedDict(
    "GetNamespaceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef",
    {
        "Namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationRequestRequestTypeDef = TypedDict(
    "GetOperationRequestRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationResponseTypeDef = TypedDict(
    "GetOperationResponseTypeDef",
    {
        "Operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
        "ResourcePath": NotRequired[str],
        "FailureThreshold": NotRequired[int],
    },
)

HealthCheckCustomConfigTypeDef = TypedDict(
    "HealthCheckCustomConfigTypeDef",
    {
        "FailureThreshold": NotRequired[int],
    },
)

HttpInstanceSummaryTypeDef = TypedDict(
    "HttpInstanceSummaryTypeDef",
    {
        "InstanceId": NotRequired[str],
        "NamespaceName": NotRequired[str],
        "ServiceName": NotRequired[str],
        "HealthStatus": NotRequired[HealthStatusType],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

HttpNamespaceChangeTypeDef = TypedDict(
    "HttpNamespaceChangeTypeDef",
    {
        "Description": str,
    },
)

HttpPropertiesTypeDef = TypedDict(
    "HttpPropertiesTypeDef",
    {
        "HttpName": NotRequired[str],
    },
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "CreatorRequestId": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "ServiceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["NamespaceFilterTypeDef"]],
    },
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List["NamespaceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["OperationFilterTypeDef"]],
    },
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["ServiceFilterTypeDef"]],
    },
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "Services": List["ServiceSummaryTypeDef"],
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

NamespaceFilterTypeDef = TypedDict(
    "NamespaceFilterTypeDef",
    {
        "Name": Literal["TYPE"],
        "Values": Sequence[str],
        "Condition": NotRequired[FilterConditionType],
    },
)

NamespacePropertiesTypeDef = TypedDict(
    "NamespacePropertiesTypeDef",
    {
        "DnsProperties": NotRequired["DnsPropertiesTypeDef"],
        "HttpProperties": NotRequired["HttpPropertiesTypeDef"],
    },
)

NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[NamespaceTypeType],
        "Description": NotRequired[str],
        "ServiceCount": NotRequired[int],
        "Properties": NotRequired["NamespacePropertiesTypeDef"],
        "CreateDate": NotRequired[datetime],
    },
)

NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[NamespaceTypeType],
        "Description": NotRequired[str],
        "ServiceCount": NotRequired[int],
        "Properties": NotRequired["NamespacePropertiesTypeDef"],
        "CreateDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
    },
)

OperationFilterTypeDef = TypedDict(
    "OperationFilterTypeDef",
    {
        "Name": OperationFilterNameType,
        "Values": Sequence[str],
        "Condition": NotRequired[FilterConditionType],
    },
)

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Status": NotRequired[OperationStatusType],
    },
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[OperationTypeType],
        "Status": NotRequired[OperationStatusType],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "Targets": NotRequired[Dict[OperationTargetTypeType, str]],
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

PrivateDnsNamespaceChangeTypeDef = TypedDict(
    "PrivateDnsNamespaceChangeTypeDef",
    {
        "Description": NotRequired[str],
        "Properties": NotRequired["PrivateDnsNamespacePropertiesChangeTypeDef"],
    },
)

PrivateDnsNamespacePropertiesChangeTypeDef = TypedDict(
    "PrivateDnsNamespacePropertiesChangeTypeDef",
    {
        "DnsProperties": "PrivateDnsPropertiesMutableChangeTypeDef",
    },
)

PrivateDnsNamespacePropertiesTypeDef = TypedDict(
    "PrivateDnsNamespacePropertiesTypeDef",
    {
        "DnsProperties": "PrivateDnsPropertiesMutableTypeDef",
    },
)

PrivateDnsPropertiesMutableChangeTypeDef = TypedDict(
    "PrivateDnsPropertiesMutableChangeTypeDef",
    {
        "SOA": "SOAChangeTypeDef",
    },
)

PrivateDnsPropertiesMutableTypeDef = TypedDict(
    "PrivateDnsPropertiesMutableTypeDef",
    {
        "SOA": "SOATypeDef",
    },
)

PublicDnsNamespaceChangeTypeDef = TypedDict(
    "PublicDnsNamespaceChangeTypeDef",
    {
        "Description": NotRequired[str],
        "Properties": NotRequired["PublicDnsNamespacePropertiesChangeTypeDef"],
    },
)

PublicDnsNamespacePropertiesChangeTypeDef = TypedDict(
    "PublicDnsNamespacePropertiesChangeTypeDef",
    {
        "DnsProperties": "PublicDnsPropertiesMutableChangeTypeDef",
    },
)

PublicDnsNamespacePropertiesTypeDef = TypedDict(
    "PublicDnsNamespacePropertiesTypeDef",
    {
        "DnsProperties": "PublicDnsPropertiesMutableTypeDef",
    },
)

PublicDnsPropertiesMutableChangeTypeDef = TypedDict(
    "PublicDnsPropertiesMutableChangeTypeDef",
    {
        "SOA": "SOAChangeTypeDef",
    },
)

PublicDnsPropertiesMutableTypeDef = TypedDict(
    "PublicDnsPropertiesMutableTypeDef",
    {
        "SOA": "SOATypeDef",
    },
)

RegisterInstanceRequestRequestTypeDef = TypedDict(
    "RegisterInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Attributes": Mapping[str, str],
        "CreatorRequestId": NotRequired[str],
    },
)

RegisterInstanceResponseTypeDef = TypedDict(
    "RegisterInstanceResponseTypeDef",
    {
        "OperationId": str,
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

SOAChangeTypeDef = TypedDict(
    "SOAChangeTypeDef",
    {
        "TTL": int,
    },
)

SOATypeDef = TypedDict(
    "SOATypeDef",
    {
        "TTL": int,
    },
)

ServiceChangeTypeDef = TypedDict(
    "ServiceChangeTypeDef",
    {
        "Description": NotRequired[str],
        "DnsConfig": NotRequired["DnsConfigChangeTypeDef"],
        "HealthCheckConfig": NotRequired["HealthCheckConfigTypeDef"],
    },
)

ServiceFilterTypeDef = TypedDict(
    "ServiceFilterTypeDef",
    {
        "Name": Literal["NAMESPACE_ID"],
        "Values": Sequence[str],
        "Condition": NotRequired[FilterConditionType],
    },
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ServiceTypeType],
        "Description": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "DnsConfig": NotRequired["DnsConfigTypeDef"],
        "HealthCheckConfig": NotRequired["HealthCheckConfigTypeDef"],
        "HealthCheckCustomConfig": NotRequired["HealthCheckCustomConfigTypeDef"],
        "CreateDate": NotRequired[datetime],
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceId": NotRequired[str],
        "Description": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "DnsConfig": NotRequired["DnsConfigTypeDef"],
        "Type": NotRequired[ServiceTypeType],
        "HealthCheckConfig": NotRequired["HealthCheckConfigTypeDef"],
        "HealthCheckCustomConfig": NotRequired["HealthCheckCustomConfigTypeDef"],
        "CreateDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
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

UpdateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "UpdateHttpNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": "HttpNamespaceChangeTypeDef",
        "UpdaterRequestId": NotRequired[str],
    },
)

UpdateHttpNamespaceResponseTypeDef = TypedDict(
    "UpdateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInstanceCustomHealthStatusRequestRequestTypeDef = TypedDict(
    "UpdateInstanceCustomHealthStatusRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Status": CustomHealthStatusType,
    },
)

UpdatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "UpdatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": "PrivateDnsNamespaceChangeTypeDef",
        "UpdaterRequestId": NotRequired[str],
    },
)

UpdatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "UpdatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": "PublicDnsNamespaceChangeTypeDef",
        "UpdaterRequestId": NotRequired[str],
    },
)

UpdatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "UpdatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "Id": str,
        "Service": "ServiceChangeTypeDef",
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
