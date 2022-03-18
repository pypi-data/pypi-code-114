"""Module for preprocessing Indonesia Name and Address.

Dictionary for preproccesing on dict_files folder.
Roman library used for converting roman number to arabic.
"""

# import library
import os
import re
from functools import reduce

import roman

# membuat dictionary untuk preprocessing nama dan alamat
dict_alamat = {}
dict_nama = {}

here = os.path.dirname(os.path.abspath(__file__))

# menambahkan tiap baris dari file txt ke dictionary
with open(os.path.join(here, 'dict_files', 'dict_alamat.txt'), 'r') as file:
    for line in file:
        key, value = line.replace('\'', '').rstrip('\n').split(':')
        dict_alamat[key] = value

with open(os.path.join(here, 'dict_files', 'dict_nama.txt'), 'r') as file:
    for line in file:
        key, value = line.replace('\'', '').rstrip('\n').split(':')
        dict_nama[key] = value


class Preprocessing:
    """Preprocessing class."""

    def __init__(self, tipe='alamat'):
        """Class initialization.

        Args:
            tipe (str, optional): valid value : 'alamat' for address or 'nama' for name. Defaults to 'alamat'.
        """
        self.tipe = tipe

    # standarisasi penulisan nama dan alamat
    def standardize(self, strings):
        """Standardize function.

        Args:
            strings (_type_): input string

        Returns:
            _type_: returning standarized string based on type (name or address)
        """
        tipe = self.tipe
        if tipe == 'alamat':
            result = " ".join(dict_alamat.get(ele, ele) for ele in strings.split())
        else:
            result = re.sub(r'\s', '_', strings)
            for i, k in dict_nama.items():
                str_from = '(_|^)' + i + '(_|$)'
                str_to = '_' + k + '_'
                result = re.sub(str_from, str_to, result)
            result = re.sub('_', ' ', result)
        return result

    def preprocessing(self, strings):
        """Preprocessing function.

        Args:
            strings (_type_): input string

        Returns:
            _type_: return preprocessed string
        """
        tipe = self.tipe

        # kata-kata tidak berguna
        stopword = [
            'please specify',
            'hold mail',
            'holdmail',
            'dummy',
            'unknown',
            'middlename',
            'npwp',
            'qq',
            'sp_xplor',
            'null',
            'anonymous',
            'not_associate',
        ]

        if isinstance(strings, str):
            # lowercase
            result = strings.lower()

            # remove non ascii chars
            result = re.sub(r'[^\x00-\x7f]', '', result)

            # remove old style name
            if re.match(r'^(?:\w ){2,}[A-z]($|\W)', result):
                result = ''.join(result.split())

            # remove inside bracket
            result = re.sub(r'\([^)]*\)', '', result)

            # remove stopword
            result = reduce(lambda a, b: a.replace(b, ''), stopword, result)

            if tipe == 'nama':
                # remove number
                result = re.sub(r'\d+', '', result)
            if tipe == 'alamat':
                # remove kodepos
                result = re.sub(r' \d\d\d\d\d', '', result)

            # remove punctuation
            result = re.sub(r'[^\w\s]', ' ', result)

            # remove whitespace
            result = result.strip()

            # remove double space
            result = re.sub(r'\s+', ' ', result)

            # standardize
            result = self.standardize(result)

            # remove whitespace
            result = result.strip()

            # remove double space
            result = re.sub(r'\s+', ' ', result)

            # hapus nama 1 kata diulang
            if tipe == 'nama':
                result = [x.strip() for x in result.split()]
                result = ' '.join(list(dict.fromkeys(result)))

            # roman to arabic
            if tipe == 'alamat':
                result = ' '.join(
                    [
                        str(roman.fromRoman(x))
                        if re.match("(^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$)", x)
                        else x
                        for x in result.upper().split()
                    ]
                ).lower()

            return result
        else:
            return strings
