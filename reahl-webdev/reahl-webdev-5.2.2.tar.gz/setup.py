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
    name='reahl-webdev',
    version='5.2.2',
    description='Web-specific development tools for Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl development tools for testing and working with web based programs. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.webdev', 'reahl.webdev_dev'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-web>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-component>=5.2,<5.3', 'reahl-tofu>=5.2,<5.3', 'selenium>=2.42,<3.141.9999', 'watchdog>=0.8.3,<0.10.999', 'WebOb>=1.8,<1.8.999', 'setuptools>=32.3.1', 'prompt_toolkit>=2.0.10,<2.0.999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-doc>=5.2,<5.3', 'reahl-tofu>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3'],
    test_suite='reahl.webdev_dev',
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
            'reahl-web = egg:5.2',
            'reahl-dev = egg:5.2',
            'reahl-component = egg:5.2',
            'reahl-tofu = egg:5.2',
            'selenium = thirdpartyegg:2.42 [3.141.9999]',
            'watchdog = thirdpartyegg:0.8.3 [0.10.999]',
            'WebOb = thirdpartyegg:1.8 [1.8.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'prompt_toolkit = thirdpartyegg:2.0.10 [2.0.999]'    ],
        'reahl.versiondeps.5.1': [
            'reahl-web = egg:5.1',
            'reahl-dev = egg:5.1',
            'reahl-component = egg:5.1',
            'reahl-tofu = egg:5.1',
            'selenium = thirdpartyegg:2.42 [3.141.9999]',
            'watchdog = thirdpartyegg:0.8.3 [0.10.999]',
            'WebOb = thirdpartyegg:1.8 [1.8.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'prompt_toolkit = thirdpartyegg:2.0.10 [2.0.999]'    ],
        'reahl.versiondeps.5.0': [
            'reahl-web = egg:5.0',
            'reahl-dev = egg:5.0',
            'reahl-component = egg:5.0',
            'reahl-tofu = egg:5.0',
            'reahl-domain = egg:5.0',
            'lxml = thirdpartyegg:4.2 [4.5.999]',
            'WebTest = thirdpartyegg:2.0 [2.0.999]',
            'selenium = thirdpartyegg:2.42 [3.141.9999]',
            'watchdog = thirdpartyegg:0.8.3 [0.10.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'WebOb = thirdpartyegg:1.8 [1.8.999]',
            'prompt_toolkit = thirdpartyegg:2.0.10 [2.0.999]'    ],
        'reahl.versiondeps.4.0': [
            'reahl-web = egg:4.0',
            'reahl-dev = egg:4.0',
            'reahl-component = egg:4.0',
            'reahl-tofu = egg:4.0',
            'reahl-domain = egg:4.0',
            'lxml = thirdpartyegg:4.2 [4.2.999]',
            'WebTest = thirdpartyegg:2.0 [2.0.999]',
            'selenium = thirdpartyegg:2.42 [2.9999]',
            'watchdog = thirdpartyegg:0.8.3 [0.8.999.3]',
            'setuptools = thirdpartyegg:32.3.1',
            'webob = thirdpartyegg:1.4 [1.4.999]'    ],
        'reahl.versiondeps.3.2': [
            'reahl-web = egg:3.2',
            'reahl-dev = egg:3.2',
            'reahl-component = egg:3.2',
            'reahl-tofu = egg:3.2',
            'reahl-domain = egg:3.2',
            'lxml = thirdpartyegg:3.3 [3.3.999]',
            'WebTest = thirdpartyegg:2.0 [2.0.999]',
            'selenium = thirdpartyegg:2.42 [2.9999]',
            'watchdog = thirdpartyegg:0.8.3 [0.8.999.3]'    ],
        'reahl.versiondeps.3.1': [
            'reahl-web = egg:3.1',
            'reahl-dev = egg:3.1',
            'reahl-component = egg:3.1',
            'reahl-tofu = egg:3.1',
            'reahl-domain = egg:3.1',
            'lxml = thirdpartyegg:3.3 [3.3.999]',
            'WebTest = thirdpartyegg:2.0 [2.0.999]',
            'selenium = thirdpartyegg:2.42 [2.42.999]'    ],
        'reahl.versiondeps.3.0': [
            'reahl-web = egg:3.0',
            'reahl-dev = egg:3.0',
            'reahl-component = egg:3.0',
            'reahl-tofu = egg:3.0',
            'lxml = thirdpartyegg:3.3 [3.3.999]',
            'WebTest = thirdpartyegg:2.0 [2.0.999]',
            'selenium = thirdpartyegg:2.42 [2.42.999]'    ],
        'reahl.versiondeps.2.1': [
            'reahl-web = egg:2.1',
            'reahl-dev = egg:2.1',
            'reahl-component = egg:2.1',
            'reahl-tofu = egg:2.1',
            'lxml = thirdpartyegg:3.2',
            'WebTest = thirdpartyegg:1.4 [1.5]',
            'selenium = thirdpartyegg:2.25 [2.27]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-web = egg:2.0',
            'reahl-dev = egg:2.0',
            'reahl-component = egg:2.0',
            'reahl-tofu = egg:2.0',
            'lxml = thirdpartyegg:3.2',
            'WebTest = thirdpartyegg:1.4 [1.5]',
            'selenium = thirdpartyegg:2.25 [2.27]'    ],
        'reahl.component.commands': [
            'ServeCurrentProject = reahl.webdev.commands:ServeCurrentProject',
            'SyncFiles = reahl.webdev.commands:SyncFiles',
            'CreateConfig = reahl.webdev.commands:CreateConfig'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={'pillow': ['Pillow>=2.5,<7.1.999']},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
