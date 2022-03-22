"""
Type annotations for appmesh service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    DefaultGatewayRouteRewriteType,
    DnsResponseTypeType,
    DurationUnitType,
    EgressFilterTypeType,
    GatewayRouteStatusCodeType,
    GrpcRetryPolicyEventType,
    HttpMethodType,
    HttpSchemeType,
    ListenerTlsModeType,
    MeshStatusCodeType,
    PortProtocolType,
    RouteStatusCodeType,
    VirtualGatewayListenerTlsModeType,
    VirtualGatewayPortProtocolType,
    VirtualGatewayStatusCodeType,
    VirtualNodeStatusCodeType,
    VirtualRouterStatusCodeType,
    VirtualServiceStatusCodeType,
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
    "AccessLogTypeDef",
    "AwsCloudMapInstanceAttributeTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "BackendDefaultsTypeDef",
    "BackendTypeDef",
    "ClientPolicyTlsTypeDef",
    "ClientPolicyTypeDef",
    "ClientTlsCertificateTypeDef",
    "CreateGatewayRouteInputRequestTypeDef",
    "CreateGatewayRouteOutputTypeDef",
    "CreateMeshInputRequestTypeDef",
    "CreateMeshOutputTypeDef",
    "CreateRouteInputRequestTypeDef",
    "CreateRouteOutputTypeDef",
    "CreateVirtualGatewayInputRequestTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "CreateVirtualNodeInputRequestTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "CreateVirtualRouterInputRequestTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "CreateVirtualServiceInputRequestTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteGatewayRouteInputRequestTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DeleteMeshInputRequestTypeDef",
    "DeleteMeshOutputTypeDef",
    "DeleteRouteInputRequestTypeDef",
    "DeleteRouteOutputTypeDef",
    "DeleteVirtualGatewayInputRequestTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DeleteVirtualNodeInputRequestTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DeleteVirtualRouterInputRequestTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DeleteVirtualServiceInputRequestTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeGatewayRouteInputRequestTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "DescribeMeshInputRequestTypeDef",
    "DescribeMeshOutputTypeDef",
    "DescribeRouteInputRequestTypeDef",
    "DescribeRouteOutputTypeDef",
    "DescribeVirtualGatewayInputRequestTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "DescribeVirtualNodeInputRequestTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "DescribeVirtualRouterInputRequestTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "DescribeVirtualServiceInputRequestTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "FileAccessLogTypeDef",
    "GatewayRouteDataTypeDef",
    "GatewayRouteHostnameMatchTypeDef",
    "GatewayRouteHostnameRewriteTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteSpecTypeDef",
    "GatewayRouteStatusTypeDef",
    "GatewayRouteTargetTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcGatewayRouteMetadataTypeDef",
    "GrpcGatewayRouteRewriteTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcMetadataMatchMethodTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcRouteActionTypeDef",
    "GrpcRouteMatchTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataTypeDef",
    "GrpcRouteTypeDef",
    "GrpcTimeoutTypeDef",
    "HeaderMatchMethodTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "HttpGatewayRouteHeaderTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpGatewayRoutePathRewriteTypeDef",
    "HttpGatewayRoutePrefixRewriteTypeDef",
    "HttpGatewayRouteRewriteTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpPathMatchTypeDef",
    "HttpQueryParameterTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpRouteActionTypeDef",
    "HttpRouteHeaderTypeDef",
    "HttpRouteMatchTypeDef",
    "HttpRouteTypeDef",
    "HttpTimeoutTypeDef",
    "ListGatewayRoutesInputRequestTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "ListMeshesInputRequestTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesInputRequestTypeDef",
    "ListRoutesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualGatewaysInputRequestTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesInputRequestTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersInputRequestTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesInputRequestTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "ListenerTimeoutTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "ListenerTlsTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "ListenerTypeDef",
    "LoggingTypeDef",
    "MatchRangeTypeDef",
    "MeshDataTypeDef",
    "MeshRefTypeDef",
    "MeshSpecTypeDef",
    "MeshStatusTypeDef",
    "OutlierDetectionTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "QueryParameterMatchTypeDef",
    "ResourceMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "RouteDataTypeDef",
    "RouteRefTypeDef",
    "RouteSpecTypeDef",
    "RouteStatusTypeDef",
    "ServiceDiscoveryTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TagRefTypeDef",
    "TagResourceInputRequestTypeDef",
    "TcpRouteActionTypeDef",
    "TcpRouteTypeDef",
    "TcpTimeoutTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "TlsValidationContextTrustTypeDef",
    "TlsValidationContextTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGatewayRouteInputRequestTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "UpdateMeshInputRequestTypeDef",
    "UpdateMeshOutputTypeDef",
    "UpdateRouteInputRequestTypeDef",
    "UpdateRouteOutputTypeDef",
    "UpdateVirtualGatewayInputRequestTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "UpdateVirtualNodeInputRequestTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
    "UpdateVirtualRouterInputRequestTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "UpdateVirtualServiceInputRequestTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayDataTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayRefTypeDef",
    "VirtualGatewaySpecTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualNodeDataTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeRefTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualNodeSpecTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualRouterDataTypeDef",
    "VirtualRouterListenerTypeDef",
    "VirtualRouterRefTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualRouterSpecTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualServiceDataTypeDef",
    "VirtualServiceProviderTypeDef",
    "VirtualServiceRefTypeDef",
    "VirtualServiceSpecTypeDef",
    "VirtualServiceStatusTypeDef",
    "WeightedTargetTypeDef",
)

AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "file": NotRequired["FileAccessLogTypeDef"],
    },
)

AwsCloudMapInstanceAttributeTypeDef = TypedDict(
    "AwsCloudMapInstanceAttributeTypeDef",
    {
        "key": str,
        "value": str,
    },
)

AwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "AwsCloudMapServiceDiscoveryTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
        "attributes": NotRequired[Sequence["AwsCloudMapInstanceAttributeTypeDef"]],
    },
)

BackendDefaultsTypeDef = TypedDict(
    "BackendDefaultsTypeDef",
    {
        "clientPolicy": NotRequired["ClientPolicyTypeDef"],
    },
)

BackendTypeDef = TypedDict(
    "BackendTypeDef",
    {
        "virtualService": NotRequired["VirtualServiceBackendTypeDef"],
    },
)

ClientPolicyTlsTypeDef = TypedDict(
    "ClientPolicyTlsTypeDef",
    {
        "validation": "TlsValidationContextTypeDef",
        "certificate": NotRequired["ClientTlsCertificateTypeDef"],
        "enforce": NotRequired[bool],
        "ports": NotRequired[Sequence[int]],
    },
)

ClientPolicyTypeDef = TypedDict(
    "ClientPolicyTypeDef",
    {
        "tls": NotRequired["ClientPolicyTlsTypeDef"],
    },
)

ClientTlsCertificateTypeDef = TypedDict(
    "ClientTlsCertificateTypeDef",
    {
        "file": NotRequired["ListenerTlsFileCertificateTypeDef"],
        "sds": NotRequired["ListenerTlsSdsCertificateTypeDef"],
    },
)

CreateGatewayRouteInputRequestTypeDef = TypedDict(
    "CreateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": "GatewayRouteSpecTypeDef",
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateGatewayRouteOutputTypeDef = TypedDict(
    "CreateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeshInputRequestTypeDef = TypedDict(
    "CreateMeshInputRequestTypeDef",
    {
        "meshName": str,
        "clientToken": NotRequired[str],
        "spec": NotRequired["MeshSpecTypeDef"],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateMeshOutputTypeDef = TypedDict(
    "CreateMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteInputRequestTypeDef = TypedDict(
    "CreateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateRouteOutputTypeDef = TypedDict(
    "CreateRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualGatewayInputRequestTypeDef = TypedDict(
    "CreateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualGatewaySpecTypeDef",
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateVirtualGatewayOutputTypeDef = TypedDict(
    "CreateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualNodeInputRequestTypeDef = TypedDict(
    "CreateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualNodeSpecTypeDef",
        "virtualNodeName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateVirtualNodeOutputTypeDef = TypedDict(
    "CreateVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualRouterInputRequestTypeDef = TypedDict(
    "CreateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualRouterSpecTypeDef",
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateVirtualRouterOutputTypeDef = TypedDict(
    "CreateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualServiceInputRequestTypeDef = TypedDict(
    "CreateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualServiceSpecTypeDef",
        "virtualServiceName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
        "tags": NotRequired[Sequence["TagRefTypeDef"]],
    },
)

CreateVirtualServiceOutputTypeDef = TypedDict(
    "CreateVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayRouteInputRequestTypeDef = TypedDict(
    "DeleteGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)

DeleteGatewayRouteOutputTypeDef = TypedDict(
    "DeleteGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMeshInputRequestTypeDef = TypedDict(
    "DeleteMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)

DeleteMeshOutputTypeDef = TypedDict(
    "DeleteMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRouteInputRequestTypeDef = TypedDict(
    "DeleteRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)

DeleteRouteOutputTypeDef = TypedDict(
    "DeleteRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualGatewayInputRequestTypeDef = TypedDict(
    "DeleteVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)

DeleteVirtualGatewayOutputTypeDef = TypedDict(
    "DeleteVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualNodeInputRequestTypeDef = TypedDict(
    "DeleteVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
        "meshOwner": NotRequired[str],
    },
)

DeleteVirtualNodeOutputTypeDef = TypedDict(
    "DeleteVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualRouterInputRequestTypeDef = TypedDict(
    "DeleteVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)

DeleteVirtualRouterOutputTypeDef = TypedDict(
    "DeleteVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualServiceInputRequestTypeDef = TypedDict(
    "DeleteVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
        "meshOwner": NotRequired[str],
    },
)

DeleteVirtualServiceOutputTypeDef = TypedDict(
    "DeleteVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayRouteInputRequestTypeDef = TypedDict(
    "DescribeGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeGatewayRouteOutputTypeDef = TypedDict(
    "DescribeGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMeshInputRequestTypeDef = TypedDict(
    "DescribeMeshInputRequestTypeDef",
    {
        "meshName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeMeshOutputTypeDef = TypedDict(
    "DescribeMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteInputRequestTypeDef = TypedDict(
    "DescribeRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeRouteOutputTypeDef = TypedDict(
    "DescribeRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualGatewayInputRequestTypeDef = TypedDict(
    "DescribeVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeVirtualGatewayOutputTypeDef = TypedDict(
    "DescribeVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualNodeInputRequestTypeDef = TypedDict(
    "DescribeVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeVirtualNodeOutputTypeDef = TypedDict(
    "DescribeVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualRouterInputRequestTypeDef = TypedDict(
    "DescribeVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeVirtualRouterOutputTypeDef = TypedDict(
    "DescribeVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualServiceInputRequestTypeDef = TypedDict(
    "DescribeVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
        "meshOwner": NotRequired[str],
    },
)

DescribeVirtualServiceOutputTypeDef = TypedDict(
    "DescribeVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsServiceDiscoveryTypeDef = TypedDict(
    "DnsServiceDiscoveryTypeDef",
    {
        "hostname": str,
        "responseType": NotRequired[DnsResponseTypeType],
    },
)

DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "unit": NotRequired[DurationUnitType],
        "value": NotRequired[int],
    },
)

EgressFilterTypeDef = TypedDict(
    "EgressFilterTypeDef",
    {
        "type": EgressFilterTypeType,
    },
)

FileAccessLogTypeDef = TypedDict(
    "FileAccessLogTypeDef",
    {
        "path": str,
    },
)

GatewayRouteDataTypeDef = TypedDict(
    "GatewayRouteDataTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "GatewayRouteSpecTypeDef",
        "status": "GatewayRouteStatusTypeDef",
        "virtualGatewayName": str,
    },
)

GatewayRouteHostnameMatchTypeDef = TypedDict(
    "GatewayRouteHostnameMatchTypeDef",
    {
        "exact": NotRequired[str],
        "suffix": NotRequired[str],
    },
)

GatewayRouteHostnameRewriteTypeDef = TypedDict(
    "GatewayRouteHostnameRewriteTypeDef",
    {
        "defaultTargetHostname": NotRequired[DefaultGatewayRouteRewriteType],
    },
)

GatewayRouteRefTypeDef = TypedDict(
    "GatewayRouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "gatewayRouteName": str,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

GatewayRouteSpecTypeDef = TypedDict(
    "GatewayRouteSpecTypeDef",
    {
        "grpcRoute": NotRequired["GrpcGatewayRouteTypeDef"],
        "http2Route": NotRequired["HttpGatewayRouteTypeDef"],
        "httpRoute": NotRequired["HttpGatewayRouteTypeDef"],
        "priority": NotRequired[int],
    },
)

GatewayRouteStatusTypeDef = TypedDict(
    "GatewayRouteStatusTypeDef",
    {
        "status": GatewayRouteStatusCodeType,
    },
)

GatewayRouteTargetTypeDef = TypedDict(
    "GatewayRouteTargetTypeDef",
    {
        "virtualService": "GatewayRouteVirtualServiceTypeDef",
    },
)

GatewayRouteVirtualServiceTypeDef = TypedDict(
    "GatewayRouteVirtualServiceTypeDef",
    {
        "virtualServiceName": str,
    },
)

GrpcGatewayRouteActionTypeDef = TypedDict(
    "GrpcGatewayRouteActionTypeDef",
    {
        "target": "GatewayRouteTargetTypeDef",
        "rewrite": NotRequired["GrpcGatewayRouteRewriteTypeDef"],
    },
)

GrpcGatewayRouteMatchTypeDef = TypedDict(
    "GrpcGatewayRouteMatchTypeDef",
    {
        "hostname": NotRequired["GatewayRouteHostnameMatchTypeDef"],
        "metadata": NotRequired[Sequence["GrpcGatewayRouteMetadataTypeDef"]],
        "serviceName": NotRequired[str],
    },
)

GrpcGatewayRouteMetadataTypeDef = TypedDict(
    "GrpcGatewayRouteMetadataTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired["GrpcMetadataMatchMethodTypeDef"],
    },
)

GrpcGatewayRouteRewriteTypeDef = TypedDict(
    "GrpcGatewayRouteRewriteTypeDef",
    {
        "hostname": NotRequired["GatewayRouteHostnameRewriteTypeDef"],
    },
)

GrpcGatewayRouteTypeDef = TypedDict(
    "GrpcGatewayRouteTypeDef",
    {
        "action": "GrpcGatewayRouteActionTypeDef",
        "match": "GrpcGatewayRouteMatchTypeDef",
    },
)

GrpcMetadataMatchMethodTypeDef = TypedDict(
    "GrpcMetadataMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired["MatchRangeTypeDef"],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)

GrpcRetryPolicyTypeDef = TypedDict(
    "GrpcRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": "DurationTypeDef",
        "grpcRetryEvents": NotRequired[Sequence[GrpcRetryPolicyEventType]],
        "httpRetryEvents": NotRequired[Sequence[str]],
        "tcpRetryEvents": NotRequired[Sequence[Literal["connection-error"]]],
    },
)

GrpcRouteActionTypeDef = TypedDict(
    "GrpcRouteActionTypeDef",
    {
        "weightedTargets": Sequence["WeightedTargetTypeDef"],
    },
)

GrpcRouteMatchTypeDef = TypedDict(
    "GrpcRouteMatchTypeDef",
    {
        "metadata": NotRequired[Sequence["GrpcRouteMetadataTypeDef"]],
        "methodName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)

GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired["MatchRangeTypeDef"],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)

GrpcRouteMetadataTypeDef = TypedDict(
    "GrpcRouteMetadataTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired["GrpcRouteMetadataMatchMethodTypeDef"],
    },
)

GrpcRouteTypeDef = TypedDict(
    "GrpcRouteTypeDef",
    {
        "action": "GrpcRouteActionTypeDef",
        "match": "GrpcRouteMatchTypeDef",
        "retryPolicy": NotRequired["GrpcRetryPolicyTypeDef"],
        "timeout": NotRequired["GrpcTimeoutTypeDef"],
    },
)

GrpcTimeoutTypeDef = TypedDict(
    "GrpcTimeoutTypeDef",
    {
        "idle": NotRequired["DurationTypeDef"],
        "perRequest": NotRequired["DurationTypeDef"],
    },
)

HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired["MatchRangeTypeDef"],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)

HealthCheckPolicyTypeDef = TypedDict(
    "HealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": PortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
        "path": NotRequired[str],
        "port": NotRequired[int],
    },
)

HttpGatewayRouteActionTypeDef = TypedDict(
    "HttpGatewayRouteActionTypeDef",
    {
        "target": "GatewayRouteTargetTypeDef",
        "rewrite": NotRequired["HttpGatewayRouteRewriteTypeDef"],
    },
)

HttpGatewayRouteHeaderTypeDef = TypedDict(
    "HttpGatewayRouteHeaderTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired["HeaderMatchMethodTypeDef"],
    },
)

HttpGatewayRouteMatchTypeDef = TypedDict(
    "HttpGatewayRouteMatchTypeDef",
    {
        "headers": NotRequired[Sequence["HttpGatewayRouteHeaderTypeDef"]],
        "hostname": NotRequired["GatewayRouteHostnameMatchTypeDef"],
        "method": NotRequired[HttpMethodType],
        "path": NotRequired["HttpPathMatchTypeDef"],
        "prefix": NotRequired[str],
        "queryParameters": NotRequired[Sequence["HttpQueryParameterTypeDef"]],
    },
)

HttpGatewayRoutePathRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePathRewriteTypeDef",
    {
        "exact": NotRequired[str],
    },
)

HttpGatewayRoutePrefixRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePrefixRewriteTypeDef",
    {
        "defaultPrefix": NotRequired[DefaultGatewayRouteRewriteType],
        "value": NotRequired[str],
    },
)

HttpGatewayRouteRewriteTypeDef = TypedDict(
    "HttpGatewayRouteRewriteTypeDef",
    {
        "hostname": NotRequired["GatewayRouteHostnameRewriteTypeDef"],
        "path": NotRequired["HttpGatewayRoutePathRewriteTypeDef"],
        "prefix": NotRequired["HttpGatewayRoutePrefixRewriteTypeDef"],
    },
)

HttpGatewayRouteTypeDef = TypedDict(
    "HttpGatewayRouteTypeDef",
    {
        "action": "HttpGatewayRouteActionTypeDef",
        "match": "HttpGatewayRouteMatchTypeDef",
    },
)

HttpPathMatchTypeDef = TypedDict(
    "HttpPathMatchTypeDef",
    {
        "exact": NotRequired[str],
        "regex": NotRequired[str],
    },
)

HttpQueryParameterTypeDef = TypedDict(
    "HttpQueryParameterTypeDef",
    {
        "name": str,
        "match": NotRequired["QueryParameterMatchTypeDef"],
    },
)

HttpRetryPolicyTypeDef = TypedDict(
    "HttpRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": "DurationTypeDef",
        "httpRetryEvents": NotRequired[Sequence[str]],
        "tcpRetryEvents": NotRequired[Sequence[Literal["connection-error"]]],
    },
)

HttpRouteActionTypeDef = TypedDict(
    "HttpRouteActionTypeDef",
    {
        "weightedTargets": Sequence["WeightedTargetTypeDef"],
    },
)

HttpRouteHeaderTypeDef = TypedDict(
    "HttpRouteHeaderTypeDef",
    {
        "name": str,
        "invert": NotRequired[bool],
        "match": NotRequired["HeaderMatchMethodTypeDef"],
    },
)

HttpRouteMatchTypeDef = TypedDict(
    "HttpRouteMatchTypeDef",
    {
        "headers": NotRequired[Sequence["HttpRouteHeaderTypeDef"]],
        "method": NotRequired[HttpMethodType],
        "path": NotRequired["HttpPathMatchTypeDef"],
        "prefix": NotRequired[str],
        "queryParameters": NotRequired[Sequence["HttpQueryParameterTypeDef"]],
        "scheme": NotRequired[HttpSchemeType],
    },
)

HttpRouteTypeDef = TypedDict(
    "HttpRouteTypeDef",
    {
        "action": "HttpRouteActionTypeDef",
        "match": "HttpRouteMatchTypeDef",
        "retryPolicy": NotRequired["HttpRetryPolicyTypeDef"],
        "timeout": NotRequired["HttpTimeoutTypeDef"],
    },
)

HttpTimeoutTypeDef = TypedDict(
    "HttpTimeoutTypeDef",
    {
        "idle": NotRequired["DurationTypeDef"],
        "perRequest": NotRequired["DurationTypeDef"],
    },
)

ListGatewayRoutesInputRequestTypeDef = TypedDict(
    "ListGatewayRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListGatewayRoutesOutputTypeDef = TypedDict(
    "ListGatewayRoutesOutputTypeDef",
    {
        "gatewayRoutes": List["GatewayRouteRefTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeshesInputRequestTypeDef = TypedDict(
    "ListMeshesInputRequestTypeDef",
    {
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListMeshesOutputTypeDef = TypedDict(
    "ListMeshesOutputTypeDef",
    {
        "meshes": List["MeshRefTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoutesInputRequestTypeDef = TypedDict(
    "ListRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListRoutesOutputTypeDef = TypedDict(
    "ListRoutesOutputTypeDef",
    {
        "nextToken": str,
        "routes": List["RouteRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List["TagRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualGatewaysInputRequestTypeDef = TypedDict(
    "ListVirtualGatewaysInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListVirtualGatewaysOutputTypeDef = TypedDict(
    "ListVirtualGatewaysOutputTypeDef",
    {
        "nextToken": str,
        "virtualGateways": List["VirtualGatewayRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualNodesInputRequestTypeDef = TypedDict(
    "ListVirtualNodesInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListVirtualNodesOutputTypeDef = TypedDict(
    "ListVirtualNodesOutputTypeDef",
    {
        "nextToken": str,
        "virtualNodes": List["VirtualNodeRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualRoutersInputRequestTypeDef = TypedDict(
    "ListVirtualRoutersInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListVirtualRoutersOutputTypeDef = TypedDict(
    "ListVirtualRoutersOutputTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List["VirtualRouterRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualServicesInputRequestTypeDef = TypedDict(
    "ListVirtualServicesInputRequestTypeDef",
    {
        "meshName": str,
        "limit": NotRequired[int],
        "meshOwner": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListVirtualServicesOutputTypeDef = TypedDict(
    "ListVirtualServicesOutputTypeDef",
    {
        "nextToken": str,
        "virtualServices": List["VirtualServiceRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTimeoutTypeDef = TypedDict(
    "ListenerTimeoutTypeDef",
    {
        "grpc": NotRequired["GrpcTimeoutTypeDef"],
        "http": NotRequired["HttpTimeoutTypeDef"],
        "http2": NotRequired["HttpTimeoutTypeDef"],
        "tcp": NotRequired["TcpTimeoutTypeDef"],
    },
)

ListenerTlsAcmCertificateTypeDef = TypedDict(
    "ListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

ListenerTlsCertificateTypeDef = TypedDict(
    "ListenerTlsCertificateTypeDef",
    {
        "acm": NotRequired["ListenerTlsAcmCertificateTypeDef"],
        "file": NotRequired["ListenerTlsFileCertificateTypeDef"],
        "sds": NotRequired["ListenerTlsSdsCertificateTypeDef"],
    },
)

ListenerTlsFileCertificateTypeDef = TypedDict(
    "ListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

ListenerTlsSdsCertificateTypeDef = TypedDict(
    "ListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

ListenerTlsTypeDef = TypedDict(
    "ListenerTlsTypeDef",
    {
        "certificate": "ListenerTlsCertificateTypeDef",
        "mode": ListenerTlsModeType,
        "validation": NotRequired["ListenerTlsValidationContextTypeDef"],
    },
)

ListenerTlsValidationContextTrustTypeDef = TypedDict(
    "ListenerTlsValidationContextTrustTypeDef",
    {
        "file": NotRequired["TlsValidationContextFileTrustTypeDef"],
        "sds": NotRequired["TlsValidationContextSdsTrustTypeDef"],
    },
)

ListenerTlsValidationContextTypeDef = TypedDict(
    "ListenerTlsValidationContextTypeDef",
    {
        "trust": "ListenerTlsValidationContextTrustTypeDef",
        "subjectAlternativeNames": NotRequired["SubjectAlternativeNamesTypeDef"],
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "portMapping": "PortMappingTypeDef",
        "connectionPool": NotRequired["VirtualNodeConnectionPoolTypeDef"],
        "healthCheck": NotRequired["HealthCheckPolicyTypeDef"],
        "outlierDetection": NotRequired["OutlierDetectionTypeDef"],
        "timeout": NotRequired["ListenerTimeoutTypeDef"],
        "tls": NotRequired["ListenerTlsTypeDef"],
    },
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "accessLog": NotRequired["AccessLogTypeDef"],
    },
)

MatchRangeTypeDef = TypedDict(
    "MatchRangeTypeDef",
    {
        "end": int,
        "start": int,
    },
)

MeshDataTypeDef = TypedDict(
    "MeshDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "MeshSpecTypeDef",
        "status": "MeshStatusTypeDef",
    },
)

MeshRefTypeDef = TypedDict(
    "MeshRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
    },
)

MeshSpecTypeDef = TypedDict(
    "MeshSpecTypeDef",
    {
        "egressFilter": NotRequired["EgressFilterTypeDef"],
    },
)

MeshStatusTypeDef = TypedDict(
    "MeshStatusTypeDef",
    {
        "status": NotRequired[MeshStatusCodeType],
    },
)

OutlierDetectionTypeDef = TypedDict(
    "OutlierDetectionTypeDef",
    {
        "baseEjectionDuration": "DurationTypeDef",
        "interval": "DurationTypeDef",
        "maxEjectionPercent": int,
        "maxServerErrors": int,
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

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "port": int,
        "protocol": PortProtocolType,
    },
)

QueryParameterMatchTypeDef = TypedDict(
    "QueryParameterMatchTypeDef",
    {
        "exact": NotRequired[str],
    },
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshOwner": str,
        "resourceOwner": str,
        "uid": str,
        "version": int,
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

RouteDataTypeDef = TypedDict(
    "RouteDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "status": "RouteStatusTypeDef",
        "virtualRouterName": str,
    },
)

RouteRefTypeDef = TypedDict(
    "RouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "routeName": str,
        "version": int,
        "virtualRouterName": str,
    },
)

RouteSpecTypeDef = TypedDict(
    "RouteSpecTypeDef",
    {
        "grpcRoute": NotRequired["GrpcRouteTypeDef"],
        "http2Route": NotRequired["HttpRouteTypeDef"],
        "httpRoute": NotRequired["HttpRouteTypeDef"],
        "priority": NotRequired[int],
        "tcpRoute": NotRequired["TcpRouteTypeDef"],
    },
)

RouteStatusTypeDef = TypedDict(
    "RouteStatusTypeDef",
    {
        "status": RouteStatusCodeType,
    },
)

ServiceDiscoveryTypeDef = TypedDict(
    "ServiceDiscoveryTypeDef",
    {
        "awsCloudMap": NotRequired["AwsCloudMapServiceDiscoveryTypeDef"],
        "dns": NotRequired["DnsServiceDiscoveryTypeDef"],
    },
)

SubjectAlternativeNameMatchersTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersTypeDef",
    {
        "exact": Sequence[str],
    },
)

SubjectAlternativeNamesTypeDef = TypedDict(
    "SubjectAlternativeNamesTypeDef",
    {
        "match": "SubjectAlternativeNameMatchersTypeDef",
    },
)

TagRefTypeDef = TypedDict(
    "TagRefTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagRefTypeDef"],
    },
)

TcpRouteActionTypeDef = TypedDict(
    "TcpRouteActionTypeDef",
    {
        "weightedTargets": Sequence["WeightedTargetTypeDef"],
    },
)

TcpRouteTypeDef = TypedDict(
    "TcpRouteTypeDef",
    {
        "action": "TcpRouteActionTypeDef",
        "timeout": NotRequired["TcpTimeoutTypeDef"],
    },
)

TcpTimeoutTypeDef = TypedDict(
    "TcpTimeoutTypeDef",
    {
        "idle": NotRequired["DurationTypeDef"],
    },
)

TlsValidationContextAcmTrustTypeDef = TypedDict(
    "TlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": Sequence[str],
    },
)

TlsValidationContextFileTrustTypeDef = TypedDict(
    "TlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

TlsValidationContextSdsTrustTypeDef = TypedDict(
    "TlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

TlsValidationContextTrustTypeDef = TypedDict(
    "TlsValidationContextTrustTypeDef",
    {
        "acm": NotRequired["TlsValidationContextAcmTrustTypeDef"],
        "file": NotRequired["TlsValidationContextFileTrustTypeDef"],
        "sds": NotRequired["TlsValidationContextSdsTrustTypeDef"],
    },
)

TlsValidationContextTypeDef = TypedDict(
    "TlsValidationContextTypeDef",
    {
        "trust": "TlsValidationContextTrustTypeDef",
        "subjectAlternativeNames": NotRequired["SubjectAlternativeNamesTypeDef"],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateGatewayRouteInputRequestTypeDef = TypedDict(
    "UpdateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": "GatewayRouteSpecTypeDef",
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)

UpdateGatewayRouteOutputTypeDef = TypedDict(
    "UpdateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMeshInputRequestTypeDef = TypedDict(
    "UpdateMeshInputRequestTypeDef",
    {
        "meshName": str,
        "clientToken": NotRequired[str],
        "spec": NotRequired["MeshSpecTypeDef"],
    },
)

UpdateMeshOutputTypeDef = TypedDict(
    "UpdateMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRouteInputRequestTypeDef = TypedDict(
    "UpdateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)

UpdateRouteOutputTypeDef = TypedDict(
    "UpdateRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVirtualGatewayInputRequestTypeDef = TypedDict(
    "UpdateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualGatewaySpecTypeDef",
        "virtualGatewayName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)

UpdateVirtualGatewayOutputTypeDef = TypedDict(
    "UpdateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVirtualNodeInputRequestTypeDef = TypedDict(
    "UpdateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualNodeSpecTypeDef",
        "virtualNodeName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)

UpdateVirtualNodeOutputTypeDef = TypedDict(
    "UpdateVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVirtualRouterInputRequestTypeDef = TypedDict(
    "UpdateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualRouterSpecTypeDef",
        "virtualRouterName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)

UpdateVirtualRouterOutputTypeDef = TypedDict(
    "UpdateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVirtualServiceInputRequestTypeDef = TypedDict(
    "UpdateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualServiceSpecTypeDef",
        "virtualServiceName": str,
        "clientToken": NotRequired[str],
        "meshOwner": NotRequired[str],
    },
)

UpdateVirtualServiceOutputTypeDef = TypedDict(
    "UpdateVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualGatewayAccessLogTypeDef = TypedDict(
    "VirtualGatewayAccessLogTypeDef",
    {
        "file": NotRequired["VirtualGatewayFileAccessLogTypeDef"],
    },
)

VirtualGatewayBackendDefaultsTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsTypeDef",
    {
        "clientPolicy": NotRequired["VirtualGatewayClientPolicyTypeDef"],
    },
)

VirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTlsTypeDef",
    {
        "validation": "VirtualGatewayTlsValidationContextTypeDef",
        "certificate": NotRequired["VirtualGatewayClientTlsCertificateTypeDef"],
        "enforce": NotRequired[bool],
        "ports": NotRequired[Sequence[int]],
    },
)

VirtualGatewayClientPolicyTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTypeDef",
    {
        "tls": NotRequired["VirtualGatewayClientPolicyTlsTypeDef"],
    },
)

VirtualGatewayClientTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayClientTlsCertificateTypeDef",
    {
        "file": NotRequired["VirtualGatewayListenerTlsFileCertificateTypeDef"],
        "sds": NotRequired["VirtualGatewayListenerTlsSdsCertificateTypeDef"],
    },
)

VirtualGatewayConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayConnectionPoolTypeDef",
    {
        "grpc": NotRequired["VirtualGatewayGrpcConnectionPoolTypeDef"],
        "http": NotRequired["VirtualGatewayHttpConnectionPoolTypeDef"],
        "http2": NotRequired["VirtualGatewayHttp2ConnectionPoolTypeDef"],
    },
)

VirtualGatewayDataTypeDef = TypedDict(
    "VirtualGatewayDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualGatewaySpecTypeDef",
        "status": "VirtualGatewayStatusTypeDef",
        "virtualGatewayName": str,
    },
)

VirtualGatewayFileAccessLogTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogTypeDef",
    {
        "path": str,
    },
)

VirtualGatewayGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "VirtualGatewayHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": VirtualGatewayPortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
        "path": NotRequired[str],
        "port": NotRequired[int],
    },
)

VirtualGatewayHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
        "maxPendingRequests": NotRequired[int],
    },
)

VirtualGatewayListenerTlsAcmCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

VirtualGatewayListenerTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsCertificateTypeDef",
    {
        "acm": NotRequired["VirtualGatewayListenerTlsAcmCertificateTypeDef"],
        "file": NotRequired["VirtualGatewayListenerTlsFileCertificateTypeDef"],
        "sds": NotRequired["VirtualGatewayListenerTlsSdsCertificateTypeDef"],
    },
)

VirtualGatewayListenerTlsFileCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

VirtualGatewayListenerTlsSdsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

VirtualGatewayListenerTlsTypeDef = TypedDict(
    "VirtualGatewayListenerTlsTypeDef",
    {
        "certificate": "VirtualGatewayListenerTlsCertificateTypeDef",
        "mode": VirtualGatewayListenerTlsModeType,
        "validation": NotRequired["VirtualGatewayListenerTlsValidationContextTypeDef"],
    },
)

VirtualGatewayListenerTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    {
        "file": NotRequired["VirtualGatewayTlsValidationContextFileTrustTypeDef"],
        "sds": NotRequired["VirtualGatewayTlsValidationContextSdsTrustTypeDef"],
    },
)

VirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "trust": "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
        "subjectAlternativeNames": NotRequired["SubjectAlternativeNamesTypeDef"],
    },
)

VirtualGatewayListenerTypeDef = TypedDict(
    "VirtualGatewayListenerTypeDef",
    {
        "portMapping": "VirtualGatewayPortMappingTypeDef",
        "connectionPool": NotRequired["VirtualGatewayConnectionPoolTypeDef"],
        "healthCheck": NotRequired["VirtualGatewayHealthCheckPolicyTypeDef"],
        "tls": NotRequired["VirtualGatewayListenerTlsTypeDef"],
    },
)

VirtualGatewayLoggingTypeDef = TypedDict(
    "VirtualGatewayLoggingTypeDef",
    {
        "accessLog": NotRequired["VirtualGatewayAccessLogTypeDef"],
    },
)

VirtualGatewayPortMappingTypeDef = TypedDict(
    "VirtualGatewayPortMappingTypeDef",
    {
        "port": int,
        "protocol": VirtualGatewayPortProtocolType,
    },
)

VirtualGatewayRefTypeDef = TypedDict(
    "VirtualGatewayRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

VirtualGatewaySpecTypeDef = TypedDict(
    "VirtualGatewaySpecTypeDef",
    {
        "listeners": Sequence["VirtualGatewayListenerTypeDef"],
        "backendDefaults": NotRequired["VirtualGatewayBackendDefaultsTypeDef"],
        "logging": NotRequired["VirtualGatewayLoggingTypeDef"],
    },
)

VirtualGatewayStatusTypeDef = TypedDict(
    "VirtualGatewayStatusTypeDef",
    {
        "status": VirtualGatewayStatusCodeType,
    },
)

VirtualGatewayTlsValidationContextAcmTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": Sequence[str],
    },
)

VirtualGatewayTlsValidationContextFileTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

VirtualGatewayTlsValidationContextSdsTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

VirtualGatewayTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    {
        "acm": NotRequired["VirtualGatewayTlsValidationContextAcmTrustTypeDef"],
        "file": NotRequired["VirtualGatewayTlsValidationContextFileTrustTypeDef"],
        "sds": NotRequired["VirtualGatewayTlsValidationContextSdsTrustTypeDef"],
    },
)

VirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTypeDef",
    {
        "trust": "VirtualGatewayTlsValidationContextTrustTypeDef",
        "subjectAlternativeNames": NotRequired["SubjectAlternativeNamesTypeDef"],
    },
)

VirtualNodeConnectionPoolTypeDef = TypedDict(
    "VirtualNodeConnectionPoolTypeDef",
    {
        "grpc": NotRequired["VirtualNodeGrpcConnectionPoolTypeDef"],
        "http": NotRequired["VirtualNodeHttpConnectionPoolTypeDef"],
        "http2": NotRequired["VirtualNodeHttp2ConnectionPoolTypeDef"],
        "tcp": NotRequired["VirtualNodeTcpConnectionPoolTypeDef"],
    },
)

VirtualNodeDataTypeDef = TypedDict(
    "VirtualNodeDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualNodeSpecTypeDef",
        "status": "VirtualNodeStatusTypeDef",
        "virtualNodeName": str,
    },
)

VirtualNodeGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualNodeGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualNodeHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
        "maxPendingRequests": NotRequired[int],
    },
)

VirtualNodeRefTypeDef = TypedDict(
    "VirtualNodeRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualNodeName": str,
    },
)

VirtualNodeServiceProviderTypeDef = TypedDict(
    "VirtualNodeServiceProviderTypeDef",
    {
        "virtualNodeName": str,
    },
)

VirtualNodeSpecTypeDef = TypedDict(
    "VirtualNodeSpecTypeDef",
    {
        "backendDefaults": NotRequired["BackendDefaultsTypeDef"],
        "backends": NotRequired[Sequence["BackendTypeDef"]],
        "listeners": NotRequired[Sequence["ListenerTypeDef"]],
        "logging": NotRequired["LoggingTypeDef"],
        "serviceDiscovery": NotRequired["ServiceDiscoveryTypeDef"],
    },
)

VirtualNodeStatusTypeDef = TypedDict(
    "VirtualNodeStatusTypeDef",
    {
        "status": VirtualNodeStatusCodeType,
    },
)

VirtualNodeTcpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeTcpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)

VirtualRouterDataTypeDef = TypedDict(
    "VirtualRouterDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualRouterSpecTypeDef",
        "status": "VirtualRouterStatusTypeDef",
        "virtualRouterName": str,
    },
)

VirtualRouterListenerTypeDef = TypedDict(
    "VirtualRouterListenerTypeDef",
    {
        "portMapping": "PortMappingTypeDef",
    },
)

VirtualRouterRefTypeDef = TypedDict(
    "VirtualRouterRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualRouterName": str,
    },
)

VirtualRouterServiceProviderTypeDef = TypedDict(
    "VirtualRouterServiceProviderTypeDef",
    {
        "virtualRouterName": str,
    },
)

VirtualRouterSpecTypeDef = TypedDict(
    "VirtualRouterSpecTypeDef",
    {
        "listeners": NotRequired[Sequence["VirtualRouterListenerTypeDef"]],
    },
)

VirtualRouterStatusTypeDef = TypedDict(
    "VirtualRouterStatusTypeDef",
    {
        "status": VirtualRouterStatusCodeType,
    },
)

VirtualServiceBackendTypeDef = TypedDict(
    "VirtualServiceBackendTypeDef",
    {
        "virtualServiceName": str,
        "clientPolicy": NotRequired["ClientPolicyTypeDef"],
    },
)

VirtualServiceDataTypeDef = TypedDict(
    "VirtualServiceDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualServiceSpecTypeDef",
        "status": "VirtualServiceStatusTypeDef",
        "virtualServiceName": str,
    },
)

VirtualServiceProviderTypeDef = TypedDict(
    "VirtualServiceProviderTypeDef",
    {
        "virtualNode": NotRequired["VirtualNodeServiceProviderTypeDef"],
        "virtualRouter": NotRequired["VirtualRouterServiceProviderTypeDef"],
    },
)

VirtualServiceRefTypeDef = TypedDict(
    "VirtualServiceRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualServiceName": str,
    },
)

VirtualServiceSpecTypeDef = TypedDict(
    "VirtualServiceSpecTypeDef",
    {
        "provider": NotRequired["VirtualServiceProviderTypeDef"],
    },
)

VirtualServiceStatusTypeDef = TypedDict(
    "VirtualServiceStatusTypeDef",
    {
        "status": VirtualServiceStatusCodeType,
    },
)

WeightedTargetTypeDef = TypedDict(
    "WeightedTargetTypeDef",
    {
        "virtualNode": str,
        "weight": int,
    },
)
