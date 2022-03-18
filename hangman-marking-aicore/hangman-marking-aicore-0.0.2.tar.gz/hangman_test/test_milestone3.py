from hangman.hangman_solution import Hangman
from hangman.hangman_solution import play_game
import unittest
from contextlib import redirect_stdout
import io
from unittest.mock import patch, call

class HangmanTestCase(unittest.TestCase):

    def setUp(self):
        word_list = ['WatermelonBanana']
        f = io.StringIO()
        with redirect_stdout(f):
            self.game = Hangman(word_list, 5)
        self.init_message = f.getvalue()

    def test_check_ask_letter_right(self):
        f = io.StringIO()
        with redirect_stdout(f):
            with unittest.mock.patch('builtins.input', return_value='a'):
                self.game.ask_letter()
            message = f.getvalue()
        
        expected_message = "Nice! a is in the word!\n['_', 'a', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'a', '_', 'a', '_', 'a']\n"
        self.assertEqual(message, expected_message, 'The check_ask_letter method is not working properly, check that the message has the right format')

    def test_check_ask_letter_wrong_guess(self):
        f = io.StringIO()
        with redirect_stdout(f):
            with unittest.mock.patch('builtins.input', return_value='z'):
                self.game.ask_letter()
            message = f.getvalue()
        
        expected_message = "Sorry, z is not in the word.\nYou have 4 lives left.\n"
        self.assertEqual(message, expected_message, 'The check_ask_letter method is not working properly. Check that the message has the right format')

    def test_check_repeated(self):
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', return_value='a') as input_mock:
                self.game.ask_letter()
            # actual_value = f.getvalue()
        f = io.StringIO()
        with redirect_stdout(f):  
            with self.assertRaises(Exception) as context:
                with patch('builtins.input', side_effect=['a']) as input_mock:
                    self.game.ask_letter()
            actual_value = f.getvalue()
        expected = 'a was already tried\n'
        self.assertEqual(actual_value, expected, 'The ask_letter method is not checking for repeated words. If it does, make sure that the message has the right format')


if __name__ == '__main__':

    unittest.main(verbosity=0)
    