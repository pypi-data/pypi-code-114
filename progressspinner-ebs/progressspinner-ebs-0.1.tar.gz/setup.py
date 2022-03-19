import os

from setuptools import find_packages, setup

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='progressspinner-ebs',
    version='0.1',
    author='Kathryn Taylee',
    author_email='kived@github.com',
    maintainer='Chintalagiri Shashank',
    maintainer_email='shashank@chintal.in',
    url='https://github.com/chintal/progressspinner-ebs',
    packages=find_packages(),
    include_package_data=True,
    description='Fork of kivy-garden progress spinner',
    long_description="",
    install_requires=[
        'kivy>=1.11.1',
    ]
)
