# this deals with item 24: use classmethod polymorphism to construct objects generically
import os
import threading

class BaseInput(object):
    """Base class for Input"""
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, params):
        """Each subclass needs to provide its own generate_input method"""
        raise NotImplementedError

class FileInput(BaseInput):
    """File Input"""
    def __init__(self, path):
        self.path = path

    def read(self):
        """return the result of reading the file"""
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, params):
        # you can call this witout knowing how to make an object
        file_dir = params['file_dir']
        inputs = []
        for filename in os.listdir(file_dir):
            path = os.path.join(file_dir, filename)
            inputs.append(cls(path))
        return inputs


class BaseWorker(object):
    """Base Worker class"""
    def __init__(self, input):
        self.input = input
        self.output = None

    def map(self):
        raise NotImplementedError

    def reduce(self):
        raise NotImplementedError

    @classmethod
    def generate_workers(cls, inputs):
        workers = []
        for inp in inputs:
            workers.append(cls(inp))
        return workers
    # check if generate workers can work without providing classmethod...


class LineCounterWorker(BaseWorker):
    """Line Counter Worker"""

    def map(self):
        self.output = self.input.read().count('\n')

    def reduce(self, other):
        self.output += other.output


# to construct objects generically
def map_reduce(input_cls, worker_cls, params):
    inputs = input_cls.generate_inputs(params)
    if len(inputs) == 0:
        raise ValueError('cannot map reduce on inputs with 0 length')

    workers = worker_cls.generate_workers(inputs)
    threads = []
    for w in workers:
        threads.append(threading.Thread(target=w.map))

    for t in threads: t.start()
    for t in threads: t.join()

    # all threads finished. reduce the results
    w0 = workers[0]
    for w in workers[1:]:
        w0.reduce(w)

    return w0.output
