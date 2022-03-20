import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='progresslogger',
    version='1.0.0',
    description='A simple, lightweight logger for your Python loops',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/michael-genson/progresslogger',
    author='Michael Genson',
    author_email='genson.michael@gmail.com',
    license='GNU',
    packages=['progresslogger'],
    zip_safe=False
    )