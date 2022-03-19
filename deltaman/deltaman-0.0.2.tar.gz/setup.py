#!/usr/bin/env python
import re
from setuptools import setup

proj_name = main_pkg = 'deltaman'
github_url = f"https://github.com/wonderbeyond/{proj_name}"

with open(f'{main_pkg}/__init__.py') as f:
    __version__, = re.findall('__version__: str = "(.*)"', f.read())

with open('README.md') as f:
    long_description = f.read()

setup(
    name=main_pkg,
    version=__version__,
    packages=['deltaman'],

    requires=[],
    install_requires=['lark'],

    package_data={main_pkg: ['*.lark']},

    author="Wonder",
    author_email="wonderbeyond@gmail.com",
    description="Parsing timedelta from human",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    license_files=('LICENSE',),
    keywords="Python human timedelta parsing",
    url=github_url,
    zip_safe=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Documentation': github_url,
        'Source': github_url,
        'Tracker': github_url,
    },
)
