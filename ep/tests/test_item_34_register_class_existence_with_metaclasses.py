import unittest

from item_34_register_class_existence_with_metaclasses import Point3Db, deserialize


class TestMetaRegistration(unittest.TestCase):
    """Test the usage of meta classes to register classes for easy deserialization"""

    def test_auto_register_with_meta(self):
        """Test auto register with metaclass for deserialization"""
        p3 = Point3Db(10, -7, 3)
        serialized = p3.serialize()
        obj = deserialize(serialized)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, -7)
        self.assertEqual(obj.z, 3)
