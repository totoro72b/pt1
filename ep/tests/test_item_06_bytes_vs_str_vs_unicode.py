import unittest

from item_06_bytes_vs_str_vs_unicode import to_str, to_bytes


class TestBytesVsStr(unittest.TestCase):

    def test_str(self):
        """Test converting stuff to unicode (str in python 3)"""
        s = 'abcdefg'  # string stays the same
        self.assertTrue(isinstance(s, str))
        s2 = to_str(s)
        self.assertEqual(s, s2)

        b = b'asdf'
        self.assertTrue(isinstance(b, bytes))
        self.assertEqual(to_str(b), 'asdf')


    def test_to_bytes(self):
        """Test converting stuff to bytes"""
        b = b'asdf'  # test bytes stay the same
        self.assertTrue(isinstance(b, bytes))
        self.assertEqual(to_bytes(b), b)

        s = 'abc'
        self.assertTrue(isinstance(s, str))
        s2 = to_bytes(s)
        self.assertEqual(s2, b'abc')
        self.assertTrue(isinstance(s2, bytes))

