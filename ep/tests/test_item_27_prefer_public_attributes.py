# most of the stuff aren't really tests; it's really just to test my own understanding
import unittest

from item_27_prefer_public_attributes import (Example,
                                              SubExample,
                                              MyClass,
                                              MyIntegerClass,
                                              MyIntegerNewClass,
                                              ValueClass,
                                              SubValueClass,
                                              GoodValueClass,
                                              GoodSubValueClass)


class TestPublicVsPrivateAttributes(unittest.TestCase):

    def test_basics(self):
        """Test the basic mechanism of public vs private attributes"""
        e = Example()
        self.assertEqual(e.foo, 5)
        self.assertEqual(e._duh, 2)
        with self.assertRaises(AttributeError):
            e.__bar
        self.assertEqual(e._Example__bar, 3)

        self.assertEqual(e.get_bar(), 3)
        self.assertEqual(e.get_bar_classmethod(), 3)
        self.assertEqual(Example.get_bar_classmethod(), 3)
        self.assertEqual(Example.get_bar_classmethod_instance(e), 3)

    def test_subclass(self):
        """Test if subclass can access parent's stuff"""
        e = SubExample()
        self.assertEqual(e.foo, 5)
        self.assertEqual(e._duh, 2)
        with self.assertRaises(AttributeError):
            e.__bar
        self.assertEqual(e._Example__bar, 3)  # NOTE subclass still append parent's classname

        self.assertEqual(e.get_bar(), 3)
        self.assertEqual(e.get_bar_classmethod(), 3)
        self.assertEqual(SubExample.get_bar_classmethod(), 3)
        self.assertEqual(SubExample.get_bar_classmethod_instance(e), 3)

    def test_brittle_subclass(self):
        myint = MyIntegerClass(10)
        self.assertEqual(myint.get_value(), 10)

        myintnew = MyIntegerNewClass(10)
        with self.assertRaises(AttributeError):
            myintnew.get_value()

    def test_subclass_override(self):
        v = ValueClass()
        self.assertEqual(v.get_value(), 5)

        v = SubValueClass()
        self.assertNotEqual(v.get_value(), 5)  # NOTE subclass overrode parent's value!!

    def test_subclass_not_override(self):
        v = GoodValueClass()
        self.assertEqual(v.get_value(), 5)

        v = GoodSubValueClass()
        self.assertEqual(v.get_value(), 5)  # NOTE subclass no longer overrides parent's value here
