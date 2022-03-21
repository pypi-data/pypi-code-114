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
    name='reahl-paypalsupport',
    version='5.2.1',
    description='Support for payments via PayPal.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nThis package contains add-on facilities using which you can process payments via PayPal. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.messages', 'reahl.paypalsupport'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-component>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'setuptools>=32.3.1', 'paypal-checkout-serversdk'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3'],
    test_suite='tests',
    entry_points={
        'reahl.persistlist': [
            '0 = reahl.paypalsupport.paypalsupport:PayPalOrder'    ],
        'reahl.versions': [
            '5.2 = 5.2'    ],
        'reahl.versiondeps.5.2': [
            'reahl-component = egg:5.2',
            'reahl-sqlalchemysupport = egg:5.2',
            'reahl-web = egg:5.2',
            'reahl-web-declarative = egg:5.2',
            'reahl-domain = egg:5.2',
            'setuptools = thirdpartyegg:32.3.1',
            'paypal-checkout-serversdk = thirdpartyegg:_'    ],
        'reahl.migratelist.5.2': [
            '0 = reahl.paypalsupport.migrations:CreatePaypal'    ],
        'reahl.configspec': [
            'config = reahl.paypalsupport.paypalconfig:PayPalSiteConfig'    ],
        'reahl.translations': [
            'reahl-paypalsupport = reahl.messages'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
