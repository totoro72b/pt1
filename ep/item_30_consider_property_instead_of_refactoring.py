import datetime

# consider using property over refactoring
# original stuff here with leaky bucket
class LeakyBucket(object):
    """The leaky bucket algo ensures that whenever the bucket is filled,
    the amount of quota does not carry over from one period to the next."""

    def __init__(self, max_quota, delta):
        self.period_delta = datetime.timedelta(seconds=delta)
        self.max_quota = max_quota
        self.reset_time = datetime.datetime.now()  # after reset_time, butcket becomes empty
        self.quota_consumed = 0

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        """set the amount in the bucket"""
        pass

    @property
    def in_period(self):
        """Return True iff < period_delta time since last reset time"""
        return self.datetime.datetime.now() <= self.reset_time + self.period_delta

    def refill(self, amount):
        """Refill the bucket to full without overflow"""
        # if it's after period_delta since last reset time,
        # then reset the bucket so nothing carries over to this period
        pass

    # deduct from quota
    def deduct(self, amount):
        """Deduct amount from the bucket"""
        pass


