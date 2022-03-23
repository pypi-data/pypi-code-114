"""
Type annotations for nimble service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/type_defs.html)

Usage::

    ```python
    from mypy_boto3_nimble.type_defs import AcceptEulasRequestRequestTypeDef

    data: AcceptEulasRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    LaunchProfilePlatformType,
    LaunchProfileStateType,
    LaunchProfileStatusCodeType,
    LaunchProfileValidationStateType,
    LaunchProfileValidationStatusCodeType,
    LaunchProfileValidationTypeType,
    StreamingClipboardModeType,
    StreamingImageStateType,
    StreamingImageStatusCodeType,
    StreamingInstanceTypeType,
    StreamingSessionStateType,
    StreamingSessionStatusCodeType,
    StreamingSessionStreamStateType,
    StreamingSessionStreamStatusCodeType,
    StudioComponentInitializationScriptRunContextType,
    StudioComponentStateType,
    StudioComponentStatusCodeType,
    StudioComponentSubtypeType,
    StudioComponentTypeType,
    StudioEncryptionConfigurationKeyTypeType,
    StudioStateType,
    StudioStatusCodeType,
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
    "AcceptEulasRequestRequestTypeDef",
    "AcceptEulasResponseTypeDef",
    "ActiveDirectoryComputerAttributeTypeDef",
    "ActiveDirectoryConfigurationTypeDef",
    "ComputeFarmConfigurationTypeDef",
    "CreateLaunchProfileRequestRequestTypeDef",
    "CreateLaunchProfileResponseTypeDef",
    "CreateStreamingImageRequestRequestTypeDef",
    "CreateStreamingImageResponseTypeDef",
    "CreateStreamingSessionRequestRequestTypeDef",
    "CreateStreamingSessionResponseTypeDef",
    "CreateStreamingSessionStreamRequestRequestTypeDef",
    "CreateStreamingSessionStreamResponseTypeDef",
    "CreateStudioComponentRequestRequestTypeDef",
    "CreateStudioComponentResponseTypeDef",
    "CreateStudioRequestRequestTypeDef",
    "CreateStudioResponseTypeDef",
    "DeleteLaunchProfileMemberRequestRequestTypeDef",
    "DeleteLaunchProfileRequestRequestTypeDef",
    "DeleteLaunchProfileResponseTypeDef",
    "DeleteStreamingImageRequestRequestTypeDef",
    "DeleteStreamingImageResponseTypeDef",
    "DeleteStreamingSessionRequestRequestTypeDef",
    "DeleteStreamingSessionResponseTypeDef",
    "DeleteStudioComponentRequestRequestTypeDef",
    "DeleteStudioComponentResponseTypeDef",
    "DeleteStudioMemberRequestRequestTypeDef",
    "DeleteStudioRequestRequestTypeDef",
    "DeleteStudioResponseTypeDef",
    "EulaAcceptanceTypeDef",
    "EulaTypeDef",
    "GetEulaRequestRequestTypeDef",
    "GetEulaResponseTypeDef",
    "GetLaunchProfileDetailsRequestRequestTypeDef",
    "GetLaunchProfileDetailsResponseTypeDef",
    "GetLaunchProfileInitializationRequestRequestTypeDef",
    "GetLaunchProfileInitializationResponseTypeDef",
    "GetLaunchProfileMemberRequestRequestTypeDef",
    "GetLaunchProfileMemberResponseTypeDef",
    "GetLaunchProfileRequestRequestTypeDef",
    "GetLaunchProfileResponseTypeDef",
    "GetStreamingImageRequestRequestTypeDef",
    "GetStreamingImageResponseTypeDef",
    "GetStreamingSessionRequestRequestTypeDef",
    "GetStreamingSessionResponseTypeDef",
    "GetStreamingSessionStreamRequestRequestTypeDef",
    "GetStreamingSessionStreamResponseTypeDef",
    "GetStudioComponentRequestRequestTypeDef",
    "GetStudioComponentResponseTypeDef",
    "GetStudioMemberRequestRequestTypeDef",
    "GetStudioMemberResponseTypeDef",
    "GetStudioRequestRequestTypeDef",
    "GetStudioResponseTypeDef",
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    "LaunchProfileInitializationScriptTypeDef",
    "LaunchProfileInitializationTypeDef",
    "LaunchProfileMembershipTypeDef",
    "LaunchProfileTypeDef",
    "LicenseServiceConfigurationTypeDef",
    "ListEulaAcceptancesRequestRequestTypeDef",
    "ListEulaAcceptancesResponseTypeDef",
    "ListEulasRequestRequestTypeDef",
    "ListEulasResponseTypeDef",
    "ListLaunchProfileMembersRequestRequestTypeDef",
    "ListLaunchProfileMembersResponseTypeDef",
    "ListLaunchProfilesRequestRequestTypeDef",
    "ListLaunchProfilesResponseTypeDef",
    "ListStreamingImagesRequestRequestTypeDef",
    "ListStreamingImagesResponseTypeDef",
    "ListStreamingSessionsRequestRequestTypeDef",
    "ListStreamingSessionsResponseTypeDef",
    "ListStudioComponentsRequestRequestTypeDef",
    "ListStudioComponentsResponseTypeDef",
    "ListStudioMembersRequestRequestTypeDef",
    "ListStudioMembersResponseTypeDef",
    "ListStudiosRequestRequestTypeDef",
    "ListStudiosResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NewLaunchProfileMemberTypeDef",
    "NewStudioMemberTypeDef",
    "PaginatorConfigTypeDef",
    "PutLaunchProfileMembersRequestRequestTypeDef",
    "PutStudioMembersRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptParameterKeyValueTypeDef",
    "SharedFileSystemConfigurationTypeDef",
    "StartStreamingSessionRequestRequestTypeDef",
    "StartStreamingSessionResponseTypeDef",
    "StartStudioSSOConfigurationRepairRequestRequestTypeDef",
    "StartStudioSSOConfigurationRepairResponseTypeDef",
    "StopStreamingSessionRequestRequestTypeDef",
    "StopStreamingSessionResponseTypeDef",
    "StreamConfigurationCreateTypeDef",
    "StreamConfigurationSessionStorageTypeDef",
    "StreamConfigurationTypeDef",
    "StreamingImageEncryptionConfigurationTypeDef",
    "StreamingImageTypeDef",
    "StreamingSessionStorageRootTypeDef",
    "StreamingSessionStreamTypeDef",
    "StreamingSessionTypeDef",
    "StudioComponentConfigurationTypeDef",
    "StudioComponentInitializationScriptTypeDef",
    "StudioComponentSummaryTypeDef",
    "StudioComponentTypeDef",
    "StudioEncryptionConfigurationTypeDef",
    "StudioMembershipTypeDef",
    "StudioTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLaunchProfileMemberRequestRequestTypeDef",
    "UpdateLaunchProfileMemberResponseTypeDef",
    "UpdateLaunchProfileRequestRequestTypeDef",
    "UpdateLaunchProfileResponseTypeDef",
    "UpdateStreamingImageRequestRequestTypeDef",
    "UpdateStreamingImageResponseTypeDef",
    "UpdateStudioComponentRequestRequestTypeDef",
    "UpdateStudioComponentResponseTypeDef",
    "UpdateStudioRequestRequestTypeDef",
    "UpdateStudioResponseTypeDef",
    "ValidationResultTypeDef",
    "WaiterConfigTypeDef",
)

AcceptEulasRequestRequestTypeDef = TypedDict(
    "AcceptEulasRequestRequestTypeDef",
    {
        "studioId": str,
        "clientToken": NotRequired[str],
        "eulaIds": NotRequired[Sequence[str]],
    },
)

AcceptEulasResponseTypeDef = TypedDict(
    "AcceptEulasResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActiveDirectoryComputerAttributeTypeDef = TypedDict(
    "ActiveDirectoryComputerAttributeTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)

ActiveDirectoryConfigurationTypeDef = TypedDict(
    "ActiveDirectoryConfigurationTypeDef",
    {
        "computerAttributes": NotRequired[Sequence["ActiveDirectoryComputerAttributeTypeDef"]],
        "directoryId": NotRequired[str],
        "organizationalUnitDistinguishedName": NotRequired[str],
    },
)

ComputeFarmConfigurationTypeDef = TypedDict(
    "ComputeFarmConfigurationTypeDef",
    {
        "activeDirectoryUser": NotRequired[str],
        "endpoint": NotRequired[str],
    },
)

CreateLaunchProfileRequestRequestTypeDef = TypedDict(
    "CreateLaunchProfileRequestRequestTypeDef",
    {
        "ec2SubnetIds": Sequence[str],
        "launchProfileProtocolVersions": Sequence[str],
        "name": str,
        "streamConfiguration": "StreamConfigurationCreateTypeDef",
        "studioComponentIds": Sequence[str],
        "studioId": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateLaunchProfileResponseTypeDef = TypedDict(
    "CreateLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingImageRequestRequestTypeDef = TypedDict(
    "CreateStreamingImageRequestRequestTypeDef",
    {
        "ec2ImageId": str,
        "name": str,
        "studioId": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateStreamingImageResponseTypeDef = TypedDict(
    "CreateStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingSessionRequestRequestTypeDef = TypedDict(
    "CreateStreamingSessionRequestRequestTypeDef",
    {
        "studioId": str,
        "clientToken": NotRequired[str],
        "ec2InstanceType": NotRequired[StreamingInstanceTypeType],
        "launchProfileId": NotRequired[str],
        "ownedBy": NotRequired[str],
        "streamingImageId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateStreamingSessionResponseTypeDef = TypedDict(
    "CreateStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamingSessionStreamRequestRequestTypeDef = TypedDict(
    "CreateStreamingSessionStreamRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
        "expirationInSeconds": NotRequired[int],
    },
)

CreateStreamingSessionStreamResponseTypeDef = TypedDict(
    "CreateStreamingSessionStreamResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStudioComponentRequestRequestTypeDef = TypedDict(
    "CreateStudioComponentRequestRequestTypeDef",
    {
        "name": str,
        "studioId": str,
        "type": StudioComponentTypeType,
        "clientToken": NotRequired[str],
        "configuration": NotRequired["StudioComponentConfigurationTypeDef"],
        "description": NotRequired[str],
        "ec2SecurityGroupIds": NotRequired[Sequence[str]],
        "initializationScripts": NotRequired[
            Sequence["StudioComponentInitializationScriptTypeDef"]
        ],
        "scriptParameters": NotRequired[Sequence["ScriptParameterKeyValueTypeDef"]],
        "subtype": NotRequired[StudioComponentSubtypeType],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateStudioComponentResponseTypeDef = TypedDict(
    "CreateStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStudioRequestRequestTypeDef = TypedDict(
    "CreateStudioRequestRequestTypeDef",
    {
        "adminRoleArn": str,
        "displayName": str,
        "studioName": str,
        "userRoleArn": str,
        "clientToken": NotRequired[str],
        "studioEncryptionConfiguration": NotRequired["StudioEncryptionConfigurationTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateStudioResponseTypeDef = TypedDict(
    "CreateStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "DeleteLaunchProfileMemberRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "principalId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteLaunchProfileRequestRequestTypeDef = TypedDict(
    "DeleteLaunchProfileRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteLaunchProfileResponseTypeDef = TypedDict(
    "DeleteLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStreamingImageRequestRequestTypeDef = TypedDict(
    "DeleteStreamingImageRequestRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteStreamingImageResponseTypeDef = TypedDict(
    "DeleteStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStreamingSessionRequestRequestTypeDef = TypedDict(
    "DeleteStreamingSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteStreamingSessionResponseTypeDef = TypedDict(
    "DeleteStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStudioComponentRequestRequestTypeDef = TypedDict(
    "DeleteStudioComponentRequestRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteStudioComponentResponseTypeDef = TypedDict(
    "DeleteStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStudioMemberRequestRequestTypeDef = TypedDict(
    "DeleteStudioMemberRequestRequestTypeDef",
    {
        "principalId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteStudioRequestRequestTypeDef = TypedDict(
    "DeleteStudioRequestRequestTypeDef",
    {
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteStudioResponseTypeDef = TypedDict(
    "DeleteStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EulaAcceptanceTypeDef = TypedDict(
    "EulaAcceptanceTypeDef",
    {
        "acceptedAt": NotRequired[datetime],
        "acceptedBy": NotRequired[str],
        "accepteeId": NotRequired[str],
        "eulaAcceptanceId": NotRequired[str],
        "eulaId": NotRequired[str],
    },
)

EulaTypeDef = TypedDict(
    "EulaTypeDef",
    {
        "content": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "eulaId": NotRequired[str],
        "name": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)

GetEulaRequestRequestTypeDef = TypedDict(
    "GetEulaRequestRequestTypeDef",
    {
        "eulaId": str,
    },
)

GetEulaResponseTypeDef = TypedDict(
    "GetEulaResponseTypeDef",
    {
        "eula": "EulaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileDetailsRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileDetailsRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)

GetLaunchProfileDetailsResponseTypeDef = TypedDict(
    "GetLaunchProfileDetailsResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "streamingImages": List["StreamingImageTypeDef"],
        "studioComponentSummaries": List["StudioComponentSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileInitializationRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileInitializationRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "launchProfileProtocolVersions": Sequence[str],
        "launchPurpose": str,
        "platform": str,
        "studioId": str,
    },
)

GetLaunchProfileInitializationResponseTypeDef = TypedDict(
    "GetLaunchProfileInitializationResponseTypeDef",
    {
        "launchProfileInitialization": "LaunchProfileInitializationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileMemberRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "principalId": str,
        "studioId": str,
    },
)

GetLaunchProfileMemberResponseTypeDef = TypedDict(
    "GetLaunchProfileMemberResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)

GetLaunchProfileResponseTypeDef = TypedDict(
    "GetLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingImageRequestRequestTypeDef = TypedDict(
    "GetStreamingImageRequestRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)

GetStreamingImageResponseTypeDef = TypedDict(
    "GetStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingSessionRequestRequestTypeDef = TypedDict(
    "GetStreamingSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)

GetStreamingSessionResponseTypeDef = TypedDict(
    "GetStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingSessionStreamRequestRequestTypeDef = TypedDict(
    "GetStreamingSessionStreamRequestRequestTypeDef",
    {
        "sessionId": str,
        "streamId": str,
        "studioId": str,
    },
)

GetStreamingSessionStreamResponseTypeDef = TypedDict(
    "GetStreamingSessionStreamResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioComponentRequestRequestTypeDef = TypedDict(
    "GetStudioComponentRequestRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)

GetStudioComponentResponseTypeDef = TypedDict(
    "GetStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioMemberRequestRequestTypeDef = TypedDict(
    "GetStudioMemberRequestRequestTypeDef",
    {
        "principalId": str,
        "studioId": str,
    },
)

GetStudioMemberResponseTypeDef = TypedDict(
    "GetStudioMemberResponseTypeDef",
    {
        "member": "StudioMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioRequestRequestTypeDef = TypedDict(
    "GetStudioRequestRequestTypeDef",
    {
        "studioId": str,
    },
)

GetStudioResponseTypeDef = TypedDict(
    "GetStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchProfileInitializationActiveDirectoryTypeDef = TypedDict(
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    {
        "computerAttributes": NotRequired[List["ActiveDirectoryComputerAttributeTypeDef"]],
        "directoryId": NotRequired[str],
        "directoryName": NotRequired[str],
        "dnsIpAddresses": NotRequired[List[str]],
        "organizationalUnitDistinguishedName": NotRequired[str],
        "studioComponentId": NotRequired[str],
        "studioComponentName": NotRequired[str],
    },
)

LaunchProfileInitializationScriptTypeDef = TypedDict(
    "LaunchProfileInitializationScriptTypeDef",
    {
        "script": NotRequired[str],
        "studioComponentId": NotRequired[str],
        "studioComponentName": NotRequired[str],
    },
)

LaunchProfileInitializationTypeDef = TypedDict(
    "LaunchProfileInitializationTypeDef",
    {
        "activeDirectory": NotRequired["LaunchProfileInitializationActiveDirectoryTypeDef"],
        "ec2SecurityGroupIds": NotRequired[List[str]],
        "launchProfileId": NotRequired[str],
        "launchProfileProtocolVersion": NotRequired[str],
        "launchPurpose": NotRequired[str],
        "name": NotRequired[str],
        "platform": NotRequired[LaunchProfilePlatformType],
        "systemInitializationScripts": NotRequired[
            List["LaunchProfileInitializationScriptTypeDef"]
        ],
        "userInitializationScripts": NotRequired[List["LaunchProfileInitializationScriptTypeDef"]],
    },
)

LaunchProfileMembershipTypeDef = TypedDict(
    "LaunchProfileMembershipTypeDef",
    {
        "identityStoreId": NotRequired[str],
        "persona": NotRequired[Literal["USER"]],
        "principalId": NotRequired[str],
        "sid": NotRequired[str],
    },
)

LaunchProfileTypeDef = TypedDict(
    "LaunchProfileTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "ec2SubnetIds": NotRequired[List[str]],
        "launchProfileId": NotRequired[str],
        "launchProfileProtocolVersions": NotRequired[List[str]],
        "name": NotRequired[str],
        "state": NotRequired[LaunchProfileStateType],
        "statusCode": NotRequired[LaunchProfileStatusCodeType],
        "statusMessage": NotRequired[str],
        "streamConfiguration": NotRequired["StreamConfigurationTypeDef"],
        "studioComponentIds": NotRequired[List[str]],
        "tags": NotRequired[Dict[str, str]],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "validationResults": NotRequired[List["ValidationResultTypeDef"]],
    },
)

LicenseServiceConfigurationTypeDef = TypedDict(
    "LicenseServiceConfigurationTypeDef",
    {
        "endpoint": NotRequired[str],
    },
)

ListEulaAcceptancesRequestRequestTypeDef = TypedDict(
    "ListEulaAcceptancesRequestRequestTypeDef",
    {
        "studioId": str,
        "eulaIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
    },
)

ListEulaAcceptancesResponseTypeDef = TypedDict(
    "ListEulaAcceptancesResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEulasRequestRequestTypeDef = TypedDict(
    "ListEulasRequestRequestTypeDef",
    {
        "eulaIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
    },
)

ListEulasResponseTypeDef = TypedDict(
    "ListEulasResponseTypeDef",
    {
        "eulas": List["EulaTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLaunchProfileMembersRequestRequestTypeDef = TypedDict(
    "ListLaunchProfileMembersRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListLaunchProfileMembersResponseTypeDef = TypedDict(
    "ListLaunchProfileMembersResponseTypeDef",
    {
        "members": List["LaunchProfileMembershipTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLaunchProfilesRequestRequestTypeDef = TypedDict(
    "ListLaunchProfilesRequestRequestTypeDef",
    {
        "studioId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "principalId": NotRequired[str],
        "states": NotRequired[Sequence[LaunchProfileStateType]],
    },
)

ListLaunchProfilesResponseTypeDef = TypedDict(
    "ListLaunchProfilesResponseTypeDef",
    {
        "launchProfiles": List["LaunchProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamingImagesRequestRequestTypeDef = TypedDict(
    "ListStreamingImagesRequestRequestTypeDef",
    {
        "studioId": str,
        "nextToken": NotRequired[str],
        "owner": NotRequired[str],
    },
)

ListStreamingImagesResponseTypeDef = TypedDict(
    "ListStreamingImagesResponseTypeDef",
    {
        "nextToken": str,
        "streamingImages": List["StreamingImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamingSessionsRequestRequestTypeDef = TypedDict(
    "ListStreamingSessionsRequestRequestTypeDef",
    {
        "studioId": str,
        "createdBy": NotRequired[str],
        "nextToken": NotRequired[str],
        "ownedBy": NotRequired[str],
        "sessionIds": NotRequired[str],
    },
)

ListStreamingSessionsResponseTypeDef = TypedDict(
    "ListStreamingSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List["StreamingSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioComponentsRequestRequestTypeDef = TypedDict(
    "ListStudioComponentsRequestRequestTypeDef",
    {
        "studioId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "states": NotRequired[Sequence[StudioComponentStateType]],
        "types": NotRequired[Sequence[StudioComponentTypeType]],
    },
)

ListStudioComponentsResponseTypeDef = TypedDict(
    "ListStudioComponentsResponseTypeDef",
    {
        "nextToken": str,
        "studioComponents": List["StudioComponentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioMembersRequestRequestTypeDef = TypedDict(
    "ListStudioMembersRequestRequestTypeDef",
    {
        "studioId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListStudioMembersResponseTypeDef = TypedDict(
    "ListStudioMembersResponseTypeDef",
    {
        "members": List["StudioMembershipTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudiosRequestRequestTypeDef = TypedDict(
    "ListStudiosRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)

ListStudiosResponseTypeDef = TypedDict(
    "ListStudiosResponseTypeDef",
    {
        "nextToken": str,
        "studios": List["StudioTypeDef"],
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

NewLaunchProfileMemberTypeDef = TypedDict(
    "NewLaunchProfileMemberTypeDef",
    {
        "persona": Literal["USER"],
        "principalId": str,
    },
)

NewStudioMemberTypeDef = TypedDict(
    "NewStudioMemberTypeDef",
    {
        "persona": Literal["ADMINISTRATOR"],
        "principalId": str,
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

PutLaunchProfileMembersRequestRequestTypeDef = TypedDict(
    "PutLaunchProfileMembersRequestRequestTypeDef",
    {
        "identityStoreId": str,
        "launchProfileId": str,
        "members": Sequence["NewLaunchProfileMemberTypeDef"],
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

PutStudioMembersRequestRequestTypeDef = TypedDict(
    "PutStudioMembersRequestRequestTypeDef",
    {
        "identityStoreId": str,
        "members": Sequence["NewStudioMemberTypeDef"],
        "studioId": str,
        "clientToken": NotRequired[str],
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

ScriptParameterKeyValueTypeDef = TypedDict(
    "ScriptParameterKeyValueTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

SharedFileSystemConfigurationTypeDef = TypedDict(
    "SharedFileSystemConfigurationTypeDef",
    {
        "endpoint": NotRequired[str],
        "fileSystemId": NotRequired[str],
        "linuxMountPoint": NotRequired[str],
        "shareName": NotRequired[str],
        "windowsMountDrive": NotRequired[str],
    },
)

StartStreamingSessionRequestRequestTypeDef = TypedDict(
    "StartStreamingSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

StartStreamingSessionResponseTypeDef = TypedDict(
    "StartStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartStudioSSOConfigurationRepairRequestRequestTypeDef = TypedDict(
    "StartStudioSSOConfigurationRepairRequestRequestTypeDef",
    {
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

StartStudioSSOConfigurationRepairResponseTypeDef = TypedDict(
    "StartStudioSSOConfigurationRepairResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopStreamingSessionRequestRequestTypeDef = TypedDict(
    "StopStreamingSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

StopStreamingSessionResponseTypeDef = TypedDict(
    "StopStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StreamConfigurationCreateTypeDef = TypedDict(
    "StreamConfigurationCreateTypeDef",
    {
        "clipboardMode": StreamingClipboardModeType,
        "ec2InstanceTypes": Sequence[StreamingInstanceTypeType],
        "streamingImageIds": Sequence[str],
        "maxSessionLengthInMinutes": NotRequired[int],
        "maxStoppedSessionLengthInMinutes": NotRequired[int],
        "sessionStorage": NotRequired["StreamConfigurationSessionStorageTypeDef"],
    },
)

StreamConfigurationSessionStorageTypeDef = TypedDict(
    "StreamConfigurationSessionStorageTypeDef",
    {
        "mode": Sequence[Literal["UPLOAD"]],
        "root": NotRequired["StreamingSessionStorageRootTypeDef"],
    },
)

StreamConfigurationTypeDef = TypedDict(
    "StreamConfigurationTypeDef",
    {
        "clipboardMode": StreamingClipboardModeType,
        "ec2InstanceTypes": List[StreamingInstanceTypeType],
        "streamingImageIds": List[str],
        "maxSessionLengthInMinutes": NotRequired[int],
        "maxStoppedSessionLengthInMinutes": NotRequired[int],
        "sessionStorage": NotRequired["StreamConfigurationSessionStorageTypeDef"],
    },
)

StreamingImageEncryptionConfigurationTypeDef = TypedDict(
    "StreamingImageEncryptionConfigurationTypeDef",
    {
        "keyType": Literal["CUSTOMER_MANAGED_KEY"],
        "keyArn": NotRequired[str],
    },
)

StreamingImageTypeDef = TypedDict(
    "StreamingImageTypeDef",
    {
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "ec2ImageId": NotRequired[str],
        "encryptionConfiguration": NotRequired["StreamingImageEncryptionConfigurationTypeDef"],
        "eulaIds": NotRequired[List[str]],
        "name": NotRequired[str],
        "owner": NotRequired[str],
        "platform": NotRequired[str],
        "state": NotRequired[StreamingImageStateType],
        "statusCode": NotRequired[StreamingImageStatusCodeType],
        "statusMessage": NotRequired[str],
        "streamingImageId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

StreamingSessionStorageRootTypeDef = TypedDict(
    "StreamingSessionStorageRootTypeDef",
    {
        "linux": NotRequired[str],
        "windows": NotRequired[str],
    },
)

StreamingSessionStreamTypeDef = TypedDict(
    "StreamingSessionStreamTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "expiresAt": NotRequired[datetime],
        "ownedBy": NotRequired[str],
        "state": NotRequired[StreamingSessionStreamStateType],
        "statusCode": NotRequired[StreamingSessionStreamStatusCodeType],
        "streamId": NotRequired[str],
        "url": NotRequired[str],
    },
)

StreamingSessionTypeDef = TypedDict(
    "StreamingSessionTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "ec2InstanceType": NotRequired[str],
        "launchProfileId": NotRequired[str],
        "ownedBy": NotRequired[str],
        "sessionId": NotRequired[str],
        "startedAt": NotRequired[datetime],
        "startedBy": NotRequired[str],
        "state": NotRequired[StreamingSessionStateType],
        "statusCode": NotRequired[StreamingSessionStatusCodeType],
        "statusMessage": NotRequired[str],
        "stopAt": NotRequired[datetime],
        "stoppedAt": NotRequired[datetime],
        "stoppedBy": NotRequired[str],
        "streamingImageId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "terminateAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)

StudioComponentConfigurationTypeDef = TypedDict(
    "StudioComponentConfigurationTypeDef",
    {
        "activeDirectoryConfiguration": NotRequired["ActiveDirectoryConfigurationTypeDef"],
        "computeFarmConfiguration": NotRequired["ComputeFarmConfigurationTypeDef"],
        "licenseServiceConfiguration": NotRequired["LicenseServiceConfigurationTypeDef"],
        "sharedFileSystemConfiguration": NotRequired["SharedFileSystemConfigurationTypeDef"],
    },
)

StudioComponentInitializationScriptTypeDef = TypedDict(
    "StudioComponentInitializationScriptTypeDef",
    {
        "launchProfileProtocolVersion": NotRequired[str],
        "platform": NotRequired[LaunchProfilePlatformType],
        "runContext": NotRequired[StudioComponentInitializationScriptRunContextType],
        "script": NotRequired[str],
    },
)

StudioComponentSummaryTypeDef = TypedDict(
    "StudioComponentSummaryTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "studioComponentId": NotRequired[str],
        "subtype": NotRequired[StudioComponentSubtypeType],
        "type": NotRequired[StudioComponentTypeType],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)

StudioComponentTypeDef = TypedDict(
    "StudioComponentTypeDef",
    {
        "arn": NotRequired[str],
        "configuration": NotRequired["StudioComponentConfigurationTypeDef"],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "ec2SecurityGroupIds": NotRequired[List[str]],
        "initializationScripts": NotRequired[List["StudioComponentInitializationScriptTypeDef"]],
        "name": NotRequired[str],
        "scriptParameters": NotRequired[List["ScriptParameterKeyValueTypeDef"]],
        "state": NotRequired[StudioComponentStateType],
        "statusCode": NotRequired[StudioComponentStatusCodeType],
        "statusMessage": NotRequired[str],
        "studioComponentId": NotRequired[str],
        "subtype": NotRequired[StudioComponentSubtypeType],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[StudioComponentTypeType],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)

StudioEncryptionConfigurationTypeDef = TypedDict(
    "StudioEncryptionConfigurationTypeDef",
    {
        "keyType": StudioEncryptionConfigurationKeyTypeType,
        "keyArn": NotRequired[str],
    },
)

StudioMembershipTypeDef = TypedDict(
    "StudioMembershipTypeDef",
    {
        "identityStoreId": NotRequired[str],
        "persona": NotRequired[Literal["ADMINISTRATOR"]],
        "principalId": NotRequired[str],
        "sid": NotRequired[str],
    },
)

StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "adminRoleArn": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "displayName": NotRequired[str],
        "homeRegion": NotRequired[str],
        "ssoClientId": NotRequired[str],
        "state": NotRequired[StudioStateType],
        "statusCode": NotRequired[StudioStatusCodeType],
        "statusMessage": NotRequired[str],
        "studioEncryptionConfiguration": NotRequired["StudioEncryptionConfigurationTypeDef"],
        "studioId": NotRequired[str],
        "studioName": NotRequired[str],
        "studioUrl": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "updatedAt": NotRequired[datetime],
        "userRoleArn": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "UpdateLaunchProfileMemberRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "persona": Literal["USER"],
        "principalId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
    },
)

UpdateLaunchProfileMemberResponseTypeDef = TypedDict(
    "UpdateLaunchProfileMemberResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLaunchProfileRequestRequestTypeDef = TypedDict(
    "UpdateLaunchProfileRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "launchProfileProtocolVersions": NotRequired[Sequence[str]],
        "name": NotRequired[str],
        "streamConfiguration": NotRequired["StreamConfigurationCreateTypeDef"],
        "studioComponentIds": NotRequired[Sequence[str]],
    },
)

UpdateLaunchProfileResponseTypeDef = TypedDict(
    "UpdateLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStreamingImageRequestRequestTypeDef = TypedDict(
    "UpdateStreamingImageRequestRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)

UpdateStreamingImageResponseTypeDef = TypedDict(
    "UpdateStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStudioComponentRequestRequestTypeDef = TypedDict(
    "UpdateStudioComponentRequestRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
        "clientToken": NotRequired[str],
        "configuration": NotRequired["StudioComponentConfigurationTypeDef"],
        "description": NotRequired[str],
        "ec2SecurityGroupIds": NotRequired[Sequence[str]],
        "initializationScripts": NotRequired[
            Sequence["StudioComponentInitializationScriptTypeDef"]
        ],
        "name": NotRequired[str],
        "scriptParameters": NotRequired[Sequence["ScriptParameterKeyValueTypeDef"]],
        "subtype": NotRequired[StudioComponentSubtypeType],
        "type": NotRequired[StudioComponentTypeType],
    },
)

UpdateStudioComponentResponseTypeDef = TypedDict(
    "UpdateStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStudioRequestRequestTypeDef = TypedDict(
    "UpdateStudioRequestRequestTypeDef",
    {
        "studioId": str,
        "adminRoleArn": NotRequired[str],
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "userRoleArn": NotRequired[str],
    },
)

UpdateStudioResponseTypeDef = TypedDict(
    "UpdateStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationResultTypeDef = TypedDict(
    "ValidationResultTypeDef",
    {
        "state": LaunchProfileValidationStateType,
        "statusCode": LaunchProfileValidationStatusCodeType,
        "statusMessage": str,
        "type": LaunchProfileValidationTypeType,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
