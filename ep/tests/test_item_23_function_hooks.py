# test item 23: passing functions as API hooks
import unittest
from collections import defaultdict

from item_23_function_hook import log_missing_w_closure, MissedCounter, CountMissing


class TestFunctionHooks(unittest.TestCase):

    def setUp(self):

        self.current = {'a': 1, 'b': 2}
        self.new_dict = {'a': 10, 'c': 10}  # only a exists in current
        self.expected = {'a': 11, 'b': 2, 'c': 10}

    def test_approach2_func_w_closure(self):
        """Test passing a function with stateful closure as the API hook"""
        d, missed_count = log_missing_w_closure(self.current, self.new_dict)
        self.assertEqual(d, self.expected)
        self.assertEqual(missed_count, 1)

    def test_approach3_class(self):
        """Test passing a counter class's method as the API hook"""
        counter = MissedCounter()

        d = defaultdict(counter.missing, self.current)
        for k, v in self.new_dict.items():
            d[k] += v

        self.assertEqual(counter.missed, 1)

    def test_approach4_callable_class(self):
        """Test passing a class with callable interface as the hook"""
        counter = CountMissing()
        self.assertTrue(callable(counter))

        d = defaultdict(counter, self.current)
        for k, v in self.new_dict.items():
            d[k] += v

        self.assertEqual(counter.missed, 1)
