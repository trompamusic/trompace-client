# Tests for mutations pertaining to digital document objects.
import os
import unittest

from connection import submit_query
from mutations.document import mutation_create_document, mutation_update_document, mutation_delete_document, \
    mutation_add_broad_match_document, mutation_remove_broad_match_document, \
    mutation_add_digital_document_subject_of_composition, mutation_remove_digital_document_subject_of_composition
from tests import util


class TestDocument(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "document")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT.txt")

        created_document = mutation_create_document("A Document", "https://www.cpdl.org", "https://www.cpdl.org",
                                                    "https://www.cpdl.org/A_Document", "https://www.upf.edu",
                                                    "This is a document", "Document", "en")
        self.assertEqual(created_document, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_UPDATE.txt")

        created_update = mutation_update_document('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                  publisher="Https://www.cpdl.org")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_DELETE.txt")

        created_delete = mutation_delete_document('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_add_broad_match(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_BROAD_MATCH.txt")

        created_match = mutation_add_broad_match_document("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                          "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_broad_match(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_REMOVE_BROAD_MATCH.txt")

        created_match = mutation_remove_broad_match_document("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                             "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_add_subject(self):
        expected = util.read_file(self.data_dir, "EXPECTED_DOCUMENT_SUBJECT_COMPOSITION.txt")

        created_match = mutation_add_digital_document_subject_of_composition("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                                             "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_subject(self):
        expected = util.read_file(self.data_dir, "EXPECTED_REMOVE_DOCUMENT_SUBJECT_COMPOSITION.txt")

        created_match = mutation_remove_digital_document_subject_of_composition("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                                                "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_query(self):
        created_document = mutation_create_document("A Document", "https://www.cpdl.org", "https://www.cpdl.org",
                                                    "https://www.cpdl.org/A_Document", "https://www.upf.edu",
                                                    "This is a document", "Document", "en")
        query_output = submit_query(created_document)
        self.assertEqual(query_output['data']['CreateDigitalDocument']['name'], "A Document")
        created_update = mutation_update_document(query_output['data']['CreateDigitalDocument']['identifier'],
                                                  publisher="Https://www.cpdl.org")
        query_output_update = submit_query(created_update)
        self.assertEqual(query_output_update['data']['UpdateDigitalDocument']['identifier'],
                         query_output['data']['CreateDigitalDocument']['identifier'])
        created_delete = mutation_delete_document(query_output['data']['CreateDigitalDocument']['identifier'])
        query_output_delete = submit_query(created_delete)
        self.assertEqual(query_output_delete['data']['DeleteDigitalDocument']['identifier'],
                         query_output['data']['CreateDigitalDocument']['identifier'])
