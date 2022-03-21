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
    name='reahl-dev',
    version='5.2.1',
    description='The core Reahl development tools.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-dev is the component containing general Reahl development tools. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.dev', 'reahl.dev_dev'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'Babel>=2.1,<2.9.999', 'twine>=1.15.0,<3.8.9999', 'wheel>=0.34.0', 'tzlocal>=2.0.0,<4.1.9999', 'setuptools>=32.3.1', 'pip>=10.0.0'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0'],
    test_suite='reahl.dev_dev',
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
            'reahl-tofu = egg:5.2',
            'reahl-stubble = egg:5.2',
            'Babel = thirdpartyegg:2.1 [2.9.999]',
            'twine = thirdpartyegg:1.15.0 [3.8.9999]',
            'wheel = thirdpartyegg:0.34.0',
            'tzlocal = thirdpartyegg:2.0.0 [4.1.9999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'reahl-tofu = egg:5.1',
            'reahl-stubble = egg:5.1',
            'Babel = thirdpartyegg:2.1 [2.8.999]',
            'twine = thirdpartyegg:1.15.0 [3.1.9999]',
            'wheel = thirdpartyegg:0.34.0 [0.34.9999]',
            'tzlocal = thirdpartyegg:2.0.0 [2.0.9999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'reahl-tofu = egg:5.0',
            'reahl-stubble = egg:5.0',
            'Babel = thirdpartyegg:2.1 [2.8.999]',
            'twine = thirdpartyegg:1.15.0 [3.1.9999]',
            'wheel = thirdpartyegg:0.34.0 [0.34.9999]',
            'tzlocal = thirdpartyegg:2.0.0 [2.0.9999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'reahl-tofu = egg:4.0',
            'reahl-stubble = egg:4.0',
            'six = thirdpartyegg:_',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'twine = thirdpartyegg:1.11.0 [1.11.9999]',
            'wheel = thirdpartyegg:0.29.0 [0.29.9999]',
            'tzlocal = thirdpartyegg:1.2.0 [1.2.9999]',
            'setuptools = thirdpartyegg:32.3.1',
            'pip = thirdpartyegg:10.0.0'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'reahl-tofu = egg:3.2',
            'reahl-bzrsupport = egg:3.2',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'twine = thirdpartyegg:1.4.0 [1.4.9999]',
            'wheel = thirdpartyegg:0.24.0 [0.24.9999]'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'reahl-tofu = egg:3.1',
            'reahl-bzrsupport = egg:3.1',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'twine = thirdpartyegg:1.4.0 [1.4.9999]',
            'wheel = thirdpartyegg:0.24.0 [0.24.9999]'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'reahl-tofu = egg:3.0',
            'reahl-bzrsupport = egg:3.0',
            'Babel = thirdpartyegg:1.3 [1.3.9999]'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'reahl-tofu = egg:2.1',
            'reahl-bzrsupport = egg:2.1',
            'Babel = thirdpartyegg:0.9 [0.10]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'reahl-tofu = egg:2.0',
            'reahl-bzrsupport = egg:2.0',
            'Babel = thirdpartyegg:0.9 [0.10]'    ],
        'reahl.component.commands': [
            'Refresh = reahl.dev.devshell:Refresh',
            'ExplainLegend = reahl.dev.devshell:ExplainLegend',
            'List = reahl.dev.devshell:List',
            'Select = reahl.dev.devshell:Select',
            'ClearSelection = reahl.dev.devshell:ClearSelection',
            'ListSelections = reahl.dev.devshell:ListSelections',
            'Save = reahl.dev.devshell:Save',
            'Read = reahl.dev.devshell:Read',
            'DeleteSelection = reahl.dev.devshell:DeleteSelection',
            'Shell = reahl.dev.devshell:Shell',
            'Setup = reahl.dev.devshell:Setup',
            'Build = reahl.dev.devshell:Build',
            'Sign = reahl.dev.devshell:Sign',
            'ListMissingDependencies = reahl.dev.devshell:ListMissingDependencies',
            'DebInstall = reahl.dev.devshell:DebInstall',
            'Upload = reahl.dev.devshell:Upload',
            'MarkReleased = reahl.dev.devshell:MarkReleased',
            'SubstVars = reahl.dev.devshell:SubstVars',
            'Debianise = reahl.dev.devshell:Debianise',
            'Info = reahl.dev.devshell:Info',
            'ExtractMessages = reahl.dev.devshell:ExtractMessages',
            'MergeTranslations = reahl.dev.devshell:MergeTranslations',
            'CompileTranslations = reahl.dev.devshell:CompileTranslations',
            'AddLocale = reahl.dev.devshell:AddLocale',
            'UpdateAptRepository = reahl.dev.devshell:UpdateAptRepository',
            'ServeSMTP = reahl.dev.mailtest:ServeSMTP',
            'UpdateCopyright = reahl.dev.devshell:UpdateCopyright'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
