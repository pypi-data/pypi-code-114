from setuptools import setup, find_packages
from pathlib import Path

directory = Path(__file__).parent
longDescription = (directory/'README.md').read_text()

setup(
    name='wbsearch',
    version='1.2.3',
    packages=['wbsearch'],
    author='Cargo',
    install_requires=['click', 'KvK'],
    long_description=longDescription,
    long_description_content_type='text/markdown',
    entry_points='''
    [console_scripts]
    wbsearch=wbsearch:search
    '''
)