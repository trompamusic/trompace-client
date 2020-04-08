import os
import unittest


class CeTestCase(unittest.TestCase):

    data_dir = ""

    def read_file(self, filename):
        if self.data_dir:
            with open(os.path.join(self.data_dir, filename)) as fp:
                return fp.read()
