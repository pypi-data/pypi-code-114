from rich import print

from ..build.service_foundry_client import BadRequestException


def handle_exception(exception):
    if type(exception) == BadRequestException:
        print(f"status={exception.status_code}, message={exception.message}")
    elif type(exception) == ConnectionError:
        print(f"Couldn't connect to Servicefoundry.")
    else:
        print(f"status={exception.status_code}, message={exception.message}")
        print(exception)
    raise exception
