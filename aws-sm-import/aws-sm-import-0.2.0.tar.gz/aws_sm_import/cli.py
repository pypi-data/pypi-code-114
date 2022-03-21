import json

import yaml
from dotenv import dotenv_values

import click as click
import boto3


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def load_env(path):
    return dotenv_values(path)


def load_json(path):
    with open(path) as f:
        return json.load(f)


@click.command()
@click.option("--append-only", is_flag=True, default=False)
@click.option("--create", is_flag=True, default=True)
@click.option("--kms-key")
@click.argument("secret")
@click.argument("path", type=click.Path())
def cli(secret, path, append_only, kms_key, create):
    if path.endswith(".env"):
        vars = load_env(path)
    elif path.endswith(".json"):
        vars = load_json(path)
    elif path.endswith(".yaml") or path.endswith(".yml"):
        vars = load_yaml(path)
    else:
        click.secho(f"Unknown input format", fg="red")
        raise click.Abort()

    sm = boto3.client("secretsmanager")

    try:
        response = sm.describe_secret(SecretId=secret,)
    except sm.exceptions.ResourceNotFoundException as e:
        if not create:
            click.secho(f"Abort. Missing secret.", fg="red")
            raise click.Abort()

        params = dict(Name=secret, SecretString=json.dumps(vars))

        if kms_key:
            params["KmsKeyId"] = kms_key

        sm.create_secret(**params)
        click.secho(f"Secret {secret} has been created.", fg="green")

    try:
        secrets = json.loads(sm.get_secret_value(SecretId=secret,).get("SecretString"))
    except sm.exceptions.ResourceNotFoundException as e:
        secrets = {}

    updates = 0

    if append_only:
        for k, v in {k: v for k, v in vars.items() if k not in secrets}.items():
            updates += 1
            secrets[k] = v

        if not updates:
            click.secho(f"No new entries. Skipping import.", fg="blue")
            return
    else:
        secrets = vars

    params = dict(SecretId=secret, SecretString=json.dumps(secrets))
    if kms_key:
        params["KmsKeyId"] = kms_key

    sm.update_secret(**params)

    click.secho(f"Secret {secret} has been updated.", fg="green")
