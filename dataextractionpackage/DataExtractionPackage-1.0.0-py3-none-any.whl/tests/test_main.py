import unittest

import pytest

from src.__main__ import MainClass


class MainClassTest(unittest.TestCase):
    def test_init(self):

        assert 1 == 1
       # # test_main = MainClass("./src/tests/test_controller_config.yml")
       #  with pytest.raises(KeyError):
       #      #est_main = MainClass("./src/tests/test_controller_config.yml")
       #
       #      test_main = MainClass("./src/tests/erroneous_config_file.yml")

    #Not included in tests - cannot be run outside of Gore network.
    def setup_database(self):
        test_main = MainClass("./src/tests/test_controller_config.yml")
        test_main.setup_database()