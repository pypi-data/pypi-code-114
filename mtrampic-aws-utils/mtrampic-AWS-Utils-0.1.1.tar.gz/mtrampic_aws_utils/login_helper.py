import datetime
import json
import urllib.parse
from typing import Iterable, no_type_check

import boto3
import requests
import typer


login_helper: typer.Typer = typer.Typer()



def construct_federated_url(
    profile_name: str = None, issuer: str = "RBI-PingFederate", account_id: str = None
) -> str:
    """
    Constructs a URL that gives federated users direct access to the AWS Management
    Console.
    1. Acquires temporary credentials from AWS Security Token Service (AWS STS) that
    can be used to assume a role with limited permissions.
    2. Uses the temporary credentials to request a sign-in token from the
    AWS federation endpoint.
    3. Builds a URL that can be used in a browser to navigate to the AWS federation
    endpoint, includes the sign-in token for authentication, and redirects to
    the AWS Management Console with permissions defined by the role that was
    specified in step 1.
    :param assume_role_arn: The role that specifies the permissions that are granted.
    The current user must have permission to assume the role.
    :param profile_name: The name of the profile for the boto3 session to generate URL.
    :param issuer: The organization that issues the URL.
    :param account_id: AWS Account ID of which we want to jump in for support, pre-generates url.
    :return: The federated URL.
    """
    if profile_name is not None:
        session = boto3.Session(profile_name=profile_name)
        temp_credentials = session.get_credentials().get_frozen_credentials()
        session_data = {
            "sessionId": temp_credentials.access_key,
            "sessionKey": temp_credentials.secret_key,
            "sessionToken": temp_credentials.token,
        }
    elif account_id is not None:
        session = boto3.Session(profile_name="262291017001-Admin")
        sts_c = session.client("sts")
        response = sts_c.assume_role(
            RoleArn="arn:aws:iam::{}:role/AWSCloudFormationStackSetExecutionRole".format(
                account_id
            ),
            RoleSessionName="CCOE-Support",
            DurationSeconds=datetime.timedelta(hours=1).seconds,
        )
        temp_credentials = response["Credentials"]
        session_data = {
            "sessionId": temp_credentials["AccessKeyId"],
            "sessionKey": temp_credentials["SecretAccessKey"],
            "sessionToken": temp_credentials["SessionToken"],
        }
    aws_federated_signin_endpoint = "https://signin.aws.amazon.com/federation"
    # Make a request to the AWS federation endpoint to get a sign-in token.
    # The requests.get function URL-encodes the parameters and builds the query string
    # before making the request.
    response = requests.get(
        aws_federated_signin_endpoint,
        params={
            "Action": "getSigninToken",
            #'SessionDuration': datetime.timedelta(hours=1).seconds,
            "Session": json.dumps(session_data),
        },
    )
    signin_token = json.loads(response.text)
    # Make a federated URL that can be used to sign into the AWS Management Console.
    query_string = urllib.parse.urlencode(
        {
            "Action": "login",
            "Issuer": issuer,
            "Destination": "https://console.aws.amazon.com/",
            "SigninToken": signin_token["SigninToken"],
        }
    )
    federated_url = f"{aws_federated_signin_endpoint}?{query_string}"
    return federated_url
    # snippet-end:[iam.python.construct_federated_url]


def complete_profiles_from_aws_config(incomplete: str) -> Iterable[str]:
    for profile in boto3.session.Session().available_profiles:
        if profile.startswith(incomplete):
            yield (profile)


@no_type_check
@login_helper.command()
def generate_login_url(
    profile: str = typer.Option(
        "262291017001-Admin",
        help="The name to say hi to.",
        autocompletion=complete_profiles_from_aws_config,
    )
) -> str:
    """
    Generate console presigned URL for specific AWS Config profile.
    """
    login_url = construct_federated_url(profile_name=profile)
    typer.echo(login_url)


@no_type_check
@login_helper.command()
def support_account(
    account_id: str = typer.Option(
        "601034470122", help="Account ID where Console Login will be generated for."
    )
) -> str:
    """
    Jump into account via presigned URL for Console, this requires Master IAM Credentials and access to AWSCloudFormationStackSetExecutionRole.
    """
    login_url = construct_federated_url(account_id=account_id)
    typer.echo(login_url)
