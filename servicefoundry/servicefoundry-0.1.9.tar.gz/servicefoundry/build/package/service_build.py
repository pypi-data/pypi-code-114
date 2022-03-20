# from depfoundry.dependency_generator import RequirementsGenerator, find_local_py_modules
# from depfoundry.depfoundry import build_dependency

from .util import prepare_build_dir, create_requirements_file, create_docker_file

from ..service_def import ServiceBuild

import logging

import tarfile
import os.path


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


logger = logging.getLogger()


def package(base_dir, name, service_build: ServiceBuild):
    build_path = f"{service_build.build_dir}/{name}/build"
    prepare_build_dir(base_dir, build_path, name, service_build)

    requirement_txt_file = create_requirements_file(service_build)

    if service_build.service_type == "fast_api_build":
        template_file = "package/docker_template/python_fastapi.j2"
    elif service_build.service_type == "streamlit_build":
        template_file = "package/docker_template/python_streamlit.j2"

    # @TODO proper check extension.
    module_name = service_build.service.split(".")[0]

    create_docker_file(
        build_path,
        template_file,
        python_version=service_build.version,
        requirement_txt_file=requirement_txt_file,
        port=service_build.port,
        service=module_name,
    )

    make_tarfile(f"{build_path}.tar.gz", build_path)
    return f"{build_path}.tar.gz"
