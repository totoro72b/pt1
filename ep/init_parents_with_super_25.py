# init parent classes with super
# write diamond class with __init__ to show that it does not work
# write diamond class with super to show it works

class BaseClass(object):
    def __init__(self, num):
        self.num = num

class PlusFive(BaseClass):
    def __init__(self):
        self.num += 5

class TimesTwo(BaseClass):
    def __init__(self):
        self.num *= 2

class TimesTwoPlusFiveBad(BaseClass, TimesTwo, PlusFive):
    """Illustrate that not using super leads to unintended consequences"""
    def __init__(self, num):
        BaseClass.__init__(num)
        PlusFive.__init__()
        TimesTwo.__init__()
