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
BulkRequests cli client
'''

import logging
from queue import Queue
from bulkrequests import clirequests
from bulkrequests import parser
from bulkrequests import constants
from bulkrequests import dcquery


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def process_request(paths, params):
    '''
    manage bulkrequests calls according to user requeriments
    '''

    connections = Queue()  # thread safe queue for bulkrequests connections

    # create a queue with many connections as threads
    for thread in range(params['threads']):
        connections.put(dcquery.BulkRequests(params))

    if params['get_qos']:
        if params['size']:
            clirequests.process_get_qos_and_size(connections, paths, params)

        else:
            clirequests.process_get_qos(connections, paths, params)

    elif params['get_locality']:
        if params['size']:
            clirequests.process_get_locality_and_size(connections, paths, params)

        else:
            clirequests.process_get_locality(connections, paths, params)

    elif params['set_qos'] == constants.DISK_TAPE_QOS:
        clirequests.process_set_qos(connections, paths, params)

    elif params['set_qos'] == constants.TAPE_QOS:
        clirequests.process_set_qos(connections, paths, params)

    elif params['set_qos'] == constants.DISK_QOS:
        logging.error('This option is not implemented yet')

    else:
        logging.debug('no option recognized %s', params)


def main():
    '''
    main function
    '''

    try:
        bkparser = parser.BulkRequestsParser()
        parse_ok = bkparser.get_parameters()
        if parse_ok:
            params = bkparser.params
            bulkrequest = dcquery.BulkRequests(params)

            if params['recursive']:
                # get all files absolute paths
                paths = bulkrequest.get_all_absolute_paths(bkparser.filenames)

            else:
                # remove directories from the list
                paths = bulkrequest.remove_dirs(bkparser.filenames)

            process_request(paths, params)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
