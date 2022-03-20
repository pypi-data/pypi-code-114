#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('requirements/test.txt') as f:
    test_requirements = f.readlines()

setup(
    author='Mitchell Lisle',
    author_email='m.lisle90@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description='A data engineering utility library for siphoning data around',
    entry_points={
        'console_scripts': [
            'siphon=siphon.cli:main',
        ],
    },
    install_requires=requirements,
    license='GNU General Public License v3',
    include_package_data=True,
    keywords='siphon',
    name='siphon-data',
    packages=find_packages(include=['siphon', 'siphon.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mitchelllisle/siphon',
    version='0.6.1',
    zip_safe=False,
)
