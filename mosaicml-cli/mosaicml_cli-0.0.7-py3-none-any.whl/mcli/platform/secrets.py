""" Create Secrets """
import argparse
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Union

from mcli.cli.m_create.create_secret import configure_secret_argparser, create_secret_helptext
from mcli.config import MCLIConfig
from mcli.config_objects.mcli_secret import (SECRET_CLASS_MAP, MCLIDockerRegistrySecret, MCLIGenericEnvironmentSecret,
                                             MCLIGenericMountedSecret, MCLIGenericSecret, MCLIPlatform, MCLIS3Secret,
                                             MCLISecret, MCLISSHSecret, SecretType)
from mcli.utils.utils_interactive import list_options, query_yes_no
from mcli.utils.utils_kube import list_secrets
from mcli.utils.utils_kube_labels import label
from mcli.utils.utils_string_validation import (validate_secret_key, validate_secret_name,
                                                validate_simple_absolute_directory, validate_simple_absolute_filename)

_secret_default_prompt_options = {
    'allow_custom_response': True,
    'options': [],
    'pre_helptext': None,
}


class ExistingSecret(NamedTuple):
    name: str
    is_mcli: bool


def get_existing_platform_secrets(platform: MCLIPlatform,
                                  secret_name: str) -> Tuple[List[str], Optional[ExistingSecret]]:
    """Gets a list of existing secrets from the specified platform. If `secret_name` is in the list, also returns a
    tuple of secret_name and whether it is an `mcli` created secret.

    Args:
        platform: Platform to check for secrets
        secret_name: Name fo the secret

    Returns:
        Tuple of:
        List of secret names
        ExistingSecret or None: Tuple of secret name and True if it was created by `mcli`
            If the secret does not exist, then None is returned.
    """

    with MCLIPlatform.use(platform):
        secret_list: List[Dict[str, Any]] = list_secrets(platform.namespace)['items']

        existing_names = []
        existing_secret = None
        for secret in secret_list:
            name = secret['metadata']['name']
            existing_names.append(name)
            if name != secret_name:
                continue

            is_mcli = label.mosaic.MCLI_VERSION in secret['metadata'].get('labels', {})
            existing_secret = ExistingSecret(secret_name, is_mcli)

    return existing_names, existing_secret


def create_new_secret(
    secret_type: Optional[Union[str, SecretType]] = None,
    secret_name: Optional[str] = None,
    **kwargs,
) -> int:

    def print_secret_parser_usage() -> None:
        parser = argparse.ArgumentParser()
        configure_secret_argparser(parser, secret_handler=lambda _: 1)
        parser.print_usage()

    if secret_type is None and secret_name is None:
        print('Missing required positional arguments')
        print_secret_parser_usage()
        print(create_secret_helptext)
        return 1
    assert secret_type is not None
    secret_type = SecretType.ensure_enum(secret_type)

    conf = MCLIConfig.load_config()
    if not conf.platforms:
        print('No platforms found. You must have at least one platform setup before you add secrets. '
              'Please try running `mcli create platform` first to generate one.')
        return 1
    ref_platform = conf.platforms[0]

    existing_secrets = conf.secrets
    if secret_name is None:
        secret_name = list_options(
            input_text='Unique Secret Name',
            helptext='Secret Name',
            validate=validate_secret_name,
            **_secret_default_prompt_options,
        )
    assert secret_name is not None

    if not validate_secret_name(secret_name):
        return 1

    if secret_name in {x.name for x in existing_secrets}:
        print(
            f'Secret Name: {secret_name} already taken.'
            ' Please choose a unique Secret Name. ',
            ' To see all env variables `mcli get secrets`',
        )
        print_secret_parser_usage()
        return 1

    try_import = False
    existing_kube_secrets, existing_secret = get_existing_platform_secrets(ref_platform, secret_name)
    if existing_secret:
        print(f'Secret named {secret_name} already exists in platform {ref_platform.name}')
        if existing_secret.is_mcli:
            try_import = query_yes_no(f'Would you like to try to import the secret from platform {ref_platform.name}?')
            if try_import:
                pulled_secret = _pull_from_k8s(ref_platform, secret_name, secret_type)
                kwargs.update(pulled_secret)
            else:
                print(f'A secret named {secret_name} already exists.'
                      f' Please choose a name not in {existing_kube_secrets}.')
                return 1
        else:
            print(f'A secret named {secret_name} already exists but is not an `mcli` created secret.'
                  f' Please choose a name not in {existing_kube_secrets}.')
            return 1

    generated_secret: Optional[MCLISecret] = None
    if secret_type == SecretType.docker_registry:
        generated_secret = _create_docker_registry_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.generic_mounted:
        generated_secret = _create_generic_mounted_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.generic_environment:
        generated_secret = _create_generic_environment_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.ssh:
        generated_secret = _create_ssh_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.s3_credentials:
        generated_secret = _create_s3_secret(secret_name=secret_name, **kwargs)
    else:
        raise NotImplementedError(f'The secret type: {secret_type} is not implemented yet')
    assert generated_secret is not None
    print(generated_secret)
    conf.secrets.append(generated_secret)
    conf.save_config()

    # Sync to all known platforms
    for platform in conf.platforms:
        generated_secret.sync_to_platform(platform)

    return 0


def _pull_from_k8s(platform: MCLIPlatform, secret_name: str, secret_type: SecretType) -> Dict[str, Any]:

    secret_class = SECRET_CLASS_MAP.get(secret_type)
    if not secret_class:
        raise NotImplementedError(f'The secret type: {secret_type} is not implemented yet')

    generated_secret = secret_class(secret_name, secret_type)
    generated_secret.pull(platform)

    secret_dict = {key: value for key, value in asdict(generated_secret).items() if key not in ('name', 'secret_type')}
    return secret_dict


def _create_docker_registry_secret(
    secret_name: str,
    docker_username: Optional[str] = None,
    docker_password: Optional[str] = None,
    docker_email: Optional[str] = None,
    docker_server: Optional[str] = None,
    **kwargs,
) -> MCLISecret:
    del kwargs

    if docker_username is None:
        docker_username = list_options(
            input_text='Docker Username',
            helptext='DockerID',
            **_secret_default_prompt_options,
        )
    if docker_password is None:
        docker_password = list_options(
            input_text='Docker Password',
            helptext='Docker Access Token in Security',
            **_secret_default_prompt_options,
        )
    if docker_email is None:
        docker_email = list_options(
            input_text='Docker Email',
            helptext='Email associated with DockerID',
            **_secret_default_prompt_options,
        )

    if docker_server is None:
        docker_server = list_options(
            input_text='Docker Server',
            default_response='https://index.docker.io/v1/',
            helptext='Server location for the registry',
            **_secret_default_prompt_options,
        )

    assert docker_username is not None
    assert docker_password is not None
    assert docker_email is not None

    docker_secret = MCLIDockerRegistrySecret(
        name=secret_name,
        secret_type=SecretType.docker_registry,
        docker_username=docker_username,
        docker_password=docker_password,
        docker_email=docker_email,
        docker_server=docker_server,
    )
    return docker_secret


def _create_generic_secret(
    secret_name: str,
    value: Optional[str] = None,
    **kwargs,
) -> MCLIGenericSecret:
    del kwargs
    secret_value = value

    if secret_value is None:
        secret_value = list_options(
            input_text='Secret Value',
            helptext='Secret Data',
            **_secret_default_prompt_options,
        )
    assert secret_value is not None

    generic_secret = MCLIGenericSecret(
        name=secret_name,
        secret_type=SecretType.generic,
        value=secret_value,
    )
    return generic_secret


def _create_generic_mounted_secret(
    secret_name: str,
    value: Optional[str] = None,
    mount_path: Optional[str] = None,
    **kwargs,
) -> MCLIGenericMountedSecret:
    del kwargs

    generic_secret = _create_generic_secret(
        secret_name=secret_name,
        value=value,
    )

    if mount_path is None:
        mount_path = list_options(
            input_text='Mount Path For Secret',
            helptext='Mount Path',
            validate=validate_simple_absolute_filename,
            **_secret_default_prompt_options,
        )
    assert mount_path is not None
    #TODO(HEK339): Ensure mount_path parent folder is not used by any other secrets

    return MCLIGenericMountedSecret.from_generic_secret(
        generic_secret=generic_secret,
        mount_path=mount_path,
    )


def _create_generic_environment_secret(
    secret_name: str,
    value: Optional[str] = None,
    env_key: Optional[str] = None,
    **kwargs,
) -> MCLIGenericEnvironmentSecret:
    del kwargs

    generic_secret = _create_generic_secret(
        secret_name=secret_name,
        value=value,
    )

    if env_key is None:
        env_key = list_options(
            input_text='Environment Key to use, KEY in KEY=VALUE',
            helptext='Environment Key',
            validate=validate_secret_key,
            **_secret_default_prompt_options,
        )
    assert env_key is not None

    return MCLIGenericEnvironmentSecret.from_generic_secret(
        generic_secret=generic_secret,
        env_key=env_key,
    )


def _create_ssh_secret(
    secret_name: str,
    ssh_private_key_path: Optional[str] = None,
    mount_path: Optional[str] = None,
    **kwargs,
) -> MCLISSHSecret:
    del kwargs

    if ssh_private_key_path is None:
        ssh_private_key_path = list_options(
            input_text='SSH private key',
            helptext='Path to your private SSH key',
            validate=validate_simple_absolute_filename,
            **_secret_default_prompt_options,
        )
    assert ssh_private_key_path is not None

    if mount_path is None:
        mount_path = list_options(
            input_text='Mount Path',
            helptext='Mount path for private SSH key within container',
            validate=validate_simple_absolute_filename,
            **_secret_default_prompt_options,
        )
    assert mount_path is not None
    #TODO(HEK339): Ensure mount_path parent folder is not used by any other secrets

    # Attempt to read key
    with open(ssh_private_key_path, 'r', encoding='utf8') as fh:
        ssh_private_key: str = fh.read()

    return MCLISSHSecret(
        name=secret_name,
        secret_type=SecretType.ssh,
        mount_path=mount_path,
        value=ssh_private_key,
    )


def _create_s3_secret(
    secret_name: str,
    credentials_file: Optional[str] = None,
    config_file: Optional[str] = None,
    mount_directory: Optional[str] = None,
    **kwargs,
) -> MCLIS3Secret:
    del kwargs

    if credentials_file is None:
        credentials_file = list_options(
            input_text='Credentials file path',
            helptext='Path to your S3 credentials file',
            default_response=str(Path('~/.aws/credentials').expanduser()),
            **_secret_default_prompt_options,
        )

    if config_file is None:
        config_file = list_options(
            input_text='Config file path',
            helptext='Path to your S3 config file',
            default_response=str(Path('~/.aws/config').expanduser()),
            **_secret_default_prompt_options,
        )

    if mount_directory is None:
        mount_directory = list_options(
            input_text='Mount Directory',
            helptext='Mount directory for the AWS Credentials within container',
            validate=validate_simple_absolute_directory,
            **_secret_default_prompt_options,
        )
    assert mount_directory is not None
    if mount_directory[-1] != '/':
        mount_directory += '/'

    assert credentials_file is not None
    assert config_file is not None

    with open(credentials_file, 'r', encoding='utf8') as fh:
        credentials = fh.read()

    with open(config_file, 'r', encoding='utf8') as fh:
        config_ = fh.read()

    return MCLIS3Secret(
        name=secret_name,
        secret_type=SecretType.s3_credentials,
        credentials=credentials,
        mount_directory=mount_directory,
        config=config_,
    )
