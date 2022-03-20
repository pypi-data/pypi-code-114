"""Some Docstring"""
import os
import codecs

from skbuild import setup
from setuptools import find_packages

from pathlib import Path


def template_files(template_name: str):
    """Get template files"""
    template_dir = Path() / "abies" / "templates"
    template_choice = template_dir / template_name
    tfiles = [p.as_posix() for p in filter(Path.is_file, template_choice.glob("**/*"))]

    return [os.path.relpath(tf, template_dir) for tf in tfiles]


plugin_basic_files = template_files("plugin_basic")


def _read(rel_path: str):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path: str):
    """Parse __version__ from a file."""
    for line in _read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise RuntimeError("Unable to find version string.")


# These are all the libraries that need to be available
abies_library_modules = [
    "vdff",
]


def _lib_pkg_data(lib: str) -> dict[str, list[str]]:
    """List of all package data files in each library module."""
    return ["py.typed", f"_{lib}/__init__.pyi"]


library_modules_pkg_data = {
    f"abies.library.{m}": _lib_pkg_data(m) for m in abies_library_modules
}

setup(
    name="Abies",
    author="Frank Sodari",
    author_email="franksodari@gmail.com",
    version=get_version("abies/__init__.py"),
    url="https://github.com/AbiesDSP/Abies",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "abies.framework": [
            "py.typed",
            "_framework/__init__.pyi",
            "*.h",
            "*.cpp",
            "*.txt",
        ],
        # Include all rtl files in the package.
        "abies.library": [
            "rtl/*.sv",
            "rtl/*.v",
            "rtl/*.vhd",
            "rtl/include/*.svh",
            "rtl/include/.vh",
        ],
        # Include all library data
        **library_modules_pkg_data,
        # Include all templates.
        "abies.templates": plugin_basic_files,
        # AbiesConfig.cmake lets you find the Abies CMake package with find_package.
        "abies.cmake": ["AbiesConfig.cmake"],
    },
    # This is so we can install the .pyd library in the right place.
    cmake_install_dir="abies",
    # Additional packages required by Abies.
    install_requires=["cookiecutter"],
)
