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
    name='reahl-doc',
    version='5.2.1',
    description='Documentation and examples for Reahl.',
    long_description='Reahl is a web application framework that allows a Python programmer to work in terms of useful abstractions - using a single programming language.\n\nReahl-doc contains documentation and examples of Reahl.\n\nSee http://www.reahl.org/docs/5.1/tutorial/gettingstarted-install.d.html for installation instructions. ',
    url='http://www.reahl.org',
    maintainer='Iwan Vosloo',
    maintainer_email='iwan@reahl.org',
    packages=['reahl', 'reahl.doc', 'reahl.doc.examples', 'reahl.doc.examples.features', 'reahl.doc.examples.features.access', 'reahl.doc.examples.features.carousel', 'reahl.doc.examples.features.dynamiccontent', 'reahl.doc.examples.features.i18nexample', 'reahl.doc.examples.features.i18nexample.i18nexamplemessages', 'reahl.doc.examples.features.layout', 'reahl.doc.examples.features.pageflow', 'reahl.doc.examples.features.persistence', 'reahl.doc.examples.features.tabbedpanel', 'reahl.doc.examples.features.validation', 'reahl.doc.examples.howtos', 'reahl.doc.examples.howtos.ajaxbootstrap', 'reahl.doc.examples.howtos.ajaxbootstrap.ajaxbootstrap_dev', 'reahl.doc.examples.howtos.bootstrapsass', 'reahl.doc.examples.howtos.bootstrapsassmultihomed', 'reahl.doc.examples.howtos.chartplotly', 'reahl.doc.examples.howtos.chartplotly2', 'reahl.doc.examples.howtos.customisingerrorpages', 'reahl.doc.examples.howtos.customisingerrorpages.customisingerrorpages_dev', 'reahl.doc.examples.howtos.dynamiccontenterrors', 'reahl.doc.examples.howtos.hellodockernginx', 'reahl.doc.examples.howtos.hellonginx', 'reahl.doc.examples.howtos.optimisticconcurrency', 'reahl.doc.examples.howtos.optimisticconcurrency.optimisticconcurrency_dev', 'reahl.doc.examples.howtos.pagerbootstrap', 'reahl.doc.examples.howtos.pagerbootstrap.pagerbootstrap_dev', 'reahl.doc.examples.howtos.paymentpaypal', 'reahl.doc.examples.howtos.responsivedisclosure', 'reahl.doc.examples.howtos.responsivedisclosure.responsivedisclosure_dev', 'reahl.doc.examples.tutorial', 'reahl.doc.examples.tutorial.accessbootstrap', 'reahl.doc.examples.tutorial.accessbootstrap.accessbootstrap_dev', 'reahl.doc.examples.tutorial.addressbook1', 'reahl.doc.examples.tutorial.addressbook1.addressbook1_dev', 'reahl.doc.examples.tutorial.addressbook2', 'reahl.doc.examples.tutorial.addressbook2.addressbook2_dev', 'reahl.doc.examples.tutorial.addressbook2bootstrap', 'reahl.doc.examples.tutorial.addressbook2bootstrap.addressbook2bootstrap_dev', 'reahl.doc.examples.tutorial.addresslist', 'reahl.doc.examples.tutorial.bootstrapgrids', 'reahl.doc.examples.tutorial.componentconfigbootstrap', 'reahl.doc.examples.tutorial.componentconfigbootstrap.componentconfigbootstrap_dev', 'reahl.doc.examples.tutorial.datatablebootstrap', 'reahl.doc.examples.tutorial.datatablebootstrap.datatablebootstrap_dev', 'reahl.doc.examples.tutorial.dynamiccontent', 'reahl.doc.examples.tutorial.dynamiccontent.dynamiccontent_dev', 'reahl.doc.examples.tutorial.hello', 'reahl.doc.examples.tutorial.helloanywhere', 'reahl.doc.examples.tutorial.i18nexamplebootstrap', 'reahl.doc.examples.tutorial.i18nexamplebootstrap.i18nexamplebootstrap_dev', 'reahl.doc.examples.tutorial.i18nexamplebootstrap.i18nexamplebootstrapmessages', 'reahl.doc.examples.tutorial.jobsbootstrap', 'reahl.doc.examples.tutorial.jobsbootstrap.jobsbootstrap_dev', 'reahl.doc.examples.tutorial.login1bootstrap', 'reahl.doc.examples.tutorial.login1bootstrap.login1bootstrap_dev', 'reahl.doc.examples.tutorial.login2bootstrap', 'reahl.doc.examples.tutorial.login2bootstrap.login2bootstrap_dev', 'reahl.doc.examples.tutorial.migrationexamplebootstrap', 'reahl.doc.examples.tutorial.migrationexamplebootstrap.migrationexamplebootstrap_dev', 'reahl.doc.examples.tutorial.pageflow1', 'reahl.doc.examples.tutorial.pageflow1.pageflow1_dev', 'reahl.doc.examples.tutorial.pagelayout', 'reahl.doc.examples.tutorial.parameterised1', 'reahl.doc.examples.tutorial.parameterised2', 'reahl.doc.examples.tutorial.parameterised2.parameterised2_dev', 'reahl.doc.examples.tutorial.sessionscopebootstrap', 'reahl.doc.examples.tutorial.sessionscopebootstrap.sessionscopebootstrap_dev', 'reahl.doc.examples.tutorial.slots', 'reahl.doc.examples.tutorial.tablebootstrap', 'reahl.doc.examples.tutorial.tablebootstrap.etc', 'reahl.doc.examples.tutorial.tablebootstrap.tablebootstrap_dev', 'reahl.doc.examples.web', 'reahl.doc.examples.web.basichtmlinputs', 'reahl.doc.examples.web.basichtmlinputs.basichtmlinputs_dev', 'reahl.doc.examples.web.basichtmlwidgets', 'reahl.doc.examples.web.fileupload', 'reahl.doc_dev', 'reahl.messages'],
    py_modules=[],
    include_package_data=True,
    package_data={'': ['*/LC_MESSAGES/*.mo']},
    namespace_packages=['reahl', 'reahl.messages'],
    install_requires=['reahl-web>=5.2,<5.3', 'reahl-component>=5.2,<5.3', 'reahl-sqlalchemysupport>=5.2,<5.3', 'reahl-web-declarative>=5.2,<5.3', 'reahl-domain>=5.2,<5.3', 'reahl-domainui>=5.2,<5.3', 'reahl-commands>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-paypalsupport>=5.2,<5.3', 'pytest>=3.0', 'setuptools>=32.3.1', 'plotly>=5.1.0,<5.6.99999'],
    setup_requires=['setuptools-git>=1.1', 'pytest-runner'],
    tests_require=['pytest>=3.0', 'Sphinx', 'sphinxcontrib-plantuml', 'reahl-tofu>=5.2,<5.3', 'reahl-stubble>=5.2,<5.3', 'reahl-dev>=5.2,<5.3', 'reahl-webdev>=5.2,<5.3', 'reahl-browsertools>=5.2,<5.3', 'reahl-postgresqlsupport>=5.2,<5.3', 'reahl-sqlitesupport>=5.2,<5.3', 'reahl-mysqlsupport>=5.2,<5.3'],
    test_suite='reahl.doc_dev',
    entry_points={
        'reahl.persistlist': [
            '0 = reahl.doc.examples.features.persistence.persistence:Comment',
            '1 = reahl.doc.examples.features.dynamiccontent.dynamiccontent:Calculator',
            '2 = reahl.doc.examples.web.fileupload.fileupload:Comment',
            '3 = reahl.doc.examples.web.fileupload.fileupload:AttachedFile',
            '4 = reahl.doc.examples.tutorial.test_model2:Address',
            '5 = reahl.doc.examples.tutorial.addressbook2.addressbook2:Address',
            '6 = reahl.doc.examples.tutorial.addressbook2bootstrap.addressbook2bootstrap:Address',
            '7 = reahl.doc.examples.tutorial.addressbook1.addressbook1:Address',
            '8 = reahl.doc.examples.tutorial.pageflow1.pageflow1:Address',
            '9 = reahl.doc.examples.tutorial.parameterised1.parameterised1:Address',
            '10 = reahl.doc.examples.tutorial.parameterised2.parameterised2:Address',
            '11 = reahl.doc.examples.tutorial.sessionscopebootstrap.sessionscopebootstrap:User',
            '12 = reahl.doc.examples.tutorial.sessionscopebootstrap.sessionscopebootstrap:LoginSession',
            '13 = reahl.doc.examples.tutorial.accessbootstrap.accessbootstrap:AddressBook',
            '14 = reahl.doc.examples.tutorial.accessbootstrap.accessbootstrap:Collaborator',
            '15 = reahl.doc.examples.tutorial.accessbootstrap.accessbootstrap:Address',
            '16 = reahl.doc.examples.tutorial.i18nexamplebootstrap.i18nexamplebootstrap:Address',
            '17 = reahl.doc.examples.tutorial.componentconfigbootstrap.componentconfigbootstrap:Address',
            '18 = reahl.doc.examples.tutorial.migrationexamplebootstrap.migrationexamplebootstrap:Address',
            '19 = reahl.doc.examples.tutorial.jobsbootstrap.jobsbootstrap:Address',
            '20 = reahl.doc.examples.tutorial.tablebootstrap.tablebootstrap:Address',
            '21 = reahl.doc.examples.tutorial.datatablebootstrap.datatablebootstrap:Address',
            '22 = reahl.doc.examples.tutorial.dynamiccontent.dynamiccontent:InvestmentOrder',
            '23 = reahl.doc.examples.tutorial.dynamiccontent.dynamiccontent:Allocation',
            '24 = reahl.doc.examples.howtos.paymentpaypal.paymentpaypal:ShoppingCart',
            '25 = reahl.doc.examples.howtos.responsivedisclosure.responsivedisclosure:InvestmentOrder',
            '26 = reahl.doc.examples.howtos.responsivedisclosure.responsivedisclosure:Allocation',
            '27 = reahl.doc.examples.howtos.responsivedisclosure.responsivedisclosure:IDDocument'    ],
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
            'reahl-component = egg:5.2',
            'reahl-sqlalchemysupport = egg:5.2',
            'reahl-web-declarative = egg:5.2',
            'reahl-domain = egg:5.2',
            'reahl-domainui = egg:5.2',
            'reahl-commands = egg:5.2',
            'reahl-dev = egg:5.2',
            'reahl-paypalsupport = egg:5.2',
            'pytest = thirdpartyegg:3.0',
            'setuptools = thirdpartyegg:32.3.1',
            'plotly = thirdpartyegg:5.1.0 [5.6.99999]'    ],
        'reahl.versiondeps.5.1': [
            'reahl-web = egg:5.1',
            'reahl-component = egg:5.1',
            'reahl-sqlalchemysupport = egg:5.1',
            'reahl-web-declarative = egg:5.1',
            'reahl-domain = egg:5.1',
            'reahl-domainui = egg:5.1',
            'reahl-commands = egg:5.1',
            'reahl-dev = egg:5.1',
            'pytest = thirdpartyegg:3.0',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.5.0': [
            'reahl-web = egg:5.0',
            'reahl-component = egg:5.0',
            'reahl-sqlalchemysupport = egg:5.0',
            'reahl-web-declarative = egg:5.0',
            'reahl-domain = egg:5.0',
            'reahl-domainui = egg:5.0',
            'reahl-commands = egg:5.0',
            'pytest = thirdpartyegg:3.0',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.4.0': [
            'reahl-web = egg:4.0',
            'reahl-component = egg:4.0',
            'reahl-sqlalchemysupport = egg:4.0',
            'reahl-web-declarative = egg:4.0',
            'reahl-domain = egg:4.0',
            'reahl-domainui = egg:4.0',
            'reahl-commands = egg:4.0',
            'pytest = thirdpartyegg:3.0',
            'setuptools = thirdpartyegg:32.3.1'    ],
        'reahl.versiondeps.3.2': [
            'reahl-web = egg:3.2',
            'reahl-component = egg:3.2',
            'reahl-sqlalchemysupport = egg:3.2',
            'reahl-web-declarative = egg:3.2',
            'reahl-domain = egg:3.2',
            'reahl-domainui = egg:3.2',
            'nose = thirdpartyegg:_'    ],
        'reahl.versiondeps.3.1': [
            'reahl-web = egg:3.1',
            'reahl-component = egg:3.1',
            'reahl-sqlalchemysupport = egg:3.1',
            'reahl-web-declarative = egg:3.1',
            'reahl-domain = egg:3.1',
            'reahl-domainui = egg:3.1'    ],
        'reahl.versiondeps.3.0': [
            'reahl-web = egg:3.0',
            'reahl-component = egg:3.0',
            'reahl-sqlalchemysupport = egg:3.0',
            'reahl-web-declarative = egg:3.0',
            'reahl-domain = egg:3.0',
            'reahl-domainui = egg:3.0'    ],
        'reahl.versiondeps.2.1': [
            'reahl-web = egg:2.1',
            'reahl-component = egg:2.1',
            'reahl-sqlalchemysupport = egg:2.1',
            'reahl-web-elixirimpl = egg:2.1',
            'reahl-domain = egg:2.1',
            'reahl-domainui = egg:2.1'    ],
        'reahl.versiondeps.2.0': [
            'reahl-web = egg:2.0',
            'reahl-component = egg:2.0',
            'reahl-sqlalchemysupport = egg:2.0',
            'reahl-web-elixirimpl = egg:2.0',
            'reahl-domain = egg:2.0',
            'reahl-domainui = egg:2.0'    ],
        'reahl.configspec': [
            'config = reahl.doc.examples.tutorial.componentconfigbootstrap.componentconfigbootstrap:AddressConfig'    ],
        'reahl.scheduled_jobs': [
            'reahl.doc.examples.tutorial.jobsbootstrap.jobsbootstrap:Address.clear_added_flags = reahl.doc.examples.tutorial.jobsbootstrap.jobsbootstrap:Address.clear_added_flags'    ],
        'reahl.component.commands': [
            'GetExample = reahl.doc.commands:GetExample',
            'ListExamples = reahl.doc.commands:ListExamples'    ],
        'reahl.translations': [
            'reahl-doc = reahl.messages'    ],
        'reahl.eggs': [
            'Egg = reahl.component.eggs:ReahlEgg'    ],
                 },
    extras_require={'pillow': ['Pillow>=2.5,<7.1.999']},
    cmdclass={'install_test_dependencies': InstallTestDependencies}
)
