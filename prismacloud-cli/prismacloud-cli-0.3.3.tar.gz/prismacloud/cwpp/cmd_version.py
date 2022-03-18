import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("version", short_help="Shows CWPP version.")
@pass_environment
def cli(ctx):
    version = prismacloud.api.get("version")
    prismacloud.cli.output(version)