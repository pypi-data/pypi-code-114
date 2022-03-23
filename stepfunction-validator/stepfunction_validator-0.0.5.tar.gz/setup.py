from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

DESCRIPTION = 'YAML validator for the CLI'
LONG_DESCRIPTION = 'A package that allows to validate a YAML file against the schema you provided in the CLI.'

# Setting up
setup(
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description
)