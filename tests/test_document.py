# Tests for mutations pertaining to digital document objects.
import os
import unittest

from trompace.mutations import document
from tests import util


class TestDocument(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "document")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT.txt")

        created_document = document.mutation_create_document("A Document", "https://www.cpdl.org", "https://www.cpdl.org",
                                                    "https://www.cpdl.org/A_Document", "https://www.upf.edu",
                                                    "This is a document", "Document", "en")
        self.assertEqual(created_document, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_UPDATE.txt")

        created_update = document.mutation_update_document('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                  publisher="Https://www.cpdl.org")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_DELETE.txt")

        created_delete = document.mutation_delete_document('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_add_broad_match(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_BROAD_MATCH.txt")

        created_match = document.mutation_add_broad_match_document("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                          "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_broad_match(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_REMOVE_BROAD_MATCH.txt")

        created_match = document.mutation_remove_broad_match_document(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_add_exampleOf(self):
        expected = util.read_file(self.data_dir, "expected_Document_add_exampleOf_Composition.txt")

        created_match = document.mutation_add_digital_document_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_merge_exampleOf(self):
        expected = util.read_file(self.data_dir, "expected_Document_merge_exampleOf_Composition.txt")

        created_match = document.mutation_merge_digital_document_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_exampleOf(self):
        expected = util.read_file(self.data_dir, "expected_Document_remove_exampleOf_Composition.txt")

        created_match = document.mutation_remove_digital_document_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
