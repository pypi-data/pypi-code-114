"""
Type annotations for mq service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef

    data: AvailabilityZoneTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AuthenticationStrategyType,
    BrokerStateType,
    BrokerStorageTypeType,
    ChangeTypeType,
    DayOfWeekType,
    DeploymentModeType,
    EngineTypeType,
    SanitizationWarningReasonType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AvailabilityZoneTypeDef",
    "BrokerEngineTypeTypeDef",
    "BrokerInstanceOptionTypeDef",
    "BrokerInstanceTypeDef",
    "BrokerSummaryTypeDef",
    "ConfigurationIdTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationsTypeDef",
    "CreateBrokerRequestRequestTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DeleteBrokerRequestRequestTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerRequestRequestTypeDef",
    "DescribeBrokerResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "ListBrokersRequestRequestTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PaginatorConfigTypeDef",
    "PendingLogsTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SanitizationWarningTypeDef",
    "UpdateBrokerRequestRequestTypeDef",
    "UpdateBrokerResponseTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserPendingChangesTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "WeeklyStartTimeTypeDef",
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)

BrokerEngineTypeTypeDef = TypedDict(
    "BrokerEngineTypeTypeDef",
    {
        "EngineType": NotRequired[EngineTypeType],
        "EngineVersions": NotRequired[List["EngineVersionTypeDef"]],
    },
)

BrokerInstanceOptionTypeDef = TypedDict(
    "BrokerInstanceOptionTypeDef",
    {
        "AvailabilityZones": NotRequired[List["AvailabilityZoneTypeDef"]],
        "EngineType": NotRequired[EngineTypeType],
        "HostInstanceType": NotRequired[str],
        "StorageType": NotRequired[BrokerStorageTypeType],
        "SupportedDeploymentModes": NotRequired[List[DeploymentModeType]],
        "SupportedEngineVersions": NotRequired[List[str]],
    },
)

BrokerInstanceTypeDef = TypedDict(
    "BrokerInstanceTypeDef",
    {
        "ConsoleURL": NotRequired[str],
        "Endpoints": NotRequired[List[str]],
        "IpAddress": NotRequired[str],
    },
)

BrokerSummaryTypeDef = TypedDict(
    "BrokerSummaryTypeDef",
    {
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
        "BrokerArn": NotRequired[str],
        "BrokerId": NotRequired[str],
        "BrokerName": NotRequired[str],
        "BrokerState": NotRequired[BrokerStateType],
        "Created": NotRequired[datetime],
        "HostInstanceType": NotRequired[str],
    },
)

ConfigurationIdTypeDef = TypedDict(
    "ConfigurationIdTypeDef",
    {
        "Id": str,
        "Revision": NotRequired[int],
    },
)

ConfigurationRevisionTypeDef = TypedDict(
    "ConfigurationRevisionTypeDef",
    {
        "Created": datetime,
        "Revision": int,
        "Description": NotRequired[str],
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": NotRequired[Dict[str, str]],
    },
)

ConfigurationsTypeDef = TypedDict(
    "ConfigurationsTypeDef",
    {
        "Current": NotRequired["ConfigurationIdTypeDef"],
        "History": NotRequired[List["ConfigurationIdTypeDef"]],
        "Pending": NotRequired["ConfigurationIdTypeDef"],
    },
)

CreateBrokerRequestRequestTypeDef = TypedDict(
    "CreateBrokerRequestRequestTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerName": str,
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "PubliclyAccessible": bool,
        "Users": Sequence["UserTypeDef"],
        "AuthenticationStrategy": NotRequired[AuthenticationStrategyType],
        "Configuration": NotRequired["ConfigurationIdTypeDef"],
        "CreatorRequestId": NotRequired[str],
        "EncryptionOptions": NotRequired["EncryptionOptionsTypeDef"],
        "LdapServerMetadata": NotRequired["LdapServerMetadataInputTypeDef"],
        "Logs": NotRequired["LogsTypeDef"],
        "MaintenanceWindowStartTime": NotRequired["WeeklyStartTimeTypeDef"],
        "SecurityGroups": NotRequired[Sequence[str]],
        "StorageType": NotRequired[BrokerStorageTypeType],
        "SubnetIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateBrokerResponseTypeDef = TypedDict(
    "CreateBrokerResponseTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConfigurationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationRequestRequestTypeDef",
    {
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Name": str,
        "AuthenticationStrategy": NotRequired[AuthenticationStrategyType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Password": str,
        "Username": str,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
    },
)

DeleteBrokerRequestRequestTypeDef = TypedDict(
    "DeleteBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DeleteBrokerResponseTypeDef = TypedDict(
    "DeleteBrokerResponseTypeDef",
    {
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeBrokerEngineTypesRequestRequestTypeDef = TypedDict(
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    {
        "EngineType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "DescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List["BrokerEngineTypeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerInstanceOptionsRequestRequestTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    {
        "EngineType": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StorageType": NotRequired[str],
    },
)

DescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List["BrokerInstanceOptionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerRequestRequestTypeDef = TypedDict(
    "DescribeBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DescribeBrokerResponseTypeDef = TypedDict(
    "DescribeBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List["BrokerInstanceTypeDef"],
        "BrokerName": str,
        "BrokerState": BrokerStateType,
        "Configurations": "ConfigurationsTypeDef",
        "Created": datetime,
        "DeploymentMode": DeploymentModeType,
        "EncryptionOptions": "EncryptionOptionsTypeDef",
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsSummaryTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "PendingAuthenticationStrategy": AuthenticationStrategyType,
        "PendingEngineVersion": str,
        "PendingHostInstanceType": str,
        "PendingLdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "PendingSecurityGroups": List[str],
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": BrokerStorageTypeType,
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List["UserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "ConfigurationRevision": str,
    },
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "ConfigurationId": str,
        "Created": datetime,
        "Data": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": "UserPendingChangesTypeDef",
        "Username": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionOptionsTypeDef = TypedDict(
    "EncryptionOptionsTypeDef",
    {
        "UseAwsOwnedKey": bool,
        "KmsKeyId": NotRequired[str],
    },
)

EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "Name": NotRequired[str],
    },
)

LdapServerMetadataInputTypeDef = TypedDict(
    "LdapServerMetadataInputTypeDef",
    {
        "Hosts": Sequence[str],
        "RoleBase": str,
        "RoleSearchMatching": str,
        "ServiceAccountPassword": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserSearchMatching": str,
        "RoleName": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "UserRoleName": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)

LdapServerMetadataOutputTypeDef = TypedDict(
    "LdapServerMetadataOutputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleSearchMatching": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserSearchMatching": str,
        "RoleName": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "UserRoleName": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)

ListBrokersRequestRequestTypeDef = TypedDict(
    "ListBrokersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListBrokersResponseTypeDef = TypedDict(
    "ListBrokersResponseTypeDef",
    {
        "BrokerSummaries": List["BrokerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "ListConfigurationRevisionsRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List["ConfigurationTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "BrokerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "NextToken": str,
        "Users": List["UserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogsSummaryTypeDef = TypedDict(
    "LogsSummaryTypeDef",
    {
        "General": bool,
        "GeneralLogGroup": str,
        "Audit": NotRequired[bool],
        "AuditLogGroup": NotRequired[str],
        "Pending": NotRequired["PendingLogsTypeDef"],
    },
)

LogsTypeDef = TypedDict(
    "LogsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
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

PendingLogsTypeDef = TypedDict(
    "PendingLogsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
    },
)

RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
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

SanitizationWarningTypeDef = TypedDict(
    "SanitizationWarningTypeDef",
    {
        "Reason": SanitizationWarningReasonType,
        "AttributeName": NotRequired[str],
        "ElementName": NotRequired[str],
    },
)

UpdateBrokerRequestRequestTypeDef = TypedDict(
    "UpdateBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
        "AuthenticationStrategy": NotRequired[AuthenticationStrategyType],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Configuration": NotRequired["ConfigurationIdTypeDef"],
        "EngineVersion": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "LdapServerMetadata": NotRequired["LdapServerMetadataInputTypeDef"],
        "Logs": NotRequired["LogsTypeDef"],
        "MaintenanceWindowStartTime": NotRequired["WeeklyStartTimeTypeDef"],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)

UpdateBrokerResponseTypeDef = TypedDict(
    "UpdateBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": "ConfigurationIdTypeDef",
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "Data": str,
        "Description": NotRequired[str],
    },
)

UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Warnings": List["SanitizationWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Password": NotRequired[str],
    },
)

UserPendingChangesTypeDef = TypedDict(
    "UserPendingChangesTypeDef",
    {
        "PendingChange": ChangeTypeType,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[List[str]],
    },
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Username": str,
        "PendingChange": NotRequired[ChangeTypeType],
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Password": str,
        "Username": str,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
    },
)

WeeklyStartTimeTypeDef = TypedDict(
    "WeeklyStartTimeTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "TimeOfDay": str,
        "TimeZone": NotRequired[str],
    },
)
