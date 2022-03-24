""" Prisma Cloud API Configuration and Library """

import logging
import os
import json

import click

import prismacloud.version

from prismacloud.pc_lib import pc_api


def pc_config():
    """ map pc configuration to pc_lib configuration """
    click.get_current_context()
    settings = get_config()
    # Map settings from this pc cli to the pc_lib/pc_api library.
    return {
        'api':         settings['api_endpoint'],
        'api_compute': settings['pcc_api_endpoint'],
        'username':    settings['access_key_id'],
        'password':    settings['secret_key'],
        'ca_bundle':   False
    }


def get_endpoint(endpoint, query_params=None, api='cwpp'):
    """ make a GET request without using the pc_lib library """
    pc_api.configure(pc_config())
    logging.debug('Calling API Endpoint: %s', endpoint)
    result = None
    if api == 'cspm':
        result = pc_api.execute('GET', endpoint, query_params)
    if api == 'cwpp':
        if not endpoint.startswith('api'):
            endpoint = 'api/v1/%s' % endpoint
        result = pc_api.execute_compute('GET', endpoint, query_params)
    if api == 'code':
        result = pc_api.execute_code_security('GET', endpoint, query_params)
    return result


def get_config():
    """ read or write configuration from or to a file """
    params = click.get_current_context().find_root().params
    # To fix calling 'pc' without a command.
    if 'configuration' not in params:
        params['configuration'] = 'credentials'
    logging.info('Running prismacloud-cli version %s', prismacloud.version.version)
    config_directory = os.environ['HOME'] + '/.prismacloud/'
    config_file_name = config_directory + params['configuration'] + '.json'
    if not os.path.exists(config_directory):
        logging.info('Configuration directory does not exist, creating $HOME/.prismacloud')
        try:
            os.makedirs(config_directory)
        except Exception as ex:
            logging.info(ex)
    if os.path.exists(config_directory + params['configuration'] + '.json'):
        try:
            config_file_settings = read_config_file(config_file_name)
        except Exception as ex:
            logging.info(ex)
        logging.debug('Configuration loaded from file: %s', config_file_name)
    else:
        config_file_settings = {
            'api_endpoint':     input('Enter your CSPM API URL (Optional if PCCE), eg: api.prismacloud.io: '),
            'pcc_api_endpoint': input('Enter your CWPP API URL (Optional if PCEE), eg: example.cloud.twistlock.com/tenant or twistlock.example.com: '),
            'access_key_id':    input('Enter your Access Key (or Username if PCCE): '),
            'secret_key':       input('Enter your Secret Key (or Password if PCCE): ')
        }
        json_string = json.dumps(config_file_settings, sort_keys=True, indent=4)
        with open(config_file_name, 'w') as config_file:
            config_file.write(json_string)
            logging.debug('Configuration written to file: %s', config_file_name)
    return config_file_settings


def read_config_file(config_file_name):
    """ read configuration from a file """
    logging.debug('Reading configuration from file: %s', config_file_name)
    try:
        with open(config_file_name, 'r') as config_file:
            config_file_settings = json.load(config_file)
    except Exception as ex:
        logging.info(ex)
    if not ('api_endpoint' in config_file_settings and config_file_settings['api_endpoint']):
        config_file_settings['api_endpoint'] = ''
    return config_file_settings

pc_api.configure(pc_config())
