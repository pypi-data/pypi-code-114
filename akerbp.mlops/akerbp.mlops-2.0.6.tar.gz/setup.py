"""
setup.py 

Information used to build the package
"""
from turtle import update
from setuptools import find_namespace_packages, setup
import os
import subprocess
from subprocess import check_output


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

ENV = os.environ["ENV"]

def get_current_version(path_to_version_file = "./version.txt"): 
    """Get the current version number that is kept track of in the version.txt file. 
    If the latest version was a pre-release or the package was deployed to test/dev, we 
    remove the pre-release tag from the package version. 

    Args:
        path_to_version_file (str, optional): path to version number file. Defaults to "./version.txt".

    Returns:
        str: version number
    """
    with open(path_to_version_file, "r") as f: 
        version = f.readlines()[0]
    # extract version WITHOUT pre-release label
    if len(pre_release := version.split("-")) > 1: 
        version = pre_release[0]
    return version 

def update_current_version(new_version, path_to_version_file = "./version.txt"):
    """Helper function to update the version number in the version.txt file

    Args:
        new_version (str): incremented version number based on environment and commit message
        path_to_version_file (str, optional): path to version number file. Defaults to "./version.txt".
    """
    with open(path_to_version_file, "r+") as f: 
        f.truncate(0)
        f.write(new_version)

def increment_version(): 
    """Increment version number by specifying type of update in the commit message.
    The function extracts the current version from a text file, examines the latest commit
    and increment the version number based on the content of the commmit message and the environment. 
    The updated version number is then updated in the text file keeping track of the current 
    version of the package.

    The version number is tagged as a pre-release if the package is deployed in a test or dev environment.

    Returns:
        str: new version number
    """
    version = get_current_version()
    if ENV == "prod":
        update_current_version(version)
        return version 
    else:
        # Increment the package version based on the commit message in dev and test, and tag as pre-release
        major, minor, patch = version.split(".")
        commit_msg = check_output(["git", "log", "-1", "--pretty=%B"]).decode("ascii").strip().lower()
        words_in_commit_msg = commit_msg.split()

        # Remove special characters from commit message
        for i, word in enumerate(words_in_commit_msg):
            if word == "pre-release" or word == "pre-release:":
                continue
            alphanumeric = [char for char in word if char.isalnum()]
            word = "".join(alphanumeric)
            words_in_commit_msg[i] = word
    
        # Increment version based on commit message
        if "major" in words_in_commit_msg:
            major = int(major) + 1
            minor, patch = 0, 0
        elif "minor" in words_in_commit_msg:
            minor = int(minor) + 1
            patch = 0
        else:
            patch = int(patch) + 1

        new_version = f"{major}.{minor}.{patch}"
        # Tag version number with pre-release
        new_version += "-alpha"
        
        # Update with pre-relase label in version file, as these are used in install.sh
        update_current_version(new_version)

        return new_version

setup(
    name="akerbp.mlops", 
    version=increment_version(),
    author="Alfonso M. Canterla",
    author_email="alfonso.canterla@soprasteria.com",
    maintainer="Christian N. Lehre",
    maintainer_email="christian.lehre@soprasteria.com",
    description="MLOps framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/akerbp/akerbp.mlops/",
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "cognite-sdk-experimental>=0.69.0",
        "pytest>=6.1.1",
        "pydantic>=1.7.3",
        "PyYAML==5.4.1"
    ],
    scripts=[
        'src/akerbp/mlops/deployment/deploy_training_service.sh', 
        'src/akerbp/mlops/deployment/deploy_prediction_service.sh',
        'src/akerbp/mlops/gc/install_gc_sdk.sh'
    ],
    include_package_data=True,
    package_data={'': [
        'mlops/gc/Dockerfile', 
        'mlops/gc/requirements.app',
        'mlops/gc/install_req_file.sh',
        'mlops/deployment/bitbucket-pipelines.yml' 
        ]},
)