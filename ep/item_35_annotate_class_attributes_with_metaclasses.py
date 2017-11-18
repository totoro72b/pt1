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
    def __new__(meta, name, bases, class_dict):
        for k, v in class_dict.items():
            if isinstance(v, Field):
                v.internal_name = '_' + k

        cls  = type.__new__(meta, name, bases, class_dict)  # hmm still not sure how this works
        # print('meta:{}\nname:{}\nbases:{}\nclass_dict:{}\ncls={}'.format(meta, name, bases, class_dict, cls))
        # from nose.tools import set_trace; set_trace()
        return cls


class BetterRow(object, metaclass=Meta):
    pass


class Woo(BetterRow):
    # NOTE
    # silly for testing purposes, to show that Meta.__new__ is called for every layer of inheritance
    # so it's called 3 times in this case. one for Customer (with base class = Woo,)
    # one for Woo (with base class=BetterRow), one for BetterRow (with base class=object)
    # can be seen in the print+nose in Meta
    wow = 'muahaha'


class Customer(Woo):
    """NOTE Field is the descriptor class, and
    the results from Field().__get__() is returned when calling customer.first_name
    when customer.first_name = 'asdf' is called, field.__set__(customer_instance, 'asdf') is called,
    so 'asdf' is assigned to the 'internal_name'('_first_name' in this case) of customer_instance.

    NOTE: the 'internal_name' attribute of the customer_instance is stored in Field, initially
    assigned by the Metaclass. so before everything starts, the field_instance for first_name
    got assigned field.internal_name = '_first_name',
    and the other field instance got field2.internal_name = '_last_name'
    """
    first_name = Field()
    last_name = Field()
