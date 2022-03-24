# coding: utf-8
from __future__ import absolute_import
from setuptools import setup, find_packages

__author__ = 'damirazo <me@damirazo.ru>'


setup(
    name='creadoc',
    version='0.0.8',
    description=u'Дизайнер отчетов на основе Stimulsoft Report Js',
    url='https://github.com/damirazo/creadoc',
    author='damirazo',
    author_email='me@damirazo.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: General',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['demo', 'tests']),
    include_package_data=True,
    install_requires=(
        'Django>=1.11.12',
        'm3-core>=3.0',
        'm3-legacy>=2.1.1',
        'm3-mutex>=2.0.4',
        'm3-ui>=2.0.8,<3.1',
        'm3-users>=2.2.4',
    ),
)
