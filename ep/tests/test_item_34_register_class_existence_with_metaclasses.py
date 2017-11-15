import unittest

from item_34_register_class_existence_with_metaclasses import Point3D, deserialize, Vector3D


class TestMetaRegistration(unittest.TestCase):
    """Test the usage of meta classes to register classes for easy deserialization"""

    # def test_serialization(self):
        # """test serialize an object"""
        # pt = Point3D(1,2,3)
        # serialized = pt.serialize()
        # obj = deserialize(serialized)
        # self.assertEqual(pt.x, obj.x)
        # self.assertEqual(pt.y, obj.y)
        # self.assertEqual(pt.z, obj.z)

    def test_book_example(self):
        """Why works in the book but not in my code?"""
        v3 = Vector3D(10, -7, 3)
        data = v3.serialize()
        obj = deserialize(data)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, -7)
        self.assertEqual(obj.z, 3)

