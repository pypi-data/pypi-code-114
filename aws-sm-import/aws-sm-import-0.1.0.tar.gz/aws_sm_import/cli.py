import json

import yaml
from dotenv import dotenv_values

import click as click
import boto3


def load_yaml(path):
    return yaml.safe_load(path)


def load_env(path):
    return dotenv_values(path)


def load_json(path):
    return json.loads(path)


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
    elif path.endswith(".yaml"):
        vars = load_yaml(path)
    else:
        raise click.Abort("Unknown format")

    sm = boto3.client("secretsmanager")

    try:
        response = sm.get_secret_value(SecretId=secret,)

        current = json.loads(response.get("SecretString"))
        updates = 0

        if append_only:
            for k, v in {k: v for k, v in vars.items() if k not in current}.items():
                updates += 1
                current[k] = v

            if not updates:
                click.secho(f"No new entries. Skipping import.", fg="blue")
                return
        else:
            current = vars

        params = dict(SecretId=secret, SecretString=json.dumps(current))
        if kms_key:
            params["KmsKeyId"] = kms_key

        sm.update_secret(**params)

        click.secho(f"Secret {secret} has been updated.", fg="green")

    except sm.exceptions.ResourceNotFoundException as e:
        if not create:
            raise click.Abort("Failed to locate secret")

        params = dict(Name=secret, SecretString=json.dumps(vars))

        if kms_key:
            params["KmsKeyId"] = kms_key

        sm.create_secret(**params)
        click.secho(f"Secret {secret} has been created.", fg="green")
