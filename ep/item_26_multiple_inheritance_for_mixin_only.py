from collections import abc
# item 26: use muptiple inheritance for mixin only
# a mixin that transforms a python object to a dictionary that's ready for seralization
class ToDictMixin(object):
    def to_dict(self):
        """Return a dictionary representation of this object"""
        return self._traverse(self.__dict__)

    def _traverse(self, obj):
        """Return a dictionary representation of this obj"""
        if isinstance(obj, ToDictMixin):
            return obj.to_dict()
        if isinstance(obj, dict):
            return {k: self._traverse(v) for k, v in obj.items()}
        if isinstance(obj, tuple) or isinstance(obj, list):
            return [self._traverse(item) for item in obj]
        # if it's any other object with __dict__ attr, use it!
        if hasattr(obj, '__dict__'):
            return self._traverse(obj.__dict__)
        if isinstance(obj, str) or isinstance(obj, int):
            return obj

        raise ValueError('does not handle type {}'.format(type(obj)))
