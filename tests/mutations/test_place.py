# Tests for mutations pertaining to entry points.
import os

from tests import CeTestCase
from trompace.mutations import place


class TestPlace(CeTestCase):
    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "place")

    def test_mutation_create_place(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_place.txt"))

        mutation = place.mutation_create_place(
            title="Place title", contributor="https://placedatabase.com", creator="https://upf.edu",
            source="https://placedatabase.com/place", format_="text/html", name="Place title", language="en")

        assert expected == mutation

    def test_mutation_update_place(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_place.txt"))

        mutation = place.mutation_update_place(
            identifier="cf515c79-c32f-43c8-a9ef-39f5daa7f847",
            title="Another place", name="Another place")

        assert expected == mutation

    def test_mutation_delete_place(self):
        expected = """mutation {
  DeletePlace(
identifier: "placeid"
) {
identifier
}
}"""
        mutation = place.mutation_delete_place('placeid')
        assert mutation == expected

    def test_mutation_merge_person_birthplace(self):
        expected = """mutation {
  MergePersonBirthPlace(
    from: {identifier: "personid"}
    to: {identifier: "placeid"}
  ) {
    from {
      identifier
    }
    to {
      identifier
    }
  }
}"""
        mutation = place.mutation_merge_person_birthplace('personid', 'placeid')
        assert mutation == expected

    def test_mutation_remove_person_birthplace(self):
        expected = """mutation {
  RemovePersonBirthPlace(
    from: {identifier: "personid"}
    to: {identifier: "placeid"}
  ) {
    from {
      identifier
    }
    to {
      identifier
    }
  }
}"""
        mutation = place.mutation_remove_person_birthplace('personid', 'placeid')
        assert mutation == expected

    def test_mutation_merge_person_deathplace(self):
        expected = """mutation {
  MergePersonDeathPlace(
    from: {identifier: "personid"}
    to: {identifier: "placeid"}
  ) {
    from {
      identifier
    }
    to {
      identifier
    }
  }
}"""
        mutation = place.mutation_merge_person_deathplace('personid', 'placeid')
        assert mutation == expected

    def test_mutation_remove_person_deathplace(self):
        expected = """mutation {
  RemovePersonDeathPlace(
    from: {identifier: "personid"}
    to: {identifier: "placeid"}
  ) {
    from {
      identifier
    }
    to {
      identifier
    }
  }
}"""
        mutation = place.mutation_remove_person_deathplace('personid', 'placeid')
        assert mutation == expected
