import unittest

from item_38_use_lock_to_prevent_data_races import run_threads_safe


class TestThreadSafeIncrement(unittest.TestCase):

    def test_safe_threads_inc1(self):
        count = run_threads_safe(100, 10000)
        self.assertEqual(count, 100 * 10000)

    # following tests pass. commented out because it takes too long
    # def test_safe_threads_inc2(self):
        # count = run_threads_safe(50, 100000)
        # self.assertEqual(count, 50 * 100000)

    # def test_safe_threads_inc3(self):
        # count = run_threads_safe(10, 500000)
        # self.assertEqual(count, 10 * 500000)
