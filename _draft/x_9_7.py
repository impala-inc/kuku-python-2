# x_9_7
#
#

import unittest


class DictTest(unittest.TestCase):
    def test_array(self):
        self.assertDictEqual({'banana': 'バナナ', 'apple': 'リンゴ'}, {
                             'apple': 'リンゴ', 'banana': 'バナナ'})


if __name__ == '__main__':
    unittest.main()
