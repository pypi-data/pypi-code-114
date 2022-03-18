#!/usr/bin/env python3

'''
MIT License

Copyright (c) 2021 Mikhail Hyde & Cole Crescas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import pandas as pd
import numpy as np
import boto3
from pandas.core.frame import DataFrame
from botocore.exceptions import NoCredentialsError
from HALsn.sysLogger import sysLogger


class dataSupervisor:
    '''
    Object to host data parsing and collection objects. Allows for conversion
    of List[List] to a pandas DataFrame, exporting csvs, and pushing to AWS
    S3 bucket.
    '''
    def __init__(self, map: dict, headers: bool = False, s3_enable: bool = False):

        self.logger = sysLogger()

        # Generate S3 object if enabled
        self.s3_enable = s3_enable
        if self.s3_enable:
            self.s3 = s3()

        # Parser - Contains List[List] and Parsed DataFrame
        self.parser = parser(map, headers)

        # Data Path
        self.datapath = '/home/pi/'
        # Filename
        self.filename = 'default.csv'
        # File Relative to Home Dir
        self.localfile = self.datapath + self.filename

    def generate(self, specific: bool) -> None:
        '''
        Calls the relevant parse method to convert
        currently stored data into a Pandas 
        DataFrame
        '''
        if specific:
            self.parser.parse()
        else:
            self.parser.interpreted_parse()

    def export(self) -> None:
        '''
        Simultaneously exports a local CSV and pushes
        that CSV to the S3 Bucket.
        '''
        self.export_csv()
        if self.s3_enable:
            self.s3.upload_to_s3(self.localfile)
            self.logger.INFO(
                f'Succesfully Uploaded {self.filename} to AWS S3 {self.s3.bucket}')

    def export_csv(self) -> None:
        '''
        Exports the parsed and formatted Dataframe as a CSV
        file to the predetermined directory.
        '''
        if self.localfile:
            self.parser.df.to_csv(self.localfile, index=False)
            self.logger.INFO(
                f'Created Report {self.filename} and saved to {self.localfile}')
        else:
            self.logger.ERROR('Could not create report. The local file member has not been set')

    def collect_row(self, *args) -> None:
        '''
        Takes an arbitrary amount of arguments
        of any type. Breaks down all inputs into
        a single list and appends the list to the
        dataframe. 
        '''
        if not self.parser.headers:
            row = []
            for arg in args:
                arg = self.flatten(arg)
                row += arg

            self.parser.lst.append(row)
        else:
            self.logger.ERROR(
                f'Method does not work if headers are pre-defined. Headers are currently {self.parser.headers}')

    def init_frames(self) -> None:
        '''
        Initializes DataFrame and List to start new
        logging frame
        '''
        self.parser.df = pd.DataFrame()
        self.parser.lst = []

    def add_filename(self, filepath: str, filename: str) -> None:
        '''
        Generates a TimeStamp (string) to be appended
        to CSV file for export

        ::returns:: String
        '''
        self.filepath = filepath
        self.filename = filename
        if filename[-4:] != '.csv':
            self.filename += '.csv'

        self.localfile = self.filepath + self.filename


class parser:
    '''
    Handles data collection and data conversion. Built around a pandas dataframe,
    this object allows for all Pandas Dataframe related methods as well as HALsn
    specific data conversion methods.
    '''
    def __init__(self, map: dict, headers: list = False):

        # DataFrame - Enables Pandas methods and data manipulation
        self.df = pd.DataFrame()
        # Dictionary of product queries to describe parsing methods
        self.product_map = map
        # Initial List to gather data pre-parsing
        self.lst = []

        # Look up table of conversion functions
        self.convert_fnc = {'KC':  self._kc_conv,
                            'HEX': self._convertHex,
                            'PWM': self._pwm,
                            'INT': self._cast_int,
                            'SNB': self._snb}

        # Headers - Typically a list but false if generic method
        # is desired
        if headers != False:
            self.headers = headers

    def parse(self) -> None:
        '''
        Converts list of lists containing both
        BDP and external data and converts into
        a pandas DataFrame with pre-defined
        headers.
        '''
        for row in self.lst:
            clean_lst = []
            for data in row:
                clean_lst.append(self.convertBDP(data))
            self.flatten(clean_lst)
            self.df = self.df.append(
                pd.DataFrame(((np.asarray(clean_lst)).reshape(1, -1)), columns=self.headers))

    def interpreted_parse(self) -> None:
        '''
        Converts list of lists containing both
        BDP and external data and converts into
        a pandas DataFrame with universal headers
        determined by BDP Keys.
        '''
        headers = []
        clean_lst = []
        ext_idx = 1
        for data in self.lst[0]:
            key = self._get_key(data)
            if key == None:
                key = 'ES' + str(ext_idx)
                ext_idx += 1
            if key == 'KC':
                key = ['KC1', 'KC2', 'KC3', 'KC4',
                       'KC5', 'KC6', 'KC7', 'KC8']
            clean_lst.append(self.convertBDP(data))
            headers.append(key)
        clean_lst = self.flatten(clean_lst)
        headers = self.flatten(headers)
        self.df = self.df.append(pd.DataFrame(((np.asarray(clean_lst)).reshape(1, -1)), columns=headers))
        
        for row in self.lst[1:]:
            clean_lst = []
            for data in row:
                clean_lst.append(self.convertBDP(data))
            clean_lst = self.flatten(clean_lst)
            self.df = self.df.append(pd.DataFrame(((np.asarray(clean_lst)).reshape(1, -1)), columns=headers))
            
    
    def convertBDP(self, data: str) -> list:
        '''
        Univsersal function for converting BDP
        responses into readable data. References
        the query hash map of the device it is
        interpretting.
        '''
        key = self._get_key(data)
        if key is None:
            return data
        for inst in self.product_map.values():

            if key == inst[0][1:inst[2]]:
                if inst[-1] == 0:
                    return data[1:-1]
                fnc = self.convert_fnc[inst[-1]]
                return fnc(data[inst[2]:-1])

    def flatten(self, lst: list) -> list:
        '''
        Takes a list as an input and recursively
        processes through the list to remove any
        embedded iterables.
        '''
        flat_list = []

        for idx in lst:
            if type(idx) == list or type(idx) == tuple:
                flat_list += self.flatten(idx)
            else:
                flat_list.append(idx)

        return flat_list

    def _get_key(self, entry: str) -> str:
        '''
        Finds the BDP Command defining characters
        in the data string and returns the key for
        correlating parsing methods
        '''
        for value in self.product_map.values():
            if type(entry) == str:
                match = value[0][1:value[2]]
                key = entry[1:value[2]]
                if key == match:
                    return key
        return None

    def _kc_conv(self, data: str) -> list:
        '''
        Special function to handle parsing of
        the KC type BDP command.
        '''
        basket = self._cast_int(data[0])
        size = self._convertHex(data[1])
        style = self._cast_int(data[2])
        ounces = self._convertHex(data[3:5])
        block = self._convertHex(data[5:7])
        temp = self._convertHex(data[7:9])
        volume = self._convertHex(data[9:13])
        time = self._convertHex(data[13:15])

        return [basket, size, style, ounces, block, temp, volume, time]

    @staticmethod
    def _pwm(data: str) -> int:
        '''
        Maps BDP PWM values of 0-64
        to values of 0-100
        '''
        return (int(data) / 64) * 100

    @staticmethod
    def _convertHex(data: str) -> int:
        '''
        Converts HEX numbers into
        their decimal equivalent
        '''
        return int(data, 16)

    @staticmethod
    def _cast_int(data: str) -> int:
        '''
        Casts the input data as
        an integer
        '''
        return int(data)

    @staticmethod
    def _snb(data: str) -> int:
        '''
        Special HEX conversion method
        for SF - P2 builds.
        '''
        return int(data[1:], 16)

class s3:
    '''
    Object contains necessary AWS S3 methods and attributes such as
    credentials and pushing files to AWS S3 bucket.
    '''
    def __init__(self):
        # System Logger - Prints to Screen and Contributes to Log File
        self.logger = sysLogger()

        # ALL AWS S3 CREDENTIALS ARE HELD IN ENVIRONMENT VARIABLES

        # AWS S3 Access Key - Points to the appropriate bucket
        self.ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
        # AWS S3 Secret Key - S3 Bucket Password
        self.SECRET_KEY = os.environ['AWS_SECRET_KEY']
        # AWS S3 Bucket Name
        self.bucket = os.environ['BUCKET']

        # Boto S3 Object - Provides methods for pushing to S3
        self.s3 = boto3.client('s3', aws_access_key_id=self.ACCESS_KEY,
                               aws_secret_access_key=self.SECRET_KEY)

    def upload_to_s3(self, filename: str, localfile: str) -> bool:
        '''
        Uploads a single file to the AWS s3 bucket.
        '''
        try:
            self.s3.upload_file(Filename=localfile,
                                Bucket=self.bucket,
                                Key=filename)
            return True
        except FileNotFoundError:
            self.logger.ERROR("The file was not found")
            return False
        except NoCredentialsError:
            self.logger.ERROR("Credentials not available")
            return False


class errorHandler():
    '''
    Handles conversion of pandas dataframe into a generic HALsn format
    that conforms to the SQL schema for data distribution.
    '''
    def __init__(self, msg_df: DataFrame, server: bool = True):

        # Temporary check to see which machine his hosting the master df
        if server:
            self.master = pd.read_csv(
                '/home/hal/HALsn/HALsn/sample_data/master_df.csv')
        else:
            self.master = pd.read_csv(
                '/home/pi/HALsn/HALsn/sample_data/master_df.csv')

        # Input DF - Compared against master
        self.msg_df = msg_df

        # If the message DF is of type Pandas.core.frame.DataFrame
        # the data is Padded
        if self.type_check():
            self.pad_data()
        else:
            raise TypeError(
                'Argument is not of the pandas.core.frame.DataFrame type')

    def pad_data(self) -> None:
        '''
        Pads the data into master dataframe.
        overwrites the master dataframe
        '''
        lst = []

        for i in self.msg_df.columns.tolist():
            if i in self.master.columns.tolist():
                lst.append(i)

        for j in lst:
            self.master[j] = self.msg_df[j]

        self.master = self.master.replace(r'^\s*$', np.NaN, regex=True)

        self.master['SKU_ID'] = self.master['WX'].str[2:4]
        self.master['TEST_TYPE_ID'] = self.master['WX'].str[11:13]
        self.master['BUILD_ID'] = self.master['WX'].str[7:9]

    def type_check(self) -> bool:
        '''
        Checks that the init argument is of type
        pandas.core.frame.DataFrame
        '''
        return type(self.msg_df) == DataFrame

    def pad_check(self) -> bool:
        '''
        Checks the validity of pickle_df before progressing to next check
        '''
        return self.msg_df.equals(self.master[self.master.columns[~self.master.isna().all()]])

    def info_check(self) -> bool:
        '''
        Checks that the rows and columns are correct
        '''
        no_na_master = self.master[self.master.columns[self.master.isna().all()]]
        return len(self.msg_df.columns) == len(no_na_master.columns)

    def check_mising(self) -> bool:
        '''
        Checks for missing values in the df. This wont
        work because padded df will have a lot missing
        '''
        return (self.msg_df.isna().sum().sum() < 10)

    def verify(self) -> bool:
        '''
        Calls all check methods
        '''
        if self.pad_check() & self.info_check() & self.check_mising():
            return True
        else:
            return False
