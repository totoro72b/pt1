import unittest
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from item_41_true_parallelism import gcd


# test item 41
class TestParallelism(unittest.TestCase):

    def test_pool_thread(self):
        simple_numbers = [(123, 246), (7, 9)]
        pool = ThreadPoolExecutor(max_workers=2)
        results = list(pool.map(gcd, simple_numbers))
        self.assertEqual(results, [123, 1])

    def test_pool_process(self):
        simple_numbers = [(123, 246), (7, 9)]
        pool = ProcessPoolExecutor(max_workers=2)
        results = list(pool.map(gcd, simple_numbers))
        self.assertEqual(results, [123, 1])

