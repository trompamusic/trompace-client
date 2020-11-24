import os
import unittest
from graphql.language import parse, print_ast


class CeTestCase(unittest.TestCase):

    @property
    def test_directory(self):
        return os.path.dirname(__file__)

    data_dir = ""

    def read_file(self, filename):
        if self.data_dir:
            with open(os.path.join(self.data_dir, filename)) as fp:
                return fp.read()

    def compare_queries(self, q1,q2):
        # It normalizes the queries in the same format and suppresses format differences (i.e. spaces, tables, \n)
        return print_ast(parse(q1)) == print_ast(parse(q2))