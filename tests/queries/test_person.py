# Tests for queries pertaining to person objects.
import os

from trompace.queries import person

from tests import CeTestCase


class TestPerson(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "person")

    def test_query(self):
        expected = self.read_file(os.path.join(self.data_dir, "query_person_parameter.txt"))
        created_person = person.query_person(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        assert created_person == expected

    def test_query_all(self):
        expected = self.read_file(os.path.join(self.data_dir, "query_person.txt"))
        created_person = person.query_person()
        assert created_person == expected
