#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

print(requirements)

setup_requirements = [ ]

test_requirements = [ ]

setup(
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
            'calc20=calc20.calc20:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='calc20',
    name='calc20',
    packages=find_packages(include=['calc20', 'chinadaily.*']),
    setup_requires=requirements,
    version='0.0.2',
    exclude_package_data={'': ["*.xlsx"]},
)
