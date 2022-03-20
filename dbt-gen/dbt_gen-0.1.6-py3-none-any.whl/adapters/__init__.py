from .base import BaseAdapter
from .bigquery_adapter import BigQueryAdapter
from .snowflake_adapter import SnowflakeAdapter


def get_adapter(profile: dict, database=None) -> BaseAdapter:
    adapter_name = profile["type"]
    if adapter_name == "bigquery":
        return BigQueryAdapter.from_dbt_profile(profile, database=database)
    elif adapter_name == "snowflake":
        return SnowflakeAdapter.from_dbt_profile(profile, database=database)
    else:
        raise ValueError(f"Adapter {adapter_name} not exists")
