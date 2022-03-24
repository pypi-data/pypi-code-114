import unittest
import os
import numpy as np
from ratelib import Rate, RateFilter


def readfile(file_path):
    lines = []
    with open(file_path, "r") as fd:
        lines = fd.readlines()
    return lines


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(TEST_DIR, "data")
REAC1 = readfile(os.path.join(DATA_DIR, "reac1.reaclib"))
REAC4 = readfile(os.path.join(DATA_DIR, "reac4.reaclib"))
REAC11 = readfile(os.path.join(DATA_DIR, "reac11.reaclib"))
RATE1 = readfile(os.path.join(DATA_DIR, "rate1.talys"))


class TestRate(unittest.TestCase):
    """
    Test Rate and RateFilter modules
    """
    def test_loading(self):
        rate = Rate()
        rate.init_by_lines(REAC1)
        self.assertEqual(rate.chapter, 1)
        self.assertEqual(rate.rtype, "w")

    def test_format(self):
        rate = Rate()
        rate.init_by_lines(REAC11)
        self.assertEqual(rate.reaclib_format(), REAC11)

    def test_constant(self):
        rate = Rate()
        rate.init_by_values(nuclei=["n", "p"], chapter=1, rtype="w", rvals=1.)
        self.assertTrue(rate.is_constant())

    def test_fit(self):
        rate = Rate()
        rvals = np.loadtxt(RATE1)[::20, :2]
        err = rate.init_by_values(reaction="tb180 + n -> tb181", rtype=" ",
                                  dset="cust", reverse=False, rvals=rvals)
        self.assertTrue(err < 0.1)

    def test_filter(self):
        rate = Rate()
        rate.init_by_lines(REAC4)
        # True
        r_f = RateFilter(rtype="n")
        self.assertTrue(r_f.check_matches(rate))
        r_f = RateFilter(reaction="n + p -> d")
        self.assertTrue(r_f.check_matches(rate))
        r_f = RateFilter(reaction="n + p -> d")
        self.assertTrue(r_f.check_matches(rate))
        r_f = RateFilter(initial=["p"])
        self.assertTrue(r_f.check_matches(rate))
        r_f = RateFilter(final=["d"])
        self.assertTrue(r_f.check_matches(rate))
        r_f = RateFilter(nuclei=["n", "d"], chapter=4)
        self.assertTrue(r_f.check_matches(rate))
        # False
        r_f = RateFilter(final=["n"], exact=True)
        self.assertFalse(r_f.check_matches(rate))


if __name__ == '__main__':
    unittest.main()
