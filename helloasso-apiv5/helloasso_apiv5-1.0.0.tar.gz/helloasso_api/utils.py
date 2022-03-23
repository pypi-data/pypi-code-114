import logging


def get_log(name: str):
    logger = logging.getLogger(name)
    logger.addHandler(logging.NullHandler())
    return logger
