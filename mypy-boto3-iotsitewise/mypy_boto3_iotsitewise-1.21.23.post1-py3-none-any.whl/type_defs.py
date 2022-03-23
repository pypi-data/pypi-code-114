"""
Type annotations for iotsitewise service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsitewise.type_defs import AccessPolicySummaryTypeDef

    data: AccessPolicySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AggregateTypeType,
    AssetModelStateType,
    AssetStateType,
    AuthModeType,
    BatchPutAssetPropertyValueErrorCodeType,
    CapabilitySyncStatusType,
    ComputeLocationType,
    ConfigurationStateType,
    DetailedErrorCodeType,
    DisassociatedDataStorageStateType,
    EncryptionTypeType,
    ErrorCodeType,
    ForwardingConfigStateType,
    IdentityTypeType,
    ListAssetsFilterType,
    ListTimeSeriesTypeType,
    LoggingLevelType,
    MonitorErrorCodeType,
    PermissionType,
    PortalStateType,
    PropertyDataTypeType,
    PropertyNotificationStateType,
    QualityType,
    ResourceTypeType,
    StorageTypeType,
    TimeOrderingType,
    TraversalDirectionType,
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
    "AccessPolicySummaryTypeDef",
    "AggregatedValueTypeDef",
    "AggregatesTypeDef",
    "AlarmsTypeDef",
    "AssetCompositeModelTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyInfoTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelCompositeModelDefinitionTypeDef",
    "AssetModelCompositeModelTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelStatusTypeDef",
    "AssetModelSummaryTypeDef",
    "AssetPropertyTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetRelationshipSummaryTypeDef",
    "AssetStatusTypeDef",
    "AssetSummaryTypeDef",
    "AssociateAssetsRequestRequestTypeDef",
    "AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "AttributeTypeDef",
    "BatchAssociateProjectAssetsRequestRequestTypeDef",
    "BatchAssociateProjectAssetsResponseTypeDef",
    "BatchDisassociateProjectAssetsRequestRequestTypeDef",
    "BatchDisassociateProjectAssetsResponseTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "BatchPutAssetPropertyValueRequestRequestTypeDef",
    "BatchPutAssetPropertyValueResponseTypeDef",
    "CompositeModelPropertyTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "ConfigurationStatusTypeDef",
    "CreateAccessPolicyRequestRequestTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateAssetModelRequestRequestTypeDef",
    "CreateAssetModelResponseTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "CreateAssetResponseTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateGatewayRequestRequestTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CustomerManagedS3StorageTypeDef",
    "DashboardSummaryTypeDef",
    "DeleteAccessPolicyRequestRequestTypeDef",
    "DeleteAssetModelRequestRequestTypeDef",
    "DeleteAssetModelResponseTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeleteAssetResponseTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteGatewayRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeletePortalResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteTimeSeriesRequestRequestTypeDef",
    "DescribeAccessPolicyRequestRequestTypeDef",
    "DescribeAccessPolicyResponseTypeDef",
    "DescribeAssetModelRequestRequestTypeDef",
    "DescribeAssetModelResponseTypeDef",
    "DescribeAssetPropertyRequestRequestTypeDef",
    "DescribeAssetPropertyResponseTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationRequestRequestTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    "DescribeGatewayRequestRequestTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePortalRequestRequestTypeDef",
    "DescribePortalResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeStorageConfigurationResponseTypeDef",
    "DescribeTimeSeriesRequestRequestTypeDef",
    "DescribeTimeSeriesResponseTypeDef",
    "DetailedErrorTypeDef",
    "DisassociateAssetsRequestRequestTypeDef",
    "DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    "ErrorDetailsTypeDef",
    "ExpressionVariableTypeDef",
    "ForwardingConfigTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "GatewayPlatformTypeDef",
    "GatewaySummaryTypeDef",
    "GetAssetPropertyAggregatesRequestRequestTypeDef",
    "GetAssetPropertyAggregatesResponseTypeDef",
    "GetAssetPropertyValueHistoryRequestRequestTypeDef",
    "GetAssetPropertyValueHistoryResponseTypeDef",
    "GetAssetPropertyValueRequestRequestTypeDef",
    "GetAssetPropertyValueResponseTypeDef",
    "GetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    "GreengrassTypeDef",
    "GreengrassV2TypeDef",
    "GroupIdentityTypeDef",
    "IAMRoleIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "IdentityTypeDef",
    "ImageFileTypeDef",
    "ImageLocationTypeDef",
    "ImageTypeDef",
    "InterpolatedAssetPropertyValueTypeDef",
    "ListAccessPoliciesRequestRequestTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAssetModelsRequestRequestTypeDef",
    "ListAssetModelsResponseTypeDef",
    "ListAssetRelationshipsRequestRequestTypeDef",
    "ListAssetRelationshipsResponseTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListAssetsResponseTypeDef",
    "ListAssociatedAssetsRequestRequestTypeDef",
    "ListAssociatedAssetsResponseTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListGatewaysRequestRequestTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "ListPortalsResponseTypeDef",
    "ListProjectAssetsRequestRequestTypeDef",
    "ListProjectAssetsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimeSeriesRequestRequestTypeDef",
    "ListTimeSeriesResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MeasurementProcessingConfigTypeDef",
    "MeasurementTypeDef",
    "MetricProcessingConfigTypeDef",
    "MetricTypeDef",
    "MetricWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "MultiLayerStorageTypeDef",
    "PaginatorConfigTypeDef",
    "PortalResourceTypeDef",
    "PortalStatusTypeDef",
    "PortalSummaryTypeDef",
    "ProjectResourceTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNotificationTypeDef",
    "PropertyTypeDef",
    "PropertyTypeTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutDefaultEncryptionConfigurationRequestRequestTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "PutStorageConfigurationRequestRequestTypeDef",
    "PutStorageConfigurationResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeInNanosTypeDef",
    "TimeSeriesSummaryTypeDef",
    "TransformProcessingConfigTypeDef",
    "TransformTypeDef",
    "TumblingWindowTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessPolicyRequestRequestTypeDef",
    "UpdateAssetModelRequestRequestTypeDef",
    "UpdateAssetModelResponseTypeDef",
    "UpdateAssetPropertyRequestRequestTypeDef",
    "UpdateAssetRequestRequestTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationRequestRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    "UpdateGatewayRequestRequestTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdatePortalResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UserIdentityTypeDef",
    "VariableValueTypeDef",
    "VariantTypeDef",
    "WaiterConfigTypeDef",
)

AccessPolicySummaryTypeDef = TypedDict(
    "AccessPolicySummaryTypeDef",
    {
        "id": str,
        "identity": "IdentityTypeDef",
        "resource": "ResourceTypeDef",
        "permission": PermissionType,
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
    },
)

AggregatedValueTypeDef = TypedDict(
    "AggregatedValueTypeDef",
    {
        "timestamp": datetime,
        "value": "AggregatesTypeDef",
        "quality": NotRequired[QualityType],
    },
)

AggregatesTypeDef = TypedDict(
    "AggregatesTypeDef",
    {
        "average": NotRequired[float],
        "count": NotRequired[float],
        "maximum": NotRequired[float],
        "minimum": NotRequired[float],
        "sum": NotRequired[float],
        "standardDeviation": NotRequired[float],
    },
)

AlarmsTypeDef = TypedDict(
    "AlarmsTypeDef",
    {
        "alarmRoleArn": str,
        "notificationLambdaArn": NotRequired[str],
    },
)

AssetCompositeModelTypeDef = TypedDict(
    "AssetCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
        "properties": List["AssetPropertyTypeDef"],
        "description": NotRequired[str],
    },
)

AssetErrorDetailsTypeDef = TypedDict(
    "AssetErrorDetailsTypeDef",
    {
        "assetId": str,
        "code": Literal["INTERNAL_FAILURE"],
        "message": str,
    },
)

AssetHierarchyInfoTypeDef = TypedDict(
    "AssetHierarchyInfoTypeDef",
    {
        "parentAssetId": NotRequired[str],
        "childAssetId": NotRequired[str],
    },
)

AssetHierarchyTypeDef = TypedDict(
    "AssetHierarchyTypeDef",
    {
        "name": str,
        "id": NotRequired[str],
    },
)

AssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "AssetModelCompositeModelDefinitionTypeDef",
    {
        "name": str,
        "type": str,
        "description": NotRequired[str],
        "properties": NotRequired[Sequence["AssetModelPropertyDefinitionTypeDef"]],
    },
)

AssetModelCompositeModelTypeDef = TypedDict(
    "AssetModelCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
        "description": NotRequired[str],
        "properties": NotRequired[List["AssetModelPropertyTypeDef"]],
    },
)

AssetModelHierarchyDefinitionTypeDef = TypedDict(
    "AssetModelHierarchyDefinitionTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
    },
)

AssetModelHierarchyTypeDef = TypedDict(
    "AssetModelHierarchyTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
        "id": NotRequired[str],
    },
)

AssetModelPropertyDefinitionTypeDef = TypedDict(
    "AssetModelPropertyDefinitionTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
    },
)

AssetModelPropertyTypeDef = TypedDict(
    "AssetModelPropertyTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
        "id": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
    },
)

AssetModelStatusTypeDef = TypedDict(
    "AssetModelStatusTypeDef",
    {
        "state": AssetModelStateType,
        "error": NotRequired["ErrorDetailsTypeDef"],
    },
)

AssetModelSummaryTypeDef = TypedDict(
    "AssetModelSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetModelStatusTypeDef",
    },
)

AssetPropertyTypeDef = TypedDict(
    "AssetPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
        "alias": NotRequired[str],
        "notification": NotRequired["PropertyNotificationTypeDef"],
        "dataTypeSpec": NotRequired[str],
        "unit": NotRequired[str],
    },
)

AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": "VariantTypeDef",
        "timestamp": "TimeInNanosTypeDef",
        "quality": NotRequired[QualityType],
    },
)

AssetRelationshipSummaryTypeDef = TypedDict(
    "AssetRelationshipSummaryTypeDef",
    {
        "relationshipType": Literal["HIERARCHY"],
        "hierarchyInfo": NotRequired["AssetHierarchyInfoTypeDef"],
    },
)

AssetStatusTypeDef = TypedDict(
    "AssetStatusTypeDef",
    {
        "state": AssetStateType,
        "error": NotRequired["ErrorDetailsTypeDef"],
    },
)

AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

AssociateAssetsRequestRequestTypeDef = TypedDict(
    "AssociateAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
        "clientToken": NotRequired[str],
    },
)

AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef = TypedDict(
    "AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
        "clientToken": NotRequired[str],
    },
)

AssociatedAssetsSummaryTypeDef = TypedDict(
    "AssociatedAssetsSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "defaultValue": NotRequired[str],
    },
)

BatchAssociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "BatchAssociateProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "assetIds": Sequence[str],
        "clientToken": NotRequired[str],
    },
)

BatchAssociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchAssociateProjectAssetsResponseTypeDef",
    {
        "errors": List["AssetErrorDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateProjectAssetsRequestRequestTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "assetIds": Sequence[str],
        "clientToken": NotRequired[str],
    },
)

BatchDisassociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsResponseTypeDef",
    {
        "errors": List["AssetErrorDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutAssetPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorEntryTypeDef",
    {
        "entryId": str,
        "errors": List["BatchPutAssetPropertyErrorTypeDef"],
    },
)

BatchPutAssetPropertyErrorTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorTypeDef",
    {
        "errorCode": BatchPutAssetPropertyValueErrorCodeType,
        "errorMessage": str,
        "timestamps": List["TimeInNanosTypeDef"],
    },
)

BatchPutAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "BatchPutAssetPropertyValueRequestRequestTypeDef",
    {
        "entries": Sequence["PutAssetPropertyValueEntryTypeDef"],
    },
)

BatchPutAssetPropertyValueResponseTypeDef = TypedDict(
    "BatchPutAssetPropertyValueResponseTypeDef",
    {
        "errorEntries": List["BatchPutAssetPropertyErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompositeModelPropertyTypeDef = TypedDict(
    "CompositeModelPropertyTypeDef",
    {
        "name": str,
        "type": str,
        "assetProperty": "PropertyTypeDef",
    },
)

ConfigurationErrorDetailsTypeDef = TypedDict(
    "ConfigurationErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
)

ConfigurationStatusTypeDef = TypedDict(
    "ConfigurationStatusTypeDef",
    {
        "state": ConfigurationStateType,
        "error": NotRequired["ConfigurationErrorDetailsTypeDef"],
    },
)

CreateAccessPolicyRequestRequestTypeDef = TypedDict(
    "CreateAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAccessPolicyResponseTypeDef = TypedDict(
    "CreateAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssetModelRequestRequestTypeDef = TypedDict(
    "CreateAssetModelRequestRequestTypeDef",
    {
        "assetModelName": str,
        "assetModelDescription": NotRequired[str],
        "assetModelProperties": NotRequired[Sequence["AssetModelPropertyDefinitionTypeDef"]],
        "assetModelHierarchies": NotRequired[Sequence["AssetModelHierarchyDefinitionTypeDef"]],
        "assetModelCompositeModels": NotRequired[
            Sequence["AssetModelCompositeModelDefinitionTypeDef"]
        ],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssetModelResponseTypeDef = TypedDict(
    "CreateAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssetRequestRequestTypeDef = TypedDict(
    "CreateAssetRequestRequestTypeDef",
    {
        "assetName": str,
        "assetModelId": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDashboardRequestRequestTypeDef = TypedDict(
    "CreateDashboardRequestRequestTypeDef",
    {
        "projectId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
        "dashboardDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGatewayRequestRequestTypeDef = TypedDict(
    "CreateGatewayRequestRequestTypeDef",
    {
        "gatewayName": str,
        "gatewayPlatform": "GatewayPlatformTypeDef",
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateGatewayResponseTypeDef = TypedDict(
    "CreateGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
        "portalDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "portalLogoImageFile": NotRequired["ImageFileTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
        "portalAuthMode": NotRequired[AuthModeType],
        "notificationSenderEmail": NotRequired[str],
        "alarms": NotRequired["AlarmsTypeDef"],
    },
)

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalStartUrl": str,
        "portalStatus": "PortalStatusTypeDef",
        "ssoApplicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "portalId": str,
        "projectName": str,
        "projectDescription": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerManagedS3StorageTypeDef = TypedDict(
    "CustomerManagedS3StorageTypeDef",
    {
        "s3ResourceArn": str,
        "roleArn": str,
    },
)

DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "description": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
    },
)

DeleteAccessPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteAssetModelRequestRequestTypeDef = TypedDict(
    "DeleteAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteAssetModelResponseTypeDef = TypedDict(
    "DeleteAssetModelResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "assetId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteAssetResponseTypeDef = TypedDict(
    "DeleteAssetResponseTypeDef",
    {
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDashboardRequestRequestTypeDef = TypedDict(
    "DeleteDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteGatewayRequestRequestTypeDef = TypedDict(
    "DeleteGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
    },
)

DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalId": str,
        "clientToken": NotRequired[str],
    },
)

DeletePortalResponseTypeDef = TypedDict(
    "DeletePortalResponseTypeDef",
    {
        "portalStatus": "PortalStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteTimeSeriesRequestRequestTypeDef = TypedDict(
    "DeleteTimeSeriesRequestRequestTypeDef",
    {
        "alias": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

DescribeAccessPolicyRequestRequestTypeDef = TypedDict(
    "DescribeAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
    },
)

DescribeAccessPolicyResponseTypeDef = TypedDict(
    "DescribeAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
        "accessPolicyCreationDate": datetime,
        "accessPolicyLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetModelRequestRequestTypeDef = TypedDict(
    "DescribeAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
    },
)

DescribeAssetModelResponseTypeDef = TypedDict(
    "DescribeAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelName": str,
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelTypeDef"],
        "assetModelCreationDate": datetime,
        "assetModelLastUpdateDate": datetime,
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetPropertyRequestRequestTypeDef = TypedDict(
    "DescribeAssetPropertyRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
    },
)

DescribeAssetPropertyResponseTypeDef = TypedDict(
    "DescribeAssetPropertyResponseTypeDef",
    {
        "assetId": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperty": "PropertyTypeDef",
        "compositeModel": "CompositeModelPropertyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetRequestRequestTypeDef = TypedDict(
    "DescribeAssetRequestRequestTypeDef",
    {
        "assetId": str,
    },
)

DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperties": List["AssetPropertyTypeDef"],
        "assetHierarchies": List["AssetHierarchyTypeDef"],
        "assetCompositeModels": List["AssetCompositeModelTypeDef"],
        "assetCreationDate": datetime,
        "assetLastUpdateDate": datetime,
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardRequestRequestTypeDef = TypedDict(
    "DescribeDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
    },
)

DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "dashboardName": str,
        "projectId": str,
        "dashboardDescription": str,
        "dashboardDefinition": str,
        "dashboardCreationDate": datetime,
        "dashboardLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayCapabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
    },
)

DescribeGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayRequestRequestTypeDef = TypedDict(
    "DescribeGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
    },
)

DescribeGatewayResponseTypeDef = TypedDict(
    "DescribeGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "gatewayArn": str,
        "gatewayPlatform": "GatewayPlatformTypeDef",
        "gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"],
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortalRequestRequestTypeDef = TypedDict(
    "DescribePortalRequestRequestTypeDef",
    {
        "portalId": str,
    },
)

DescribePortalResponseTypeDef = TypedDict(
    "DescribePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalName": str,
        "portalDescription": str,
        "portalClientId": str,
        "portalStartUrl": str,
        "portalContactEmail": str,
        "portalStatus": "PortalStatusTypeDef",
        "portalCreationDate": datetime,
        "portalLastUpdateDate": datetime,
        "portalLogoImageLocation": "ImageLocationTypeDef",
        "roleArn": str,
        "portalAuthMode": AuthModeType,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectId": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "projectName": str,
        "portalId": str,
        "projectDescription": str,
        "projectCreationDate": datetime,
        "projectLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorageConfigurationResponseTypeDef = TypedDict(
    "DescribeStorageConfigurationResponseTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": "MultiLayerStorageTypeDef",
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "configurationStatus": "ConfigurationStatusTypeDef",
        "lastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeSeriesRequestRequestTypeDef = TypedDict(
    "DescribeTimeSeriesRequestRequestTypeDef",
    {
        "alias": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
    },
)

DescribeTimeSeriesResponseTypeDef = TypedDict(
    "DescribeTimeSeriesResponseTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "alias": str,
        "timeSeriesId": str,
        "dataType": PropertyDataTypeType,
        "dataTypeSpec": str,
        "timeSeriesCreationDate": datetime,
        "timeSeriesLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetailedErrorTypeDef = TypedDict(
    "DetailedErrorTypeDef",
    {
        "code": DetailedErrorCodeType,
        "message": str,
    },
)

DisassociateAssetsRequestRequestTypeDef = TypedDict(
    "DisassociateAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
        "clientToken": NotRequired[str],
    },
)

DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef = TypedDict(
    "DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef",
    {
        "alias": str,
        "assetId": str,
        "propertyId": str,
        "clientToken": NotRequired[str],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
        "details": NotRequired[List["DetailedErrorTypeDef"]],
    },
)

ExpressionVariableTypeDef = TypedDict(
    "ExpressionVariableTypeDef",
    {
        "name": str,
        "value": "VariableValueTypeDef",
    },
)

ForwardingConfigTypeDef = TypedDict(
    "ForwardingConfigTypeDef",
    {
        "state": ForwardingConfigStateType,
    },
)

GatewayCapabilitySummaryTypeDef = TypedDict(
    "GatewayCapabilitySummaryTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
    },
)

GatewayPlatformTypeDef = TypedDict(
    "GatewayPlatformTypeDef",
    {
        "greengrass": NotRequired["GreengrassTypeDef"],
        "greengrassV2": NotRequired["GreengrassV2TypeDef"],
    },
)

GatewaySummaryTypeDef = TypedDict(
    "GatewaySummaryTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "gatewayPlatform": NotRequired["GatewayPlatformTypeDef"],
        "gatewayCapabilitySummaries": NotRequired[List["GatewayCapabilitySummaryTypeDef"]],
    },
)

GetAssetPropertyAggregatesRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyAggregatesRequestRequestTypeDef",
    {
        "aggregateTypes": Sequence[AggregateTypeType],
        "resolution": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "GetAssetPropertyAggregatesResponseTypeDef",
    {
        "aggregatedValues": List["AggregatedValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryRequestRequestTypeDef",
    {
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startDate": NotRequired[Union[datetime, str]],
        "endDate": NotRequired[Union[datetime, str]],
        "qualities": NotRequired[Sequence[QualityType]],
        "timeOrdering": NotRequired[TimeOrderingType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryResponseTypeDef",
    {
        "assetPropertyValueHistory": List["AssetPropertyValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssetPropertyValueRequestRequestTypeDef = TypedDict(
    "GetAssetPropertyValueRequestRequestTypeDef",
    {
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
    },
)

GetAssetPropertyValueResponseTypeDef = TypedDict(
    "GetAssetPropertyValueResponseTypeDef",
    {
        "propertyValue": "AssetPropertyValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInterpolatedAssetPropertyValuesRequestRequestTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesRequestRequestTypeDef",
    {
        "startTimeInSeconds": int,
        "endTimeInSeconds": int,
        "quality": QualityType,
        "intervalInSeconds": int,
        "type": str,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "startTimeOffsetInNanos": NotRequired[int],
        "endTimeOffsetInNanos": NotRequired[int],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "intervalWindowInSeconds": NotRequired[int],
    },
)

GetInterpolatedAssetPropertyValuesResponseTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    {
        "interpolatedAssetPropertyValues": List["InterpolatedAssetPropertyValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GreengrassTypeDef = TypedDict(
    "GreengrassTypeDef",
    {
        "groupArn": str,
    },
)

GreengrassV2TypeDef = TypedDict(
    "GreengrassV2TypeDef",
    {
        "coreDeviceThingName": str,
    },
)

GroupIdentityTypeDef = TypedDict(
    "GroupIdentityTypeDef",
    {
        "id": str,
    },
)

IAMRoleIdentityTypeDef = TypedDict(
    "IAMRoleIdentityTypeDef",
    {
        "arn": str,
    },
)

IAMUserIdentityTypeDef = TypedDict(
    "IAMUserIdentityTypeDef",
    {
        "arn": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "user": NotRequired["UserIdentityTypeDef"],
        "group": NotRequired["GroupIdentityTypeDef"],
        "iamUser": NotRequired["IAMUserIdentityTypeDef"],
        "iamRole": NotRequired["IAMRoleIdentityTypeDef"],
    },
)

ImageFileTypeDef = TypedDict(
    "ImageFileTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "type": Literal["PNG"],
    },
)

ImageLocationTypeDef = TypedDict(
    "ImageLocationTypeDef",
    {
        "id": str,
        "url": str,
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "id": NotRequired[str],
        "file": NotRequired["ImageFileTypeDef"],
    },
)

InterpolatedAssetPropertyValueTypeDef = TypedDict(
    "InterpolatedAssetPropertyValueTypeDef",
    {
        "timestamp": "TimeInNanosTypeDef",
        "value": "VariantTypeDef",
    },
)

ListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestRequestTypeDef",
    {
        "identityType": NotRequired[IdentityTypeType],
        "identityId": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "iamArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAccessPoliciesResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseTypeDef",
    {
        "accessPolicySummaries": List["AccessPolicySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetModelsRequestRequestTypeDef = TypedDict(
    "ListAssetModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssetModelsResponseTypeDef = TypedDict(
    "ListAssetModelsResponseTypeDef",
    {
        "assetModelSummaries": List["AssetModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetRelationshipsRequestRequestTypeDef = TypedDict(
    "ListAssetRelationshipsRequestRequestTypeDef",
    {
        "assetId": str,
        "traversalType": Literal["PATH_TO_ROOT"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssetRelationshipsResponseTypeDef = TypedDict(
    "ListAssetRelationshipsResponseTypeDef",
    {
        "assetRelationshipSummaries": List["AssetRelationshipSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "assetModelId": NotRequired[str],
        "filter": NotRequired[ListAssetsFilterType],
    },
)

ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "assetSummaries": List["AssetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociatedAssetsRequestRequestTypeDef = TypedDict(
    "ListAssociatedAssetsRequestRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": NotRequired[str],
        "traversalDirection": NotRequired[TraversalDirectionType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssociatedAssetsResponseTypeDef = TypedDict(
    "ListAssociatedAssetsResponseTypeDef",
    {
        "assetSummaries": List["AssociatedAssetsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDashboardsRequestRequestTypeDef = TypedDict(
    "ListDashboardsRequestRequestTypeDef",
    {
        "projectId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "dashboardSummaries": List["DashboardSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysRequestRequestTypeDef = TypedDict(
    "ListGatewaysRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "gatewaySummaries": List["GatewaySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "portalSummaries": List["PortalSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectAssetsRequestRequestTypeDef = TypedDict(
    "ListProjectAssetsRequestRequestTypeDef",
    {
        "projectId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListProjectAssetsResponseTypeDef = TypedDict(
    "ListProjectAssetsResponseTypeDef",
    {
        "assetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "portalId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projectSummaries": List["ProjectSummaryTypeDef"],
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

ListTimeSeriesRequestRequestTypeDef = TypedDict(
    "ListTimeSeriesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "assetId": NotRequired[str],
        "aliasPrefix": NotRequired[str],
        "timeSeriesType": NotRequired[ListTimeSeriesTypeType],
    },
)

ListTimeSeriesResponseTypeDef = TypedDict(
    "ListTimeSeriesResponseTypeDef",
    {
        "TimeSeriesSummaries": List["TimeSeriesSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "level": LoggingLevelType,
    },
)

MeasurementProcessingConfigTypeDef = TypedDict(
    "MeasurementProcessingConfigTypeDef",
    {
        "forwardingConfig": "ForwardingConfigTypeDef",
    },
)

MeasurementTypeDef = TypedDict(
    "MeasurementTypeDef",
    {
        "processingConfig": NotRequired["MeasurementProcessingConfigTypeDef"],
    },
)

MetricProcessingConfigTypeDef = TypedDict(
    "MetricProcessingConfigTypeDef",
    {
        "computeLocation": ComputeLocationType,
    },
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "expression": str,
        "variables": Sequence["ExpressionVariableTypeDef"],
        "window": "MetricWindowTypeDef",
        "processingConfig": NotRequired["MetricProcessingConfigTypeDef"],
    },
)

MetricWindowTypeDef = TypedDict(
    "MetricWindowTypeDef",
    {
        "tumbling": NotRequired["TumblingWindowTypeDef"],
    },
)

MonitorErrorDetailsTypeDef = TypedDict(
    "MonitorErrorDetailsTypeDef",
    {
        "code": NotRequired[MonitorErrorCodeType],
        "message": NotRequired[str],
    },
)

MultiLayerStorageTypeDef = TypedDict(
    "MultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": "CustomerManagedS3StorageTypeDef",
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

PortalResourceTypeDef = TypedDict(
    "PortalResourceTypeDef",
    {
        "id": str,
    },
)

PortalStatusTypeDef = TypedDict(
    "PortalStatusTypeDef",
    {
        "state": PortalStateType,
        "error": NotRequired["MonitorErrorDetailsTypeDef"],
    },
)

PortalSummaryTypeDef = TypedDict(
    "PortalSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "startUrl": str,
        "status": "PortalStatusTypeDef",
        "description": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
        "roleArn": NotRequired[str],
    },
)

ProjectResourceTypeDef = TypedDict(
    "ProjectResourceTypeDef",
    {
        "id": str,
    },
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "description": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastUpdateDate": NotRequired[datetime],
    },
)

PropertyNotificationTypeDef = TypedDict(
    "PropertyNotificationTypeDef",
    {
        "topic": str,
        "state": PropertyNotificationStateType,
    },
)

PropertyTypeDef = TypedDict(
    "PropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
        "alias": NotRequired[str],
        "notification": NotRequired["PropertyNotificationTypeDef"],
        "unit": NotRequired[str],
        "type": NotRequired["PropertyTypeTypeDef"],
    },
)

PropertyTypeTypeDef = TypedDict(
    "PropertyTypeTypeDef",
    {
        "attribute": NotRequired["AttributeTypeDef"],
        "measurement": NotRequired["MeasurementTypeDef"],
        "transform": NotRequired["TransformTypeDef"],
        "metric": NotRequired["MetricTypeDef"],
    },
)

PutAssetPropertyValueEntryTypeDef = TypedDict(
    "PutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "propertyValues": Sequence["AssetPropertyValueTypeDef"],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
    },
)

PutDefaultEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "PutDefaultEncryptionConfigurationRequestRequestTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyId": NotRequired[str],
    },
)

PutDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

PutStorageConfigurationRequestRequestTypeDef = TypedDict(
    "PutStorageConfigurationRequestRequestTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": NotRequired["MultiLayerStorageTypeDef"],
        "disassociatedDataStorage": NotRequired[DisassociatedDataStorageStateType],
        "retentionPeriod": NotRequired["RetentionPeriodTypeDef"],
    },
)

PutStorageConfigurationResponseTypeDef = TypedDict(
    "PutStorageConfigurationResponseTypeDef",
    {
        "storageType": StorageTypeType,
        "multiLayerStorage": "MultiLayerStorageTypeDef",
        "disassociatedDataStorage": DisassociatedDataStorageStateType,
        "retentionPeriod": "RetentionPeriodTypeDef",
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "portal": NotRequired["PortalResourceTypeDef"],
        "project": NotRequired["ProjectResourceTypeDef"],
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "numberOfDays": NotRequired[int],
        "unlimited": NotRequired[bool],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TimeInNanosTypeDef = TypedDict(
    "TimeInNanosTypeDef",
    {
        "timeInSeconds": int,
        "offsetInNanos": NotRequired[int],
    },
)

TimeSeriesSummaryTypeDef = TypedDict(
    "TimeSeriesSummaryTypeDef",
    {
        "timeSeriesId": str,
        "dataType": PropertyDataTypeType,
        "timeSeriesCreationDate": datetime,
        "timeSeriesLastUpdateDate": datetime,
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "alias": NotRequired[str],
        "dataTypeSpec": NotRequired[str],
    },
)

TransformProcessingConfigTypeDef = TypedDict(
    "TransformProcessingConfigTypeDef",
    {
        "computeLocation": ComputeLocationType,
        "forwardingConfig": NotRequired["ForwardingConfigTypeDef"],
    },
)

TransformTypeDef = TypedDict(
    "TransformTypeDef",
    {
        "expression": str,
        "variables": Sequence["ExpressionVariableTypeDef"],
        "processingConfig": NotRequired["TransformProcessingConfigTypeDef"],
    },
)

TumblingWindowTypeDef = TypedDict(
    "TumblingWindowTypeDef",
    {
        "interval": str,
        "offset": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateAccessPolicyRequestRequestTypeDef = TypedDict(
    "UpdateAccessPolicyRequestRequestTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
        "clientToken": NotRequired[str],
    },
)

UpdateAssetModelRequestRequestTypeDef = TypedDict(
    "UpdateAssetModelRequestRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelName": str,
        "assetModelDescription": NotRequired[str],
        "assetModelProperties": NotRequired[Sequence["AssetModelPropertyTypeDef"]],
        "assetModelHierarchies": NotRequired[Sequence["AssetModelHierarchyTypeDef"]],
        "assetModelCompositeModels": NotRequired[Sequence["AssetModelCompositeModelTypeDef"]],
        "clientToken": NotRequired[str],
    },
)

UpdateAssetModelResponseTypeDef = TypedDict(
    "UpdateAssetModelResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssetPropertyRequestRequestTypeDef = TypedDict(
    "UpdateAssetPropertyRequestRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": NotRequired[str],
        "propertyNotificationState": NotRequired[PropertyNotificationStateType],
        "clientToken": NotRequired[str],
    },
)

UpdateAssetRequestRequestTypeDef = TypedDict(
    "UpdateAssetRequestRequestTypeDef",
    {
        "assetId": str,
        "assetName": str,
        "clientToken": NotRequired[str],
    },
)

UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef",
    {
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDashboardRequestRequestTypeDef = TypedDict(
    "UpdateDashboardRequestRequestTypeDef",
    {
        "dashboardId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
        "dashboardDescription": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

UpdateGatewayCapabilityConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
    },
)

UpdateGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayRequestRequestTypeDef = TypedDict(
    "UpdateGatewayRequestRequestTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
    },
)

UpdatePortalRequestRequestTypeDef = TypedDict(
    "UpdatePortalRequestRequestTypeDef",
    {
        "portalId": str,
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
        "portalDescription": NotRequired[str],
        "portalLogoImage": NotRequired["ImageTypeDef"],
        "clientToken": NotRequired[str],
        "notificationSenderEmail": NotRequired[str],
        "alarms": NotRequired["AlarmsTypeDef"],
    },
)

UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portalStatus": "PortalStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "projectName": str,
        "projectDescription": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "id": str,
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "propertyId": str,
        "hierarchyId": NotRequired[str],
    },
)

VariantTypeDef = TypedDict(
    "VariantTypeDef",
    {
        "stringValue": NotRequired[str],
        "integerValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "booleanValue": NotRequired[bool],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
