import unittest
import factor as f


class MyTestCase(unittest.TestCase):
    def test_two(self):
        self.assertEqual({2: 1}, f.factor(2))

    def test_power_of_two(self):
        self.assertEqual({2: 3}, f.factor(8))

    def test_three(self):
        self.assertEqual({3: 1}, f.factor(3))

    def test_power_of_three(self):
        self.assertEqual({3: 3}, f.factor(27))

    def test_six(self):
        self.assertEqual({2: 1, 3: 1, 5: 1}, f.factor(30))

    def test_seven(self):
        self.assertEqual({7: 1}, f.factor(7))

    def test_one(self):
        """
        Should this be {1: 1}?
        :return:
        """
        self.assertEqual({}, f.factor(1))

    def test_49(self):
        self.assertEqual({7: 2}, f.factor(49))


if __name__ == '__main__':
    unittest.main()
