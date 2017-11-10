import unittest

from item_28_use_abc_for_custom_containers import (FrequencyList,
                                                   BinaryNode,
                                                   IndexableNode)

class TestABC(unittest.TestCase):
    def test_get_frequency(self):
        """Test FrequencyList"""
        stuff = ('a', 'b', 'a', 'c')
        fl = FrequencyList(stuff)
        f = fl.get_frequency()
        self.assertEqual(f['a'], 0.5)
        self.assertEqual(f['b'], 0.25)
        self.assertEqual(f['c'], 0.25)
        self.assertEqual(type(fl), FrequencyList)
        self.assertEqual(len(fl), len(stuff))  # can use len method
        self.assertEqual(repr(fl), "['a', 'b', 'a', 'c']")  # can use repr too

    def test_indexable(self):
        """Test indexable binary nodes stuff"""
        root = IndexableNode(3)
        root.left = IndexableNode(1, None, IndexableNode(2))
        root.right = IndexableNode(4)

        self.assertEqual(root[0].value, 1)
        self.assertEqual(root[1].value, 2)
        self.assertEqual(root[2].value, 3)
        self.assertEqual(root[3].value, 4)
