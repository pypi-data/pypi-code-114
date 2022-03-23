"""
Type annotations for migration-hub-refactor-spaces service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_migration_hub_refactor_spaces/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_migration_hub_refactor_spaces.type_defs import ApiGatewayProxyConfigTypeDef

    data: ApiGatewayProxyConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ApiGatewayEndpointTypeType,
    ApplicationStateType,
    EnvironmentStateType,
    ErrorCodeType,
    ErrorResourceTypeType,
    HttpMethodType,
    RouteStateType,
    RouteTypeType,
    ServiceEndpointTypeType,
    ServiceStateType,
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
    "ApiGatewayProxyConfigTypeDef",
    "ApiGatewayProxyInputTypeDef",
    "ApiGatewayProxySummaryTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteEnvironmentResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentVpcTypeDef",
    "ErrorResponseTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRouteRequestRequestTypeDef",
    "GetRouteResponseTypeDef",
    "GetServiceRequestRequestTypeDef",
    "GetServiceResponseTypeDef",
    "LambdaEndpointConfigTypeDef",
    "LambdaEndpointInputTypeDef",
    "LambdaEndpointSummaryTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListEnvironmentVpcsRequestRequestTypeDef",
    "ListEnvironmentVpcsResponseTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListRoutesRequestRequestTypeDef",
    "ListRoutesResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RouteSummaryTypeDef",
    "ServiceSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UriPathRouteInputTypeDef",
    "UrlEndpointConfigTypeDef",
    "UrlEndpointInputTypeDef",
    "UrlEndpointSummaryTypeDef",
)

ApiGatewayProxyConfigTypeDef = TypedDict(
    "ApiGatewayProxyConfigTypeDef",
    {
        "ApiGatewayId": NotRequired[str],
        "EndpointType": NotRequired[ApiGatewayEndpointTypeType],
        "NlbArn": NotRequired[str],
        "NlbName": NotRequired[str],
        "ProxyUrl": NotRequired[str],
        "StageName": NotRequired[str],
        "VpcLinkId": NotRequired[str],
    },
)

ApiGatewayProxyInputTypeDef = TypedDict(
    "ApiGatewayProxyInputTypeDef",
    {
        "EndpointType": NotRequired[ApiGatewayEndpointTypeType],
        "StageName": NotRequired[str],
    },
)

ApiGatewayProxySummaryTypeDef = TypedDict(
    "ApiGatewayProxySummaryTypeDef",
    {
        "ApiGatewayId": NotRequired[str],
        "EndpointType": NotRequired[ApiGatewayEndpointTypeType],
        "NlbArn": NotRequired[str],
        "NlbName": NotRequired[str],
        "ProxyUrl": NotRequired[str],
        "StageName": NotRequired[str],
        "VpcLinkId": NotRequired[str],
    },
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApiGatewayProxy": NotRequired["ApiGatewayProxySummaryTypeDef"],
        "ApplicationId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedByAccountId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired["ErrorResponseTypeDef"],
        "LastUpdatedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "ProxyType": NotRequired[Literal["API_GATEWAY"]],
        "State": NotRequired[ApplicationStateType],
        "Tags": NotRequired[Dict[str, str]],
        "VpcId": NotRequired[str],
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "Name": str,
        "ProxyType": Literal["API_GATEWAY"],
        "VpcId": str,
        "ApiGatewayProxy": NotRequired["ApiGatewayProxyInputTypeDef"],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApiGatewayProxy": "ApiGatewayProxyInputTypeDef",
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentRequestRequestTypeDef",
    {
        "Name": str,
        "NetworkFabricType": Literal["TRANSIT_GATEWAY"],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateEnvironmentResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": Literal["TRANSIT_GATEWAY"],
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteRequestRequestTypeDef = TypedDict(
    "CreateRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteType": RouteTypeType,
        "ServiceIdentifier": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "UriPathRoute": NotRequired["UriPathRouteInputTypeDef"],
    },
)

CreateRouteResponseTypeDef = TypedDict(
    "CreateRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "OwnerAccountId": str,
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
        "UriPathRoute": "UriPathRouteInputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentIdentifier": str,
        "Name": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "LambdaEndpoint": NotRequired["LambdaEndpointInputTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "UrlEndpoint": NotRequired["UrlEndpointInputTypeDef"],
        "VpcId": NotRequired[str],
    },
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "LambdaEndpoint": "LambdaEndpointInputTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": "UrlEndpointInputTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)

DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "State": ApplicationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)

DeleteEnvironmentResponseTypeDef = TypedDict(
    "DeleteEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "State": EnvironmentStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)

DeleteRouteResponseTypeDef = TypedDict(
    "DeleteRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "LastUpdatedTime": datetime,
        "RouteId": str,
        "ServiceId": str,
        "State": RouteStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ServiceIdentifier": str,
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired["ErrorResponseTypeDef"],
        "LastUpdatedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "NetworkFabricType": NotRequired[Literal["TRANSIT_GATEWAY"]],
        "OwnerAccountId": NotRequired[str],
        "State": NotRequired[EnvironmentStateType],
        "Tags": NotRequired[Dict[str, str]],
        "TransitGatewayId": NotRequired[str],
    },
)

EnvironmentVpcTypeDef = TypedDict(
    "EnvironmentVpcTypeDef",
    {
        "AccountId": NotRequired[str],
        "CidrBlocks": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
        "EnvironmentId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "VpcId": NotRequired[str],
        "VpcName": NotRequired[str],
    },
)

ErrorResponseTypeDef = TypedDict(
    "ErrorResponseTypeDef",
    {
        "AccountId": NotRequired[str],
        "AdditionalDetails": NotRequired[Dict[str, str]],
        "Code": NotRequired[ErrorCodeType],
        "Message": NotRequired[str],
        "ResourceIdentifier": NotRequired[str],
        "ResourceType": NotRequired[ErrorResourceTypeType],
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "ApiGatewayProxy": "ApiGatewayProxyConfigTypeDef",
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)

GetEnvironmentResponseTypeDef = TypedDict(
    "GetEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": Literal["TRANSIT_GATEWAY"],
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "TransitGatewayId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteRequestRequestTypeDef = TypedDict(
    "GetRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)

GetRouteResponseTypeDef = TypedDict(
    "GetRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "IncludeChildPaths": bool,
        "LastUpdatedTime": datetime,
        "Methods": List[HttpMethodType],
        "OwnerAccountId": str,
        "PathResourceToId": Dict[str, str],
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "SourcePath": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ServiceIdentifier": str,
    },
)

GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LambdaEndpoint": "LambdaEndpointConfigTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": "UrlEndpointConfigTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LambdaEndpointConfigTypeDef = TypedDict(
    "LambdaEndpointConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

LambdaEndpointInputTypeDef = TypedDict(
    "LambdaEndpointInputTypeDef",
    {
        "Arn": str,
    },
)

LambdaEndpointSummaryTypeDef = TypedDict(
    "LambdaEndpointSummaryTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaryList": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentVpcsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentVpcsRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEnvironmentVpcsResponseTypeDef = TypedDict(
    "ListEnvironmentVpcsResponseTypeDef",
    {
        "EnvironmentVpcList": List["EnvironmentVpcTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "EnvironmentSummaryList": List["EnvironmentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoutesRequestRequestTypeDef = TypedDict(
    "ListRoutesRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRoutesResponseTypeDef = TypedDict(
    "ListRoutesResponseTypeDef",
    {
        "NextToken": str,
        "RouteSummaryList": List["RouteSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "NextToken": str,
        "ServiceSummaryList": List["ServiceSummaryTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "Policy": str,
        "ResourceArn": str,
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

RouteSummaryTypeDef = TypedDict(
    "RouteSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedByAccountId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired["ErrorResponseTypeDef"],
        "IncludeChildPaths": NotRequired[bool],
        "LastUpdatedTime": NotRequired[datetime],
        "Methods": NotRequired[List[HttpMethodType]],
        "OwnerAccountId": NotRequired[str],
        "PathResourceToId": NotRequired[Dict[str, str]],
        "RouteId": NotRequired[str],
        "RouteType": NotRequired[RouteTypeType],
        "ServiceId": NotRequired[str],
        "SourcePath": NotRequired[str],
        "State": NotRequired[RouteStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreatedByAccountId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "EndpointType": NotRequired[ServiceEndpointTypeType],
        "EnvironmentId": NotRequired[str],
        "Error": NotRequired["ErrorResponseTypeDef"],
        "LambdaEndpoint": NotRequired["LambdaEndpointSummaryTypeDef"],
        "LastUpdatedTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "ServiceId": NotRequired[str],
        "State": NotRequired[ServiceStateType],
        "Tags": NotRequired[Dict[str, str]],
        "UrlEndpoint": NotRequired["UrlEndpointSummaryTypeDef"],
        "VpcId": NotRequired[str],
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

UriPathRouteInputTypeDef = TypedDict(
    "UriPathRouteInputTypeDef",
    {
        "ActivationState": Literal["ACTIVE"],
        "SourcePath": str,
        "IncludeChildPaths": NotRequired[bool],
        "Methods": NotRequired[Sequence[HttpMethodType]],
    },
)

UrlEndpointConfigTypeDef = TypedDict(
    "UrlEndpointConfigTypeDef",
    {
        "HealthUrl": NotRequired[str],
        "Url": NotRequired[str],
    },
)

UrlEndpointInputTypeDef = TypedDict(
    "UrlEndpointInputTypeDef",
    {
        "Url": str,
        "HealthUrl": NotRequired[str],
    },
)

UrlEndpointSummaryTypeDef = TypedDict(
    "UrlEndpointSummaryTypeDef",
    {
        "HealthUrl": NotRequired[str],
        "Url": NotRequired[str],
    },
)
