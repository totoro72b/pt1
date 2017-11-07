import unittest
import copy

from item_26_multiple_inheritance_for_mixin_only import ToDictMixin

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
