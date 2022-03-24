import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.command("check", short_help="[CSPM] Output details about the current user")
@pass_environment
def cli(ctx):
    result = pc_lib.pc_api.current_user()
    cli_output(result)
