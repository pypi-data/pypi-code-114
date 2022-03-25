import sys
import os
import logging.handlers
sys.path.append('../')
from common.variables import LOGGING_LEVEL

SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

PATH = os.getcwd()
PATH = os.path.join(PATH, 'server.log')

STEAM = logging.StreamHandler(sys.stderr)
STEAM.setFormatter(SERVER_FORMATTER)
STEAM.setLevel(logging.INFO)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STEAM)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    STREAM_HANDLER = logging.StreamHandler(sys.stdout)
    STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
    STREAM_HANDLER.setLevel(logging.WARNING)
    LOGGER.addHandler(STREAM_HANDLER)

    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.warning('Предупреждение')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
