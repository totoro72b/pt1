# use descriptor class and metaclasses to annotate class attributes

# simple naive example
class NaiveField(object):
    def __init__(self, name):
        """record the name and internal name"""
        # self.name = name  # optional
        self.internal_name = '_' + name

    def __get__(self, instance, instance_type):
        if instance is None: return self  # when is instance None?
        # NOTE: no need for super here. getattr calls __getattr__, not __get__
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class MyRow(object):
    foo = NaiveField('field1')  # here, names don't actually have to match as long as they're unique
    bar = NaiveField('bar')

# downside of the above approach is that, you have to duplicate the names (or put something at 2 places)
#################### approach 2 that does not require duplication

class Field(object):
    def __init__(self):
        self.internal_name = None  # will be assigned by metaclass

    def __get__(self, instance, instance_type):
        if instance is None: return self  # when is instance None?
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):
    def __new__(meta, name, bases, class_dict):  # mabc
        for k, v in class_dict.items():
            if isinstance(v, Field):  # why is it Field??
                print('before assignment, dict={}'.format(v.__dict__))
                v.internal_name = '_' + k
                print('after assignment, dict={}'.format(v.__dict__))

        cls  = type.__new__(meta, name, bases, class_dict)  # hmm still not sure how this works
        return cls


class BetterRow(object, metaclass=Meta):
    pass


class Customer(BetterRow):
    first_name = Field()
    last_name = Field()


