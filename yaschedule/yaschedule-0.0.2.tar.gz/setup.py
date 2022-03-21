from setuptools import setup, find_packages

version = '0.0.2'

setup(
    name='yaschedule',
    version=version,
    description='Lib for getting schedule data from Yandex Schedule API',
    url='https://github.com/StannisGr/yaschedule',
    author='StannisGr',
    author_email='bvc344@gmail.com',
    license='Apache License 2.0',
    platforms=['any'],
    keywords='yandex, schedule, api',
    packages=find_packages(),
    install_requires=[
    'certifi>=2021.10.8',
    'charset-normalizer>=2.0.12',
    'idna>=3.3',
    'requests>=2.27.1',
    'urllib3>=1.26.9',
    ],
)
