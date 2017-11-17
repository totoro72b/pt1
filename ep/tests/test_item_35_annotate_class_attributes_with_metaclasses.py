import unittest

from item_35_annotate_class_attributes_with_metaclasses import MyRow, Customer


class TestDBRow(unittest.TestCase):

    def test_my_row(self):
        """Test naive implementation of database row"""
        row = MyRow()
        row.foo = 1
        row.bar = 'asdf'
        self.assertEqual(row.foo, 1)
        self.assertEqual(row.bar, 'asdf')

    def test_my_row(self):
        """Test the sophisticated implementation of database row"""
        row = Customer()
        row.first_name = 'gigi'
        row.last_name = 'the kitty'
        self.assertEqual(row.first_name, 'gigi')
        self.assertEqual(row.last_name, 'the kitty')


