import unittest

from lc204_count_primes import Solution


class TestCountPrimes(unittest.TestCase):
    def setUp(self):
        self.soln = Solution()
        self.test_primes = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),
        (4, 2),
        (5, 2),
        (6, 3),
        (7, 3),
        (8, 4),
        (9, 4),
        (10, 4),
        (11, 4),
        (12, 5)]

    def test_count_primes_slow(self):
        """Slow version: Test some simple cases"""
        for n, num_primes in self.test_primes:
            self.assertEqual(self.soln.countPrimes_slow(n), num_primes)

    def test_count_primes(self):
        """better version: Test some simple cases"""
        for n, num_primes in self.test_primes:
            self.assertEqual(self.soln.countPrimes(n), num_primes)

    def test_count_primes_improved(self):
        """Improved: Test some simple cases"""
        for n, num_primes in self.test_primes:
            self.assertEqual(self.soln.countPrimesImproved(n), num_primes)
