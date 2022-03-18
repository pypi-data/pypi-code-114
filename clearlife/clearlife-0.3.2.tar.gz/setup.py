#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
$ python setup.py register sdist upload

First Time register project on pypi
https://pypi.org/manage/projects/

More secure to use twine to upload
$ pip3 install twine
$ python3 setup.py sdist
$ twine upload dist/clearlifed-0.0.1.tar.gz

Best practices for setup.py and requirements.txt
https://caremad.io/posts/2013/07/setup-vs-requirement/
"""


from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='clearlife',
    version='0.3.2',  #  also change in src/clearlifed/__init__.py
    license='AGPL3',
    description='ClearLIFE Server SDK',
    long_description="Key management using derived keys for server applications.",
    author='',
    author_email='',
    url='https://gitlab.com/clearos/clearfoundation/clearlife-sdk',
    packages=['clearlife'],
    py_modules=[splitext(basename(path))[0] for path in glob('clearlife/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        # uncomment if you test on these interpreters:
        #'Programming Language :: Python :: Implementation :: PyPy',
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    python_requires='>=3.8.6',
    install_requires=[
        'termcolor==1.1.0',
        'cython==0.29.23',
        'aries_cloudagent==0.6.0',
        'pysodium==0.7.9',
        'didauth',
        'attrdict'
    ],
    setup_requires=[
    ],
    entry_points={
        'console_scripts': [
            'clearlife = clearlife.cli:main'
        ]
    },
)

