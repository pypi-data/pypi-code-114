import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="env_set",
    version="0.0.1",
    author="Felix Orinda",
    author_email="forinda82@gmail.com.com",
    description="A small example package",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/forinda/env_set",
    project_urls={
        "Bug Tracker": "https://github.com/forinda/env_set/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "env_set"},
    packages=find_packages(where="env_set"),
    python_requires=">=3.5",
)