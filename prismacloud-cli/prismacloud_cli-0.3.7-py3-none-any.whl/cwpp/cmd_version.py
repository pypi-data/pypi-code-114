import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.command("version", short_help="[CWPP] Shows CWPP version.")
@pass_environment
def cli(ctx):
    version = pc_lib.get_endpoint("version")
    cli_output(version)
