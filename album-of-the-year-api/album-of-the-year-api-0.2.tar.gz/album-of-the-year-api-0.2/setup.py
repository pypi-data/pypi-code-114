from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = f.read().splitlines()

setup(
    name='album-of-the-year-api',
    description='A light weight Python library that acts as an API for the website albumoftheyear.org',
    version='0.2',
    license='GNU',
    author="Jahsias White",
    author_email='jahsias.white@gmail.com',
    find_packages=['albumoftheyearapi'],
    install_requires=install_requires,
    url='https://github.com/JahsiasWhite/AlbumOfTheYearWrapper'
)