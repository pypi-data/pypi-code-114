import logging
from functools import lru_cache

import pandas as pd
import snowflake.connector
from .base import ColumnInfo, BaseAdapter

logger = logging.getLogger(__name__)


class SnowflakeAdapter(BaseAdapter):
    name = "snowflake"

    def __init__(self, user, password, account, warehouse, role, database):
        self.user = user
        self._password = password
        self.account = account
        self.warehouse = warehouse
        self.role = role
        self.database = database
        self._conn = None

    @classmethod
    def from_dbt_profile(cls, profile: dict, database=None):
        database = database or profile["database"]
        return cls(
            user=profile["user"],
            password=profile["password"],
            account=profile["account"],
            warehouse=profile["warehouse"],
            role=profile["role"],
            database=database,
        )

    @property
    def _connection(self):
        if not self._conn:
            self._conn = snowflake.connector.connect(
                user=self.user,
                password=self._password,
                account=self.account,
                warehouse=self.warehouse,
                role=self.role,
                database=self.database,
            )
        return self._conn

    def execute(self, query, **kwargs):
        cursor = self._connection.cursor(snowflake.connector.DictCursor)
        try:
            cursor.execute(query, **kwargs)
            return cursor.fetchall()
        finally:
            cursor.close()

    def execute_pandas(self, query, **kwargs) -> pd.DataFrame:
        cursor = self._connection.cursor()
        try:
            cursor.execute(query, **kwargs)
            return cursor.fetch_pandas_all()
        finally:
            cursor.close()

    @lru_cache()
    def get_column_metadata_df(self, dataset) -> pd.DataFrame:
        query = f"select * from information_schema.columns where table_schema = '{dataset.upper()}';"
        dataframe = self.execute_pandas(query)
        dataframe.columns = dataframe.columns.str.lower()
        dataframe = dataframe.loc[
            dataframe["table_schema"].apply(lambda x: (x.lower() != "information_schema" and not x.startswith("_")))
            & dataframe["table_name"].apply(lambda x: not x.startswith("_")),
            :,
        ]
        dataframe.sort_values(by=["table_schema", "table_name", "ordinal_position"], inplace=True)
        return dataframe

    def list_datasets(self):
        query = "select distinct schema_name from information_schema.schemata;"
        meta_df = self.execute_pandas(query)
        for schema in meta_df["SCHEMA_NAME"].unique():
            yield schema.lower()

    def list_tables(self, dataset):
        meta_df = self.get_column_metadata_df(dataset)
        meta_df = meta_df.loc[meta_df["table_schema"] == dataset.upper(), :]
        for table in meta_df["table_name"].unique():
            yield table.lower()

    def list_columns(self, dataset, table):
        meta_df = self.get_column_metadata_df(dataset)
        meta_df = meta_df.loc[
            (meta_df["table_schema"] == dataset.upper()) & (meta_df["table_name"] == table.upper()), :
        ]
        rows = meta_df.to_dict(orient="records")
        for row in rows:
            yield ColumnInfo(
                database=self.database,
                schema=dataset,
                table=table,
                name=row["column_name"].lower(),
                position=row["ordinal_position"],
                dtype=row["data_type"],
                nullable=True if row["is_nullable"] == "YES" else False,
                extra=row,
            )

    # def __del__(self):
    #     if self._conn:
    #         print("Closing Snowflake connection")
    #         self._conn.close()
