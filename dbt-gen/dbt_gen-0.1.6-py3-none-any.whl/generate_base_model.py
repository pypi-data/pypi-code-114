import os

from jinja2 import Template
from tqdm import tqdm

from .adapters import get_adapter
from .generate_base_test import make_test
from .runner import MultiThreadRunner
from .templater import get_template
from .utils import DEFAULT_DBT_PROFILE_PATH, list_yaml, read_dbt_profile, read_source_yaml, write_file

template = get_template("base_model.sql")


def make_model_sql(*args, **kwargs):
    sql = template.render(*args, **kwargs)
    return sql


def generate_base_from_source(adapter, output_folder, source):
    source_identifier = source.get("schema", source["name"])

    for table in source["tables"]:
        table_name = table["name"]
        table_identifier = table.get("identifier", table_name)

        # Identifier is name used in database
        columns = adapter.list_columns(source_identifier, table_identifier)

        # While, name is used in dbt
        sql_content = make_model_sql({"source_name": source["name"], "table_name": table_name, "columns": columns})
        sql_path = os.path.join(output_folder, f"stg__{table_name}.sql")
        write_file(sql_path, sql_content)


def generate_base_model(profile_path, output_folder, source_path, profile_name="default", target="dev", threads=None):
    os.makedirs(output_folder, exist_ok=True)

    profile = read_dbt_profile(profile_path, profile_name=profile_name, target=target)

    bm_tasks = {}
    bt_tasks = {}
    for path in list_yaml(source_path):
        for source in read_source_yaml(path):
            adapter = get_adapter(profile, database=source["database"])

            # Make subfolder for base models
            sub_folder = os.path.join(output_folder, source["name"])
            os.makedirs(sub_folder, exist_ok=True)

            # Base model task
            bm_tasks[source["name"]] = {"adapter": adapter, "output_folder": sub_folder, "source": source}

            # Base test task
            bt_tasks[source["name"]] = {
                "adapter": adapter,
                "source": source,
                "output_path": os.path.join(sub_folder, "schema.yml"),
            }

    bm_runner = MultiThreadRunner(generate_base_from_source, bm_tasks, threads=threads)
    for result in tqdm(bm_runner.run(), total=len(bm_tasks)):
        # print(f"Generated base models of source: {result['task_name']}")
        pass
    print("Done generating base models")

    bt_runner = MultiThreadRunner(make_test, bt_tasks, threads=threads)
    for result in tqdm(bt_runner.run(), total=len(bt_tasks)):
        # print(f"Generated base tests of source: {result['task_name']}")
        pass
    print("Done generating base tests")


def run(args):
    if args.template:
        global template
        print(f"Use custom template at {args.template}")
        with open(args.template, "r", encoding="utf-8") as file:
            template = Template(file.read())

    generate_base_model(
        profile_path=args.profile_path,
        output_folder=args.output_folder,
        source_path=args.source_path,
        profile_name=args.profile_name,
        target=args.target,
        threads=args.threads,
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
    parser.add_argument(
        "--threads",
        type=int,
        default=None,
        help="Max threads. Default is your machine number of threads.",
    )
    parser.add_argument("--template", type=str, default=None, help="Path to custom Jinja template.")
