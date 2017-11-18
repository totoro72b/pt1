import json


registry = {}

def register(cls):
    registry[cls.__name__] = cls


class Meta(type):
    def __new__(meta, name, bases, class_dict):  # m nbc
        cls = type.__new__(meta, name, bases, class_dict)
        register(cls)
        return cls


class Serializable(object, metaclass=Meta):
    """Provide method to serialize the args of a class"""
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args,
                           'class': self.__class__.__name__
                          })


def deserialize(serialized):
    params = json.loads(serialized)
    cls = registry[params['class']]
    return cls(*params['args'])


class Point3Db(Serializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z
