import unittest
from ratelib import Nucleus


class TestNucleus(unittest.TestCase):
    """
    Testing Nucleus module
    """
    def test_simple(self):
        nuc = Nucleus("fe56")
        self.assertEqual(nuc.A, 56)
        self.assertEqual(nuc.Z, 26)
        self.assertEqual(nuc.N, 30)

    def test_element_names(self):
        for charge in range(126):
            mass = charge * 2 if charge else 1
            nuc = Nucleus(Z=charge, A=mass)
            self.assertIsInstance(nuc.name, str)

    def test_tritium(self):
        nuc1 = Nucleus(A=3, Z=1)
        nuc2 = Nucleus("h3")
        self.assertEqual(nuc1.name, "t")
        self.assertEqual(nuc1.A, 3)
        self.assertTrue(nuc1 == nuc2)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            Nucleus(A=1, Z=3)
        with self.assertRaises(ValueError):
            Nucleus(A=13)

    def test_nearest(self):
        nuc = Nucleus("h3")
        self.assertEqual(len(nuc.neighbours()), 8)


if __name__ == '__main__':
    unittest.main()
