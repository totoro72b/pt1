import unittest

from item_28_use_abc_for_custom_containers import (FrequencyList,
                                                   BinaryNode,
                                                   IndexableNode,
                                                   SequenceNode,
                                                   NotDoneYet,
                                                   FreebieNode
                                                  )

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

        self.assertEqual(root[0], 1)
        self.assertEqual(root[1], 2)
        self.assertEqual(root[2], 3)
        self.assertEqual(root[3], 4)
        with self.assertRaises(IndexError):
            root[4]

        with self.assertRaises(TypeError):
            len(root)

        self.assertEqual(len(list(root)), 4)  # can turn into a list too!
        self.assertTrue(1 in root)
        self.assertFalse(11 in root)

    def test_sequence_node(self):
        """Test the sequence len interface"""
        root = SequenceNode(3)
        root.left = SequenceNode(1, None, SequenceNode(2))
        root.right = SequenceNode(4)

        self.assertEqual(root[0], 1)
        self.assertEqual(root[1], 2)
        self.assertEqual(root[2], 3)
        self.assertEqual(root[3], 4)
        with self.assertRaises(IndexError):
            root[4]

        self.assertEqual(len(list(root)), 4)  # can turn into a list too!
        self.assertTrue(1 in root)
        self.assertFalse(11 in root)
        self.assertEqual(len(root), 4)  # now can get length!

        with self.assertRaises(AttributeError):
            root.count(1)

        with self.assertRaises(AttributeError):
            root.index(1)

    def test_abc_takes_effect(self):
        """Test(or show) that abc compains when we have not implemented the complete interface"""
        with self.assertRaises(TypeError):
            NotDoneYet()
            root.index(1)

    def test_abc_takes_effect2(self):
        """Test(or show) that abc ensures that we have the complete interface, and get us freebies"""
        root = FreebieNode(3)
        root.left = FreebieNode(1, None, FreebieNode(2))
        root.right = FreebieNode(4)

        # original still works
        self.assertEqual(root[0], 1)
        self.assertEqual(root[1], 2)
        self.assertEqual(root[2], 3)
        self.assertEqual(root[3], 4)
        with self.assertRaises(IndexError):
            root[4]

        self.assertTrue(1 in root)
        self.assertFalse(11 in root)
        self.assertEqual(len(root), 4)

        self.assertEqual(root.count(1), 1)  # get count and index for free!
        self.assertEqual(root.index(1), 0)
