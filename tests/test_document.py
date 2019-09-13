# Tests for mutations pertaining to digital document objects.

import mutations
from mutations.document import mutation_create_document, mutation_update_document, mutation_delete_document, mutation_add_broad_match_document, mutation_remove_broad_match_document, mutation_add_digital_document_subject_of_composition, mutation_remove_digital_document_subject_of_composition
from connection import submit_query

import unittest

with open("./tests/EXPECTED_DOCUMENT.txt", "r") as txt_file:
    EXPECTED_DOCUMENT = txt_file.read()
with open("./tests/EXPECTED_DOCUMENT_UPDATE.txt", "r") as txt_file:
    EXPECTED_UPDATE = txt_file.read()
with open("./tests/EXPECTED_DOCUMENT_DELETE.txt", "r") as txt_file:
    EXPECTED_DELETE = txt_file.read()
with open("./tests/EXPECTED_DOCUMENT_BROAD_MATCH.txt", "r") as txt_file:
    EXPECTED_DOCUMENT_BROAD_MATCH = txt_file.read()
with open("./tests/EXPECTED_DOCUMENT_REMOVE_BROAD_MATCH.txt", "r") as txt_file:
    EXPECTED_DOCUMENT_REMOVE_BROAD_MATCH = txt_file.read()
with open("./tests/EXPECTED_DOCUMENT_SUBJECT_COMPOSITION.txt", "r") as txt_file:
    EXPECTED_DOCUMENT_SUBJECT_COMPOSITION = txt_file.read()
with open("./tests/EXPECTED_REMOVE_DOCUMENT_SUBJECT_COMPOSITION.txt", "r") as txt_file:
    EXPECTED_REMOVE_DOCUMENT_SUBJECT_COMPOSITION = txt_file.read()

class TestDocument(unittest.TestCase):

    def test_create(self):
        created_document = mutation_create_document("A Document", "https://www.cpdl.org", "https://www.cpdl.org", "https://www.cpdl.org/A_Document", "https://www.upf.edu", "This is a document", "Document", "en")
        self.assertEqual(created_document, EXPECTED_DOCUMENT)

    def test_update(self):
        created_update = mutation_update_document('2eeca6dd-c62c-490e-beb0-2e3899fca74f',publisher="Https://www.cpdl.org")
        self.assertEqual(created_update, EXPECTED_UPDATE)

    def test_delete(self):
        created_delete = mutation_delete_document('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, EXPECTED_DELETE)

    def test_add_broad_match(self):
        created_match = mutation_add_broad_match_document("ff562d2e-2265-4f61-b340-561c92e797e9", "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, EXPECTED_DOCUMENT_BROAD_MATCH)

    def test_remove_broad_match(self):
        created_match = mutation_remove_broad_match_document("ff562d2e-2265-4f61-b340-561c92e797e9", "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, EXPECTED_DOCUMENT_REMOVE_BROAD_MATCH)

    def test_add_subject(self):
        created_match = mutation_add_digital_document_subject_of_composition("ff562d2e-2265-4f61-b340-561c92e797e9", "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, EXPECTED_DOCUMENT_SUBJECT_COMPOSITION)

    def test_remove_subject(self):
        created_match = mutation_remove_digital_document_subject_of_composition("ff562d2e-2265-4f61-b340-561c92e797e9", "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, EXPECTED_REMOVE_DOCUMENT_SUBJECT_COMPOSITION)
        

    def test_query(self):
        created_document = mutation_create_document("A Document", "https://www.cpdl.org", "https://www.cpdl.org", "https://www.cpdl.org/A_Document", "https://www.upf.edu", "This is a document", "Document", "en")
        query_output = submit_query(created_document)
        self.assertEqual(query_output['data']['CreateDigitalDocument']['name'], "A Document")
        created_update = mutation_update_document(query_output['data']['CreateDigitalDocument']['identifier'], publisher="Https://www.cpdl.org")
        query_output_update = submit_query(created_update)
        self.assertEqual(query_output_update['data']['UpdateDigitalDocument']['identifier'], query_output['data']['CreateDigitalDocument']['identifier'])
        created_delete = mutation_delete_document(query_output['data']['CreateDigitalDocument']['identifier'])
        query_output_delete = submit_query(created_delete)
        self.assertEqual(query_output_delete['data']['DeleteDigitalDocument']['identifier'], query_output['data']['CreateDigitalDocument']['identifier'])


if __name__ == '__main__':
    unittest.main()