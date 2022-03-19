import sys
import logging

def configure_logging(logger_name: str, file_name: str, level: str,
                      format: str =
                      '[%(asctime)s][%(levelname)-7s] %(pathname)s at line %(lineno)4d (%(funcName)20s): %(message)s') \
        -> logging.Handler:
    """
    Generic Function that configures a specific logger

    :param logger_name: Name of the logger to configure
    :param file_name: the file name where to write logs. "stderr" and "stdout" are also accepted.
    :param level: string representation of the level, e.g., debug, information, warning, error
    :param format: format of the messages
    """
    handler: logging.Handler
    if file_name == "stdout":
        handler = logging.StreamHandler(stream=sys.stdout)
    elif file_name == "stderr":
        handler = logging.StreamHandler(stream=sys.stderr)
    else:
        handler = logging.FileHandler(file_name)

    handler.setFormatter(logging.Formatter(fmt=format))

    level = logging.getLevelName(level.upper())

    logger = logging.getLogger(logger_name)

    logger.propagate = False

    logger.setLevel(level)
    logger.addHandler(handler)

    return handler