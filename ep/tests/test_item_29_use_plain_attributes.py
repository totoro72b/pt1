import unittest

from item_29_use_plain_attributes import (VoltageResistence,
                                          BoundedResistence,
                                          FixedResistence
                                         )


class TestUsePublicAttributes(unittest.TestCase):
    """Test the usage of property and setter"""

    def test_voltage_resistence(self):
        """Test VoltageResistence"""
        vr = VoltageResistence(50)
        self.assertEqual(vr.current, 0)
        vr.voltage = 20
        self.assertEqual(vr.current, 0.4)

    def test_bounded_resistor(self):
        """Test the bounded resistor works"""
        br = BoundedResistence(10)
        self.assertEqual(br.ohms, 10)

        with self.assertRaises(ValueError):
            br.ohms = 0

        with self.assertRaises(ValueError):  # NOTE constructor also uses the setter
            BoundedResistence(-1)

    def test_fixed_resistence(self):
        """Test the FixedResistence works"""
        fr = FixedResistence(10)

        with self.assertRaises(ValueError):  # NOTE constructor also uses the setter
            fr.ohms = 1

        with self.assertRaises(ValueError):
            FixedResistence(0)

