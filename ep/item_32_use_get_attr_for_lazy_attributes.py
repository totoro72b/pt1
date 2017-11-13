# __get_attr__ and __set_attr__ for lazy attributes
"""
__get_attr__  is called
1. if it's defined, AND
2. if it does not exists in instance.__dict__ (that's when AttributeError occurs)


__get_attribute__ is called
1. if it's defined
2. when the attribute exists OR does NOT exist in instance.__dict__

__get_attr__ and __get_attribute__ are called by getattr and hasattr
"""

class Lazy1(object):
    def __init__(self):
        self.exists = False

    def __getattr__(self, name):
        print('get attr %s' % name)
        try:
            return super().__getattr__(name)
        except AttributeError:
            print('attribute error for %s' % name)
            value = 'value for % name' % name
            setattr(self, name, value)
            return value

class Lazy2(object):
    def __init__(self):
        self.exists = False

    def __getattribute__(self, name):
        print('get attribute %s' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            print('attribute error for %s' % name)
            value = 'value for % name' % name
            setattr(self, name, value)
            return value
