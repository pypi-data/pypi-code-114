import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.command("users", short_help="[CWPP] Retrieves a list of all users")
@pass_environment
def cli(ctx):
    result = pc_lib.get_endpoint("users")
    cli_output(result)
