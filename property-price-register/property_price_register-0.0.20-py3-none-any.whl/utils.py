import os
import zipfile

import requests

from property_price_register.constants import PPR_URL


def isnan(num):
    return num != num


def download_zip(filename):
    req = requests.get(PPR_URL, verify=False)
    with open(filename, 'wb') as output_file:
        output_file.write(req.content)


def extract_zip(filename):
    dirpath = os.path.splitext(filename)[0]
    os.mkdir(dirpath)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(dirpath)
