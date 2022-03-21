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
    name='reahl-sqlalchemysupport',
    version='5.2.1',
    description='Support for using SqlAlchemy with Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis package contains infrastructure necessary to use Reahl with SqlAlchemy or Elixir. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.sqlalchemysupport', 'reahl.sqlalchemysupport_dev'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-commands>=5.2,<5.3', 'SQLAlchemy>=1.2.0,<1.4.999', 'alembic>=0.9.6,<1.7.999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-sqlitesupport>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3'],
    test_suite='reahl.sqlalchemysupport_dev',
    entry_points={
        'reahl.persistlist': [
            '0 = reahl.sqlalchemysupport:SchemaVersion'    ],
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
            'SQLAlchemy = thirdpartyegg:1.2.0 [1.4.999]',
            'alembic = thirdpartyegg:0.9.6 [1.7.999]'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'reahl-commands = egg:5.1',
            'SQLAlchemy = thirdpartyegg:1.2.0 [1.3.999]',
            'alembic = thirdpartyegg:0.9.6 [1.4.999]'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'reahl-commands = egg:5.0',
            'SQLAlchemy = thirdpartyegg:1.2.0 [1.3.999]',
            'alembic = thirdpartyegg:0.9.6 [1.4.999]'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'reahl-commands = egg:4.0',
            'sqlalchemy = thirdpartyegg:1.2.0 [1.2.999]',
            'alembic = thirdpartyegg:0.9.6 [0.9.999]'    ],
        'reahl.migratelist.4.0': [
            '0 = reahl.sqlalchemysupport.migrations:ChangesToBeMySqlCompatible'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'sqlalchemy = thirdpartyegg:0.9.2 [0.9.999]',
            'alembic = thirdpartyegg:0.6 [0.6.999]'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'sqlalchemy = thirdpartyegg:0.9.2 [0.9.999]',
            'alembic = thirdpartyegg:0.6 [0.6.999]'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'sqlalchemy = thirdpartyegg:0.9.2 [0.9.999]',
            'alembic = thirdpartyegg:0.6 [0.6.999]'    ],
        'reahl.migratelist.3.0': [
            '0 = reahl.sqlalchemysupport.elixirmigration:ElixirToDeclarativeSqlAlchemySupportChanges'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'sqlalchemy = thirdpartyegg:0.7 [0.7.999]',
            'alembic = thirdpartyegg:0.5 [0.5.999]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'sqlalchemy = thirdpartyegg:0.7 [0.7.999]',
            'alembic = thirdpartyegg:0.5 [0.5.999]'    ],
        'reahl.migratelist.2.0': [
            '0 = reahl.sqlalchemysupport.migrations:CreateDatabase'    ],
        'reahl.configspec': [
            'config = reahl.sqlalchemysupport:SqlAlchemyConfig'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
