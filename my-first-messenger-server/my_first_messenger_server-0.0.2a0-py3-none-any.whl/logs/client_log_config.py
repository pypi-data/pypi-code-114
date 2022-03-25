import sys
import os
import logging
sys.path.append('../')
from common.variables import LOGGING_LEVEL

CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

PATH = os.getcwd()
PATH = os.path.join(PATH, 'client.log')

STREAM = logging.StreamHandler(sys.stderr)
STREAM.setFormatter(CLIENT_FORMATTER)
STREAM.setLevel(logging.INFO)
LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    STREAM_HANDLER = logging.StreamHandler(sys.stdout)
    STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
    STREAM_HANDLER.setLevel(logging.ERROR)
    LOGGER.addHandler(STREAM_HANDLER)

    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.warning('Предупреждение')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
