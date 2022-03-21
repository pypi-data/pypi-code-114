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
    name='reahl-domainui',
    version='5.2.1',
    description='A user interface for reahl-domain.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis Reahl component contains a user interface for some of the domain functionality in reahl-domainui. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.domainui', 'reahl.domainui.bootstrap', 'reahl.domainui_dev', 'reahl.domainui_dev.bootstrap', 'reahl.messages'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'setuptools>=32.3.1'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3'],
    test_suite='reahl.domainui_dev',
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
            'reahl-sqlalchemysupport = egg:5.2',
            'reahl-web = egg:5.2',
            'reahl-web-declarative = egg:5.2',
            'reahl-domain = egg:5.2',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'reahl-sqlalchemysupport = egg:5.1',
            'reahl-web = egg:5.1',
            'reahl-web-declarative = egg:5.1',
            'reahl-domain = egg:5.1',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'reahl-sqlalchemysupport = egg:5.0',
            'reahl-web = egg:5.0',
            'reahl-web-declarative = egg:5.0',
            'reahl-domain = egg:5.0',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'reahl-sqlalchemysupport = egg:4.0',
            'reahl-web = egg:4.0',
            'reahl-web-declarative = egg:4.0',
            'reahl-domain = egg:4.0',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'reahl-sqlalchemysupport = egg:3.2',
            'reahl-web = egg:3.2',
            'reahl-web-declarative = egg:3.2',
            'reahl-domain = egg:3.2'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'reahl-sqlalchemysupport = egg:3.1',
            'reahl-web = egg:3.1',
            'reahl-web-declarative = egg:3.1',
            'reahl-domain = egg:3.1'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'reahl-sqlalchemysupport = egg:3.0',
            'reahl-web = egg:3.0',
            'reahl-domain = egg:3.0'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'reahl-sqlalchemysupport = egg:2.1',
            'reahl-web = egg:2.1',
            'reahl-domain = egg:2.1'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'reahl-sqlalchemysupport = egg:2.0',
            'reahl-web = egg:2.0',
            'reahl-domain = egg:2.0'    ],
        'reahl.configspec': [
            'config = reahl.domainuiegg:DomainUiConfig'    ],
        'reahl.workflowui.task_widgets': [
            'bootstrap.TaskWidget = reahl.domainui.bootstrap.workflow:TaskWidget'    ],
        'reahl.translations': [
            'reahl-domainui = reahl.messages'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
