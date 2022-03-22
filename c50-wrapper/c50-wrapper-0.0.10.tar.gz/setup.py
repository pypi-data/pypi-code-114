# -*- coding: utf-8 -*-
"""
setup.py
------------
c50 wrapper setup script.
"""
from setuptools import setup, find_packages
# builds the project dependency list
install_requires = None
with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()
    install_requires = list(
        map(
            lambda x: x.replace('==', '>=').replace('\\','').strip(),
            filter(
                lambda x: not x.strip().startswith('--hash=') and not x.strip().startswith('# via -r'),
                install_requires
            )
        )
    )

# setup function call
setup(
    name="c50-wrapper",
    version="0.0.10",
    author="Luis Felipe Muller",
    author_email="luisfmuller@gmail.com",
    description=(
        "A python wrapper fot the C5.0 algorithm that works on linux applications; " 
        "With the wrapper developers can train decision tree models in pure python and pandas;"
    ),
    keywords=["Decision Tree", "C5.0", "Machine Learning"],
    # Install project dependencies
    install_requires=install_requires,

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md', "*.json", '*.zip', '../bin/c5.0', '../bin/report'],
    },
    include_package_data=True,
    packages=find_packages(exclude=["*tests"]),
)
