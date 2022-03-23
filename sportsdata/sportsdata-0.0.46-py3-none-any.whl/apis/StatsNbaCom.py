from ..nba.constants import *
import types
from enum import Enum
from inspect import isclass

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

import requests
import logging
import json
from pandas import DataFrame

################################
# Decorators for the NBA Class #
################################
def clean_inputs(func):
    """
    Iterates over a function's parameters checking for Enum, if one is found, the value is used instead

    Args:
        func: Underlying function to be wrapped

    Returns: Wrapped function

    """

    def new_func(*args, **kwargs):
        cleaned_args = []
        for i in range(len(args)):
            if isclass(type(args[i])) and issubclass(type(args[i]), Enum):
                clean_arg = args[i].value
                cleaned_args.append(clean_arg)
            else:
                cleaned_args.append(args[i])

        for key, val in kwargs.items():
            if isclass(type(val)) and issubclass(type(val), Enum):
                kwargs[key] = val.value

        data = func(*cleaned_args, **kwargs)
        return data

    return new_func


class StatsNbaCom:
    def __init__(self):
        # Get a logger
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
        self.logger = logging.getLogger('sportsdata')

        # Read the specification file
        self.specs = json.loads(pkg_resources.read_text('sportsdata.data', 'stats.nba.com.json'))
        self.logger.info(self.specs.keys())

        self.parameters = {}
        for param in self.specs['parameters']:
            self.parameters[param['name']] = {
                'default': param['default'],
                'values': param['values']
            }

        # Create methods for each api endpoint
        for endpoint in self.specs['stats_endpoints']:
            self.add_api_method(endpoint)

    @staticmethod
    def _get_row_set(rs):
        data = []
        for row in rs['rowSet']:
            data_point = dict(zip([h.lower() for h in rs['headers']], row))
            data.append(data_point)
        return data

    @staticmethod
    def _get_data_frames(response, rename_to={}):
        """
        Parse the response for any results and load them into data frames
        Args:
            response:
            rename_to:

        Returns:
            All Result Sets Found as Data Frames

        """
        frames = {}
        info = json.loads(response.text)
        result_sets = info['resultSets']
        for rs in result_sets:
            rs_name = rs['name']
            if rs_name in rename_to.keys():
                rs_name = rename_to[rs_name]

            frames[rs_name] = DataFrame(rs['rowSet'], columns=rs['headers'])

        # Check if there is only one result, if so no need for a dictionary
        if len(frames) == 1:
            key = next(iter(frames))
            frames = frames[key]

        return frames

    @staticmethod
    def _get_dictionary(response):
        return json.loads(response.text)

    def add_api_method(self, endpoint):
        """
        Dynamically builds a method for each endpoint in the specification file
        :param endpoint:
        :param cls:
        :param name:
        :return:
        """

        def dynamic_method(self2: StatsNbaCom, **kwargs):
            url = endpoint['url']
            parameters = endpoint['parameters']

            # Set the log level, default to DEBUG messages
            log_level = logging.DEBUG
            if 'log_level' in kwargs:
                log_level = kwargs['log_level']

            self2.logger.log(log_level, url)
            self2.logger.log(log_level, kwargs)

            # Determine the ResponseType
            return_type = ReturnType.DICTIONARY.value
            if 'ReturnType' in kwargs:
                return_type = kwargs['ReturnType']

            url_parameters = {}
            # Add each parameter to the url
            for param in parameters:
                value = ''

                # Was this parameter passed into to the method?
                if param in kwargs:
                    value = kwargs[param]

                # Does this parameter have a default value
                elif param in self.parameters:
                    value = self.parameters[param]['default']

                # Is the value for the parameter a legal value for this parameter
                # if param in self.parameters and value not in self.parameters[param]['values']:
                #     self.logger.warning(f"The value '{value}' is not a legal value for '{param}'")
                #     value = ''

                # Add the parameter and its value to the dictionary of url parameters
                url_parameters[param] = value

            self2.logger.log(log_level, url_parameters)
            request_headers = {
                'Host': 'stats.nba.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'x-nba-stats-origin': 'stats',
                'x-nba-stats-token': 'true',
                'Connection': 'keep-alive',
                'Referer': 'https://stats.nba.com/',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
            }
            response = requests.get(url, params=url_parameters, headers=request_headers, timeout=10)

            if return_type == ReturnType.DICTIONARY or return_type == ReturnType.DICTIONARY.value:
                return_value = self2._get_dictionary(response)
            elif return_type == ReturnType.RESPONSE or return_type == ReturnType.RESPONSE.value:
                return_value = response
            elif return_type == ReturnType.DATA_FRAMES or return_type == ReturnType.DATA_FRAMES.value:
                return_value = self2._get_data_frames(response)

            # Close the response before leaving
            response.close()

            return return_value

        dynamic_method.__name__ = endpoint['name']
        setattr(self, dynamic_method.__name__, types.MethodType(dynamic_method, self))
