from collections import deque
from queue import Queue
from time import sleep
import threading
from threading import Lock

# use queue to coordinate work between threads
# my queue that attemps to solve this
class MyQueue(object):
    def __init__(self):
        self.queue = deque()
        self.lock = Lock()

    def get(self):
        with self.lock:
            item = self.queue.popleft()
            return item

    def put(self, item):
        with self.lock:
            self.queue.append(item)


class Worker(threading.Thread):
    """a worker that process an item and move it to the next queue"""

    def __init__(self, func, in_queue, out_queue, total_count):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.num_polled = 0
        self.num_done = 0
        self.total_count = total_count

    def run(self):
        """process an item from in_queue and put it to the out_queue"""
        while self.num_done < self.total_count:
            try:
                self.num_polled += 1
                item = self.in_queue.get()
            except IndexError:
                print('empty in queue')
                sleep(0.01)
            else:
                item = self.func(item)
                self.out_queue.put(item)
                self.num_done += 1


# placeholder functions
def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item

# queues to hold the (intermediary) work items
total_items = 50000
to_download_queue = MyQueue()
download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()

workers = [Worker(download, to_download_queue, download_queue, total_items),
           Worker(resize, download_queue, resize_queue, total_items),
           Worker(upload, resize_queue, upload_queue, total_items)
          ]

# put initial item to specify what needs to be downloaded
for i in range(total_items):
    to_download_queue.put(object())

# start the pipeline process
for t in workers:
    t.start()

for t in workers:
    t.join()

print('total num items processed %d. total times polled %d.' % (workers[-1].num_done, workers[-1].num_polled))

################
# try Queue class check out if task_done called order matters? or threads matter?
q = Queue()
# consumer
def consume():
    print('consumer waiting')
    q.get()
    q.task_done()
    print('consumer done')

# producer
t = threading.Thread(target=consume)
t.start()

t2 = threading.Thread(target=consume)
t2.start()

for i in range(2):
    q.put(object())
print('producer waiting...')
q.join()
print('producer done')


# a class for closable queue
class ClosableQueue(Queue):
    SENTINEL = object()

    # def __init__(self):
        # self.queue = Queue()

    # def put(self, item):
        # self.queue.put(item)

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        try:
            item = self.get()
            if item is self.SENTINEL:
                return  # exit the thread???
            yield item
        finally:
            self.task_done()


# Stoppable Worker that utilizes the closable queue
class StoppableWorker(threading.Thread):
    """a worker that gets an item from in_queue and transforms it and puts on the out_queue"""
    def __init__(self, in_queue, out_queue, func):
        super().__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.func = func

    def run(self):
        for item in self.in_queue:  # this run method will exit when SENTINEL is reached in ClosableQueue
            item = self.func(item)
            self.out_queue.put(item)


# create the pipes
closable_download_queue = ClosableQueue()
closable_resize_queue = ClosableQueue()
closable_upload_queue = ClosableQueue()
closable_done_queue = ClosableQueue()

# fill in the initial items
for i in range(100):
    closable_download_queue.put(object())

closable_download_queue.close()

# line up the pipes
links = [(closable_download_queue, closable_resize_queue, download),
         (closable_resize_queue, closable_upload_queue, resize),
         (closable_upload_queue, closable_done_queue, upload)]

for q_in, q_out, func in links:
    t = StoppableWorker(q_in, q_out, func)
    t.start()

closable_upload_queue.join()
print('upload done')
print('num items in done queue %d' % len([x for x in closable_done_queue]))
