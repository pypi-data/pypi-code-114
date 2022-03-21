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
    name='reahl-component',
    version='5.2.1',
    description='The component framework of Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThe reahl-component framework extends setuptools distribution packages to package and distribute more than just code. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.component', 'reahl.component_dev', 'reahl.messages'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['Babel>=2.1,<2.9.999', 'python-dateutil>=2.8,<2.8.999', 'wrapt>=1.11.0,<1.13.999', 'setuptools>=32.3.1', 'pip>=10.0.0'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'graphviz', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-sqlitesupport>=5.2,<5.3', 'reahl-mysqlsupport>=5.2,<5.3'],
    test_suite='reahl.component_dev',
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
            'Babel = thirdpartyegg:2.1 [2.9.999]',
            'python-dateutil = thirdpartyegg:2.8 [2.8.999]',
            'wrapt = thirdpartyegg:1.11.0 [1.13.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.5.1': [
            'Babel = thirdpartyegg:2.1 [2.8.999]',
            'python-dateutil = thirdpartyegg:2.8 [2.8.999]',
            'wrapt = thirdpartyegg:1.11.0 [1.12.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.5.0': [
            'Babel = thirdpartyegg:2.1 [2.8.999]',
            'python-dateutil = thirdpartyegg:2.8 [2.8.999]',
            'wrapt = thirdpartyegg:1.11.0 [1.12.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.4.0': [
            'six = thirdpartyegg:_',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'python-dateutil = thirdpartyegg:2.2 [2.2.999]',
            'wrapt = thirdpartyegg:1.10.2 [1.10.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.3.2': [
            'six = thirdpartyegg:_',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'python-dateutil = thirdpartyegg:2.2 [2.2.999]',
            'wrapt = thirdpartyegg:1.10.2 [1.10.999]'    ],
        'reahl.versiondeps.3.1': [
            'six = thirdpartyegg:_',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'python-dateutil = thirdpartyegg:2.2 [2.2.999]',
            'wrapt = thirdpartyegg:1.10.2 [1.10.999]'    ],
        'reahl.versiondeps.3.0': [
            'six = thirdpartyegg:_',
            'Babel = thirdpartyegg:1.3 [1.3.9999]',
            'python-dateutil = thirdpartyegg:2.2 [2.2.999]',
            'decorator = thirdpartyegg:3.4 [3.4]'    ],
        'reahl.versiondeps.2.1': [
            'six = thirdpartyegg:_',
            'Babel = thirdpartyegg:0.9 [0.10]',
            'python-dateutil = thirdpartyegg:1.5 [1.6]',
            'decorator = thirdpartyegg:3.4 [3.4]'    ],
        'reahl.versiondeps.2.0': [
            'Babel = thirdpartyegg:0.9 [0.10]',
            'python-dateutil = thirdpartyegg:1.5 [1.6]',
            'decorator = thirdpartyegg:3.4 [3.4]'    ],
        'console_scripts': [
            'reahl = reahl.component.shelltools:ReahlCommandline.execute_one'    ],
        'reahl.component.commands': [
            'AddAlias = reahl.component.shelltools:AddAlias',
            'RemoveAlias = reahl.component.shelltools:RemoveAlias'    ],
        'reahl.component.databasecontrols': [
            'NullDatabaseControl = reahl.component.dbutils:NullDatabaseControl'    ],
        'reahl.translations': [
            'reahl-component = reahl.messages'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
