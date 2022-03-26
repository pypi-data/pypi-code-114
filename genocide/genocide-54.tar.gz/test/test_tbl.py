# This file is placed in the Public Domain.


"table"


import inspect
import os
import sys
import unittest


from genocide.object import Object, keys, values
from genocide.table import Tbl


import genocide.table


Tbl.add(genocide.object)


class Test_Table(unittest.TestCase):

    def test_mod(self):
        self.assertTrue("genocide.object" in keys(Tbl.mod))
