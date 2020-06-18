# Tests for queries pertaining to person objects.
import os
import unittest

from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries import person

from tests import util


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "person")

    def test_query(self):
        expected = util.read_file(self.data_dir, "query_person_parameter.txt")
        created_person = person.query_person(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        self.assertEqual(created_person, expected)

    def test_query_all(self):
        expected = util.read_file(self.data_dir, "query_person.txt")
        created_person = person.query_person()
        self.assertEqual(created_person, expected)
