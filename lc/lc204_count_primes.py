import math

class Solution(object):
    def countPrimes_slow(self, n):
        """Return the number of primes p where p < n and n >= 0"""
        if n <= 2:
            return 0
        # if n == 2, 2 is a rpime. but not include that
        primes = [2]
        for k in range(3, n):
            # test if any of the primes divides k
            is_prime = True
            for p in primes:
                if k % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(k)
        return len(primes)

    def countPrimes(self, n):
        """Return the number of primes p where p < n and n >= 0 (fast version)"""
        if n <= 2:
            return 0
        # now at least [0, 1, 2, ...]
        primes = [True] * n
        primes[0], primes[1] = False, False
        for k in range(2, n):
            if primes[k]:
                # knock out multiples of k
                primes[k*2:n:k] = [False] * len(primes[k*2:n:k])
        return primes.count(True)

    def countPrimesImproved(self, n):
        """Return the number of primes p where p < n and n >= 0 (fast version)"""
        if n <= 2:
            return 0
        # now at least [0, 1, 2, ...]
        primes = [True] * n
        primes[0], primes[1] = False, False
        for k in range(2, math.ceil(n**0.5)):  # NOTE: since we start at k*k, it's meaningless empty set when k > sqrt(n)
            if primes[k]:
                # knock out multiples of k
                # NOTE: Improved: start from k*k because k*2 shoulda been knocked out by prime 2
                primes[k*k:n:k] = [False] * len(primes[k*k:n:k])
        return primes.count(True)




