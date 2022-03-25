from __future__ import annotations

import logging as _logging
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from types import TracebackType
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Final,
    Iterable,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)
from warnings import warn

import pandas as pd
import pyarrow as pa
from atoti_core import (
    BASE_SCENARIO_NAME,
    EMPTY_MAPPING,
    SESSION_DOC,
    MissingPluginError,
    PathLike,
    deprecated,
    doc,
    keyword_only_dataclass,
)
from atoti_query import Auth, ClientCertificate, QuerySession
from numpy.typing import NDArray

from ._arrow_utils import get_data_types_from_arrow
from ._delegate_mutable_mapping import DelegateMutableMapping
from ._docs_utils import (
    CLIENT_SIDE_ENCRYPTION_DOC,
    CSV_KWARGS,
    PARQUET_KWARGS,
    TABLE_CREATION_KWARGS,
)
from ._file_utils import split_path_and_pattern
from ._local_session import LocalSession
from ._pandas_utils import pandas_to_arrow
from ._path_utils import stem_path
from ._runtime_type_checking_utils import typecheck
from ._sources.csv import CsvDataSource
from ._sources.parquet import ParquetDataSource
from ._spark_utils import write_spark_to_parquet
from ._transaction import Transaction
from .client_side_encryption_config import ClientSideEncryptionConfig
from .config import (
    BasicAuthenticationConfig,
    BrandingConfig,
    ClientCertificateConfig,
    HttpsConfig,
    I18nConfig,
    JwtConfig,
    KerberosConfig,
    LdapConfig,
    LoggingConfig,
    OidcConfig,
    UserContentStorageConfig,
)
from .config._session_config import SessionConfig, create_authentication_config
from .config.user_content_storage_config import (
    _create_user_content_storage_config_from_path_or_url,
)
from .cube import Cube
from .cubes import Cubes
from .experimental._distributed.session import DistributedSession
from .table import Table, _get_client_side_encryption
from .tables import Tables
from .type import DataType

if TYPE_CHECKING:
    # PySpark is only imported for type checking as we don't want it as a dependency
    from pyspark.sql import (  # pylint: disable=undeclared-dependency
        DataFrame as SparkDataFrame,
    )

_CubeCreationMode = Literal[  # pylint: disable=invalid-name
    "auto", "manual", "no_measures"
]


def _infer_table_name(
    *, path: PathLike, pattern: Optional[str], table_name: Optional[str]
) -> str:
    """Infer the name of a table given the path and table_name parameters."""
    if pattern is not None and table_name is None:
        raise ValueError(
            "The table_name parameter is required when the path argument is a glob pattern."
        )
    return table_name or stem_path(path).capitalize()


@keyword_only_dataclass
@dataclass(frozen=True)
class _SessionPrivateParameters:
    config: Optional[SessionConfig] = None


@keyword_only_dataclass
@dataclass(frozen=True)
class _CreateTablePrivateParameters:
    is_parameter_table: bool = False


class Session(LocalSession[Cubes]):
    """Holds a connection to the Java gateway."""

    @doc(**SESSION_DOC)
    def __init__(
        self,
        *,
        name: Optional[str] = "Unnamed",
        app_extensions: Optional[Mapping[str, Union[str, Path]]] = None,
        authentication: Optional[
            Union[BasicAuthenticationConfig, KerberosConfig, LdapConfig, OidcConfig]
        ] = None,
        branding: Optional[BrandingConfig] = None,
        certificate_authority: Optional[Union[str, Path]] = None,
        client_certificate: Optional[ClientCertificateConfig] = None,
        extra_jars: Iterable[Union[str, Path]] = (),
        https: Optional[HttpsConfig] = None,
        i18n: Optional[I18nConfig] = None,
        java_options: Iterable[str] = (),
        jwt: Optional[JwtConfig] = None,
        logging: Optional[LoggingConfig] = None,  # pylint: disable=W0621
        port: int = 0,
        same_site: Optional[Literal["none", "strict"]] = None,
        user_content_storage: Optional[
            Union[
                Path,
                str,
                UserContentStorageConfig,
            ]
        ] = None,
        **kwargs: Any,
    ):
        """Create a session.

        Args:

            name: The name of the session.

                For a better prototyping experience in notebooks, creating a session with the same name as an already running session will close the latter one.
                Pass ``None`` to opt out of this behavior.
            app_extensions: Mapping from the name of an extension (i.e. :guilabel:`name` property in their :guilabel:`package.json`) to the path of its :guilabel:`dist` directory.

                Note:
                    This requires the :mod:`atoti-plus <atoti_plus>` plugin.

                Extensions can enhance the built-in app in many ways such as:

                * Adding new type of widgets.
                * Attaching custom menu items or titlebar buttons to a set of widgets.
                * Providing other React contexts to the components rendered by the app.

                The :download:`app extension template <../../app-extension-template/extension.zip>` can be used as a starting point.
            authentication: The configuration to enable authentication on the session.

                Note:
                    This requires the :mod:`atoti-plus <atoti_plus>` plugin.

                Users and roles are configured using :attr:`atoti.Session.security`.
            branding: The config to customize some elements of the UI to change its appearance.
            {certificate_authority}
            client_certificate: The config to enable client certificate based authentication on the session.
            extra_jars: The paths to the JARs to add to the classpath of the Java process when starting the session.
            https: The config providing certificates to enable HTTPS on the session.
            i18n: The config to internationalize the session.
            java_options: The additional options to pass when starting the Java process (e.g. for optimization or debugging purposes).

                In particular, the ``-Xmx`` option can be set to increase the amount of RAM that the session can use.

                If this option is not specified, the JVM default memory setting is used which is 25% of the machine memory.
            jwt: The config to set the key pair used to validate JWTs when authenticating with the session.
            logging: The config describing how to handle session logs.
            port: The port on which the session will be exposed.

                Defaults to a random available port.
            same_site: The value to use for the *SameSite* attribute of the HTTP cookie sent by the session when *authentication* is configured.

                Note:
                    This requires the :mod:`atoti-plus <atoti_plus>` plugin.

                See https://web.dev/samesite-cookies-explained for more information.

                Setting it to ``none`` requires the session to be served through HTTPS.

                Defaults to ``lax``.
            user_content_storage: The location of the database where the user content will be stored.
                The user content is what is not part of the data sources, such as the dashboards, widgets, and filters saved in the application.
                If a path to a directory is given, it will be created if needed.
                When ``None``, the user content is kept in memory and is thus lost when the session is closed.
        """
        private_parameters = _SessionPrivateParameters(**kwargs)

        config = private_parameters.config or SessionConfig(
            app_extensions=app_extensions or None,
            authentication=create_authentication_config(authentication)
            if authentication
            else None,
            branding=branding,
            client_certificate=client_certificate,
            extra_jars=extra_jars,
            https=https,
            i18n=i18n,
            java_options=java_options,
            jwt=jwt,
            logging=logging,  # pylint: disable=W0621
            port=port,
            same_site=same_site,
            user_content_storage=_create_user_content_storage_config_from_path_or_url(
                user_content_storage
            )
            if isinstance(user_content_storage, (Path, str))
            else user_content_storage,
        )

        if name is not None:
            _sessions._clear_duplicate_sessions(name)

        super().__init__(
            name=name,
            config=config,
            distributed=False,
            certificate_authority=certificate_authority,
        )

        self._warn_if_license_about_to_expire()
        # https://github.com/python/mypy/issues/12183
        self._cubes = Cubes(
            _delete_cube=self._java_api.delete_cube,
            _retrieve_cube=self._retrieve_cube,  # type: ignore[arg-type]
            _retrieve_cubes=self._retrieve_cubes,  # type: ignore[arg-type]
        )
        self._tables = Tables(java_api=self._java_api)

        if name is not None:
            _sessions._sessions[name] = self

    def __enter__(self) -> Session:
        """Enter this session's context manager.

        Returns:
            self: to assign it to the "as" keyword.

        """
        return self

    @property
    def cubes(self) -> Cubes:
        """Cubes of the session."""
        return self._cubes

    @property
    def tables(self) -> Tables:  # noqa: D401
        """Tables of the session."""
        return self._tables

    @doc(
        **TABLE_CREATION_KWARGS,
        # Declare the types here because blackdoc and doctest conflict when inlining it in the docstring.
        data_types="""{"Date": tt.type.LOCAL_DATE, "Product": tt.type.STRING, "Quantity": tt.type.NULLABLE_DOUBLE}""",
    )
    def create_table(
        self,
        name: str,
        *,
        types: Mapping[str, DataType],
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        hierarchized_columns: Optional[Iterable[str]] = None,
        **kwargs: Any,
    ) -> Table:
        """Create a table from a schema.

        Args:
            name: The name of the table to create.
            types: Types for all columns of the table.
                This defines the columns which will be expected in any future data loaded into the table.
            {keys}
            {partitioning}
            {hierarchized_columns}

        Example:

            >>> from datetime import date
            >>> table = session.create_table(
            ...     "Product",
            ...     types={data_types},
            ...     keys=["Date"],
            ... )
            >>> table.head()
            Empty DataFrame
            Columns: [Product, Quantity]
            Index: []
            >>> table.append((date(2021, 5, 19), "TV", 15.0))
            >>> table.head()
                       Product  Quantity
            Date
            2021-05-19      TV      15.0

        """
        private_parameters = _CreateTablePrivateParameters(**kwargs)
        self._java_api.create_table(
            name,
            types=types,
            keys=keys,
            partitioning=partitioning,
            hierarchized_columns=hierarchized_columns,
            is_parameter_table=private_parameters.is_parameter_table,
        )
        return Table(_name=name, _java_api=self._java_api)

    @doc(**TABLE_CREATION_KWARGS)
    def read_pandas(
        self,
        dataframe: pd.DataFrame,
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        hierarchized_columns: Optional[Iterable[str]] = None,
        **kwargs: Any,
    ) -> Table:
        """Read a pandas DataFrame into a table.

        All the named indices of the DataFrame are included into the table.
        Multilevel columns are flattened into a single string name.

        Args:
            dataframe: The DataFrame to load.
            {table_name}
            {keys}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from pandas dtypes.
            {hierarchized_columns}

        Returns:
            The created table holding the content of the DataFrame.
        """
        arrow_table = pandas_to_arrow(dataframe, types=types)
        return self._read_arrow(
            arrow_table,
            table_name=table_name,
            keys=keys,
            partitioning=partitioning,
            types=types,
            hierarchized_columns=hierarchized_columns,
            **kwargs,
        )

    def _read_arrow(
        self,
        arrow_table: pa.Table,  # type: ignore
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        hierarchized_columns: Optional[Iterable[str]] = None,
        **kwargs: Any,
    ) -> Table:
        types_from_arrow = get_data_types_from_arrow(
            arrow_table,
            keys=keys,
        )
        types = {**types_from_arrow, **types} if types is not None else types_from_arrow
        table = self.create_table(
            table_name,
            types=types,
            keys=keys,
            partitioning=partitioning,
            hierarchized_columns=hierarchized_columns,
            **kwargs,
        )
        table._load_arrow(arrow_table)
        return table

    @doc(**TABLE_CREATION_KWARGS)
    @typecheck(ignored_params=["dataframe"])
    def read_spark(
        self,
        dataframe: SparkDataFrame,
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        hierarchized_columns: Optional[Iterable[str]] = None,
    ) -> Table:
        """Read a Spark DataFrame into a table.

        Args:
            dataframe: The DataFrame to load.
            {table_name}
            {keys}
            {partitioning}
            {hierarchized_columns}

        Returns:
            The created table holding the content of the DataFrame.
        """
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "spark"
            write_spark_to_parquet(dataframe, directory=path)
            return self.read_parquet(
                path=path,
                keys=keys,
                table_name=table_name,
                partitioning=partitioning,
                hierarchized_columns=hierarchized_columns,
            )

    @doc(**{**TABLE_CREATION_KWARGS, **CSV_KWARGS, **CLIENT_SIDE_ENCRYPTION_DOC})
    def read_csv(
        self,
        path: PathLike,
        *,
        keys: Iterable[str] = (),
        table_name: Optional[str] = None,
        separator: Optional[str] = None,
        encoding: str = "utf-8",
        process_quotes: Optional[bool] = None,
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        columns: Mapping[str, str] = EMPTY_MAPPING,
        array_separator: Optional[str] = None,
        hierarchized_columns: Optional[Iterable[str]] = None,
        date_patterns: Mapping[str, str] = EMPTY_MAPPING,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> Table:
        """Read a CSV file into a table.

        Args:
            {path}
            {keys}
            table_name: The name of the table to create.
                Required when *path* is a glob pattern.
                Otherwise, defaults to the final component of the *path* argument.
            {separator}
            {encoding}
            {process_quotes}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from the first 1,000 lines.
            {columns}
            {array_separator}
            {hierarchized_columns}
            {date_patterns}
            {client_side_encryption}

        Returns:
            The created table holding the content of the CSV file(s).
        """
        full_path = path
        path, pattern = split_path_and_pattern(path, ".csv")

        table_name = _infer_table_name(
            path=path, pattern=pattern, table_name=table_name
        )

        csv_file_format = CsvDataSource(
            _load_data_into_table=self._java_api.load_data_into_table,
            _discover_csv_file_format=self._java_api.discover_csv_file_format,
        ).discover_file_format(
            path=path,
            keys=keys,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            pattern=pattern,
            date_patterns=date_patterns,
            client_side_encryption=_get_client_side_encryption(
                client_side_encryption, java_api=self._java_api
            ),
            columns=columns,
        )
        types = (
            {**csv_file_format.types, **types}
            if types is not None
            else csv_file_format.types
        )
        process_quotes = (
            process_quotes
            if process_quotes is not None
            else csv_file_format.process_quotes
        )
        separator = separator if separator is not None else csv_file_format.separator
        date_patterns = (
            {**csv_file_format.date_patterns, **date_patterns}
            if date_patterns is not None
            else csv_file_format.date_patterns
        )

        table = self.create_table(
            table_name,
            types=types,
            keys=keys,
            partitioning=partitioning,
            hierarchized_columns=hierarchized_columns,
        )
        table.load_csv(
            full_path,
            columns=columns,
            separator=separator,
            encoding=encoding,
            process_quotes=process_quotes,
            array_separator=array_separator,
            date_patterns=date_patterns,
            client_side_encryption=client_side_encryption,
        )
        return table

    @doc(**{**TABLE_CREATION_KWARGS, **PARQUET_KWARGS, **CLIENT_SIDE_ENCRYPTION_DOC})
    def read_parquet(
        self,
        path: PathLike,
        *,
        keys: Iterable[str] = (),
        columns: Mapping[str, str] = EMPTY_MAPPING,
        table_name: Optional[str] = None,
        partitioning: Optional[str] = None,
        hierarchized_columns: Optional[Iterable[str]] = None,
        client_side_encryption: Optional[ClientSideEncryptionConfig] = None,
    ) -> Table:
        """Read a Parquet file into a table.

        Args:
            {path}
            {keys}
            {columns}
            table_name: The name of the table to create.
                Required when *path* is a glob pattern.
                Otherwise, defaults to the final component of the *path* argument.
            {partitioning}
            {hierarchized_columns}
            {client_side_encryption}

        Returns:
            The created table holding the content of the Parquet file(s).
        """
        full_path = path
        path, pattern = split_path_and_pattern(path, ".parquet")
        table_name = _infer_table_name(
            path=path, pattern=pattern, table_name=table_name
        )

        inferred_types = ParquetDataSource(
            _load_data_into_table=self._java_api.load_data_into_table,
            _infer_types=self._java_api.infer_table_types_from_source,
        ).infer_parquet_types(
            path=path,
            keys=keys,
            pattern=pattern,
            client_side_encryption=_get_client_side_encryption(
                client_side_encryption, java_api=self._java_api
            ),
            columns=columns,
        )

        table = self.create_table(
            table_name,
            types=inferred_types,
            keys=keys,
            partitioning=partitioning,
            hierarchized_columns=hierarchized_columns,
        )
        table.load_parquet(
            full_path, client_side_encryption=client_side_encryption, columns=columns
        )
        return table

    @doc(**TABLE_CREATION_KWARGS)
    def read_numpy(
        self,
        array: NDArray[Any],
        *,
        columns: Sequence[str],
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        hierarchized_columns: Optional[Iterable[str]] = None,
    ) -> Table:
        """Read a NumPy 2D array into a new table.

        Args:
            array: The NumPy 2D ndarray to read the data from.
            columns: The names to use for the table's columns.
                They must be in the same order as the values in the NumPy array.
            {table_name}
            {keys}
            {partitioning}
            types: Types for some or all columns of the table.
                Types for non specified columns will be inferred from numpy data types.
            {hierarchized_columns}

        Returns:
            The created table holding the content of the array.
        """
        dataframe = pd.DataFrame(array, columns=columns)
        return self.read_pandas(
            dataframe,
            table_name=table_name,
            keys=keys,
            partitioning=partitioning,
            types=types,
            hierarchized_columns=hierarchized_columns,
        )

    def read_sql(  # pylint: disable=no-self-use
        self,
        query: str,
        *,
        url: str,
        table_name: str,
        driver: Optional[str] = None,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        hierarchized_columns: Optional[Iterable[str]] = None,
    ) -> Table:
        raise MissingPluginError("sql")

    def start_transaction(self, scenario_name: str = BASE_SCENARIO_NAME) -> Transaction:
        """Start a transaction to batch several table operations.

        * It is more efficient than doing each table operation one after the other.
        * It avoids possibly incorrect intermediate states (e.g. if loading some new data requires dropping existing rows first).

        .. note::
            Some operations are not allowed during a transaction:

            * Long-running operations such as :meth:`atoti.Table.load_kafka`.
            * Operations changing the structure of the session's tables such as :meth:`atoti.Table.join` or :meth:`atoti.Session.read_parquet`.
            * Operations not related to data loading or dropping such as defining a new measure.
            * Operations on parameter tables created from :meth:`atoti.Cube.create_parameter_hierarchy_from_members` and :meth:`atoti.Cube.create_parameter_simulation`.
            * Operations on other source scenarios than the one the transaction is started on.

        Args:
            scenario_name: The name of the source scenario impacted by all the table operations inside the transaction.

        Example:
            >>> df = pd.DataFrame(
            ...     columns=["City", "Price"],
            ...     data=[
            ...         ("Berlin", 150.0),
            ...         ("London", 240.0),
            ...         ("New York", 270.0),
            ...         ("Paris", 200.0),
            ...     ],
            ... )
            >>> table = session.read_pandas(
            ...     df, keys=["City"], table_name="start_transaction example"
            ... )
            >>> cube = session.create_cube(table)
            >>> extra_df = pd.DataFrame(
            ...     columns=["City", "Price"],
            ...     data=[
            ...         ("Singapore", 250.0),
            ...     ],
            ... )
            >>> with session.start_transaction():
            ...     table += ("New York", 100.0)
            ...     table.drop({"City": "Paris"})
            ...     table.load_pandas(extra_df)
            ...
            >>> table.head().sort_index()
                       Price
            City
            Berlin     150.0
            London     240.0
            New York   100.0
            Singapore  250.0

        """
        return Transaction(
            scenario_name,
            start=self._java_api.start_transaction,
            end=self._java_api.end_transaction,
        )

    def create_cube(
        self,
        base_table: Table,
        name: Optional[str] = None,
        *,
        mode: _CubeCreationMode = "auto",
    ) -> Cube:
        """Create a cube based on the passed table.

        Args:
            base_table: The base table of the cube.
            name: The name of the created cube.
                Defaults to the name of the base table.
            mode: The cube creation mode:

                * ``auto``: Creates hierarchies for every key column or non-numeric column of the table, and measures for every numeric column.
                * ``manual``: Does not create any hierarchy or measure (except from the count).
                * ``no_measures``: Creates the hierarchies like ``auto`` but does not create any measures.

                For tables with ``hierarchized_columns`` specified, these will be converted into
                hierarchies regardless of the cube creation mode.

        Example:
            >>> table = session.create_table(
            ...     "Table",
            ...     types={"id": tt.type.STRING, "value": tt.type.NULLABLE_DOUBLE},
            ... )
            >>> cube_auto = session.create_cube(table)
            >>> sorted(cube_auto.measures)
            ['contributors.COUNT', 'update.TIMESTAMP', 'value.MEAN', 'value.SUM']
            >>> list(cube_auto.hierarchies)
            [('Table', 'id')]
            >>> cube_no_measures = session.create_cube(table, mode="no_measures")
            >>> sorted(cube_no_measures.measures)
            ['contributors.COUNT', 'update.TIMESTAMP']
            >>> list(cube_no_measures.hierarchies)
            [('Table', 'id')]
            >>> cube_manual = session.create_cube(table, mode="manual")
            >>> sorted(cube_manual.measures)
            ['contributors.COUNT', 'update.TIMESTAMP']
            >>> list(cube_manual.hierarchies)
            []

        See Also:
            Hierarchies and measures created by a :meth:`~atoti.Table.join`.
        """
        if name is None:
            name = base_table.name

        self._java_api.create_cube_from_table(
            table_name=base_table.name, cube_name=name, creation_mode=mode.upper()
        )
        self._java_api.refresh()
        Cube(
            java_api=self._java_api,
            name=name,
            base_table=base_table,
            session_name=self.name,
            query_mdx=self.query_mdx,
            execute_gaq=self._create_query_session()._execute_gaq,
            read_pandas=self.read_pandas,
        )

        return self.cubes[name]

    def create_scenario(self, name: str, *, origin: str = BASE_SCENARIO_NAME) -> None:
        """Create a new source scenario.

        Args:
            name: The name of the scenario.
            origin: The scenario to fork.
        """
        self._java_api.create_scenario(name, origin)

    def delete_scenario(self, scenario: str) -> None:
        """Delete the source scenario with the provided name if it exists."""
        if scenario == BASE_SCENARIO_NAME:
            raise ValueError("Cannot delete the base scenario")
        self._java_api.delete_scenario(scenario)

    @property
    def scenarios(self) -> Sequence[str]:
        """Collection of source scenarios of the session."""
        return self._java_api.get_scenarios()

    def export_translations_template(self, path: PathLike) -> None:
        """Export a template containing all translatable values in the session's cubes.

        Args:
            path: The path at which to write the template.
        """
        self._java_api.export_i18n_template(path)

    def _retrieve_cube(self, cube_name: str) -> Cube:
        java_cube = self._java_api.retrieve_cube(cube_name)
        return Cube(
            java_api=self._java_api,
            name=java_cube.getName(),
            base_table=self.tables[java_cube.getStoreName()],
            session_name=self.name,
            query_mdx=self.query_mdx,
            execute_gaq=self._create_query_session()._execute_gaq,
            read_pandas=self.read_pandas,
        )

    def _retrieve_cubes(self) -> Dict[str, Cube]:
        return {
            java_cube.getName(): Cube(
                java_api=self._java_api,
                name=java_cube.getName(),
                base_table=self.tables[java_cube.getStoreName()],
                session_name=self.name,
                query_mdx=self.query_mdx,
                execute_gaq=self._create_query_session()._execute_gaq,
                read_pandas=self.read_pandas,
            )
            for java_cube in self._java_api.retrieve_cubes()
        }

    def _warn_if_license_about_to_expire(
        self, *, minimum_remaining_time: timedelta = timedelta(days=7)
    ) -> None:
        remaining_time = self._java_api.license_end_date - datetime.now()
        if remaining_time < minimum_remaining_time:
            required_action = (
                "update to atoti's latest version or upgrade to Atoti+"
                if self._java_api.is_community_license
                else "contact ActiveViam to get a new license"
            )
            warn(
                f"The license is about to expire, {required_action} in the coming {remaining_time.days} days.",
                category=FutureWarning,
            )


_Session = Union[Session, DistributedSession, QuerySession]


@keyword_only_dataclass
@dataclass(frozen=True)
class _Sessions(DelegateMutableMapping[str, _Session]):

    _sessions: Dict[str, _Session] = field(default_factory=dict, init=False)

    def _get_underlying(self) -> Dict[str, _Session]:
        """Get the underlying mapping."""
        self._remove_closed_sessions()
        return self._sessions

    @typecheck
    def _open_query_session(
        self,
        url: str,
        name: Optional[str] = None,
        *,
        auth: Optional[Auth] = None,
        client_certificate: Optional[ClientCertificate] = None,
    ) -> QuerySession:
        deprecated(
            "Opening query sessions like this is deprecated, use `atoti_query.QuerySession()` directly instead."
        )
        self._clear_duplicate_sessions(name or url)
        query_session = QuerySession(
            url, auth=auth, name=name, client_certificate=client_certificate
        )
        self[name or url] = query_session
        return query_session

    def _clear_duplicate_sessions(self, name: str) -> None:
        self._remove_closed_sessions()
        if name in self._sessions:
            _logging.getLogger("atoti.session").warning(
                """Deleting existing "%s" session to create the new one.""", name
            )
            del self[name]

    def __enter__(self) -> _Sessions:
        return self

    def __exit__(  # pylint: disable=too-many-positional-parameters
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.close()

    def close(self) -> None:
        """Close all the opened sessions."""
        for session in self._sessions.values():
            if isinstance(session, Session):
                session.close()

    def _remove_closed_sessions(self) -> None:
        sessions_to_remove = [
            session
            for session in self._sessions.values()
            if isinstance(session, Session) and session.closed
        ]
        for session in sessions_to_remove:
            session_name = session.name

            if session_name is None:
                raise ValueError(
                    "Sessions in this mutable mapping are expected to have a name."
                )

            del self._sessions[session_name]

    def _update(self, other: Mapping[str, _Session]) -> None:
        self._remove_closed_sessions()
        for session_name, session in other.items():
            if session_name in self._sessions:
                del self[session_name]
            self._sessions[session_name] = session

    def __getitem__(self, key: str) -> _Session:
        """Get a session."""
        self._remove_closed_sessions()
        return self._sessions[key]

    def __delitem__(self, key: str) -> None:
        """Remove a session.

        This method also stops the Java session, destroying all Java objects attached to it.
        """
        self._remove_closed_sessions()
        if key in self._sessions:
            session = self._sessions[key]
            if isinstance(session, Session):
                session.close()
            del self._sessions[key]


# pylint: disable=invalid-name
_sessions: Final = _Sessions()
