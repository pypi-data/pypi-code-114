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
    name='reahl-domain',
    version='5.2.1',
    description='End-user domain functionality for use with Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis Reahl component includes functionality modelling user accounts, some simple workflow concepts and more. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.domain', 'reahl.domain_dev', 'reahl.messages'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-mailutil>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'passlib>=1.7.1,<1.7.9999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3'],
    test_suite='reahl.domain_dev',
    entry_points={
        'reahl.persistlist': [
            '0 = reahl.partymodel:Party',
            '1 = reahl.systemaccountmodel:SystemAccount',
            '2 = reahl.systemaccountmodel:LoginSession',
            '3 = reahl.systemaccountmodel:EmailAndPasswordSystemAccount',
            '4 = reahl.systemaccountmodel:AccountManagementInterface',
            '5 = reahl.systemaccountmodel:VerificationRequest',
            '6 = reahl.systemaccountmodel:VerifyEmailRequest',
            '7 = reahl.systemaccountmodel:NewPasswordRequest',
            '8 = reahl.systemaccountmodel:ActivateAccount',
            '9 = reahl.systemaccountmodel:ChangeAccountEmail',
            '10 = reahl.workflowmodel:DeferredAction',
            '11 = reahl.workflowmodel:Requirement',
            '12 = reahl.workflowmodel:Queue',
            '13 = reahl.workflowmodel:Task'    ],
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
            'reahl-mailutil = egg:5.2',
            'reahl-sqlalchemysupport = egg:5.2',
            'reahl-web-declarative = egg:5.2',
            'passlib = thirdpartyegg:1.7.1 [1.7.9999]'    ],
        'reahl.migratelist.5.2': [
            '0 = reahl.domain.migrations:AddPolimorphicEntityName'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'reahl-mailutil = egg:5.1',
            'reahl-sqlalchemysupport = egg:5.1',
            'reahl-web-declarative = egg:5.1',
            'passlib = thirdpartyegg:1.7.1 [1.7.9999]'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'reahl-mailutil = egg:5.0',
            'reahl-sqlalchemysupport = egg:5.0',
            'reahl-web-declarative = egg:5.0',
            'passlib = thirdpartyegg:1.7.1 [1.7.9999]'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'reahl-mailutil = egg:4.0',
            'reahl-sqlalchemysupport = egg:4.0',
            'reahl-web-declarative = egg:4.0',
            'passlib = thirdpartyegg:1.7.1 [1.7.9999]'    ],
        'reahl.migratelist.4.0': [
            '0 = reahl.domain.migrations:ChangeSchemaToBeMySqlCompatible',
            '1 = reahl.domain.migrations:ChangePasswordHash',
            '2 = reahl.domain.migrations:RemoveDeadApacheDigestColumn'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'reahl-mailutil = egg:3.2',
            'reahl-sqlalchemysupport = egg:3.2',
            'reahl-web-declarative = egg:3.2'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'reahl-mailutil = egg:3.1',
            'reahl-sqlalchemysupport = egg:3.1',
            'reahl-web-declarative = egg:3.1'    ],
        'reahl.migratelist.3.1': [
            '0 = reahl.domain.migrations:AddLoginSession'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'reahl-mailutil = egg:3.0',
            'reahl-interfaces = egg:3.0',
            'reahl-sqlalchemysupport = egg:3.0'    ],
        'reahl.migratelist.3.0': [
            '0 = reahl.domain.migrations:ElixirToDeclarativeDomainChanges'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'reahl-mailutil = egg:2.1',
            'reahl-interfaces = egg:2.1',
            'reahl-sqlalchemysupport = egg:2.1',
            'elixir = thirdpartyegg:0.7 [0.8]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'reahl-mailutil = egg:2.0',
            'reahl-interfaces = egg:2.0',
            'reahl-sqlalchemysupport = egg:2.0',
            'elixir = thirdpartyegg:0.7 [0.8]'    ],
        'reahl.migratelist.2.0': [
            '0 = reahl.domain.migrations:CreateDatabase'    ],
        'reahl.configspec': [
            'config = reahl.systemaccountmodel:SystemAccountConfig'    ],
        'reahl.scheduled_jobs': [
            'reahl.workflowmodel:DeferredAction.check_deadline = reahl.workflowmodel:DeferredAction.check_deadline'    ],
        'reahl.translations': [
            'reahl-domain = reahl.messages'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
