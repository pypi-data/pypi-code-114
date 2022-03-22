from setuptools import setup

setup(
    name='fentik',
    version='0.0.1',
    packages=['fentik'],
    scripts=['scripts/fentik'],
    install_requires=[
        'PrettyTable',
        'graphqlclient',
    ],
)
