from abc import ABC, abstractmethod, abstractclassmethod
from typing import Generator, Mapping, Any

import pandas as pd


class ColumnInfo:
    def __init__(
        self,
        database,
        schema,
        table,
        name,
        position,
        dtype,
        nullable: bool = True,
        extra: Mapping[str, Any] = None,
    ):
        self.database = database
        self.table = table
        self.schema = schema
        self.name = name
        self.position = int(position)
        self.nullable = bool(nullable)
        self.dtype = dtype
        self.extra = extra or {}

    def __str__(self) -> str:
        return f"Column: {self.name}, position: {self.position}, nullable: {self.nullable}, dtype: {self.dtype}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> str:
        return {
            "database": self.database,
            "schema": self.schema,
            "table": self.table,
            "name": self.name,
            "position": self.position,
            "nullable": self.nullable,
            "dtype": self.dtype,
            "extra": self.extra,
        }


class BaseAdapter(ABC):
    name = None

    def __init__(self, database) -> None:
        self.database = database

    @abstractclassmethod
    def from_dbt_profile(cls, profile: Mapping[str, Any], database=None):
        pass

    @abstractmethod
    def list_datasets(self) -> Generator[str, None, None]:
        pass

    @abstractmethod
    def list_tables(self, dataset: str) -> Generator[str, None, None]:
        pass

    @abstractmethod
    def list_columns(self, dataset: str, table: str) -> Generator[ColumnInfo, None, None]:
        pass

    @abstractmethod
    def execute(self, query, **kwargs) -> Any:
        pass

    @abstractmethod
    def execute_pandas(self, query, **kwargs) -> pd.DataFrame:
        pass
