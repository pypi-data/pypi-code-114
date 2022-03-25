import inspect
import logging
import sys
import traceback
from socket import socket
sys.path.append('../')
import logs.client_log_config
import logs.server_log_config

if sys.argv[0].find('client_dist') == -1:
    logger = logging.getLogger('server_dist')
else:
    logger = logging.getLogger('client_dist')


def log(func_to_log):
    """ A decorator logs function calls. """

    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        logger.debug(f'Была вызвана функция {func_to_log.__name__} с параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}. '
                     f'Вызов из функции {traceback.format_stack()[0].strip().split()[-1]}. '
                     f'Вызов из функции {inspect.stack()[1][3]}.')
        return ret

    return log_saver


def login_required(func):
    """
    A decorator checks that the client is authorized on the server.
    """
    def checker(*args, **kwargs):
        from server.core import MessageProcessor
        from common.variables import ACTION, PRESENCE
        if isinstance(args[0], MessageProcessor):
            found = False
            for arg in args:
                if isinstance(arg, socket):
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True

            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == PRESENCE:
                        found = True
            if not found:
                raise TypeError
        return func(*args, **kwargs)

    return checker
