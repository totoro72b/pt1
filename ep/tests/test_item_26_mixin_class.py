import unittest
import copy

from item_26_multiple_inheritance_for_mixin_only import (ToDictMixin,
                                                         BinaryTreeNode,
                                                         BinaryTreeWithParent)

class TestToDictMixin(unittest.TestCase):
    def test_basic_types(self):
        """Test converting a basic object to its dictionary form"""
        class MyClass(ToDictMixin):
            def __init__(self):
                self.a = 'apple'
                self.b = 1
                self.c = ('a', 'b', 'c')
                self.d = {'key': 'val'}
                self.e = ['item1', 'item2']

        obj = MyClass()
        expected = {'a': 'apple',
                    'b': 1,
                    'c': ['a', 'b', 'c'],
                    'd': {'key': 'val'},
                    'e': ['item1', 'item2']
                   }
        self.assertEqual(obj.to_dict(), expected)

    def test_more_complex_example(self):
        self.maxDiff = None
        class MyClass(ToDictMixin):
            def __init__(self):
                self.a = 'apple'
                self.b = 1
                self.c = ('a', 'b', 'c')
                self.d = {'key': 'val'}
                self.e = ['item1', 'item2']

        obj2 = MyClass()
        obj = MyClass()
        obj.d['nested_obj'] = obj2
        obj.e.append(obj2)
        obj.b = obj2

        base = {'a': 'apple',
                'b': 1,
                'c': ['a', 'b', 'c'],
                'd': {'key': 'val'},
                'e': ['item1', 'item2']}

        expected = copy.deepcopy(base)
        expected['d']['nested_obj'] = base
        expected['e'].append(base)
        expected['b'] = base

        self.assertEqual(obj.to_dict(), expected)

    def test_on_binary_tree(self):
        """Test on binary tree structure"""

        right_branch = BinaryTreeNode(7, BinaryTreeNode(6), BinaryTreeNode(8))
        tree = BinaryTreeNode(5, BinaryTreeNode(1), right_branch)
        expected = {'value': 5,
                    'left': { 'value': 1,
                             'left': None,
                             'right': None},
                    'right':{'value': 7,
                             'left': { 'value': 6,
                                       'left': None,
                                       'right': None},
                             'right': { 'value': 8,
                                       'left': None,
                                       'right': None}
                            }
                   }
        self.assertEqual(tree.to_dict(), expected)

    def test_binary_tree_with_parent1(self):
        """Test binary tree with parent"""
        root = BinaryTreeWithParent(1)
        left = BinaryTreeWithParent(2, parent=root)
        right = BinaryTreeWithParent(3, parent=root)
        root.left = left
        root.right = right
        expected = {'value': 1,
                    'left': {'value': 2,
                             'left': None,
                             'right': None,
                              'parent': 1
                            },
                    'right':{'value': 3,
                             'left': None,
                             'right': None,
                              'parent': 1
                            },
                    'parent': None
                   }
        self.assertEqual(root.to_dict(), expected)
