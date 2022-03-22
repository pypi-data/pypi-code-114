"""
Type annotations for appstream service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef

    data: AccessEndpointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ActionType,
    ApplicationAttributeType,
    AppVisibilityType,
    AuthenticationTypeType,
    FleetAttributeType,
    FleetErrorCodeType,
    FleetStateType,
    FleetTypeType,
    ImageBuilderStateChangeReasonCodeType,
    ImageBuilderStateType,
    ImageStateChangeReasonCodeType,
    ImageStateType,
    MessageActionType,
    PermissionType,
    PlatformTypeType,
    SessionConnectionStateType,
    SessionStateType,
    StackAttributeType,
    StackErrorCodeType,
    StorageConnectorTypeType,
    StreamViewType,
    UsageReportExecutionErrorCodeType,
    UserStackAssociationErrorCodeType,
    VisibilityTypeType,
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
    "AccessEndpointTypeDef",
    "AppBlockTypeDef",
    "ApplicationFleetAssociationTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "ApplicationSettingsTypeDef",
    "ApplicationTypeDef",
    "AssociateApplicationFleetRequestRequestTypeDef",
    "AssociateApplicationFleetResultTypeDef",
    "AssociateApplicationToEntitlementRequestRequestTypeDef",
    "AssociateFleetRequestRequestTypeDef",
    "BatchAssociateUserStackRequestRequestTypeDef",
    "BatchAssociateUserStackResultTypeDef",
    "BatchDisassociateUserStackRequestRequestTypeDef",
    "BatchDisassociateUserStackResultTypeDef",
    "ComputeCapacityStatusTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageRequestRequestTypeDef",
    "CopyImageResponseTypeDef",
    "CreateAppBlockRequestRequestTypeDef",
    "CreateAppBlockResultTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResultTypeDef",
    "CreateDirectoryConfigRequestRequestTypeDef",
    "CreateDirectoryConfigResultTypeDef",
    "CreateEntitlementRequestRequestTypeDef",
    "CreateEntitlementResultTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResultTypeDef",
    "CreateImageBuilderRequestRequestTypeDef",
    "CreateImageBuilderResultTypeDef",
    "CreateImageBuilderStreamingURLRequestRequestTypeDef",
    "CreateImageBuilderStreamingURLResultTypeDef",
    "CreateStackRequestRequestTypeDef",
    "CreateStackResultTypeDef",
    "CreateStreamingURLRequestRequestTypeDef",
    "CreateStreamingURLResultTypeDef",
    "CreateUpdatedImageRequestRequestTypeDef",
    "CreateUpdatedImageResultTypeDef",
    "CreateUsageReportSubscriptionResultTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DeleteAppBlockRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteDirectoryConfigRequestRequestTypeDef",
    "DeleteEntitlementRequestRequestTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteImageBuilderRequestRequestTypeDef",
    "DeleteImageBuilderResultTypeDef",
    "DeleteImagePermissionsRequestRequestTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageResultTypeDef",
    "DeleteStackRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeAppBlocksRequestRequestTypeDef",
    "DescribeAppBlocksResultTypeDef",
    "DescribeApplicationFleetAssociationsRequestRequestTypeDef",
    "DescribeApplicationFleetAssociationsResultTypeDef",
    "DescribeApplicationsRequestRequestTypeDef",
    "DescribeApplicationsResultTypeDef",
    "DescribeDirectoryConfigsRequestRequestTypeDef",
    "DescribeDirectoryConfigsResultTypeDef",
    "DescribeEntitlementsRequestRequestTypeDef",
    "DescribeEntitlementsResultTypeDef",
    "DescribeFleetsRequestRequestTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeImageBuildersRequestRequestTypeDef",
    "DescribeImageBuildersResultTypeDef",
    "DescribeImagePermissionsRequestRequestTypeDef",
    "DescribeImagePermissionsResultTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeSessionsRequestRequestTypeDef",
    "DescribeSessionsResultTypeDef",
    "DescribeStacksRequestRequestTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeUsageReportSubscriptionsRequestRequestTypeDef",
    "DescribeUsageReportSubscriptionsResultTypeDef",
    "DescribeUserStackAssociationsRequestRequestTypeDef",
    "DescribeUserStackAssociationsResultTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "DescribeUsersResultTypeDef",
    "DirectoryConfigTypeDef",
    "DisableUserRequestRequestTypeDef",
    "DisassociateApplicationFleetRequestRequestTypeDef",
    "DisassociateApplicationFromEntitlementRequestRequestTypeDef",
    "DisassociateFleetRequestRequestTypeDef",
    "DomainJoinInfoTypeDef",
    "EnableUserRequestRequestTypeDef",
    "EntitledApplicationTypeDef",
    "EntitlementAttributeTypeDef",
    "EntitlementTypeDef",
    "ExpireSessionRequestRequestTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "ListAssociatedFleetsRequestRequestTypeDef",
    "ListAssociatedFleetsResultTypeDef",
    "ListAssociatedStacksRequestRequestTypeDef",
    "ListAssociatedStacksResultTypeDef",
    "ListEntitledApplicationsRequestRequestTypeDef",
    "ListEntitledApplicationsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceErrorTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "ScriptDetailsTypeDef",
    "ServiceAccountCredentialsTypeDef",
    "SessionTypeDef",
    "SharedImagePermissionsTypeDef",
    "StackErrorTypeDef",
    "StackTypeDef",
    "StartFleetRequestRequestTypeDef",
    "StartImageBuilderRequestRequestTypeDef",
    "StartImageBuilderResultTypeDef",
    "StopFleetRequestRequestTypeDef",
    "StopImageBuilderRequestRequestTypeDef",
    "StopImageBuilderResultTypeDef",
    "StorageConnectorTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResultTypeDef",
    "UpdateDirectoryConfigRequestRequestTypeDef",
    "UpdateDirectoryConfigResultTypeDef",
    "UpdateEntitlementRequestRequestTypeDef",
    "UpdateEntitlementResultTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateFleetResultTypeDef",
    "UpdateImagePermissionsRequestRequestTypeDef",
    "UpdateStackRequestRequestTypeDef",
    "UpdateStackResultTypeDef",
    "UsageReportSubscriptionTypeDef",
    "UserSettingTypeDef",
    "UserStackAssociationErrorTypeDef",
    "UserStackAssociationTypeDef",
    "UserTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

AccessEndpointTypeDef = TypedDict(
    "AccessEndpointTypeDef",
    {
        "EndpointType": Literal["STREAMING"],
        "VpceId": NotRequired[str],
    },
)

AppBlockTypeDef = TypedDict(
    "AppBlockTypeDef",
    {
        "Name": str,
        "Arn": str,
        "SetupScriptDetails": "ScriptDetailsTypeDef",
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "SourceS3Location": NotRequired["S3LocationTypeDef"],
        "CreatedTime": NotRequired[datetime],
    },
)

ApplicationFleetAssociationTypeDef = TypedDict(
    "ApplicationFleetAssociationTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
    },
)

ApplicationSettingsResponseTypeDef = TypedDict(
    "ApplicationSettingsResponseTypeDef",
    {
        "Enabled": NotRequired[bool],
        "SettingsGroup": NotRequired[str],
        "S3BucketName": NotRequired[str],
    },
)

ApplicationSettingsTypeDef = TypedDict(
    "ApplicationSettingsTypeDef",
    {
        "Enabled": bool,
        "SettingsGroup": NotRequired[str],
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": NotRequired[str],
        "DisplayName": NotRequired[str],
        "IconURL": NotRequired[str],
        "LaunchPath": NotRequired[str],
        "LaunchParameters": NotRequired[str],
        "Enabled": NotRequired[bool],
        "Metadata": NotRequired[Dict[str, str]],
        "WorkingDirectory": NotRequired[str],
        "Description": NotRequired[str],
        "Arn": NotRequired[str],
        "AppBlockArn": NotRequired[str],
        "IconS3Location": NotRequired["S3LocationTypeDef"],
        "Platforms": NotRequired[List[PlatformTypeType]],
        "InstanceFamilies": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
    },
)

AssociateApplicationFleetRequestRequestTypeDef = TypedDict(
    "AssociateApplicationFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
    },
)

AssociateApplicationFleetResultTypeDef = TypedDict(
    "AssociateApplicationFleetResultTypeDef",
    {
        "ApplicationFleetAssociation": "ApplicationFleetAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateApplicationToEntitlementRequestRequestTypeDef = TypedDict(
    "AssociateApplicationToEntitlementRequestRequestTypeDef",
    {
        "StackName": str,
        "EntitlementName": str,
        "ApplicationIdentifier": str,
    },
)

AssociateFleetRequestRequestTypeDef = TypedDict(
    "AssociateFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "StackName": str,
    },
)

BatchAssociateUserStackRequestRequestTypeDef = TypedDict(
    "BatchAssociateUserStackRequestRequestTypeDef",
    {
        "UserStackAssociations": Sequence["UserStackAssociationTypeDef"],
    },
)

BatchAssociateUserStackResultTypeDef = TypedDict(
    "BatchAssociateUserStackResultTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateUserStackRequestRequestTypeDef = TypedDict(
    "BatchDisassociateUserStackRequestRequestTypeDef",
    {
        "UserStackAssociations": Sequence["UserStackAssociationTypeDef"],
    },
)

BatchDisassociateUserStackResultTypeDef = TypedDict(
    "BatchDisassociateUserStackResultTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComputeCapacityStatusTypeDef = TypedDict(
    "ComputeCapacityStatusTypeDef",
    {
        "Desired": int,
        "Running": NotRequired[int],
        "InUse": NotRequired[int],
        "Available": NotRequired[int],
    },
)

ComputeCapacityTypeDef = TypedDict(
    "ComputeCapacityTypeDef",
    {
        "DesiredInstances": int,
    },
)

CopyImageRequestRequestTypeDef = TypedDict(
    "CopyImageRequestRequestTypeDef",
    {
        "SourceImageName": str,
        "DestinationImageName": str,
        "DestinationRegion": str,
        "DestinationImageDescription": NotRequired[str],
    },
)

CopyImageResponseTypeDef = TypedDict(
    "CopyImageResponseTypeDef",
    {
        "DestinationImageName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppBlockRequestRequestTypeDef = TypedDict(
    "CreateAppBlockRequestRequestTypeDef",
    {
        "Name": str,
        "SourceS3Location": "S3LocationTypeDef",
        "SetupScriptDetails": "ScriptDetailsTypeDef",
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateAppBlockResultTypeDef = TypedDict(
    "CreateAppBlockResultTypeDef",
    {
        "AppBlock": "AppBlockTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "IconS3Location": "S3LocationTypeDef",
        "LaunchPath": str,
        "Platforms": Sequence[PlatformTypeType],
        "InstanceFamilies": Sequence[str],
        "AppBlockArn": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "WorkingDirectory": NotRequired[str],
        "LaunchParameters": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateApplicationResultTypeDef = TypedDict(
    "CreateApplicationResultTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDirectoryConfigRequestRequestTypeDef = TypedDict(
    "CreateDirectoryConfigRequestRequestTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": Sequence[str],
        "ServiceAccountCredentials": NotRequired["ServiceAccountCredentialsTypeDef"],
    },
)

CreateDirectoryConfigResultTypeDef = TypedDict(
    "CreateDirectoryConfigResultTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEntitlementRequestRequestTypeDef = TypedDict(
    "CreateEntitlementRequestRequestTypeDef",
    {
        "Name": str,
        "StackName": str,
        "AppVisibility": AppVisibilityType,
        "Attributes": Sequence["EntitlementAttributeTypeDef"],
        "Description": NotRequired[str],
    },
)

CreateEntitlementResultTypeDef = TypedDict(
    "CreateEntitlementResultTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceType": str,
        "ImageName": NotRequired[str],
        "ImageArn": NotRequired[str],
        "FleetType": NotRequired[FleetTypeType],
        "ComputeCapacity": NotRequired["ComputeCapacityTypeDef"],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "MaxUserDurationInSeconds": NotRequired[int],
        "DisconnectTimeoutInSeconds": NotRequired[int],
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "EnableDefaultInternetAccess": NotRequired[bool],
        "DomainJoinInfo": NotRequired["DomainJoinInfoTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "IdleDisconnectTimeoutInSeconds": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "StreamView": NotRequired[StreamViewType],
        "Platform": NotRequired[PlatformTypeType],
        "MaxConcurrentSessions": NotRequired[int],
        "UsbDeviceFilterStrings": NotRequired[Sequence[str]],
    },
)

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "Fleet": "FleetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageBuilderRequestRequestTypeDef = TypedDict(
    "CreateImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceType": str,
        "ImageName": NotRequired[str],
        "ImageArn": NotRequired[str],
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "IamRoleArn": NotRequired[str],
        "EnableDefaultInternetAccess": NotRequired[bool],
        "DomainJoinInfo": NotRequired["DomainJoinInfoTypeDef"],
        "AppstreamAgentVersion": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "AccessEndpoints": NotRequired[Sequence["AccessEndpointTypeDef"]],
    },
)

CreateImageBuilderResultTypeDef = TypedDict(
    "CreateImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImageBuilderStreamingURLRequestRequestTypeDef = TypedDict(
    "CreateImageBuilderStreamingURLRequestRequestTypeDef",
    {
        "Name": str,
        "Validity": NotRequired[int],
    },
)

CreateImageBuilderStreamingURLResultTypeDef = TypedDict(
    "CreateImageBuilderStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackRequestRequestTypeDef = TypedDict(
    "CreateStackRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "StorageConnectors": NotRequired[Sequence["StorageConnectorTypeDef"]],
        "RedirectURL": NotRequired[str],
        "FeedbackURL": NotRequired[str],
        "UserSettings": NotRequired[Sequence["UserSettingTypeDef"]],
        "ApplicationSettings": NotRequired["ApplicationSettingsTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "AccessEndpoints": NotRequired[Sequence["AccessEndpointTypeDef"]],
        "EmbedHostDomains": NotRequired[Sequence[str]],
    },
)

CreateStackResultTypeDef = TypedDict(
    "CreateStackResultTypeDef",
    {
        "Stack": "StackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingURLRequestRequestTypeDef = TypedDict(
    "CreateStreamingURLRequestRequestTypeDef",
    {
        "StackName": str,
        "FleetName": str,
        "UserId": str,
        "ApplicationId": NotRequired[str],
        "Validity": NotRequired[int],
        "SessionContext": NotRequired[str],
    },
)

CreateStreamingURLResultTypeDef = TypedDict(
    "CreateStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUpdatedImageRequestRequestTypeDef = TypedDict(
    "CreateUpdatedImageRequestRequestTypeDef",
    {
        "existingImageName": str,
        "newImageName": str,
        "newImageDescription": NotRequired[str],
        "newImageDisplayName": NotRequired[str],
        "newImageTags": NotRequired[Mapping[str, str]],
        "dryRun": NotRequired[bool],
    },
)

CreateUpdatedImageResultTypeDef = TypedDict(
    "CreateUpdatedImageResultTypeDef",
    {
        "image": "ImageTypeDef",
        "canUpdateImage": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUsageReportSubscriptionResultTypeDef = TypedDict(
    "CreateUsageReportSubscriptionResultTypeDef",
    {
        "S3BucketName": str,
        "Schedule": Literal["DAILY"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
        "MessageAction": NotRequired[MessageActionType],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
    },
)

DeleteAppBlockRequestRequestTypeDef = TypedDict(
    "DeleteAppBlockRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDirectoryConfigRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryConfigRequestRequestTypeDef",
    {
        "DirectoryName": str,
    },
)

DeleteEntitlementRequestRequestTypeDef = TypedDict(
    "DeleteEntitlementRequestRequestTypeDef",
    {
        "Name": str,
        "StackName": str,
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageBuilderRequestRequestTypeDef = TypedDict(
    "DeleteImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageBuilderResultTypeDef = TypedDict(
    "DeleteImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePermissionsRequestRequestTypeDef = TypedDict(
    "DeleteImagePermissionsRequestRequestTypeDef",
    {
        "Name": str,
        "SharedAccountId": str,
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageResultTypeDef = TypedDict(
    "DeleteImageResultTypeDef",
    {
        "Image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStackRequestRequestTypeDef = TypedDict(
    "DeleteStackRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

DescribeAppBlocksRequestRequestTypeDef = TypedDict(
    "DescribeAppBlocksRequestRequestTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeAppBlocksResultTypeDef = TypedDict(
    "DescribeAppBlocksResultTypeDef",
    {
        "AppBlocks": List["AppBlockTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationFleetAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationFleetAssociationsRequestRequestTypeDef",
    {
        "FleetName": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeApplicationFleetAssociationsResultTypeDef = TypedDict(
    "DescribeApplicationFleetAssociationsResultTypeDef",
    {
        "ApplicationFleetAssociations": List["ApplicationFleetAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationsRequestRequestTypeDef",
    {
        "Arns": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeApplicationsResultTypeDef = TypedDict(
    "DescribeApplicationsResultTypeDef",
    {
        "Applications": List["ApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectoryConfigsRequestRequestTypeDef = TypedDict(
    "DescribeDirectoryConfigsRequestRequestTypeDef",
    {
        "DirectoryNames": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeDirectoryConfigsResultTypeDef = TypedDict(
    "DescribeDirectoryConfigsResultTypeDef",
    {
        "DirectoryConfigs": List["DirectoryConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntitlementsRequestRequestTypeDef = TypedDict(
    "DescribeEntitlementsRequestRequestTypeDef",
    {
        "StackName": str,
        "Name": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeEntitlementsResultTypeDef = TypedDict(
    "DescribeEntitlementsResultTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetsRequestRequestTypeDef = TypedDict(
    "DescribeFleetsRequestRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {
        "Fleets": List["FleetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageBuildersRequestRequestTypeDef = TypedDict(
    "DescribeImageBuildersRequestRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeImageBuildersResultTypeDef = TypedDict(
    "DescribeImageBuildersResultTypeDef",
    {
        "ImageBuilders": List["ImageBuilderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeImagePermissionsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "SharedAwsAccountIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeImagePermissionsResultTypeDef = TypedDict(
    "DescribeImagePermissionsResultTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List["SharedImagePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Arns": NotRequired[Sequence[str]],
        "Type": NotRequired[VisibilityTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSessionsRequestRequestTypeDef = TypedDict(
    "DescribeSessionsRequestRequestTypeDef",
    {
        "StackName": str,
        "FleetName": str,
        "UserId": NotRequired[str],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
        "AuthenticationType": NotRequired[AuthenticationTypeType],
    },
)

DescribeSessionsResultTypeDef = TypedDict(
    "DescribeSessionsResultTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksRequestRequestTypeDef = TypedDict(
    "DescribeStacksRequestRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsageReportSubscriptionsRequestRequestTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeUsageReportSubscriptionsResultTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsResultTypeDef",
    {
        "UsageReportSubscriptions": List["UsageReportSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserStackAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeUserStackAssociationsRequestRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "UserName": NotRequired[str],
        "AuthenticationType": NotRequired[AuthenticationTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeUserStackAssociationsResultTypeDef = TypedDict(
    "DescribeUserStackAssociationsResultTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersRequestRequestTypeDef = TypedDict(
    "DescribeUsersRequestRequestTypeDef",
    {
        "AuthenticationType": AuthenticationTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DirectoryConfigTypeDef = TypedDict(
    "DirectoryConfigTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": NotRequired[List[str]],
        "ServiceAccountCredentials": NotRequired["ServiceAccountCredentialsTypeDef"],
        "CreatedTime": NotRequired[datetime],
    },
)

DisableUserRequestRequestTypeDef = TypedDict(
    "DisableUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

DisassociateApplicationFleetRequestRequestTypeDef = TypedDict(
    "DisassociateApplicationFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
    },
)

DisassociateApplicationFromEntitlementRequestRequestTypeDef = TypedDict(
    "DisassociateApplicationFromEntitlementRequestRequestTypeDef",
    {
        "StackName": str,
        "EntitlementName": str,
        "ApplicationIdentifier": str,
    },
)

DisassociateFleetRequestRequestTypeDef = TypedDict(
    "DisassociateFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "StackName": str,
    },
)

DomainJoinInfoTypeDef = TypedDict(
    "DomainJoinInfoTypeDef",
    {
        "DirectoryName": NotRequired[str],
        "OrganizationalUnitDistinguishedName": NotRequired[str],
    },
)

EnableUserRequestRequestTypeDef = TypedDict(
    "EnableUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

EntitledApplicationTypeDef = TypedDict(
    "EntitledApplicationTypeDef",
    {
        "ApplicationIdentifier": str,
    },
)

EntitlementAttributeTypeDef = TypedDict(
    "EntitlementAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "Name": str,
        "StackName": str,
        "AppVisibility": AppVisibilityType,
        "Attributes": List["EntitlementAttributeTypeDef"],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

ExpireSessionRequestRequestTypeDef = TypedDict(
    "ExpireSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

FleetErrorTypeDef = TypedDict(
    "FleetErrorTypeDef",
    {
        "ErrorCode": NotRequired[FleetErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "InstanceType": str,
        "ComputeCapacityStatus": "ComputeCapacityStatusTypeDef",
        "State": FleetStateType,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "ImageName": NotRequired[str],
        "ImageArn": NotRequired[str],
        "FleetType": NotRequired[FleetTypeType],
        "MaxUserDurationInSeconds": NotRequired[int],
        "DisconnectTimeoutInSeconds": NotRequired[int],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "CreatedTime": NotRequired[datetime],
        "FleetErrors": NotRequired[List["FleetErrorTypeDef"]],
        "EnableDefaultInternetAccess": NotRequired[bool],
        "DomainJoinInfo": NotRequired["DomainJoinInfoTypeDef"],
        "IdleDisconnectTimeoutInSeconds": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "StreamView": NotRequired[StreamViewType],
        "Platform": NotRequired[PlatformTypeType],
        "MaxConcurrentSessions": NotRequired[int],
        "UsbDeviceFilterStrings": NotRequired[List[str]],
    },
)

ImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ImageBuilderStateChangeReasonTypeDef",
    {
        "Code": NotRequired[ImageBuilderStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

ImageBuilderTypeDef = TypedDict(
    "ImageBuilderTypeDef",
    {
        "Name": str,
        "Arn": NotRequired[str],
        "ImageArn": NotRequired[str],
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "InstanceType": NotRequired[str],
        "Platform": NotRequired[PlatformTypeType],
        "IamRoleArn": NotRequired[str],
        "State": NotRequired[ImageBuilderStateType],
        "StateChangeReason": NotRequired["ImageBuilderStateChangeReasonTypeDef"],
        "CreatedTime": NotRequired[datetime],
        "EnableDefaultInternetAccess": NotRequired[bool],
        "DomainJoinInfo": NotRequired["DomainJoinInfoTypeDef"],
        "NetworkAccessConfiguration": NotRequired["NetworkAccessConfigurationTypeDef"],
        "ImageBuilderErrors": NotRequired[List["ResourceErrorTypeDef"]],
        "AppstreamAgentVersion": NotRequired[str],
        "AccessEndpoints": NotRequired[List["AccessEndpointTypeDef"]],
    },
)

ImagePermissionsTypeDef = TypedDict(
    "ImagePermissionsTypeDef",
    {
        "allowFleet": NotRequired[bool],
        "allowImageBuilder": NotRequired[bool],
    },
)

ImageStateChangeReasonTypeDef = TypedDict(
    "ImageStateChangeReasonTypeDef",
    {
        "Code": NotRequired[ImageStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Name": str,
        "Arn": NotRequired[str],
        "BaseImageArn": NotRequired[str],
        "DisplayName": NotRequired[str],
        "State": NotRequired[ImageStateType],
        "Visibility": NotRequired[VisibilityTypeType],
        "ImageBuilderSupported": NotRequired[bool],
        "ImageBuilderName": NotRequired[str],
        "Platform": NotRequired[PlatformTypeType],
        "Description": NotRequired[str],
        "StateChangeReason": NotRequired["ImageStateChangeReasonTypeDef"],
        "Applications": NotRequired[List["ApplicationTypeDef"]],
        "CreatedTime": NotRequired[datetime],
        "PublicBaseImageReleasedDate": NotRequired[datetime],
        "AppstreamAgentVersion": NotRequired[str],
        "ImagePermissions": NotRequired["ImagePermissionsTypeDef"],
        "ImageErrors": NotRequired[List["ResourceErrorTypeDef"]],
    },
)

LastReportGenerationExecutionErrorTypeDef = TypedDict(
    "LastReportGenerationExecutionErrorTypeDef",
    {
        "ErrorCode": NotRequired[UsageReportExecutionErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

ListAssociatedFleetsRequestRequestTypeDef = TypedDict(
    "ListAssociatedFleetsRequestRequestTypeDef",
    {
        "StackName": str,
        "NextToken": NotRequired[str],
    },
)

ListAssociatedFleetsResultTypeDef = TypedDict(
    "ListAssociatedFleetsResultTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociatedStacksRequestRequestTypeDef = TypedDict(
    "ListAssociatedStacksRequestRequestTypeDef",
    {
        "FleetName": str,
        "NextToken": NotRequired[str],
    },
)

ListAssociatedStacksResultTypeDef = TypedDict(
    "ListAssociatedStacksResultTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitledApplicationsRequestRequestTypeDef = TypedDict(
    "ListEntitledApplicationsRequestRequestTypeDef",
    {
        "StackName": str,
        "EntitlementName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntitledApplicationsResultTypeDef = TypedDict(
    "ListEntitledApplicationsResultTypeDef",
    {
        "EntitledApplications": List["EntitledApplicationTypeDef"],
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

NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "EniPrivateIpAddress": NotRequired[str],
        "EniId": NotRequired[str],
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

ResourceErrorTypeDef = TypedDict(
    "ResourceErrorTypeDef",
    {
        "ErrorCode": NotRequired[FleetErrorCodeType],
        "ErrorMessage": NotRequired[str],
        "ErrorTimestamp": NotRequired[datetime],
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
)

ScriptDetailsTypeDef = TypedDict(
    "ScriptDetailsTypeDef",
    {
        "ScriptS3Location": "S3LocationTypeDef",
        "ExecutablePath": str,
        "TimeoutInSeconds": int,
        "ExecutableParameters": NotRequired[str],
    },
)

ServiceAccountCredentialsTypeDef = TypedDict(
    "ServiceAccountCredentialsTypeDef",
    {
        "AccountName": str,
        "AccountPassword": str,
    },
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": SessionStateType,
        "ConnectionState": NotRequired[SessionConnectionStateType],
        "StartTime": NotRequired[datetime],
        "MaxExpirationTime": NotRequired[datetime],
        "AuthenticationType": NotRequired[AuthenticationTypeType],
        "NetworkAccessConfiguration": NotRequired["NetworkAccessConfigurationTypeDef"],
    },
)

SharedImagePermissionsTypeDef = TypedDict(
    "SharedImagePermissionsTypeDef",
    {
        "sharedAccountId": str,
        "imagePermissions": "ImagePermissionsTypeDef",
    },
)

StackErrorTypeDef = TypedDict(
    "StackErrorTypeDef",
    {
        "ErrorCode": NotRequired[StackErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "Name": str,
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "StorageConnectors": NotRequired[List["StorageConnectorTypeDef"]],
        "RedirectURL": NotRequired[str],
        "FeedbackURL": NotRequired[str],
        "StackErrors": NotRequired[List["StackErrorTypeDef"]],
        "UserSettings": NotRequired[List["UserSettingTypeDef"]],
        "ApplicationSettings": NotRequired["ApplicationSettingsResponseTypeDef"],
        "AccessEndpoints": NotRequired[List["AccessEndpointTypeDef"]],
        "EmbedHostDomains": NotRequired[List[str]],
    },
)

StartFleetRequestRequestTypeDef = TypedDict(
    "StartFleetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartImageBuilderRequestRequestTypeDef = TypedDict(
    "StartImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
        "AppstreamAgentVersion": NotRequired[str],
    },
)

StartImageBuilderResultTypeDef = TypedDict(
    "StartImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFleetRequestRequestTypeDef = TypedDict(
    "StopFleetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopImageBuilderRequestRequestTypeDef = TypedDict(
    "StopImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopImageBuilderResultTypeDef = TypedDict(
    "StopImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageConnectorTypeDef = TypedDict(
    "StorageConnectorTypeDef",
    {
        "ConnectorType": StorageConnectorTypeType,
        "ResourceIdentifier": NotRequired[str],
        "Domains": NotRequired[Sequence[str]],
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

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "IconS3Location": NotRequired["S3LocationTypeDef"],
        "LaunchPath": NotRequired[str],
        "WorkingDirectory": NotRequired[str],
        "LaunchParameters": NotRequired[str],
        "AppBlockArn": NotRequired[str],
        "AttributesToDelete": NotRequired[Sequence[ApplicationAttributeType]],
    },
)

UpdateApplicationResultTypeDef = TypedDict(
    "UpdateApplicationResultTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDirectoryConfigRequestRequestTypeDef = TypedDict(
    "UpdateDirectoryConfigRequestRequestTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": NotRequired[Sequence[str]],
        "ServiceAccountCredentials": NotRequired["ServiceAccountCredentialsTypeDef"],
    },
)

UpdateDirectoryConfigResultTypeDef = TypedDict(
    "UpdateDirectoryConfigResultTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEntitlementRequestRequestTypeDef = TypedDict(
    "UpdateEntitlementRequestRequestTypeDef",
    {
        "Name": str,
        "StackName": str,
        "Description": NotRequired[str],
        "AppVisibility": NotRequired[AppVisibilityType],
        "Attributes": NotRequired[Sequence["EntitlementAttributeTypeDef"]],
    },
)

UpdateEntitlementResultTypeDef = TypedDict(
    "UpdateEntitlementResultTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetRequestRequestTypeDef = TypedDict(
    "UpdateFleetRequestRequestTypeDef",
    {
        "ImageName": NotRequired[str],
        "ImageArn": NotRequired[str],
        "Name": NotRequired[str],
        "InstanceType": NotRequired[str],
        "ComputeCapacity": NotRequired["ComputeCapacityTypeDef"],
        "VpcConfig": NotRequired["VpcConfigTypeDef"],
        "MaxUserDurationInSeconds": NotRequired[int],
        "DisconnectTimeoutInSeconds": NotRequired[int],
        "DeleteVpcConfig": NotRequired[bool],
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "EnableDefaultInternetAccess": NotRequired[bool],
        "DomainJoinInfo": NotRequired["DomainJoinInfoTypeDef"],
        "IdleDisconnectTimeoutInSeconds": NotRequired[int],
        "AttributesToDelete": NotRequired[Sequence[FleetAttributeType]],
        "IamRoleArn": NotRequired[str],
        "StreamView": NotRequired[StreamViewType],
        "Platform": NotRequired[PlatformTypeType],
        "MaxConcurrentSessions": NotRequired[int],
        "UsbDeviceFilterStrings": NotRequired[Sequence[str]],
    },
)

UpdateFleetResultTypeDef = TypedDict(
    "UpdateFleetResultTypeDef",
    {
        "Fleet": "FleetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImagePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateImagePermissionsRequestRequestTypeDef",
    {
        "Name": str,
        "SharedAccountId": str,
        "ImagePermissions": "ImagePermissionsTypeDef",
    },
)

UpdateStackRequestRequestTypeDef = TypedDict(
    "UpdateStackRequestRequestTypeDef",
    {
        "Name": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "StorageConnectors": NotRequired[Sequence["StorageConnectorTypeDef"]],
        "DeleteStorageConnectors": NotRequired[bool],
        "RedirectURL": NotRequired[str],
        "FeedbackURL": NotRequired[str],
        "AttributesToDelete": NotRequired[Sequence[StackAttributeType]],
        "UserSettings": NotRequired[Sequence["UserSettingTypeDef"]],
        "ApplicationSettings": NotRequired["ApplicationSettingsTypeDef"],
        "AccessEndpoints": NotRequired[Sequence["AccessEndpointTypeDef"]],
        "EmbedHostDomains": NotRequired[Sequence[str]],
    },
)

UpdateStackResultTypeDef = TypedDict(
    "UpdateStackResultTypeDef",
    {
        "Stack": "StackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageReportSubscriptionTypeDef = TypedDict(
    "UsageReportSubscriptionTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "Schedule": NotRequired[Literal["DAILY"]],
        "LastGeneratedReportDate": NotRequired[datetime],
        "SubscriptionErrors": NotRequired[List["LastReportGenerationExecutionErrorTypeDef"]],
    },
)

UserSettingTypeDef = TypedDict(
    "UserSettingTypeDef",
    {
        "Action": ActionType,
        "Permission": PermissionType,
    },
)

UserStackAssociationErrorTypeDef = TypedDict(
    "UserStackAssociationErrorTypeDef",
    {
        "UserStackAssociation": NotRequired["UserStackAssociationTypeDef"],
        "ErrorCode": NotRequired[UserStackAssociationErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

UserStackAssociationTypeDef = TypedDict(
    "UserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
        "SendEmailNotification": NotRequired[bool],
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "AuthenticationType": AuthenticationTypeType,
        "Arn": NotRequired[str],
        "UserName": NotRequired[str],
        "Enabled": NotRequired[bool],
        "Status": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
