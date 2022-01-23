# x_9_3
#
#

import unittest


class OnitaijiMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class OnitaijiMemberTests(unittest.TestCase):
    def setUp(self):
        self.momotaro = OnitaijiMember('桃太郎', 16)

    def test_name(self):
        self.assertEqual(self.momotaro.name, '桃太郎')

    def test_age(self):
        self.assertEqual(self.momotaro.age, 16)

    def tearDown(self):
        del self.momotaro


if __name__ == '__main__':
    unittest.main()
