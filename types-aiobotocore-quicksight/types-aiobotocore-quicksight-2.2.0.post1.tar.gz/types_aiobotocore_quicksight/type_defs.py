"""
Type annotations for quicksight service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_quicksight/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AnalysisErrorTypeType,
    AssignmentStatusType,
    ColumnDataTypeType,
    ColumnTagNameType,
    DashboardBehaviorType,
    DashboardErrorTypeType,
    DashboardUIStateType,
    DataSetImportModeType,
    DataSourceErrorInfoTypeType,
    DataSourceTypeType,
    EditionType,
    EmbeddingIdentityTypeType,
    FileFormatType,
    GeoSpatialDataRoleType,
    IdentityTypeType,
    IngestionErrorTypeType,
    IngestionRequestSourceType,
    IngestionRequestTypeType,
    IngestionStatusType,
    IngestionTypeType,
    InputColumnDataTypeType,
    JoinTypeType,
    MemberTypeType,
    NamespaceErrorTypeType,
    NamespaceStatusType,
    ResourceStatusType,
    RowLevelPermissionFormatVersionType,
    RowLevelPermissionPolicyType,
    StatusType,
    TemplateErrorTypeType,
    TextQualifierType,
    ThemeTypeType,
    UserRoleType,
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
    "AccountCustomizationTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AmazonOpenSearchParametersTypeDef",
    "AnalysisErrorTypeDef",
    "AnalysisSearchFilterTypeDef",
    "AnalysisSourceEntityTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "AnalysisSummaryTypeDef",
    "AnalysisTypeDef",
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "BorderStyleTypeDef",
    "CalculatedColumnTypeDef",
    "CancelIngestionRequestRequestTypeDef",
    "CancelIngestionResponseTypeDef",
    "CastColumnTypeOperationTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ColumnTagTypeDef",
    "CreateAccountCustomizationRequestRequestTypeDef",
    "CreateAccountCustomizationResponseTypeDef",
    "CreateAnalysisRequestRequestTypeDef",
    "CreateAnalysisResponseTypeDef",
    "CreateColumnsOperationTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFolderMembershipRequestRequestTypeDef",
    "CreateFolderMembershipResponseTypeDef",
    "CreateFolderRequestRequestTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateGroupMembershipRequestRequestTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIAMPolicyAssignmentRequestRequestTypeDef",
    "CreateIAMPolicyAssignmentResponseTypeDef",
    "CreateIngestionRequestRequestTypeDef",
    "CreateIngestionResponseTypeDef",
    "CreateNamespaceRequestRequestTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateTemplateAliasRequestRequestTypeDef",
    "CreateTemplateAliasResponseTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateThemeAliasRequestRequestTypeDef",
    "CreateThemeAliasResponseTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "CredentialPairTypeDef",
    "CustomSqlTypeDef",
    "DashboardErrorTypeDef",
    "DashboardPublishOptionsTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSourceEntityTypeDef",
    "DashboardSourceTemplateTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardTypeDef",
    "DashboardVersionSummaryTypeDef",
    "DashboardVersionTypeDef",
    "DataColorPaletteTypeDef",
    "DataSetConfigurationTypeDef",
    "DataSetReferenceTypeDef",
    "DataSetSchemaTypeDef",
    "DataSetSummaryTypeDef",
    "DataSetTypeDef",
    "DataSetUsageConfigurationTypeDef",
    "DataSourceCredentialsTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DataSourceParametersTypeDef",
    "DataSourceTypeDef",
    "DateTimeParameterTypeDef",
    "DecimalParameterTypeDef",
    "DeleteAccountCustomizationRequestRequestTypeDef",
    "DeleteAccountCustomizationResponseTypeDef",
    "DeleteAnalysisRequestRequestTypeDef",
    "DeleteAnalysisResponseTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteDataSetResponseTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteFolderMembershipRequestRequestTypeDef",
    "DeleteFolderMembershipResponseTypeDef",
    "DeleteFolderRequestRequestTypeDef",
    "DeleteFolderResponseTypeDef",
    "DeleteGroupMembershipRequestRequestTypeDef",
    "DeleteGroupMembershipResponseTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteGroupResponseTypeDef",
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteTemplateAliasRequestRequestTypeDef",
    "DeleteTemplateAliasResponseTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteTemplateResponseTypeDef",
    "DeleteThemeAliasRequestRequestTypeDef",
    "DeleteThemeAliasResponseTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "DeleteThemeResponseTypeDef",
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    "DeleteUserByPrincipalIdResponseTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeAccountCustomizationRequestRequestTypeDef",
    "DescribeAccountCustomizationResponseTypeDef",
    "DescribeAccountSettingsRequestRequestTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    "DescribeAnalysisPermissionsResponseTypeDef",
    "DescribeAnalysisRequestRequestTypeDef",
    "DescribeAnalysisResponseTypeDef",
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    "DescribeDashboardPermissionsResponseTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    "DescribeDataSetPermissionsResponseTypeDef",
    "DescribeDataSetRequestRequestTypeDef",
    "DescribeDataSetResponseTypeDef",
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    "DescribeDataSourcePermissionsResponseTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeFolderPermissionsRequestRequestTypeDef",
    "DescribeFolderPermissionsResponseTypeDef",
    "DescribeFolderRequestRequestTypeDef",
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    "DescribeFolderResponseTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    "DescribeIngestionRequestRequestTypeDef",
    "DescribeIngestionResponseTypeDef",
    "DescribeIpRestrictionRequestRequestTypeDef",
    "DescribeIpRestrictionResponseTypeDef",
    "DescribeNamespaceRequestRequestTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "DescribeTemplateAliasRequestRequestTypeDef",
    "DescribeTemplateAliasResponseTypeDef",
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    "DescribeTemplatePermissionsResponseTypeDef",
    "DescribeTemplateRequestRequestTypeDef",
    "DescribeTemplateResponseTypeDef",
    "DescribeThemeAliasRequestRequestTypeDef",
    "DescribeThemeAliasResponseTypeDef",
    "DescribeThemePermissionsRequestRequestTypeDef",
    "DescribeThemePermissionsResponseTypeDef",
    "DescribeThemeRequestRequestTypeDef",
    "DescribeThemeResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "ErrorInfoTypeDef",
    "ExasolParametersTypeDef",
    "ExportToCSVOptionTypeDef",
    "FieldFolderTypeDef",
    "FilterOperationTypeDef",
    "FolderMemberTypeDef",
    "FolderSearchFilterTypeDef",
    "FolderSummaryTypeDef",
    "FolderTypeDef",
    "GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    "GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "GetDashboardEmbedUrlRequestRequestTypeDef",
    "GetDashboardEmbedUrlResponseTypeDef",
    "GetSessionEmbedUrlRequestRequestTypeDef",
    "GetSessionEmbedUrlResponseTypeDef",
    "GroupMemberTypeDef",
    "GroupTypeDef",
    "GutterStyleTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "IngestionTypeDef",
    "InputColumnTypeDef",
    "IntegerParameterTypeDef",
    "JiraParametersTypeDef",
    "JoinInstructionTypeDef",
    "JoinKeyPropertiesTypeDef",
    "LinkSharingConfigurationTypeDef",
    "ListAnalysesRequestRequestTypeDef",
    "ListAnalysesResponseTypeDef",
    "ListDashboardVersionsRequestRequestTypeDef",
    "ListDashboardVersionsResponseTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFolderMembersRequestRequestTypeDef",
    "ListFolderMembersResponseTypeDef",
    "ListFoldersRequestRequestTypeDef",
    "ListFoldersResponseTypeDef",
    "ListGroupMembershipsRequestRequestTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    "ListIAMPolicyAssignmentsRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsResponseTypeDef",
    "ListIngestionsRequestRequestTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateAliasesRequestRequestTypeDef",
    "ListTemplateAliasesResponseTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListThemeAliasesRequestRequestTypeDef",
    "ListThemeAliasesResponseTypeDef",
    "ListThemeVersionsRequestRequestTypeDef",
    "ListThemeVersionsResponseTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ListThemesResponseTypeDef",
    "ListUserGroupsRequestRequestTypeDef",
    "ListUserGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LogicalTableSourceTypeDef",
    "LogicalTableTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "MariaDbParametersTypeDef",
    "MemberIdArnPairTypeDef",
    "MySqlParametersTypeDef",
    "NamespaceErrorTypeDef",
    "NamespaceInfoV2TypeDef",
    "OracleParametersTypeDef",
    "OutputColumnTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersTypeDef",
    "PhysicalTableTypeDef",
    "PostgreSqlParametersTypeDef",
    "PrestoParametersTypeDef",
    "ProjectOperationTypeDef",
    "QueueInfoTypeDef",
    "RdsParametersTypeDef",
    "RedshiftParametersTypeDef",
    "RegisterUserRequestRequestTypeDef",
    "RegisterUserResponseTypeDef",
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    "RelationalTableTypeDef",
    "RenameColumnOperationTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreAnalysisRequestRequestTypeDef",
    "RestoreAnalysisResponseTypeDef",
    "RowInfoTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "RowLevelPermissionTagConfigurationTypeDef",
    "RowLevelPermissionTagRuleTypeDef",
    "S3ParametersTypeDef",
    "S3SourceTypeDef",
    "SearchAnalysesRequestRequestTypeDef",
    "SearchAnalysesResponseTypeDef",
    "SearchDashboardsRequestRequestTypeDef",
    "SearchDashboardsResponseTypeDef",
    "SearchFoldersRequestRequestTypeDef",
    "SearchFoldersResponseTypeDef",
    "ServiceNowParametersTypeDef",
    "SessionTagTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetStyleTypeDef",
    "SheetTypeDef",
    "SnowflakeParametersTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "SslPropertiesTypeDef",
    "StringParameterTypeDef",
    "TagColumnOperationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "TemplateAliasTypeDef",
    "TemplateErrorTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "TemplateSourceEntityTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TemplateSummaryTypeDef",
    "TemplateTypeDef",
    "TemplateVersionSummaryTypeDef",
    "TemplateVersionTypeDef",
    "TeradataParametersTypeDef",
    "ThemeAliasTypeDef",
    "ThemeConfigurationTypeDef",
    "ThemeErrorTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ThemeVersionTypeDef",
    "TileLayoutStyleTypeDef",
    "TileStyleTypeDef",
    "TransformOperationTypeDef",
    "TwitterParametersTypeDef",
    "UIColorPaletteTypeDef",
    "UntagColumnOperationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateAccountCustomizationRequestRequestTypeDef",
    "UpdateAccountCustomizationResponseTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateAnalysisPermissionsRequestRequestTypeDef",
    "UpdateAnalysisPermissionsResponseTypeDef",
    "UpdateAnalysisRequestRequestTypeDef",
    "UpdateAnalysisResponseTypeDef",
    "UpdateDashboardPermissionsRequestRequestTypeDef",
    "UpdateDashboardPermissionsResponseTypeDef",
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    "UpdateDashboardPublishedVersionResponseTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateDataSetPermissionsRequestRequestTypeDef",
    "UpdateDataSetPermissionsResponseTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateDataSourcePermissionsRequestRequestTypeDef",
    "UpdateDataSourcePermissionsResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFolderPermissionsRequestRequestTypeDef",
    "UpdateFolderPermissionsResponseTypeDef",
    "UpdateFolderRequestRequestTypeDef",
    "UpdateFolderResponseTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIAMPolicyAssignmentRequestRequestTypeDef",
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    "UpdateIpRestrictionRequestRequestTypeDef",
    "UpdateIpRestrictionResponseTypeDef",
    "UpdateTemplateAliasRequestRequestTypeDef",
    "UpdateTemplateAliasResponseTypeDef",
    "UpdateTemplatePermissionsRequestRequestTypeDef",
    "UpdateTemplatePermissionsResponseTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateThemeAliasRequestRequestTypeDef",
    "UpdateThemeAliasResponseTypeDef",
    "UpdateThemePermissionsRequestRequestTypeDef",
    "UpdateThemePermissionsResponseTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "UpdateThemeResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UploadSettingsTypeDef",
    "UserTypeDef",
    "VpcConnectionPropertiesTypeDef",
)

AccountCustomizationTypeDef = TypedDict(
    "AccountCustomizationTypeDef",
    {
        "DefaultTheme": NotRequired[str],
        "DefaultEmailCustomizationTemplate": NotRequired[str],
    },
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "AccountName": NotRequired[str],
        "Edition": NotRequired[EditionType],
        "DefaultNamespace": NotRequired[str],
        "NotificationEmail": NotRequired[str],
    },
)

ActiveIAMPolicyAssignmentTypeDef = TypedDict(
    "ActiveIAMPolicyAssignmentTypeDef",
    {
        "AssignmentName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)

AdHocFilteringOptionTypeDef = TypedDict(
    "AdHocFilteringOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)

AmazonElasticsearchParametersTypeDef = TypedDict(
    "AmazonElasticsearchParametersTypeDef",
    {
        "Domain": str,
    },
)

AmazonOpenSearchParametersTypeDef = TypedDict(
    "AmazonOpenSearchParametersTypeDef",
    {
        "Domain": str,
    },
)

AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef",
    {
        "Type": NotRequired[AnalysisErrorTypeType],
        "Message": NotRequired[str],
    },
)

AnalysisSearchFilterTypeDef = TypedDict(
    "AnalysisSearchFilterTypeDef",
    {
        "Operator": NotRequired[Literal["StringEquals"]],
        "Name": NotRequired[Literal["QUICKSIGHT_USER"]],
        "Value": NotRequired[str],
    },
)

AnalysisSourceEntityTypeDef = TypedDict(
    "AnalysisSourceEntityTypeDef",
    {
        "SourceTemplate": NotRequired["AnalysisSourceTemplateTypeDef"],
    },
)

AnalysisSourceTemplateTypeDef = TypedDict(
    "AnalysisSourceTemplateTypeDef",
    {
        "DataSetReferences": Sequence["DataSetReferenceTypeDef"],
        "Arn": str,
    },
)

AnalysisSummaryTypeDef = TypedDict(
    "AnalysisSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "AnalysisId": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ResourceStatusType],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "AnalysisId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ResourceStatusType],
        "Errors": NotRequired[List["AnalysisErrorTypeDef"]],
        "DataSetArns": NotRequired[List[str]],
        "ThemeArn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "Sheets": NotRequired[List["SheetTypeDef"]],
    },
)

AnonymousUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
    },
)

AnonymousUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": NotRequired["AnonymousUserDashboardEmbeddingConfigurationTypeDef"],
    },
)

AthenaParametersTypeDef = TypedDict(
    "AthenaParametersTypeDef",
    {
        "WorkGroup": NotRequired[str],
    },
)

AuroraParametersTypeDef = TypedDict(
    "AuroraParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AuroraPostgreSqlParametersTypeDef = TypedDict(
    "AuroraPostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AwsIotAnalyticsParametersTypeDef = TypedDict(
    "AwsIotAnalyticsParametersTypeDef",
    {
        "DataSetName": str,
    },
)

BorderStyleTypeDef = TypedDict(
    "BorderStyleTypeDef",
    {
        "Show": NotRequired[bool],
    },
)

CalculatedColumnTypeDef = TypedDict(
    "CalculatedColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnId": str,
        "Expression": str,
    },
)

CancelIngestionRequestRequestTypeDef = TypedDict(
    "CancelIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

CancelIngestionResponseTypeDef = TypedDict(
    "CancelIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CastColumnTypeOperationTypeDef = TypedDict(
    "CastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": ColumnDataTypeType,
        "Format": NotRequired[str],
    },
)

ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "Text": NotRequired[str],
    },
)

ColumnGroupColumnSchemaTypeDef = TypedDict(
    "ColumnGroupColumnSchemaTypeDef",
    {
        "Name": NotRequired[str],
    },
)

ColumnGroupSchemaTypeDef = TypedDict(
    "ColumnGroupSchemaTypeDef",
    {
        "Name": NotRequired[str],
        "ColumnGroupColumnSchemaList": NotRequired[List["ColumnGroupColumnSchemaTypeDef"]],
    },
)

ColumnGroupTypeDef = TypedDict(
    "ColumnGroupTypeDef",
    {
        "GeoSpatialColumnGroup": NotRequired["GeoSpatialColumnGroupTypeDef"],
    },
)

ColumnLevelPermissionRuleTypeDef = TypedDict(
    "ColumnLevelPermissionRuleTypeDef",
    {
        "Principals": NotRequired[Sequence[str]],
        "ColumnNames": NotRequired[Sequence[str]],
    },
)

ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "Name": NotRequired[str],
        "DataType": NotRequired[str],
        "GeographicRole": NotRequired[str],
    },
)

ColumnTagTypeDef = TypedDict(
    "ColumnTagTypeDef",
    {
        "ColumnGeographicRole": NotRequired[GeoSpatialDataRoleType],
        "ColumnDescription": NotRequired["ColumnDescriptionTypeDef"],
    },
)

CreateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "CreateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "Namespace": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAccountCustomizationResponseTypeDef = TypedDict(
    "CreateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAnalysisRequestRequestTypeDef = TypedDict(
    "CreateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
        "SourceEntity": "AnalysisSourceEntityTypeDef",
        "Parameters": NotRequired["ParametersTypeDef"],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "ThemeArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAnalysisResponseTypeDef = TypedDict(
    "CreateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateColumnsOperationTypeDef = TypedDict(
    "CreateColumnsOperationTypeDef",
    {
        "Columns": Sequence["CalculatedColumnTypeDef"],
    },
)

CreateDashboardRequestRequestTypeDef = TypedDict(
    "CreateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
        "SourceEntity": "DashboardSourceEntityTypeDef",
        "Parameters": NotRequired["ParametersTypeDef"],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "VersionDescription": NotRequired[str],
        "DashboardPublishOptions": NotRequired["DashboardPublishOptionsTypeDef"],
        "ThemeArn": NotRequired[str],
    },
)

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSetRequestRequestTypeDef = TypedDict(
    "CreateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Mapping[str, "PhysicalTableTypeDef"],
        "ImportMode": DataSetImportModeType,
        "LogicalTableMap": NotRequired[Mapping[str, "LogicalTableTypeDef"]],
        "ColumnGroups": NotRequired[Sequence["ColumnGroupTypeDef"]],
        "FieldFolders": NotRequired[Mapping[str, "FieldFolderTypeDef"]],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RowLevelPermissionDataSet": NotRequired["RowLevelPermissionDataSetTypeDef"],
        "RowLevelPermissionTagConfiguration": NotRequired[
            "RowLevelPermissionTagConfigurationTypeDef"
        ],
        "ColumnLevelPermissionRules": NotRequired[Sequence["ColumnLevelPermissionRuleTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "DataSetUsageConfiguration": NotRequired["DataSetUsageConfigurationTypeDef"],
    },
)

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "DataSourceParameters": NotRequired["DataSourceParametersTypeDef"],
        "Credentials": NotRequired["DataSourceCredentialsTypeDef"],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "VpcConnectionProperties": NotRequired["VpcConnectionPropertiesTypeDef"],
        "SslProperties": NotRequired["SslPropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFolderMembershipRequestRequestTypeDef = TypedDict(
    "CreateFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

CreateFolderMembershipResponseTypeDef = TypedDict(
    "CreateFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "FolderMember": "FolderMemberTypeDef",
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFolderRequestRequestTypeDef = TypedDict(
    "CreateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": NotRequired[str],
        "FolderType": NotRequired[Literal["SHARED"]],
        "ParentFolderArn": NotRequired[str],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupMembershipRequestRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": "GroupMemberTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Description": NotRequired[str],
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
        "Namespace": str,
        "PolicyArn": NotRequired[str],
        "Identities": NotRequired[Mapping[str, Sequence[str]]],
    },
)

CreateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIngestionRequestRequestTypeDef = TypedDict(
    "CreateIngestionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "IngestionId": str,
        "AwsAccountId": str,
        "IngestionType": NotRequired[IngestionTypeType],
    },
)

CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": IngestionStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNamespaceRequestRequestTypeDef = TypedDict(
    "CreateNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "IdentityStore": Literal["QUICKSIGHT"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateAliasRequestRequestTypeDef = TypedDict(
    "CreateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

CreateTemplateAliasResponseTypeDef = TypedDict(
    "CreateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "SourceEntity": "TemplateSourceEntityTypeDef",
        "Name": NotRequired[str],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "VersionDescription": NotRequired[str],
    },
)

CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThemeAliasRequestRequestTypeDef = TypedDict(
    "CreateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

CreateThemeAliasResponseTypeDef = TypedDict(
    "CreateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThemeRequestRequestTypeDef = TypedDict(
    "CreateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "Name": str,
        "BaseThemeId": str,
        "Configuration": "ThemeConfigurationTypeDef",
        "VersionDescription": NotRequired[str],
        "Permissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "ThemeId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialPairTypeDef = TypedDict(
    "CredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
        "AlternateDataSourceParameters": NotRequired[Sequence["DataSourceParametersTypeDef"]],
    },
)

CustomSqlTypeDef = TypedDict(
    "CustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": NotRequired[Sequence["InputColumnTypeDef"]],
    },
)

DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef",
    {
        "Type": NotRequired[DashboardErrorTypeType],
        "Message": NotRequired[str],
    },
)

DashboardPublishOptionsTypeDef = TypedDict(
    "DashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": NotRequired["AdHocFilteringOptionTypeDef"],
        "ExportToCSVOption": NotRequired["ExportToCSVOptionTypeDef"],
        "SheetControlsOption": NotRequired["SheetControlsOptionTypeDef"],
    },
)

DashboardSearchFilterTypeDef = TypedDict(
    "DashboardSearchFilterTypeDef",
    {
        "Operator": Literal["StringEquals"],
        "Name": NotRequired[Literal["QUICKSIGHT_USER"]],
        "Value": NotRequired[str],
    },
)

DashboardSourceEntityTypeDef = TypedDict(
    "DashboardSourceEntityTypeDef",
    {
        "SourceTemplate": NotRequired["DashboardSourceTemplateTypeDef"],
    },
)

DashboardSourceTemplateTypeDef = TypedDict(
    "DashboardSourceTemplateTypeDef",
    {
        "DataSetReferences": Sequence["DataSetReferenceTypeDef"],
        "Arn": str,
    },
)

DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "DashboardId": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "PublishedVersionNumber": NotRequired[int],
        "LastPublishedTime": NotRequired[datetime],
    },
)

DashboardTypeDef = TypedDict(
    "DashboardTypeDef",
    {
        "DashboardId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired["DashboardVersionTypeDef"],
        "CreatedTime": NotRequired[datetime],
        "LastPublishedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

DashboardVersionSummaryTypeDef = TypedDict(
    "DashboardVersionSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[ResourceStatusType],
        "SourceEntityArn": NotRequired[str],
        "Description": NotRequired[str],
    },
)

DashboardVersionTypeDef = TypedDict(
    "DashboardVersionTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "Errors": NotRequired[List["DashboardErrorTypeDef"]],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[ResourceStatusType],
        "Arn": NotRequired[str],
        "SourceEntityArn": NotRequired[str],
        "DataSetArns": NotRequired[List[str]],
        "Description": NotRequired[str],
        "ThemeArn": NotRequired[str],
        "Sheets": NotRequired[List["SheetTypeDef"]],
    },
)

DataColorPaletteTypeDef = TypedDict(
    "DataColorPaletteTypeDef",
    {
        "Colors": NotRequired[Sequence[str]],
        "MinMaxGradient": NotRequired[Sequence[str]],
        "EmptyFillColor": NotRequired[str],
    },
)

DataSetConfigurationTypeDef = TypedDict(
    "DataSetConfigurationTypeDef",
    {
        "Placeholder": NotRequired[str],
        "DataSetSchema": NotRequired["DataSetSchemaTypeDef"],
        "ColumnGroupSchemaList": NotRequired[List["ColumnGroupSchemaTypeDef"]],
    },
)

DataSetReferenceTypeDef = TypedDict(
    "DataSetReferenceTypeDef",
    {
        "DataSetPlaceholder": str,
        "DataSetArn": str,
    },
)

DataSetSchemaTypeDef = TypedDict(
    "DataSetSchemaTypeDef",
    {
        "ColumnSchemaList": NotRequired[List["ColumnSchemaTypeDef"]],
    },
)

DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSetId": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "ImportMode": NotRequired[DataSetImportModeType],
        "RowLevelPermissionDataSet": NotRequired["RowLevelPermissionDataSetTypeDef"],
        "RowLevelPermissionTagConfigurationApplied": NotRequired[bool],
        "ColumnLevelPermissionRulesApplied": NotRequired[bool],
    },
)

DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSetId": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "PhysicalTableMap": NotRequired[Dict[str, "PhysicalTableTypeDef"]],
        "LogicalTableMap": NotRequired[Dict[str, "LogicalTableTypeDef"]],
        "OutputColumns": NotRequired[List["OutputColumnTypeDef"]],
        "ImportMode": NotRequired[DataSetImportModeType],
        "ConsumedSpiceCapacityInBytes": NotRequired[int],
        "ColumnGroups": NotRequired[List["ColumnGroupTypeDef"]],
        "FieldFolders": NotRequired[Dict[str, "FieldFolderTypeDef"]],
        "RowLevelPermissionDataSet": NotRequired["RowLevelPermissionDataSetTypeDef"],
        "RowLevelPermissionTagConfiguration": NotRequired[
            "RowLevelPermissionTagConfigurationTypeDef"
        ],
        "ColumnLevelPermissionRules": NotRequired[List["ColumnLevelPermissionRuleTypeDef"]],
        "DataSetUsageConfiguration": NotRequired["DataSetUsageConfigurationTypeDef"],
    },
)

DataSetUsageConfigurationTypeDef = TypedDict(
    "DataSetUsageConfigurationTypeDef",
    {
        "DisableUseAsDirectQuerySource": NotRequired[bool],
        "DisableUseAsImportedSource": NotRequired[bool],
    },
)

DataSourceCredentialsTypeDef = TypedDict(
    "DataSourceCredentialsTypeDef",
    {
        "CredentialPair": NotRequired["CredentialPairTypeDef"],
        "CopySourceArn": NotRequired[str],
    },
)

DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef",
    {
        "Type": NotRequired[DataSourceErrorInfoTypeType],
        "Message": NotRequired[str],
    },
)

DataSourceParametersTypeDef = TypedDict(
    "DataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": NotRequired["AmazonElasticsearchParametersTypeDef"],
        "AthenaParameters": NotRequired["AthenaParametersTypeDef"],
        "AuroraParameters": NotRequired["AuroraParametersTypeDef"],
        "AuroraPostgreSqlParameters": NotRequired["AuroraPostgreSqlParametersTypeDef"],
        "AwsIotAnalyticsParameters": NotRequired["AwsIotAnalyticsParametersTypeDef"],
        "JiraParameters": NotRequired["JiraParametersTypeDef"],
        "MariaDbParameters": NotRequired["MariaDbParametersTypeDef"],
        "MySqlParameters": NotRequired["MySqlParametersTypeDef"],
        "OracleParameters": NotRequired["OracleParametersTypeDef"],
        "PostgreSqlParameters": NotRequired["PostgreSqlParametersTypeDef"],
        "PrestoParameters": NotRequired["PrestoParametersTypeDef"],
        "RdsParameters": NotRequired["RdsParametersTypeDef"],
        "RedshiftParameters": NotRequired["RedshiftParametersTypeDef"],
        "S3Parameters": NotRequired["S3ParametersTypeDef"],
        "ServiceNowParameters": NotRequired["ServiceNowParametersTypeDef"],
        "SnowflakeParameters": NotRequired["SnowflakeParametersTypeDef"],
        "SparkParameters": NotRequired["SparkParametersTypeDef"],
        "SqlServerParameters": NotRequired["SqlServerParametersTypeDef"],
        "TeradataParameters": NotRequired["TeradataParametersTypeDef"],
        "TwitterParameters": NotRequired["TwitterParametersTypeDef"],
        "AmazonOpenSearchParameters": NotRequired["AmazonOpenSearchParametersTypeDef"],
        "ExasolParameters": NotRequired["ExasolParametersTypeDef"],
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSourceId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[DataSourceTypeType],
        "Status": NotRequired[ResourceStatusType],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "DataSourceParameters": NotRequired["DataSourceParametersTypeDef"],
        "AlternateDataSourceParameters": NotRequired[List["DataSourceParametersTypeDef"]],
        "VpcConnectionProperties": NotRequired["VpcConnectionPropertiesTypeDef"],
        "SslProperties": NotRequired["SslPropertiesTypeDef"],
        "ErrorInfo": NotRequired["DataSourceErrorInfoTypeDef"],
    },
)

DateTimeParameterTypeDef = TypedDict(
    "DateTimeParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[Union[datetime, str]],
    },
)

DecimalParameterTypeDef = TypedDict(
    "DecimalParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[float],
    },
)

DeleteAccountCustomizationRequestRequestTypeDef = TypedDict(
    "DeleteAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": NotRequired[str],
    },
)

DeleteAccountCustomizationResponseTypeDef = TypedDict(
    "DeleteAccountCustomizationResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "RecoveryWindowInDays": NotRequired[int],
        "ForceDeleteWithoutRecovery": NotRequired[bool],
    },
)

DeleteAnalysisResponseTypeDef = TypedDict(
    "DeleteAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "DeletionTime": datetime,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDashboardRequestRequestTypeDef = TypedDict(
    "DeleteDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": NotRequired[int],
    },
)

DeleteDashboardResponseTypeDef = TypedDict(
    "DeleteDashboardResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "DashboardId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DeleteDataSetResponseTypeDef = TypedDict(
    "DeleteDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFolderMembershipRequestRequestTypeDef = TypedDict(
    "DeleteFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

DeleteFolderMembershipResponseTypeDef = TypedDict(
    "DeleteFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFolderRequestRequestTypeDef = TypedDict(
    "DeleteFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DeleteFolderResponseTypeDef = TypedDict(
    "DeleteFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupMembershipRequestRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupMembershipResponseTypeDef = TypedDict(
    "DeleteGroupMembershipResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupResponseTypeDef = TypedDict(
    "DeleteGroupResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DeleteIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTemplateAliasRequestRequestTypeDef = TypedDict(
    "DeleteTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

DeleteTemplateAliasResponseTypeDef = TypedDict(
    "DeleteTemplateAliasResponseTypeDef",
    {
        "Status": int,
        "TemplateId": str,
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "VersionNumber": NotRequired[int],
    },
)

DeleteTemplateResponseTypeDef = TypedDict(
    "DeleteTemplateResponseTypeDef",
    {
        "RequestId": str,
        "Arn": str,
        "TemplateId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteThemeAliasRequestRequestTypeDef = TypedDict(
    "DeleteThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DeleteThemeAliasResponseTypeDef = TypedDict(
    "DeleteThemeAliasResponseTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "VersionNumber": NotRequired[int],
    },
)

DeleteThemeResponseTypeDef = TypedDict(
    "DeleteThemeResponseTypeDef",
    {
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserByPrincipalIdRequestRequestTypeDef = TypedDict(
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    {
        "PrincipalId": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "DeleteUserByPrincipalIdResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountCustomizationRequestRequestTypeDef = TypedDict(
    "DescribeAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": NotRequired[str],
        "Resolved": NotRequired[bool],
    },
)

DescribeAccountCustomizationResponseTypeDef = TypedDict(
    "DescribeAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountSettingsRequestRequestTypeDef = TypedDict(
    "DescribeAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeAccountSettingsResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseTypeDef",
    {
        "AccountSettings": "AccountSettingsTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisPermissionsResponseTypeDef = TypedDict(
    "DescribeAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisId": str,
        "AnalysisArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisResponseTypeDef = TypedDict(
    "DescribeAnalysisResponseTypeDef",
    {
        "Analysis": "AnalysisTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)

DescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "DescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "Status": int,
        "RequestId": str,
        "LinkSharingConfiguration": "LinkSharingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardRequestRequestTypeDef = TypedDict(
    "DescribeDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)

DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "Dashboard": "DashboardTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "DescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSetRequestRequestTypeDef = TypedDict(
    "DescribeDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetResponseTypeDef = TypedDict(
    "DescribeDataSetResponseTypeDef",
    {
        "DataSet": "DataSetTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "DescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderRequestRequestTypeDef = TypedDict(
    "DescribeFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderResponseTypeDef = TypedDict(
    "DescribeFolderResponseTypeDef",
    {
        "Status": int,
        "Folder": "FolderTypeDef",
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DescribeIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    {
        "IAMPolicyAssignment": "IAMPolicyAssignmentTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIngestionRequestRequestTypeDef = TypedDict(
    "DescribeIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

DescribeIngestionResponseTypeDef = TypedDict(
    "DescribeIngestionResponseTypeDef",
    {
        "Ingestion": "IngestionTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpRestrictionRequestRequestTypeDef = TypedDict(
    "DescribeIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeIpRestrictionResponseTypeDef = TypedDict(
    "DescribeIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "IpRestrictionRuleMap": Dict[str, str],
        "Enabled": bool,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "Namespace": "NamespaceInfoV2TypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplateAliasRequestRequestTypeDef = TypedDict(
    "DescribeTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

DescribeTemplateAliasResponseTypeDef = TypedDict(
    "DescribeTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)

DescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "DescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTemplateRequestRequestTypeDef = TypedDict(
    "DescribeTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)

DescribeTemplateResponseTypeDef = TypedDict(
    "DescribeTemplateResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemeAliasRequestRequestTypeDef = TypedDict(
    "DescribeThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DescribeThemeAliasResponseTypeDef = TypedDict(
    "DescribeThemeAliasResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)

DescribeThemePermissionsResponseTypeDef = TypedDict(
    "DescribeThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThemeRequestRequestTypeDef = TypedDict(
    "DescribeThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)

DescribeThemeResponseTypeDef = TypedDict(
    "DescribeThemeResponseTypeDef",
    {
        "Theme": "ThemeTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "Type": NotRequired[IngestionErrorTypeType],
        "Message": NotRequired[str],
    },
)

ExasolParametersTypeDef = TypedDict(
    "ExasolParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

ExportToCSVOptionTypeDef = TypedDict(
    "ExportToCSVOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)

FieldFolderTypeDef = TypedDict(
    "FieldFolderTypeDef",
    {
        "description": NotRequired[str],
        "columns": NotRequired[Sequence[str]],
    },
)

FilterOperationTypeDef = TypedDict(
    "FilterOperationTypeDef",
    {
        "ConditionExpression": str,
    },
)

FolderMemberTypeDef = TypedDict(
    "FolderMemberTypeDef",
    {
        "MemberId": NotRequired[str],
        "MemberType": NotRequired[MemberTypeType],
    },
)

FolderSearchFilterTypeDef = TypedDict(
    "FolderSearchFilterTypeDef",
    {
        "Operator": NotRequired[Literal["StringEquals"]],
        "Name": NotRequired[Literal["PARENT_FOLDER_ARN"]],
        "Value": NotRequired[str],
    },
)

FolderSummaryTypeDef = TypedDict(
    "FolderSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "FolderId": NotRequired[str],
        "Name": NotRequired[str],
        "FolderType": NotRequired[Literal["SHARED"]],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "FolderId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "FolderType": NotRequired[Literal["SHARED"]],
        "FolderPath": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef = TypedDict(
    "GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AuthorizedResourceArns": Sequence[str],
        "ExperienceConfiguration": "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
        "SessionLifetimeInMinutes": NotRequired[int],
        "SessionTags": NotRequired[Sequence["SessionTagTypeDef"]],
    },
)

GenerateEmbedUrlForAnonymousUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef = TypedDict(
    "GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserArn": str,
        "ExperienceConfiguration": "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
        "SessionLifetimeInMinutes": NotRequired[int],
    },
)

GenerateEmbedUrlForRegisteredUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GeoSpatialColumnGroupTypeDef = TypedDict(
    "GeoSpatialColumnGroupTypeDef",
    {
        "Name": str,
        "CountryCode": Literal["US"],
        "Columns": Sequence[str],
    },
)

GetDashboardEmbedUrlRequestRequestTypeDef = TypedDict(
    "GetDashboardEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "IdentityType": EmbeddingIdentityTypeType,
        "SessionLifetimeInMinutes": NotRequired[int],
        "UndoRedoDisabled": NotRequired[bool],
        "ResetDisabled": NotRequired[bool],
        "StatePersistenceEnabled": NotRequired[bool],
        "UserArn": NotRequired[str],
        "Namespace": NotRequired[str],
        "AdditionalDashboardIds": NotRequired[Sequence[str]],
    },
)

GetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "GetDashboardEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionEmbedUrlRequestRequestTypeDef = TypedDict(
    "GetSessionEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "EntryPoint": NotRequired[str],
        "SessionLifetimeInMinutes": NotRequired[int],
        "UserArn": NotRequired[str],
    },
)

GetSessionEmbedUrlResponseTypeDef = TypedDict(
    "GetSessionEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupMemberTypeDef = TypedDict(
    "GroupMemberTypeDef",
    {
        "Arn": NotRequired[str],
        "MemberName": NotRequired[str],
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Arn": NotRequired[str],
        "GroupName": NotRequired[str],
        "Description": NotRequired[str],
        "PrincipalId": NotRequired[str],
    },
)

GutterStyleTypeDef = TypedDict(
    "GutterStyleTypeDef",
    {
        "Show": NotRequired[bool],
    },
)

IAMPolicyAssignmentSummaryTypeDef = TypedDict(
    "IAMPolicyAssignmentSummaryTypeDef",
    {
        "AssignmentName": NotRequired[str],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
    },
)

IAMPolicyAssignmentTypeDef = TypedDict(
    "IAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "AssignmentName": NotRequired[str],
        "PolicyArn": NotRequired[str],
        "Identities": NotRequired[Dict[str, List[str]]],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
    },
)

IngestionTypeDef = TypedDict(
    "IngestionTypeDef",
    {
        "Arn": str,
        "IngestionStatus": IngestionStatusType,
        "CreatedTime": datetime,
        "IngestionId": NotRequired[str],
        "ErrorInfo": NotRequired["ErrorInfoTypeDef"],
        "RowInfo": NotRequired["RowInfoTypeDef"],
        "QueueInfo": NotRequired["QueueInfoTypeDef"],
        "IngestionTimeInSeconds": NotRequired[int],
        "IngestionSizeInBytes": NotRequired[int],
        "RequestSource": NotRequired[IngestionRequestSourceType],
        "RequestType": NotRequired[IngestionRequestTypeType],
    },
)

InputColumnTypeDef = TypedDict(
    "InputColumnTypeDef",
    {
        "Name": str,
        "Type": InputColumnDataTypeType,
    },
)

IntegerParameterTypeDef = TypedDict(
    "IntegerParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[int],
    },
)

JiraParametersTypeDef = TypedDict(
    "JiraParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

JoinInstructionTypeDef = TypedDict(
    "JoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": JoinTypeType,
        "OnClause": str,
        "LeftJoinKeyProperties": NotRequired["JoinKeyPropertiesTypeDef"],
        "RightJoinKeyProperties": NotRequired["JoinKeyPropertiesTypeDef"],
    },
)

JoinKeyPropertiesTypeDef = TypedDict(
    "JoinKeyPropertiesTypeDef",
    {
        "UniqueKey": NotRequired[bool],
    },
)

LinkSharingConfigurationTypeDef = TypedDict(
    "LinkSharingConfigurationTypeDef",
    {
        "Permissions": NotRequired[List["ResourcePermissionTypeDef"]],
    },
)

ListAnalysesRequestRequestTypeDef = TypedDict(
    "ListAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAnalysesResponseTypeDef = TypedDict(
    "ListAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDashboardVersionsRequestRequestTypeDef = TypedDict(
    "ListDashboardVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDashboardVersionsResponseTypeDef = TypedDict(
    "ListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List["DashboardVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDashboardsRequestRequestTypeDef = TypedDict(
    "ListDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSetsRequestRequestTypeDef = TypedDict(
    "ListDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List["DataSetSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "DataSources": List["DataSourceTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFolderMembersRequestRequestTypeDef = TypedDict(
    "ListFolderMembersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFolderMembersResponseTypeDef = TypedDict(
    "ListFolderMembersResponseTypeDef",
    {
        "Status": int,
        "FolderMemberList": List["MemberIdArnPairTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFoldersRequestRequestTypeDef = TypedDict(
    "ListFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFoldersResponseTypeDef = TypedDict(
    "ListFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List["FolderSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "ListGroupMembershipsRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List["GroupMemberTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIAMPolicyAssignmentsForUserRequestRequestTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIAMPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List["ActiveIAMPolicyAssignmentTypeDef"],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIAMPolicyAssignmentsRequestRequestTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIAMPolicyAssignmentsResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List["IAMPolicyAssignmentSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIngestionsRequestRequestTypeDef = TypedDict(
    "ListIngestionsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {
        "Ingestions": List["IngestionTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List["NamespaceInfoV2TypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
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
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplateAliasesRequestRequestTypeDef = TypedDict(
    "ListTemplateAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTemplateAliasesResponseTypeDef = TypedDict(
    "ListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List["TemplateAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "ListTemplateVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List["TemplateVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List["TemplateSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThemeAliasesRequestRequestTypeDef = TypedDict(
    "ListThemeAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListThemeAliasesResponseTypeDef = TypedDict(
    "ListThemeAliasesResponseTypeDef",
    {
        "ThemeAliasList": List["ThemeAliasTypeDef"],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThemeVersionsRequestRequestTypeDef = TypedDict(
    "ListThemeVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListThemeVersionsResponseTypeDef = TypedDict(
    "ListThemeVersionsResponseTypeDef",
    {
        "ThemeVersionSummaryList": List["ThemeVersionSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThemesRequestRequestTypeDef = TypedDict(
    "ListThemesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Type": NotRequired[ThemeTypeType],
    },
)

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "ThemeSummaryList": List["ThemeSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserGroupsRequestRequestTypeDef = TypedDict(
    "ListUserGroupsRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListUserGroupsResponseTypeDef = TypedDict(
    "ListUserGroupsResponseTypeDef",
    {
        "GroupList": List["GroupTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserList": List["UserTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogicalTableSourceTypeDef = TypedDict(
    "LogicalTableSourceTypeDef",
    {
        "JoinInstruction": NotRequired["JoinInstructionTypeDef"],
        "PhysicalTableId": NotRequired[str],
        "DataSetArn": NotRequired[str],
    },
)

LogicalTableTypeDef = TypedDict(
    "LogicalTableTypeDef",
    {
        "Alias": str,
        "Source": "LogicalTableSourceTypeDef",
        "DataTransforms": NotRequired[Sequence["TransformOperationTypeDef"]],
    },
)

ManifestFileLocationTypeDef = TypedDict(
    "ManifestFileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

MarginStyleTypeDef = TypedDict(
    "MarginStyleTypeDef",
    {
        "Show": NotRequired[bool],
    },
)

MariaDbParametersTypeDef = TypedDict(
    "MariaDbParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

MemberIdArnPairTypeDef = TypedDict(
    "MemberIdArnPairTypeDef",
    {
        "MemberId": NotRequired[str],
        "MemberArn": NotRequired[str],
    },
)

MySqlParametersTypeDef = TypedDict(
    "MySqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef",
    {
        "Type": NotRequired[NamespaceErrorTypeType],
        "Message": NotRequired[str],
    },
)

NamespaceInfoV2TypeDef = TypedDict(
    "NamespaceInfoV2TypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "CapacityRegion": NotRequired[str],
        "CreationStatus": NotRequired[NamespaceStatusType],
        "IdentityStore": NotRequired[Literal["QUICKSIGHT"]],
        "NamespaceError": NotRequired["NamespaceErrorTypeDef"],
    },
)

OracleParametersTypeDef = TypedDict(
    "OracleParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[ColumnDataTypeType],
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

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "StringParameters": NotRequired[Sequence["StringParameterTypeDef"]],
        "IntegerParameters": NotRequired[Sequence["IntegerParameterTypeDef"]],
        "DecimalParameters": NotRequired[Sequence["DecimalParameterTypeDef"]],
        "DateTimeParameters": NotRequired[Sequence["DateTimeParameterTypeDef"]],
    },
)

PhysicalTableTypeDef = TypedDict(
    "PhysicalTableTypeDef",
    {
        "RelationalTable": NotRequired["RelationalTableTypeDef"],
        "CustomSql": NotRequired["CustomSqlTypeDef"],
        "S3Source": NotRequired["S3SourceTypeDef"],
    },
)

PostgreSqlParametersTypeDef = TypedDict(
    "PostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

PrestoParametersTypeDef = TypedDict(
    "PrestoParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
    },
)

ProjectOperationTypeDef = TypedDict(
    "ProjectOperationTypeDef",
    {
        "ProjectedColumns": Sequence[str],
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "WaitingOnIngestion": str,
        "QueuedIngestion": str,
    },
)

RdsParametersTypeDef = TypedDict(
    "RdsParametersTypeDef",
    {
        "InstanceId": str,
        "Database": str,
    },
)

RedshiftParametersTypeDef = TypedDict(
    "RedshiftParametersTypeDef",
    {
        "Database": str,
        "Host": NotRequired[str],
        "Port": NotRequired[int],
        "ClusterId": NotRequired[str],
    },
)

RegisterUserRequestRequestTypeDef = TypedDict(
    "RegisterUserRequestRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "Email": str,
        "UserRole": UserRoleType,
        "AwsAccountId": str,
        "Namespace": str,
        "IamArn": NotRequired[str],
        "SessionName": NotRequired[str],
        "UserName": NotRequired[str],
        "CustomPermissionsName": NotRequired[str],
        "ExternalLoginFederationProviderType": NotRequired[str],
        "CustomFederationProviderUrl": NotRequired[str],
        "ExternalLoginId": NotRequired[str],
    },
)

RegisterUserResponseTypeDef = TypedDict(
    "RegisterUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisteredUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
    },
)

RegisteredUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": NotRequired["RegisteredUserDashboardEmbeddingConfigurationTypeDef"],
        "QuickSightConsole": NotRequired[
            "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef"
        ],
        "QSearchBar": NotRequired["RegisteredUserQSearchBarEmbeddingConfigurationTypeDef"],
    },
)

RegisteredUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": NotRequired[str],
    },
)

RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    {
        "InitialPath": NotRequired[str],
    },
)

RelationalTableTypeDef = TypedDict(
    "RelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": Sequence["InputColumnTypeDef"],
        "Catalog": NotRequired[str],
        "Schema": NotRequired[str],
    },
)

RenameColumnOperationTypeDef = TypedDict(
    "RenameColumnOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnName": str,
    },
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "Principal": str,
        "Actions": Sequence[str],
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

RestoreAnalysisRequestRequestTypeDef = TypedDict(
    "RestoreAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

RestoreAnalysisResponseTypeDef = TypedDict(
    "RestoreAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RowInfoTypeDef = TypedDict(
    "RowInfoTypeDef",
    {
        "RowsIngested": NotRequired[int],
        "RowsDropped": NotRequired[int],
        "TotalRowsInDataset": NotRequired[int],
    },
)

RowLevelPermissionDataSetTypeDef = TypedDict(
    "RowLevelPermissionDataSetTypeDef",
    {
        "Arn": str,
        "PermissionPolicy": RowLevelPermissionPolicyType,
        "Namespace": NotRequired[str],
        "FormatVersion": NotRequired[RowLevelPermissionFormatVersionType],
        "Status": NotRequired[StatusType],
    },
)

RowLevelPermissionTagConfigurationTypeDef = TypedDict(
    "RowLevelPermissionTagConfigurationTypeDef",
    {
        "TagRules": Sequence["RowLevelPermissionTagRuleTypeDef"],
        "Status": NotRequired[StatusType],
    },
)

RowLevelPermissionTagRuleTypeDef = TypedDict(
    "RowLevelPermissionTagRuleTypeDef",
    {
        "TagKey": str,
        "ColumnName": str,
        "TagMultiValueDelimiter": NotRequired[str],
        "MatchAllValue": NotRequired[str],
    },
)

S3ParametersTypeDef = TypedDict(
    "S3ParametersTypeDef",
    {
        "ManifestFileLocation": "ManifestFileLocationTypeDef",
    },
)

S3SourceTypeDef = TypedDict(
    "S3SourceTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": Sequence["InputColumnTypeDef"],
        "UploadSettings": NotRequired["UploadSettingsTypeDef"],
    },
)

SearchAnalysesRequestRequestTypeDef = TypedDict(
    "SearchAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence["AnalysisSearchFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchAnalysesResponseTypeDef = TypedDict(
    "SearchAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List["AnalysisSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchDashboardsRequestRequestTypeDef = TypedDict(
    "SearchDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence["DashboardSearchFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchDashboardsResponseTypeDef = TypedDict(
    "SearchDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List["DashboardSummaryTypeDef"],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchFoldersRequestRequestTypeDef = TypedDict(
    "SearchFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence["FolderSearchFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchFoldersResponseTypeDef = TypedDict(
    "SearchFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List["FolderSummaryTypeDef"],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceNowParametersTypeDef = TypedDict(
    "ServiceNowParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

SessionTagTypeDef = TypedDict(
    "SessionTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SheetControlsOptionTypeDef = TypedDict(
    "SheetControlsOptionTypeDef",
    {
        "VisibilityState": NotRequired[DashboardUIStateType],
    },
)

SheetStyleTypeDef = TypedDict(
    "SheetStyleTypeDef",
    {
        "Tile": NotRequired["TileStyleTypeDef"],
        "TileLayout": NotRequired["TileLayoutStyleTypeDef"],
    },
)

SheetTypeDef = TypedDict(
    "SheetTypeDef",
    {
        "SheetId": NotRequired[str],
        "Name": NotRequired[str],
    },
)

SnowflakeParametersTypeDef = TypedDict(
    "SnowflakeParametersTypeDef",
    {
        "Host": str,
        "Database": str,
        "Warehouse": str,
    },
)

SparkParametersTypeDef = TypedDict(
    "SparkParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

SqlServerParametersTypeDef = TypedDict(
    "SqlServerParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

SslPropertiesTypeDef = TypedDict(
    "SslPropertiesTypeDef",
    {
        "DisableSsl": NotRequired[bool],
    },
)

StringParameterTypeDef = TypedDict(
    "StringParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)

TagColumnOperationTypeDef = TypedDict(
    "TagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": Sequence["ColumnTagTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateAliasTypeDef = TypedDict(
    "TemplateAliasTypeDef",
    {
        "AliasName": NotRequired[str],
        "Arn": NotRequired[str],
        "TemplateVersionNumber": NotRequired[int],
    },
)

TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef",
    {
        "Type": NotRequired[TemplateErrorTypeType],
        "Message": NotRequired[str],
    },
)

TemplateSourceAnalysisTypeDef = TypedDict(
    "TemplateSourceAnalysisTypeDef",
    {
        "Arn": str,
        "DataSetReferences": Sequence["DataSetReferenceTypeDef"],
    },
)

TemplateSourceEntityTypeDef = TypedDict(
    "TemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": NotRequired["TemplateSourceAnalysisTypeDef"],
        "SourceTemplate": NotRequired["TemplateSourceTemplateTypeDef"],
    },
)

TemplateSourceTemplateTypeDef = TypedDict(
    "TemplateSourceTemplateTypeDef",
    {
        "Arn": str,
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "TemplateId": NotRequired[str],
        "Name": NotRequired[str],
        "LatestVersionNumber": NotRequired[int],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired["TemplateVersionTypeDef"],
        "TemplateId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "CreatedTime": NotRequired[datetime],
    },
)

TemplateVersionSummaryTypeDef = TypedDict(
    "TemplateVersionSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "CreatedTime": NotRequired[datetime],
        "Status": NotRequired[ResourceStatusType],
        "Description": NotRequired[str],
    },
)

TemplateVersionTypeDef = TypedDict(
    "TemplateVersionTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "Errors": NotRequired[List["TemplateErrorTypeDef"]],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[ResourceStatusType],
        "DataSetConfigurations": NotRequired[List["DataSetConfigurationTypeDef"]],
        "Description": NotRequired[str],
        "SourceEntityArn": NotRequired[str],
        "ThemeArn": NotRequired[str],
        "Sheets": NotRequired[List["SheetTypeDef"]],
    },
)

TeradataParametersTypeDef = TypedDict(
    "TeradataParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

ThemeAliasTypeDef = TypedDict(
    "ThemeAliasTypeDef",
    {
        "Arn": NotRequired[str],
        "AliasName": NotRequired[str],
        "ThemeVersionNumber": NotRequired[int],
    },
)

ThemeConfigurationTypeDef = TypedDict(
    "ThemeConfigurationTypeDef",
    {
        "DataColorPalette": NotRequired["DataColorPaletteTypeDef"],
        "UIColorPalette": NotRequired["UIColorPaletteTypeDef"],
        "Sheet": NotRequired["SheetStyleTypeDef"],
    },
)

ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef",
    {
        "Type": NotRequired[Literal["INTERNAL_FAILURE"]],
        "Message": NotRequired[str],
    },
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ThemeId": NotRequired[str],
        "LatestVersionNumber": NotRequired[int],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ThemeId": NotRequired[str],
        "Version": NotRequired["ThemeVersionTypeDef"],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "Type": NotRequired[ThemeTypeType],
    },
)

ThemeVersionSummaryTypeDef = TypedDict(
    "ThemeVersionSummaryTypeDef",
    {
        "VersionNumber": NotRequired[int],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Status": NotRequired[ResourceStatusType],
    },
)

ThemeVersionTypeDef = TypedDict(
    "ThemeVersionTypeDef",
    {
        "VersionNumber": NotRequired[int],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "BaseThemeId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Configuration": NotRequired["ThemeConfigurationTypeDef"],
        "Errors": NotRequired[List["ThemeErrorTypeDef"]],
        "Status": NotRequired[ResourceStatusType],
    },
)

TileLayoutStyleTypeDef = TypedDict(
    "TileLayoutStyleTypeDef",
    {
        "Gutter": NotRequired["GutterStyleTypeDef"],
        "Margin": NotRequired["MarginStyleTypeDef"],
    },
)

TileStyleTypeDef = TypedDict(
    "TileStyleTypeDef",
    {
        "Border": NotRequired["BorderStyleTypeDef"],
    },
)

TransformOperationTypeDef = TypedDict(
    "TransformOperationTypeDef",
    {
        "ProjectOperation": NotRequired["ProjectOperationTypeDef"],
        "FilterOperation": NotRequired["FilterOperationTypeDef"],
        "CreateColumnsOperation": NotRequired["CreateColumnsOperationTypeDef"],
        "RenameColumnOperation": NotRequired["RenameColumnOperationTypeDef"],
        "CastColumnTypeOperation": NotRequired["CastColumnTypeOperationTypeDef"],
        "TagColumnOperation": NotRequired["TagColumnOperationTypeDef"],
        "UntagColumnOperation": NotRequired["UntagColumnOperationTypeDef"],
    },
)

TwitterParametersTypeDef = TypedDict(
    "TwitterParametersTypeDef",
    {
        "Query": str,
        "MaxRows": int,
    },
)

UIColorPaletteTypeDef = TypedDict(
    "UIColorPaletteTypeDef",
    {
        "PrimaryForeground": NotRequired[str],
        "PrimaryBackground": NotRequired[str],
        "SecondaryForeground": NotRequired[str],
        "SecondaryBackground": NotRequired[str],
        "Accent": NotRequired[str],
        "AccentForeground": NotRequired[str],
        "Danger": NotRequired[str],
        "DangerForeground": NotRequired[str],
        "Warning": NotRequired[str],
        "WarningForeground": NotRequired[str],
        "Success": NotRequired[str],
        "SuccessForeground": NotRequired[str],
        "Dimension": NotRequired[str],
        "DimensionForeground": NotRequired[str],
        "Measure": NotRequired[str],
        "MeasureForeground": NotRequired[str],
    },
)

UntagColumnOperationTypeDef = TypedDict(
    "UntagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "TagNames": Sequence[ColumnTagNameType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "UpdateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "Namespace": NotRequired[str],
    },
)

UpdateAccountCustomizationResponseTypeDef = TypedDict(
    "UpdateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": "AccountCustomizationTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DefaultNamespace": str,
        "NotificationEmail": NotRequired[str],
    },
)

UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateAnalysisPermissionsResponseTypeDef = TypedDict(
    "UpdateAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisArn": str,
        "AnalysisId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAnalysisRequestRequestTypeDef = TypedDict(
    "UpdateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
        "SourceEntity": "AnalysisSourceEntityTypeDef",
        "Parameters": NotRequired["ParametersTypeDef"],
        "ThemeArn": NotRequired[str],
    },
)

UpdateAnalysisResponseTypeDef = TypedDict(
    "UpdateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "UpdateStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "GrantLinkPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokeLinkPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "UpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "LinkSharingConfiguration": "LinkSharingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDashboardPublishedVersionRequestRequestTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": int,
    },
)

UpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDashboardRequestRequestTypeDef = TypedDict(
    "UpdateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
        "SourceEntity": "DashboardSourceEntityTypeDef",
        "Parameters": NotRequired["ParametersTypeDef"],
        "VersionDescription": NotRequired[str],
        "DashboardPublishOptions": NotRequired["DashboardPublishOptionsTypeDef"],
        "ThemeArn": NotRequired[str],
    },
)

UpdateDashboardResponseTypeDef = TypedDict(
    "UpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "UpdateDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSetRequestRequestTypeDef = TypedDict(
    "UpdateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Mapping[str, "PhysicalTableTypeDef"],
        "ImportMode": DataSetImportModeType,
        "LogicalTableMap": NotRequired[Mapping[str, "LogicalTableTypeDef"]],
        "ColumnGroups": NotRequired[Sequence["ColumnGroupTypeDef"]],
        "FieldFolders": NotRequired[Mapping[str, "FieldFolderTypeDef"]],
        "RowLevelPermissionDataSet": NotRequired["RowLevelPermissionDataSetTypeDef"],
        "RowLevelPermissionTagConfiguration": NotRequired[
            "RowLevelPermissionTagConfigurationTypeDef"
        ],
        "ColumnLevelPermissionRules": NotRequired[Sequence["ColumnLevelPermissionRuleTypeDef"]],
        "DataSetUsageConfiguration": NotRequired["DataSetUsageConfigurationTypeDef"],
    },
)

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "UpdateDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "DataSourceParameters": NotRequired["DataSourceParametersTypeDef"],
        "Credentials": NotRequired["DataSourceCredentialsTypeDef"],
        "VpcConnectionProperties": NotRequired["VpcConnectionPropertiesTypeDef"],
        "SslProperties": NotRequired["SslPropertiesTypeDef"],
    },
)

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFolderPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateFolderPermissionsResponseTypeDef = TypedDict(
    "UpdateFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFolderRequestRequestTypeDef = TypedDict(
    "UpdateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": str,
    },
)

UpdateFolderResponseTypeDef = TypedDict(
    "UpdateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Description": NotRequired[str],
    },
)

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "PolicyArn": NotRequired[str],
        "Identities": NotRequired[Mapping[str, Sequence[str]]],
    },
)

UpdateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIpRestrictionRequestRequestTypeDef = TypedDict(
    "UpdateIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "IpRestrictionRuleMap": NotRequired[Mapping[str, str]],
        "Enabled": NotRequired[bool],
    },
)

UpdateIpRestrictionResponseTypeDef = TypedDict(
    "UpdateIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateAliasRequestRequestTypeDef = TypedDict(
    "UpdateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

UpdateTemplateAliasResponseTypeDef = TypedDict(
    "UpdateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": "TemplateAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "UpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "SourceEntity": "TemplateSourceEntityTypeDef",
        "VersionDescription": NotRequired[str],
        "Name": NotRequired[str],
    },
)

UpdateTemplateResponseTypeDef = TypedDict(
    "UpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThemeAliasRequestRequestTypeDef = TypedDict(
    "UpdateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

UpdateThemeAliasResponseTypeDef = TypedDict(
    "UpdateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": "ThemeAliasTypeDef",
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThemePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "GrantPermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
        "RevokePermissions": NotRequired[Sequence["ResourcePermissionTypeDef"]],
    },
)

UpdateThemePermissionsResponseTypeDef = TypedDict(
    "UpdateThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List["ResourcePermissionTypeDef"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThemeRequestRequestTypeDef = TypedDict(
    "UpdateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "BaseThemeId": str,
        "Name": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "Configuration": NotRequired["ThemeConfigurationTypeDef"],
    },
)

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "ThemeId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Email": str,
        "Role": UserRoleType,
        "CustomPermissionsName": NotRequired[str],
        "UnapplyCustomPermissions": NotRequired[bool],
        "ExternalLoginFederationProviderType": NotRequired[str],
        "CustomFederationProviderUrl": NotRequired[str],
        "ExternalLoginId": NotRequired[str],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadSettingsTypeDef = TypedDict(
    "UploadSettingsTypeDef",
    {
        "Format": NotRequired[FileFormatType],
        "StartFromRow": NotRequired[int],
        "ContainsHeader": NotRequired[bool],
        "TextQualifier": NotRequired[TextQualifierType],
        "Delimiter": NotRequired[str],
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Arn": NotRequired[str],
        "UserName": NotRequired[str],
        "Email": NotRequired[str],
        "Role": NotRequired[UserRoleType],
        "IdentityType": NotRequired[IdentityTypeType],
        "Active": NotRequired[bool],
        "PrincipalId": NotRequired[str],
        "CustomPermissionsName": NotRequired[str],
        "ExternalLoginFederationProviderType": NotRequired[str],
        "ExternalLoginFederationProviderUrl": NotRequired[str],
        "ExternalLoginId": NotRequired[str],
    },
)

VpcConnectionPropertiesTypeDef = TypedDict(
    "VpcConnectionPropertiesTypeDef",
    {
        "VpcConnectionArn": str,
    },
)
