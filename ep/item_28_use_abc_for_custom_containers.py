from collections.abc import Sequence
# when need to define customized container types, inherit from abc to make sure you don't miss shit

# by subclassing from list, you get all of list's standard functionalities. no need to use abc
class FrequencyList(list):
    """A list that also returns frequency"""
    def __init__(self, stuff):
        super().__init__(stuff)

    def get_frequency(self):
        d = {}
        total = 0
        for item in self:
            d.setdefault(item, 0)
            d[item] += 1
            total += 1

        for k, v in d.items():
            d[k] = v/total

        return d

# but when building something that acts like a list but doesn't inherit from list,
# use abc to help you reinforce the interface
class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):
    num = 0

    def search(self, node, index):
        """return (found, count) the node at the given index if exists, otherwise (False, None)
        index is zero based.
        """
        self.num = 0
        return self._traversal(self, index+1)


    def _traversal(self, node, n):
        if node.left:
            found, x = self._traversal(node.left, n)
            if found:
                return found, x
        self.num += 1
        if self.num == n:
            return node, self.num

        if node.right:
            found, x = self._traversal(node.right, n)
            if found:
                return found, x
        return None, self.num

    def __getitem__(self, index):
        """return the ith node of the binary tree (zero indexed)"""
        found, count = self.search(self, index)
        if found:
            return found.value
        raise IndexError


# list interface also requires __len__
class SequenceNode(IndexableNode):
    def __len__(self):
        found, count = self.search(self, -1)
        return count


# we still need to define stuff like count, index
# with abc's sequence interface,  we can get it for free!
class FreebieNode(SequenceNode, Sequence):
    pass


class NotDoneYet(Sequence):
    pass

