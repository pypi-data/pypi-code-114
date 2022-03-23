from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()


setup(
    name='ezx-pyapi',
    version='0.2',
    license='MIT',
    author="EZX Inc.",
    author_email='support@ezxinc.com',
    packages=find_packages('.'),
    package_dir={'': '.'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='EZX iServer API trading',
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown'
)

