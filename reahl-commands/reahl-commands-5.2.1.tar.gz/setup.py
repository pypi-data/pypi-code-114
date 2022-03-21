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
    name='reahl-commands',
    version='5.2.1',
    description='The component framework of Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-commands contains useful command line commands for reahl components. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.commands'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=5.2,<5.3'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3'],
    test_suite='tests',
    entry_points={
        'reahl.versions': [
            '5.2 = 5.2',
            '5.1 = 5.1',
            '5.0 = 5.0',
            '4.0 = 4.0'    ],
        'reahl.versiondeps.5.2': [
            'reahl-component = egg:5.2'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0'    ],
        'reahl.versiondeps.4.0': [
            'six = thirdpartyegg:_',
            'reahl-component = egg:4.0'    ],
        'reahl.migratelist.4.0': [
            '0 = reahl.commands.migrations:ReahlCommandsReahlSchemaInitialise'    ],
        'reahl.component.commands': [
            'CreateDBUser = reahl.commands.prodshell:CreateDBUser',
            'DropDBUser = reahl.commands.prodshell:DropDBUser',
            'CreateDB = reahl.commands.prodshell:CreateDB',
            'DropDB = reahl.commands.prodshell:DropDB',
            'BackupDB = reahl.commands.prodshell:BackupDB',
            'RestoreDB = reahl.commands.prodshell:RestoreDB',
            'BackupAllDB = reahl.commands.prodshell:BackupAllDB',
            'RestoreAllDB = reahl.commands.prodshell:RestoreAllDB',
            'SizeDB = reahl.commands.prodshell:SizeDB',
            'RunJobs = reahl.commands.prodshell:RunJobs',
            'CreateDBTables = reahl.commands.prodshell:CreateDBTables',
            'DropDBTables = reahl.commands.prodshell:DropDBTables',
            'MigrateDB = reahl.commands.prodshell:MigrateDB',
            'DiffDB = reahl.commands.prodshell:DiffDB',
            'ListConfig = reahl.commands.prodshell:ListConfig',
            'CheckConfig = reahl.commands.prodshell:CheckConfig',
            'ListDependencies = reahl.commands.prodshell:ListDependencies',
            'ListVersionHistory = reahl.commands.prodshell:ListVersionHistory',
            'ExportStaticFiles = reahl.commands.prodshell:ExportStaticFiles',
            'ComponentInfo = reahl.commands.prodshell:ComponentInfo'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
