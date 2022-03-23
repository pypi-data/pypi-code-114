"""
Type annotations for amp service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amp/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_amp.type_defs import AlertManagerDefinitionDescriptionTypeDef

    data: AlertManagerDefinitionDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AlertManagerDefinitionStatusCodeType,
    RuleGroupsNamespaceStatusCodeType,
    WorkspaceStatusCodeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlertManagerDefinitionDescriptionTypeDef",
    "AlertManagerDefinitionStatusTypeDef",
    "CreateAlertManagerDefinitionRequestRequestTypeDef",
    "CreateAlertManagerDefinitionResponseTypeDef",
    "CreateRuleGroupsNamespaceRequestRequestTypeDef",
    "CreateRuleGroupsNamespaceResponseTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteAlertManagerDefinitionRequestRequestTypeDef",
    "DeleteRuleGroupsNamespaceRequestRequestTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DescribeAlertManagerDefinitionRequestRequestTypeDef",
    "DescribeAlertManagerDefinitionResponseTypeDef",
    "DescribeRuleGroupsNamespaceRequestRequestTypeDef",
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "ListRuleGroupsNamespacesRequestRequestTypeDef",
    "ListRuleGroupsNamespacesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAlertManagerDefinitionRequestRequestTypeDef",
    "PutAlertManagerDefinitionResponseTypeDef",
    "PutRuleGroupsNamespaceRequestRequestTypeDef",
    "PutRuleGroupsNamespaceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuleGroupsNamespaceDescriptionTypeDef",
    "RuleGroupsNamespaceStatusTypeDef",
    "RuleGroupsNamespaceSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateWorkspaceAliasRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

AlertManagerDefinitionDescriptionTypeDef = TypedDict(
    "AlertManagerDefinitionDescriptionTypeDef",
    {
        "createdAt": datetime,
        "data": bytes,
        "modifiedAt": datetime,
        "status": "AlertManagerDefinitionStatusTypeDef",
    },
)

AlertManagerDefinitionStatusTypeDef = TypedDict(
    "AlertManagerDefinitionStatusTypeDef",
    {
        "statusCode": AlertManagerDefinitionStatusCodeType,
        "statusReason": NotRequired[str],
    },
)

CreateAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "CreateAlertManagerDefinitionRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "workspaceId": str,
        "clientToken": NotRequired[str],
    },
)

CreateAlertManagerDefinitionResponseTypeDef = TypedDict(
    "CreateAlertManagerDefinitionResponseTypeDef",
    {
        "status": "AlertManagerDefinitionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "CreateRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "name": str,
        "workspaceId": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "CreateRuleGroupsNamespaceResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "alias": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "tags": Dict[str, str],
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteAlertManagerDefinitionRequestRequestTypeDef",
    {
        "workspaceId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "name": str,
        "workspaceId": str,
        "clientToken": NotRequired[str],
    },
)

DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "clientToken": NotRequired[str],
    },
)

DescribeAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeAlertManagerDefinitionRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeAlertManagerDefinitionResponseTypeDef = TypedDict(
    "DescribeAlertManagerDefinitionResponseTypeDef",
    {
        "alertManagerDefinition": "AlertManagerDefinitionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "name": str,
        "workspaceId": str,
    },
)

DescribeRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    {
        "ruleGroupsNamespace": "RuleGroupsNamespaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleGroupsNamespacesRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsNamespacesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListRuleGroupsNamespacesResponseTypeDef = TypedDict(
    "ListRuleGroupsNamespacesResponseTypeDef",
    {
        "nextToken": str,
        "ruleGroupsNamespaces": List["RuleGroupsNamespaceSummaryTypeDef"],
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

ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "alias": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List["WorkspaceSummaryTypeDef"],
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

PutAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "PutAlertManagerDefinitionRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "workspaceId": str,
        "clientToken": NotRequired[str],
    },
)

PutAlertManagerDefinitionResponseTypeDef = TypedDict(
    "PutAlertManagerDefinitionResponseTypeDef",
    {
        "status": "AlertManagerDefinitionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "PutRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "name": str,
        "workspaceId": str,
        "clientToken": NotRequired[str],
    },
)

PutRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "PutRuleGroupsNamespaceResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": Dict[str, str],
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

RuleGroupsNamespaceDescriptionTypeDef = TypedDict(
    "RuleGroupsNamespaceDescriptionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "data": bytes,
        "modifiedAt": datetime,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": NotRequired[Dict[str, str]],
    },
)

RuleGroupsNamespaceStatusTypeDef = TypedDict(
    "RuleGroupsNamespaceStatusTypeDef",
    {
        "statusCode": RuleGroupsNamespaceStatusCodeType,
        "statusReason": NotRequired[str],
    },
)

RuleGroupsNamespaceSummaryTypeDef = TypedDict(
    "RuleGroupsNamespaceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": NotRequired[Dict[str, str]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateWorkspaceAliasRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceAliasRequestRequestTypeDef",
    {
        "workspaceId": str,
        "alias": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WorkspaceDescriptionTypeDef = TypedDict(
    "WorkspaceDescriptionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
        "alias": NotRequired[str],
        "prometheusEndpoint": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

WorkspaceStatusTypeDef = TypedDict(
    "WorkspaceStatusTypeDef",
    {
        "statusCode": WorkspaceStatusCodeType,
    },
)

WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
        "alias": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
