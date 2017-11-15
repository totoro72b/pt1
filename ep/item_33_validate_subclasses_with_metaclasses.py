# just mess around to try out stuff
class MyMeta(type):
    def __new__(meta, name, bases, class_dict):
        print(meta, name, bases, class_dict)
        return type.__new__(meta, name, bases, class_dict)


class Base(object):
    base_stuff = 456


class MixIn(object):
    m = 'mix!'


class MyClass(Base, MixIn, metaclass=MyMeta):
    stuff = 123

    def __init__(self):
        self.instance_var = 'foovar'

    def foo(self):
        pass


# use meta classes for class validation
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        print(meta, name, bases, class_dict)
        # do not validate abstract Polygon class
        if bases != (object,) and class_dict['sides'] < 3:
            raise ValueError('polygon must have at least 3 sides!!1')

        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    """A base class for defining a polygon"""
    sides = None

    @property
    def interior_angles(self):
        return (self.sides - 2) * 180


# comment, otherwise nothing in this file can be imported!
# class PolygonBad(Polygon):
    # """A class that defines a polygon"""
    # sides = 2


class Triangle(Polygon):
    """yeah a triangle"""
    sides = 3
