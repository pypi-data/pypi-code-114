"""
Type annotations for workspaces service client paginators.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_workspaces.client import WorkSpacesClient
    from types_aiobotocore_workspaces.paginator import (
        DescribeAccountModificationsPaginator,
        DescribeIpGroupsPaginator,
        DescribeWorkspaceBundlesPaginator,
        DescribeWorkspaceDirectoriesPaginator,
        DescribeWorkspaceImagesPaginator,
        DescribeWorkspacesPaginator,
        DescribeWorkspacesConnectionStatusPaginator,
        ListAvailableManagementCidrRangesPaginator,
    )

    session = get_session()
    with session.create_client("workspaces") as client:
        client: WorkSpacesClient

        describe_account_modifications_paginator: DescribeAccountModificationsPaginator = client.get_paginator("describe_account_modifications")
        describe_ip_groups_paginator: DescribeIpGroupsPaginator = client.get_paginator("describe_ip_groups")
        describe_workspace_bundles_paginator: DescribeWorkspaceBundlesPaginator = client.get_paginator("describe_workspace_bundles")
        describe_workspace_directories_paginator: DescribeWorkspaceDirectoriesPaginator = client.get_paginator("describe_workspace_directories")
        describe_workspace_images_paginator: DescribeWorkspaceImagesPaginator = client.get_paginator("describe_workspace_images")
        describe_workspaces_paginator: DescribeWorkspacesPaginator = client.get_paginator("describe_workspaces")
        describe_workspaces_connection_status_paginator: DescribeWorkspacesConnectionStatusPaginator = client.get_paginator("describe_workspaces_connection_status")
        list_available_management_cidr_ranges_paginator: ListAvailableManagementCidrRangesPaginator = client.get_paginator("list_available_management_cidr_ranges")
    ```
"""
import sys
from typing import Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import ImageTypeType
from .type_defs import (
    DescribeAccountModificationsResultTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspacesResultTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import AsyncIterator
else:
    from typing_extensions import AsyncIterator


__all__ = (
    "DescribeAccountModificationsPaginator",
    "DescribeIpGroupsPaginator",
    "DescribeWorkspaceBundlesPaginator",
    "DescribeWorkspaceDirectoriesPaginator",
    "DescribeWorkspaceImagesPaginator",
    "DescribeWorkspacesPaginator",
    "DescribeWorkspacesConnectionStatusPaginator",
    "ListAvailableManagementCidrRangesPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class DescribeAccountModificationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeaccountmodificationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeAccountModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeaccountmodificationspaginator)
        """


class DescribeIpGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeipgroupspaginator)
    """

    def paginate(
        self, *, GroupIds: Sequence[str] = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeIpGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeipgroupspaginator)
        """


class DescribeWorkspaceBundlesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacebundlespaginator)
    """

    def paginate(
        self,
        *,
        BundleIds: Sequence[str] = ...,
        Owner: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeWorkspaceBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacebundlespaginator)
        """


class DescribeWorkspaceDirectoriesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacedirectoriespaginator)
    """

    def paginate(
        self,
        *,
        DirectoryIds: Sequence[str] = ...,
        Limit: int = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeWorkspaceDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacedirectoriespaginator)
        """


class DescribeWorkspaceImagesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspaceimagespaginator)
    """

    def paginate(
        self,
        *,
        ImageIds: Sequence[str] = ...,
        ImageType: ImageTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeWorkspaceImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspaceimagespaginator)
        """


class DescribeWorkspacesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacespaginator)
    """

    def paginate(
        self,
        *,
        WorkspaceIds: Sequence[str] = ...,
        DirectoryId: str = ...,
        UserName: str = ...,
        BundleId: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeWorkspacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacespaginator)
        """


class DescribeWorkspacesConnectionStatusPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacesconnectionstatuspaginator)
    """

    def paginate(
        self, *, WorkspaceIds: Sequence[str] = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[DescribeWorkspacesConnectionStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#describeworkspacesconnectionstatuspaginator)
        """


class ListAvailableManagementCidrRangesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#listavailablemanagementcidrrangespaginator)
    """

    def paginate(
        self, *, ManagementCidrRangeConstraint: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListAvailableManagementCidrRangesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/paginators.html#listavailablemanagementcidrrangespaginator)
        """
