from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import cached_property, wraps
from math import ceil
from types import FunctionType
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

import pandas as pd
from atoti_core import (
    HierarchyCoordinates,
    JavaType,
    LevelCoordinates,
    MissingPluginError,
    convert_to_pandas,
    coordinates_to_java_description,
    deprecated,
    get_env_flag,
    is_array_type,
    keyword_only_dataclass,
    parse_java_type,
)
from py4j.clientserver import ClientServer, JavaParameters, PythonParameters
from py4j.java_collections import JavaMap, ListConverter
from py4j.java_gateway import JavaObject
from py4j.protocol import Py4JJavaError

from ._data_type_utils import parse_data_type
from ._endpoint import EndpointHandler
from ._hierarchy_arguments import HierarchyArguments
from ._level_arguments import LevelArguments
from ._partial_aggregate_providers import PartialAggregateProvider
from ._py4j_utils import (
    to_java_map,
    to_java_object_array,
    to_java_object_list,
    to_java_string_array,
    to_python_dict,
    to_python_list,
)
from ._query_plan import ExternalRetrieval, PivotRetrieval, QueryAnalysis, QueryPlan
from ._sources.csv import CsvFileFormat
from ._transaction import Transaction, is_inside_transaction
from .client_side_encryption_config import ClientSideEncryptionConfig
from .config._session_config import SessionConfig, serialize_config_to_json
from .exceptions import AtotiJavaException
from .order import CustomOrder, NaturalOrder, Order
from .report import LoadingReport, _warn_new_errors
from .type import DataType

_ATOTI_VERBOSE_JAVA_EXCEPTIONS = "ATOTI_VERBOSE_JAVA_EXCEPTIONS"


def _convert_java_levels_to_level_arguments(
    java_levels: JavaMap,  # type: ignore
) -> Dict[str, LevelArguments]:
    jlevels_dict = to_python_dict(java_levels)
    levels = {}
    for (name, jlvl) in jlevels_dict.items():
        comparator_key = jlvl.getComparatorKey()
        first_elements = (
            list(jlvl.getFirstMembers()) if jlvl.getFirstMembers() is not None else None
        )
        order = _java_comparator_to_python_order(
            comparator_key=comparator_key,
            first_elements=first_elements,
        )
        levels[name] = (
            name,
            jlvl.getPropertyName(),
            parse_data_type(jlvl.getType().getDetailType()),
            order,
        )
    return levels


def _java_comparator_to_python_order(
    *, comparator_key: str, first_elements: Optional[Sequence[Any]] = None
) -> Order:
    if comparator_key == CustomOrder(first_elements=())._key:
        return CustomOrder(first_elements=first_elements or [])

    return NaturalOrder(ascending="reverse" not in comparator_key.lower())


def _convert_java_description_to_level_coordinates(
    java_description: str,
) -> LevelCoordinates:
    level, hierarchy, dimension = java_description.split("@")
    return (dimension, hierarchy, level)


def _convert_java_hierarchies_to_python_hierarchies_arguments(
    java_hierarchies: Iterable[Any],
) -> List[HierarchyArguments]:
    return [
        HierarchyArguments(
            name=java_hierarchy.getName(),
            levels_arguments=_convert_java_levels_to_level_arguments(
                java_hierarchy.getLevels()
            ),
            dimension=java_hierarchy.getDimensionName(),
            slicing=java_hierarchy.getSlicing(),
            visible=java_hierarchy.getVisible(),
        )
        for java_hierarchy in java_hierarchies
    ]


def _enhance_py4j_errors(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
    @wraps(function)
    def wrapped_method(self: JavaApi, *args: Any, **kwargs: Any) -> Any:
        try:
            return function(self, *args, **kwargs)
        except Py4JJavaError as java_exception:
            cause = (
                str(java_exception)
                if get_env_flag(_ATOTI_VERBOSE_JAVA_EXCEPTIONS)
                else self.get_throwable_root_cause(java_exception.java_exception)
            )
            raise AtotiJavaException(
                cause,
                java_traceback=str(java_exception),
                java_exception=java_exception,
            ) from None

    return wrapped_method


class ApiMetaClass(type):
    """Meta class for the API calls."""

    def __new__(  # pylint: disable=too-many-positional-parameters
        cls, classname: str, bases: Tuple[type, ...], class_dict: Mapping[str, Any]
    ) -> ApiMetaClass:
        """Automatically wrap all of the classes methods.

        This class applies the api_call_wrapper to all of a particular classes methods.
        This allows for cleaner handling of Py4J related exceptions.
        """
        new_class_dict = {}
        for attribute_name, attribute in class_dict.items():
            if isinstance(attribute, FunctionType):
                attribute = _enhance_py4j_errors(attribute)
            new_class_dict[attribute_name] = attribute
        return type.__new__(cls, classname, bases, new_class_dict)


_REALTIME_SOURCE_KEYS = ["KAFKA"]

# pylint: disable=too-many-lines
class JavaApi(metaclass=ApiMetaClass):
    """API for communicating with the JVM."""

    _client_side_encryption: Optional[ClientSideEncryptionConfig] = None

    def __init__(
        self,
        *,
        auth_token: Optional[str] = None,
        py4j_java_port: Optional[int] = None,
        distributed: bool = False,
    ):
        """Create the Java gateway."""
        self.gateway: ClientServer = JavaApi._create_py4j_gateway(
            auth_token=auth_token, py4j_java_port=py4j_java_port
        )
        self.java_session: JavaObject = self.gateway.entry_point
        self.java_session.api(distributed)

    @property
    def java_api(self) -> Any:
        return self.java_session.api()

    @staticmethod
    def _create_py4j_gateway(
        *, auth_token: Optional[str] = None, py4j_java_port: Optional[int] = None
    ) -> ClientServer:
        # Connect to the Java side using the provided Java port and start the Python callback server with a dynamic port.
        gateway = ClientServer(
            java_parameters=JavaParameters(auth_token=auth_token, port=py4j_java_port),
            python_parameters=PythonParameters(daemonize=True, port=0),
        )

        # Retrieve the port on which the python callback server was bound to.
        cb_server = gateway.get_callback_server()
        if cb_server is None:
            raise ValueError("Null callback server from py4j gateway")
        python_port = cb_server.get_listening_port()

        # Tell the Java side to connect to the Python callback server with the new Python port.
        gateway_server = gateway.java_gateway_server
        if gateway_server is None:
            raise ValueError("Null gateway server from py4j gateway")
        # ignore type next line because we do some Java calls
        gateway_server.resetCallbackClient(
            gateway_server.getCallbackClient().getAddress(),
            python_port,
        )

        return gateway

    def shutdown(self) -> None:
        """Shutdown the connection to the Java gateway."""
        self.gateway.shutdown()

    def refresh(self) -> None:
        """Refresh the Java session."""
        self.java_api.refresh()
        _warn_new_errors(self.get_new_load_errors())

    @cached_property
    def license_end_date(self) -> datetime:
        return datetime.fromtimestamp(self.java_session.getLicenseEndDate() / 1000)

    @cached_property
    def is_community_license(self) -> bool:
        return cast(bool, self.java_session.isCommunityLicense())

    def publish_measures(self, cube_name: str) -> None:
        """Publish the new measures."""
        self._outside_transaction_api().publishMeasures(cube_name)

    def clear_session(self) -> None:
        """Refresh the pivot."""
        self.java_api.clearSession()

    def get_session_port(self) -> int:
        """Return the port of the session."""
        return cast(int, self.java_session.getPort())

    def get_throwable_root_cause(self, throwable: Any) -> str:
        """Get the root cause of a java exception."""
        return cast(str, self.java_api.getRootCause(throwable))

    def generate_jwt(self) -> str:
        """Return the JWT required to authenticate against to this session."""
        return cast(str, self.java_session.generateJwt())

    def create_endpoint(
        self,
        *,
        http_method: Literal["POST", "GET", "PUT", "DELETE"],
        route: str,
        handler: EndpointHandler,
    ) -> None:
        """Create a new custom endpoint."""
        self._outside_transaction_api().createEndpoint(
            http_method,
            route,
            handler,
        )

    def delete_role(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def upsert_role(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_role_mapping(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def upsert_role_mapping(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def remove_role_from_role_mapping(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def set_locale(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> None:
        """Set the locale to use for the session."""
        raise MissingPluginError("plus")

    def export_i18n_template(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        """Generate a template translations file at the desired location."""
        raise MissingPluginError("plus")

    def start_application(self, config: SessionConfig) -> None:
        """Start the application."""
        json_config = serialize_config_to_json(config)
        self.java_session.startServer(json_config)

    def _create_java_types(self, types: Mapping[str, DataType]) -> Any:
        """Convert the python types to java types."""
        # pylint: disable=invalid-name
        JavaColumnType = self.gateway.jvm.io.atoti.loading.impl.TypeImpl
        # pylint: enable=invalid-name
        converted = {
            field: JavaColumnType(type_value.java_type, type_value.nullable)
            for (field, type_value) in types.items()
        }
        return to_java_map(converted, gateway=self.gateway)

    def _create_java_types_list(self, types: Iterable[DataType]) -> JavaObject:
        """Convert list of python types to java types."""
        converted = [
            self._get_java_object_from_data_type(type_value) for type_value in types
        ]
        return to_java_object_list(converted, gateway=self.gateway)

    def _create_java_types_list_from_javatype(
        self, types: Iterable[JavaType]
    ) -> JavaObject:
        """Convert list of python types to java types."""
        converted = [
            self._get_java_object_from_java_type(type_value) for type_value in types
        ]
        return to_java_object_list(converted, gateway=self.gateway)

    def _get_java_object_from_data_type(self, data_type: DataType) -> JavaObject:
        # pylint: disable=invalid-name
        atoti_package = self.gateway.jvm.io.atoti
        JavaColumnType = atoti_package.loading.impl.TypeImpl
        # pylint: enable=invalid-name
        return JavaColumnType(data_type.java_type, data_type.nullable)

    def _get_java_object_from_java_type(self, java_type: JavaType) -> Any:
        # pylint: disable=invalid-name
        atoti_package = self.gateway.jvm.io.atoti
        JavaColumnType = atoti_package.loading.impl.TypeImpl
        # pylint: enable=invalid-name
        return JavaColumnType(java_type, True)

    def _outside_transaction_api(self) -> Any:
        return self.java_api.outsideTransactionApi(is_inside_transaction())

    def _enterprise_api(self) -> Any:
        return self.java_api.enterpriseApi(is_inside_transaction())

    def get_tables(self) -> List[str]:
        """List all the tables of the session."""
        return to_python_list(self.java_api.getStores())

    def create_table_params(
        self,
        *,
        keys: Iterable[str],
        partitioning: Optional[str],
        types: Mapping[str, DataType],
        hierarchized_columns: Optional[Iterable[str]] = None,
        is_parameter_table: bool,
    ) -> Any:
        """Create the table parameters."""
        java_keys = ListConverter().convert(keys, self.gateway._gateway_client)
        java_types = self._create_java_types(types)
        java_hierarchized_columns = (
            ListConverter().convert(hierarchized_columns, self.gateway._gateway_client)
            if hierarchized_columns is not None
            else None
        )
        package = self.gateway.jvm.io.atoti.loading.impl
        params = package.StoreParams(
            java_keys,
            partitioning,
            java_types,
            java_hierarchized_columns,
            is_parameter_table,
        )
        return params

    def create_loading_params(
        self,
        *,
        scenario_name: str,
    ) -> Any:
        """Create the loading parameters."""
        package = self.gateway.jvm.io.atoti.loading.impl
        params = package.LoadingParams()
        params.setBranch(scenario_name)
        return params

    def create_table(
        self,
        name: str,
        *,
        types: Mapping[str, DataType],
        keys: Iterable[str],
        partitioning: Optional[str],
        hierarchized_columns: Optional[Iterable[str]],
        is_parameter_table: bool,
    ) -> None:
        """Create a java store from its schema."""
        table_params = self.create_table_params(
            keys=keys,
            partitioning=partitioning,
            types=types,
            hierarchized_columns=hierarchized_columns,
            is_parameter_table=is_parameter_table,
        )
        self._outside_transaction_api().createStore(name, table_params)

    def delete_table(self, table_name: str) -> None:
        self._outside_transaction_api().deleteStore(table_name)

    def convert_source_params(self, params: Mapping[str, Any]) -> Any:
        """Convert the params to Java Objects."""
        java_params = {}
        for param in params:
            value = params[param]
            if isinstance(value, Mapping):
                value = to_java_map(value, gateway=self.gateway)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                value = to_java_object_list(value, gateway=self.gateway)
            java_params[param] = value
        return to_java_map(java_params, gateway=self.gateway)

    def discover_csv_file_format(
        self,
        *,
        keys: Iterable[str],
        source_params: Mapping[str, Any],
    ) -> CsvFileFormat:
        source_params = self.convert_source_params(source_params)
        types = {}
        java_csv_format = self._outside_transaction_api().discoverCsvFileFormat(
            to_java_object_list(keys, gateway=self.gateway),
            source_params,
        )
        for column_name, java_type in to_python_dict(
            java_csv_format.getTypes()
        ).items():
            data_type = DataType(
                java_type=parse_java_type(java_type.getJavaType()),
                nullable=java_type.nullable(),
            )
            types[column_name] = data_type

        file_format = CsvFileFormat(
            process_quotes=java_csv_format.shouldProcessQuotes(),
            separator=java_csv_format.getSeparator(),
            types=types,
            date_patterns=to_python_dict(java_csv_format.getDatePatterns()),
        )
        return file_format

    def infer_table_types_from_source(
        self,
        *,
        source_key: str,
        keys: Iterable[str],
        source_params: Mapping[str, Any],
    ) -> Dict[str, DataType]:
        """Infer Table types from a data source."""
        source_params = self.convert_source_params(source_params)
        types = {}
        for column_name, java_type in to_python_dict(
            self._outside_transaction_api().inferTypesFromDataSource(
                source_key,
                to_java_object_list(keys, gateway=self.gateway),
                source_params,
            )
        ).items():
            types[column_name] = DataType(
                java_type=parse_java_type(java_type.getJavaType()),
                nullable=java_type.nullable(),
            )
        return types

    def load_data_into_table(
        self,
        table_name: str,
        *,
        source_key: str,
        scenario_name: str,
        source_params: Mapping[str, Any],
    ) -> None:
        """Load the data into an existing table with a given source."""
        load_params = self.create_loading_params(scenario_name=scenario_name)
        source_params = self.convert_source_params(source_params)
        self._inside_transaction(
            lambda: cast(
                None,
                self.java_api.loadDataSourceIntoStore(
                    table_name,
                    source_key,
                    load_params,
                    source_params,
                ),
            ),
            scenario_name=scenario_name,
            source_key=source_key,
        )

        # Check if errors happened during the loading
        _warn_new_errors(self.get_new_load_errors())

    def create_scenario(self, scenario_name: str, parent_scenario: str) -> None:
        """Create a new scenario on the table."""
        self._outside_transaction_api().createBranch(scenario_name, parent_scenario)

    def get_scenarios(self) -> List[str]:
        """Get the list of scenarios defined in the current session."""
        return to_python_list(self.java_api.getBranches())

    def delete_scenario(self, scenario: str) -> None:
        """Delete a scenario from the table."""
        self._outside_transaction_api().deleteBranch(scenario)

    def start_transaction(self, *, scenario_name: str, is_user_initiated: bool) -> int:
        """Start a multi operation transaction on the datastore."""
        return cast(
            int, self.java_api.startTransaction(scenario_name, is_user_initiated)
        )

    def end_transaction(
        self, *, has_succeeded: bool, transaction_id: Optional[int]
    ) -> None:
        """End a multi operation transaction on the datastore."""
        self.java_api.endTransaction(has_succeeded, transaction_id)

    def get_aggregates_cache_capacity(self, *, cube_name: str) -> int:
        jcache_desc = self._outside_transaction_api().getAggregatesCacheDescription(
            cube_name
        )
        return cast(int, jcache_desc.getSize())

    def set_aggregates_cache_capacity(self, capacity: int, *, cube_name: str) -> None:
        self._outside_transaction_api().setAggregatesCache(cube_name, capacity)

    def _convert_partial_provider(self, provider: PartialAggregateProvider) -> Any:
        """Convert the partial provider to the Java Object."""
        levels = ListConverter().convert(
            [
                coordinates_to_java_description(level_coordinates)
                for level_coordinates in provider.levels_coordinates
            ],
            self.gateway._gateway_client,
        )
        measures = ListConverter().convert(
            provider.measures_names,
            self.gateway._gateway_client,
        )
        java_class: Any = self.gateway.jvm.io.atoti.api.impl.PythonPartialProvider  # type: ignore
        return java_class(provider.key, levels, measures)

    def get_aggregate_providers(
        self,
        cube_name: str,
    ) -> List[PartialAggregateProvider]:
        """Get the partial aggregates providers."""
        java_providers = self._outside_transaction_api().getPartialAggregateProviders(
            cube_name
        )
        return [
            PartialAggregateProvider(
                key=provider.getKey(),
                levels_coordinates=[
                    _convert_java_description_to_level_coordinates(level)
                    for level in to_python_list(provider.getLevels())
                ],
                measures_names=to_python_list(provider.getMeasures()),
            )
            for provider in to_python_list(java_providers)
        ]

    def set_aggregate_providers(
        self,
        cube_name: str,
        providers: Iterable[PartialAggregateProvider],
    ) -> None:
        """Set the partial aggregate providers."""
        java_providers = ListConverter().convert(
            [self._convert_partial_provider(provider) for provider in providers],
            self.gateway._gateway_client,
        )
        self._outside_transaction_api().setPartialAggregateProviders(
            cube_name, java_providers
        )

    def join_distributed_cluster(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        """Join the distributed cluster at the given address for the given distributed cube."""
        raise MissingPluginError("plus")

    @keyword_only_dataclass
    @dataclass(frozen=True)
    class ColumnDescription:
        """Table column description."""

        name: str
        data_type: DataType

    def get_table_schema(self, table_name: str) -> List[JavaApi.ColumnDescription]:
        """Return the schema of the java table."""
        schema = self.java_api.getStoreSchema(table_name)
        columns_descriptions = []
        for i in range(0, len(list(schema.fieldNames()))):
            columns_descriptions.append(
                JavaApi.ColumnDescription(
                    name=schema.fieldNames()[i],
                    data_type=DataType(
                        java_type=parse_java_type(schema.types()[i].getJavaType()),
                        nullable=schema.types()[i].nullable(),
                    ),
                )
            )
        return columns_descriptions

    def get_table_partitioning(self, table_name: str) -> str:
        """Return the table's partitioning."""
        return cast(
            str, self._outside_transaction_api().getStorePartitioning(table_name)
        )

    @staticmethod
    def _convert_reports(reports: Any) -> List[LoadingReport]:
        """Convert the Java report to Python ones."""
        return [
            LoadingReport(
                name=r.getName(),
                source=r.getType(),
                loaded=r.getLoadedCount(),
                errors=r.getErrorCount(),
                duration=r.getDuration(),
                error_messages=to_python_list(r.getFailureMessages()),
            )
            for r in to_python_list(reports)
        ]

    def get_loading_report(self, table_name: str) -> List[LoadingReport]:
        """Return the loading report of the table."""
        reports = self.java_api.getLoadingReports(table_name)
        return self._convert_reports(reports)

    def get_new_load_errors(self) -> Dict[str, int]:
        """Return the new loading errors per table."""
        errors = self.java_api.getNewLoadingErrors()
        return to_python_dict(errors)

    def get_key_columns(self, table_name: str) -> List[str]:
        """Return the list of key columns for the table."""
        java_columns = self._outside_transaction_api().getKeyFields(table_name)
        return to_python_list(java_columns)

    def get_selection_fields(self, cube_name: str) -> List[str]:
        """Return the list of fields that are part of the cube's datastore selection."""
        java_fields = self._outside_transaction_api().getSelectionFields(cube_name)
        return to_python_list(java_fields)

    def create_cube_from_table(
        self,
        *,
        table_name: str,
        cube_name: str,
        creation_mode: str,
    ) -> None:
        """Create a cube from a given table."""
        self._outside_transaction_api().createCubeFromStore(
            table_name, cube_name, creation_mode
        )

    def create_distributed_cube(self, cube_name: str) -> None:
        """Create a distributed cube."""
        self.java_api.createDistributedCube(cube_name)

    def generate_cube_schema_image(self, cube_name: str) -> str:
        """Generate the cube schema image and return its path."""
        return cast(str, self._outside_transaction_api().getCubeSchemaPath(cube_name))

    def generate_datastore_schema_image(self) -> str:
        """Generate the datastore schema image and return its path."""
        return cast(str, self._outside_transaction_api().getDatastoreSchemaPath())

    def delete_cube(self, cube_name: str) -> None:
        """Delete a cube from the current session."""
        self._outside_transaction_api().deleteCube(cube_name)

    def create_join(
        self,
        table_name: str,
        other_table_name: str,
        *,
        mapping: Optional[Mapping[str, str]],
    ) -> None:
        """Define a join between two tables."""
        jmapping = (
            to_java_map(mapping, gateway=self.gateway) if mapping is not None else None
        )

        self._outside_transaction_api().createReferences(
            table_name, other_table_name, jmapping
        )

    def get_table_size(self, table_name: str, *, table_scenario: str) -> int:
        """Get the size of the table on its current scenario."""
        return cast(
            int,
            self._outside_transaction_api().getStoreSize(table_name, table_scenario),
        )

    def delete_rows_from_table(
        self,
        *,
        table_name: str,
        scenario_name: str,
        coordinates: Iterable[Mapping[str, Any]],
    ) -> None:
        """Delete rows from the table matching the provided coordinates."""
        jcoordinates_list: Any = None
        if coordinates:
            jcoordinates = [
                to_java_map(column_values, gateway=self.gateway)
                for column_values in coordinates
            ]
            jcoordinates_list = ListConverter().convert(
                jcoordinates, self.gateway._gateway_client
            )
        self._inside_transaction(
            lambda: cast(
                None,
                self.java_api.deleteOnStoreBranch(
                    table_name, scenario_name, jcoordinates_list
                ),
            ),
            scenario_name=scenario_name,
        )

    def get_table_dataframe(
        self,
        table_name: str,
        n: int,
        *,
        types: Mapping[str, DataType],
        keys: Iterable[str],
        scenario_name: str,
    ) -> pd.DataFrame:
        """Return the first given rows of the table as a pandas DataFrame."""
        dfrh = self._outside_transaction_api().dataFrameRowsAndHeaders(
            table_name, scenario_name, n
        )

        headers = to_python_list(dfrh.getContentHeader())
        rows = to_python_list(dfrh.getContentRows())

        java_types: Sequence[JavaType] = [
            data_type.java_type for data_type in types.values()
        ]

        data = [
            [
                cell.toString()
                if isinstance(cell, JavaObject)
                and not is_array_type(java_types[column_index])
                else cell
                for column_index, cell in enumerate(row)
            ]
            for row in rows
        ]

        dataframe = pd.DataFrame(
            data=data,
            columns=headers,
        )

        for name, data_type in types.items():
            dataframe[name] = convert_to_pandas(
                dataframe[name].apply(
                    lambda cell: None if cell is None else to_python_list(cell)
                )
                if is_array_type(data_type.java_type)
                else dataframe[name],
                java_type=data_type.java_type,
            )

        if keys:
            dataframe.set_index(keys, inplace=True)

        return dataframe

    def update_hierarchies_for_cube(
        self,
        cube_name: str,
        *,
        structure: Mapping[str, Mapping[str, Mapping[str, str]]],
    ) -> None:
        java_structure = to_java_map(
            {
                dimension_name: to_java_map(
                    {
                        hierarchy_name: to_java_map(levels, gateway=self.gateway)
                        for hierarchy_name, levels in hierarchy.items()
                    },
                    gateway=self.gateway,
                )
                for dimension_name, hierarchy in structure.items()
            },
            gateway=self.gateway,
        )
        self._outside_transaction_api().updateHierarchiesForCube(
            cube_name, java_structure
        )

    def create_analysis_hierarchy(
        self, name: str, *, cube_name: str, table_name: str, column_name: str
    ) -> None:
        """Create an analysis hierarchy from an existing table column."""
        self._outside_transaction_api().createAnalysisHierarchy(
            cube_name,
            name,
            table_name,
            column_name,
        )

    def create_date_hierarchy(
        self,
        *,
        cube_name: str,
        table_name: str,
        field: str,
        hierarchy_name: str,
        levels: Mapping[str, str],
    ) -> None:
        pair = self.gateway.jvm.com.quartetfs.fwk.impl.Pair
        converted = [pair(name, pattern) for (name, pattern) in levels.items()]
        levels_list = to_java_object_list(converted, gateway=self.gateway)
        self._outside_transaction_api().createDateHierarchy(
            cube_name,
            table_name,
            field,
            hierarchy_name,
            levels_list,
        )

    def update_hierarchy_coordinate(
        self,
        *,
        cube_name: str,
        hierarchy_coordinates: HierarchyCoordinates,
        new_dim: str,
        new_hier: str,
    ) -> None:
        """Change the coordinate of a hierarchy."""
        self._outside_transaction_api().updateHierarchyCoordinate(
            cube_name,
            coordinates_to_java_description(hierarchy_coordinates),
            f"{new_hier}@{new_dim}",
        )

    def update_hierarchy_slicing(
        self,
        *,
        cube_name: str,
        hierarchy_coordinates: HierarchyCoordinates,
        slicing: bool,
    ) -> None:
        """Update whether the hierarchy is slicing or not."""
        self._outside_transaction_api().setHierarchySlicing(
            cube_name,
            coordinates_to_java_description(hierarchy_coordinates),
            slicing,
        )

    def update_level_order(
        self,
        order: Order,
        *,
        cube_name: str,
        level_coordinates: LevelCoordinates,
    ) -> None:
        comparator_key = order._key if order is not None else None
        first_elements = (
            to_java_object_array(order.first_elements, gateway=self.gateway)
            if isinstance(order, CustomOrder)
            else None
        )

        self._outside_transaction_api().updateLevelComparator(
            cube_name,
            coordinates_to_java_description(level_coordinates),
            comparator_key,
            first_elements,
        )

    def drop_level(
        self, level_coordinates: LevelCoordinates, *, cube_name: str
    ) -> None:
        """Delete a level."""
        self._outside_transaction_api().deleteLevel(
            cube_name, coordinates_to_java_description(level_coordinates)
        )

    def drop_hierarchy(
        self, cube_name: str, hierarchy_coordinates: HierarchyCoordinates
    ) -> None:
        """Drop a hierarchy from the cube."""
        self._outside_transaction_api().dropHierarchy(
            cube_name, coordinates_to_java_description(hierarchy_coordinates)
        )

    def retrieve_cubes(self) -> List[Any]:
        """Retrieve the cubes of the session."""
        return to_python_list(self._outside_transaction_api().retrieveCubes())

    def retrieve_cube(self, cube_name: str) -> Any:
        """Retrieve a cube of the session using its name."""
        return self._outside_transaction_api().retrieveCube(cube_name)

    def retrieve_hierarchies(
        self,
        cube_name: str,
    ) -> Dict[HierarchyCoordinates, HierarchyArguments]:
        """Retrieve the hierarchies of the cube."""
        java_hierarchies = self._outside_transaction_api().retrieveHierarchies(
            cube_name
        )
        return {
            (hierarchy.dimension, hierarchy.name): hierarchy
            for hierarchy in _convert_java_hierarchies_to_python_hierarchies_arguments(
                to_python_dict(java_hierarchies).values()
            )
        }

    def retrieve_hierarchy(
        self, name: str, *, cube_name: str, dimension: Optional[str]
    ) -> List[HierarchyArguments]:
        """Retrieve a cube's hierarchy."""
        # Get the hierarchy from the java side.
        java_hierarchies = to_python_list(
            self._outside_transaction_api().retrieveHierarchy(
                cube_name, dimension, name
            )
        )

        return _convert_java_hierarchies_to_python_hierarchies_arguments(
            java_hierarchies
        )

    def retrieve_hierarchy_for_level(
        self,
        level_name: str,
        *,
        cube_name: str,
        dimension_name: Optional[str],
        hierarchy_name: Optional[str],
    ) -> List[HierarchyArguments]:
        """Retrieve the hierarchy containing a level with the given name."""
        java_hierarchies = to_python_list(
            self._outside_transaction_api().retrieveHierarchyForLevel(
                cube_name, dimension_name, hierarchy_name, level_name
            )
        )
        return _convert_java_hierarchies_to_python_hierarchies_arguments(
            java_hierarchies
        )

    def set_hierarchy_visibility(
        self,
        *,
        cube_name: str,
        dimension: Optional[str],
        name: str,
        visible: bool,
    ) -> None:
        self._outside_transaction_api().setHierarchyVisibility(
            cube_name, dimension, name, visible
        )

    def set_measure_folder(
        self, *, cube_name: str, measure_name: str, folder: Optional[str]
    ) -> None:
        """Set the folder of a measure."""
        self._outside_transaction_api().setMeasureFolder(
            cube_name, measure_name, folder
        )

    def set_measure_formatter(
        self, *, cube_name: str, measure_name: str, formatter: Optional[str]
    ) -> None:
        """Set the formatter of a measure."""
        self._outside_transaction_api().setMeasureFormatter(
            cube_name, measure_name, formatter
        )

    def set_visible(
        self, *, cube_name: str, measure_name: str, visible: Optional[bool]
    ) -> None:
        """Set the visibility of a measure."""
        self._outside_transaction_api().setMeasureVisibility(
            cube_name, measure_name, visible
        )

    def set_measure_description(
        self, *, cube_name: str, measure_name: str, description: Optional[str]
    ) -> None:
        """Set the measure description."""
        self._outside_transaction_api().setMeasureDescription(
            cube_name, measure_name, description
        )

    @keyword_only_dataclass
    @dataclass(frozen=True)
    class JavaMeasureDescription:
        """Description of a measure to build."""

        folder: str
        formatter: str
        visible: bool
        underlying_type: DataType
        description: Optional[str]

    def get_full_measures(
        self, cube_name: str
    ) -> Dict[str, JavaApi.JavaMeasureDescription]:
        """Retrieve the list of the cube's measures, including their required levels."""
        java_measures = self._outside_transaction_api().getFullMeasures(cube_name)
        measures = to_python_list(java_measures)
        final_measures: Dict[str, JavaApi.JavaMeasureDescription] = {}
        for measure in measures:
            final_measures[measure.getName()] = JavaApi.JavaMeasureDescription(
                folder=measure.getFolder(),
                formatter=measure.getFormatter(),
                visible=measure.isVisible(),
                underlying_type=parse_data_type(measure.getType()),
                description=measure.getDescription(),
            )
        return final_measures

    def get_measure(
        self, cube_name: str, measure_name: str
    ) -> JavaApi.JavaMeasureDescription:
        """Retrieve all the details about a measure defined in the cube."""
        measure = self._outside_transaction_api().getMeasure(cube_name, measure_name)
        return JavaApi.JavaMeasureDescription(
            folder=measure.getFolder(),
            formatter=measure.getFormatter(),
            visible=measure.isVisible(),
            underlying_type=parse_data_type(measure.getType()),
            description=measure.getDescription(),
        )

    def get_required_levels(self, cube_name: str, measure_name: str) -> List[str]:
        """Get the required levels of a measure."""
        return to_python_list(
            self._outside_transaction_api().getRequiredLevels(cube_name, measure_name)
        )

    @staticmethod
    def create_retrieval(jretr: Any) -> PivotRetrieval:
        """Convert Java retrieval to Python."""
        loc_str = ", ".join(
            [
                str(loc.getDimension())
                + "@"
                + str(loc.getHierarchy())
                + "@"
                + "\\".join(to_python_list(loc.getLevel()))
                + ": "
                + "\\".join(str(x) for x in to_python_list(loc.getPath()))
                for loc in to_python_list(jretr.getLocation())
            ]
        )
        timings = to_python_dict(jretr.getTimingInfo())
        return PivotRetrieval(
            id=jretr.getRetrievalId(),
            retrieval_type=jretr.getType(),
            location=loc_str,
            filter_id=jretr.getFilterId(),
            measures=to_python_list(jretr.getMeasures()),
            start_times=list(timings.get("startTime", [])),
            elapsed_times=list(timings.get("elapsedTime", [])),
            result_sizes=list(jretr.getResultSizes()),
            retrieval_filter=str(jretr.getFilterId()),
            partitioning=jretr.getPartitioning(),
            measures_provider=jretr.getMeasureProvider(),
        )

    @staticmethod
    def create_external_retrieval(jretr: Any) -> ExternalRetrieval:
        timings = to_python_dict(jretr.getTimingInfo())
        return ExternalRetrieval(
            id=jretr.getRetrievalId(),
            retrieval_type="ExternalDatastoreRetrieval",
            start_times=list(timings.get("startTime", [])),
            elapsed_times=list(timings.get("elapsedTime", [])),
            result_sizes=list(jretr.getResultSizes()),
            store=jretr.getStore(),
            joined_measures=list(jretr.getJoinedMeasure()),
            condition=jretr.getCondition(),
            fields=list(jretr.getFields()),
        )

    @staticmethod
    def create_query_plan(jplan: Any) -> QueryPlan:
        """Create a query plan."""
        jinfos = jplan.getPlanInfo()
        infos = {
            "ActivePivot": {
                "Type": jinfos.getPivotType(),
                "Id": jinfos.getPivotId(),
                "Branch": jinfos.getBranch(),
                "Epoch": jinfos.getEpoch(),
            },
            "Cube filters": {
                f.getId(): f.getDescription()
                for f in to_python_list(jplan.getQueryFilters())
            },
            "Continuous": jinfos.isContinuous(),
            "Range sharing": jinfos.getRangeSharing(),
            "Missed prefetches": jinfos.getMissedPrefetchBehavior(),
            "Cache": jinfos.getAggregatesCache(),
            "Global timings (ms)": to_python_dict(jinfos.getGlobalTimings()),
        }
        retrievals = [
            JavaApi.create_retrieval(retrieval)
            for retrieval in to_python_list(jplan.getAggregateRetrievals())
        ]
        dependencies = {
            key: to_python_list(item)
            for key, item in to_python_dict(jplan.getDependencies()).items()
        }
        external_retrievals = [
            JavaApi.create_external_retrieval(retrieval)
            for retrieval in to_python_list(jplan.getExternalRetrievals())
        ]
        external_dependencies = {
            key: to_python_list(item)
            for key, item in to_python_dict(jplan.getExternalDependencies()).items()
        }
        return QueryPlan(
            infos=infos,
            retrievals=retrievals,
            dependencies=dependencies,
            external_retrievals=external_retrievals,
            external_dependencies=external_dependencies,
        )

    def analyse_mdx(self, mdx: str, *, timeout: Union[int, timedelta]) -> QueryAnalysis:
        """Analyse an MDX query on a given cube."""
        if isinstance(timeout, int):
            deprecated(
                "Passing a timeout of type `int` is deprecated, pass a `datetime.timedelta` instead."
            )
            timeout = timedelta(seconds=timeout)

        jplans = to_python_list(
            self._outside_transaction_api().analyseMdx(
                mdx, ceil(timeout.total_seconds())
            )
        )
        plans = [
            JavaApi.create_query_plan(jplan)
            for jplan in jplans
            if jplan.getPlanInfo().getClass().getSimpleName() == "PlanInfoData"
        ]
        return QueryAnalysis(query_plans=plans)

    def copy_measure(
        self,
        copied_measure_name: str,
        new_name: str,
        *,
        cube_name: str,
    ) -> None:
        """Copy a measure."""
        self._outside_transaction_api().copyMeasure(
            cube_name, copied_measure_name, new_name
        )

    def create_measure(  # pylint: disable=too-many-positional-parameters
        self,
        cube_name: str,
        measure_name: Optional[str],
        measure_plugin_key: str,
        *args: Any,
    ) -> str:
        """Create a new measure with by giving its constructor arguments."""
        return cast(
            str,
            self._outside_transaction_api().createMeasure(
                cube_name,
                measure_name,
                measure_plugin_key,
                to_java_object_array(
                    [self.levels_to_descriptions(arg) for arg in args],
                    gateway=self.gateway,
                ),
            ),
        )

    def register_aggregation_function(
        self,
        *,
        additional_imports: Iterable[str],
        additional_methods: Iterable[str],
        contribute_source_code: str,
        decontribute_source_code: Optional[str],
        merge_source_code: str,
        terminate_source_code: str,
        buffer_types: Iterable[JavaType],
        output_type: JavaType,
        plugin_key: str,
    ) -> None:
        """Register a new user defined aggregation function."""
        java_output_type = self._get_java_object_from_java_type(output_type)
        java_buffer_types = self._create_java_types_list_from_javatype(buffer_types)
        java_imports = ListConverter().convert(
            additional_imports, self.gateway._gateway_client
        )
        java_methods = ListConverter().convert(
            additional_methods, self.gateway._gateway_client
        )
        self._outside_transaction_api().registerUserDefinedAggregateFunction(
            contribute_source_code,
            decontribute_source_code,
            merge_source_code,
            terminate_source_code,
            java_buffer_types,
            java_output_type,
            plugin_key,
            java_imports,
            java_methods,
        )

    def levels_to_descriptions(self, arg: Any) -> Any:
        """Recursively convert levels and hierarchies to their java descriptions."""
        if isinstance(arg, tuple):
            return to_java_object_array(
                tuple(self.levels_to_descriptions(e) for e in arg),
                gateway=self.gateway,
            )
        if isinstance(arg, Mapping):
            return to_java_map(
                {
                    self.levels_to_descriptions(k): self.levels_to_descriptions(v)
                    for k, v in arg.items()
                },
                gateway=self.gateway,
            )
        if isinstance(arg, (list, set)):
            return ListConverter().convert(
                [self.levels_to_descriptions(e) for e in arg],
                self.gateway._gateway_client,
            )
        return arg

    def aggregated_measure(
        self,
        *,
        cube_name: str,
        measure_name: Optional[str],
        table_name: str,
        column_name: str,
        agg_function: str,
        required_levels_coordinates: Iterable[LevelCoordinates],
    ) -> str:
        """Create a new aggregated measure and return its name."""
        java_required_levels = to_java_string_array(
            [
                coordinates_to_java_description(level_coordinates)
                for level_coordinates in required_levels_coordinates
            ],
            gateway=self.gateway,
        )
        return cast(
            str,
            self._outside_transaction_api().aggregatedMeasure(
                cube_name,
                measure_name,
                table_name,
                column_name,
                agg_function,
                java_required_levels,
            ),
        )

    def value_measure(
        self,
        *,
        cube_name: str,
        measure_name: Optional[str],
        table_name: str,
        column_name: str,
        column_type: DataType,
        required_levels_coordinates: Optional[Iterable[LevelCoordinates]],
    ) -> str:
        """Create a new table value measure and return its name."""
        java_required_levels = (
            to_java_string_array(
                [
                    coordinates_to_java_description(level_coordinates)
                    for level_coordinates in required_levels_coordinates
                ],
                gateway=self.gateway,
            )
            if required_levels_coordinates is not None
            else None
        )
        # pylint: disable=invalid-name
        JavaColumnType = self.gateway.jvm.io.atoti.loading.impl.TypeImpl
        # pylint: enable=invalid-name
        java_type = JavaColumnType(column_type.java_type, column_type.nullable)
        return cast(
            str,
            self._outside_transaction_api().createValueMeasure(
                cube_name,
                measure_name,
                table_name,
                column_name,
                java_type,
                java_required_levels,
            ),
        )

    def delete_measure(self, *, cube_name: str, measure_name: str) -> bool:
        """Delete a measure and return ``True`` if the measure has been found and deleted."""
        return cast(
            bool, self._outside_transaction_api().deleteMeasure(cube_name, measure_name)
        )

    def create_parameter_simulation(
        self,
        *,
        cube_name: str,
        simulation_name: str,
        measures: Mapping[str, Optional[Union[float, int]]],
        levels_coordinates: Iterable[LevelCoordinates],
        base_scenario_name: str,
    ) -> str:
        """Create a simulation in the cube and return the name of its backing table."""
        jmeasures = to_java_map(measures, gateway=self.gateway)
        jlevels = to_java_string_array(
            [
                coordinates_to_java_description(level_coordinates)
                for level_coordinates in levels_coordinates
            ],
            gateway=self.gateway,
        )
        return cast(
            str,
            self._outside_transaction_api().createParameterSimulation(
                cube_name, simulation_name, jlevels, base_scenario_name, jmeasures
            ),
        )

    def _inside_transaction(
        self,
        callback: Callable[[], None],
        *,
        scenario_name: str,
        source_key: Optional[str] = None,
    ) -> None:
        if is_inside_transaction() or source_key in _REALTIME_SOURCE_KEYS:
            callback()
        else:
            with Transaction(
                scenario_name,
                start=self.start_transaction,
                end=self.end_transaction,
                is_user_initiated=False,
            ):
                callback()

    def block_until_widget_loaded(self, widget_id: str) -> bool:
        """Block until the widget is loaded or the JupyterLab extension is found unresponsive."""
        return cast(bool, self.java_api.blockUntilWidgetLoaded(widget_id))

    def get_shared_context_values(self, cube_name: str) -> Dict[str, str]:
        return to_python_dict(
            self._outside_transaction_api().getCubeShareContextValues(cube_name)
        )

    def set_shared_context_value(self, *, cube_name: str, key: str, value: str) -> None:
        self._outside_transaction_api().setCubeSharedContextValue(cube_name, key, value)

    def get_user(self, *args: Any, **kwargs: Any) -> Any:  # pylint: disable=no-self-use
        raise MissingPluginError("plus")

    def get_users(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def create_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_individual_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_individual_roles_for_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def upsert_individual_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def delete_individual_roles_for_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_default_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def set_default_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def change_user_password(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def delete_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")
