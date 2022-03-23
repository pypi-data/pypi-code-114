from setuptools import setup
from setuptools import find_packages


setup(
    name = 'fileheaderPy',
    version = '8.0.0',
    author = 'Maycon Cypriano Batestin',
    author_email = 'mayconcipriano@gmail.com',
    packages = ['fileheaderPy'],
    description = 'A way to create script python with beatiful header',
    long_description = 'file: README.md',
    url = 'https://github.com/batestin1/',
    project_urls = {
        'Código fonte': 'https://github.com/batestin1/',
        'Download': 'https://github.com/batestin1/'
    },
    keywords = 'A way to create script python with beatiful header',
    classifiers = [


    ],
    install_requires=[
            'art'
        ]

)