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
    name='reahl-workstation',
    version='5.2.2',
    description='Useful commands to ease development.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-workstation contains a few utilities that helps to have available on a developer workstation. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.workstation', 'reahl.workstation_dev'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=5.2,<5.3'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3'],
    test_suite='reahl.workstation_dev',
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
            'reahl-component = egg:4.0',
            'six = thirdpartyegg:_'    ],
        'reahl.component.commands': [
            'Xpra = reahl.workstation.xprasupport:ControlXpra',
            'Ngrok = reahl.workstation.ngroksupport:Ngrok'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
