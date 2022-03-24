import unittest
from unittest.mock import MagicMock
from src.wraperr.wrap_error import wrap_error


class TestWrapError(unittest.TestCase):
    def test_handles_exception_by_default(self):
        expected_exception = Exception()

        def func_that_fails_if_requested(should_fail: bool):
            if should_fail:
                raise expected_exception

        error_handler = MagicMock()

        wrapped = wrap_error(error_handler)(func_that_fails_if_requested)

        error_handler.assert_not_called()

        wrapped(False)
        error_handler.assert_not_called()

        wrapped(True)
        error_handler.assert_called_once()
        error_handler.assert_called_once_with(expected_exception)

    def test_handles_specific_type_of_exception(self):
        expected_exception_type = ValueError
        expected_exception = expected_exception_type()

        def func_that_fails_if_requested(should_fail: bool):
            if should_fail:
                raise expected_exception

        error_handler = MagicMock()

        wrapped = wrap_error(error_handler, ValueError)(
            func_that_fails_if_requested
        )

        error_handler.assert_not_called()

        wrapped(False)
        error_handler.assert_not_called()

        wrapped(True)
        error_handler.assert_called_once()
        error_handler.assert_called_once_with(expected_exception)

    def test_does_not_handle_exception_types_that_are_not_specified(self):
        unexpected_exception_type = Exception
        unexpected_exception = unexpected_exception_type()
        expected_exception_type = ValueError

        def func_that_fails_if_requested(should_fail: bool):
            if should_fail:
                raise unexpected_exception

        error_handler = MagicMock()

        wrapped = wrap_error(error_handler, expected_exception_type)(
            func_that_fails_if_requested
        )

        error_handler.assert_not_called()

        wrapped(False)
        error_handler.assert_not_called()

        with self.assertRaises(unexpected_exception_type):
            wrapped(True)

        error_handler.assert_not_called()

    def test_can_combine_multiple_exception_types(self):
        expected_exception_type_1 = ValueError
        expected_exception_1 = expected_exception_type_1()
        expected_exception_type_2 = AttributeError
        expected_exception_2 = expected_exception_type_2()

        def func_that_fails_with_different_errors_when_requested(
            exception_type
        ):
            if exception_type == expected_exception_type_1:
                raise expected_exception_1
            elif exception_type == expected_exception_type_2:
                raise expected_exception_2

        error_handler_1 = MagicMock()
        error_handler_2 = MagicMock()

        wrapped = wrap_error(error_handler_1, expected_exception_type_1)(
            wrap_error(error_handler_2, expected_exception_type_2)(
                func_that_fails_with_different_errors_when_requested
            )
        )

        error_handler_1.assert_not_called()
        error_handler_2.assert_not_called()

        wrapped(expected_exception_type_1)
        error_handler_1.assert_called_once()
        error_handler_1.assert_called_once_with(expected_exception_1)
        error_handler_2.assert_not_called()

        wrapped(expected_exception_type_2)
        error_handler_1.assert_called_once()
        error_handler_1.assert_called_once_with(expected_exception_1)
        error_handler_2.assert_called_once()
        error_handler_2.assert_called_once_with(expected_exception_2)
