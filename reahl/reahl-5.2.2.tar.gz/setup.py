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
    name='reahl',
    version='5.2.2',
    description='The Reahl web framework.',
    long_description='Reahl is a web application framework for Python programmers.\n\nWith Reahl, programming is done purely in Python, using concepts familiar from GUI programming---like reusable Widgets and Events. There\'s no need for a programmer to know several different languages (HTML, JavaScript, template languages, etc) or to keep up with the tricks of these trades. The abstractions presented by Reahl relieve the programmer from the burden of dealing with the annoying problems of the web: security, accessibility, progressive enhancement (or graceful degradation) and browser quirks.\n\nReahl consists of many different eggs that are not all needed all of the time. This package does not contain much itself, but is an entry point for installing a set of Reahl eggs:\n\nInstall Reahl by installing with extras, eg: pip install "reahl[declarative,sqlite,dev,doc]" to install everything needed to run Reahl on sqlite, the dev tools and documentation. (On Windows platforms, use easy_install instead of pip.)\n\nSee http://www.reahl.org/docs/5.2/tutorial/gettingstarted-install.d.html for installation instructions. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=[],
    py_modules=[],
    include_package_data=False,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=[],
    install_requires=[],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0'],
    test_suite='tests',
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
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={'all': ['reahl-component>=5.2,<5.3', 'reahl-web>=5.2,<5.3', 'reahl-mailutil>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'reahl-domainui>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3', 'reahl-sqlitesupport>=5.2,<5.3', 'reahl-mysqlsupport>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-tofu>=5.2,<5.3', 'reahl-doc>=5.2,<5.3'], 'web': ['reahl-component>=5.2,<5.3', 'reahl-web>=5.2,<5.3', 'reahl-mailutil>=5.2,<5.3'], 'sqlite': ['reahl-sqlitesupport>=5.2,<5.3'], 'postgresql': ['reahl-postgresqlsupport>=5.2,<5.3'], 'mysql': ['reahl-mysqlsupport>=5.2,<5.3'], 'declarative': ['reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'reahl-domainui>=5.2,<5.3'], 'dev': ['reahl-dev>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-tofu>=5.2,<5.3'], 'doc': ['reahl-doc>=5.2,<5.3']},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
