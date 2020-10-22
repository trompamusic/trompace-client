import os

from freezegun import freeze_time

from trompace.mutations import definedterm
from tests import CeTestCase


class TestDefinedTerm(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "definedterm")

    @freeze_time("2020-04-09T10:57:55")
    def test_create_defined_term_set(self):
        expected = self.read_file("create_definedtermset.txt")

        create_dts = definedterm.create_defined_term_set(
            creator="https://trompamusic.eu/user/mozart",
            name="Bowing direction",
            additionaltype="https://vocab.trompamusic.eu/vocab#TagCollection")
        assert create_dts == expected

    @freeze_time("2020-04-09T10:57:55")
    def test_create_defined_term(self):
        expected = self.read_file("create_definedterm.txt")

        create_dt = definedterm.create_defined_term(
            creator="https://trompamusic.eu/user/mozart",
            termcode="up",
            additionaltype="https://vocab.trompamusic.eu/vocab#TagCollectionElement")
        assert create_dt == expected

    def test_defined_term_add_to_defined_term_set(self):
        expected = self.read_file("definedterm_addto_definedtermset.txt")

        add = definedterm.defined_term_add_to_defined_term_set(
            defined_term_set="f65d0bce-061a-4a6f-baa0-f8c3a292cc41",
            defined_term="5bd8a1c8-4e9e-4640-ae4b-134680af9acf")
        assert add == expected

    @freeze_time("2020-03-24T20:11:20")
    def test_update_defined_term_set(self):
        expected = self.read_file("update_definedtermset.txt")

        update_dts = definedterm.update_defined_term_set("f65d0bce-061a-4a6f-baa0-f8c3a292cc41",
                                                         name="Bowing direction")
        assert update_dts == expected

    @freeze_time("2020-04-04T15:31:04+00:00")
    def test_update_defined_term(self):
        expected = self.read_file("update_definedterm.txt")

        update_dts = definedterm.update_defined_term("07e8458f-7597-4a67-80bd-06035d01456f",
                                                     termcode="down")
        assert update_dts == expected

    def test_delete_defined_term_set(self):
        expected = self.read_file("delete_definedtermset.txt")

        delete_dts = definedterm.delete_defined_term_set("f65d0bce-061a-4a6f-baa0-f8c3a292cc41")
        assert delete_dts == expected

    def test_delete_defined_term(self):
        expected = self.read_file("delete_definedterm.txt")

        delete_dt = definedterm.delete_defined_term("5bd8a1c8-4e9e-4640-ae4b-134680af9acf")
        assert delete_dt == expected
