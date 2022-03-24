import os

DEFAULT_LANGUAGE_VERSION = 8


def get_network_config(network_name):
    return os.path.join(
        os.environ["SYMENV_DIR"],
        f"assembly-dev/mock-network/{network_name}/network-config.json",
    )
