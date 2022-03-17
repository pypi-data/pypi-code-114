"""
`embedops_authorization`
=======================================================================
Managing the user login functions
* Author(s): Bailey Steinfadt
"""
import os
import base64
import pathlib
import webbrowser
from time import sleep
import requests
import dotenv
import click
from dynaconf import Dynaconf
from dynaconf.loaders import toml_loader
from embedops_cli.api.configuration import Configuration
from embedops_cli.api.rest import ApiException
from embedops_cli.api.api_client import ApiClient
from embedops_cli.eo_types import LoginFailureException, UnauthorizedUserException
from embedops_cli.api.default_api import DefaultApi


user_secrets = os.path.join(os.path.expanduser("~"), ".eosecrets.toml")


def get_auth_token(secrets_file=user_secrets) -> str:
    """Retrieve the Auth0 token from user secrets"""
    key = None
    if not os.path.exists(secrets_file):
        return key
    settings = Dynaconf(SETTINGS_FILES=[secrets_file])
    try:
        key = settings.EMBEDOPS_AUTH_TOKEN
    except AttributeError:
        # eat the attribute error because it's expected when the user has not logged in
        pass
    return key


def set_auth_token(auth_token: str, secrets_file=user_secrets):
    """Set the Auth0 token in user secrets"""
    try:
        toml_loader.write(secrets_file, {"EMBEDOPS_AUTH_TOKEN": auth_token}, merge=True)
    except (IOError) as exc:
        raise LoginFailureException from exc


def fetch_registry_token() -> str:
    """Retrieve a GitLab token for the user's group and store it"""
    user_client = get_user_client()

    user = user_client.get_my_user()
    if len(user.groups) < 1:
        raise UnauthorizedUserException

    first_group_membership = user.groups[0]
    org_id = first_group_membership.group.org_id

    token_record = user_client.get_gitlab_access_token_for_org(org_id)
    registry_token = token_record.token.token
    set_registry_token(registry_token)


def get_registry_token(secrets_file=user_secrets):
    """Retrieve the Auth0 token from user secrets"""
    if not os.path.exists(secrets_file):
        raise UnauthorizedUserException
    settings = Dynaconf(SETTINGS_FILES=[secrets_file])
    try:
        registry_token = settings.EMBEDOPS_GL_TOKEN
    except AttributeError as exc:
        raise UnauthorizedUserException from exc
    if not registry_token:
        raise UnauthorizedUserException
    return registry_token


def set_registry_token(gitlab_token: str, secrets_file=user_secrets):
    """Set the GitLab/EmbedOps registry access token in user secrets"""
    try:
        toml_loader.write(secrets_file, {"EMBEDOPS_GL_TOKEN": gitlab_token}, merge=True)

    except (IOError) as exc:
        raise LoginFailureException from exc


def auth0_url_encode(byte_data):
    """
    Safe encoding handles + and /, and also replace = with nothing
    :param byte_data:
    :return:
    """
    return base64.urlsafe_b64encode(byte_data).decode("utf-8").replace("=", "")


def request_authorization():  # pylint: disable=too-many-locals
    """start the routine for the user to authenticate with Auth0"""

    ############## Setup request bits ################
    env_path = pathlib.Path(".") / ".env"
    dotenv.load_dotenv(dotenv_path=env_path)

    # TODO: we'll need to set this to where the .env are stored in the application
    # FIXMEEEEEEE
    client_id = "6Sm3VSVQ15B9IxTFKmwrjcPzXaH0oC1P"
    base_url = "https://embedops-dev.us.auth0.com/oauth"

    code_obj = request_user_code(client_id, base_url)

    # Request the user code and verification url, show instructions to user
    user_code = code_obj["user_code"]
    show_login_instructions(user_code)

    # Open the browser window to the login url
    # Start the server and poll until the callback has been invoked
    verification_url = code_obj["verification_uri_complete"]
    device_code = code_obj["device_code"]

    return launch_login_url(verification_url, base_url, device_code, client_id)


def request_user_code(client_id, base_url):
    """Request the code to show to the user"""
    # We generate a nonce (state) that is used to protect against attackers invoking the callback
    data = {
        "audience": "https://app-dev.embedops.com",
        "scope": "openid email profile offline_access",
        "client_id": client_id,
    }
    url = f"{base_url}/device/code"

    code_req_response = requests.post(url, data=data)
    return code_req_response.json()


def show_login_instructions(user_code):
    """Printing some pretty instrcutions for the user while logging in"""
    click.secho("\n")
    click.secho("    ****************************", fg="magenta")
    click.secho("     *** ", nl=False, fg="magenta")
    click.secho("Check your browser", nl=False, fg="cyan")
    click.secho(" ***", fg="magenta")

    click.secho("        *** ", nl=False, fg="magenta")
    click.secho("for this code ", nl=False, fg="cyan")
    click.secho("***", fg="magenta")
    click.secho(f"          >> {user_code} <<", fg="bright_red")
    click.secho("           **+++++++++**", fg="magenta")


def launch_login_url(verification_url, base_url, device_code, client_id):
    """Launch the url for the user to log into EmbedOps"""
    webbrowser.open_new(verification_url)

    click.secho(f"\nPossibly polling FOREVER for verification:\n")
    verified = False
    while not verified:
        url = f"{base_url}/token"
        token_data = {
            "device_code": device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "client_id": client_id,
        }
        token_resp = None
        token_record = None
        try:
            token_resp = requests.post(url, data=token_data)
        except RuntimeError as exc:
            raise LoginFailureException from exc

        if token_resp:
            token_record = token_resp.json()
            click.secho("\n")
            break
        click.secho(".", nl=False, fg="bright_green")
        sleep(0.1)

    return token_record["access_token"]


def check_token():
    """Check whether the token received is good or not"""
    user = None
    user_client = get_user_client()
    try:
        user = user_client.get_my_user()
    except (ValueError, TypeError, ApiException):
        return False

    return user is not None


def get_user_client():
    """Get a client for the embedops API as the currently signed in user"""
    api_host = "http://localhost:7080"
    auth_token = get_auth_token()
    configuration = Configuration()
    configuration.host = f"{api_host}/api/v1"
    configuration.api_key["Authorization"] = auth_token
    configuration.api_key_prefix["Authorization"] = "Bearer"

    api_client = ApiClient(configuration=configuration)

    return DefaultApi(api_client=api_client)


def _get_user_record():

    user_client = get_user_client()
    return user_client.get_my_user()
