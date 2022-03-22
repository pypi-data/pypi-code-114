# -*- coding: utf-8 -*-

from setuptools import setup
from distutils.util import convert_path


_package_name = 'el_validator'

_namespace_dict = {}
_version_path = convert_path(f'{_package_name}/__version__.py')
with open(_version_path) as _version_file:
    exec(_version_file.read(), _namespace_dict)
_package_version = _namespace_dict['__version__']

setup(
    name = _package_name,
    packages = [_package_name],
    version = f"{_package_version}",
    license='MIT',
    description = 'Cerberus and validator-collection based custom validator python package.',
    long_description = open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author = 'Batkhuu Byambajav',
    author_email = 'batkhuu@ellexi.com',
    url = 'https://bitbucket.org/ellexiinc/el_validator/',
    download_url = f'https://bitbucket.org/ellexiinc/el_validator/get/release-{_package_version}.tar.gz',
    keywords = [_package_name, 'validator', 'validators', 'validate', 'validation', 'data-validation', 'Cerberus', 'validator-collection', 'custom-validator'],
    install_requires = [
            'Cerberus>=1.3.4',
            'pydantic>=1.8.2',
            'importlib-metadata>=4.8.1',
            'el-logging>=0.2.24',
            'jsonschema>=4.0.0',
            'validator-collection>=1.5.0'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
