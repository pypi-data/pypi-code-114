import pandas as pd
import logging


def df_to_csv(dataframe, filename):
    """
    :param dataframe: dataframe having the flattened json
    :param filename: name of the csv file where data will be saved
    :return: None
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise AttributeError('dataframe arg in df_to_csv() is not a dataframe')
    if not isinstance(filename, str) or not filename.endswith('.csv'):
        raise NameError('Please Provide Valid CSV File Name')

    dataframe.to_csv(filename, index=False, encoding='UTF-8-sig')
    '''
    :param index:    True will write row names
    :param encoding: A string representing the encoding to use in the output file
                         UTF-8-sig is given because utf-8 is not printing "-" correctly
    '''

    logging.info('file generated successfully {}'.format(filename))


# Function to convert Dataframe to xml file

def df_to_xml(dataframe, filename):
    """
    :param dataframe: dataframe having the flattened json
    :param filename: name of the xml file where data will be saved
    :return: None
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise AttributeError('dataframe arg in df_to_xml() is not a dataframe')
    if not isinstance(filename, str) or not filename.endswith('.xml'):
        raise NameError('Please Provide Valid XML File Name')

    dataframe.to_xml(filename)

    logging.info('file generated successfully {}'.format(filename))

def df_to_html(dataframe, filename):
    """
    :param dataframe: dataframe having the flattened json
    :param filename: name of the xml file where data will be saved
    :return: None
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise AttributeError('dataframe arg in df_to_html() is not a dataframe')
    if not isinstance(filename, str) or not filename.endswith('.html'):
        raise NameError('Please Provide Valid HTML File Name')

    dataframe.to_html(filename, escape=False, na_rep=" ", index=False)
    '''
    :param escape: True will convert the characters <, >, and & to HTML-safe sequences.
    :param na_rep: by default null values will be printed as NaN, so given " "
    :param index : Whether to print index (row) labels
    '''
    logging.info('file generated successfully {}'.format(filename))
