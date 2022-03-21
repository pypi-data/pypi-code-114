import click
import prismacloud.api
from prismacloud.cli import pass_environment
import logging


@click.group("alert", short_help="[CSPM] Returns a list of alerts that match the constraints specified in the query parameters.")
@pass_environment
def cli(ctx):
    pass

@click.command()
@click.option('--compliance-standard', help='Compliance standard, e.g.: \'CIS v1.4.0 (AWS)\'')
@click.option('--amount', default='1', help='Number of units selected with --unit')
@click.option('--unit', default='day', type=click.Choice(['minute', 'hour', 'day', 'week', 'month', 'year'],case_sensitive=False))
@click.option('--detailed/--no-detailed', default=False)
@click.option('--status', default='open', type=click.Choice(['open', 'resolved', 'snoozed', 'dismissed'],case_sensitive=False))
def list(compliance_standard, amount, unit, detailed, status):
    """
    
    Returns a list of alerts from the Prisma Cloud platform.

    
    """

    data = {
            "timeType": "relative",
            "timeAmount": amount,
            "timeUnit": unit,
            "limit": "10",
            "detailed": detailed,
            "alert.status": status,
            "policy.complianceStandard": compliance_standard
        }
    
    # Search for compliance id given a name as input
    result = prismacloud.api.get("v2/alert", data, type='cspm')

    alerts = result["items"]

    try:
        while result["nextPageToken"]:
            data = {
                "pageToken": result["nextPageToken"]
            }

            result["nextPageToken"] = ''

            result = prismacloud.api.get("v2/alert", data, type='cspm')
            alerts = alerts + result["items"]

            try:
                value = result["nextPageToken"]
            except KeyError:
                break
    except:
        pass

    prismacloud.cli.output(alerts)
        
cli.add_command(list)

