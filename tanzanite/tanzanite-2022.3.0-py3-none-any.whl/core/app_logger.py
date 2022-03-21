# -*- coding: utf-8 -*-

"""
Logger customization.
"""

# Standard imports
import logging
import logging.config
import os
import sys

from typing import (
    Dict,
    Union,
)

CLIFF_LOG_FILE_MESSAGE_FORMAT = '[%(asctime)s] %(levelname)-8s %(name)s %(message)s'  # noqa
CLIFF_CONSOLE_MESSAGE_FORMAT = '%(message)s'
DEFAULT_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DETAILED_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
ACCESS_LOG_FORMAT = '%(client_addr)s %(levelname)-8s - "%(request_line)s" %(status_code)s'  # noqa
CONSOLE_LOG_FORMAT = '%(name)-12s: %(levelname)-8s %(message)s'
LOG_LEVEL = (
    'DEBUG'
    if os.environ.get('TANZANITE_DEBUG', 'false') == 'true'
    else 'INFO'
)


# https://stackoverflow.com/questions/66602480/fastapi-uvicorn-not-logging-errors
#
# add your handler to it (in my case, I'm working with quart, but you can do
# this with Flask etc. as well, they're all the same):
# UVICORN_LOG_CONFIG['log_config']['loggers']['quart'] = {
#     'handlers': ['default'], 'level': 'INFO'
# }


def get_file_handler(log_file=None):
    """
    Return a file logging handler.
    """
    if log_file is None:
        log_file = f"tanzanite-{os.environ.get('D2_ENVIRONMENT')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
    return file_handler


def get_stream_handler():
    """
    Return a stream logging handler.
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(CONSOLE_LOG_FORMAT))
    return stream_handler


def get_logger(name, log_level=logging.INFO, log_file=None):
    """
    Add custom handlers to logger and return it for use.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    if log_file is not None:
        logger.addHandler(get_file_handler(log_file=log_file))
    logger.addHandler(get_stream_handler())
    return logger


def get_logging_config(
    log_level: Union[str, None] = LOG_LEVEL,
    log_file: Union[str, None] = None,
) -> Dict:
    """
    Return a dictionary containing 'log_config' contents suitable for
    passing to `uvicorn.run()`.
    """
    # fh = logging.handlers.WatchedFileHandler('tanzanite.log')
    # fh = logging.FileHandler('tanzanite.log')
    # stream_dest = ('ext://sys.stderr' if log_file is None else fh)
    # Based on default per: print(json.dumps(uvicorn.config.LOGGING_CONFIG))
    # logging_config = {}
    # logging_config['log_config'] = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'formatters': {
    #         'default': {
    #             '()': 'uvicorn.logging.DefaultFormatter',
    #             'fmt': f'{DEFAULT_LOG_FORMAT}',
    #             'use_colors': True,
    #         },
    #         'access': {
    #             '()': 'uvicorn.logging.AccessFormatter',
    #             'fmt': f'{ACCESS_LOG_FORMAT}',
    #             'use_colors': True,
    #         },
    #     },
    #     'handlers': {
    #         'default': {
    #             'formatter': 'default',
    #             'level': 'NOTSET',
    #             'class': 'logging.StreamHandler',
    #             'stream': stream_dest,
    #         },
    #         'access': {
    #             'formatter': 'access',
    #             'level': 'NOTSET',
    #             'class': 'logging.StreamHandler',
    #             'stream': stream_dest,
    #         },
    #         'console': {
    #             'formatter': 'default',
    #             'level': log_level,
    #             'class': 'logging.StreamHandler',
    #             'stream': 'ext://sys.stderr',
    #         }
    #     },
    #     'loggers': {
    #         'alembic': {
    #             'handlers': ['default'],
    #             'level': log_level,
    #             'propagate': True,
    #         },
    #         'stevedore.extension': {
    #             'handlers': ['default'],
    #             'level': log_level,
    #             'propagate': True,
    #         },
    #         'tanzanite': {
    #             'handlers': ['default'],
    #             'level': log_level,
    #             'propagate': True,
    #         },
    #         'uvicorn.asgi': {
    #             'handlers': ['default'],
    #             'level': log_level,
    #             'propagate': True,
    #         },
    #         'uvicorn.error': {
    #             'handlers': ['default'],
    #             'level': log_level,
    #             'propagate': True,
    #         },
    #         'uvicorn.access': {
    #             'handlers': ['access'],
    #             'level': log_level,
    #             'propagate': False,
    #         },
    #     },
    # }
    access_log_file = log_file.replace('.log', '-access.log')
    logging_config = {}
    logging_config['log_config'] = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'detailed': {
                'class': 'logging.Formatter',
                'format': DETAILED_LOG_FORMAT,
                'use_colors': False,
            },
            'access': {
                'class': 'logging.Formatter',
                'format': ACCESS_LOG_FORMAT,
                'use_colors': False,
            },
            'console': {
                'class': 'logging.Formatter',
                'format': CONSOLE_LOG_FORMAT,
                'use_colors': True,
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'detailed',
                'filename': log_file,
                'level': 'DEBUG',
                'mode': 'a',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
                'level': 'INFO',
                'stream': 'ext://sys.stderr',
            },
            'access': {
                'class': 'logging.FileHandler',
                # 'formatter': 'access',
                'level': log_level,
                'filename': access_log_file,
                'mode': 'a',
            },
        },
        'loggers': {
            'alembic': {
                'handlers': ['file'],
                # 'level': 'DEBUG',
                'propagate': True,
            },
            'stevedore.extension': {
                'handlers': ['file', 'console'],
                # 'level': 'DEBUG',
                'propagate': False,
            },
            'tanzanite': {
                'handlers': ['file', 'console'],
                # 'level': 'INFO',
                'propagate': False,
            },
            'tanzanite-api': {
                'handlers': ['file', 'console'],
                # 'level': 'INFO',
                'propagate': False,
            },
            'uvicorn.asgi': {
                'handlers': ['access', 'console'],
                # 'level': 'DEBUG',
                'propagate': True,
            },
            'uvicorn.error': {
                'handlers': ['access'],
                # 'level': 'DEBUG',
                'propagate': False,
            },
            'uvicorn.access': {
                'handlers': ['access'],
                # 'level': 'INFO',
                'propagate': False,
            },
        },
    }
    return logging_config


def global_configure_logging(
    log_file=None,
    verbose_level=1,
    stderr=sys.stderr,
    log_file_message_format=None,
    console_message_format=None,
) -> None:
    """
    Configure logging to file and/or console.
    """
    # This function is patterned after the cliff `app.configure_logging()`
    # method and is abstracted out here to more consistently handle
    # logging across all Tanzanite components.
    #
    # It creates a new `root_logger` that contains handlers for
    # log output when `--log-file` is specified on the command line,
    # along with a `StreamHandler` for console output.
    #
    # FIXME: Reconcile differences between above and this function.
    if log_file_message_format is None:
        log_file_message_format = CLIFF_LOG_FILE_MESSAGE_FORMAT
    if console_message_format is None:
        console_message_format = CLIFF_CONSOLE_MESSAGE_FORMAT
    root_logger = logging.getLogger('')
    file_log_level = {
        0: logging.INFO,
        1: logging.DEBUG,
        2: logging.DEBUG,
    }.get(verbose_level, logging.DEBUG)
    root_logger.setLevel(file_log_level)
    # Set up logging to a file
    if log_file:
        file_handler = logging.FileHandler(filename=log_file)
        formatter = logging.Formatter(log_file_message_format)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    # Always send higher-level messages to the console via stderr
    console = logging.StreamHandler(stderr)
    console_level = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }.get(verbose_level, logging.DEBUG)
    console.setLevel(console_level)
    formatter = logging.Formatter(console_message_format)
    console.setFormatter(formatter)
    root_logger.addHandler(console)
    for log_source in [
        'alembic',
        'stevedore.extension',
        # 'urllib3.connectionpool',
        'uvicorn.asgi',
        'uvicorn.errors',
        'uvicorn.access',
    ]:
        logger = logging.getLogger(log_source)
        logger.setLevel(console_level)
    # Ignore these logs
    for log_source in [
        'multipart.multipart',
    ]:
        logger = logging.getLogger(log_source)
        logger.setLevel(logging.WARNING)
    if verbose_level < 2:
        logging.captureWarnings(True)
    return


def configure_logging(
    log_level: Union[str, None] = LOG_LEVEL,
    log_file: Union[str, None] = None,
):
    """
    Configure logging module for consistent logging output across
    Tanzanite components (including `alembic`, which configures
    logging itself in a manner that disables logging configurations
    already put in place.

    See: https://stackoverflow.com/questions/66602480/fastapi-uvicorn-not-logging-errors

    """  # noqa
    # for handler in logging.root.handlers[:]:
    #     logging.root.removeHandler(handler)
    config = get_logging_config(
        log_level=log_level,
        log_file=log_file,
    )
    if log_file is not None:
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            datefmt='%y%m%dT%H:%M%S',
            force=True,
        )
    logging.config.dictConfig(config['log_config'])
    return config
