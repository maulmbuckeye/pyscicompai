import unittest
from fractal_tree.fractal_tree import get_parameters

SYSTEM_EXIT_SUCCESS = '0'
SYSTEM_EXIT_FAILURE = '[^0]'


class MyTestCase(unittest.TestCase):

    @staticmethod
    def _get_parameters_from_cmd_line_string(cmd_line: str) -> tuple[int, int, bool]:
        cmd_line_list = cmd_line.split(' ') if cmd_line.strip() != '' else []
        return get_parameters(cmd_line_list)

    def test_defaults(self):
        depth, size, has_jitter = self._get_parameters_from_cmd_line_string('')
        self.assertEqual(7, depth)
        self.assertEqual(200, size)
        self.assertTrue(has_jitter)

    def test_depth_9(self):
        depth, size, has_jitter = self._get_parameters_from_cmd_line_string('-d 9')
        self.assertEqual(9, depth)
        self.assertEqual(200, size)
        self.assertTrue(has_jitter)

    def test_nojitter(self):
        depth, size, has_jitter = self._get_parameters_from_cmd_line_string('--nj')
        self.assertEqual(7, depth)
        self.assertEqual(200, size)
        self.assertFalse(has_jitter)

    def test_help(self):
        with self.assertRaisesRegex(SystemExit, SYSTEM_EXIT_SUCCESS):
            _ = self._get_parameters_from_cmd_line_string('-h')

    def test_depth_with_no_arg(self):
        with self.assertRaisesRegex(SystemExit, SYSTEM_EXIT_FAILURE):
            _ = self._get_parameters_from_cmd_line_string('-d')


if __name__ == '__main__':
    unittest.main()
