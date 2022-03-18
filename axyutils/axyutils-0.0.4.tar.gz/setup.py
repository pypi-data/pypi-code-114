import setuptools

import axyutils

setuptools.setup(
    name         = 'axyutils',
    version      = axyutils.__version__,
    author       = 'AXY',
    author_email = 'axy@declassed.art',
    description  = 'Declassed utilities',

    long_description = axyutils.__doc__,
    long_description_content_type = 'text/x-rst',

    url = 'https://declassed.art/repository/axyutils',

    packages = [
        'axyutils'
    ],

    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha'
    ],

    python_requires = '>=3.6',
)
