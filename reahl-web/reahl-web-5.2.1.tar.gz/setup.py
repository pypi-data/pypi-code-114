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
    name='reahl-web',
    version='5.2.1',
    description='The core Reahl web framework',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis package contains the core of the Reahl framework.\n\nSee http://www.reahl.org/docs/5.1/tutorial/gettingstarted-install.d.html for installation instructions. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.messages', 'reahl.web', 'reahl.web.bootstrap', 'reahl.web.holder', 'reahl.web.static', 'reahl.web.static.jquery', 'reahl.web_dev', 'reahl.web_dev.advanced', 'reahl.web_dev.advanced.subresources', 'reahl.web_dev.appstructure', 'reahl.web_dev.bootstrap', 'reahl.web_dev.inputandvalidation', 'reahl.web_dev.widgets'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-mailutil>=5.2,<5.3', 'ply>=3.8,<3.11.999', 'rjsmin>=1.2.0,<1.2.999', 'rcssmin>=1.1.0,<1.1.999', 'beautifulsoup4>=4.6,<4.10.999', 'WebOb>=1.8,<1.8.999', 'Babel>=2.1,<2.9.999', 'setuptools>=32.3.1', 'lxml>=4.2,<4.7.999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'plotly>=5.1.0,<5.6.99999', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3', 'reahl-dev>=5.2,<5.3'],
    test_suite='reahl.web_dev',
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
            'reahl-mailutil = egg:5.2',
            'ply = thirdpartyegg:3.8 [3.11.999]',
            'rjsmin = thirdpartyegg:1.2.0 [1.2.999]',
            'rcssmin = thirdpartyegg:1.1.0 [1.1.999]',
            'beautifulsoup4 = thirdpartyegg:4.6 [4.10.999]',
            'WebOb = thirdpartyegg:1.8 [1.8.999]',
            'Babel = thirdpartyegg:2.1 [2.9.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'lxml = thirdpartyegg:4.2 [4.7.999]'    ],
        'reahl.versiondeps.5.1': [
            'reahl-component = egg:5.1',
            'reahl-mailutil = egg:5.1',
            'ply = thirdpartyegg:3.8 [3.11.999]',
            'slimit = thirdpartyegg:0.8 [0.8.999]',
            'cssmin = thirdpartyegg:0.2 [0.2.999]',
            'beautifulsoup4 = thirdpartyegg:4.6 [4.6.999]',
            'WebOb = thirdpartyegg:1.8 [1.8.999]',
            'Babel = thirdpartyegg:2.1 [2.8.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'lxml = thirdpartyegg:4.2 [4.5.999]'    ],
        'reahl.versiondeps.5.0': [
            'reahl-component = egg:5.0',
            'reahl-mailutil = egg:5.0',
            'ply = thirdpartyegg:3.8 [3.11.999]',
            'slimit = thirdpartyegg:0.8 [0.8.999]',
            'cssmin = thirdpartyegg:0.2 [0.2.999]',
            'beautifulsoup4 = thirdpartyegg:4.6 [4.6.999]',
            'WebOb = thirdpartyegg:1.8 [1.8.999]',
            'Babel = thirdpartyegg:2.1 [2.8.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'lxml = thirdpartyegg:4.2 [4.5.999]'    ],
        'reahl.versiondeps.4.0': [
            'reahl-component = egg:4.0',
            'reahl-mailutil = egg:4.0',
            'ply = thirdpartyegg:3.8 [3.8.999]',
            'slimit = thirdpartyegg:0.8 [0.8.999]',
            'cssmin = thirdpartyegg:0.2 [0.2.999]',
            'BeautifulSoup4 = thirdpartyegg:4.6 [4.6.999]',
            'webob = thirdpartyegg:1.4 [1.4.999]',
            'Babel = thirdpartyegg:2.1 [2.1.999]',
            'setuptools = thirdpartyegg:32.3.1',
            'lxml = thirdpartyegg:4.2 [4.2.999]'    ],
        'reahl.versiondeps.3.2': [
            'reahl-component = egg:3.2',
            'ply = thirdpartyegg:3.8 [3.8.999]',
            'slimit = thirdpartyegg:0.8 [0.8.999]',
            'cssmin = thirdpartyegg:0.2 [0.2.999]',
            'BeautifulSoup4 = thirdpartyegg:4.3 [4.3.999]',
            'webob = thirdpartyegg:1.4 [1.4.999]',
            'Babel = thirdpartyegg:2.1 [2.1.999]'    ],
        'reahl.versiondeps.3.1': [
            'reahl-component = egg:3.1',
            'ply = thirdpartyegg:3.8 [3.8.999]',
            'slimit = thirdpartyegg:0.8 [0.8.999]',
            'cssmin = thirdpartyegg:0.2 [0.2.999]',
            'BeautifulSoup4 = thirdpartyegg:4.3 [4.3.999]',
            'webob = thirdpartyegg:1.4 [1.4.999]',
            'Babel = thirdpartyegg:2.1 [2.1.999]'    ],
        'reahl.versiondeps.3.0': [
            'reahl-component = egg:3.0',
            'reahl-interfaces = egg:3.0',
            'slimit = thirdpartyegg:0.8 [0.8.999]',
            'cssmin = thirdpartyegg:0.2 [0.2.999]',
            'BeautifulSoup4 = thirdpartyegg:4.3 [4.3.999]',
            'webob = thirdpartyegg:1.4 [1.4.999]',
            'Babel = thirdpartyegg:1.3 [1.3.999]'    ],
        'reahl.versiondeps.2.1': [
            'reahl-component = egg:2.1',
            'reahl-interfaces = egg:2.1',
            'slimit = thirdpartyegg:0.8 [0.9]',
            'cssmin = thirdpartyegg:0.1 [0.2]',
            'BeautifulSoup = thirdpartyegg:3.2 [3.3]',
            'webob = thirdpartyegg:1.2 [1.3]',
            'Babel = thirdpartyegg:0.9 [0.10]'    ],
        'reahl.versiondeps.2.0': [
            'reahl-component = egg:2.0',
            'reahl-interfaces = egg:2.0',
            'slimit = thirdpartyegg:0.8 [0.9]',
            'cssmin = thirdpartyegg:0.1 [0.2]',
            'BeautifulSoup = thirdpartyegg:3.2 [3.3]',
            'webob = thirdpartyegg:1.2 [1.3]',
            'Babel = thirdpartyegg:0.9 [0.10]'    ],
        'reahl.configspec': [
            'config = reahl.web.egg:WebConfig'    ],
        'reahl.translations': [
            'reahl-web = reahl.messages'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
