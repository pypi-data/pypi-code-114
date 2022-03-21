# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import re

import setuptools

VERSIONFILE = "availsim4core/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS: dict = {
    'core': [
        'numpy',
        'pandas',
        'datetime',
        'matplotlib',
        'openpyxl',
        'scipy',
        'xlsxwriter',
        'qmcpy',
        'matplotlib',
        'networkx',
        'pygraphviz'
    ],
    'test': [
        'pytest',
        'memory_profiler',
        'Pillow',
        'pytest-cov',
    ],
    'dev': [
        # 'requirement-for-development-purposes-only',
    ],
    'doc': [
        'sphinx',
        'sphinx-glpi-theme',
        'sphinx-autoapi',
        'sphinxcontrib.napoleon',
        'sphinx-autodoc-typehints',
    ],
}

setuptools.setup(
    name="availsim4",
    version=verstr,
    author="TE-MPE",
    author_email="te-dep-mpe-ms@cern.ch",
    license='gpl-3.0',
    description="Availsim4 is a tool to predict reliability and availability "
                "of modern particle accelerators and their related systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.cern.ch/availsim4/availsim4",
    python_requires='>=3.7, <4',
    setup_requires=['wheel'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS['core'],
    extras_require={
        **REQUIREMENTS,
        # The 'dev' extra is the union of 'test' and 'doc', with an option
        # to have explicit development dependencies listed.
        'dev': [req
                for extra in ['dev', 'test', 'doc']
                for req in REQUIREMENTS.get(extra, [])],
        # The 'all' extra is the union of all requirements.
        'all': [req for reqs in REQUIREMENTS.values() for req in reqs],
    },
    packages=setuptools.find_packages(),
    package_data={'availsim4core': ['logging/logging.conf', 'version.txt']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'availsim4=availsim4core.main:main',
        ],
    },
)
