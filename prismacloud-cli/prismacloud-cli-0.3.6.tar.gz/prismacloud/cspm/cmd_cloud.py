import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.group("cloud", short_help="[CSPM] Lists all cloud accounts onboarded onto the Prisma Cloud platform")
@pass_environment
def cli(ctx):
    """List Cloud Accounts and Types"""
    pass

@click.command()
def list():
    """Returns Cloud Accounts."""
    result = pc_lib.pc_api.cloud_accounts_list_read()
    cli_output(result)

@click.command()
def names():
    """Returns Cloud Account IDs and Names."""
    result = pc_lib.pc_api.cloud_accounts_list_names_read()
    cli_output(result)

@click.command()
def type():
    """Returns all Cloud Types."""
    result = pc_lib.pc_api.cloud_types_list_read()
    cli_output(result)

cli.add_command(list)
cli.add_command(names)
cli.add_command(type)
