from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


numbers = [(1963309, 2265973), (12334512, 53209783),
           (93756232, 1503821), (1432968, 3475920)]

# item 41 use concurrent.futures for True Parallelism
def gcd(numbers):
    """Return gcd of a and b"""
    a, b = numbers
    if a <= 0 or b <= 0:
        raise ValueError
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

start = time.time()
pool = ProcessPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time.time()
print('ProcessPool: results = {}, used {}s'.format(results, end - start))

# use ThreadPoolExecutor
start = time.time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time.time()
print('ThreadPool: results = {}, used {}s'.format(results, end - start))
