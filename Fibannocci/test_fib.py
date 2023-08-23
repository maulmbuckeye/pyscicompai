import unittest
import fib


class MyTestCase(unittest.TestCase):

    f = fib.BorrowedFibGen()

    def test_fib1(self):
        self.assertEqual(1, self.f.fib(1))

    def test_fib3(self):
        self.assertEqual(2, self.f.fib(3))

    def test_fib10(self):
        self.assertEqual(55, self.f.fib(10))

    def test_fib20(self):
        self.assertEqual(6765, self.f. fib(20))


if __name__ == '__main__':
    unittest.main()
