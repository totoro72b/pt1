import unittest

from chap_04_01_parity_of_a_word import (
    count_bits_naive,
    count_bits_better,
    compute_parity_w_cache
)


class TestParity(unittest.TestCase):
    def test_count_bits_naive(self):
        self.assertEqual(count_bits_naive(0), 0)
        self.assertEqual(count_bits_naive(1), 1)
        self.assertEqual(count_bits_naive(2), 1)
        self.assertEqual(count_bits_naive(3), 2)
        self.assertEqual(count_bits_naive(7), 3)
        self.assertEqual(count_bits_naive(15), 4)
        with self.assertRaises(ValueError):
            count_bits_naive(-1)

    def test_count_bits_better(self):
        self.assertEqual(count_bits_better(0), 0)
        self.assertEqual(count_bits_better(1), 1)
        self.assertEqual(count_bits_better(2), 1)
        self.assertEqual(count_bits_better(3), 2)
        self.assertEqual(count_bits_better(7), 3)
        self.assertEqual(count_bits_better(15), 4)
        with self.assertRaises(ValueError):
            count_bits_naive(-1)


    def test_compute_parity_w_cache(self):
        self.assertEqual(compute_parity_w_cache(0), 0)
        self.assertEqual(compute_parity_w_cache(1), 1)
        self.assertEqual(compute_parity_w_cache(2), 1)
        self.assertEqual(compute_parity_w_cache(3), 0)
        self.assertEqual(compute_parity_w_cache(7), 1)
        self.assertEqual(compute_parity_w_cache(15), 0)

        # works with negatives!
        self.assertEqual(compute_parity_w_cache(-1), 0)
        self.assertEqual(compute_parity_w_cache(0x0001000100010001), 0)
        self.assertEqual(compute_parity_w_cache(0x00010011ffff000f), 1)
