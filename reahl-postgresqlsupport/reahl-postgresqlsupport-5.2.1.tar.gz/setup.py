from setuptools import setup, Command
class InstallTestDependencies(Command):
    user_options = []
    def run(self):
        import sys
        import subprocess
        if self.distribution.tests_require: subprocess.check_call([sys.executable, "-m", "pip", "install", "-q"]+self.distribution.tests_require)

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

setup(
    name='reahl-postgresqlsupport',
    version='5.2.1',
    description='Support for using PostgreSQL with Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis package contains infrastructure necessary to use Reahl with PostgreSQL. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-commands>=5.2,<5.3', 'psycopg2-binary>=2.8,<2.8.9999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0'],
    test_suite='tests',
    entry_points={
        'reahl.versions': [
            '5.2 = 5.2',
            '5.1 = 5.1',
            '5.0 = 5.0',
            '4.0 = 4.0',
            '3.2 = 3.2',
            '3.1 = 3.1',
            '3.0 = 3.0',
            '2.1 = 2.1',
            '2.0 = 2.0'    ],
        'reahl.versiondeps.5.2': [
            'reahl-component = egg:5.2',
            'reahl-commands = egg:5.2',
            'psycopg2-binary = thirdpartyegg:2.8 [2.8.9999]'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'reahl-commands = egg:5.1',
            'psycopg2-binary = thirdpartyegg:2.8 [2.8.9999]'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'reahl-commands = egg:5.0',
            'psycopg2-binary = thirdpartyegg:2.8 [2.8.9999]'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'reahl-commands = egg:4.0',
            'psycopg2-binary = thirdpartyegg:2.7 [2.7.9999]'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'psycopg2 = thirdpartyegg:2.5 [2.5.9999]'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'psycopg2 = thirdpartyegg:2.5 [2.5.9999]'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'psycopg2 = thirdpartyegg:2.5 [2.5.9999]'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'psycopg2 = thirdpartyegg:2.4 [2.5]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'psycopg2 = thirdpartyegg:2.4 [2.5]'    ],
        'reahl.component.databasecontrols': [
            'PostgresqlControl = reahl.postgresqlsupport:PostgresqlControl'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
