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
    name='reahl-mailutil',
    version='5.2.1',
    description='Simple utilities for sending email from Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-mailutil is a simple library for sending emails (optionally from ReST sources). ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.mailutil', 'reahl.mailutil_dev'],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl'],
    install_requires=['reahl-component>=5.2,<5.3', 'docutils>=0.14,<0.18.999', 'Pygments>=2.1.0,<2.11.999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3'],
    test_suite='reahl.mailutil_dev',
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
            'docutils = thirdpartyegg:0.14 [0.18.999]',
            'Pygments = thirdpartyegg:2.1.0 [2.11.999]'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'docutils = thirdpartyegg:0.14 [0.16.999]',
            'Pygments = thirdpartyegg:2.1.0 [2.6.999]'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'docutils = thirdpartyegg:0.14 [0.16.999]',
            'Pygments = thirdpartyegg:2.1.0 [2.6.999]'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'docutils = thirdpartyegg:0.12 [0.12.999]',
            'Pygments = thirdpartyegg:2.1.0 [2.1.999]'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'docutils = thirdpartyegg:0.12 [0.12.999]',
            'Pygments = thirdpartyegg:2.1.0 [2.1.999]'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'docutils = thirdpartyegg:0.12 [0.12.999]'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'docutils = thirdpartyegg:0.12 [0.12]'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'docutils = thirdpartyegg:0.8 [0.9]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'docutils = thirdpartyegg:0.8 [0.9]'    ],
        'reahl.configspec': [
            'config = reahl.mailutil.reusableconfig:MailConfig'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
