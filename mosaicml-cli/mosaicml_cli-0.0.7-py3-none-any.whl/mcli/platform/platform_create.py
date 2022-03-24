""" mcli create Platform Entrypoint """
from kubernetes.config.config_exception import ConfigException

from mcli.config import MCLIConfig
from mcli.config_objects import MCLIPlatform
from mcli.platform.platform_info import get_platform_list
from mcli.utils.utils_interactive import list_options
from mcli.utils.utils_kube import KubeContext, get_kube_contexts
from mcli.utils.utils_string_validation import validate_rfc1123_name


def create_new_platform(**kwargs) -> int:
    del kwargs

    platform_list = get_platform_list()
    platform_clusters = [x.kubernetes_context for x in platform_list]
    platform_names = [x.name for x in platform_list]
    platform_names_string = ', '.join(platform_names) if platform_list else 'None'
    print(f'Existing Platforms: {platform_names_string}\n')

    try:
        kube_contexts = get_kube_contexts()
    except ConfigException as e:
        raise ConfigException('Could not find a valid kubeconfig file. If you think this is wrong, double-check your '
                              '`$KUBECONFIG` environment variable.') from e

    unregistered_contexts = [x for x in kube_contexts if x.cluster not in platform_clusters]
    if not unregistered_contexts:
        raise RuntimeError('All platforms from your kubeconfig file have already been added.')

    def print_kube_context(kc: KubeContext) -> str:
        return kc.cluster

    new_context = list_options(
        input_text='Which Platform would you like to set up?',
        options=unregistered_contexts,
        default_response=unregistered_contexts[0],
        pre_helptext='Select the platform to set up ',
        helptext=f'default ({print_kube_context( unregistered_contexts[0] )})',
        print_option=(print_kube_context),
    )
    print('Received a value for new_context')
    shortname = new_context.cluster.split('-')[0]

    def validate_platform(x: str):
        if x in platform_names:
            print(f'{x} already choosen, please name it something different')
            return False
        return True

    platform_name = list_options(
        input_text='Choose a platform shortname',
        options=[shortname],
        default_response=shortname,
        pre_helptext=' ',
        allow_custom_response=True,
        validate=validate_platform,
    )

    namespace = list_options(
        input_text='Select your namespace',
        options=[new_context.namespace],
        default_response=new_context.namespace,
        pre_helptext=' ',
        allow_custom_response=True,
        validate=lambda x: bool(validate_rfc1123_name(x)) if x else False,
    )
    assert namespace is not None

    new_platform = MCLIPlatform(
        name=platform_name,
        kubernetes_context=new_context.cluster,
        namespace=namespace,
    )

    config = MCLIConfig.load_config()
    config.platforms.append(new_platform)
    config.save_config()

    # Sync all secrets
    for secret in config.secrets:
        secret.pull(config.platforms[0])  # Pulls secret data into memory
        secret.sync_to_platform(new_platform)

    return 0
