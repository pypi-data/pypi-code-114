#!/usr/bin/env python3
"""
    Simple tools to help format data.
"""


from IPython.display import HTML, display


def make_table(headings: [], data: [[]], columns: bool = False, row_headings: [] = None):
    """
    Creates table from given headings and data.
    headings should be a list of strings.
    Data should be a list of tuples or arrays with length of len(headings)
    If columns is given and True, data consists of tuples / arrays of columns, else it's elements are interpreted as columns.
    In row mode (default) each element of data should be of len(headings), in column mode, there should be len(headings) elements of equal length in data.
    Will return False if data input is bad.
    :param headings: Row of column headings
    :param data: list of table rows (list of lists)
    :param columns: If True, data is interpreted as list of columns, instead of rows.
    :param row_headings: If given, a column with given contents as headings is added as first column.
    :return: No return. Table is displayed using IPython.display.
    """
    if not (type(headings) in [type([]), type(())] and type(data) in [type([]), type(())] and (
            not row_headings or type(row_headings) in [type([]), type(())])):
        print("1")
        return False
    if columns:
        if row_headings and not len(row_headings) == len(data[0]):
            print(data[0], len(data[0]), len(row_headings))
            print(2)
            return False
        if not len(data) == len(headings):
            print(3)
            return False
        rows = len(data[0])
        for column in data:
            if not len(column) == rows:
                print(4)
                return False
        formatted_data = []
        for i in range(0, rows):
            formatted_data.append([el[i] for el in data])
        data = formatted_data
    else:
        if row_headings and not len(row_headings) == len(data):
            print(5)
            return False
        for row in data:
            if not len(row) == len(headings):
                print(row)
                print(6)
                return False

    table = "<table><tr>"
    if row_headings:
        table += "<th></th>"
    for heading in headings:
        table += "<th>" + str(heading) + "</th>"
    table += "</tr>"
    for i, row in enumerate(data):
        table += "<tr>"
        if row_headings:
            table += "<td><b>" + row_headings[i] + "</td>"
        for element in row:
            table += "<td>" + str(element) + "</td>"
        table += "</tr>"
    table += "</table>"
    display(HTML(table))

