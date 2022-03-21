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
    name='reahl-web-declarative',
    version='5.2.2',
    description='An implementation of Reahl persisted classes using SqlAlchemy.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nSome core elements of Reahl can be implemented for use with different persistence technologies. This is such an implementation based on SqlAlchemy. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.webdeclarative', 'reahl.webdeclarative_dev'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web>=5.2,<5.3', 'reahl-component>=5.2,<5.3'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['WebOb>=1.8,<1.8.999', 'pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3'],
    test_suite='reahl.webdeclarative_dev',
    entry_points={
        'reahl.persistlist': [
            '0 = reahl.webdeclarative.webdeclarative:UserSession',
            '1 = reahl.webdeclarative.webdeclarative:SessionData',
            '2 = reahl.webdeclarative.webdeclarative:UserInput',
            '3 = reahl.webdeclarative.webdeclarative:PersistedException',
            '4 = reahl.webdeclarative.webdeclarative:PersistedFile'    ],
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
            'reahl-sqlalchemysupport = egg:5.2',
            'reahl-web = egg:5.2',
            'reahl-component = egg:5.2'    ],
        'reahl.migratelist.5.2': [
            '0 = reahl.webdeclarative.migrations:AddPolimorphicEntityName'    ],
        'reahl.versiondeps.5.1': [
            'reahl-sqlalchemysupport = egg:5.1',
            'reahl-web = egg:5.1',
            'reahl-component = egg:5.1'    ],
        'reahl.versiondeps.5.0': [
            'reahl-sqlalchemysupport = egg:5.0',
            'reahl-web = egg:5.0',
            'reahl-component = egg:5.0'    ],
        'reahl.migratelist.5.0': [
            '0 = reahl.webdeclarative.migrations:AddViewPathToSessionData'    ],
        'reahl.versiondeps.4.0': [
            'reahl-sqlalchemysupport = egg:4.0',
            'reahl-web = egg:4.0',
            'reahl-component = egg:4.0'    ],
        'reahl.migratelist.4.0': [
            '0 = reahl.webdeclarative.migrations:AllowNullUserInputValue'    ],
        'reahl.versiondeps.3.2': [
            'reahl-sqlalchemysupport = egg:3.2',
            'reahl-web = egg:3.2',
            'reahl-component = egg:3.2'    ],
        'reahl.versiondeps.3.1': [
            'reahl-sqlalchemysupport = egg:3.1',
            'reahl-web = egg:3.1',
            'reahl-component = egg:3.1'    ],
        'reahl.migratelist.3.1': [
            '0 = reahl.webdeclarative.migrations:MergeWebUserSessionToUserSession',
            '1 = reahl.webdeclarative.migrations:RenameContentType'    ],
        'reahl.versiondeps.3.0': [
            'reahl-interfaces = egg:3.0',
            'reahl-sqlalchemysupport = egg:3.0',
            'reahl-web = egg:3.0',
            'reahl-component = egg:3.0',
            'reahl-domain = egg:3.0'    ],
        'reahl.migratelist.3.0': [
            '0 = reahl.webdeclarative.migrations:ElixirToDeclarativeWebDeclarativeChanges'    ],
        'reahl.versiondeps.2.1': [
            'reahl-interfaces = egg:2.1',
            'reahl-sqlalchemysupport = egg:2.1',
            'reahl-web = egg:2.1',
            'reahl-component = egg:2.1',
            'reahl-domain = egg:2.1'    ],
        'reahl.migratelist.2.1': [
            '0 = reahl.webdeclarative.migrations:RenameRegionToUi'    ],
        'reahl.versiondeps.2.0': [
            'reahl-interfaces = egg:2.0',
            'reahl-sqlalchemysupport = egg:2.0',
            'reahl-web = egg:2.0',
            'reahl-component = egg:2.0',
            'reahl-domain = egg:2.0'    ],
        'reahl.migratelist.2.0': [
            '0 = reahl.webdeclarative.migrations:CreateDatabase'    ],
        'reahl.configspec': [
            'config = reahl.webdeclarative.webdeclarative:WebDeclarativeConfig'    ],
        'reahl.scheduled_jobs': [
            'reahl.webdeclarative.webdeclarative:UserSession.remove_dead_sessions = reahl.webdeclarative.webdeclarative:UserSession.remove_dead_sessions'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
