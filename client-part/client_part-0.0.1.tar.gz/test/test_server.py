"""Unit-тесты сервера"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import ACCOUNT_LOGIN, USER,CURRENT_TIME, ACTION, CODE_RESPONSE, CODE_ERROR, CODE_PRESENCE
from server import process_client_message

class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''
    err_dict = {
        CODE_RESPONSE: 400,
        CODE_ERROR: 'Bad Request'
    }
    ok_dict = {CODE_RESPONSE: 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(process_client_message(
            {CURRENT_TIME: '1.1', USER: {ACCOUNT_LOGIN: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', CURRENT_TIME: '1.1', USER: {ACCOUNT_LOGIN: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        self.assertEqual(process_client_message(
            {ACTION: CODE_PRESENCE, USER: {ACCOUNT_LOGIN: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(process_client_message(
            {ACTION: CODE_PRESENCE, CURRENT_TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(process_client_message(
            {ACTION: CODE_PRESENCE, CURRENT_TIME: 1.1, USER: {ACCOUNT_LOGIN: 'Guest1'}}), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(process_client_message(
            {ACTION: CODE_PRESENCE, CURRENT_TIME: 1.1, USER: {ACCOUNT_LOGIN: 'Guest'}}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
