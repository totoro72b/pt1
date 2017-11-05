import unittest

from lc204_count_primes import Solution


class TestCountPrimes(unittest.TestCase):
    def setUp(self):
        self.soln = Solution()

    def test_count_primes_slow(self):
        """Test some simple cases"""
        self.assertEqual(self.soln.countPrimes_slow(0), 0)
        self.assertEqual(self.soln.countPrimes_slow(1), 0)
        self.assertEqual(self.soln.countPrimes_slow(2), 0)
        self.assertEqual(self.soln.countPrimes_slow(3), 1)
        self.assertEqual(self.soln.countPrimes_slow(4), 2)
        self.assertEqual(self.soln.countPrimes_slow(5), 2)
        self.assertEqual(self.soln.countPrimes_slow(6), 3)
        self.assertEqual(self.soln.countPrimes_slow(7), 3)
        self.assertEqual(self.soln.countPrimes_slow(8), 4)
        self.assertEqual(self.soln.countPrimes_slow(9), 4)
        self.assertEqual(self.soln.countPrimes_slow(10), 4)
        self.assertEqual(self.soln.countPrimes_slow(11), 4)
        self.assertEqual(self.soln.countPrimes_slow(12), 5)
