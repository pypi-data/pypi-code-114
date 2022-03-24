import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.command("license", short_help="[CWPP] Returns the license stats including the credit per defender")
@pass_environment
def cli(ctx):
    result = pc_lib.get_endpoint("stats/license")
    cli_output(result)