import os
from setuptools import setup

current_path = os.path.abspath('C:\\Users\\Peter\\Desktop\\Personal\\11_Repository\\pyjr\\')


def read_file(*parts):
    with open(os.path.join(current_path, *parts), encoding='utf-8') as reader:
        return reader.read()


setup(
    name='pyjr',
    version='0.0.3',
    packages=['pyjr', ],
    author='Peter Rigali',
    author_email='peterjrigali@gmail.com',
    license='MIT',
    description='Functions and Classes for assisting with ETL.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='',
)
