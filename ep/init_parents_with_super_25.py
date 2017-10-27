# init parent classes with super
# write diamond class with __init__ to show that it does not work
# write diamond class with super to show it works


class BaseClass(object):
    def __init__(self, num):
        self.num = num


class PlusFiveBad(BaseClass):
    def __init__(self, num):
        BaseClass.__init__(self, num)
        self.num += 5


class TimesTwoBad(BaseClass):
    def __init__(self, num):
        BaseClass.__init__(self, num)
        self.num *= 2


class TimesTwoPlusFiveBad(TimesTwoBad, PlusFiveBad):
    """Illustrate that not using super leads to unintended consequences"""
    def __init__(self, num):
        TimesTwoBad.__init__(self, num)
        PlusFiveBad.__init__(self, num)


class PlusFive(BaseClass):
    def __init__(self, num):
        super(PlusFive, self).__init__(num)
        self.num += 5


class TimesTwo(BaseClass):
    def __init__(self, num):
        super(TimesTwo, self).__init__(num)
        self.num *= 2


class TimesTwoPlusFive(TimesTwo, PlusFive):
    """Illustrate that using super just works"""
    def __init__(self, num):
        super(__class__, self).__init__(num)
