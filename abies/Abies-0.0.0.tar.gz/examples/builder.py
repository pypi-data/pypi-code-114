#!/usr/bin/env python3
""" Plugin builder. """
from pathlib import Path
import os
import shutil
import abies
from abies import builder
from abies import templates

from cookiecutter.main import cookiecutter

from contextlib import contextmanager

tmp_dir = Path("_tmp")


@contextmanager
def cleanup_project(prj_dir: Path):

    orig = Path()
    try:
        # Delete the original dir and start over.
        if prj_dir.exists():
            shutil.rmtree(prj_dir)
        os.chdir(prj_dir.parent)
        yield
    finally:
        os.chdir(orig)


if __name__ == "__main__":

    prj_name = "some_module"
    prj_dir = tmp_dir / prj_name

    os.makedirs(tmp_dir, exist_ok=True)

    config = templates.TemplateConfig(prj_name)

    # print(abies.get_cmake_dir())

    abies_cmake_path = Path(abies.get_cmake_dir())

    with cleanup_project(prj_dir):
        templates.create_from_template("plugin_basic", config)
