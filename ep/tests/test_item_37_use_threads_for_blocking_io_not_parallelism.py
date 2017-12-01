import unittest

from item_37_use_threads_for_blocking_io_not_parallelism import factorize


class TestFactorize(unittest.TestCase):

    def test_factorize(self):
        """Test that the function correctly computes the factors of a number"""
        self.assertEqual(factorize(1), [1])
        self.assertEqual(factorize(2), [1, 2])
        self.assertEqual(factorize(3), [1, 3])
        self.assertEqual(factorize(4), [1, 2, 4])
        self.assertEqual(factorize(10), [1, 2, 5, 10])
        self.assertEqual(factorize(17), [1, 17])
