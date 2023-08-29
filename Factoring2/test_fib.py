import unittest
from fac import fac


class MyTestCase(unittest.TestCase):
    def test_fibone(self):
        self.assertEqual([], fac(1))

    def test_fac_of_2_is_2(self):
        self.assertEqual([2], fac(2))

    def test_facfive(self):
        self.assertEqual([5], fac(5))

    def test_factsix(self):
        self.assertEqual([2, 3], fac(6))

    def test_fac8(self):
        self.assertEqual([2, 2, 2], fac(8))

    def test_fac32(self):
        self.assertEqual([2, 2, 2, 2, 2], fac(32))

    def test_fac58(self):
        self.assertEqual([2, 29], fac(58))


if __name__ == '__main__':
    unittest.main()
