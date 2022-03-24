import os
import zipfile

from sqlcarve.validator.validator import *
from sqlalchemy import *
import sqlalchemy.exc as exc
import logging as log

from sqlcarve.validator.helpers import *


# from helpers import json_extract


class Connexion:
    # host = ''
    # user = ''
    # password = ''
    # port = ''
    # database = ''
    engine = ''

    def connect(dialect, db_name, connector='', user_n='', password='', host='', port=''):
        try:
            if dialect == 'sqlite':
                engine = create_engine(
                    dialect + ':///' + db_name
                )
            else:
                engine = create_engine(
                    dialect + '+' + connector + '://' + user_n + ':' + password + '@' + host + ':' + port + '/' + db_name
                )

            conn = engine.connect()
            log.info('connected')
            return conn
        except EOFError as error:
            log.error(error)

    @staticmethod
    def json_connect():
        for root, dirs, files in os.walk("..\\resources"):
            file = [x for x in files if x.startswith("connexion.json")][0]
            with open(os.path.join(root, file)) as json_file:
                data = json.load(json_file)
                helper = GestionJsonHelper()
                dialect_name = helper.json_extract(data, 'dialect_name')[0]
                dialect = helper.json_extract(data, 'dialect')[0]

                connector = dialect['connector']
                host = dialect['host']
                user = dialect['user']
                password = dialect['password']
                port = dialect['port']
                db = dialect['db']

                return Connexion.connect(dialect_name, db, connector, user, password, host, port)

    def close(connection):

        conn = connection.close()
        log.info("closed")
        return conn


class Executor:

    @staticmethod
    def execute_query(statement, conn):

        # print("here", statement)
        result = []

        try:
            # for queries in stmtList:
            # result.append([stmtList.index(queries), queries[0], conn.execute(queries[1])])

            result = conn.execute(statement)
        except exc.OperationalError as error:
            log.error(error)

        # for index, file_name, list_row in result:
        #     #print("\n", index, file_name)
        #     msg = "\n" + str(index) + " " + file_name
        #     log.info(msg)
        #     for row in list_row:
        #         print(row)

        for row in result:
            log.debug(row)

        return result
