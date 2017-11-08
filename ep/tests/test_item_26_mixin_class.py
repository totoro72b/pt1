import unittest
import copy
import json

from item_26_multiple_inheritance_for_mixin_only import (ToDictMixin,
                                                         ToJsonMixin,
                                                         BinaryTreeNode,
                                                         BinaryTreeWithParent,
                                                         BinaryTreeWithJson,
                                                         NamedSubTree,
                                                         DatacenterRack)

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
        root.left = BinaryTreeWithParent(2, parent=root)
        root.right = BinaryTreeWithParent(3, parent=root)
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

    def test_binary_tree_with_parent2(self):
        """Test other classes that use tree as attributes"""

        root = BinaryTreeWithParent(1)
        root.left = BinaryTreeWithParent(2, parent=root)
        root.right = BinaryTreeWithParent(3, parent=root)
        named_tree = NamedSubTree('awesome tree', root)

        expected = {'name': 'awesome tree',
                    'tree': {'value': 1,
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
                   }

        self.assertEqual(named_tree.to_dict(), expected)

    # def test_tree_json_mixin(self):
        # # TODO would be cool the recursively "inflate" all the nodes so this would pass
        # """Test ToDictMixin and ToJsonMixin used together in trees"""

        # right_branch = BinaryTreeWithJson(7, BinaryTreeWithJson(6), BinaryTreeWithJson(8))
        # tree = BinaryTreeWithJson(5, BinaryTreeWithJson(1), right_branch)
        # expected = {'value': 5,
                    # 'left': { 'value': 1,
                             # 'left': None,
                             # 'right': None},
                    # 'right':{'value': 7,
                             # 'left': { 'value': 6,
                                       # 'left': None,
                                       # 'right': None},
                             # 'right': { 'value': 8,
                                       # 'left': None,
                                       # 'right': None}
                            # }
                   # }
        # self.assertEqual(BinaryTreeWithJson.from_json(tree.to_json()), tree)

    def test_datacenter_json_mixin(self):
        """Test ToDictMixin and ToJsonMixin used together in flat objects"""
        switch_specs = {'ports': 5, 'speed': 1000}
        machines_specs = [{'ram': 8e9, 'cpu': 3e9, 'disk': 1e12},
                          {'ram': 12e9, 'cpu': 4e9, 'disk': 1e12},
                          {'ram': 16e9, 'cpu': 5e9, 'disk': 1e12}]
        datacenter = DatacenterRack(switch_specs, machines_specs)
        self.assertEqual(DatacenterRack.from_json(datacenter.to_json()), datacenter)

    def test_datacenter_json_mixin_round_trip_json_serialization(self):
        """Test ToDictMixin and ToJsonMixin used together in flat objects"""
        serialized = """{"switch": {"ports": 5, "speed": 1000},
                          "machines": [
                              {"ram": 89, "cpu": 39, "disk": 112},
                              {"ram": 129, "cpu": 49, "disk": 112},
                              {"ram": 169, "cpu": 59, "disk": 112}
                          ]
                     }"""
        round_trip = DatacenterRack.from_json(serialized).to_json()
        # self.assertEqual(round_trip, serialized)
        # the above 2 version might not have the same white spaces etc., so test below instead
        self.assertEqual(json.loads(round_trip), json.loads(serialized))
