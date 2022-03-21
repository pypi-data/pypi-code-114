#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    'et-xmlfile==1.1.0',
    'openpyxl==3.0.9',
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    version='0.0.4',
    author="Yarving Liu",
    author_email='yarving@qq.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="生成60道20以内数字减法运算题",
    entry_points={
        'console_scripts': [
            'calc20=calc20.main:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='calc20',
    name='calc20',
    packages=find_packages(
        include=['calc20', 'calc20.*']
    ),
    setup_requires=setup_requirements,
    exclude_package_data={'': ["*.xlsx"]},
    zip_safe=False,
)
