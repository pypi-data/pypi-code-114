import sys

from setuptools import setup


setup(
    name="vgmail",
    version="1.0",
    description="Python interface for gmail API",
    author='Vam Gan',
    author_email='vamgan@cmu.edu',
    license="MIT",
    packages=['vgmail'],
    install_requires=[
        'google-api-python-client',
        'bs4',
        'python-dateutil',
        'oauth2client',
        'lxml'
    ]
)