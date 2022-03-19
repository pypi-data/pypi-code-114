import logging

import click

from ..build.auth_service_client import AuthServiceClient
from ..build.const import SESSION_FILE
from ..build.session_factory import DEFAULT_TENANT_ID, get_session

logger = logging.getLogger(__name__)


def get_login_command():
    @click.command(help="Create servicefoundry login")
    def login():
        session = get_session()

        if session:
            click.echo("Already loggedIn.")
        else:
            auth_client = AuthServiceClient()
            url, user_code, device_code = auth_client.get_device_code(DEFAULT_TENANT_ID)

            click.echo(f"Login Code: {user_code}")
            click.echo(
                f"Waiting for your authentication. Go to url to complete the authentication: {url}"
            )

            session = auth_client.poll_for_auth(DEFAULT_TENANT_ID, device_code)
            session.save_session()

            click.echo(
                f"Successful Login. Session file will be stored at {SESSION_FILE}."
            )

    return login
