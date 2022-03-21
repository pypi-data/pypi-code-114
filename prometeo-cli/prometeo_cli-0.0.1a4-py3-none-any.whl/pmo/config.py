import os

PROMETEO_API_KEY = os.environ.get('PROMETEO_API_KEY')
PROMETEO_PROVIDER = os.environ.get('PROMETEO_PROVIDER')
PROMETEO_USERNAME = os.environ.get('PROMETEO_USERNAME')
PROMETEO_PASSWORD = os.environ.get('PROMETEO_PASSWORD')


def initialize():
    if PROMETEO_API_KEY == None:
        raise Exception('Please set the PROMETEO_API_KEY env variable with your api key')



