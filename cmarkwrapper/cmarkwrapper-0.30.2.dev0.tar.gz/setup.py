
  
from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name='cmarkwrapper',
    install_requires=[
        'cffi >= 1.0.0',
        'paka.cmark==2.3.0',
        'typing-extensions; python_version < "3.8"',
    ],
)