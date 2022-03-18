import click
import prismacloud.api
from prismacloud.cli import pass_environment
import logging

@click.group("stats", short_help="Retrieve statistics for the resources protected by Prisma Cloud Compute")
@pass_environment
def cli(ctx):
    pass

@click.command()
def license():
    result = prismacloud.api.get("stats/license")
    prismacloud.cli.output(result)

@click.command()
def dashboard():
    result = prismacloud.api.get("stats/dashboard")
    prismacloud.cli.output(result)

@click.command()
def events():
    result = prismacloud.api.get("stats/events")
    prismacloud.cli.output(result)

@click.command()
def daily():
    result = prismacloud.api.get("stats/daily")
    prismacloud.cli.output(result)

@click.command()
@click.option('-cve', '--cve')
def vulnerabilities(cve):
    if not cve:
        result = prismacloud.api.get("stats/vulnerabilities")
    else:
        logging.debug("Parameter CVE defined, search for impacted resources")
        result = prismacloud.api.get("stats/vulnerabilities/impacted-resources",  { "cve": cve })

    prismacloud.cli.output(result)

cli.add_command(dashboard)
cli.add_command(license)
cli.add_command(events)
cli.add_command(daily)
cli.add_command(vulnerabilities)