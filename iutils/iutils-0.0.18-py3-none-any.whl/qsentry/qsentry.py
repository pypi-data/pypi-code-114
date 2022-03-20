import click

from .api import SentryApi


# The common_options idea is borrowed from https://github.com/pallets/click/issues/108
common_options = [
    click.option(
        "--auth-token",
        envvar="QSENTRY_AUTH_TOKEN",
        help="The auth token for invoke sentry apis.",
    ),
    click.option(
        "--host-url",
        default="https://sentry.io",
        help="The host URL for the sentry service.",
    ),
    click.option(
        "--org",
        envvar="QSENTRY_ORG_SLUG",
        help="The organization slug.",
    ),
]


def add_common_options(options):
    def _add_common_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_common_options


@click.group(invoke_without_command=True)
def main(*args, **kwargs):
    pass


@main.command()
@add_common_options(common_options)
@click.option(
    "--team",
    envvar="QSENTRY_TEAM_SLUG",
    help="The team slug.",
)
def list_admins(**kwargs):
    for member in SentryApi(
        kwargs["host_url"], kwargs["auth_token"]
    ).filter_by_role_name(
        org_slug=kwargs["org"],
        team_slug=kwargs["team"],
        role_name="admin",
        attributes=["id", "name", "email"],
    ):
        print(f"{member['id']}, {member['name']}, {member['email']}")


if __name__ == "__main__":
    main()
