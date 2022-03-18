import click
import prismacloud.api
from prismacloud.cli import pass_environment


@click.command("settings", short_help="Shows CWPP settings.")
@pass_environment
def cli(ctx):
    settings = prismacloud.api.get("settings/defender")
    prismacloud.cli.output(settings)