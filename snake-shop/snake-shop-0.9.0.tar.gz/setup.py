#!/usr/bin/env python
import os
from pathlib import Path
from setuptools import find_packages, setup


def get_version():
    path = Path(str(Path(__file__).parent) + os.sep + 'VERSION')
    if path.is_file():
        with open(path) as f:
            return f.read().strip()
    return '0.0.0'


install_requires = [
    'django>=2.2,<3.3',
]

tests_require = [
]

setup(
    name='snake-shop',
    version=get_version(),
    author="Snake-Soft",
    author_email="info@snake-soft.com",
    description="Online-Shop",
    url='https://www.snake-soft.com/',
    #long_description=open('README.rst').read(),
    license='GPL3',
    package_dir={'': '.'},
    packages=find_packages(),
    #package_data={
    #    'templates': ['*'],
    #},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
)
