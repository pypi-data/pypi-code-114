#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jens Neuhaus",
    author_email='hey@automagically.cloud',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Automagically Client / SDK",
    entry_points={
        'console_scripts': [
            'automagically=automagically.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='automagically',
    name='automagically',
    packages=find_packages(include=['automagically', 'automagically.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/automagically-cloud/python-client',
    version='0.1.1',
    zip_safe=False,
)
