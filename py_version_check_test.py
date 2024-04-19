import unittest
from py_version_check import *

class TestVersions(unittest.TestCase):

    def test_minor_normal1(self):
        self.assertEqual(minor_version("1.0", "1.1"), True)

    def test_minor_normal2(self):
        self.assertEqual(minor_version("0.1", "1.1"), True)

    def test_minor_normal3(self):
        self.assertEqual(minor_version("0.1.0", "1.1.0"), True)

    def test_minor_normal4(self):
        self.assertEqual(minor_version("0.1.0", "0.1.1"), True)

    def test_minor_normal5(self):
        self.assertEqual(minor_version("0.1.0", "0.1.0"), False)

    def test_major_normal1(self):
        self.assertEqual(major_version("0.1.0", "0.1.0"), False)

    def test_equal_normal1(self):
        self.assertEqual(equal_version("0.1.0", "0.1.0"), True)

    def test_minor_tricky1(self):
        self.assertEqual(minor_version("01.0", "010.0"), True)

    def test_minor_tricky2(self):
        self.assertEqual(minor_version("01.0", "0.010.0"), False)

    def test_minor_tricky3(self):
        self.assertEqual(minor_version("01.0", "00002.010.0"), True)

    def test_minor_tricky4(self):
        self.assertEqual(minor_version("01.0", str(0.1)), False)

    def test_minor_tricky5(self):
        self.assertEqual(minor_version("001.30", str(1.35)), True)

if __name__ == '__main__':
    unittest.main()