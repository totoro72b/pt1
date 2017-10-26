import unittest

from init_parents_with_super_25 import TimesTwoPlusFiveBad

class TestSuperParents(unittest.TestCase):
    def test_bad(self):
        """Test that not using has unintended consequences"""
        num = 10
        obj = TimesTwoPlusFiveBad(10)
        self.assertTrue(obj.num != 10*2+5)
        # actually it equals 

iasdfasdfsdaf

