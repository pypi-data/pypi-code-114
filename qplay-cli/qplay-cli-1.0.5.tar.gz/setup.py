from setuptools import setup, find_packages

setup(
    name="qplay-cli",
    version='1.0.5',
    packages=['qplay_cli', 'qplay_cli.api_clients', 'qplay_cli.dataset', 'qplay_cli.backtest', 'qplay_cli.user', 'qplay_cli.machine'],
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'retrying',
        'ec2-metadata'
    ],
    entry_points='''
        [console_scripts]
        quantplay=qplay_cli.main:quantplay
    ''',
)