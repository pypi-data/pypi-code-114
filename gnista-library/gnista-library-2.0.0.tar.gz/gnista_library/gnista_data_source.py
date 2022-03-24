import uuid
from typing import Any, List, Optional, Type, TypeVar, Union

from structlog import get_logger

from data_source_client import AuthenticatedClient
from data_source_client.api.data_source import (
    data_source_create_data_source,
    data_source_get,
    data_source_update_auto_detect_task_configs,
)
from data_source_client.models.auto_detect_task_config import AutoDetectTaskConfig
from data_source_client.models.create_data_source_request import CreateDataSourceRequest
from data_source_client.models.data_import_description_config import DataImportDescriptionConfig
from data_source_client.models.data_source_details_dto import DataSourceDetailsDTO
from data_source_client.models.en_data_source_state import EnDataSourceState
from data_source_client.models.problem_details import ProblemDetails
from data_source_client.models.update_auto_detect_task_configs_request import UpdateAutoDetectTaskConfigsRequest
from data_source_client.types import UNSET, Unset

from .gnista_connetion import GnistaConnection

log = get_logger()

# pylint: disable=C0103
T = TypeVar("T", bound="GnistaDataSource")


class GnistaDataSource:

    data_source_id: uuid.UUID
    data_import_description: Union[Unset, None, DataImportDescriptionConfig] = UNSET
    auto_detect_task_configs: Union[Unset, None, List[AutoDetectTaskConfig]] = UNSET
    details: Union[Unset, None, DataSourceDetailsDTO] = UNSET
    created_data_points: Union[Unset, None, List[str]] = UNSET
    state: Union[Unset, EnDataSourceState] = UNSET

    @classmethod
    def create_new(
        cls: Type[T],
        connection: GnistaConnection,
        request: CreateDataSourceRequest,
    ) -> Union[T, None]:
        token = connection.get_access_token()
        client = AuthenticatedClient(
            base_url=connection.datasource_base_url, token=token, verify_ssl=connection.verify_ssl
        )

        new_id = uuid.uuid4()
        response = data_source_create_data_source.sync(
            workspace_id=connection.workspace_id, data_source_id=str(new_id), client=client, json_body=request
        )

        if isinstance(response, ProblemDetails):
            log.error(response)
            return None

        data_source = cls(connection=connection, data_source_id=new_id)
        return data_source

    def __init__(self, connection: GnistaConnection, data_source_id: uuid.UUID):
        self.connection = connection
        self.data_source_id = data_source_id
        self._load_details()

    def __str__(self):
        return "GnistaDataSource " + self.data_source_id

    def _load_details(self):
        token = self.connection.get_access_token()
        client = AuthenticatedClient(
            base_url=self.connection.datasource_base_url, token=token, verify_ssl=self.connection.verify_ssl
        )

        data_source = data_source_get.sync(
            client=client,
            data_source_id=str(self.data_source_id),
            workspace_id=self.connection.workspace_id,
        )

        if data_source is None:
            raise Exception("Cannot load Datasource")

        self.data_import_description = data_source.data_import_description
        self.auto_detect_task_configs = data_source.auto_detect_task_configs
        self.details = data_source.details
        self.created_data_points = data_source.created_data_points
        self.state = data_source.state

    def update_auto_detect_task_configs(
        self, request: UpdateAutoDetectTaskConfigsRequest
    ) -> Optional[Union[Any, ProblemDetails]]:
        token = self.connection.get_access_token()
        client = AuthenticatedClient(
            base_url=self.connection.datasource_base_url, token=token, verify_ssl=self.connection.verify_ssl
        )

        response = data_source_update_auto_detect_task_configs.sync(
            client=client,
            data_source_id=str(self.data_source_id),
            workspace_id=self.connection.workspace_id,
            json_body=request,
        )

        if isinstance(response, ProblemDetails):
            log.error(response)

        return response
