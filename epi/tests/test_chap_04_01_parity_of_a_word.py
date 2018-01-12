import unittest

from chap_04_01_parity_of_a_word import count_bits_naive, count_bits_better


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
