import click
import re
from sentry_sdk import set_user

from ocean import api, code, utils
from ocean.main import pass_env
from ocean.utils import sprint, PrintType, print_ocean_logo


@click.group(cls=utils.AliasedGroup)
def cli():
    print_ocean_logo()
    pass


@cli.command()
@pass_env
def login(ctx):
    sprint(f"Login to '{ctx.get_url()}'")

    email = click.prompt("Email")
    password = click.prompt("Password", hide_input=True)

    res = api.post(ctx, code.API_SIGNIN, {code.EMAIL: email, code.PASSWORD: password})

    if res.status_code == 200:
        body = res.json()
        ctx.update_config(code.TOKEN, body.get(code.TOKEN))
        ctx.update_config("username", body.get("user").get(code.EMAIL).split("@")[0])
        ctx.update_config(code.EMAIL, body.get("user").get(code.EMAIL))
        set_user({"email": email})
        sprint("Login Success.", PrintType.SUCCESS)
    else:
        sprint("Login Failed.", PrintType.Failed)


@cli.command()
@pass_env
def logout(ctx):
    ctx.update_config(code.TOKEN, "")
    sprint("Logout Success.", PrintType.SUCCESS)


@cli.command()
@pass_env
def register(ctx):
    email_regex = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    password_regex = (
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@!#%*?&])[A-Za-z\d$@$!#%*?&]{8,}$"
    )

    email = click.prompt("Email")
    while not re.search(email_regex, email):
        sprint("Email is not valid.", PrintType.FAILED)
        email = click.prompt("Email")

    password1 = click.prompt("Password", hide_input=True)
    while not re.search(password_regex, password1):
        sprint(
            "Password is not valid. Please enter at least one alphabet uppercase, lower case, number and special character.",
            PrintType.FAILED,
        )
        password1 = click.prompt("Password", hide_input=True)
    password2 = click.prompt("Re-enter Password", hide_input=True)
    while password1 != password2:
        sprint("Password is not same. Please re-enter password.", PrintType.FAILED)
        password2 = click.prompt("Re-enter Password", hide_input=True)

    username = click.prompt("User name")
    while len(username) < 3:
        sprint("User name is at least 3 characters.", PrintType.FAILED)
        username = click.prompt("User name")

    res = api.post(
        ctx,
        code.API_SIGNUP,
        {
            code.EMAIL: email,
            code.PASSWORD1: password1,
            code.PASSWORD2: password2,
            code.USERNAME: username,
        },
    )
    if res.status_code == 201:
        sprint("Register Success.", PrintType.SUCCESS)
    else:
        sprint("Register Failed.", PrintType.FAILED)
