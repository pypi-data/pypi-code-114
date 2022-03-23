import click

from .api import SentryApi
from .commands import *


# The common_options idea is borrowed from https://github.com/pallets/click/issues/108
common_options = [
    click.option(
        "--auth-token",
        required=True,
        envvar="QSENTRY_AUTH_TOKEN",
        help="The auth token for invoke sentry apis. Can read from the QSENTRY_AUTH_TOKEN env variable.",
    ),
    click.option(
        "--host-url",
        required=True,
        envvar="QSENTRY_HOST_URL",
        default="https://sentry.io/",
        show_default=True,
        help="The host URL for the sentry service. Can read from the QSENTRY_HOST_URL env variable.",
    ),
    click.option(
        "--org",
        envvar="QSENTRY_ORG_SLUG",
        help="The organization slug. Can read from the QSENTRY_ORG_SLUG env variable.",
    ),
    click.option(
        "--count/--no-count",
        is_flag=True,
        default=False,
        help="Show the count of objects (members, teams and etc.)",
    ),
]


def add_common_options(options):
    def _add_common_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_common_options


def comma_separated_string_to_array(ctx, param, value):
    val = []
    for item in value:
        val += item.split(",")
    return val


@click.group(invoke_without_command=True)
def main(*args, **kwargs):
    pass


@main.command()
@add_common_options(common_options)
@click.option(
    "--list-all",
    default=["id", "name", "email"],
    show_default=True,
    multiple=True,
    is_flag=False,
    flag_value="id,name,email",
    callback=comma_separated_string_to_array,
    help="""List all members of an organization. The argument to this option should
            be a comma separated string. This option can be specified multiple
            times, each with an attribute you want to see for the listed members.""",
)
@click.option(
    "--search-by",
    help="""Search a member by an attribute such as id, email and etc. The argument to
            this option should be in "<attr>:<value>" form, for example, "id=123"
            or "email=foo@example.com".""",
)
@click.option(
    "--team",
    envvar="QSENTRY_TEAM_SLUG",
    help="""Show the members of a given team. Can use the --role option to filter
            by roles.""",
)
@click.option(
    "--role", default="admin", show_default=True, help="The role of the member."
)
def members(**kwargs):
    """Show member related things"""
    MembersCommand(**kwargs).run(**kwargs)


@main.command()
@add_common_options(common_options)
def teams(**kwargs):
    """Show teams related things"""
    TeamsCommand(**kwargs).run(**kwargs)


@main.command()
@add_common_options(common_options)
@click.option(
    "--list-members",
    is_flag=True,
    help="List all members of a given organization.",
)
def orgs(**kwargs):
    "Show organization related things"
    OrgsCommand(**kwargs).run(**kwargs)


if __name__ == "__main__":
    main()
