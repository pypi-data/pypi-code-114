import click

from .api import SentryApi
from .commands import *


def add_common_options(options):
    def _add_common_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_common_options


def comma_separated_string_to_array(ctx, param, value):
    """Split a non empty string and return the result list

    Or return an empty list if the value is empty string.
    """
    return value.split(",") if value else []


# The common_options idea is borrowed from https://github.com/pallets/click/issues/108
common_options = [
    click.option(
        "--auth-token",
        required=True,
        envvar="QSENTRY_AUTH_TOKEN",
        help="""The auth token for invoking sentry apis. Can read from the
                QSENTRY_AUTH_TOKEN env variable.""",
    ),
    click.option(
        "--host-url",
        required=True,
        envvar="QSENTRY_HOST_URL",
        default="https://sentry.io/",
        show_default=True,
        help="""The host URL for the sentry service. Can read from the
                QSENTRY_HOST_URL env variable.""",
    ),
    click.option(
        "--org",
        required=True,
        envvar="QSENTRY_ORG_SLUG",
        help="""The organization slug. Can read from the QSENTRY_ORG_SLUG env
                variable.""",
    ),
    click.option(
        "--count/--no-count",
        is_flag=True,
        default=False,
        help="Show the count of objects (members, teams and etc.)",
    ),
]

common_orgs_options = [
    click.option(
        "--attrs",
        default="",
        callback=comma_separated_string_to_array,
        help="""The argument to this option should be a comma separated string.
                For example, "id,name".""",
    ),
]


@click.group(invoke_without_command=True)
def main(*args, **kwargs):
    pass


@main.group(invoke_without_command=True)
def orgs(*args, **kwargs):
    """Organization related commands"""
    pass


@main.group(invoke_without_command=True)
def members(*args, **kwargs):
    """Member related commands"""
    pass


@main.command()
@add_common_options(common_options)
def teams(**kwargs):
    """Team related commands"""
    TeamsCommand(**kwargs).run(**kwargs)


# Member sub-commands
@members.command(name="list")
@add_common_options(common_options)
@click.option(
    "--all",
    is_flag=True,
    help="""List all members of an organization. It shows the member's id and
            email by default. Use the --attrs option to change what attributes
            to show.""",
)
@click.option(
    "--team",
    envvar="QSENTRY_TEAM_SLUG",
    help="""Show the members of a given team. Should be used with --role option
            to filter by roles.""",
)
@click.option(
    "--role", default="admin", show_default=True, help="The role of the member."
)
@click.option(
    "--attrs",
    default="",
    callback=comma_separated_string_to_array,
    help="""The argument to this option should be a comma separated string. For
            example, "id,email,name".""",
)
def list_command(**kwargs):
    """List members"""
    MembersCommand(**kwargs).list_command(**kwargs)


@members.command()
@add_common_options(common_options)
@click.argument("search_by_term")
def search_by(**kwargs):
    MembersCommand(**kwargs).search_by(kwargs["search_by_term"])


# Organization sub-commands
@orgs.command()
@add_common_options(common_options)
@add_common_options(common_orgs_options)
def list_projects(**kwargs):
    """List all projects of the given organization.

    List the project's id and name by default. Use the --attrs option to change
    what attributes to show.
    """
    attrs = kwargs["attrs"] if kwargs["attrs"] else ["id", "name"]
    OrgsCommand(**kwargs).list_projects(attrs)


@orgs.command()
@add_common_options(common_options)
@add_common_options(common_orgs_options)
def list_users(**kwargs):
    """List all users of the given organization.

    List the user's id and email by default. Use the --attrs option to change
    what attributes to show.
    """
    attrs = kwargs["attrs"] if kwargs["attrs"] else ["id", "email"]
    OrgsCommand(**kwargs).list_users(attrs)


if __name__ == "__main__":
    main()
