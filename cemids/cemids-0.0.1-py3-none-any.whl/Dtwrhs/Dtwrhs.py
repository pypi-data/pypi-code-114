#!/usr/bin/env python
# -*- coding: utf-8; buffer-read-only: t -*-

__author__ = "Gregorio Ambrosio"
__contact__ = "gambrosio[at]malaga.eu"
__copyright__ = "Copyright 2022, Gregorio Ambrosio"
__date__ = "2022/03/21"
__license__ = "MIT"

import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
from cemids.log import logger

__all__ = ['Dtwrhs']

# @logger.catch
class Dtwrhs():
    """Dtwrhs class with methods for CEMI Data Science Toolbox

    The Dtwrhs class encapsulates methods to manage PostgreSQL dtwrhs_db

    Attributes:
        engine (str, optional):
            engine explanation
        host (str, optional):
            host explanation
        database (str, optional):
            database explanation
        port (str, optional):
            port explanation
        user (str, optional):
            user explanation
        password (str, optional):
            password explanation

    """

    def __init__(self,
                 engine='postgresql',
                 host='dpgsql1.aytomalaga.intranet',
                 database='dtwrhs_db',
                 port='5432',
                 user='dtwrhs',
                 password='nald3ytd'
                 ):
        """ Dtwrhs constructor method """
        self.__engine = engine
        self.__host = host
        self.__database = database
        self.__port = port
        self.__user = user
        self.__pass = password
        self.__con = None

        logger.debug('engine   : {}', self.__engine)
        logger.debug('host     : {}', self.__host)
        logger.debug('database : {}', self.__database)
        logger.debug('port     : {}', self.__port)
        logger.debug('user     : {}', self.__user)
        logger.debug('password : {}', self.__password)

        # Initialization functions
        try:
            self.__open_database()
        except Exception as e:
            logger.error("Dtwrhs object cannot be instantiated")
            # return None
            raise e

    def __del__(self):
        """ Dtwrhs destructor method"""

    def __open_database(self):

        """
        This function makes the connection with the database and calls the
        initialization functions, e.g. create temporal views
        """

        db_param = {
            "host"      : self.__host,
            "database"  : self.__database,
            "user"      : self.__user,
            "password"  : self.__password
        }

        try:
            # connect to the PostgreSQL server
            logger.debug("Connecting to the PostgreSQL database: {}", self.__database)
            # self.__con = psycopg2.connect(**db_param)
            conn_str=(
                f'postgresql+psycopg2://'
                f'{self.__user}:{self.__password}@'
                f'{self.__host}/{self.__database}'
            )
            self.__con = create_engine(conn_str).connect()
            logger.success("Connection is established with {}", self.__database)
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("Error while trying to open database: {}", error.args[0])
            raise


    def __close_dataset(self):
        """
        This function closes the connection with the database
        """
        self.__con.close()
        logger.info("The connection with the database has been successfully closed")

    def get_con(self):
        """
        This function returns the sql connection variable
        """
        return self.__con


    """
    Framework
    """


    """
    Stuff
    """
    def select_column(self, column_name, table_name):
        '''
        Returns a dataframe with grouped column values
        (without repetition)
        '''

        # Get a cursor to execute SQLite statements
        cur = self.__con.cursor()
        sql_str = (f"select {column_name}  from {table_name} group by {column_name};")
        df_rows = pd.read_sql_query(sql_str, self.__con)
        return df_rows

    def query(self, sql, df=True):
        """Execute a sqlquery over robotathome database

        Parameters
        ----------
        sql: can be a string with a sql query or a file name that contains the
             sql query
        df:  boolean indicating if result is returned as a DataFrame (True) or
             as a sqlite row list (False).  This option (False) is mandatory if
             the query string has more than one sql command, i.e., it's a script

        Returns
        -------
        ans: a DataFrame or a sqlite row list

        """


        if os.path.isfile(sql):
            script = open(sql, 'r')
            query = script.read()
        else:
            query = sql

        if df:
            ans = pd.read_sql_query(query, self.__con)
        else:
            cur = self.__con.cursor()
            cur.executescript(query)
            ans = cur.fetchall()

        if os.path.isfile(sql):
            script.close()

        return ans


    """
    Lab
    """
