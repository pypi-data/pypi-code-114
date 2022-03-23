"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_finspace_data/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_finspace_data.type_defs import ChangesetErrorInfoTypeDef

    data: ChangesetErrorInfoTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ApiAccessType,
    ApplicationPermissionType,
    ChangeTypeType,
    ColumnDataTypeType,
    DatasetKindType,
    DatasetStatusType,
    DataViewStatusType,
    ErrorCategoryType,
    ExportFileFormatType,
    IngestionStatusType,
    UserStatusType,
    UserTypeType,
    locationTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChangesetErrorInfoTypeDef",
    "ChangesetSummaryTypeDef",
    "ColumnDefinitionTypeDef",
    "CreateChangesetRequestRequestTypeDef",
    "CreateChangesetResponseTypeDef",
    "CreateDataViewRequestRequestTypeDef",
    "CreateDataViewResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreatePermissionGroupRequestRequestTypeDef",
    "CreatePermissionGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CredentialsTypeDef",
    "DataViewDestinationTypeParamsTypeDef",
    "DataViewErrorInfoTypeDef",
    "DataViewSummaryTypeDef",
    "DatasetOwnerInfoTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeletePermissionGroupRequestRequestTypeDef",
    "DeletePermissionGroupResponseTypeDef",
    "DisableUserRequestRequestTypeDef",
    "DisableUserResponseTypeDef",
    "EnableUserRequestRequestTypeDef",
    "EnableUserResponseTypeDef",
    "GetChangesetRequestRequestTypeDef",
    "GetChangesetResponseTypeDef",
    "GetDataViewRequestRequestTypeDef",
    "GetDataViewResponseTypeDef",
    "GetDatasetRequestRequestTypeDef",
    "GetDatasetResponseTypeDef",
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetWorkingLocationRequestRequestTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ListChangesetsRequestRequestTypeDef",
    "ListChangesetsResponseTypeDef",
    "ListDataViewsRequestRequestTypeDef",
    "ListDataViewsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListPermissionGroupsRequestRequestTypeDef",
    "ListPermissionGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionGroupParamsTypeDef",
    "PermissionGroupTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "ResetUserPasswordResponseTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaDefinitionTypeDef",
    "SchemaUnionTypeDef",
    "UpdateChangesetRequestRequestTypeDef",
    "UpdateChangesetResponseTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdatePermissionGroupRequestRequestTypeDef",
    "UpdatePermissionGroupResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserTypeDef",
)

ChangesetErrorInfoTypeDef = TypedDict(
    "ChangesetErrorInfoTypeDef",
    {
        "errorMessage": NotRequired[str],
        "errorCategory": NotRequired[ErrorCategoryType],
    },
)

ChangesetSummaryTypeDef = TypedDict(
    "ChangesetSummaryTypeDef",
    {
        "changesetId": NotRequired[str],
        "changesetArn": NotRequired[str],
        "datasetId": NotRequired[str],
        "changeType": NotRequired[ChangeTypeType],
        "sourceParams": NotRequired[Dict[str, str]],
        "formatParams": NotRequired[Dict[str, str]],
        "createTime": NotRequired[int],
        "status": NotRequired[IngestionStatusType],
        "errorInfo": NotRequired["ChangesetErrorInfoTypeDef"],
        "activeUntilTimestamp": NotRequired[int],
        "activeFromTimestamp": NotRequired[int],
        "updatesChangesetId": NotRequired[str],
        "updatedByChangesetId": NotRequired[str],
    },
)

ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "dataType": NotRequired[ColumnDataTypeType],
        "columnName": NotRequired[str],
        "columnDescription": NotRequired[str],
    },
)

CreateChangesetRequestRequestTypeDef = TypedDict(
    "CreateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Mapping[str, str],
        "formatParams": Mapping[str, str],
        "clientToken": NotRequired[str],
    },
)

CreateChangesetResponseTypeDef = TypedDict(
    "CreateChangesetResponseTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataViewRequestRequestTypeDef = TypedDict(
    "CreateDataViewRequestRequestTypeDef",
    {
        "datasetId": str,
        "destinationTypeParams": "DataViewDestinationTypeParamsTypeDef",
        "clientToken": NotRequired[str],
        "autoUpdate": NotRequired[bool],
        "sortColumns": NotRequired[Sequence[str]],
        "partitionColumns": NotRequired[Sequence[str]],
        "asOfTimestamp": NotRequired[int],
    },
)

CreateDataViewResponseTypeDef = TypedDict(
    "CreateDataViewResponseTypeDef",
    {
        "datasetId": str,
        "dataViewId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "datasetTitle": str,
        "kind": DatasetKindType,
        "permissionGroupParams": "PermissionGroupParamsTypeDef",
        "clientToken": NotRequired[str],
        "datasetDescription": NotRequired[str],
        "ownerInfo": NotRequired["DatasetOwnerInfoTypeDef"],
        "alias": NotRequired[str],
        "schemaDefinition": NotRequired["SchemaUnionTypeDef"],
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePermissionGroupRequestRequestTypeDef = TypedDict(
    "CreatePermissionGroupRequestRequestTypeDef",
    {
        "name": str,
        "applicationPermissions": Sequence[ApplicationPermissionType],
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

CreatePermissionGroupResponseTypeDef = TypedDict(
    "CreatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "emailAddress": str,
        "type": UserTypeType,
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "ApiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "secretAccessKey": NotRequired[str],
        "sessionToken": NotRequired[str],
    },
)

DataViewDestinationTypeParamsTypeDef = TypedDict(
    "DataViewDestinationTypeParamsTypeDef",
    {
        "destinationType": str,
        "s3DestinationExportFileFormat": NotRequired[ExportFileFormatType],
        "s3DestinationExportFileFormatOptions": NotRequired[Mapping[str, str]],
    },
)

DataViewErrorInfoTypeDef = TypedDict(
    "DataViewErrorInfoTypeDef",
    {
        "errorMessage": NotRequired[str],
        "errorCategory": NotRequired[ErrorCategoryType],
    },
)

DataViewSummaryTypeDef = TypedDict(
    "DataViewSummaryTypeDef",
    {
        "dataViewId": NotRequired[str],
        "dataViewArn": NotRequired[str],
        "datasetId": NotRequired[str],
        "asOfTimestamp": NotRequired[int],
        "partitionColumns": NotRequired[List[str]],
        "sortColumns": NotRequired[List[str]],
        "status": NotRequired[DataViewStatusType],
        "errorInfo": NotRequired["DataViewErrorInfoTypeDef"],
        "destinationTypeProperties": NotRequired["DataViewDestinationTypeParamsTypeDef"],
        "autoUpdate": NotRequired[bool],
        "createTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
    },
)

DatasetOwnerInfoTypeDef = TypedDict(
    "DatasetOwnerInfoTypeDef",
    {
        "name": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "email": NotRequired[str],
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "datasetId": NotRequired[str],
        "datasetArn": NotRequired[str],
        "datasetTitle": NotRequired[str],
        "kind": NotRequired[DatasetKindType],
        "datasetDescription": NotRequired[str],
        "ownerInfo": NotRequired["DatasetOwnerInfoTypeDef"],
        "createTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
        "schemaDefinition": NotRequired["SchemaUnionTypeDef"],
        "alias": NotRequired[str],
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePermissionGroupRequestRequestTypeDef = TypedDict(
    "DeletePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "clientToken": NotRequired[str],
    },
)

DeletePermissionGroupResponseTypeDef = TypedDict(
    "DeletePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableUserRequestRequestTypeDef = TypedDict(
    "DisableUserRequestRequestTypeDef",
    {
        "userId": str,
        "clientToken": NotRequired[str],
    },
)

DisableUserResponseTypeDef = TypedDict(
    "DisableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableUserRequestRequestTypeDef = TypedDict(
    "EnableUserRequestRequestTypeDef",
    {
        "userId": str,
        "clientToken": NotRequired[str],
    },
)

EnableUserResponseTypeDef = TypedDict(
    "EnableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangesetRequestRequestTypeDef = TypedDict(
    "GetChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
    },
)

GetChangesetResponseTypeDef = TypedDict(
    "GetChangesetResponseTypeDef",
    {
        "changesetId": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
        "createTime": int,
        "status": IngestionStatusType,
        "errorInfo": "ChangesetErrorInfoTypeDef",
        "activeUntilTimestamp": int,
        "activeFromTimestamp": int,
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataViewRequestRequestTypeDef = TypedDict(
    "GetDataViewRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)

GetDataViewResponseTypeDef = TypedDict(
    "GetDataViewResponseTypeDef",
    {
        "autoUpdate": bool,
        "partitionColumns": List[str],
        "datasetId": str,
        "asOfTimestamp": int,
        "errorInfo": "DataViewErrorInfoTypeDef",
        "lastModifiedTime": int,
        "createTime": int,
        "sortColumns": List[str],
        "dataViewId": str,
        "dataViewArn": str,
        "destinationTypeParams": "DataViewDestinationTypeParamsTypeDef",
        "status": DataViewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatasetRequestRequestTypeDef = TypedDict(
    "GetDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)

GetDatasetResponseTypeDef = TypedDict(
    "GetDatasetResponseTypeDef",
    {
        "datasetId": str,
        "datasetArn": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "createTime": int,
        "lastModifiedTime": int,
        "schemaDefinition": "SchemaUnionTypeDef",
        "alias": str,
        "status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "environmentId": str,
        "durationInMinutes": NotRequired[int],
    },
)

GetProgrammaticAccessCredentialsResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    {
        "credentials": "CredentialsTypeDef",
        "durationInMinutes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "createTime": int,
        "lastEnabledTime": int,
        "lastDisabledTime": int,
        "lastModifiedTime": int,
        "lastLoginTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkingLocationRequestRequestTypeDef = TypedDict(
    "GetWorkingLocationRequestRequestTypeDef",
    {
        "locationType": NotRequired[locationTypeType],
    },
)

GetWorkingLocationResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChangesetsRequestRequestTypeDef = TypedDict(
    "ListChangesetsRequestRequestTypeDef",
    {
        "datasetId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListChangesetsResponseTypeDef = TypedDict(
    "ListChangesetsResponseTypeDef",
    {
        "changesets": List["ChangesetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataViewsRequestRequestTypeDef = TypedDict(
    "ListDataViewsRequestRequestTypeDef",
    {
        "datasetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDataViewsResponseTypeDef = TypedDict(
    "ListDataViewsResponseTypeDef",
    {
        "nextToken": str,
        "dataViews": List["DataViewSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List["DatasetTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionGroupsRequestRequestTypeDef = TypedDict(
    "ListPermissionGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": NotRequired[str],
    },
)

ListPermissionGroupsResponseTypeDef = TypedDict(
    "ListPermissionGroupsResponseTypeDef",
    {
        "permissionGroups": List["PermissionGroupTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": NotRequired[str],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "users": List["UserTypeDef"],
        "nextToken": str,
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

PermissionGroupParamsTypeDef = TypedDict(
    "PermissionGroupParamsTypeDef",
    {
        "permissionGroupId": NotRequired[str],
        "datasetPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

PermissionGroupTypeDef = TypedDict(
    "PermissionGroupTypeDef",
    {
        "permissionGroupId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "applicationPermissions": NotRequired[List[ApplicationPermissionType]],
        "createTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
    },
)

ResetUserPasswordRequestRequestTypeDef = TypedDict(
    "ResetUserPasswordRequestRequestTypeDef",
    {
        "userId": str,
        "clientToken": NotRequired[str],
    },
)

ResetUserPasswordResponseTypeDef = TypedDict(
    "ResetUserPasswordResponseTypeDef",
    {
        "userId": str,
        "temporaryPassword": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "permission": NotRequired[str],
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

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": NotRequired[Sequence["ColumnDefinitionTypeDef"]],
        "primaryKeyColumns": NotRequired[Sequence[str]],
    },
)

SchemaUnionTypeDef = TypedDict(
    "SchemaUnionTypeDef",
    {
        "tabularSchemaConfig": NotRequired["SchemaDefinitionTypeDef"],
    },
)

UpdateChangesetRequestRequestTypeDef = TypedDict(
    "UpdateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "sourceParams": Mapping[str, str],
        "formatParams": Mapping[str, str],
        "clientToken": NotRequired[str],
    },
)

UpdateChangesetResponseTypeDef = TypedDict(
    "UpdateChangesetResponseTypeDef",
    {
        "changesetId": str,
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "clientToken": NotRequired[str],
        "datasetDescription": NotRequired[str],
        "alias": NotRequired[str],
        "schemaDefinition": NotRequired["SchemaUnionTypeDef"],
    },
)

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePermissionGroupRequestRequestTypeDef = TypedDict(
    "UpdatePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "applicationPermissions": NotRequired[Sequence[ApplicationPermissionType]],
        "clientToken": NotRequired[str],
    },
)

UpdatePermissionGroupResponseTypeDef = TypedDict(
    "UpdatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "userId": str,
        "type": NotRequired[UserTypeType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": NotRequired[str],
        "status": NotRequired[UserStatusType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "type": NotRequired[UserTypeType],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "createTime": NotRequired[int],
        "lastEnabledTime": NotRequired[int],
        "lastDisabledTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
        "lastLoginTime": NotRequired[int],
    },
)
