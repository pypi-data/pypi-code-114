from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


setup(
    name='beersolver',
    version='0.1.1',
    author="Henrique Nepomuceno",
    author_email="nepo26.hn@protonmail.com",
    packages=find_packages(),
    py_modules=['exercises/ThirdChapter/commands'],
    description="A script for solving vector mechanics Ferdinand P. Beer proposed exercises.",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/Nepo26/Beersolver",
    license="GNU GPLv3",
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'beersolver=exercises.ThirdChapter.commands:cli',
        ],
    },
)
