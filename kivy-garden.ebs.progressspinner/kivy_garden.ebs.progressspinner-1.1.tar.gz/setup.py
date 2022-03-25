
from setuptools import setup, find_namespace_packages

from io import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

URL = 'https://github.com/ebs-universe/kivy_garden.ebs.progressspinner'

setup(
    name='kivy_garden.ebs.progressspinner',
    author='Kathryn Taylee',
    author_email='kived@github.com',
    maintainer='Chintalagiri Shashank',
    maintainer_email='shashank@chintal.in',
    url=URL,
    packages=find_namespace_packages(include=['kivy_garden.*']),
    include_package_data=True,
    description='Fork of kivy-garden progress spinner',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'kivy>=1.11.1',
    ],
    keywords='Kivy kivy-garden',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    extras_require={
        'dev': ['pytest>=3.6', 'pytest-cov', 'pytest-asyncio',
                'sphinx_rtd_theme'],
        'ci': ['coveralls', 'pycodestyle', 'pydocstyle'],
    },
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
)
