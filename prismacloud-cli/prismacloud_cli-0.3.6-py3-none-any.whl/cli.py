""" Prisma Cloud CLI Configuration and Output """

#import json
import logging
import os
import sys
import warnings

#from importlib import util
#from os import path
#from pydoc import Helper

import click
import coloredlogs
import json
import pandas as pd

#from click_help_colors import HelpColorsGroup, HelpColorsCommand
#from IPython.display import display
#from jsondiff import JsonDiffer
from tabulate import tabulate

import prismacloud.version

import prismacloud.pc_lib.posture

# Set defaults
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 4)
pd.set_option('display.width', 100)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)
warnings.simplefilter(action='ignore', category=FutureWarning)
CONTEXT_SETTINGS = dict(auto_envvar_prefix="PC")

class Environment:
    """ Initialize environment and define logging """

    def __init__(self):
        """ Initialize environment  """
        self.verbose = False
        self.home = os.getcwd()

    # pylint: disable=R0201
    def log(self, msg, *args):
        """ Logs a message to stderr """
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """ Logs a message to stderr only if verbose is enabled """
        if self.verbose:
            self.log(msg, *args)

pass_environment = click.make_pass_decorator(Environment, ensure=True)
cwpp_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "cwpp"))
cspm_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "cspm"))
pccs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "pccs"))
class PrismaCloudCLI(click.MultiCommand):
    """ Collect commands """

    def list_commands(self, ctx):
        """ Read commands from command files """
        commands = []
        # Iterate through cwpp commands
        for filename in os.listdir(cwpp_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename[4:-3])
        # Iterate through cspm commands
        for filename in os.listdir(cspm_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename[4:-3])
        # Iterate through pccs commands
        for filename in os.listdir(pccs_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename[4:-3])
        commands.sort()

        return commands

    # pylint: disable=R1710
    def get_command(self, ctx, name):
        
        """ Import command """

        root = os.path.abspath(os.path.join(os.path.dirname(__file__)))

        if os.path.exists("{}/cwpp/cmd_{}.py".format(root, name)):
            try:
                mod = __import__(f"prismacloud.cwpp.cmd_{name}", None, None, ["cli"])
                return mod.cli
            except ImportError as error:
                logging.error(error.__class__.__name__ + ": " + error.message)
        elif os.path.exists("{}/cspm/cmd_{}.py".format(root, name)):
            try:
                mod = __import__(f"prismacloud.cspm.cmd_{name}", None, None, ["cli"])
                return mod.cli
            except ImportError as error:
                logging.error(error.__class__.__name__ + ": " + error.message)
        
        elif os.path.exists("{}/pccs/cmd_{}.py".format(root, name)):
            try:
                mod = __import__(f"prismacloud.pccs.cmd_{name}", None, None, ["cli"])
                return mod.cli
            except ImportError as error:
                logging.error(error.__class__.__name__ + ": " + error.message)



@click.command(cls=PrismaCloudCLI, context_settings=CONTEXT_SETTINGS, help="""

Prisma Cloud CLI

Version: {0}

""".format(prismacloud.version.version))
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode")
@click.option("-o", "--output", type=click.Choice(['text', 'csv', 'json', 'html', 'columns']), default='text')
@click.option("-c", "--config", 'configuration', help="Select configuration file in ~/.prismacloud/[CONFIGURATION].json", default="credentials")
@click.option("--columns", 'columns', help="Select columns for output", default=None)
@pass_environment
# pylint: disable=W0613
def cli(ctx, verbose, configuration, output, columns=None):
    """ Define the command line """
    ctx.configuration = configuration
    ctx.output = output
    ctx.verbose = verbose
    if ctx.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        coloredlogs.install(level='DEBUG')
    else:
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        coloredlogs.install(level='ERROR')

def cli_output(data):
    """ Formatted output """
    # Retrieve parameters
    params = click.get_current_context().find_root().params
    if params["columns"]:
        columns = params["columns"].split(",")
    # Check type of data
    if isinstance(data, list):
        data_frame = pd.DataFrame(data)

    # We have data from our request, send to dataframe
    try:
        data_frame_normalized = pd.json_normalize(data)
        print(data_frame_normalized)

        # If the size of our normalized data is 0, something went wrong
        # and we don't use the normalized data.
        # Otherwise, use the normalized data.
        if data_frame_normalized.size > 0:
            logging.debug("Using normalized data")
            data_frame = data_frame_normalized
        
        # print(data_frame)
        # Do some optimization on our dataframe
        try:
            data_frame['time'] = pd.to_datetime(data_frame.time)
            data_frame.fillna('', inplace=True)
        except Exception:
            logging.debug('No time field')
        # We have a dataframe, output here after we have dropped
        # all but the selected columns
        if params["columns"]:
            logging.debug("Dropping these columns: %s", data_frame.columns.difference(columns))
            data_frame.drop(columns=data_frame.columns.difference(columns), axis=1, inplace=True, errors='ignore')
        else:
            pass
        if params["output"] == "text":
            click.secho(tabulate(data_frame, headers = 'keys', tablefmt = 'psql'), fg='green')
        if params["output"] == "json":
            click.secho(data_frame.to_json(orient='records'), fg='green')
        if params["output"] == "csv":
            click.secho(data_frame.to_csv(), fg='green')
        if params["output"] == "html":
            click.secho(data_frame.to_html(), fg='green')
        if params["output"] == "columns":
            for column in data_frame.columns:
                click.secho(column, fg='green')
    except Exception as ex:
        # There is no dataframe, might be just a single value, like version.
        click.echo(data)
        logging.debug("Error ingesting data into dataframe: %s", ex)


if __name__ == "__main__":
    try:
        # pylint: disable=E1120
        cli()
    except Exception as ex:
        logging.error("An error has occured: %s", ex)
