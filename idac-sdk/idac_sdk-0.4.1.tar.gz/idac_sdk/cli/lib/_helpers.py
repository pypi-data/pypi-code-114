import ujson
from typing import List
import asyncclick as click
import logging

from idac_sdk.log import logger


_debug_options = [
    click.option("--debug", default=False, is_flag=True, help="Enable debug", hidden=True)
]


def set_logger_level(debug: bool) -> None:
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug level enabled")
    else:
        logger.setLevel(logging.WARN)


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


def filter_dict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict


def parse_data(ctx, param, raw: List[str]):
    parsed = dict()
    if raw is not None and len(raw) > 0:
        for v in raw:
            if "=" not in v:
                raise click.BadParameter(
                    message="Data should have format `KEY=VALUE`", ctx=ctx, param=param
                )
            key, value = v.split("=")
            parsed[key] = value if value else ""
        return parsed

    return None


def parse_json(ctx, param, raw: str):
    if raw is not None:
        return ujson.loads(raw)
