class Example(object):
    foo = 5
    _duh = 2
    __bar = 3

    def get_bar(self):
        """can be accessed by object methods"""
        return self.__bar

    @classmethod
    def get_bar_classmethod(cls):
        return cls.__bar

    @classmethod
    def get_bar_classmethod_instance(cls, instance):
        return instance.__bar


class SubExample(Example):
    def get_bar(self):
        """subclass still need to prepend PARENT's class name
           to access parent's private attribute
        """
        # return self.__bar  # NOTE: will not work, cuz it's trying _SubExample__bar
        return self._Example__bar

    @classmethod
    def get_bar_classmethod(cls):
        return cls._Example__bar

    @classmethod
    def get_bar_classmethod_instance(cls, instance):
        return instance._Example__bar


# below show why NOT to use private attributes for protection

class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)


class MyIntegerClass(MyClass):
    """A subclass that returns an integer"""
    def get_value(self):
        return int(self._MyClass__value)

########### the following change would break MyIntegerClass ########3

class MyBaseClass(object):
    """move to a base class from MyClass"""
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

class MyNewClass(MyBaseClass):
    pass

class MyIntegerNewClass(MyNewClass):
    """A subclass that returns an integer"""
    def get_value(self):
        return int(self._MyNewClass__value)

################# Do use private to avoid namespace conflicts
class ValueClass(object):
    _value = 5

    def get_value(self):
        return self._value


class SubValueClass(ValueClass):
    _value = 15


class GoodValueClass(object):
    __value = 5

    def get_value(self):
        return self.__value

class GoodSubValueClass(GoodValueClass):
    __value = 15

