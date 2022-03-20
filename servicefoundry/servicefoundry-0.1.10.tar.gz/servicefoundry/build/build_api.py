import os

from .const import SERVICE_DEF_FILE_NAME
from .package.packaging_factory import package
from .session import ServiceFoundrySession
from .session_factory import get_session
from .parser.parser import Parser
from .service_foundry_client import ServiceFoundryServiceClient


def build_and_deploy(env, base_dir="./", service_def_file_name=SERVICE_DEF_FILE_NAME):
    if not base_dir.endswith("/"):
        base_dir = f"{base_dir}/"

    service_def_file_path = f"{base_dir}{service_def_file_name}"
    if not os.path.isfile(service_def_file_path):
        raise RuntimeError(
            f"Service definition {service_def_file_name} doesn't exist in {base_dir}"
        )

    service_def = Parser(base_dir).parse(service_def_file_path)
    package_zip = package(base_dir, service_def.name, service_def.build)

    session = get_session()
    tf_client = ServiceFoundryServiceClient(session)
    return tf_client.build_and_deploy(service_def, package_zip, env)
