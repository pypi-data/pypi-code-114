"""
Type annotations for amplifyuibuilder service client paginators.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_amplifyuibuilder.client import AmplifyUIBuilderClient
    from types_aiobotocore_amplifyuibuilder.paginator import (
        ExportComponentsPaginator,
        ExportThemesPaginator,
        ListComponentsPaginator,
        ListThemesPaginator,
    )

    session = get_session()
    with session.create_client("amplifyuibuilder") as client:
        client: AmplifyUIBuilderClient

        export_components_paginator: ExportComponentsPaginator = client.get_paginator("export_components")
        export_themes_paginator: ExportThemesPaginator = client.get_paginator("export_themes")
        list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
        list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    ```
"""
import sys
from typing import Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .type_defs import (
    ExportComponentsResponseTypeDef,
    ExportThemesResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListThemesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import AsyncIterator
else:
    from typing_extensions import AsyncIterator


__all__ = (
    "ExportComponentsPaginator",
    "ExportThemesPaginator",
    "ListComponentsPaginator",
    "ListThemesPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ExportComponentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportComponents)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#exportcomponentspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ExportComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportComponents.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#exportcomponentspaginator)
        """


class ExportThemesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportThemes)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#exportthemespaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ExportThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ExportThemes.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#exportthemespaginator)
        """


class ListComponentsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListComponents)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#listcomponentspaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListComponents.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#listcomponentspaginator)
        """


class ListThemesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListThemes)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#listthemespaginator)
    """

    def paginate(
        self, *, appId: str, environmentName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Paginator.ListThemes.paginate)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/paginators.html#listthemespaginator)
        """
