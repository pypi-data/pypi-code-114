import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output
import logging

@click.group("stats", short_help="[CWPP] Retrieve statistics for the resources protected by Prisma Cloud")
@pass_environment
def cli(ctx):
    pass

@click.command()
def daily():
    result = pc_lib.get_endpoint("stats/daily")
    cli_output(result)

@click.command()
def dashboard():
    result = pc_lib.get_endpoint("stats/dashboard")
    cli_output(result)

@click.command()
def events():
    result = pc_lib.get_endpoint("stats/events")
    cli_output(result)

@click.command()
def license():
    result = pc_lib.get_endpoint("stats/license")
    cli_output(result)

@click.command()
@click.option('-cve', '--cve')
def vulnerabilities(cve):
    if not cve:
        result = pc_lib.get_endpoint("stats/vulnerabilities")
    else:
        logging.debug("Parameter CVE defined, search for impacted resources")
        result = pc_lib.get_endpoint("stats/vulnerabilities/impacted-resources", {'cve': cve})
    cli_output(result)

cli.add_command(daily)
cli.add_command(dashboard)
cli.add_command(events)
cli.add_command(license)
cli.add_command(vulnerabilities)
