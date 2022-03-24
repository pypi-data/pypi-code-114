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
dCache client querys
'''

import logging  # logs management
import os.path  # necessary for path join
from queue import LifoQueue  # FIFO queue implementation
from dcacheclient import client  # dCache client used for connection
import urllib3  # used to disable SSL warnings

from bulkrequests import constants

#     Disable SSL Warnings
urllib3.disable_warnings()


class BulkRequests():
    '''
    class to manage dCache bulk requests
    '''

    def __init__(self, params):
        # dCache client creation
        if params['url'] is not None:
            self.connection = client.Client(url=params['url'],
                                            username=params['user'],
                                            password=params['pwd'],
                                            oidc_agent_account=params['oidc_agent_account'],
                                            certificate=params['certificate'],
                                            private_key=params['private_key'],
                                            x509_proxy=params['x509_proxy'],
                                            ca_certificate=params['ca_certificate'],
                                            ca_directory=params['ca_directory'],
                                            no_check_certificate=params['no_check_certificate'])

        else:
            logging.error('No door was provided to create a bulkrequest client')

    def get_locality(self, file_path):
        '''
        takes a dcache client and a file path.
        returns a str with the file_path locality.
        '''

        result = None

        if isinstance(file_path, str):

            response = self.connection.namespace.get_file_attributes(path=file_path, locality=True)

            if not response:
                logging.error('There was an error with the response.')
                result = None

            elif response[constants.JSON_FILETYPE] == constants.JSON_REGULAR_FILETYPE:
                result = response[constants.JSON_FILELOCALITY]

        else:
            logging.error('Errors with the path: %s', file_path)

        return result

    def get_locality_and_size(self, file_path):
        '''
        takes a dcache client and a string.
        returns a tuple with the file_path locality and the file_path size
        '''

        result = None

        if isinstance(file_path, str):

            response = self.connection.namespace.get_file_attributes(path=file_path, locality=True)

            if not response:
                logging.error('There was an error with the response.')
                result = None

            elif response[constants.JSON_FILETYPE] == constants.JSON_REGULAR_FILETYPE:
                result = (response[constants.JSON_FILELOCALITY], response[constants.JSON_SIZE])

        else:
            logging.error('Errors with the path: %s', file_path)

        return result

    def get_children(self, file_path):
        '''
        takes a dcache client and a file path.
        returns a str with the childrens.
        '''

        result = dict()

        if isinstance(file_path, str):

            response = self.connection.namespace.get_file_attributes(path=file_path, children=True)

            if not response:
                logging.error('There was an error with the response.')
                result = None

            elif response[constants.JSON_FILETYPE] == constants.JSON_DIR_FILETYPE:
                result = response[constants.JSON_CHILDREN]

        return result

    def get_qos(self, file_path):
        '''
        takes a dcache client and a file path.
        returns a str with the file qos
        '''

        result = None

        if isinstance(file_path, str):

            response = self.connection.namespace.get_file_attributes(path=file_path, qos=True)

            if not response:
                logging.error('There was an error with the response.')
                result = None

            else:
                result = response[constants.JSON_CURRENTQOS]

        return result

    def get_qos_and_size(self, file_path):
        '''
        takes a dcache client and a file path.
        returns a tuple with the file qos and size
        '''

        result = None

        if isinstance(file_path, str):

            response = self.connection.namespace.get_file_attributes(path=file_path, qos=True)

            if not response:
                logging.error('There was an error with the response.')
                result = None

            else:
                result = (response[constants.JSON_CURRENTQOS], response[constants.JSON_SIZE])

        return result

    def set_qos(self, file_path, new_qos):
        '''
        takes a file path and the qos to apply

        '''

        result = None

        if isinstance(file_path, str):

            response = self.connection.namespace.cmr_resources(path=file_path, body={"action": "qos", "target": new_qos})

            if not response:
                logging.error('Errors with the connection.')
                result = None

            else:
                result = response

        return result

    def set_files_online(self, file_path):
        '''
        takes all files in file_paths and brings them online
        '''

        result = None

        if isinstance(file_path, str):
            result = self.set_qos(file_path, constants.DISK_TAPE_QOS)

            if not result:
                logging.error('Errors trying to set qos: %s', result)

        return result

    def set_files_offline(self, file_path):
        '''
        takes all files in file_paths and brings them offline
        '''

        result = None

        if isinstance(file_path, str):
            result = self.set_qos(file_path, constants.TAPE_QOS)

            if not result:
                logging.error('Errors trying to set qos: %s', result)

        return result

    def remove_dirs(self, file_paths):
        '''
        takes a list of filepaths or a str
        returns a list with only regular files filepaths
        '''

        if isinstance(file_paths, str):
            file_paths = [file_paths]

        # rebuild file_paths to remove all subdirs
        for file_path in file_paths:
            if self.get_children(file_path) == {}:  # file_path has not children, i.e. is a regular file
                yield file_path

    def get_all_absolute_paths(self, file_paths):
        '''
        gets absolute paths for all files and subdirs in file_paths
        '''

        file_stack = LifoQueue()

        if isinstance(file_paths, str):
            file_paths = [file_paths]

        for file_path in file_paths:
            file_stack.put(file_path)

        while not file_stack.empty():
            file_path = file_stack.get()
            childrens = self.get_children(file_path)

            if childrens == {}:
                yield file_path

            else:
                for children in childrens:
                    if children[constants.JSON_FILETYPE] == constants.JSON_REGULAR_FILETYPE:
                        yield os.path.join(file_path, children[constants.JSON_FILENAME])
                    else:
                        file_stack.put(os.path.join(file_path, children[constants.JSON_FILENAME]))
