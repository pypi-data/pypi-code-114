from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1.5'

setup(
    name='pyloopkey',
    packages=find_packages(include=['loopkey_client']),
    version=VERSION,
    description='Loopkey API library',
    author='Mauricio Cisneros',
    author_email='mauricio.cisneros@casai.com',
    url='https://github.com/casai-org/pyloopkey',
    install_requires=['requests>=2.20.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
