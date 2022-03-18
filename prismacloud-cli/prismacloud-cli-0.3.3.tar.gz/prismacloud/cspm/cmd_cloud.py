import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.group("cloud", short_help="[CSPM] Lists all cloud accounts onboarded onto the Prisma Cloud platform")
@pass_environment
def cli(ctx):
    """List Cloud Accounts"""
    pass

@click.command()
def list():
    """Lists all cloud accounts onboarded onto the Prisma Cloud platform."""
    result = prismacloud.api.get("cloud", type='cspm')
    prismacloud.cli.output(result)

@click.command()
def name():
    """Returns a list of cloud account IDs and names."""
    result = prismacloud.api.get("cloud/name", type='cspm')
    prismacloud.cli.output(result)

@click.command()
def type():
    """Returns all the cloud types."""
    result = prismacloud.api.get("cloud/type", type='cspm')
    prismacloud.cli.output(result)

cli.add_command(list)
cli.add_command(name)
cli.add_command(type)
