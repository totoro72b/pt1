from collections import abc
# item 26: use muptiple inheritance for mixin only
# a mixin that transforms a python object to a dictionary that's ready for seralization
class ToDictMixin(object):
    def to_dict(self):
        """Return a dictionary representation of this object"""
        return self._traverse('none', self.__dict__)

    def _traverse(self, key, obj):
        """Return a dictionary representation of this obj"""
        if isinstance(obj, ToDictMixin):
            return obj.to_dict()
        if isinstance(obj, dict):
            return {k: self._traverse(k, v) for k, v in obj.items()}
        if isinstance(obj, tuple) or isinstance(obj, list):
            return [self._traverse(key, item) for item in obj]
        # if it's any other object with __dict__ attr, use it!
        if hasattr(obj, '__dict__'):
            return self._traverse(key, obj.__dict__)

        return obj


class BinaryTreeNode(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTreeNode):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left, right)
        self.parent = parent

    # override so the backref to parent does not cause infinite recursion
    def _traverse(self, key, obj):
        # if the key is parent, stop the recursion and return parent's value instead
        if key == 'parent' and isinstance(obj, BinaryTreeNode):
            return obj.value
        return super()._traverse(key, obj)
        # p2: do i have to pass the key inorder to know the key?

