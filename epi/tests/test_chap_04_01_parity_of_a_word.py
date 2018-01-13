import unittest

from chap_04_01_parity_of_a_word import (
    count_bits_naive,
    count_bits_better,
    compute_parity_w_cache,
    compute_parity_log,
    right_prop_rightmost_set_bit,
    compute_x_mod_power_of_2,
    is_x_power_of_2
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

    def test_compute_parity_log(self):
        self.assertEqual(compute_parity_log(0), 0)
        self.assertEqual(compute_parity_log(1), 1)
        self.assertEqual(compute_parity_log(2), 1)
        self.assertEqual(compute_parity_log(3), 0)
        self.assertEqual(compute_parity_log(7), 1)
        self.assertEqual(compute_parity_log(15), 0)

        # works with negatives!
        self.assertEqual(compute_parity_log(-1), 0)
        self.assertEqual(compute_parity_log(0x0001000100010001), 0)
        self.assertEqual(compute_parity_log(0x00010011ffff000f), 1)

    def test_right_prop_rightmost_set_bit(self):
        # 0101 0000 = 2^4 + 2^6 = 16 + 64 = 80
        # 0101 1111 = 80 + 15 = 95
        self.assertEqual(right_prop_rightmost_set_bit(80), 95)
        # works for negative too
        # 1111....0000 = -1 - 15 = -16
        # 1111....1111 = -1
        self.assertEqual(right_prop_rightmost_set_bit(-16), -1)

    def test_compute_x_mod_power_of_2(self):
        self.assertEqual(compute_x_mod_power_of_2(77, 3), 5)

    def test_is_x_power_of_2(self):
        self.assertEqual(is_x_power_of_2(1), True)
        self.assertEqual(is_x_power_of_2(2), True)
        self.assertEqual(is_x_power_of_2(4), True)
        self.assertEqual(is_x_power_of_2(32), True)
        self.assertEqual(is_x_power_of_2(1024), True)
        self.assertEqual(is_x_power_of_2(1023), False)
