import time
import threading
import select

# use threads for blocking io, not for parallelism
# for example do something and try out the time
def factorize(n):
    """return factors of n where n > 0"""
    # basically just try each number from 1 to itself. if remainer == 0, then return it
    factors = []
    for i in range(1, n + 1):
        if n % i  == 0:
            factors.append(i)

    return factors


numbers = [1234561, 2345671, 3456781, 4567891]

start = time.time()
for n in numbers:
    factors = factorize(n)
    print('factors for {} is {}'.format(n, factors))

end = time.time()
print('used %.3f' % (end - start))


# check that using threads does NOT speed up

class FactorNumber(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = factorize(self.number)


threads = []
start = time.time()
for n in numbers:
    t = FactorNumber(n)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    print('result for {} is {}'.format(t.number, t.factors))

end = time.time()
print('threads used %.3f' % (end - start))

### without using class
# start = time.time()
# threads = []
# for n in numbers:
    # def func():
        # return factorize(n)
    # t = threading.Thread(target=func)
    # t.start()
    # threads.append(t)

# for t in threads:
    # t.join()
# end = time.time()
# print('threads approach 2 used %.3f' % (end - start))

# ***** however, you can use threads for doing sys calls for blocking IO. it DOES run in parallel in that case

def slow_sys_call():
    select.select([], [], [], 0.1)  # a sys call that takes 0.1s long


def without_threads():
    for i in range(5):
        slow_sys_call()


start = time.time()
without_threads()
end = time.time()
print('sys call without threads, it took %.3fs' % (end - start))


def compute_helicopter_location():
    """something to do meanwhile"""
    pass

threads = []
start = time.time()
for i in range(5):
    t = threading.Thread(target=slow_sys_call)
    t.start()
    threads.append(t)

compute_helicopter_location()

for t in threads:
    t.join()

end = time.time()
print('sys call using threads, it took %.3fs' % (end - start))
