"""
Type annotations for appflow service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef

    data: AggregationConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AggregationTypeType,
    AuthenticationTypeType,
    ConnectionModeType,
    ConnectorTypeType,
    DatadogConnectorOperatorType,
    DataPullModeType,
    DynatraceConnectorOperatorType,
    ExecutionStatusType,
    FileTypeType,
    FlowStatusType,
    GoogleAnalyticsConnectorOperatorType,
    InforNexusConnectorOperatorType,
    MarketoConnectorOperatorType,
    OAuth2GrantTypeType,
    OperatorPropertiesKeysType,
    OperatorsType,
    OperatorType,
    PrefixFormatType,
    PrefixTypeType,
    PrivateConnectionProvisioningFailureCauseType,
    PrivateConnectionProvisioningStatusType,
    S3ConnectorOperatorType,
    S3InputFileTypeType,
    SalesforceConnectorOperatorType,
    SAPODataConnectorOperatorType,
    ScheduleFrequencyTypeType,
    ServiceNowConnectorOperatorType,
    SingularConnectorOperatorType,
    SlackConnectorOperatorType,
    TaskTypeType,
    TrendmicroConnectorOperatorType,
    TriggerTypeType,
    VeevaConnectorOperatorType,
    WriteOperationTypeType,
    ZendeskConnectorOperatorType,
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
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ApiKeyCredentialsTypeDef",
    "AuthParameterTypeDef",
    "AuthenticationConfigTypeDef",
    "BasicAuthCredentialsTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorDetailTypeDef",
    "ConnectorEntityFieldTypeDef",
    "ConnectorEntityTypeDef",
    "ConnectorMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "ConnectorProfileConfigTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "ConnectorProfileTypeDef",
    "ConnectorProvisioningConfigTypeDef",
    "ConnectorRuntimeSettingTypeDef",
    "CreateConnectorProfileRequestRequestTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CustomAuthConfigTypeDef",
    "CustomAuthCredentialsTypeDef",
    "CustomConnectorDestinationPropertiesTypeDef",
    "CustomConnectorProfileCredentialsTypeDef",
    "CustomConnectorProfilePropertiesTypeDef",
    "CustomConnectorSourcePropertiesTypeDef",
    "CustomerProfilesDestinationPropertiesTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DeleteConnectorProfileRequestRequestTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DescribeConnectorEntityRequestRequestTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorProfilesRequestRequestTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeConnectorsRequestRequestTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeFlowExecutionRecordsRequestRequestTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "DestinationConnectorPropertiesTypeDef",
    "DestinationFieldPropertiesTypeDef",
    "DestinationFlowConfigTypeDef",
    "DynatraceConnectorProfileCredentialsTypeDef",
    "DynatraceConnectorProfilePropertiesTypeDef",
    "DynatraceSourcePropertiesTypeDef",
    "ErrorHandlingConfigTypeDef",
    "ErrorInfoTypeDef",
    "EventBridgeDestinationPropertiesTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionRecordTypeDef",
    "ExecutionResultTypeDef",
    "FieldTypeDetailsTypeDef",
    "FlowDefinitionTypeDef",
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    "GoogleAnalyticsMetadataTypeDef",
    "GoogleAnalyticsSourcePropertiesTypeDef",
    "HoneycodeConnectorProfileCredentialsTypeDef",
    "HoneycodeDestinationPropertiesTypeDef",
    "HoneycodeMetadataTypeDef",
    "IncrementalPullConfigTypeDef",
    "InforNexusConnectorProfileCredentialsTypeDef",
    "InforNexusConnectorProfilePropertiesTypeDef",
    "InforNexusSourcePropertiesTypeDef",
    "LambdaConnectorProvisioningConfigTypeDef",
    "ListConnectorEntitiesRequestRequestTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "MarketoDestinationPropertiesTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "OAuth2CredentialsTypeDef",
    "OAuth2DefaultsTypeDef",
    "OAuth2PropertiesTypeDef",
    "OAuthCredentialsTypeDef",
    "OAuthPropertiesTypeDef",
    "PrefixConfigTypeDef",
    "PrivateConnectionProvisioningStateTypeDef",
    "RangeTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "RegisterConnectorRequestRequestTypeDef",
    "RegisterConnectorResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationPropertiesTypeDef",
    "S3InputFormatConfigTypeDef",
    "S3OutputFormatConfigTypeDef",
    "S3SourcePropertiesTypeDef",
    "SAPODataConnectorProfileCredentialsTypeDef",
    "SAPODataConnectorProfilePropertiesTypeDef",
    "SAPODataDestinationPropertiesTypeDef",
    "SAPODataSourcePropertiesTypeDef",
    "SalesforceConnectorProfileCredentialsTypeDef",
    "SalesforceConnectorProfilePropertiesTypeDef",
    "SalesforceDestinationPropertiesTypeDef",
    "SalesforceMetadataTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "ServiceNowConnectorProfileCredentialsTypeDef",
    "ServiceNowConnectorProfilePropertiesTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SingularConnectorProfileCredentialsTypeDef",
    "SingularSourcePropertiesTypeDef",
    "SlackConnectorProfileCredentialsTypeDef",
    "SlackConnectorProfilePropertiesTypeDef",
    "SlackMetadataTypeDef",
    "SlackSourcePropertiesTypeDef",
    "SnowflakeConnectorProfileCredentialsTypeDef",
    "SnowflakeConnectorProfilePropertiesTypeDef",
    "SnowflakeDestinationPropertiesTypeDef",
    "SnowflakeMetadataTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFieldPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestRequestTypeDef",
    "StopFlowResponseTypeDef",
    "SuccessResponseHandlingConfigTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UnregisterConnectorRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectorProfileRequestRequestTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateFlowRequestRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "ZendeskDestinationPropertiesTypeDef",
    "ZendeskMetadataTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

AggregationConfigTypeDef = TypedDict(
    "AggregationConfigTypeDef",
    {
        "aggregationType": NotRequired[AggregationTypeType],
    },
)

AmplitudeConnectorProfileCredentialsTypeDef = TypedDict(
    "AmplitudeConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "secretKey": str,
    },
)

AmplitudeSourcePropertiesTypeDef = TypedDict(
    "AmplitudeSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ApiKeyCredentialsTypeDef = TypedDict(
    "ApiKeyCredentialsTypeDef",
    {
        "apiKey": str,
        "apiSecretKey": NotRequired[str],
    },
)

AuthParameterTypeDef = TypedDict(
    "AuthParameterTypeDef",
    {
        "key": NotRequired[str],
        "isRequired": NotRequired[bool],
        "label": NotRequired[str],
        "description": NotRequired[str],
        "isSensitiveField": NotRequired[bool],
        "connectorSuppliedValues": NotRequired[List[str]],
    },
)

AuthenticationConfigTypeDef = TypedDict(
    "AuthenticationConfigTypeDef",
    {
        "isBasicAuthSupported": NotRequired[bool],
        "isApiKeyAuthSupported": NotRequired[bool],
        "isOAuth2Supported": NotRequired[bool],
        "isCustomAuthSupported": NotRequired[bool],
        "oAuth2Defaults": NotRequired["OAuth2DefaultsTypeDef"],
        "customAuthConfigs": NotRequired[List["CustomAuthConfigTypeDef"]],
    },
)

BasicAuthCredentialsTypeDef = TypedDict(
    "BasicAuthCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

ConnectorConfigurationTypeDef = TypedDict(
    "ConnectorConfigurationTypeDef",
    {
        "canUseAsSource": NotRequired[bool],
        "canUseAsDestination": NotRequired[bool],
        "supportedDestinationConnectors": NotRequired[List[ConnectorTypeType]],
        "supportedSchedulingFrequencies": NotRequired[List[ScheduleFrequencyTypeType]],
        "isPrivateLinkEnabled": NotRequired[bool],
        "isPrivateLinkEndpointUrlRequired": NotRequired[bool],
        "supportedTriggerTypes": NotRequired[List[TriggerTypeType]],
        "connectorMetadata": NotRequired["ConnectorMetadataTypeDef"],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "connectorDescription": NotRequired[str],
        "connectorOwner": NotRequired[str],
        "connectorName": NotRequired[str],
        "connectorVersion": NotRequired[str],
        "connectorArn": NotRequired[str],
        "connectorModes": NotRequired[List[str]],
        "authenticationConfig": NotRequired["AuthenticationConfigTypeDef"],
        "connectorRuntimeSettings": NotRequired[List["ConnectorRuntimeSettingTypeDef"]],
        "supportedApiVersions": NotRequired[List[str]],
        "supportedOperators": NotRequired[List[OperatorsType]],
        "supportedWriteOperations": NotRequired[List[WriteOperationTypeType]],
        "connectorProvisioningType": NotRequired[Literal["LAMBDA"]],
        "connectorProvisioningConfig": NotRequired["ConnectorProvisioningConfigTypeDef"],
        "logoURL": NotRequired[str],
        "registeredAt": NotRequired[datetime],
        "registeredBy": NotRequired[str],
    },
)

ConnectorDetailTypeDef = TypedDict(
    "ConnectorDetailTypeDef",
    {
        "connectorDescription": NotRequired[str],
        "connectorName": NotRequired[str],
        "connectorOwner": NotRequired[str],
        "connectorVersion": NotRequired[str],
        "applicationType": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "registeredAt": NotRequired[datetime],
        "registeredBy": NotRequired[str],
        "connectorProvisioningType": NotRequired[Literal["LAMBDA"]],
        "connectorModes": NotRequired[List[str]],
    },
)

ConnectorEntityFieldTypeDef = TypedDict(
    "ConnectorEntityFieldTypeDef",
    {
        "identifier": str,
        "parentIdentifier": NotRequired[str],
        "label": NotRequired[str],
        "isPrimaryKey": NotRequired[bool],
        "defaultValue": NotRequired[str],
        "isDeprecated": NotRequired[bool],
        "supportedFieldTypeDetails": NotRequired["SupportedFieldTypeDetailsTypeDef"],
        "description": NotRequired[str],
        "sourceProperties": NotRequired["SourceFieldPropertiesTypeDef"],
        "destinationProperties": NotRequired["DestinationFieldPropertiesTypeDef"],
        "customProperties": NotRequired[Dict[str, str]],
    },
)

ConnectorEntityTypeDef = TypedDict(
    "ConnectorEntityTypeDef",
    {
        "name": str,
        "label": NotRequired[str],
        "hasNestedEntities": NotRequired[bool],
    },
)

ConnectorMetadataTypeDef = TypedDict(
    "ConnectorMetadataTypeDef",
    {
        "Amplitude": NotRequired[Dict[str, Any]],
        "Datadog": NotRequired[Dict[str, Any]],
        "Dynatrace": NotRequired[Dict[str, Any]],
        "GoogleAnalytics": NotRequired["GoogleAnalyticsMetadataTypeDef"],
        "InforNexus": NotRequired[Dict[str, Any]],
        "Marketo": NotRequired[Dict[str, Any]],
        "Redshift": NotRequired[Dict[str, Any]],
        "S3": NotRequired[Dict[str, Any]],
        "Salesforce": NotRequired["SalesforceMetadataTypeDef"],
        "ServiceNow": NotRequired[Dict[str, Any]],
        "Singular": NotRequired[Dict[str, Any]],
        "Slack": NotRequired["SlackMetadataTypeDef"],
        "Snowflake": NotRequired["SnowflakeMetadataTypeDef"],
        "Trendmicro": NotRequired[Dict[str, Any]],
        "Veeva": NotRequired[Dict[str, Any]],
        "Zendesk": NotRequired["ZendeskMetadataTypeDef"],
        "EventBridge": NotRequired[Dict[str, Any]],
        "Upsolver": NotRequired[Dict[str, Any]],
        "CustomerProfiles": NotRequired[Dict[str, Any]],
        "Honeycode": NotRequired["HoneycodeMetadataTypeDef"],
        "SAPOData": NotRequired[Dict[str, Any]],
    },
)

ConnectorOAuthRequestTypeDef = TypedDict(
    "ConnectorOAuthRequestTypeDef",
    {
        "authCode": NotRequired[str],
        "redirectUri": NotRequired[str],
    },
)

ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Amplitude": NotRequired[Literal["BETWEEN"]],
        "Datadog": NotRequired[DatadogConnectorOperatorType],
        "Dynatrace": NotRequired[DynatraceConnectorOperatorType],
        "GoogleAnalytics": NotRequired[GoogleAnalyticsConnectorOperatorType],
        "InforNexus": NotRequired[InforNexusConnectorOperatorType],
        "Marketo": NotRequired[MarketoConnectorOperatorType],
        "S3": NotRequired[S3ConnectorOperatorType],
        "Salesforce": NotRequired[SalesforceConnectorOperatorType],
        "ServiceNow": NotRequired[ServiceNowConnectorOperatorType],
        "Singular": NotRequired[SingularConnectorOperatorType],
        "Slack": NotRequired[SlackConnectorOperatorType],
        "Trendmicro": NotRequired[TrendmicroConnectorOperatorType],
        "Veeva": NotRequired[VeevaConnectorOperatorType],
        "Zendesk": NotRequired[ZendeskConnectorOperatorType],
        "SAPOData": NotRequired[SAPODataConnectorOperatorType],
        "CustomConnector": NotRequired[OperatorType],
    },
)

ConnectorProfileConfigTypeDef = TypedDict(
    "ConnectorProfileConfigTypeDef",
    {
        "connectorProfileProperties": "ConnectorProfilePropertiesTypeDef",
        "connectorProfileCredentials": "ConnectorProfileCredentialsTypeDef",
    },
)

ConnectorProfileCredentialsTypeDef = TypedDict(
    "ConnectorProfileCredentialsTypeDef",
    {
        "Amplitude": NotRequired["AmplitudeConnectorProfileCredentialsTypeDef"],
        "Datadog": NotRequired["DatadogConnectorProfileCredentialsTypeDef"],
        "Dynatrace": NotRequired["DynatraceConnectorProfileCredentialsTypeDef"],
        "GoogleAnalytics": NotRequired["GoogleAnalyticsConnectorProfileCredentialsTypeDef"],
        "Honeycode": NotRequired["HoneycodeConnectorProfileCredentialsTypeDef"],
        "InforNexus": NotRequired["InforNexusConnectorProfileCredentialsTypeDef"],
        "Marketo": NotRequired["MarketoConnectorProfileCredentialsTypeDef"],
        "Redshift": NotRequired["RedshiftConnectorProfileCredentialsTypeDef"],
        "Salesforce": NotRequired["SalesforceConnectorProfileCredentialsTypeDef"],
        "ServiceNow": NotRequired["ServiceNowConnectorProfileCredentialsTypeDef"],
        "Singular": NotRequired["SingularConnectorProfileCredentialsTypeDef"],
        "Slack": NotRequired["SlackConnectorProfileCredentialsTypeDef"],
        "Snowflake": NotRequired["SnowflakeConnectorProfileCredentialsTypeDef"],
        "Trendmicro": NotRequired["TrendmicroConnectorProfileCredentialsTypeDef"],
        "Veeva": NotRequired["VeevaConnectorProfileCredentialsTypeDef"],
        "Zendesk": NotRequired["ZendeskConnectorProfileCredentialsTypeDef"],
        "SAPOData": NotRequired["SAPODataConnectorProfileCredentialsTypeDef"],
        "CustomConnector": NotRequired["CustomConnectorProfileCredentialsTypeDef"],
    },
)

ConnectorProfilePropertiesTypeDef = TypedDict(
    "ConnectorProfilePropertiesTypeDef",
    {
        "Amplitude": NotRequired[Mapping[str, Any]],
        "Datadog": NotRequired["DatadogConnectorProfilePropertiesTypeDef"],
        "Dynatrace": NotRequired["DynatraceConnectorProfilePropertiesTypeDef"],
        "GoogleAnalytics": NotRequired[Mapping[str, Any]],
        "Honeycode": NotRequired[Mapping[str, Any]],
        "InforNexus": NotRequired["InforNexusConnectorProfilePropertiesTypeDef"],
        "Marketo": NotRequired["MarketoConnectorProfilePropertiesTypeDef"],
        "Redshift": NotRequired["RedshiftConnectorProfilePropertiesTypeDef"],
        "Salesforce": NotRequired["SalesforceConnectorProfilePropertiesTypeDef"],
        "ServiceNow": NotRequired["ServiceNowConnectorProfilePropertiesTypeDef"],
        "Singular": NotRequired[Mapping[str, Any]],
        "Slack": NotRequired["SlackConnectorProfilePropertiesTypeDef"],
        "Snowflake": NotRequired["SnowflakeConnectorProfilePropertiesTypeDef"],
        "Trendmicro": NotRequired[Mapping[str, Any]],
        "Veeva": NotRequired["VeevaConnectorProfilePropertiesTypeDef"],
        "Zendesk": NotRequired["ZendeskConnectorProfilePropertiesTypeDef"],
        "SAPOData": NotRequired["SAPODataConnectorProfilePropertiesTypeDef"],
        "CustomConnector": NotRequired["CustomConnectorProfilePropertiesTypeDef"],
    },
)

ConnectorProfileTypeDef = TypedDict(
    "ConnectorProfileTypeDef",
    {
        "connectorProfileArn": NotRequired[str],
        "connectorProfileName": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "connectionMode": NotRequired[ConnectionModeType],
        "credentialsArn": NotRequired[str],
        "connectorProfileProperties": NotRequired["ConnectorProfilePropertiesTypeDef"],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "privateConnectionProvisioningState": NotRequired[
            "PrivateConnectionProvisioningStateTypeDef"
        ],
    },
)

ConnectorProvisioningConfigTypeDef = TypedDict(
    "ConnectorProvisioningConfigTypeDef",
    {
        "lambda": NotRequired["LambdaConnectorProvisioningConfigTypeDef"],
    },
)

ConnectorRuntimeSettingTypeDef = TypedDict(
    "ConnectorRuntimeSettingTypeDef",
    {
        "key": NotRequired[str],
        "dataType": NotRequired[str],
        "isRequired": NotRequired[bool],
        "label": NotRequired[str],
        "description": NotRequired[str],
        "scope": NotRequired[str],
        "connectorSuppliedValueOptions": NotRequired[List[str]],
    },
)

CreateConnectorProfileRequestRequestTypeDef = TypedDict(
    "CreateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectorType": ConnectorTypeType,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": "ConnectorProfileConfigTypeDef",
        "kmsArn": NotRequired[str],
        "connectorLabel": NotRequired[str],
    },
)

CreateConnectorProfileResponseTypeDef = TypedDict(
    "CreateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFlowRequestRequestTypeDef = TypedDict(
    "CreateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": "TriggerConfigTypeDef",
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
        "destinationFlowConfigList": Sequence["DestinationFlowConfigTypeDef"],
        "tasks": Sequence["TaskTypeDef"],
        "description": NotRequired[str],
        "kmsArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAuthConfigTypeDef = TypedDict(
    "CustomAuthConfigTypeDef",
    {
        "customAuthenticationType": NotRequired[str],
        "authParameters": NotRequired[List["AuthParameterTypeDef"]],
    },
)

CustomAuthCredentialsTypeDef = TypedDict(
    "CustomAuthCredentialsTypeDef",
    {
        "customAuthenticationType": str,
        "credentialsMap": NotRequired[Mapping[str, str]],
    },
)

CustomConnectorDestinationPropertiesTypeDef = TypedDict(
    "CustomConnectorDestinationPropertiesTypeDef",
    {
        "entityName": str,
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
        "writeOperationType": NotRequired[WriteOperationTypeType],
        "idFieldNames": NotRequired[Sequence[str]],
        "customProperties": NotRequired[Mapping[str, str]],
    },
)

CustomConnectorProfileCredentialsTypeDef = TypedDict(
    "CustomConnectorProfileCredentialsTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "basic": NotRequired["BasicAuthCredentialsTypeDef"],
        "oauth2": NotRequired["OAuth2CredentialsTypeDef"],
        "apiKey": NotRequired["ApiKeyCredentialsTypeDef"],
        "custom": NotRequired["CustomAuthCredentialsTypeDef"],
    },
)

CustomConnectorProfilePropertiesTypeDef = TypedDict(
    "CustomConnectorProfilePropertiesTypeDef",
    {
        "profileProperties": NotRequired[Mapping[str, str]],
        "oAuth2Properties": NotRequired["OAuth2PropertiesTypeDef"],
    },
)

CustomConnectorSourcePropertiesTypeDef = TypedDict(
    "CustomConnectorSourcePropertiesTypeDef",
    {
        "entityName": str,
        "customProperties": NotRequired[Mapping[str, str]],
    },
)

CustomerProfilesDestinationPropertiesTypeDef = TypedDict(
    "CustomerProfilesDestinationPropertiesTypeDef",
    {
        "domainName": str,
        "objectTypeName": NotRequired[str],
    },
)

DatadogConnectorProfileCredentialsTypeDef = TypedDict(
    "DatadogConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
        "applicationKey": str,
    },
)

DatadogConnectorProfilePropertiesTypeDef = TypedDict(
    "DatadogConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

DatadogSourcePropertiesTypeDef = TypedDict(
    "DatadogSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

DeleteConnectorProfileRequestRequestTypeDef = TypedDict(
    "DeleteConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "forceDelete": NotRequired[bool],
    },
)

DeleteFlowRequestRequestTypeDef = TypedDict(
    "DeleteFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "forceDelete": NotRequired[bool],
    },
)

DescribeConnectorEntityRequestRequestTypeDef = TypedDict(
    "DescribeConnectorEntityRequestRequestTypeDef",
    {
        "connectorEntityName": str,
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorProfileName": NotRequired[str],
        "apiVersion": NotRequired[str],
    },
)

DescribeConnectorEntityResponseTypeDef = TypedDict(
    "DescribeConnectorEntityResponseTypeDef",
    {
        "connectorEntityFields": List["ConnectorEntityFieldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorProfilesRequestRequestTypeDef = TypedDict(
    "DescribeConnectorProfilesRequestRequestTypeDef",
    {
        "connectorProfileNames": NotRequired[Sequence[str]],
        "connectorType": NotRequired[ConnectorTypeType],
        "connectorLabel": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeConnectorProfilesResponseTypeDef = TypedDict(
    "DescribeConnectorProfilesResponseTypeDef",
    {
        "connectorProfileDetails": List["ConnectorProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "connectorLabel": NotRequired[str],
    },
)

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "connectorConfiguration": "ConnectorConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorsRequestRequestTypeDef = TypedDict(
    "DescribeConnectorsRequestRequestTypeDef",
    {
        "connectorTypes": NotRequired[Sequence[ConnectorTypeType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeConnectorsResponseTypeDef = TypedDict(
    "DescribeConnectorsResponseTypeDef",
    {
        "connectorConfigurations": Dict[ConnectorTypeType, "ConnectorConfigurationTypeDef"],
        "connectors": List["ConnectorDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowExecutionRecordsRequestRequestTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsRequestRequestTypeDef",
    {
        "flowName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeFlowExecutionRecordsResponseTypeDef = TypedDict(
    "DescribeFlowExecutionRecordsResponseTypeDef",
    {
        "flowExecutions": List["ExecutionRecordTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "flowArn": str,
        "description": str,
        "flowName": str,
        "kmsArn": str,
        "flowStatus": FlowStatusType,
        "flowStatusMessage": str,
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
        "destinationFlowConfigList": List["DestinationFlowConfigTypeDef"],
        "lastRunExecutionDetails": "ExecutionDetailsTypeDef",
        "triggerConfig": "TriggerConfigTypeDef",
        "tasks": List["TaskTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConnectorPropertiesTypeDef = TypedDict(
    "DestinationConnectorPropertiesTypeDef",
    {
        "Redshift": NotRequired["RedshiftDestinationPropertiesTypeDef"],
        "S3": NotRequired["S3DestinationPropertiesTypeDef"],
        "Salesforce": NotRequired["SalesforceDestinationPropertiesTypeDef"],
        "Snowflake": NotRequired["SnowflakeDestinationPropertiesTypeDef"],
        "EventBridge": NotRequired["EventBridgeDestinationPropertiesTypeDef"],
        "LookoutMetrics": NotRequired[Mapping[str, Any]],
        "Upsolver": NotRequired["UpsolverDestinationPropertiesTypeDef"],
        "Honeycode": NotRequired["HoneycodeDestinationPropertiesTypeDef"],
        "CustomerProfiles": NotRequired["CustomerProfilesDestinationPropertiesTypeDef"],
        "Zendesk": NotRequired["ZendeskDestinationPropertiesTypeDef"],
        "Marketo": NotRequired["MarketoDestinationPropertiesTypeDef"],
        "CustomConnector": NotRequired["CustomConnectorDestinationPropertiesTypeDef"],
        "SAPOData": NotRequired["SAPODataDestinationPropertiesTypeDef"],
    },
)

DestinationFieldPropertiesTypeDef = TypedDict(
    "DestinationFieldPropertiesTypeDef",
    {
        "isCreatable": NotRequired[bool],
        "isNullable": NotRequired[bool],
        "isUpsertable": NotRequired[bool],
        "isUpdatable": NotRequired[bool],
        "isDefaultedOnCreate": NotRequired[bool],
        "supportedWriteOperations": NotRequired[List[WriteOperationTypeType]],
    },
)

DestinationFlowConfigTypeDef = TypedDict(
    "DestinationFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "destinationConnectorProperties": "DestinationConnectorPropertiesTypeDef",
        "apiVersion": NotRequired[str],
        "connectorProfileName": NotRequired[str],
    },
)

DynatraceConnectorProfileCredentialsTypeDef = TypedDict(
    "DynatraceConnectorProfileCredentialsTypeDef",
    {
        "apiToken": str,
    },
)

DynatraceConnectorProfilePropertiesTypeDef = TypedDict(
    "DynatraceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

DynatraceSourcePropertiesTypeDef = TypedDict(
    "DynatraceSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

ErrorHandlingConfigTypeDef = TypedDict(
    "ErrorHandlingConfigTypeDef",
    {
        "failOnFirstDestinationError": NotRequired[bool],
        "bucketPrefix": NotRequired[str],
        "bucketName": NotRequired[str],
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "putFailuresCount": NotRequired[int],
        "executionMessage": NotRequired[str],
    },
)

EventBridgeDestinationPropertiesTypeDef = TypedDict(
    "EventBridgeDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
    },
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "mostRecentExecutionMessage": NotRequired[str],
        "mostRecentExecutionTime": NotRequired[datetime],
        "mostRecentExecutionStatus": NotRequired[ExecutionStatusType],
    },
)

ExecutionRecordTypeDef = TypedDict(
    "ExecutionRecordTypeDef",
    {
        "executionId": NotRequired[str],
        "executionStatus": NotRequired[ExecutionStatusType],
        "executionResult": NotRequired["ExecutionResultTypeDef"],
        "startedAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "dataPullStartTime": NotRequired[datetime],
        "dataPullEndTime": NotRequired[datetime],
    },
)

ExecutionResultTypeDef = TypedDict(
    "ExecutionResultTypeDef",
    {
        "errorInfo": NotRequired["ErrorInfoTypeDef"],
        "bytesProcessed": NotRequired[int],
        "bytesWritten": NotRequired[int],
        "recordsProcessed": NotRequired[int],
    },
)

FieldTypeDetailsTypeDef = TypedDict(
    "FieldTypeDetailsTypeDef",
    {
        "fieldType": str,
        "filterOperators": List[OperatorType],
        "supportedValues": NotRequired[List[str]],
        "valueRegexPattern": NotRequired[str],
        "supportedDateFormat": NotRequired[str],
        "fieldValueRange": NotRequired["RangeTypeDef"],
        "fieldLengthRange": NotRequired["RangeTypeDef"],
    },
)

FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "flowArn": NotRequired[str],
        "description": NotRequired[str],
        "flowName": NotRequired[str],
        "flowStatus": NotRequired[FlowStatusType],
        "sourceConnectorType": NotRequired[ConnectorTypeType],
        "sourceConnectorLabel": NotRequired[str],
        "destinationConnectorType": NotRequired[ConnectorTypeType],
        "destinationConnectorLabel": NotRequired[str],
        "triggerType": NotRequired[TriggerTypeType],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "lastRunExecutionDetails": NotRequired["ExecutionDetailsTypeDef"],
    },
)

GoogleAnalyticsConnectorProfileCredentialsTypeDef = TypedDict(
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

GoogleAnalyticsMetadataTypeDef = TypedDict(
    "GoogleAnalyticsMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

HoneycodeConnectorProfileCredentialsTypeDef = TypedDict(
    "HoneycodeConnectorProfileCredentialsTypeDef",
    {
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

HoneycodeDestinationPropertiesTypeDef = TypedDict(
    "HoneycodeDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
    },
)

HoneycodeMetadataTypeDef = TypedDict(
    "HoneycodeMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "datetimeTypeFieldName": NotRequired[str],
    },
)

InforNexusConnectorProfileCredentialsTypeDef = TypedDict(
    "InforNexusConnectorProfileCredentialsTypeDef",
    {
        "accessKeyId": str,
        "userId": str,
        "secretAccessKey": str,
        "datakey": str,
    },
)

InforNexusConnectorProfilePropertiesTypeDef = TypedDict(
    "InforNexusConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

InforNexusSourcePropertiesTypeDef = TypedDict(
    "InforNexusSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

LambdaConnectorProvisioningConfigTypeDef = TypedDict(
    "LambdaConnectorProvisioningConfigTypeDef",
    {
        "lambdaArn": str,
    },
)

ListConnectorEntitiesRequestRequestTypeDef = TypedDict(
    "ListConnectorEntitiesRequestRequestTypeDef",
    {
        "connectorProfileName": NotRequired[str],
        "connectorType": NotRequired[ConnectorTypeType],
        "entitiesPath": NotRequired[str],
        "apiVersion": NotRequired[str],
    },
)

ListConnectorEntitiesResponseTypeDef = TypedDict(
    "ListConnectorEntitiesResponseTypeDef",
    {
        "connectorEntityMap": Dict[str, List["ConnectorEntityTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List["ConnectorDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "flows": List["FlowDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MarketoConnectorProfileCredentialsTypeDef = TypedDict(
    "MarketoConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

MarketoConnectorProfilePropertiesTypeDef = TypedDict(
    "MarketoConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

MarketoDestinationPropertiesTypeDef = TypedDict(
    "MarketoDestinationPropertiesTypeDef",
    {
        "object": str,
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
    },
)

MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

OAuth2CredentialsTypeDef = TypedDict(
    "OAuth2CredentialsTypeDef",
    {
        "clientId": NotRequired[str],
        "clientSecret": NotRequired[str],
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

OAuth2DefaultsTypeDef = TypedDict(
    "OAuth2DefaultsTypeDef",
    {
        "oauthScopes": NotRequired[List[str]],
        "tokenUrls": NotRequired[List[str]],
        "authCodeUrls": NotRequired[List[str]],
        "oauth2GrantTypesSupported": NotRequired[List[OAuth2GrantTypeType]],
    },
)

OAuth2PropertiesTypeDef = TypedDict(
    "OAuth2PropertiesTypeDef",
    {
        "tokenUrl": str,
        "oAuth2GrantType": OAuth2GrantTypeType,
    },
)

OAuthCredentialsTypeDef = TypedDict(
    "OAuthCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

OAuthPropertiesTypeDef = TypedDict(
    "OAuthPropertiesTypeDef",
    {
        "tokenUrl": str,
        "authCodeUrl": str,
        "oAuthScopes": Sequence[str],
    },
)

PrefixConfigTypeDef = TypedDict(
    "PrefixConfigTypeDef",
    {
        "prefixType": NotRequired[PrefixTypeType],
        "prefixFormat": NotRequired[PrefixFormatType],
    },
)

PrivateConnectionProvisioningStateTypeDef = TypedDict(
    "PrivateConnectionProvisioningStateTypeDef",
    {
        "status": NotRequired[PrivateConnectionProvisioningStatusType],
        "failureMessage": NotRequired[str],
        "failureCause": NotRequired[PrivateConnectionProvisioningFailureCauseType],
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "maximum": NotRequired[float],
        "minimum": NotRequired[float],
    },
)

RedshiftConnectorProfileCredentialsTypeDef = TypedDict(
    "RedshiftConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

RedshiftConnectorProfilePropertiesTypeDef = TypedDict(
    "RedshiftConnectorProfilePropertiesTypeDef",
    {
        "databaseUrl": str,
        "bucketName": str,
        "roleArn": str,
        "bucketPrefix": NotRequired[str],
    },
)

RedshiftDestinationPropertiesTypeDef = TypedDict(
    "RedshiftDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
        "bucketPrefix": NotRequired[str],
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
    },
)

RegisterConnectorRequestRequestTypeDef = TypedDict(
    "RegisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": NotRequired[str],
        "description": NotRequired[str],
        "connectorProvisioningType": NotRequired[Literal["LAMBDA"]],
        "connectorProvisioningConfig": NotRequired["ConnectorProvisioningConfigTypeDef"],
    },
)

RegisterConnectorResponseTypeDef = TypedDict(
    "RegisterConnectorResponseTypeDef",
    {
        "connectorArn": str,
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

S3DestinationPropertiesTypeDef = TypedDict(
    "S3DestinationPropertiesTypeDef",
    {
        "bucketName": str,
        "bucketPrefix": NotRequired[str],
        "s3OutputFormatConfig": NotRequired["S3OutputFormatConfigTypeDef"],
    },
)

S3InputFormatConfigTypeDef = TypedDict(
    "S3InputFormatConfigTypeDef",
    {
        "s3InputFileType": NotRequired[S3InputFileTypeType],
    },
)

S3OutputFormatConfigTypeDef = TypedDict(
    "S3OutputFormatConfigTypeDef",
    {
        "fileType": NotRequired[FileTypeType],
        "prefixConfig": NotRequired["PrefixConfigTypeDef"],
        "aggregationConfig": NotRequired["AggregationConfigTypeDef"],
    },
)

S3SourcePropertiesTypeDef = TypedDict(
    "S3SourcePropertiesTypeDef",
    {
        "bucketName": str,
        "bucketPrefix": NotRequired[str],
        "s3InputFormatConfig": NotRequired["S3InputFormatConfigTypeDef"],
    },
)

SAPODataConnectorProfileCredentialsTypeDef = TypedDict(
    "SAPODataConnectorProfileCredentialsTypeDef",
    {
        "basicAuthCredentials": NotRequired["BasicAuthCredentialsTypeDef"],
        "oAuthCredentials": NotRequired["OAuthCredentialsTypeDef"],
    },
)

SAPODataConnectorProfilePropertiesTypeDef = TypedDict(
    "SAPODataConnectorProfilePropertiesTypeDef",
    {
        "applicationHostUrl": str,
        "applicationServicePath": str,
        "portNumber": int,
        "clientNumber": str,
        "logonLanguage": NotRequired[str],
        "privateLinkServiceName": NotRequired[str],
        "oAuthProperties": NotRequired["OAuthPropertiesTypeDef"],
    },
)

SAPODataDestinationPropertiesTypeDef = TypedDict(
    "SAPODataDestinationPropertiesTypeDef",
    {
        "objectPath": str,
        "successResponseHandlingConfig": NotRequired["SuccessResponseHandlingConfigTypeDef"],
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)

SAPODataSourcePropertiesTypeDef = TypedDict(
    "SAPODataSourcePropertiesTypeDef",
    {
        "objectPath": NotRequired[str],
    },
)

SalesforceConnectorProfileCredentialsTypeDef = TypedDict(
    "SalesforceConnectorProfileCredentialsTypeDef",
    {
        "accessToken": NotRequired[str],
        "refreshToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
        "clientCredentialsArn": NotRequired[str],
    },
)

SalesforceConnectorProfilePropertiesTypeDef = TypedDict(
    "SalesforceConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": NotRequired[str],
        "isSandboxEnvironment": NotRequired[bool],
    },
)

SalesforceDestinationPropertiesTypeDef = TypedDict(
    "SalesforceDestinationPropertiesTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)

SalesforceMetadataTypeDef = TypedDict(
    "SalesforceMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

SalesforceSourcePropertiesTypeDef = TypedDict(
    "SalesforceSourcePropertiesTypeDef",
    {
        "object": str,
        "enableDynamicFieldUpdate": NotRequired[bool],
        "includeDeletedRecords": NotRequired[bool],
    },
)

ScheduledTriggerPropertiesTypeDef = TypedDict(
    "ScheduledTriggerPropertiesTypeDef",
    {
        "scheduleExpression": str,
        "dataPullMode": NotRequired[DataPullModeType],
        "scheduleStartTime": NotRequired[Union[datetime, str]],
        "scheduleEndTime": NotRequired[Union[datetime, str]],
        "timezone": NotRequired[str],
        "scheduleOffset": NotRequired[int],
        "firstExecutionFrom": NotRequired[Union[datetime, str]],
    },
)

ServiceNowConnectorProfileCredentialsTypeDef = TypedDict(
    "ServiceNowConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

ServiceNowConnectorProfilePropertiesTypeDef = TypedDict(
    "ServiceNowConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SingularConnectorProfileCredentialsTypeDef = TypedDict(
    "SingularConnectorProfileCredentialsTypeDef",
    {
        "apiKey": str,
    },
)

SingularSourcePropertiesTypeDef = TypedDict(
    "SingularSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SlackConnectorProfileCredentialsTypeDef = TypedDict(
    "SlackConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

SlackConnectorProfilePropertiesTypeDef = TypedDict(
    "SlackConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

SlackMetadataTypeDef = TypedDict(
    "SlackMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

SlackSourcePropertiesTypeDef = TypedDict(
    "SlackSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

SnowflakeConnectorProfileCredentialsTypeDef = TypedDict(
    "SnowflakeConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

SnowflakeConnectorProfilePropertiesTypeDef = TypedDict(
    "SnowflakeConnectorProfilePropertiesTypeDef",
    {
        "warehouse": str,
        "stage": str,
        "bucketName": str,
        "bucketPrefix": NotRequired[str],
        "privateLinkServiceName": NotRequired[str],
        "accountName": NotRequired[str],
        "region": NotRequired[str],
    },
)

SnowflakeDestinationPropertiesTypeDef = TypedDict(
    "SnowflakeDestinationPropertiesTypeDef",
    {
        "object": str,
        "intermediateBucketName": str,
        "bucketPrefix": NotRequired[str],
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
    },
)

SnowflakeMetadataTypeDef = TypedDict(
    "SnowflakeMetadataTypeDef",
    {
        "supportedRegions": NotRequired[List[str]],
    },
)

SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Amplitude": NotRequired["AmplitudeSourcePropertiesTypeDef"],
        "Datadog": NotRequired["DatadogSourcePropertiesTypeDef"],
        "Dynatrace": NotRequired["DynatraceSourcePropertiesTypeDef"],
        "GoogleAnalytics": NotRequired["GoogleAnalyticsSourcePropertiesTypeDef"],
        "InforNexus": NotRequired["InforNexusSourcePropertiesTypeDef"],
        "Marketo": NotRequired["MarketoSourcePropertiesTypeDef"],
        "S3": NotRequired["S3SourcePropertiesTypeDef"],
        "Salesforce": NotRequired["SalesforceSourcePropertiesTypeDef"],
        "ServiceNow": NotRequired["ServiceNowSourcePropertiesTypeDef"],
        "Singular": NotRequired["SingularSourcePropertiesTypeDef"],
        "Slack": NotRequired["SlackSourcePropertiesTypeDef"],
        "Trendmicro": NotRequired["TrendmicroSourcePropertiesTypeDef"],
        "Veeva": NotRequired["VeevaSourcePropertiesTypeDef"],
        "Zendesk": NotRequired["ZendeskSourcePropertiesTypeDef"],
        "SAPOData": NotRequired["SAPODataSourcePropertiesTypeDef"],
        "CustomConnector": NotRequired["CustomConnectorSourcePropertiesTypeDef"],
    },
)

SourceFieldPropertiesTypeDef = TypedDict(
    "SourceFieldPropertiesTypeDef",
    {
        "isRetrievable": NotRequired[bool],
        "isQueryable": NotRequired[bool],
        "isTimestampFieldForIncrementalQueries": NotRequired[bool],
    },
)

SourceFlowConfigTypeDef = TypedDict(
    "SourceFlowConfigTypeDef",
    {
        "connectorType": ConnectorTypeType,
        "sourceConnectorProperties": "SourceConnectorPropertiesTypeDef",
        "apiVersion": NotRequired[str],
        "connectorProfileName": NotRequired[str],
        "incrementalPullConfig": NotRequired["IncrementalPullConfigTypeDef"],
    },
)

StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "executionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "flowName": str,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "flowArn": str,
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuccessResponseHandlingConfigTypeDef = TypedDict(
    "SuccessResponseHandlingConfigTypeDef",
    {
        "bucketPrefix": NotRequired[str],
        "bucketName": NotRequired[str],
    },
)

SupportedFieldTypeDetailsTypeDef = TypedDict(
    "SupportedFieldTypeDetailsTypeDef",
    {
        "v1": "FieldTypeDetailsTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "sourceFields": Sequence[str],
        "taskType": TaskTypeType,
        "connectorOperator": NotRequired["ConnectorOperatorTypeDef"],
        "destinationField": NotRequired[str],
        "taskProperties": NotRequired[Mapping[OperatorPropertiesKeysType, str]],
    },
)

TrendmicroConnectorProfileCredentialsTypeDef = TypedDict(
    "TrendmicroConnectorProfileCredentialsTypeDef",
    {
        "apiSecretKey": str,
    },
)

TrendmicroSourcePropertiesTypeDef = TypedDict(
    "TrendmicroSourcePropertiesTypeDef",
    {
        "object": str,
    },
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "triggerType": TriggerTypeType,
        "triggerProperties": NotRequired["TriggerPropertiesTypeDef"],
    },
)

TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": NotRequired["ScheduledTriggerPropertiesTypeDef"],
    },
)

UnregisterConnectorRequestRequestTypeDef = TypedDict(
    "UnregisterConnectorRequestRequestTypeDef",
    {
        "connectorLabel": str,
        "forceDelete": NotRequired[bool],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateConnectorProfileRequestRequestTypeDef = TypedDict(
    "UpdateConnectorProfileRequestRequestTypeDef",
    {
        "connectorProfileName": str,
        "connectionMode": ConnectionModeType,
        "connectorProfileConfig": "ConnectorProfileConfigTypeDef",
    },
)

UpdateConnectorProfileResponseTypeDef = TypedDict(
    "UpdateConnectorProfileResponseTypeDef",
    {
        "connectorProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFlowRequestRequestTypeDef = TypedDict(
    "UpdateFlowRequestRequestTypeDef",
    {
        "flowName": str,
        "triggerConfig": "TriggerConfigTypeDef",
        "sourceFlowConfig": "SourceFlowConfigTypeDef",
        "destinationFlowConfigList": Sequence["DestinationFlowConfigTypeDef"],
        "tasks": Sequence["TaskTypeDef"],
        "description": NotRequired[str],
    },
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "flowStatus": FlowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpsolverDestinationPropertiesTypeDef = TypedDict(
    "UpsolverDestinationPropertiesTypeDef",
    {
        "bucketName": str,
        "s3OutputFormatConfig": "UpsolverS3OutputFormatConfigTypeDef",
        "bucketPrefix": NotRequired[str],
    },
)

UpsolverS3OutputFormatConfigTypeDef = TypedDict(
    "UpsolverS3OutputFormatConfigTypeDef",
    {
        "prefixConfig": "PrefixConfigTypeDef",
        "fileType": NotRequired[FileTypeType],
        "aggregationConfig": NotRequired["AggregationConfigTypeDef"],
    },
)

VeevaConnectorProfileCredentialsTypeDef = TypedDict(
    "VeevaConnectorProfileCredentialsTypeDef",
    {
        "username": str,
        "password": str,
    },
)

VeevaConnectorProfilePropertiesTypeDef = TypedDict(
    "VeevaConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

VeevaSourcePropertiesTypeDef = TypedDict(
    "VeevaSourcePropertiesTypeDef",
    {
        "object": str,
        "documentType": NotRequired[str],
        "includeSourceFiles": NotRequired[bool],
        "includeRenditions": NotRequired[bool],
        "includeAllVersions": NotRequired[bool],
    },
)

ZendeskConnectorProfileCredentialsTypeDef = TypedDict(
    "ZendeskConnectorProfileCredentialsTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "accessToken": NotRequired[str],
        "oAuthRequest": NotRequired["ConnectorOAuthRequestTypeDef"],
    },
)

ZendeskConnectorProfilePropertiesTypeDef = TypedDict(
    "ZendeskConnectorProfilePropertiesTypeDef",
    {
        "instanceUrl": str,
    },
)

ZendeskDestinationPropertiesTypeDef = TypedDict(
    "ZendeskDestinationPropertiesTypeDef",
    {
        "object": str,
        "idFieldNames": NotRequired[Sequence[str]],
        "errorHandlingConfig": NotRequired["ErrorHandlingConfigTypeDef"],
        "writeOperationType": NotRequired[WriteOperationTypeType],
    },
)

ZendeskMetadataTypeDef = TypedDict(
    "ZendeskMetadataTypeDef",
    {
        "oAuthScopes": NotRequired[List[str]],
    },
)

ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "object": str,
    },
)
