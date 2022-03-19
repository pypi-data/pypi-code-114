from shutil import copytree, ignore_patterns
from ..util import read_text, create_file_from_content, clean_dir

from jinja2 import Template
import os
from pathlib import Path


def prepare_build_dir(base_dir, build_path, name, service_build):
    clean_dir(build_path)

    # @@TODO Behind the flag
    hidden_dir = f"{base_dir}.servicefoundry"
    clean_dir(hidden_dir)  # Remove symlink

    # Copy contents excluding pattern.
    patterns = None
    if service_build.ignore_patterns:
        patterns = ignore_patterns(*service_build.ignore_patterns)
    copytree(base_dir, build_path, ignore=patterns)
    # Create symlink inside hidden folder for easier debugging

    # @@TODO Behind the flag
    Path(hidden_dir).mkdir(exist_ok=True)
    create_file_from_content(f"{hidden_dir}/.gitignore", "*")
    os.symlink(build_path, f"{hidden_dir}/{name}")


def create_requirements_file(service_auto_build):
    requirement_txt_file = None
    if type(service_auto_build.packages) == str:
        requirement_txt_file = service_auto_build.packages
    return requirement_txt_file


def create_docker_file(build_path, template, **kwargs):
    template = Template(read_text(template))
    docker_file_str = template.render(**kwargs)
    create_file_from_content(f"{build_path}/Dockerfile", docker_file_str)
