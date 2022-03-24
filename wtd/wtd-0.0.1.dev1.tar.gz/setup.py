#!/usr/bin/env python3
"""Package build script."""
import json
import os
from setuptools import setup, find_packages
from typing import List, Tuple

import wtd as package

LOCK_FILE = 'Pipfile.lock'
README_FILE = 'README.md'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ABOUT_FILE = os.path.join(BASE_DIR, package.__name__, '__version__.py')


def parse_requirements(lock_fpath: str) -> Tuple[List[str], List[str]]:
    """Parse requirements and test requirements from a given Pipfile.lock.

    :returns: Requirements and test requirements usable by setup function.
    :rtype:   tuple[list[str], list[str]]
    """
    with open(lock_fpath) as lock_file:
        lock_deps = json.load(lock_file)

    return (
        ['%s%s' % (k, v['version']) for k, v in lock_deps['default'].items()],
        ['%s%s' % (k, v['version']) for k, v in lock_deps['develop'].items()]
    )


def main():
    """Set up the package."""
    # Load README.md file content
    with open(README_FILE) as readme_file:
        readme = readme_file.read()

    # Parse out requirements from Pipfile.lock
    requirements, test_requirements = parse_requirements(LOCK_FILE)

    # Setup the package
    setup(
        name=package.__title__,
        version=str(package.__version__),
        license=package.__license__,

        description=package.__description__,
        long_description=readme,
        long_description_content_type='text/markdown',

        author=package.__author__,
        author_email=package.__author_email__,
        url=package.__home_url__,

        packages=find_packages(),
        package_data={'': ['CHANGELOG.md']},

        python_requires='>=3.7',
        install_requires=requirements,
        tests_require=test_requirements,

        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Topic :: Utilities'
        ],

        project_urls={
            'Documentation': package.__docs_url__,
            'Source': package.__source_url__
        }
    )


if __name__ == '__main__':
    main()
