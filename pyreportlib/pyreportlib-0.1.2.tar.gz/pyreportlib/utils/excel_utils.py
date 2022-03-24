# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:45:11 2020

@author: MadsFredrikHeiervang
"""
from os import path

import pandas as pd


def _reform_dict(dictionary, t=tuple(), reform=dict()):
    for i, (key, val) in enumerate(dictionary.items()):
        t = t + (key,)
        if isinstance(val, dict):
            _reform_dict(val, t, reform)
        else:
            reform.update({t: val})
        t = t[:-1]
    reformed_dict = reform.copy()
    # reform.clear()
    return reformed_dict


def get_split_columns(columns, newcolumns=[], index_length=2):
    if len(''.join([column + '   '
                    for column in columns])) > 70 - index_length:
        i = 0
        while len(''.join([column + '   ' for column in columns[:i]] +
                          [columns[i]])) < 70 - index_length:
            i += 1
        newcolumns.append(columns[:i])
        get_split_columns(columns[i:], newcolumns)
    else:
        newcolumns.append(columns)
    return newcolumns


def excel_to_latex(filename, **kwargs):
    if isinstance(filename, list):
        return [content for file in filename
                for content in excel_to_latex(file, **kwargs)]
    dfs = []
    if isinstance(filename, pd.DataFrame):
        df = filename
    elif path.splitext(filename)[-1] == '.csv':
        df = pd.read_csv(filename, **kwargs)
    else:
        df = pd.read_excel(filename, **kwargs)
    header = kwargs.get('header', 0)
    if isinstance(header, int):
        columns = df.columns
        split_columns = get_split_columns(list(columns), newcolumns=[],
                                          index_length=len(str(df.index[-1])))
        for j, split_column in enumerate(split_columns):
            df2 = df[split_column]
            dfs.append(df2)

    else:
        columns = []
        for head in header:
            columns.append([df.columns.levels[head][i]
                            for i in df.columns.codes[head]])

        split_columns = get_split_columns(columns[-1], newcolumns=[],
                                          index_length=len(str(df.index[-1])))

        i = 0
        for j, split_column in enumerate(split_columns):
            split_dict = {}
            for column in split_column:
                if len(header) == 2:
                    columndata = list(df[columns[0][i]][column])
                    if columns[0][i] not in split_dict.keys():
                        split_dict[columns[0][i]] = {column: columndata}
                    else:
                        split_dict[columns[0][i]].update({column: columndata})
                elif len(header) == 3:
                    columndata = df[columns[0][i]][columns[1][i]][column]
                    if columns[0][i] not in split_dict.keys():
                        split_dict[columns[0][i]] = {columns[1][i]:
                                                     {column: columndata}}
                    else:
                        column_key0 = columns[0][i]
                        column_key1 = columns[1][i]
                        if columns[1][i] \
                                not in split_dict[columns[0][i]].keys():
                            split_dict[column_key0][column_key1] = {column:
                                                                    columndata}
                        else:
                            split_dict[column_key0][column_key1] \
                                .update({column: columndata})
                i += 1
            df_dict = _reform_dict(split_dict, t=tuple(), reform={})
            df2 = pd.DataFrame.from_dict(df_dict)
            df2.index = df.index
            dfs.append(df2)

    return [{'latex_code': df2.to_latex(longtable=True,
                                        multicolumn_format='c',
                                        na_rep='')} for df2 in dfs]
