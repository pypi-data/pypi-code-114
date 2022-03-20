import logging
import os
from typing import Tuple

import mysql.connector as mysql

logger = logging.getLogger(__name__)

SQL_TRUE = 0
SQL_FALSE = 1
MAX_RETRIES = 3
MAX_CONNECTION_RETRIES = 3


def create_connection():
    MYSQL_CONFIG = {
        'host': os.environ.get("MYSQL_HOST"),
        'user': os.environ.get("MYSQL_USER"),
        'passwd': os.environ.get("MYSQL_PASSWD"),
        'database': os.environ.get("MYSQL_DATABASE"),
        "charset": "utf8mb4"}
    MYSQL_CNX = mysql.MySQLConnection()

    for retry in range(MAX_CONNECTION_RETRIES):
        try:
            MYSQL_CNX.connect(**MYSQL_CONFIG)
        except mysql.Error as err:
            logger.error(f"{type(err).__name__}: {err}")
            logger.error(str(MYSQL_CONFIG))
            logger.error("error while create_connection to db: {} (try {})".format(err, retry + 1))
            if retry == MAX_CONNECTION_RETRIES - 1:
                raise
        else:
            return MYSQL_CNX


def check_connection(cnx: mysql.MySQLConnection):
    if cnx is None:
        cnx = create_connection()
    if not cnx.is_connected():
        cnx.reconnect()
    return cnx


def select_query(query: str, values: Tuple = (), cnx: mysql.MySQLConnection = None, reuse_cnx: bool = False):
    cnx = check_connection(cnx)
    for tries in range(MAX_RETRIES):
        try:
            cursor = cnx.cursor()
            cursor.execute(query, values)
            res = cursor.fetchall()
            cnx.commit()
            logger.debug("{} record(s) selected ".format(cursor.rowcount))
        except mysql.Error as err:
            logger.warning(f"{type(err).__name__}: {err}")
            logger.warning("Query was: {}".format(query))
            logger.warning("Values were: {}".format(values))
            if tries < MAX_RETRIES:
                logger.warning("retiring (try {})".format(tries))
            else:
                logger.error("max tries reached... raising error (try {})".format(tries))
                raise
        else:
            data = list()
            if len(res) >= 1:
                field_names = [i[0] for i in cursor.description]
                for row in res:
                    data.append(dict(zip(field_names, row)))
            else:
                logger.debug("Selection without result.")
                logger.debug("Query was: {}".format(query))
                logger.debug("Values were: {}".format(values))
            cursor.close()
            return data, cnx
        finally:
            if not reuse_cnx:
                cnx.close()


def execute_query(query: str, values: Tuple = (), cnx: mysql.MySQLConnection = None, reuse_cnx: bool = False,
                  many: bool = False):
    cnx = check_connection(cnx)
    for tries in range(MAX_RETRIES):
        try:
            cursor = cnx.cursor(buffered=True)
            if not many:
                cursor.execute(query, values)
            else:
                cursor.executemany(query, values)
            cnx.commit()
            logger.debug(f"{cursor.rowcount} record(s) updated/inserted")
        except mysql.Error as err:
            logger.warning(f"{type(err).__name__}: {err}")
            logger.warning("Query was: {}".format(query))
            logger.warning("Values were: {}".format(values))
            if tries < MAX_RETRIES:
                logger.warning("retiring (try {})".format(tries))
            else:
                logger.error("max tries reached... raising error (try {})".format(tries))
                raise
        else:
            return True, cnx
        finally:
            if not reuse_cnx:
                cnx.close()


def call_process(process, args):
    cnx = create_connection()
    for tries in range(MAX_RETRIES):
        try:
            cursor = cnx.cursor()
            result_args = cursor.callproc(process, args)
            cnx.commit()
            logger.debug("{} process called".format(process))
            logger.debug("return arg(s):".format(result_args))
        except mysql.Error as err:
            logger.warning(f"{type(err).__name__}: {err}")
            logger.warning("process was: {}".format(process))
            logger.warning("values were: {}".format(args))
            if tries < MAX_RETRIES:
                logger.warning("retiring (try {})".format(tries))
            else:
                logger.error("max tries reached... raising error (try {})".format(tries))
                raise
        else:
            cursor.close()
            return result_args
        finally:
            cnx.close()


def call_process_and_fetch(process, args):
    # for inserting and updating queries
    cnx = create_connection()
    for tries in range(MAX_RETRIES):
        try:
            cursor = cnx.cursor()
            result_args = cursor.callproc(process, args)
            cnx.commit()
            logger.debug("{} process called".format(process))
            logger.debug("return arg(s):".format(result_args))
        except mysql.Error as err:
            logger.warning("Failed inserting: {}".format(err))
            logger.warning("process was: {}".format(process))
            logger.warning("values were: {}".format(args))
            if tries < MAX_RETRIES:
                logger.warning("retrying (try {})".format(tries))
            else:
                logger.error("max tries reached... raising error (try {})".format(tries))
                raise
        else:
            result = list()
            for tmp_result in cursor.stored_results():
                result = tmp_result.fetchall()

            cursor.close()
            return result_args, result
