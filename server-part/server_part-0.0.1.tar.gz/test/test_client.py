"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import ACCOUNT_LOGIN, USER,CURRENT_TIME, ACTION, CODE_RESPONSE, CODE_ERROR, CODE_PRESENCE
from client import create_answer, process_answer

class TestClass(unittest.TestCase):

    def test_def_create_answer(self):
        """Тест коректного запроса"""
        test = create_answer()
        test[CURRENT_TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: CODE_PRESENCE, CURRENT_TIME: 1.1, USER: {ACCOUNT_LOGIN: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(process_answer({CODE_RESPONSE: 200}), 'Ответ сервера: 200 OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(process_answer({CODE_RESPONSE: 400, CODE_ERROR: 'Bad Request'}), 'Ответ сервера: 400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_answer, {CODE_ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()

