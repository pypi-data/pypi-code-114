################################################################################
# Copyright IBM Corporation 2021, 2022
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

"""
Tackle Data Gravity Insights

Command Line Interface (CLI) for Tackle Data Gravity Insights
"""
from argparse import ArgumentError
from email.policy import default
import os
import sys
import yaml
import json
import yaml
import click
import logging
import importlib.resources

from tqdm import tqdm
from collections import OrderedDict
from neomodel import config
from simple_ddl_parser import parse_from_file
from neomodel import config
from pathlib import Path
from collections import namedtuple

# Import our packages
from .schema2graph import schema_loader
from .tx2graph.transaction_loader import analyze, tx2neo4j, clear_all_nodes
from .code2graph import ClassGraphBuilder, MethodGraphBuilder
from .code2graph.utils.parse_config import Config


######################################################################
# cli - Grouping for sub commands
######################################################################


@click.group()
@click.option("--abstraction", "-a", default="class", help="The level of abstraction to use when building the graph. Valid options are: class, method, or full.", show_default=True)
@click.option("--quiet/--verbose", "-q/-v", required=False, help="Be more quiet/verbose", default=False, is_flag=True, show_default=True)
@click.option("--clear/--dont-clear", "-c/-dnc", help="Clear (or don't clear) graph before loading", default=True, is_flag=True, show_default=True)
@click.pass_context
def cli(ctx, abstraction, quiet, clear):
    """Tackle Data Gravity Insights"""
    ctx.ensure_object(dict)
    ctx.obj['abstraction'] = abstraction
    ctx.obj['verbose'] = not quiet
    ctx.obj['clear'] = clear

######################################################################
# schema2graph - Populates the graph from an SQL schema DDL
######################################################################


@cli.command()
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="The SQL/DDL file to load into the graph")
@click.option("--output", "-o", required=False, help="The JSON file to write the schema to")
@click.option("--validate", "-v", help="Validate file if OK but don't populate graph", is_flag=True, hidden=True)
@click.pass_context
def s2g(ctx, input, output, validate):
    """This command parses SQL schema DLL into a graph"""

    # Read the DDL file
    click.echo(f"Reading: {input}")
    result = None
    try:
        result = parse_from_file(input, group_by_type=True)
    except FileNotFoundError as error:
        raise click.ClickException(error)

    # Optionally write it output to json
    if output:
        click.echo(f"Writing: {output}")
        with open(output, "w") as f:
            contents = json.dumps(result, indent=4)
            f.write(contents)

    if validate:
        click.echo(f"File [{input}] validated.")
        exit(0)

    if ctx.obj['clear']:
        click.echo("Clearing graph...")
        schema_loader.remove_all_nodes()

    click.echo("Building Graph...")
    schema_loader.load_graph(result)
    click.echo("Graph build complete")


######################################################################
#  tx2graph - Loads output from DiVA into graph
######################################################################
@cli.command()
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="DiVA Transaction JSON file")
@click.pass_context
def tx2g(ctx, input):
    """This command loads DiVA database transactions into a graph"""

    if ctx.obj["verbose"]:
        click.echo("Verbose mode: ON")

    # ------------------
    # Configure NeoModel
    # ------------------
    config.DATABASE_URL = os.environ.get("NEO4J_BOLT_URL")
    config.ENCRYPTED_CONNECTION = False

    # ----------------------
    # Load transactions data
    # ----------------------
    yaml.add_representer(OrderedDict, lambda dumper, data: dumper.represent_mapping(
        'tag:yaml.org,2002:map', list(data.items())))
    data = json.load(open(input), object_pairs_hook=OrderedDict)

    # -------------------------
    # Set logging configuration
    # -------------------------
    loglevel = logging.WARNING
    if (ctx.obj["verbose"]):
        loglevel = logging.INFO
    logging.basicConfig(level=loglevel, format="[%(levelname)s] %(message)s")

    if ctx.obj["clear"]:
        logging.info(
            "Clear flag detected... Deleting pre-existing SQLTable nodes.")
        clear_all_nodes()

    click.echo("Building Graph...")

    logging.info("Populating transactions")
    for c, entry in tqdm(enumerate(data), total=len(data)):
        txs = analyze(entry['transactions'])
        del(entry['transactions'])
        label = yaml.dump(entry, default_flow_style=True).strip()
        tx2neo4j(txs, label)

    click.echo("Graph build complete")


######################################################################
#  code2graph - Imports code dependencies into the graph
######################################################################
@cli.command()
@click.option("--input", "-i", type=click.Path(exists=True, resolve_path=True, file_okay=False), required=True, help="DOOP output facts directory.")
@click.option("--validate", help="Testing mode, the graph won't be built.", is_flag=True, hidden=True)
@click.pass_context
def c2g(ctx, input, validate):
    """This command loads Code dependencies into the graph"""

    click.echo("code2graph generator started...")

    if ctx.obj["verbose"]:
        click.echo("Verbose mode: ON")

    # -------------------------
    # Set logging configuration
    # -------------------------
    loglevel = logging.WARNING
    if (ctx.obj["verbose"]):
        loglevel = logging.INFO
    logging.basicConfig(level=loglevel, format="[%(levelname)s] %(message)s")

    # -------------------------
    # Initialize configurations
    # -------------------------
    proj_root = importlib.resources.files('dgi.code2graph')
    usr_cfg = Config(config_file=proj_root.joinpath("etc", "config.yml"))
    usr_cfg.load_config()

    # Add the input dir to configuration.
    usr_cfg.set_config(key="GRAPH_FACTS_DIR", val=input)

    # ---------------
    # Configure Neo4J
    # ---------------
    config.DATABASE_URL = os.environ.get("NEO4J_BOLT_URL")
    config.ENCRYPTED_CONNECTION = False

    # ---------------
    # Build the graph
    # ---------------

    click.echo("Building Graph...")

    class_g_builder = ClassGraphBuilder(usr_cfg)
    method_g_builder = MethodGraphBuilder(usr_cfg)

    if ctx.obj["abstraction"].lower() == "full":
        if validate:
            click.echo("Validate mode: abstraction level is {}".format(
                ctx.obj["abstraction"].lower()))
            sys.exit()
        class_g_builder.build_ddg(clear=ctx.obj['clear'])
        method_g_builder.build_ddg(clear=ctx.obj['clear'])

    elif ctx.obj["abstraction"].lower() == "class":
        if validate:
            click.echo("Validate mode: abstraction level is {}".format(
                ctx.obj["abstraction"].lower()))
            sys.exit()
        class_g_builder.build_ddg(clear=ctx.obj['clear'])

    elif ctx.obj["abstraction"].lower() == "method":
        if validate:
            click.echo("Validate mode: abstraction level is {}".format(
                ctx.obj["abstraction"].lower()))
            sys.exit()
        method_g_builder.build_ddg(clear=ctx.obj['clear'])

    else:
        raise click.BadArgumentUsage(
            "Not a valid abstraction level. Valid options are 'class', 'method', 'full'.")

    click.echo("code2graph build complete")


# ######################################################################
# # init - Initialize a new database for collecting configuration
# ######################################################################
# @cli.command()
# @click.option("--data-directory", "-d", default=".", help="Directory of configuration database",
#               envvar="DATA_DIRECTORY", type=click.Path())
# @click.option("--windup", "-w", default=None, help="tcd-windup server host")
# @click.option("--windup-ssl", "-s", is_flag=True, help="Enable SSL for tcd-windup server")
# @pass_config
# def init(config, data_directory, windup, windup_ssl):
#     """Initialize a new configuration."""

#     if data_directory:
#         click.echo(f"Initializing database in [{data_directory}]")
#         config.data_directory = data_directory

#     if windup:
#         click.echo(f"Using tcd-windup server at {windup}")
#         config.windup_host = windup
#         config.windup_ssl = False

#     if windup_ssl:
#         click.echo("Enabling SSL for windup")
#         config.windup_ssl = windup_ssl

#     click.echo(f"Saving config to {config.FILE_NAME}")
#     config.write()


# ######################################################################
# # config - Display the current configuration
# ######################################################################
# @cli.command()
# @pass_config
# def config(config):
#     """Displays the current configuration"""
#     config.read()
#     attrs = config.__dict__
#     click.echo("Current config:")
#     for name in attrs:
#         click.echo(f"  {name}={attrs[name]}")


# ######################################################################
# # collect - Collects configuration files for a given framework
# ######################################################################
# @cli.command()
# @click.option("--framework", "-f", required=True, help="The application framework to look for")
# @click.option("--collector", "-c", required=False, help="The collector to use [file | windup]")
# @click.option("--source", "-s", default=None, help="Source folder to scan")
# @click.option("--repo", "-r", default=None, help="Public git repository to scan")
# @click.option("--all", "-a", is_flag=True, required=False, help="Collect all filenames")
# @click.option("--output", "-o", type=click.Choice(OUTPUT_FORMATS, case_sensitive=False),
#               default="json", help="Output format for collected data",
# )
# @pass_config
# def collect(config, framework, collector, source, repo, all, output):
#     """Collect configuration files for a given framework."""

#     click.echo("Running Collector...")

#     if not source and not repo:
#         raise click.BadParameter(
#             "You must specify --source or --repo\nAborting collection!"
#         )

#     if not collector:
#         collector = "file" # default to file collector

#     if config.verbose:
#         click.echo(" O P T I O N S ".center(40, "-"))
#         click.echo(f"Framework: {framework}")
#         click.echo(f"Collector: {collector}")
#         click.echo(f"Source: {source}")
#         click.echo(f"Repo: {repo}")
#         click.echo(f"All: {all}")
#         click.echo(f"Output: {output}")
#         click.echo(40 * "-")

#     if collector.lower() == "file":
#         collect = FileCollector(config)
#         details = collect.collect(framework, source, all)
#         click.echo(f"Saving results to {config.data_directory} as {output}...")
#         if output == "yaml":
#             save_to_yaml(details, os.path.join(config.data_directory, "data.yaml"))
#         elif output == "ndjson":
#             save_to_ndjson(details, os.path.join(config.data_directory, "data.ndjson"))
#         else:  # default
#             save_to_json(details, os.path.join(config.data_directory, "data.json"))
#     elif collector.lower() == "windup":
#         if repo and config.windup_host:
#             collect = WindupCollector(config)
#             details = collect.collect(framework, repo, all)
#             if config.verbose:
#                 click.echo(details)
#     else:
#         raise click.BadParameter(
#             "You must specify a --collector from [file, windup]!"
#         )

#     click.echo("Collection complete.")
