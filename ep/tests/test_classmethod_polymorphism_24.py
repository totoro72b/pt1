# this deals with item 24: use classmethod polymorphism to construct objects generically
import os
import unittest
import tempfile
import shutil

from classmethod_polymorphism_24 import (map_reduce,
                                         LineCounterWorker,
                                         FileInput)


class TestClassmethodPolymorphism(unittest.TestCase):
    def setUp(self):
        self.dir_path = '/tmp/line_counter_tests/'
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)

    def tearDown(self):
        print ('deleting folder...')
        shutil.rmtree(self.dir_path)

    def test_map_reduce(self):
        """
        Test map reduce end to end,
        since there isn't much logic for each individual class,
        let's just test them end to end.
        """
        # write files
        lst = [2, 5, 9, 10]
        for num in lst:
            f = open(os.path.join(self.dir_path, str(num) + '.txt'), 'w')
            for i in range(num):
                f.write('abc\n')
            f.close()

        # count lines
        params = {'file_dir': self.dir_path}
        total = map_reduce(FileInput, LineCounterWorker, params)
        print ('total is {}'.format(total))
        self.assertEqual(total, sum(lst))
