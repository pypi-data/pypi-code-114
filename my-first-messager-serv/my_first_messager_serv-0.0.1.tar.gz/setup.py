from setuptools import setup, find_packages

setup(
    name="my_first_messager_serv",
    version='0.0.1',
    description='part server',
    author='Pentegov Dmitriy',
    author_email="pentegov_92@mail.ru",
    packages=find_packages(),
    install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
)
