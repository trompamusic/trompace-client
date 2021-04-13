import os

from trompace.mutations import definedterm
from tests import CeTestCase
from trompace.mutations.annotation import ADDITIONAL_TYPE_TAG_COLLECTION, ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT, \
    AnnotationSchemaMotivation


class TestDefinedTerm(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "definedterm")

    def test_create_defined_term_set(self):
        expected = self.read_file("create_definedtermset.txt")

        create_dts = definedterm.create_defined_term_set(
            creator="https://trompamusic.eu/user/mozart",
            name="Bowing direction",
            additionaltype=[ADDITIONAL_TYPE_TAG_COLLECTION])
        self.assert_queries_equal(create_dts, expected)

    def test_create_defined_term(self):
        expected = self.read_file("create_definedterm.txt")

        create_dt = definedterm.create_defined_term(
            creator="https://trompamusic.eu/user/mozart",
            termcode="up",
            additionaltype=[ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT])
        self.assert_queries_equal(create_dt, expected)

    def test_create_defined_term_broader_url(self):
        expected = self.read_file("create_definedterm_broader_url.txt")

        create_dt = definedterm.create_defined_term(
            creator="https://trompamusic.eu/user/mozart",
            termcode="up",
            additionaltype=[ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
            broader_url="http://some_url/motivation")
        self.assert_queries_equal(create_dt, expected)

    def test_create_defined_term_broader_schema(self):
        expected = self.read_file("create_definedterm_broader_schema.txt")

        create_dt = definedterm.create_defined_term(
            creator="https://trompamusic.eu/user/mozart",
            termcode="up",
            additionaltype=[ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
            broader_schema=AnnotationSchemaMotivation.commenting
        )
        self.assert_queries_equal(create_dt, expected)

    def test_defined_term_add_to_defined_term_set(self):
        expected = self.read_file("definedterm_addto_definedtermset.txt")

        add = definedterm.defined_term_add_to_defined_term_set(
            defined_term_set="f65d0bce-061a-4a6f-baa0-f8c3a292cc41",
            defined_term="5bd8a1c8-4e9e-4640-ae4b-134680af9acf")
        self.assert_queries_equal(add, expected)

    def test_update_defined_term_set(self):
        expected = self.read_file("update_definedtermset.txt")

        update_dts = definedterm.update_defined_term_set("f65d0bce-061a-4a6f-baa0-f8c3a292cc41",
                                                         name="Bowing direction")
        self.assert_queries_equal(update_dts, expected)

    def test_update_defined_term(self):
        expected = self.read_file("update_definedterm.txt")

        update_dts = definedterm.update_defined_term("07e8458f-7597-4a67-80bd-06035d01456f",
                                                     termcode="down")
        self.assert_queries_equal(update_dts, expected)

    def test_delete_defined_term_set(self):
        expected = self.read_file("delete_definedtermset.txt")

        delete_dts = definedterm.delete_defined_term_set("f65d0bce-061a-4a6f-baa0-f8c3a292cc41")
        self.assert_queries_equal(delete_dts, expected)

    def test_delete_defined_term(self):
        expected = self.read_file("delete_definedterm.txt")

        delete_dt = definedterm.delete_defined_term("5bd8a1c8-4e9e-4640-ae4b-134680af9acf")
        self.assert_queries_equal(delete_dt, expected)
