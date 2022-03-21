from apiclient import APIClient
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from importlib import util
from IPython.display import display
from jsondiff import JsonDiffer
from os import path
from pydoc import Helper
from tabulate import tabulate
import click
import json
import logging
import coloredlogs
import os
import pandas as pd
import requests
import sys
import warnings
import prismacloud.version


# Set defaults
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 4)
pd.set_option('display.width', 100)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)
requests.packages.urllib3.disable_warnings()
warnings.simplefilter(action='ignore', category=FutureWarning)
CONTEXT_SETTINGS = dict(auto_envvar_prefix="PC")

class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_environment = click.make_pass_decorator(Environment, ensure=True)
cwpp_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "cwpp"))
cspm_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "cspm"))

class PrismaCloudCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []

        # Iterate through cwpp commands
        for filename in os.listdir(cwpp_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])

        # Iterate through cspm commands
        for filename in os.listdir(cspm_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])

        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"prismacloud.cwpp.cmd_{name}", None, None, ["cli"])
        except ImportError as e:
            # Importing cwpp command did not work. Try to import cspm
            try:
                mod = __import__(f"prismacloud.cspm.cmd_{name}", None, None, ["cli"])
            except ImportError as e:
                return
        return mod.cli


@click.command(cls=PrismaCloudCLI, context_settings=CONTEXT_SETTINGS, help="""

Prisma Cloud CLI 

Version: {0}

""".format(prismacloud.version.version))
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@click.option("-o", "--output", type=click.Choice(['text', 'csv', 'json', 'html', 'columns']), default='text')
@click.option("-c", "--config", 'configuration', help="Select configuration ~/.prismacloud/[CONFIGURATION].json", default="credentials")
@click.option("--columns", 'columns', help="Select columns for output", default=None)
@pass_environment
def cli(ctx, verbose, configuration, output, columns=None):
    ctx.verbose = verbose
    ctx.configuration = configuration
    ctx.output = output

    if ctx.verbose:
        logging.basicConfig(
            level=logging.DEBUG, format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        coloredlogs.install(level='DEBUG')
    else:
        logging.basicConfig(
            level=logging.ERROR, format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        coloredlogs.install(level='ERROR')

    


def output(data):
    # Retrieve parameters
    params = click.get_current_context().find_root().params

    if params["columns"]:
        columns = params["columns"].split(",")

    # Check type of data
    if isinstance(data, list):
        df = pd.DataFrame(data)
    
    # We have data from our request, send to dataframe
    try:
        logging.debug("Normalize data")
        df = pd.json_normalize(data)
        #print(df)

        # Do some optimization on our dataframe
        try:
            df['time'] = pd.to_datetime(df.time)
            df.fillna('', inplace=True)
        except:
            logging.debug('No time field')
        
        # We have a dataframe, output here after we have dropped
        # all but the selected columns
        if not params["columns"] == None:
            logging.debug("Dropping these columns: {}".format(df.columns.difference(columns)))
            df.drop(columns=df.columns.difference(columns), axis=1, inplace=True, errors='ignore')
        else:
            pass

        if params["output"] == "text":
            click.secho(tabulate(df, headers = 'keys', tablefmt = 'psql'), fg='green')
        if params["output"] == "json":
            click.secho(df.to_json(orient='records'), fg='green')
        if params["output"] == "csv":
            click.secho(df.to_csv(), fg='green')
        if params["output"] == "html":
            click.secho(df.to_html(), fg='green')
        if params["output"] == "columns":
            for column in df.columns:
                click.secho(column, fg='green')
                
    except Exception as e:
        # There is no dataframe, might be just a single value
        # like version. Show data
        click.echo(data)

        logging.debug("Error ingesting data into dataframe: {}".format(e))


if __name__ == "__main__":
    #cli()

    try:
        cli()
    except Exception as e:
        logging.error("An error has occured: {}".format(e))

