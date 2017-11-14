import unittest

from item_32_use_get_attr_for_lazy_attributes import EasyLookup

class TestGetSetAttr(unittest.TestCase):

    def test_easy_lookup(self):
        """simple est to make sure it runs"""
        d = {'asdf': 1, 'APPLE': 'hi'}
        r = EasyLookup(d)
        self.assertEqual(r.asdf, 1)
        self.assertEqual(r.APPLE, 'hi')
        with self.assertRaises(AttributeError):
            r._data  # because _data is not in self._data! muahaha

