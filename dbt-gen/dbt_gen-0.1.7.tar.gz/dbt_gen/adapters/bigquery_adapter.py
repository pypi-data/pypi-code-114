from functools import lru_cache

from google.cloud import bigquery
import pandas as pd
from typing import Generator

from .base import ColumnInfo, BaseAdapter


class BigQueryAdapter(BaseAdapter):
    name = "bigquery"

    def __init__(self, database, location="US"):
        self.database = database
        self.location = location
        self._client = None

    @property
    def client(self) -> bigquery.Client:
        if not self._client:
            self._client = bigquery.Client(project=self.database, location=self.location)
        return self._client

    @classmethod
    def from_dbt_profile(cls, profile: dict, database=None):
        database = database or profile["project"]
        return cls(database=database, location=profile.get("location", "US"))

    def execute(self, query, **kwargs):
        return self.client.query(query, **kwargs).result()

    def execute_pandas(self, query, **kwargs) -> pd.DataFrame:
        return self.client.query(query, **kwargs).result().to_dataframe(bqstorage_client=True)

    @lru_cache()
    def get_column_metadata_df(self, dataset) -> pd.DataFrame:
        query = "select *" f" from `{self.database}.{dataset}.INFORMATION_SCHEMA.COLUMNS`;"
        dataframe = self.execute_pandas(query)
        dataframe = dataframe.loc[
            dataframe["table_schema"].apply(lambda x: (x.lower() != "information_schema" and not x.startswith("_"))),
            :,
        ]
        dataframe.sort_values(by=["table_schema", "table_name", "ordinal_position"], inplace=True)
        return dataframe

    def list_datasets(self) -> Generator[str, None, None]:
        datasets = list(self.client.list_datasets(self.database))
        datasets.sort(key=lambda x: x.dataset_id)
        for dataset in datasets:
            yield dataset.dataset_id

    def list_tables(self, dataset: str) -> Generator[str, None, None]:
        meta_df = self.get_column_metadata_df(dataset)
        for name in meta_df["table_name"].unique():
            yield name

    def list_columns(self, dataset: str, table: str) -> Generator[ColumnInfo, None, None]:
        meta_df = self.get_column_metadata_df(dataset)
        meta_df = meta_df[meta_df["table_name"] == table]
        rows = meta_df.to_dict(orient="records")
        for row in rows:
            yield ColumnInfo(
                database=self.database,
                schema=dataset,
                table=table,
                name=row["column_name"],
                position=row["ordinal_position"],
                dtype=row["data_type"],
                nullable=True if row["is_nullable"] == "YES" else False,
            )
