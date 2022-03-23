"""
Type annotations for appsync service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_appsync/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_appsync.type_defs import AdditionalAuthenticationProviderTypeDef

    data: AdditionalAuthenticationProviderTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ApiCacheStatusType,
    ApiCacheTypeType,
    ApiCachingBehaviorType,
    AssociationStatusType,
    AuthenticationTypeType,
    ConflictDetectionTypeType,
    ConflictHandlerTypeType,
    DataSourceTypeType,
    DefaultActionType,
    FieldLogLevelType,
    OutputTypeType,
    ResolverKindType,
    SchemaStatusType,
    TypeDefinitionFormatType,
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
    "AdditionalAuthenticationProviderTypeDef",
    "ApiAssociationTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AssociateApiRequestRequestTypeDef",
    "AssociateApiResponseTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "CreateApiCacheRequestRequestTypeDef",
    "CreateApiCacheResponseTypeDef",
    "CreateApiKeyRequestRequestTypeDef",
    "CreateApiKeyResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
    "CreateDomainNameResponseTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "CreateFunctionResponseTypeDef",
    "CreateGraphqlApiRequestRequestTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "CreateResolverRequestRequestTypeDef",
    "CreateResolverResponseTypeDef",
    "CreateTypeRequestRequestTypeDef",
    "CreateTypeResponseTypeDef",
    "DataSourceTypeDef",
    "DeleteApiCacheRequestRequestTypeDef",
    "DeleteApiKeyRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteGraphqlApiRequestRequestTypeDef",
    "DeleteResolverRequestRequestTypeDef",
    "DeleteTypeRequestRequestTypeDef",
    "DeltaSyncConfigTypeDef",
    "DisassociateApiRequestRequestTypeDef",
    "DomainNameConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "FlushApiCacheRequestRequestTypeDef",
    "FunctionConfigurationTypeDef",
    "GetApiAssociationRequestRequestTypeDef",
    "GetApiAssociationResponseTypeDef",
    "GetApiCacheRequestRequestTypeDef",
    "GetApiCacheResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetDomainNameResponseTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResponseTypeDef",
    "GetGraphqlApiRequestRequestTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "GetIntrospectionSchemaRequestRequestTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverRequestRequestTypeDef",
    "GetResolverResponseTypeDef",
    "GetSchemaCreationStatusRequestRequestTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetTypeRequestRequestTypeDef",
    "GetTypeResponseTypeDef",
    "GraphqlApiTypeDef",
    "HttpDataSourceConfigTypeDef",
    "LambdaAuthorizerConfigTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "ListApiKeysRequestRequestTypeDef",
    "ListApiKeysResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListDomainNamesRequestRequestTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListGraphqlApisRequestRequestTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "ListResolversByFunctionRequestRequestTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversRequestRequestTypeDef",
    "ListResolversResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesRequestRequestTypeDef",
    "ListTypesResponseTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "OpenSearchServiceDataSourceConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "ResponseMetadataTypeDef",
    "StartSchemaCreationRequestRequestTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "SyncConfigTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiCacheRequestRequestTypeDef",
    "UpdateApiCacheResponseTypeDef",
    "UpdateApiKeyRequestRequestTypeDef",
    "UpdateApiKeyResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateDomainNameRequestRequestTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "UpdateFunctionRequestRequestTypeDef",
    "UpdateFunctionResponseTypeDef",
    "UpdateGraphqlApiRequestRequestTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "UpdateResolverRequestRequestTypeDef",
    "UpdateResolverResponseTypeDef",
    "UpdateTypeRequestRequestTypeDef",
    "UpdateTypeResponseTypeDef",
    "UserPoolConfigTypeDef",
)

AdditionalAuthenticationProviderTypeDef = TypedDict(
    "AdditionalAuthenticationProviderTypeDef",
    {
        "authenticationType": NotRequired[AuthenticationTypeType],
        "openIDConnectConfig": NotRequired["OpenIDConnectConfigTypeDef"],
        "userPoolConfig": NotRequired["CognitoUserPoolConfigTypeDef"],
        "lambdaAuthorizerConfig": NotRequired["LambdaAuthorizerConfigTypeDef"],
    },
)

ApiAssociationTypeDef = TypedDict(
    "ApiAssociationTypeDef",
    {
        "domainName": NotRequired[str],
        "apiId": NotRequired[str],
        "associationStatus": NotRequired[AssociationStatusType],
        "deploymentDetail": NotRequired[str],
    },
)

ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": NotRequired[int],
        "apiCachingBehavior": NotRequired[ApiCachingBehaviorType],
        "transitEncryptionEnabled": NotRequired[bool],
        "atRestEncryptionEnabled": NotRequired[bool],
        "type": NotRequired[ApiCacheTypeType],
        "status": NotRequired[ApiCacheStatusType],
    },
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "expires": NotRequired[int],
        "deletes": NotRequired[int],
    },
)

AssociateApiRequestRequestTypeDef = TypedDict(
    "AssociateApiRequestRequestTypeDef",
    {
        "domainName": str,
        "apiId": str,
    },
)

AssociateApiResponseTypeDef = TypedDict(
    "AssociateApiResponseTypeDef",
    {
        "apiAssociation": "ApiAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizationConfigTypeDef = TypedDict(
    "AuthorizationConfigTypeDef",
    {
        "authorizationType": Literal["AWS_IAM"],
        "awsIamConfig": NotRequired["AwsIamConfigTypeDef"],
    },
)

AwsIamConfigTypeDef = TypedDict(
    "AwsIamConfigTypeDef",
    {
        "signingRegion": NotRequired[str],
        "signingServiceName": NotRequired[str],
    },
)

CachingConfigTypeDef = TypedDict(
    "CachingConfigTypeDef",
    {
        "ttl": NotRequired[int],
        "cachingKeys": NotRequired[Sequence[str]],
    },
)

CognitoUserPoolConfigTypeDef = TypedDict(
    "CognitoUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "appIdClientRegex": NotRequired[str],
    },
)

CreateApiCacheRequestRequestTypeDef = TypedDict(
    "CreateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
        "transitEncryptionEnabled": NotRequired[bool],
        "atRestEncryptionEnabled": NotRequired[bool],
    },
)

CreateApiCacheResponseTypeDef = TypedDict(
    "CreateApiCacheResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApiKeyRequestRequestTypeDef = TypedDict(
    "CreateApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "description": NotRequired[str],
        "expires": NotRequired[int],
    },
)

CreateApiKeyResponseTypeDef = TypedDict(
    "CreateApiKeyResponseTypeDef",
    {
        "apiKey": "ApiKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
        "description": NotRequired[str],
        "serviceRoleArn": NotRequired[str],
        "dynamodbConfig": NotRequired["DynamodbDataSourceConfigTypeDef"],
        "lambdaConfig": NotRequired["LambdaDataSourceConfigTypeDef"],
        "elasticsearchConfig": NotRequired["ElasticsearchDataSourceConfigTypeDef"],
        "openSearchServiceConfig": NotRequired["OpenSearchServiceDataSourceConfigTypeDef"],
        "httpConfig": NotRequired["HttpDataSourceConfigTypeDef"],
        "relationalDatabaseConfig": NotRequired["RelationalDatabaseDataSourceConfigTypeDef"],
    },
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainNameRequestRequestTypeDef = TypedDict(
    "CreateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
        "certificateArn": str,
        "description": NotRequired[str],
    },
)

CreateDomainNameResponseTypeDef = TypedDict(
    "CreateDomainNameResponseTypeDef",
    {
        "domainNameConfig": "DomainNameConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionRequestRequestTypeDef = TypedDict(
    "CreateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "dataSourceName": str,
        "functionVersion": str,
        "description": NotRequired[str],
        "requestMappingTemplate": NotRequired[str],
        "responseMappingTemplate": NotRequired[str],
        "syncConfig": NotRequired["SyncConfigTypeDef"],
        "maxBatchSize": NotRequired[int],
    },
)

CreateFunctionResponseTypeDef = TypedDict(
    "CreateFunctionResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGraphqlApiRequestRequestTypeDef = TypedDict(
    "CreateGraphqlApiRequestRequestTypeDef",
    {
        "name": str,
        "authenticationType": AuthenticationTypeType,
        "logConfig": NotRequired["LogConfigTypeDef"],
        "userPoolConfig": NotRequired["UserPoolConfigTypeDef"],
        "openIDConnectConfig": NotRequired["OpenIDConnectConfigTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
        "additionalAuthenticationProviders": NotRequired[
            Sequence["AdditionalAuthenticationProviderTypeDef"]
        ],
        "xrayEnabled": NotRequired[bool],
        "lambdaAuthorizerConfig": NotRequired["LambdaAuthorizerConfigTypeDef"],
    },
)

CreateGraphqlApiResponseTypeDef = TypedDict(
    "CreateGraphqlApiResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResolverRequestRequestTypeDef = TypedDict(
    "CreateResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
        "dataSourceName": NotRequired[str],
        "requestMappingTemplate": NotRequired[str],
        "responseMappingTemplate": NotRequired[str],
        "kind": NotRequired[ResolverKindType],
        "pipelineConfig": NotRequired["PipelineConfigTypeDef"],
        "syncConfig": NotRequired["SyncConfigTypeDef"],
        "cachingConfig": NotRequired["CachingConfigTypeDef"],
        "maxBatchSize": NotRequired[int],
    },
)

CreateResolverResponseTypeDef = TypedDict(
    "CreateResolverResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypeRequestRequestTypeDef = TypedDict(
    "CreateTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
)

CreateTypeResponseTypeDef = TypedDict(
    "CreateTypeResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[DataSourceTypeType],
        "serviceRoleArn": NotRequired[str],
        "dynamodbConfig": NotRequired["DynamodbDataSourceConfigTypeDef"],
        "lambdaConfig": NotRequired["LambdaDataSourceConfigTypeDef"],
        "elasticsearchConfig": NotRequired["ElasticsearchDataSourceConfigTypeDef"],
        "openSearchServiceConfig": NotRequired["OpenSearchServiceDataSourceConfigTypeDef"],
        "httpConfig": NotRequired["HttpDataSourceConfigTypeDef"],
        "relationalDatabaseConfig": NotRequired["RelationalDatabaseDataSourceConfigTypeDef"],
    },
)

DeleteApiCacheRequestRequestTypeDef = TypedDict(
    "DeleteApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteFunctionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

DeleteGraphqlApiRequestRequestTypeDef = TypedDict(
    "DeleteGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteResolverRequestRequestTypeDef = TypedDict(
    "DeleteResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

DeleteTypeRequestRequestTypeDef = TypedDict(
    "DeleteTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)

DeltaSyncConfigTypeDef = TypedDict(
    "DeltaSyncConfigTypeDef",
    {
        "baseTableTTL": NotRequired[int],
        "deltaSyncTableName": NotRequired[str],
        "deltaSyncTableTTL": NotRequired[int],
    },
)

DisassociateApiRequestRequestTypeDef = TypedDict(
    "DisassociateApiRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DomainNameConfigTypeDef = TypedDict(
    "DomainNameConfigTypeDef",
    {
        "domainName": NotRequired[str],
        "description": NotRequired[str],
        "certificateArn": NotRequired[str],
        "appsyncDomainName": NotRequired[str],
        "hostedZoneId": NotRequired[str],
    },
)

DynamodbDataSourceConfigTypeDef = TypedDict(
    "DynamodbDataSourceConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
        "useCallerCredentials": NotRequired[bool],
        "deltaSyncConfig": NotRequired["DeltaSyncConfigTypeDef"],
        "versioned": NotRequired[bool],
    },
)

ElasticsearchDataSourceConfigTypeDef = TypedDict(
    "ElasticsearchDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

FlushApiCacheRequestRequestTypeDef = TypedDict(
    "FlushApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "functionId": NotRequired[str],
        "functionArn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "dataSourceName": NotRequired[str],
        "requestMappingTemplate": NotRequired[str],
        "responseMappingTemplate": NotRequired[str],
        "functionVersion": NotRequired[str],
        "syncConfig": NotRequired["SyncConfigTypeDef"],
        "maxBatchSize": NotRequired[int],
    },
)

GetApiAssociationRequestRequestTypeDef = TypedDict(
    "GetApiAssociationRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetApiAssociationResponseTypeDef = TypedDict(
    "GetApiAssociationResponseTypeDef",
    {
        "apiAssociation": "ApiAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiCacheRequestRequestTypeDef = TypedDict(
    "GetApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetApiCacheResponseTypeDef = TypedDict(
    "GetApiCacheResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainNameResponseTypeDef = TypedDict(
    "GetDomainNameResponseTypeDef",
    {
        "domainNameConfig": "DomainNameConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionRequestRequestTypeDef = TypedDict(
    "GetFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGraphqlApiRequestRequestTypeDef = TypedDict(
    "GetGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetGraphqlApiResponseTypeDef = TypedDict(
    "GetGraphqlApiResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntrospectionSchemaRequestRequestTypeDef = TypedDict(
    "GetIntrospectionSchemaRequestRequestTypeDef",
    {
        "apiId": str,
        "format": OutputTypeType,
        "includeDirectives": NotRequired[bool],
    },
)

GetIntrospectionSchemaResponseTypeDef = TypedDict(
    "GetIntrospectionSchemaResponseTypeDef",
    {
        "schema": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRequestRequestTypeDef = TypedDict(
    "GetResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

GetResolverResponseTypeDef = TypedDict(
    "GetResolverResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaCreationStatusRequestRequestTypeDef = TypedDict(
    "GetSchemaCreationStatusRequestRequestTypeDef",
    {
        "apiId": str,
    },
)

GetSchemaCreationStatusResponseTypeDef = TypedDict(
    "GetSchemaCreationStatusResponseTypeDef",
    {
        "status": SchemaStatusType,
        "details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypeRequestRequestTypeDef = TypedDict(
    "GetTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)

GetTypeResponseTypeDef = TypedDict(
    "GetTypeResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphqlApiTypeDef = TypedDict(
    "GraphqlApiTypeDef",
    {
        "name": NotRequired[str],
        "apiId": NotRequired[str],
        "authenticationType": NotRequired[AuthenticationTypeType],
        "logConfig": NotRequired["LogConfigTypeDef"],
        "userPoolConfig": NotRequired["UserPoolConfigTypeDef"],
        "openIDConnectConfig": NotRequired["OpenIDConnectConfigTypeDef"],
        "arn": NotRequired[str],
        "uris": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "additionalAuthenticationProviders": NotRequired[
            List["AdditionalAuthenticationProviderTypeDef"]
        ],
        "xrayEnabled": NotRequired[bool],
        "wafWebAclArn": NotRequired[str],
        "lambdaAuthorizerConfig": NotRequired["LambdaAuthorizerConfigTypeDef"],
    },
)

HttpDataSourceConfigTypeDef = TypedDict(
    "HttpDataSourceConfigTypeDef",
    {
        "endpoint": NotRequired[str],
        "authorizationConfig": NotRequired["AuthorizationConfigTypeDef"],
    },
)

LambdaAuthorizerConfigTypeDef = TypedDict(
    "LambdaAuthorizerConfigTypeDef",
    {
        "authorizerUri": str,
        "authorizerResultTtlInSeconds": NotRequired[int],
        "identityValidationExpression": NotRequired[str],
    },
)

LambdaConflictHandlerConfigTypeDef = TypedDict(
    "LambdaConflictHandlerConfigTypeDef",
    {
        "lambdaConflictHandlerArn": NotRequired[str],
    },
)

LambdaDataSourceConfigTypeDef = TypedDict(
    "LambdaDataSourceConfigTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

ListApiKeysRequestRequestTypeDef = TypedDict(
    "ListApiKeysRequestRequestTypeDef",
    {
        "apiId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListApiKeysResponseTypeDef = TypedDict(
    "ListApiKeysResponseTypeDef",
    {
        "apiKeys": List["ApiKeyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "apiId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSources": List["DataSourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainNamesRequestRequestTypeDef = TypedDict(
    "ListDomainNamesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "domainNameConfigs": List["DomainNameConfigTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsRequestRequestTypeDef = TypedDict(
    "ListFunctionsRequestRequestTypeDef",
    {
        "apiId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {
        "functions": List["FunctionConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGraphqlApisRequestRequestTypeDef = TypedDict(
    "ListGraphqlApisRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListGraphqlApisResponseTypeDef = TypedDict(
    "ListGraphqlApisResponseTypeDef",
    {
        "graphqlApis": List["GraphqlApiTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolversByFunctionRequestRequestTypeDef = TypedDict(
    "ListResolversByFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListResolversByFunctionResponseTypeDef = TypedDict(
    "ListResolversByFunctionResponseTypeDef",
    {
        "resolvers": List["ResolverTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResolversRequestRequestTypeDef = TypedDict(
    "ListResolversRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListResolversResponseTypeDef = TypedDict(
    "ListResolversResponseTypeDef",
    {
        "resolvers": List["ResolverTypeDef"],
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

ListTypesRequestRequestTypeDef = TypedDict(
    "ListTypesRequestRequestTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef",
    {
        "types": List["TypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogConfigTypeDef = TypedDict(
    "LogConfigTypeDef",
    {
        "fieldLogLevel": FieldLogLevelType,
        "cloudWatchLogsRoleArn": str,
        "excludeVerboseContent": NotRequired[bool],
    },
)

OpenIDConnectConfigTypeDef = TypedDict(
    "OpenIDConnectConfigTypeDef",
    {
        "issuer": str,
        "clientId": NotRequired[str],
        "iatTTL": NotRequired[int],
        "authTTL": NotRequired[int],
    },
)

OpenSearchServiceDataSourceConfigTypeDef = TypedDict(
    "OpenSearchServiceDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
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

PipelineConfigTypeDef = TypedDict(
    "PipelineConfigTypeDef",
    {
        "functions": NotRequired[Sequence[str]],
    },
)

RdsHttpEndpointConfigTypeDef = TypedDict(
    "RdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": NotRequired[str],
        "dbClusterIdentifier": NotRequired[str],
        "databaseName": NotRequired[str],
        "schema": NotRequired[str],
        "awsSecretStoreArn": NotRequired[str],
    },
)

RelationalDatabaseDataSourceConfigTypeDef = TypedDict(
    "RelationalDatabaseDataSourceConfigTypeDef",
    {
        "relationalDatabaseSourceType": NotRequired[Literal["RDS_HTTP_ENDPOINT"]],
        "rdsHttpEndpointConfig": NotRequired["RdsHttpEndpointConfigTypeDef"],
    },
)

ResolverTypeDef = TypedDict(
    "ResolverTypeDef",
    {
        "typeName": NotRequired[str],
        "fieldName": NotRequired[str],
        "dataSourceName": NotRequired[str],
        "resolverArn": NotRequired[str],
        "requestMappingTemplate": NotRequired[str],
        "responseMappingTemplate": NotRequired[str],
        "kind": NotRequired[ResolverKindType],
        "pipelineConfig": NotRequired["PipelineConfigTypeDef"],
        "syncConfig": NotRequired["SyncConfigTypeDef"],
        "cachingConfig": NotRequired["CachingConfigTypeDef"],
        "maxBatchSize": NotRequired[int],
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

StartSchemaCreationRequestRequestTypeDef = TypedDict(
    "StartSchemaCreationRequestRequestTypeDef",
    {
        "apiId": str,
        "definition": Union[bytes, IO[bytes], StreamingBody],
    },
)

StartSchemaCreationResponseTypeDef = TypedDict(
    "StartSchemaCreationResponseTypeDef",
    {
        "status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncConfigTypeDef = TypedDict(
    "SyncConfigTypeDef",
    {
        "conflictHandler": NotRequired[ConflictHandlerTypeType],
        "conflictDetection": NotRequired[ConflictDetectionTypeType],
        "lambdaConflictHandlerConfig": NotRequired["LambdaConflictHandlerConfigTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "arn": NotRequired[str],
        "definition": NotRequired[str],
        "format": NotRequired[TypeDefinitionFormatType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateApiCacheRequestRequestTypeDef = TypedDict(
    "UpdateApiCacheRequestRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)

UpdateApiCacheResponseTypeDef = TypedDict(
    "UpdateApiCacheResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApiKeyRequestRequestTypeDef = TypedDict(
    "UpdateApiKeyRequestRequestTypeDef",
    {
        "apiId": str,
        "id": str,
        "description": NotRequired[str],
        "expires": NotRequired[int],
    },
)

UpdateApiKeyResponseTypeDef = TypedDict(
    "UpdateApiKeyResponseTypeDef",
    {
        "apiKey": "ApiKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
        "description": NotRequired[str],
        "serviceRoleArn": NotRequired[str],
        "dynamodbConfig": NotRequired["DynamodbDataSourceConfigTypeDef"],
        "lambdaConfig": NotRequired["LambdaDataSourceConfigTypeDef"],
        "elasticsearchConfig": NotRequired["ElasticsearchDataSourceConfigTypeDef"],
        "openSearchServiceConfig": NotRequired["OpenSearchServiceDataSourceConfigTypeDef"],
        "httpConfig": NotRequired["HttpDataSourceConfigTypeDef"],
        "relationalDatabaseConfig": NotRequired["RelationalDatabaseDataSourceConfigTypeDef"],
    },
)

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainNameRequestRequestTypeDef = TypedDict(
    "UpdateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
        "description": NotRequired[str],
    },
)

UpdateDomainNameResponseTypeDef = TypedDict(
    "UpdateDomainNameResponseTypeDef",
    {
        "domainNameConfig": "DomainNameConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFunctionRequestRequestTypeDef = TypedDict(
    "UpdateFunctionRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "functionId": str,
        "dataSourceName": str,
        "functionVersion": str,
        "description": NotRequired[str],
        "requestMappingTemplate": NotRequired[str],
        "responseMappingTemplate": NotRequired[str],
        "syncConfig": NotRequired["SyncConfigTypeDef"],
        "maxBatchSize": NotRequired[int],
    },
)

UpdateFunctionResponseTypeDef = TypedDict(
    "UpdateFunctionResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGraphqlApiRequestRequestTypeDef = TypedDict(
    "UpdateGraphqlApiRequestRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "logConfig": NotRequired["LogConfigTypeDef"],
        "authenticationType": NotRequired[AuthenticationTypeType],
        "userPoolConfig": NotRequired["UserPoolConfigTypeDef"],
        "openIDConnectConfig": NotRequired["OpenIDConnectConfigTypeDef"],
        "additionalAuthenticationProviders": NotRequired[
            Sequence["AdditionalAuthenticationProviderTypeDef"]
        ],
        "xrayEnabled": NotRequired[bool],
        "lambdaAuthorizerConfig": NotRequired["LambdaAuthorizerConfigTypeDef"],
    },
)

UpdateGraphqlApiResponseTypeDef = TypedDict(
    "UpdateGraphqlApiResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResolverRequestRequestTypeDef = TypedDict(
    "UpdateResolverRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
        "dataSourceName": NotRequired[str],
        "requestMappingTemplate": NotRequired[str],
        "responseMappingTemplate": NotRequired[str],
        "kind": NotRequired[ResolverKindType],
        "pipelineConfig": NotRequired["PipelineConfigTypeDef"],
        "syncConfig": NotRequired["SyncConfigTypeDef"],
        "cachingConfig": NotRequired["CachingConfigTypeDef"],
        "maxBatchSize": NotRequired[int],
    },
)

UpdateResolverResponseTypeDef = TypedDict(
    "UpdateResolverResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTypeRequestRequestTypeDef = TypedDict(
    "UpdateTypeRequestRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
        "definition": NotRequired[str],
    },
)

UpdateTypeResponseTypeDef = TypedDict(
    "UpdateTypeResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserPoolConfigTypeDef = TypedDict(
    "UserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": DefaultActionType,
        "appIdClientRegex": NotRequired[str],
    },
)
