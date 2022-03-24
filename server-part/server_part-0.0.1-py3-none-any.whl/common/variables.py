"""Константы"""
import logging

# Порт по умолчанию для сетевого ваимодействия
DEF_PORT = 8100
# IP адрес по умолчанию для подключения клиента
DEF_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
FORMAT = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
CURRENT_TIME = 'time'
USER = 'user'
ACCOUNT_LOGIN = 'account_name'
SENDER = 'sender'
DESTINATION = 'to'

# База данных для хранения данных сервера:
SERVER_CONFIG = 'server.ini'

# Прочие ключи, используемые в протоколе
CODE_PRESENCE = 'presence'
CODE_RESPONSE = 'response'
CODE_ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'

LOGGING_LEVEL = logging.DEBUG

GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
ADD_CONTACT = 'add'
USERS_REQUEST = 'get_users'

DATA = 'bin'
PUBLIC_KEY = 'pubkey'
PUBLIC_KEY_REQUEST = 'pubkey_need'

# Словари - ответы:
# 200
RESPONSE_200 = {CODE_RESPONSE: 200}
# 202
RESPONSE_202 = {CODE_RESPONSE: 202,
                LIST_INFO:None
                }
# 400
RESPONSE_400 = {
            CODE_RESPONSE: 400,
            CODE_ERROR: None
        }

RESPONSE_205 = {
    CODE_RESPONSE: 205
}

RESPONSE_511 = {
    CODE_RESPONSE: 511,
    DATA: None
}

