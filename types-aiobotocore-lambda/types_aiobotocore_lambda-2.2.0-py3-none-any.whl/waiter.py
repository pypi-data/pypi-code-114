"""
Type annotations for lambda service client waiters.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_lambda.client import LambdaClient
    from types_aiobotocore_lambda.waiter import (
        FunctionActiveWaiter,
        FunctionActiveV2Waiter,
        FunctionExistsWaiter,
        FunctionUpdatedWaiter,
        FunctionUpdatedV2Waiter,
    )

    session = get_session()
    async with session.create_client("lambda") as client:
        client: LambdaClient

        function_active_waiter: FunctionActiveWaiter = client.get_waiter("function_active")
        function_active_v2_waiter: FunctionActiveV2Waiter = client.get_waiter("function_active_v2")
        function_exists_waiter: FunctionExistsWaiter = client.get_waiter("function_exists")
        function_updated_waiter: FunctionUpdatedWaiter = client.get_waiter("function_updated")
        function_updated_v2_waiter: FunctionUpdatedV2Waiter = client.get_waiter("function_updated_v2")
    ```
"""
from aiobotocore.waiter import AIOWaiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "FunctionActiveWaiter",
    "FunctionActiveV2Waiter",
    "FunctionExistsWaiter",
    "FunctionUpdatedWaiter",
    "FunctionUpdatedV2Waiter",
)


class FunctionActiveWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionActive)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionactivewaiter)
    """

    async def wait(
        self, *, FunctionName: str, Qualifier: str = ..., WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionActive.wait)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionactivewaiter)
        """


class FunctionActiveV2Waiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionActiveV2)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionactivev2waiter)
    """

    async def wait(
        self, *, FunctionName: str, Qualifier: str = ..., WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionActiveV2.wait)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionactivev2waiter)
        """


class FunctionExistsWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionExists)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionexistswaiter)
    """

    async def wait(
        self, *, FunctionName: str, Qualifier: str = ..., WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionExists.wait)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionexistswaiter)
        """


class FunctionUpdatedWaiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionupdatedwaiter)
    """

    async def wait(
        self, *, FunctionName: str, Qualifier: str = ..., WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionUpdated.wait)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionupdatedwaiter)
        """


class FunctionUpdatedV2Waiter(AIOWaiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionUpdatedV2)
    [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionupdatedv2waiter)
    """

    async def wait(
        self, *, FunctionName: str, Qualifier: str = ..., WaiterConfig: WaiterConfigTypeDef = ...
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Waiter.FunctionUpdatedV2.wait)
        [Show types-aiobotocore documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/waiters.html#functionupdatedv2waiter)
        """
