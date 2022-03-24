from datetime import datetime

from typing import Callable
from typing import Any


class SeqTest(object):
    """
    Teste em sequência.

    Todos os testes devem iniciar como
    "test"
    """

    def __init__(self):
        self._last_test = None
        self._tests_exec = 0

    def _run_test(self, method_test: Callable) -> None:
        method_name = method_test.__name__
        self._last_test = method_name

        start_time = datetime.now()
        method_test()  # run test

        finish_time = datetime.now() - start_time
        print(f'{finish_time}: {method_name}')

    def _check_result(self, result: Any, expected: Any, msg: str = None) -> bool:
        if result != expected:
            print('=' * 30)

            if not msg:
                print(f'\033[31m[ ERROR ]\033[m {self._last_test}: {expected} is not {result}')
            else:
                print(f'\033[31m[ ERROR ]\033[m {self._last_test}: {msg}')
            return False

        return True

    def run(self) -> None:
        """Start tests.

        :return: None
        """

        print('PySeqTest')
        print('=========')

        def filter_methods(x) -> list:
            methods = []

            for attr in x:
                attr_object = self.__getattribute__(attr)
                if attr.startswith('test') and callable(attr_object):
                    methods.append(attr_object)

            return methods

        methods_test = filter_methods(self.__dir__())

        total_tests = len(methods_test)
        print(f'{total_tests} testes presentes.\n')

        # try run setup
        try:
            setup = self.__getattribute__('setup')
        except AttributeError:
            pass
        else:
            setup()

        # run tests
        for test in methods_test:
            self._run_test(test)

        # finish all tests
        print('=' * 30)
        print(f'\nAfirmações: {self._tests_exec}')
        print('\033[32m[ OK ]\033[m Testes finalizados')

    def is_true(self, value: Any, msg_error: str = None) -> None:
        """Checks if the value is True.

        :param value: Value to check
        :param msg_error:
        :return:
        """

        result = self._check_result(value, True, msg_error)
        self._tests_exec += 1 if result else exit()

    def is_false(self, value: Any, msg_error: str = None) -> None:
        """Checks if the value is False.

        :param value: Value to check
        :param msg_error:
        :return:
        """

        result = self._check_result(value, False, msg_error)
        self._tests_exec += 1 if result else exit()

    def is_none(self, value: Any, msg_error: str = None) -> None:
        """Checks if the value is None.

        :param value: Value to check
        :param msg_error:
        :return:
        """

        result = self._check_result(value, None, msg_error)
        self._tests_exec += 1 if result else exit()

    def check_any_value(self, value: Any, expected: Any, msg_error: str = None) -> None:
        """Checks whether the value is
        the same as expected.

        :param value: Value to be compared
        :param expected: Value expected
        :param msg_error: Message if the comparison is false
        :return: None
        """

        result = self._check_result(value, expected, msg_error)
        self._tests_exec += 1 if result else exit()


if __name__ == '__main__':
    SeqTest().run()
