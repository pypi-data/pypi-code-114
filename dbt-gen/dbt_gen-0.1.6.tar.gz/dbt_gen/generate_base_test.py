import os
from typing import Any, Mapping, Optional

from tqdm import tqdm

from .adapters import BaseAdapter, BigQueryAdapter, SnowflakeAdapter, get_adapter
from .runner import Runner
from .templater import Templater
from .utils import DEFAULT_DBT_PROFILE_PATH, list_yaml, read_dbt_profile, read_source_yaml, write_file

template = Templater().load_template("base_tests.yml")


class UnsupportedException(Exception):
    pass


def get_snowflake_pkeys(adapter: SnowflakeAdapter, source: Mapping[str, Any]) -> Mapping[str, Any]:
    pkeys = {}
    for table in tqdm(source["tables"]):
        schema = source.get("schema", source["name"])
        query = f"describe table {source['database']}.{schema}.{table['name']}"
        cols = []
        for row in adapter.execute(query):
            if row["primary key"] == "Y":
                cols.append(row["name"].lower())
        pkeys[table["name"]] = cols
    return pkeys


def get_bigquery_pkeys__stitch(adapter: BigQueryAdapter, source: Mapping[str, Any]) -> Mapping[str, Any]:
    schema = source.get("schema", source["name"])
    pkeys = {}

    if "_sdc_primary_keys" in list(adapter.list_tables(schema)):
        info_df = adapter.execute_pandas(
            f"select table_name, column_name from `{source['database']}.{schema}._sdc_primary_keys`;"
        )
        for _, row in info_df.iterrows():
            cols = pkeys.setdefault(row["table_name"], [])
            cols.append(row["column_name"])
    else:
        print(f"WARNING: There is no Stitch primary key table in the dataset {schema}. Tests will be empty.")
    return pkeys


def get_pkeys(adapter: BaseAdapter, source: Mapping[str, Any]) -> Mapping[str, Any]:
    if isinstance(adapter, BigQueryAdapter):
        return get_bigquery_pkeys__stitch(adapter, source)
    elif isinstance(adapter, SnowflakeAdapter):
        return get_snowflake_pkeys(adapter, source)
    else:
        raise UnsupportedException(f"Adapter name {adapter.name} is unsupported")


def make_test(adapter: BaseAdapter, source: Mapping[str, Any], output_path: str, **kwargs) -> None:
    pkeys = get_pkeys(adapter, source)
    table_info = [
        {"name": table, "description": "", "pkeys": " || '-' || ".join(pkeys), "extra": kwargs}
        for table, pkeys in pkeys.items()
    ]
    test_yaml = template.render(tables=table_info)
    write_file(output_path, test_yaml)


def generate_base_tests(
    profile_path: str,
    source_path: str,
    output_folder: str,
    profile_name: Optional[str] = "default",
    target: Optional[str] = "dev",
    extra: Optional[Mapping[str, Any]] = None,
):
    extra = extra or {}
    profile = read_dbt_profile(profile_path, profile_name, target)

    tasks = {}
    for path in list_yaml(source_path):
        for source in read_source_yaml(path):
            adapter = get_adapter(profile, database=source["database"])
            tasks[source["name"]] = {
                "adapter": adapter,
                "source": source,
                "output_path": os.path.join(output_folder, f'{source["name"]}.yml'),
            }

    runner = Runner(make_test, tasks, **extra)

    for result in runner.run():
        print(f"Source {result['task_name']}")


def run(args):
    generate_base_tests(
        profile_path=args.profile_path,
        source_path=args.source_path,
        output_folder=args.output_folder,
        profile_name=args.profile_name,
        target=args.target,
        extra=None,
    )


def config_parser(parser):
    parser.set_defaults(func=run)
    parser.add_argument("source_path", type=str, help="Path to dbt source YAML.")
    parser.add_argument(
        "output_folder",
        type=str,
        help="Folder to write base models.",
    )
    parser.add_argument(
        "--profile-path",
        type=str,
        default=DEFAULT_DBT_PROFILE_PATH,
        help=("Path to dbt profile YAML." f" Default is {DEFAULT_DBT_PROFILE_PATH}"),
    )
    parser.add_argument("--profile-name", type=str, default="default", help="Dbt profile name. Default is `default`.")
    parser.add_argument("--target", type=str, default="dev", help="Dbt profile target. Default is `dev`.")
