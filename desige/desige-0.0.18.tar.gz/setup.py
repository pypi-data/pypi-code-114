import setuptools

import desige

setuptools.setup(
    name         = 'desige',
    version      = desige.__version__,
    author       = 'AXY',
    author_email = 'axy@declassed.art',
    description  = 'Declassed site generator',

    long_description = desige.__doc__,
    long_description_content_type = 'text/x-rst',

    url = 'https://declassed.art/repository/desige',

    packages = [
        'desige',
        'desige.extras',
        'desige.pages',
        'desige.templates',
        'desige.templates.extras'
    ],

    install_requires=[
        'axyutils',
        'clabate',
        'idna',
        'python-dateutil',
        'pyyaml'
    ],

    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],

    python_requires = '>=3.6',
)
