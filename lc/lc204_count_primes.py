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


