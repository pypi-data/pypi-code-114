import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.group("defenders", short_help="[CWPP] Retrieves Defenders information.")
@pass_environment
def cli(ctx):
    pass

@click.command()
def list():
    result = pc_lib.get_endpoint("defenders")
    prismacloud.cli.output(result)

@click.command()
def names():
    result = pc_lib.pc_api.defenders_names_list_read()
    prismacloud.cli.output(result)

@click.command()
def summary():
    result = pc_lib.get_endpoint("defenders/summary")
    prismacloud.cli.output(result)

cli.add_command(list)
cli.add_command(names)
cli.add_command(summary)