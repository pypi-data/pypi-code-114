import os

from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join("mediciasafely", "VERSION")) as f:
    version = f.read().strip()

setup(
    name="mediciasafely",
    version=version,
    packages=find_namespace_packages(exclude=["tests"]),
    include_package_data=True,
    url="https://github.com/mediciaai/mediciasafely-cli",
    description="Command line tool for running MediciaSAFELY studies locally.",
    license="GPLv3",
    author="MediciaSAFELY",
    author_email="frankie@medicia.ai",
    python_requires=">=3.8",
    entry_points={"console_scripts": ["mediciasafely=mediciasafely:main"]},
    classifiers=["License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Homepage": "https://www.medicia.ai",
        "Documentation": "https://docs.opensafely.org",
    },
)
