from collections import defaultdict
# passing functions as API hooks
# we'll use defaultdict as an example.
# it takes first function as its argument, rest are same as dict

current = {'a': 1, 'b': 2}
new_dict = {'a': 10, 'c': 10}  # only a exists in current


# approach 1: passing a plain function
def log_missing():
    print 'missing entry!'
    return 0


d = defaultdict(log_missing, current)

for k, v in new_dict.iteritems():  # should trigger one print message
    d[k] += v

expected = {'a': 11, 'b': 2, 'c': 10}
assert(d == expected)


# approach 2: passing a function with stateful closure
def log_missing_w_closure(current, new_dict):
    counter = [0]

    def log_missing():
        print 'missed!'
        counter[0] += 1  #TODO why can't  counter+=1???
        return 0

    d = defaultdict(log_missing, current)
    for k, v in new_dict.iteritems():
        d[k] += v

    return d, counter[0]


# approach 3: passing a class
class MissedCounter(object):
    def __init__(self):
        self.missed = 0

    def missing(self):
        self.missed += 1
        return 0


# approach 4: passing a callable class

class CountMissing(object):
    def __init__(self):
        self.missed = 0

    def __call__(self):
        self.missed += 1
        return 0
