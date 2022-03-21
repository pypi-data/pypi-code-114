from logging import Logger, LoggerAdapter
from typing import Union

from paretos.authentication.access_token_provider import AccessTokenProvider

from ..service.api_http_session import ApiHttpSession


class UseCaseApiHttpSession(ApiHttpSession):
    def __init__(
        self,
        api_url: str,
        access_token_provider: AccessTokenProvider,
        logger: Union[Logger, LoggerAdapter],
    ):
        super().__init__(api_url, "Use Case API", access_token_provider, logger)

    def get_customer_id(self):
        return self._access_token_provider.get_customer_id()
