# x_9_6
#
#

import unittest


class ListTest(unittest.TestCase):
    def test_array(self):
        self.assertListEqual([7, 5, 3], [7, 5, 3])


if __name__ == '__main__':
    unittest.main()
