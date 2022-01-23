# x_9_4
#
#

import unittest


def zero_divide():
    100 / 0


class ZeroDivisionTest(unittest.TestCase):
    def test_zero_divide(self):
        with self.assertRaises(ZeroDivisionError):
            zero_divide()


if __name__ == '__main__':
    unittest.main()
