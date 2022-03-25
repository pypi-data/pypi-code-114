from setuptools import setup
from setuptools import find_namespace_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="nessie-recorder",
    version="1.0.4",
    description="Tools for Nessie Circuit energy harvesting recorder",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Kai Geissdoerfer",
    packages=find_namespace_packages(include=["nessie.*"]),
    license="MIT",
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "click",
        "h5py",
        "pandas",
        "crccheck",
        "matplotlib",
    ],
    tests_require=["pytest"],
    url="https://github.com/geissdoerfer/nessie-recorder-tools",
    entry_points={"console_scripts": ["nessie-recorder=nessie.recorder:cli"]},
)
