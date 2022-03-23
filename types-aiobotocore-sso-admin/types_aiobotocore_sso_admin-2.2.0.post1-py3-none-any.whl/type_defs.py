"""
Type annotations for sso-admin service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sso_admin.type_defs import AccessControlAttributeTypeDef

    data: AccessControlAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    InstanceAccessControlAttributeConfigurationStatusType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
    StatusValuesType,
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
    "AccessControlAttributeTypeDef",
    "AccessControlAttributeValueTypeDef",
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    "AttachedManagedPolicyTypeDef",
    "CreateAccountAssignmentRequestRequestTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "CreatePermissionSetRequestRequestTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "DeleteAccountAssignmentRequestRequestTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DeletePermissionSetRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    "DescribePermissionSetRequestRequestTypeDef",
    "DescribePermissionSetResponseTypeDef",
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    "InstanceAccessControlAttributeConfigurationTypeDef",
    "InstanceMetadataTypeDef",
    "ListAccountAssignmentCreationStatusRequestRequestTypeDef",
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    "ListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    "ListAccountAssignmentsRequestRequestTypeDef",
    "ListAccountAssignmentsResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    "ListPermissionSetProvisioningStatusRequestRequestTypeDef",
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    "ListPermissionSetsRequestRequestTypeDef",
    "ListPermissionSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "PermissionSetTypeDef",
    "ProvisionPermissionSetRequestRequestTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "UpdatePermissionSetRequestRequestTypeDef",
)

AccessControlAttributeTypeDef = TypedDict(
    "AccessControlAttributeTypeDef",
    {
        "Key": str,
        "Value": "AccessControlAttributeValueTypeDef",
    },
)

AccessControlAttributeValueTypeDef = TypedDict(
    "AccessControlAttributeValueTypeDef",
    {
        "Source": Sequence[str],
    },
)

AccountAssignmentOperationStatusMetadataTypeDef = TypedDict(
    "AccountAssignmentOperationStatusMetadataTypeDef",
    {
        "Status": NotRequired[StatusValuesType],
        "RequestId": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
    },
)

AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "Status": NotRequired[StatusValuesType],
        "RequestId": NotRequired[str],
        "FailureReason": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[Literal["AWS_ACCOUNT"]],
        "PermissionSetArn": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
        "PrincipalId": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
    },
)

AccountAssignmentTypeDef = TypedDict(
    "AccountAssignmentTypeDef",
    {
        "AccountId": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
        "PrincipalId": NotRequired[str],
    },
)

AttachManagedPolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ManagedPolicyArn": str,
    },
)

AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

CreateAccountAssignmentRequestRequestTypeDef = TypedDict(
    "CreateAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
    },
)

CreateAccountAssignmentResponseTypeDef = TypedDict(
    "CreateAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "InstanceAccessControlAttributeConfiguration": (
            "InstanceAccessControlAttributeConfigurationTypeDef"
        ),
    },
)

CreatePermissionSetRequestRequestTypeDef = TypedDict(
    "CreatePermissionSetRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceArn": str,
        "Description": NotRequired[str],
        "SessionDuration": NotRequired[str],
        "RelayState": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePermissionSetResponseTypeDef = TypedDict(
    "CreatePermissionSetResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccountAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
    },
)

DeleteAccountAssignmentResponseTypeDef = TypedDict(
    "DeleteAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DeletePermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribeAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountAssignmentCreationRequestId": str,
    },
)

DescribeAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountAssignmentDeletionRequestId": str,
    },
)

DescribeAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    {
        "Status": InstanceAccessControlAttributeConfigurationStatusType,
        "StatusReason": str,
        "InstanceAccessControlAttributeConfiguration": (
            "InstanceAccessControlAttributeConfigurationTypeDef"
        ),
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ProvisionPermissionSetRequestId": str,
    },
)

DescribePermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribePermissionSetResponseTypeDef = TypedDict(
    "DescribePermissionSetResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachManagedPolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ManagedPolicyArn": str,
    },
)

GetInlinePolicyForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

GetInlinePolicyForPermissionSetResponseTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    {
        "InlinePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAccessControlAttributeConfigurationTypeDef = TypedDict(
    "InstanceAccessControlAttributeConfigurationTypeDef",
    {
        "AccessControlAttributes": Sequence["AccessControlAttributeTypeDef"],
    },
)

InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef",
    {
        "InstanceArn": NotRequired[str],
        "IdentityStoreId": NotRequired[str],
    },
)

ListAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filter": NotRequired["OperationStatusFilterTypeDef"],
    },
)

ListAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentsCreationStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filter": NotRequired["OperationStatusFilterTypeDef"],
    },
)

ListAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentsDeletionStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountAssignmentsRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentsRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountId": str,
        "PermissionSetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAccountAssignmentsResponseTypeDef = TypedDict(
    "ListAccountAssignmentsResponseTypeDef",
    {
        "AccountAssignments": List["AccountAssignmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsForProvisionedPermissionSetRequestRequestTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ProvisioningStatus": NotRequired[ProvisioningStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAccountsForProvisionedPermissionSetResponseTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    {
        "AccountIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List["InstanceMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedPoliciesInPermissionSetRequestRequestTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListManagedPoliciesInPermissionSetResponseTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    {
        "AttachedManagedPolicies": List["AttachedManagedPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filter": NotRequired["OperationStatusFilterTypeDef"],
    },
)

ListPermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    {
        "PermissionSetsProvisioningStatus": List["PermissionSetProvisioningStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountId": str,
        "ProvisioningStatus": NotRequired[ProvisioningStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPermissionSetsProvisionedToAccountResponseTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionSetsRequestRequestTypeDef = TypedDict(
    "ListPermissionSetsRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPermissionSetsResponseTypeDef = TypedDict(
    "ListPermissionSetsResponseTypeDef",
    {
        "PermissionSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ResourceArn": str,
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationStatusFilterTypeDef = TypedDict(
    "OperationStatusFilterTypeDef",
    {
        "Status": NotRequired[StatusValuesType],
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

PermissionSetProvisioningStatusMetadataTypeDef = TypedDict(
    "PermissionSetProvisioningStatusMetadataTypeDef",
    {
        "Status": NotRequired[StatusValuesType],
        "RequestId": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
    },
)

PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "Status": NotRequired[StatusValuesType],
        "RequestId": NotRequired[str],
        "AccountId": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "FailureReason": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
    },
)

PermissionSetTypeDef = TypedDict(
    "PermissionSetTypeDef",
    {
        "Name": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "SessionDuration": NotRequired[str],
        "RelayState": NotRequired[str],
    },
)

ProvisionPermissionSetRequestRequestTypeDef = TypedDict(
    "ProvisionPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "TargetType": ProvisionTargetTypeType,
        "TargetId": NotRequired[str],
    },
)

ProvisionPermissionSetResponseTypeDef = TypedDict(
    "ProvisionPermissionSetResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInlinePolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "InlinePolicy": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
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
        "InstanceArn": str,
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "InstanceAccessControlAttributeConfiguration": (
            "InstanceAccessControlAttributeConfigurationTypeDef"
        ),
    },
)

UpdatePermissionSetRequestRequestTypeDef = TypedDict(
    "UpdatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "Description": NotRequired[str],
        "SessionDuration": NotRequired[str],
        "RelayState": NotRequired[str],
    },
)
