import unittest

from item_25_init_parents_with_super import TimesTwoPlusFiveBad, TimesTwoPlusFive


class TestSuperParents(unittest.TestCase):
    def test_bad(self):
        """Test that not using has unintended consequences"""
        obj = TimesTwoPlusFiveBad(10)
        self.assertFalse(obj.num == 10*2+5)
        self.assertEqual(obj.num, 10 + 5)

    def test_good(self):
        """Test that it works as expected using super"""
        obj = TimesTwoPlusFive(10)
        self.assertTrue(obj.num == (10+5)*2)
        print('MRO is...')
        print(TimesTwoPlusFive.mro())
