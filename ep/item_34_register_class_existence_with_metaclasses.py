import json


registry = {}  # class name -> class

def register(cls):
    registry[cls.__class__.__name__] = cls

def register_class(cls):
    registry[cls.__class__.__name__] = cls


def deserialize(serialized):
    params = json.loads(serialized)
    print(registry)
    cls = registry[params['class_name']]
    return cls(*params['args'])


class RegisterMeta(type):
    def __new__(meta, name, bases, class_dict):
        """Register class under class name"""
        cls = type.__new__(meta, name, bases, class_dict)
        register(cls)
        return cls


# use metaclasses to register classes, so you can deserialize a class super easily!
class Serializable(object, metaclass=RegisterMeta):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        """Serialize the args for this object"""
        return json.dumps({'args': self.args,
                           'class_name': self.__class__.__name__})


class Point3D(Serializable):
    """Describe a 3D point"""
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z


############ code from book
class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })
    def __repr__(self):
        pass


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class RegisteredSerializable(BetterSerializable,
                             metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z
