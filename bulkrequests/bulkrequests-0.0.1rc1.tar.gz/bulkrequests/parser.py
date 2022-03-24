# bulkrequests
# Copyright (C) 2022  Dario Graña, Pau Tallada
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program;  If not, see <https://www.gnu.org/licenses/>.


'''
dCache BulkRequests parser
'''

import argparse  # used for argument parsing
import configparser  # used to parse configfile
import os  # used for many os requirements
import logging  # used for logging pourposes


# setup default client file
DEFAULT_RC_PATH = '$HOME/.bulkrequestsrc'

# get environment variables
ENV_USER = os.getenv('BULKREQUESTS_USER')
ENV_PWD = os.getenv('BULKREQUESTS_PWD')
ENV_URL = os.getenv('BULKREQUESTS_URL')
ENV_OIDC_AGENT_ACC = os.getenv('BULKREQUESTS_OIDC_AGENT_ACC')
ENV_CERTIFICATE = os.getenv('BULKREQUESTS_CERTIFICATE')
ENV_PRIVATE_KEY = os.getenv('BULKREQUESTS_PRIVATE_KEY')
ENV_X509_PROXY = os.getenv('BULKREQUESTS_X509_PROXY')
ENV_CA_CERTIFICATE = os.getenv('BULKREQUESTS_CA_CERTIFICATE')
ENV_CA_DIRECTORY = os.getenv('BULKREQUESTS_CA_DIRECTORY')
ENV_NO_CHECK_CERT = os.getenv('BULKREQUESTS_NO_CHECK_CERT')


class BulkRequestsParser():
    '''
    BulkRequests parser Class. Creates a parser with argparse, adds the arguments
    loads the parameters and stores it localy.
    It can also parse a file with filenames to be managed by BulkRequests
    '''

    def __init__(self):
        # bulkrequests parser creation

        self.parser = argparse.ArgumentParser()
        self.add_arguments_to_parser()
        self.args = None
        self.params = dict()
        self.filenames = None
        self.arg_parse_ok = False
        self.filename_parse_ok = False

    def add_arguments_to_parser(self):
        '''
        adds all necessary arguments to the parser
        '''

        self.parser.add_argument('-u', '--user', type=str, help='username for dCache')
        self.parser.add_argument('-p', '--pwd', type=str, help='password for dCache')
        self.parser.add_argument('--oidc-agent-account', type=str, help='oidc agent account to be used')
        self.parser.add_argument('-f', '--file', type=str, help='reads a file from cli')
        self.parser.add_argument('-j', '--threads', type=int, default=1, help='how many threads should be created')
        self.parser.add_argument('--url', type=str, help='takes a url from cli')
        self.parser.add_argument('--certificate', type=str, help='certificate to use')
        self.parser.add_argument('--private-key', type=str, help='private key to use')
        self.parser.add_argument('--x509-proxy', type=str, help='x509 proxy to use')
        self.parser.add_argument('--ca-certificate', type=str, help='CA certificate to use')
        self.parser.add_argument('--ca-directory', type=str, help='takes a CA directory from cli')
        self.parser.add_argument('--no-check-certificate', action='store_true', help='Dont validate the servers certificate')
        self.parser.add_argument('-c', '--config', type=str, help='reads a config file')
        self.parser.add_argument('--get-locality', action='store_true', help='print file locality')
        self.parser.add_argument('--get-qos', action='store_true', help='print file qos')
        self.parser.add_argument('--set-qos', type=str, choices=['disk', 'tape', 'disk+tape'], help='set file qos')
        self.parser.add_argument('--size', action='store_true', default=False, help='report query size for get_qos and get_locality')
        self.parser.add_argument('--human', action='store_true', default=False, help='print in a human readable format')
        self.parser.add_argument('-q', '--quiet', action='store_true', default=False, help='shows only a summary')
        self.parser.add_argument('-r', '--recursive', action='store_true', help='manipulate directories recursively')
        self.parser.add_argument('-d', '--debug', action='store_true', help='show debug information')
        self.parser.add_argument('dcachepath', type=str, nargs='?', help='takes a dcache path')

    def get_parameters(self):
        '''
        orchestates the parsing actions
        '''

        self.args = self.parser.parse_args()

        self.load_params_from_cli_args()

        self._params_sanity_check()

        if self.params['file'] is not None and self.arg_parse_ok:
            self.parse_user_filenames_file(self.params['file'])

        elif self.params['dcachepath'] is not None and self.arg_parse_ok:
            self.filenames = self.params['dcachepath']

        else:
            logging.debug('There were problems loading arguments')
            self.parser.print_help()
            self.arg_parse_ok = False

        return self.arg_parse_ok

    def load_params_from_cli_args(self):
        '''
        parses a configfile, environment vars or the cli options
        and loads all arguments into a dict
        '''

        path = os.path.expandvars(DEFAULT_RC_PATH)
        if os.access(path, os.R_OK):  # parse $HOME/.dcacheclientrc
            self.parse_configfile(path)

        else:
            # initialize all necessary dict values with default value
            self.params['user'] = None
            self.params['pwd'] = None
            self.params['url'] = None
            self.params['oidc_agent_account'] = None
            self.params['certificate'] = None
            self.params['private_key'] = None
            self.params['x509_proxy'] = None
            self.params['ca_certificate'] = None
            self.params['ca_directory'] = None
            self.params['no_check_certificate'] = None
            self.arg_parse_ok = False

        if self.args.config is not None:
            # parse config file passed from cli
            path = os.path.expandvars(self.args.config)
            self.parse_configfile(path)

        if self.args.user is not None:
            # load username from arguments
            self.params['user'] = self.args.user

        if self.args.pwd is not None:
            # load username from arguments
            self.params['pwd'] = self.args.pwd

        elif self.args.oidc_agent_account is not None:
            # load necessary variables for oidc_agent_account
            self.params['oidc_agent_account'] = self.args.oidc_agent_account

        elif ENV_USER is not None and ENV_PWD is not None:
            # load necessary variables from environment
            self.params['user'] = ENV_USER
            self.params['pwd'] = ENV_PWD

        elif ENV_OIDC_AGENT_ACC is not None:
            # load oidc agent account from environment variables
            self.params['oidc_agent_account'] = ENV_OIDC_AGENT_ACC
            if self.args.oidc_agent_account is not None:
                # load oidc agent account from cli
                self.params['oidc_agent_account'] = self.args.oidc_agent_account

        if self.args.url is not None:
            # load endpoint url from cli
            self.params['url'] = self.args.url
        elif ENV_URL is not None:
            # load endpoint url from environment variables
            self.params['url'] = ENV_URL

        if self.args.certificate is not None:
            # load certificate from cli
            self.params['certificate'] = self.args.certificate
        elif ENV_CERTIFICATE is not None:
            # load certificate from environment variables
            self.params['certificate'] = ENV_CERTIFICATE

        if self.args.private_key is not None:
            # load private_key from cli
            self.params['private_key'] = self.args.private_key
        elif ENV_PRIVATE_KEY is not None:
            # load private_key from environment variables
            self.params['private_key'] = ENV_PRIVATE_KEY

        if self.args.x509_proxy is not None:
            # load x509_proxy from cli
            self.params['x509_proxy'] = self.args.x509_proxy
        elif ENV_X509_PROXY is not None:
            # load x509_proxy from environment variables
            self.params['x509_proxy'] = ENV_X509_PROXY

        if self.args.ca_certificate is not None:
            # load ca_certificate from cli
            self.params['ca_certificate'] = self.args.ca_certificate
        elif ENV_CA_CERTIFICATE is not None:
            # load ca_certificate from environment variables
            self.params['ca_certificate'] = ENV_CA_CERTIFICATE

        if self.args.ca_directory is not None:
            # load CA directory from cli
            self.params['ca_directory'] = self.args.ca_directory
        elif ENV_CA_DIRECTORY is not None:
            # load CA directory from environment variables
            self.params['ca_directory'] = ENV_CA_DIRECTORY

        if self.args.no_check_certificate is not None:
            # load no check certificate from cli
            self.params['no_check_certificate'] = self.args.no_check_certificate
        elif ENV_CA_DIRECTORY is not None:
            # load no check certificate from environment variables
            self.params['no_check_certificate'] = ENV_CA_DIRECTORY

        if self.args.debug:
            # setup debug log level
            logging.getLogger().setLevel(logging.DEBUG)

        # setup local options
        self.params['debug'] = self.args.debug
        self.params['recursive'] = self.args.recursive
        self.params['quiet'] = self.args.quiet

        self.params['dcachepath'] = self.args.dcachepath
        self.params['file'] = self.args.file
        self.params['threads'] = self.args.threads

        self.params['get_locality'] = self.args.get_locality
        self.params['get_qos'] = self.args.get_qos
        self.params['set_qos'] = self.args.set_qos
        self.params['size'] = self.args.size
        self.params['human'] = self.args.human

        self.arg_parse_ok = True

    def parse_configfile(self, path):
        '''
        parse a configuration file located in path
        '''

        if os.access(path, os.R_OK):  # the file exists and I can read it
            config = configparser.ConfigParser()
            config.read(path)
            default_section = config['DEFAULT']
            self.params['user'] = default_section.get('user', None)
            self.params['pwd'] = default_section.get('pwd', None)
            self.params['url'] = default_section.get('url', None)
            self.params['oidc_agent_account'] = default_section.get('oidc-agent-account', None)
            self.params['certificate'] = default_section.get('certificate', None)
            self.params['private_key'] = default_section.get('private_key', None)
            self.params['x509_proxy'] = default_section.get('x509-proxy', None)
            self.params['ca_certificate'] = default_section.get('ca-certificate', None)
            self.params['ca_directory'] = default_section.get('ca-directory', None)
            self.params['no_check_certificate'] = default_section.get('no-check-certificate', None)

        else:
            logging.error('No configfile found at %s or it is not accessible', path)
            self.arg_parse_ok = False

    def parse_user_filenames_file(self, path):
        '''
        takes the path of a file and parses the file.
        The file must contain paths to files or directories into dCache.
        '''

        access_ok = os.access(path, os.R_OK)

        if access_ok:
            # file in path can be readed
            with open(path, mode='r') as files:
                paths = files.readlines()
                self.filenames = [path.strip() for path in paths]
                self.filename_parse_ok = True
        else:
            logging.error('File %s cannot be readed', path)
            self.filename_parse_ok = False

    def _params_sanity_check(self):
        '''
        check if params contains enough information to create a connection
        '''

        user_and_pass = self.params['user'] is None or self.params['pwd'] is None
        token = self.params['oidc_agent_account'] is None
        x509_proxy = self.params['x509_proxy'] is None

        if user_and_pass and token and x509_proxy:
            logging.error('No authentication method found')
            self.arg_parse_ok = False

        if self.params['url'] is None:
            logging.error('No URL found')
            self.arg_parse_ok = False

        if self.params['dcachepath'] is None and self.params['file'] is None:
            logging.error('No files or paths were provided')
            self.arg_parse_ok = False

        if self.params['dcachepath'] is not None and self.params['file'] is not None:
            logging.error('Options file and dcachepath are mutualy exclusive')
            self.arg_parse_ok = False

        if self.params['get_locality'] is False and self.params['get_qos'] is False and self.params['set_qos'] is None:
            logging.error('No actions were provided')
            self.arg_parse_ok = False

        if self.params['size'] is True and self.params['get_qos'] is False and self.params['get_locality'] is False:
            logging.error('The size options should be used with the --get-qos or --get-locality options')
            self.arg_parse_ok = False
