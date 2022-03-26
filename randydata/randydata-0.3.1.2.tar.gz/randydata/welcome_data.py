#!/usr/bin/env python3
"""
    Some simple tools to handle data from sql and excel as a custom datatype.
"""


import mysql.connector
import pandas as pd
import sqlalchemy


def create_datatype_from_attributes(name: str, attributes: [str], bool_values: [str] = [], methods: dict = {}):
    """
    Creates new datatype with given name, attributes and methods.
    :param name: Name of new datatype class
    :param attributes: List of Class property names
    :param bool_values: Values that should be interpreted as booleans even if given 0 / 1
    :param methods: Dict of names and functions for Class methods
    :return: Class of new datatype
    """
    def constructor(self, arguments: dict):
        for attribute in attributes:
            self.__dict__.update([(attribute, arguments[attribute])])
            for bool_value in bool_values:
                if arguments[bool_value]:
                    self.__dict__.update([(bool_value, True)])
                else:
                    self.__dict__.update([(bool_value, False)])
        for attribute in arguments:
            if arguments[attribute] == "":
                self.__dict__.update([(attribute, None)])

    for method in methods:
        if type(methods[method]) is not type(create_datatype_from_attributes):
            methods.pop(method)

    methods["__init__"] = constructor

    return type(name, (object, ), methods)


def create_datatype_from_sql(name: str, database: str, table: str, host: str = "localhost", username: str = "root",
                             password: str = "", no_bool: [str] = [], methods: dict = {}) -> [object]:
    """
       A new datatype with MySQL columns interpreted as properties and
       methods from methods argument is created and a list of those rows as objects of that datatype is returned.
       :param name: Name of new datatype class
       :param database: Name of mysql database
       :param table: Name of (new) table in database to hold data
       :param host: Hostname of MySQL table
       :param username: MySQL username
       :param password: password to mysql database
       :param no_bool: list of field names that could, but SHOULD NOT, be interpreted as
                       bools (contain only 0 and 1 or None)
       :param methods: Names and functions for methods the new datatype class should hold
       :return: List containing the rows of the MySQL database as objects of the newly created datatype
   """
    con = mysql.connector.connect(
        host=host,
        username=username,
        database=database,
        password=password
    )
    db = con.cursor()

    db.execute("SELECT * FROM {};".format(table))
    rows = []
    column_names = [column_name.lower() for column_name in db.column_names]
    for row in db:
        rows.append(dict(zip(column_names, row)))

    bool_values = []
    for column_name in column_names:
        column = [row[column_name] for row in rows]
        if column_name not in no_bool and column and all(el in [None, 0, 1] for el in column):
            bool_values.append(column_name)

    data_type = create_datatype_from_attributes(name=name, attributes=column_names, bool_values=bool_values,
                                                methods=methods)
    objects = []
    for row in rows:
        objects.append(data_type(row))
    return objects


def read_excel_to_sql(path: str, database: str, table: str, host: str = "localhost", username: str = "root",
                      password: str = "", override_table: bool = True, append: bool = False) -> bool:
    """
       Data from excel table is read into Mysql database.
       :param path: Path to excel file to read
       :param database: Name of mysql database
       :param table: Name of (new) table in database to hold data
       :param host: Hostname of MySQL table
       :param username: MySQL username
       :param password: password to mysql database
       :param override_table: If True, table with given name is deleted if exists and newly created with contents
                               from excel file
       :param append: If True (AND override_table is FALSE) new data is appended to table if it exists.
                       Dangerous as it might cause involuntary data duplicates and false analysis results
       :return: True if successful, False if not.
   """
    try:
        con = mysql.connector.connect(
            host=host,
            database=database,
            username=username,
            password=password
        )
    except mysql.connector.Error as dberr:
        print("Couldn't connect to database. Does it exist and is accessible? Is the password correct?")
        print(dberr)
        return False

    df = pd.read_excel(path)
    if_exists = "fail"
    if override_table:
        if_exists = "replace"
    elif append:
        if_exists = "append"
    # df.to_sql(name=table, con=con)
    engine = sqlalchemy.create_engine("mysql://{user}@{host}/{db}".format(user="root", host="localhost", db=database))
    df.to_sql(name=table, con=engine, if_exists=if_exists)
    con.close()
    return True


def create_datatype_from_excel(name: str, path: str, database: str, table: str, host: str = "localhost",
                               username: str = "root", password: str = "", override_table: bool = True,
                               append: bool = False, no_bool: [str] = [], methods: dict = {}) -> [object]:
    """
    Shorthand for read_excel_to_sql() and create_datatype_from_sql.
    Data from excel table is read into Mysql database, a new datatype with excel columns interpreted as properties and
    methods from methods argument is created and a list of those rows as objects of that datatype is returned.
    :param name: Name of new datatype class
    :param path: Path to excel file to read
    :param database: Name of mysql database
    :param table: Name of (new) table in database to hold data
    :param host: Hostname of MySQL table
    :param username: MySQL username
    :param password: password to mysql database
    :param override_table: If True, table with given name is deleted if exists and newly created with contents
                            from excel file
    :param append: If True (AND override_table is FALSE) new data is appended to table if it exists.
                    Dangerous as it might cause involuntary data duplicates and false analysis results
    :param no_bool: list of field names that could, but SHOULD NOT, be interpreted as
                    bools (contain only 0 and 1 or None)
    :param methods: Methods the new datatype class should hold
    :return: List containing the rows of the excel file as objects of the newly created datatype
    """
    if read_excel_to_sql(path=path, database=database, table=table, host=host, username=username, password=password, override_table=override_table, append=append):
        return create_datatype_from_sql(name=name, database=database, table=table, no_bool=no_bool, methods=methods)
    return False


if __name__ == "__main__":
    read_excel_to_sql(path="~/Documents/Jupyter/FalllisteNackt.xlsx", database="data", table="Liste2")
    patients = create_datatype_from_sql("Patient", "data", "Liste2")
    print(type(patients[0].dob))
    # print(patients[0].bmi)
