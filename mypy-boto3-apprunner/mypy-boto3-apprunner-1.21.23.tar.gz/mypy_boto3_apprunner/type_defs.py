"""
Type annotations for apprunner service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apprunner/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apprunner.type_defs import AssociateCustomDomainRequestRequestTypeDef

    data: AssociateCustomDomainRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AutoScalingConfigurationStatusType,
    CertificateValidationRecordStatusType,
    ConfigurationSourceType,
    ConnectionStatusType,
    CustomDomainAssociationStatusType,
    EgressTypeType,
    HealthCheckProtocolType,
    ImageRepositoryTypeType,
    OperationStatusType,
    OperationTypeType,
    RuntimeType,
    ServiceStatusType,
    VpcConnectorStatusType,
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
    "AssociateCustomDomainRequestRequestTypeDef",
    "AssociateCustomDomainResponseTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AutoScalingConfigurationSummaryTypeDef",
    "AutoScalingConfigurationTypeDef",
    "CertificateValidationRecordTypeDef",
    "CodeConfigurationTypeDef",
    "CodeConfigurationValuesTypeDef",
    "CodeRepositoryTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "CreateAutoScalingConfigurationRequestRequestTypeDef",
    "CreateAutoScalingConfigurationResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateVpcConnectorRequestRequestTypeDef",
    "CreateVpcConnectorResponseTypeDef",
    "CustomDomainTypeDef",
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    "DeleteAutoScalingConfigurationResponseTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteVpcConnectorRequestRequestTypeDef",
    "DeleteVpcConnectorResponseTypeDef",
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    "DescribeAutoScalingConfigurationResponseTypeDef",
    "DescribeCustomDomainsRequestRequestTypeDef",
    "DescribeCustomDomainsResponseTypeDef",
    "DescribeServiceRequestRequestTypeDef",
    "DescribeServiceResponseTypeDef",
    "DescribeVpcConnectorRequestRequestTypeDef",
    "DescribeVpcConnectorResponseTypeDef",
    "DisassociateCustomDomainRequestRequestTypeDef",
    "DisassociateCustomDomainResponseTypeDef",
    "EgressConfigurationTypeDef",
    "EncryptionConfigurationTypeDef",
    "HealthCheckConfigurationTypeDef",
    "ImageConfigurationTypeDef",
    "ImageRepositoryTypeDef",
    "InstanceConfigurationTypeDef",
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    "ListAutoScalingConfigurationsResponseTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVpcConnectorsRequestRequestTypeDef",
    "ListVpcConnectorsResponseTypeDef",
    "NetworkConfigurationTypeDef",
    "OperationSummaryTypeDef",
    "PauseServiceRequestRequestTypeDef",
    "PauseServiceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeServiceRequestRequestTypeDef",
    "ResumeServiceResponseTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "SourceCodeVersionTypeDef",
    "SourceConfigurationTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StartDeploymentResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "VpcConnectorTypeDef",
)

AssociateCustomDomainRequestRequestTypeDef = TypedDict(
    "AssociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
        "EnableWWWSubdomain": NotRequired[bool],
    },
)

AssociateCustomDomainResponseTypeDef = TypedDict(
    "AssociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "ConnectionArn": NotRequired[str],
        "AccessRoleArn": NotRequired[str],
    },
)

AutoScalingConfigurationSummaryTypeDef = TypedDict(
    "AutoScalingConfigurationSummaryTypeDef",
    {
        "AutoScalingConfigurationArn": NotRequired[str],
        "AutoScalingConfigurationName": NotRequired[str],
        "AutoScalingConfigurationRevision": NotRequired[int],
    },
)

AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "AutoScalingConfigurationArn": NotRequired[str],
        "AutoScalingConfigurationName": NotRequired[str],
        "AutoScalingConfigurationRevision": NotRequired[int],
        "Latest": NotRequired[bool],
        "Status": NotRequired[AutoScalingConfigurationStatusType],
        "MaxConcurrency": NotRequired[int],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "DeletedAt": NotRequired[datetime],
    },
)

CertificateValidationRecordTypeDef = TypedDict(
    "CertificateValidationRecordTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
        "Status": NotRequired[CertificateValidationRecordStatusType],
    },
)

CodeConfigurationTypeDef = TypedDict(
    "CodeConfigurationTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
        "CodeConfigurationValues": NotRequired["CodeConfigurationValuesTypeDef"],
    },
)

CodeConfigurationValuesTypeDef = TypedDict(
    "CodeConfigurationValuesTypeDef",
    {
        "Runtime": RuntimeType,
        "BuildCommand": NotRequired[str],
        "StartCommand": NotRequired[str],
        "Port": NotRequired[str],
        "RuntimeEnvironmentVariables": NotRequired[Mapping[str, str]],
    },
)

CodeRepositoryTypeDef = TypedDict(
    "CodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": "SourceCodeVersionTypeDef",
        "CodeConfiguration": NotRequired["CodeConfigurationTypeDef"],
    },
)

ConnectionSummaryTypeDef = TypedDict(
    "ConnectionSummaryTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "ProviderType": NotRequired[Literal["GITHUB"]],
        "Status": NotRequired[ConnectionStatusType],
        "CreatedAt": NotRequired[datetime],
    },
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "ProviderType": NotRequired[Literal["GITHUB"]],
        "Status": NotRequired[ConnectionStatusType],
        "CreatedAt": NotRequired[datetime],
    },
)

CreateAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "CreateAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
        "MaxConcurrency": NotRequired[int],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAutoScalingConfigurationResponseTypeDef = TypedDict(
    "CreateAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "ProviderType": Literal["GITHUB"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "ServiceName": str,
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "InstanceConfiguration": NotRequired["InstanceConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "HealthCheckConfiguration": NotRequired["HealthCheckConfigurationTypeDef"],
        "AutoScalingConfigurationArn": NotRequired[str],
        "NetworkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
    },
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcConnectorRequestRequestTypeDef = TypedDict(
    "CreateVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorName": str,
        "Subnets": Sequence[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateVpcConnectorResponseTypeDef = TypedDict(
    "CreateVpcConnectorResponseTypeDef",
    {
        "VpcConnector": "VpcConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDomainTypeDef = TypedDict(
    "CustomDomainTypeDef",
    {
        "DomainName": str,
        "EnableWWWSubdomain": bool,
        "Status": CustomDomainAssociationStatusType,
        "CertificateValidationRecords": NotRequired[List["CertificateValidationRecordTypeDef"]],
    },
)

DeleteAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

DeleteAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)

DeleteVpcConnectorResponseTypeDef = TypedDict(
    "DeleteVpcConnectorResponseTypeDef",
    {
        "VpcConnector": "VpcConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)

DescribeAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": "AutoScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomDomainsRequestRequestTypeDef = TypedDict(
    "DescribeCustomDomainsRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeCustomDomainsResponseTypeDef = TypedDict(
    "DescribeCustomDomainsResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomains": List["CustomDomainTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceRequestRequestTypeDef = TypedDict(
    "DescribeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

DescribeServiceResponseTypeDef = TypedDict(
    "DescribeServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcConnectorRequestRequestTypeDef = TypedDict(
    "DescribeVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)

DescribeVpcConnectorResponseTypeDef = TypedDict(
    "DescribeVpcConnectorResponseTypeDef",
    {
        "VpcConnector": "VpcConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCustomDomainRequestRequestTypeDef = TypedDict(
    "DisassociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)

DisassociateCustomDomainResponseTypeDef = TypedDict(
    "DisassociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": "CustomDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EgressConfigurationTypeDef = TypedDict(
    "EgressConfigurationTypeDef",
    {
        "EgressType": NotRequired[EgressTypeType],
        "VpcConnectorArn": NotRequired[str],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)

HealthCheckConfigurationTypeDef = TypedDict(
    "HealthCheckConfigurationTypeDef",
    {
        "Protocol": NotRequired[HealthCheckProtocolType],
        "Path": NotRequired[str],
        "Interval": NotRequired[int],
        "Timeout": NotRequired[int],
        "HealthyThreshold": NotRequired[int],
        "UnhealthyThreshold": NotRequired[int],
    },
)

ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "RuntimeEnvironmentVariables": NotRequired[Mapping[str, str]],
        "StartCommand": NotRequired[str],
        "Port": NotRequired[str],
    },
)

ImageRepositoryTypeDef = TypedDict(
    "ImageRepositoryTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
        "ImageConfiguration": NotRequired["ImageConfigurationTypeDef"],
    },
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "Cpu": NotRequired[str],
        "Memory": NotRequired[str],
        "InstanceRoleArn": NotRequired[str],
    },
)

ListAutoScalingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": NotRequired[str],
        "LatestOnly": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAutoScalingConfigurationsResponseTypeDef = TypedDict(
    "ListAutoScalingConfigurationsResponseTypeDef",
    {
        "AutoScalingConfigurationSummaryList": List["AutoScalingConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "ConnectionSummaryList": List["ConnectionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "OperationSummaryList": List["OperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "ServiceSummaryList": List["ServiceSummaryTypeDef"],
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

ListVpcConnectorsRequestRequestTypeDef = TypedDict(
    "ListVpcConnectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListVpcConnectorsResponseTypeDef = TypedDict(
    "ListVpcConnectorsResponseTypeDef",
    {
        "VpcConnectors": List["VpcConnectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "EgressConfiguration": NotRequired["EgressConfigurationTypeDef"],
    },
)

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[OperationTypeType],
        "Status": NotRequired[OperationStatusType],
        "TargetArn": NotRequired[str],
        "StartedAt": NotRequired[datetime],
        "EndedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

PauseServiceRequestRequestTypeDef = TypedDict(
    "PauseServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

PauseServiceResponseTypeDef = TypedDict(
    "PauseServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
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

ResumeServiceRequestRequestTypeDef = TypedDict(
    "ResumeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

ResumeServiceResponseTypeDef = TypedDict(
    "ResumeServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ServiceName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceUrl": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Status": NotRequired[ServiceStatusType],
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "ServiceUrl": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "InstanceConfiguration": "InstanceConfigurationTypeDef",
        "AutoScalingConfigurationSummary": "AutoScalingConfigurationSummaryTypeDef",
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "DeletedAt": NotRequired[datetime],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "HealthCheckConfiguration": NotRequired["HealthCheckConfigurationTypeDef"],
    },
)

SourceCodeVersionTypeDef = TypedDict(
    "SourceCodeVersionTypeDef",
    {
        "Type": Literal["BRANCH"],
        "Value": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "CodeRepository": NotRequired["CodeRepositoryTypeDef"],
        "ImageRepository": NotRequired["ImageRepositoryTypeDef"],
        "AutoDeploymentsEnabled": NotRequired[bool],
        "AuthenticationConfiguration": NotRequired["AuthenticationConfigurationTypeDef"],
    },
)

StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)

StartDeploymentResponseTypeDef = TypedDict(
    "StartDeploymentResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "SourceConfiguration": NotRequired["SourceConfigurationTypeDef"],
        "InstanceConfiguration": NotRequired["InstanceConfigurationTypeDef"],
        "AutoScalingConfigurationArn": NotRequired[str],
        "HealthCheckConfiguration": NotRequired["HealthCheckConfigurationTypeDef"],
        "NetworkConfiguration": NotRequired["NetworkConfigurationTypeDef"],
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConnectorTypeDef = TypedDict(
    "VpcConnectorTypeDef",
    {
        "VpcConnectorName": NotRequired[str],
        "VpcConnectorArn": NotRequired[str],
        "VpcConnectorRevision": NotRequired[int],
        "Subnets": NotRequired[List[str]],
        "SecurityGroups": NotRequired[List[str]],
        "Status": NotRequired[VpcConnectorStatusType],
        "CreatedAt": NotRequired[datetime],
        "DeletedAt": NotRequired[datetime],
    },
)
