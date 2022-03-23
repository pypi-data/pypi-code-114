from setuptools import setup

setup(
    name='nbstrip',
    author="Colm Talbot",
    url="https://github.com/ColmTalbot/nbstrip",
    version='0.1.0',
    py_modules=['nbstrip'],
    entry_points='''
        [console_scripts]
        nbstrip=nbstrip:main
    ''',
)
