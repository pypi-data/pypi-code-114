# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
import pandas

class XLSXReaderError(Exception):
    pass
class XLSXReaderEmptyStringError(Exception):
    pass

class XLSXReader:

    pragma_for_expression = '#'

    @staticmethod
    def read(file_path):
        """
        Read the XLSX given file with Panda and returns it as a Panda data Frame.
        -> dictionary: sheetsName
            --> dictionary: Lines Number
                --> dictionary: columnName
                        -> Value
        :param file_path: .xlsx file path
        :return: the Panda data frame of the given file.
        """
        data = pandas.read_excel(file_path, sheet_name=None, engine='openpyxl', keep_default_na=False)

        dictionary = {}
        for key in data.keys():
            dictionary[key] = data[key].to_dict('index')
        return dictionary

    @staticmethod
    def clean_cell_str_else_raise(entry_str: str, exception_message_hint: str = ""):
        """
        Extracts the unique word within a string, removing any space (" ") and forcing to upper
        :param entry_str
        :param exception_message_hint: hint about where does the string comes from in order to print a debug information
        """
        ret = entry_str.replace(" ", "").replace("'", "").replace('"', '').replace('“', '').replace('”', '').upper()
        if ret != '':
            return ret
        else:
            message_exception = f"Empty string in one cell, here is an exception_message_hint, maybe: {exception_message_hint}"
            logging.exception(message_exception)
            raise XLSXReaderEmptyStringError(message_exception)

    @staticmethod
    def extract_from_str_list(cell_entry_str: str, exception_message_hint: str = ""):
        """
        Extracts elements from a given list in the format '[1., 2., 3.]'
        :param cell_entry_str is a string representing either a list of float or a list of string.
        :param exception_message_hint: hint about where does the string comes from in order to print a debug information
        """

        # if the string start with a '#', then it's some expression to evaluate
        if cell_entry_str[0] == XLSXReader.pragma_for_expression:
            import numpy  # for a possible execution of python code in the "eval" of function extract_from_str_list
            output_list = eval(cell_entry_str[1:])
            if isinstance(output_list,(numpy.ndarray,range)):
                output_list=list(output_list)
            if not isinstance(output_list,list):
                message_exception = f"A string containing {XLSXReader.pragma_for_expression} as first character has been" \
                                    f" evaluated to extract a list out of it but the attempt failed. The content of the" \
                                    f" string is {cell_entry_str}, the variable evaluated is {output_list} of type {type(output_list)}"
                import logging
                logging.exception(message_exception)
                raise XLSXReaderError(message_exception)

        else:

            # if the string is a list with explicit brackets, we remove them
            if cell_entry_str[0] == "[" and cell_entry_str[-1] == "]":
                cell_entry_str = cell_entry_str[1:-1]

            # any space, quote, double quote are removed; all those symbols are likely artefacts of lists
            clean_list = XLSXReader.clean_cell_str_else_raise(cell_entry_str,exception_message_hint=exception_message_hint).split(",")

            try:
                # if the list is only composed of numeric, we return floats
                output_list = [float(i) for i in clean_list]
            except ValueError:
                # else we redo the analysis, trying to spot any list within a string
                output_list = [XLSXReader.transform_str_of_list_in_list(i) for i in clean_list]

        return output_list

    @staticmethod
    def transform_str_of_list_in_list(str_in):
        # test to check if a string contains a list
        if str_in[0] == "[" and str_in[-1] == "]":
            return XLSXReader.extract_from_str_list(str_in)
        else:
            return str_in