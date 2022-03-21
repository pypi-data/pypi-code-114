__author__ = "Affan"
__copyright__ = "Copyright (C) 2022 Affan"
__license__ = "Public Domain"
__version__ = "1.0"

import pandas as pd
import requests
import json
import logging
from flatten_json import flatten
import os
import pdfkit

logging.basicConfig(filename='file2.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger()


class MuseumAPI:

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return 'Museum API URL is : {self.url} '.format(self=self)

    def api_to_dataframe(self, st=None, sp=None):
        """
        :param st: Integer number from where the objectIDs Index starts
        parameter st type: integer
        :param sp: Integer number from where the objectIDs Index stops
        parameter sp type: integer
        :return: returns dataframe of API_json_objects
        """

        req = requests.get(self.url)
        json_dict = req.json()

        # slicing through objectIDs and Checking Whether objectIDs are between 0 and 830985
        if (st is None) and (sp is None):
            ids = list(json_dict['objectIDs'][:50])
            logger.info('objectIDs are taken from 0 to 50')

        elif (st is not None) and (sp is None):

            if (st < 0) or (st > 830985):
                logger.error('The Index of start and stop should be between 0 and 830985')
                raise IndexError('The Index of start and stop should be between 0 and 830985')

            ids = list(json_dict['objectIDs'][st:st + 50])
            logger.info('objectIDs are taken from %d to %d', st, st + 50)

        elif (st is None) and (sp is not None):

            if (sp < 0) or (sp > 830985):
                logger.error('The Index of start and stop should be between 0 and 830985')
                raise IndexError('The Index of start and stop should be between 0 and 830985')

            ids = list(json_dict['objectIDs'][:sp])
            logger.info('objectIDs are taken from 0 to %d', sp)

        else:
            if (st < 0) or (sp > 830985):
                logger.error('The Index of start and stop should be between 0 and 830985')
                raise IndexError('The Index of start and stop should be between 0 and 830985')

            ids = list(json_dict['objectIDs'])[st:sp]
            logger.info('objectIDs are taken from %d to %d', st, sp)

        urls = []
        list_url = [self.url + '/' + str(i) for i in ids]

        # Iterating through different objectid's and appending flattened json data
        for ur in list_url:
            req = requests.get(ur)
            logger.debug('%s has response %s', ur, req)
            json_dict = json.loads(req.content)
            flat = flatten(json_dict)
            urls.append(flat)
        return pd.json_normalize(urls)

    @staticmethod
    def dataframe_to_csv(dataframe, csv_filename):
        """
        :param dataframe: pandas dataframe consists of Museum_API information
        :param csv_filename: new csv_file to write from dataframe
        parameter csv_filename type: string

        creates csv_file
        """

        # checks whether the dataframe is empty or not
        if dataframe.empty:
            logger.error('DataFrame is empty')
            raise Exception('DataFrame is empty')

        # adding the csv extension if it is not present
        if csv_filename[-4:] != '.csv':
            csv_filename = csv_filename + '.csv'
            dataframe.to_csv(csv_filename, encoding='utf-8-sig')

        dataframe.to_csv(csv_filename, encoding='utf-8-sig')
        logging.info('%s is created', csv_filename)

    @staticmethod
    def dataframe_to_xml(dataframe, xml_filename):
        """
        :param dataframe: pandas dataframe consists of Museum_API information
        :param xml_filename: new xml_file to write from dataframe
        parameter xml_filename: string

        creates xml file
        """

        # checking whether dataframe is empty or not
        if dataframe.empty:
            logger.error('DataFrame is empty')
            raise Exception('DataFrame is empty')

        # adding the xml extension if it is not present
        if xml_filename[-4:] != '.xml':
            xml_filename = xml_filename + '.xml'
            dataframe.to_xml(xml_filename)

        dataframe.to_xml(xml_filename)
        logging.info('%s is created', xml_filename)

    @staticmethod
    def dataframe_to_html(dataframe, html_filename):
        """
        :param dataframe: pandas dataframe consists of Museum_API information
        :param html_filename: new html_file to write from dataframe
        parameter html_filename type: string

        creates html file
        """

        # checking whether dataframe is empty or not
        if dataframe.empty:
            logger.error('DataFrame is empty')
            raise Exception('DataFrame is empty')

        # adding the html extension if it is not present
        if html_filename[-5:] != '.html':
            html_filename = html_filename + '.xml'

        file = open(html_filename, 'w')
        write_html = dataframe.to_html()
        file.write(write_html)
        file.close()
        logger.info('%s is created', html_filename)

    @staticmethod
    def html_to_pdf(html_filename, pdf_filename):
        """
        for converting html to pdf , Install wkhtmltopdf and copy its
        executable file to path environment variables

        :param html_filename: existing html_file
        parameter html_filename type: string
        :param pdf_filename: new pdf_file
        parameter pdf_filename type: string

        creates pdf file
        """

        # check whether the html file is present or not
        if os.path.isfile(html_filename):
            pass
        else:
            logger.error('%s file does not exists', html_filename)
            raise FileNotFoundError('%s does not exists', html_filename)

        # check whether html_file is empty or not
        if os.path.exists(html_filename) and os.stat(html_filename).st_size == 0:
            logger.error('%s file is empty', html_filename)
            raise FileExistsError("%s is empty", html_filename)

        # Adjusting page layout options of pdf
        options = {
            'page-height': '1300',
            'page-width': '300', 'orientation': 'Landscape',
            'margin-top': '0.8in', 'margin-right': '0.7in', 'margin-bottom': '0.7in', 'margin-left': '0.7in',
            'encoding': 'utf-8-sig'}

        # adding the pdf extension if it is not present
        if pdf_filename[-4:] != '.pdf':
            pdf_filename = pdf_filename + '.pdf'

        pdfkit.from_file(html_filename, pdf_filename, options=options)
        logger.info('%s is created', pdf_filename)
