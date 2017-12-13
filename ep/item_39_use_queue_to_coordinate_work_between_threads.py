from collections import deque
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
