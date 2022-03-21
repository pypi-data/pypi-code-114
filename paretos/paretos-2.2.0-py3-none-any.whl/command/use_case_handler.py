from logging import Logger
from typing import Dict, List

from paretos.use_case.use_case_api_client import UseCaseApiClient
from paretos.service.exceptions import (
    InvalidResponseStructure,
    RequestFailed,
    ResponseParsingError,
)


class UseCaseHandler:
    def __init__(self, logger: Logger, api_client: UseCaseApiClient):
        self.__logger = logger
        self.__api_client = api_client

    def upload_training_data_file(self, use_case_id: str, file_path: str):
        try:
            self.__api_client.upload_training_data_file_from_path(
                use_case_id, file_path
            )
        except OSError as e:
            self.__logger.error("Could not open file for upload: %s", e)
            raise e
        except (RequestFailed, InvalidResponseStructure, ResponseParsingError) as e:
            self.__logger.error("Request failed: %s", e)
            raise e
