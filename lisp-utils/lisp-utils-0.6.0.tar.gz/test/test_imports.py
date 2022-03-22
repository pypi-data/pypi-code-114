import unittest


class Imports(unittest.TestCase):


    def test_imports(self):
        """
        Verifica che gli import abbiano successo
        """
        try:
            from lisp_utils.configuration import Configuration, ConfigurationFileError
            from lisp_utils.database import Database
        except (ModuleNotFoundError, ImportError) as e:
            print(e)

        self.assertIn('Configuration', locals())
        self.assertIn('ConfigurationFileError', locals())
        self.assertIn('Database', locals())


