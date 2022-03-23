from logging import Logger

from fastapi import Request
from fastapi.encoders import jsonable_encoder


def log_debug_data(logger: Logger, msg: str, request: Request = None, **kwargs) -> None:
    extras = {}
    if request is not None:
        extras['client'] = request.client
    extras.update({key: jsonable_encoder(value) for key, value in kwargs.items()})
    logger.debug(msg, extra=extras)
