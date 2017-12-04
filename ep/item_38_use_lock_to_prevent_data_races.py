import threading
# GIL will not protect you from race conditions. use Lock.

def inc_worker(num_times, counter):
    """increment the counter by num_times"""
    for i in range(num_times):
        counter.increment(1)


class CounterNotSafe():
    def __init__(self):
        self.count = 0

    def increment(self, amt):
        self.count += amt


def run_threads(num_threads, count_per_thread):
    """show that using threads without lock doesn't protect you from race condition"""
    counter = CounterNotSafe()
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=inc_worker, args=(count_per_thread, counter))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print('not thread safe: expect to get %d, but got %d' % (num_threads * count_per_thread, counter.count))

run_threads(10, 100000)


class CounterThreadSafe():
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self, amt):
        with self.lock:
            self.count += amt


def run_threads_safe(num_threads, count_per_thread):
    """show that using threads without lock doesn't protect you from race condition"""
    counter = CounterThreadSafe()
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=inc_worker, args=(count_per_thread, counter))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print('thread safe: expect to get %d, but got %d' % (num_threads * count_per_thread, counter.count))
    return counter.count

run_threads_safe(10, 100000)
