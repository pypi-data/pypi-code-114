# setup.py
import setuptools

setuptools.setup(
    name='my_hello_lib', # Имя пакета
    version='0.0.1',  # Версия пакета
    author='mmorfii',
    author_email='dasha.zueva@list.ru',
    description='My Package hello world',
    packages=setuptools.find_packages(),
)