import unittest

from item_33_validate_subclasses_with_metaclasses import Polygon, Triangle


class TestMetaValidation(unittest.TestCase):

    def test_bad_poly(self):
        """Test that a bad class cannot be evaluated"""

        with self.assertRaises(ValueError):
            class PolygonBad(Polygon):
                """A class that defines a polygon"""
                sides = 2

    def test_good_poly(self):
        """Test that a good class can be imported"""
        t = Triangle()
        self.assertEqual(t.interior_angles, 180)


