"""Generate dbt source.yml file.
Read profiles.yml
Connect data warehouse
List all sources
Create source.yml file

Data warehouse supported:
- Snowflake
- BigQuery
"""
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

from .adapters import get_adapter
from .utils import DEFAULT_DBT_PROFILE_PATH, read_dbt_profile, write_file


def make_source_yaml(database, name, tables, schema=None):
    contents = [
        "version: 2",
        "",
        "sources:",
        f"  - name: {name}",
        f"    database: {database}",
    ]
    if schema:
        contents.append(f"    schema: {schema}")

    contents.append("    tables:")
    for tbl in tables:
        if tbl.startswith("_"):
            continue

        contents.append(f"      - name: {tbl.lower()}")

    contents.append("")
    return "\n".join(contents)


def generate_source(adapter, dataset, source_folder):
    dataset = dataset.lower()
    tables = adapter.list_tables(dataset)
    yaml_content = make_source_yaml(adapter.database, dataset, tables)
    yaml_path = os.path.join(source_folder, f"{dataset}.yml")
    write_file(yaml_path, yaml_content)


def generate_source_job(
    dbt_profile_path, source_folder, database=None, profile_name="default", target="dev", threads=None
):
    os.makedirs(source_folder, exist_ok=True)
    profile = read_dbt_profile(dbt_profile_path, profile_name=profile_name, target=target)
    adapter = get_adapter(profile, database=database)

    with ThreadPoolExecutor(threads) as executor:
        futures = {}
        for dataset in adapter.list_datasets():
            futures[executor.submit(generate_source, adapter, dataset, source_folder)] = dataset

        for ft in tqdm(as_completed(futures), total=len(futures)):
            pass

    print("Done")


def run(args):
    generate_source_job(
        dbt_profile_path=args.profile_path,
        source_folder=args.source_folder,
        profile_name=args.profile_name,
        target=args.target,
        database=args.database,
        threads=args.threads,
    )


def config_parser(parser):
    parser.set_defaults(func=run)
    parser.add_argument(
        "source_folder",
        type=str,
        help="Folder to write source YAML files",
    )
    parser.add_argument(
        "--profile-path",
        type=str,
        default=DEFAULT_DBT_PROFILE_PATH,
        help=("Path to dbt profile YAML." f" Default is {DEFAULT_DBT_PROFILE_PATH}"),
    )
    parser.add_argument("--profile-name", type=str, default="default", help="Dbt profile name. Default is `default`.")
    parser.add_argument("--target", type=str, default="dev", help="Dbt profile target. Default is `dev`.")
    parser.add_argument(
        "--database",
        type=str,
        default=None,
        help="Database to inspect. Default is the database in profile.",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=None,
        help="Max threads. Default is your machine number of threads.",
    )
