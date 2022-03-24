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
BulkRequests cli requests
'''

import concurrent.futures
from humanize import naturalsize
import logging
from alive_progress import alive_bar
from bulkrequests import constants


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def process_get_qos_and_size(connections, paths, params):
    '''
    manage get_qos request. Takes a queue of bulkrequests connections,
    a list of paths and the parser params.
    '''

    qos_result = dict()
    qos_result[constants.DISK_QOS] = 0
    qos_result[constants.TAPE_QOS] = 0
    qos_result[constants.DISK_TAPE_QOS] = 0

    size_result = dict()
    size_result[constants.DISK_QOS] = 0
    size_result[constants.TAPE_QOS] = 0
    size_result[constants.DISK_TAPE_QOS] = 0

    future = list()  # list to save future of threads

    def get_qos_and_size(path):
        '''
        get_qos_and_size function for threading purposes
        '''

        connection = connections.get()  # get a bulkrequest connection
        qos = connection.get_qos_and_size(path)  # get the the qos of the path
        connections.put(connection)

        return (path, qos)  # qos=(file_qos, file_size)

    with concurrent.futures.ThreadPoolExecutor(max_workers=params['threads']) as executor:
        if params['quiet']:  # process request showing a progress bar
            for path in paths:
                future.append(executor.submit(get_qos_and_size, path))

            with alive_bar(len(future), force_tty=True) as bar:
                for qos in concurrent.futures.as_completed(future):
                    bar()
                    qos_result[qos.result()[1][0]] += 1  # get the file qos
                    size_result[qos.result()[1][0]] += qos.result()[1][1]  # get the file size

            if params['human']:  # print in a human readable format
                print("{0} {1} {2}".format(constants.DISK_QOS, qos_result[constants.DISK_QOS], naturalsize(size_result[constants.DISK_QOS], False, True)))
                print("{0} {1} {2}".format(constants.TAPE_QOS, qos_result[constants.TAPE_QOS], naturalsize(size_result[constants.TAPE_QOS], False, True)))
                print("{0} {1} {2}".format(constants.DISK_TAPE_QOS, qos_result[constants.DISK_TAPE_QOS],
                                           naturalsize(size_result[constants.DISK_TAPE_QOS], False, True)))
            else:
                print("{0} {1} {2}".format(constants.DISK_QOS, qos_result[constants.DISK_QOS], size_result[constants.DISK_QOS]))
                print("{0} {1} {2}".format(constants.TAPE_QOS, qos_result[constants.TAPE_QOS], size_result[constants.TAPE_QOS]))
                print("{0} {1} {2}".format(constants.DISK_TAPE_QOS, qos_result[constants.DISK_TAPE_QOS],
                                           size_result[constants.DISK_TAPE_QOS]))

        else:  # process request showing the processed paths
            for path in paths:
                future.append(executor.submit(get_qos_and_size, path))

            for qos in concurrent.futures.as_completed(future):
                if params['human']:  # print in a human readable format
                    print("{0} {1} {2}".format(qos.result()[0], qos.result()[1][0], naturalsize(qos.result()[1][1], False, True)))
                else:
                    print("{0} {1} {2}".format(qos.result()[0], qos.result()[1][0], qos.result()[1][1]))


def process_get_locality_and_size(connections, paths, params):
    '''
    manage get_locality request. Takes a queue of bulkrequests connections,
    a list of paths and the parser params.
    '''

    locality_result = dict()
    locality_result[constants.ONLINE_LOC] = 0
    locality_result[constants.NEARLINE_LOC] = 0
    locality_result[constants.ONLINE_AND_NEARLINE_LOC] = 0

    size_result = dict()
    size_result[constants.ONLINE_LOC] = 0
    size_result[constants.NEARLINE_LOC] = 0
    size_result[constants.ONLINE_AND_NEARLINE_LOC] = 0

    future = list()  # list to save future of threads

    def get_locality_and_size(path):
        '''
        get_locality_and_size function for threading purposes
        '''

        connection = connections.get()
        locality = connection.get_locality_and_size(path)
        connections.put(connection)

        return (path, locality)  # locality = (file_locality, file_size)

    with concurrent.futures.ThreadPoolExecutor(max_workers=params['threads']) as executor:
        if params['quiet']:  # process request showing a progress bar
            for path in paths:
                future.append(executor.submit(get_locality_and_size, path))

            with alive_bar(len(future), force_tty=True) as bar:
                for locality in concurrent.futures.as_completed(future):
                    bar()
                    locality_result[locality.result()[1][0]] += 1
                    size_result[locality.result()[1][0]] += locality.result()[1][1]

            if params['human']:  # print in a human readable format
                print("{0} {1} {2}".format(constants.ONLINE_LOC, locality_result[constants.ONLINE_LOC],
                                           naturalsize(size_result[constants.ONLINE_LOC], False, True)))
                print("{0} {1} {2}".format(constants.NEARLINE_LOC, locality_result[constants.NEARLINE_LOC],
                                           naturalsize(size_result[constants.NEARLINE_LOC], False, True)))
                print("{0} {1} {2}".format(constants.ONLINE_AND_NEARLINE_LOC, locality_result[constants.ONLINE_AND_NEARLINE_LOC],
                                           naturalsize(size_result[constants.ONLINE_AND_NEARLINE_LOC], False, True)))
            else:
                print("{0} {1} {2}".format(constants.ONLINE_LOC, locality_result[constants.ONLINE_LOC], size_result[constants.ONLINE_LOC]))
                print("{0} {1} {2}".format(constants.NEARLINE_LOC, locality_result[constants.NEARLINE_LOC], size_result[constants.NEARLINE_LOC]))
                print("{0} {1} {2}".format(constants.ONLINE_AND_NEARLINE_LOC, locality_result[constants.ONLINE_AND_NEARLINE_LOC],
                                           size_result[constants.ONLINE_AND_NEARLINE_LOC]))

        else:  # process request showing the processed paths
            for path in paths:
                future.append(executor.submit(get_locality_and_size, path))

            for locality in concurrent.futures.as_completed(future):
                if params['human']:  # print in a human readable format
                    print("{0} {1} {2}".format(locality.result()[0], locality.result()[1][0], naturalsize(locality.result()[1][1], False, True)))
                else:
                    print("{0} {1} {2}".format(locality.result()[0], locality.result()[1][0], locality.result()[1][1]))


def process_get_qos(connections, paths, params):
    '''
    manage get_qos request. Takes a queue of bulkrequests connections,
    a list of paths and the parser params.
    '''

    result = dict()
    result[constants.DISK_QOS] = 0
    result[constants.TAPE_QOS] = 0
    result[constants.DISK_TAPE_QOS] = 0

    future = list()  # list to save future of threads

    def get_qos(path):
        '''
        get_qos function for threading purposes
        '''

        connection = connections.get()  # get a bulkrequest connection
        qos = connection.get_qos(path)  # get the the qos of the path
        connections.put(connection)

        return (path, qos)

    with concurrent.futures.ThreadPoolExecutor(max_workers=params['threads']) as executor:
        if params['quiet']:  # process request showing a progress bar
            for path in paths:
                future.append(executor.submit(get_qos, path))

            with alive_bar(len(future), force_tty=True) as bar:
                for qos in concurrent.futures.as_completed(future):
                    bar()
                    result[qos.result()[1]] += 1

            print("{0} {1}".format(constants.DISK_QOS, result[constants.DISK_QOS]))
            print("{0} {1}".format(constants.TAPE_QOS, result[constants.TAPE_QOS]))
            print("{0} {1}".format(constants.DISK_TAPE_QOS, result[constants.DISK_TAPE_QOS]))

        else:  # process request showing the processed paths
            for path in paths:
                future.append(executor.submit(get_qos, path))

            for qos in concurrent.futures.as_completed(future):
                print("{0} {1}".format(qos.result()[0], qos.result()[1]))


def process_get_locality(connections, paths, params):
    '''
    manage get_locality request. Takes a queue of bulkrequests connections,
    a list of paths and the parser params.
    '''

    result = dict()
    result[constants.ONLINE_LOC] = 0
    result[constants.NEARLINE_LOC] = 0
    result[constants.ONLINE_AND_NEARLINE_LOC] = 0

    future = list()  # list to save future of threads

    def get_locality(path):
        '''
        get_locality function for threading purposes
        '''

        connection = connections.get()
        locality = connection.get_locality(path)
        connections.put(connection)

        return (path, locality)

    with concurrent.futures.ThreadPoolExecutor(max_workers=params['threads']) as executor:
        if params['quiet']:  # process request showing a progress bar
            for path in paths:
                future.append(executor.submit(get_locality, path))

            with alive_bar(len(future), force_tty=True) as bar:
                for locality in concurrent.futures.as_completed(future):
                    bar()
                    result[locality.result()[1]] += 1

            print("{0} {1}".format(constants.ONLINE_LOC, result[constants.ONLINE_LOC]))
            print("{0} {1}".format(constants.NEARLINE_LOC, result[constants.NEARLINE_LOC]))
            print("{0} {1}".format(constants.ONLINE_AND_NEARLINE_LOC, result[constants.ONLINE_AND_NEARLINE_LOC]))

        else:  # process request showing the processed paths
            for path in paths:
                future.append(executor.submit(get_locality, path))

            for locality in concurrent.futures.as_completed(future):
                print("{0} {1}".format(locality.result()[0], locality.result()[1]))


def process_set_qos(connections, paths, params):
    '''
    manage set_qos request. Takes a queue of bulkrequests connections,
    a list of paths and the parser params.
    '''

    future = list()  # list to save future of threads

    def set_files_online(path):
        '''
        set_files_online function for threading purposes
        '''

        connection = connections.get()
        connection.set_files_online(path)
        connections.put(connection)

        return path

    def set_files_offline(path):
        '''
        set_files_offline function for threading purposes
        '''

        connection = connections.get()
        connection.set_files_offline(path)
        connections.put(connection)

        return path

    if params['set_qos'] == constants.TAPE_QOS:
        new_qos = set_files_offline
    else:
        new_qos = set_files_online

    with concurrent.futures.ThreadPoolExecutor(max_workers=params['threads']) as executor:
        if params['quiet']:  # process request showing a progress bar
            for count, path in enumerate(paths):
                future.append(executor.submit(new_qos, path))

            with alive_bar(len(future), force_tty=True) as bar:
                for qos in concurrent.futures.as_completed(future):
                    bar()

        else:  # process request showing the processed paths
            for path in paths:
                future.append(executor.submit(new_qos, path))

            for path in concurrent.futures.as_completed(future):
                print("{0} {1}".format(path.result(), params['set_qos']))
