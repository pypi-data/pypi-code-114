"""
Classes and functions useful across both the server and client side of the platform.
"""
from archipelagos.common.data import DataType


# The URL that the platform is located at

PLATFORM_URL = "https://www.archipelagos-labs.com"


class ReturnCodes:
    """
    The return codes used in the platform.
    """
    SUCCESS = 0
    UNEXPECTED_SYSTEM_ERROR = 1
    UNRECOGNISED_USER = 2
    INSUFFICIENT_PERMISSIONS = 3
    UNRECOGNISED_TIME_SERIES = 4
    UNSPECIFIED_FORMAT = 5
    UNRECOGNISED_FORMAT = 6
    UNSPECIFIED_SOURCE = 7
    UNSPECIFIED_CODE = 8
    UNSPECIFIED_ID = 9
    UNSPECIFIED_API_KEY = 10
    INVALID_MAX_SIZE = 11
    INVALID_START = 12
    INVALID_END = 13
    INVALID_FEATURES = 14
    INVALID_FLATTEN = 15
    INVALID_TYPE = 16
    INVALID_ORDER = 17
    TOO_MANY_CONCURRENT_REQUESTS = 18
    TOO_MANY_REQUESTS = 19
    UNRECOGNISED_COLLECTION = 20
    INVALID_FILTERS = 21
    UNRECOGNISED_FILE_STORE = 22
    UNRECOGNISED_FILE = 23
    INVALID_PATTERN = 24
    INVALID_FILENAME = 25


def get_url(data_type: DataType, source: str, code: str, did: str):
    """
    Generates the website URL for a specified dataset.

    :param data_type: The type of the data.
    :type data_type: DataType

    :param source: The source for the data.
    :type source: DataType

    :param code: The code for the data.
    :type code: str

    :param did: The ID for the data.
    :type did: str

    :return: The URL.
    :rtype: str
    """
    return PLATFORM_URL + "/" + str(data_type).lower() + "/" + source + "/" + code + "/" + did
