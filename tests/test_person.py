# Tests for mutations pertaining to person objects.
import os
import unittest

from trompace.queries import person as person_query
from trompace.mutations.person import mutation_create_person, mutation_update_person, mutation_delete_person
from tests import util


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "person")

    def test_query(self):
        expected = util.read_file(self.data_dir, "query_person_parameter.txt")

        created_person = person_query.query_person(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        self.assertEqual(created_person, expected)

    def test_query_all(self):
        expected = util.read_file(self.data_dir, "query_person.txt")

        created_person = person_query.query_person()
        self.assertEqual(created_person, expected)

    def test_create(self):
        expected = util.read_file(self.data_dir, "create_person.txt")

        created_person = mutation_create_person(title="A. J. Fynn", contributor="https://www.cpdl.org",
                                                creator="https://www.upf.edu", source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                                                language="en", format_="text/html",
                                                description="Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology")
        self.assertEqual(created_person, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "update_person.txt")

        created_update = mutation_update_person('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                title="A. J. Fynn")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "delete_person.txt")

        created_delete = mutation_delete_person('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)