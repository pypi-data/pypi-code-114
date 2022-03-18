from setuptools import setup
from pathlib import Path

directory = Path(__file__).parent
longDescription = (directory/'README.md').read_text()

setup(
    name='preparepack',
    author='Cargo',
    version='1.2.0',
    packages=['prepack'],
    install_requires=['click'],
    long_description=longDescription,
    license='MIT',
    long_description_content_type='text/markdown',
    entry_points='''
    [console_scripts]
    prepack=prepack:prepack
    buildpack=prepack:build
    '''
)
