# Tests for mutations pertaining to musical compositions and works related objects.

import mutations
from mutations.work import mutation_create_composition, mutation_update_composition, mutation_delete_composition, mutation_add_composition_author, mutation_remove_composition_author
from connection import submit_query

import unittest

with open("./tests/EXPECTED_COMPOSITION.txt", "r") as txt_file:
    EXPECTED_COMPOSITION = txt_file.read()
with open("./tests/EXPECTED_COMPOSITION_UPDATE.txt", "r") as txt_file:
    EXPECTED_UPDATE = txt_file.read()
with open("./tests/EXPECTED_COMPOSITION_DELETE.txt", "r") as txt_file:
    EXPECTED_DELETE = txt_file.read()
with open("./tests/EXPECTED_WORK_ADD_COMPOSER.txt", "r") as txt_file:
    EXPECTED_WORK_ADD_COMPOSER = txt_file.read()
with open("./tests/EXPECTED_WORK_REMOVE_COMPOSER.txt", "r") as txt_file:
    EXPECTED_WORK_REMOVE_COMPOSER = txt_file.read()

class TestDocument(unittest.TestCase):

    def test_create(self):
        created_composition = mutation_create_composition("A Musical Composition", "https://www.cpdl.org", "https://www.cpdl.org", "https://www.cpdl.org/A_Composition", "https://www.upf.edu", "This is a musical composition", "Composition", "en")
        self.assertEqual(created_composition, EXPECTED_COMPOSITION)

    def test_update(self):
        created_update = mutation_update_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',publisher="Https://www.cpdl.org")
        self.assertEqual(created_update, EXPECTED_UPDATE)

    def test_delete(self):
        created_delete = mutation_delete_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, EXPECTED_DELETE)

    def test_add_composer(self):
        created_add_composer = mutation_add_composition_author('2eeca6dd-c62c-490e-beb0-2e3899fca74f', '59ce8093-5e0e-4d59-bfa6-805edb11e396')
        self.assertEqual(created_add_composer, EXPECTED_WORK_ADD_COMPOSER)

    def test_remove_composer(self):
        created_remove_composer = mutation_remove_composition_author('2eeca6dd-c62c-490e-beb0-2e3899fca74f', '59ce8093-5e0e-4d59-bfa6-805edb11e396')
        self.assertEqual(created_remove_composer, EXPECTED_WORK_REMOVE_COMPOSER)

    def test_query(self):
        created_composition = mutation_create_composition("A Musical Composition", "https://www.cpdl.org", "https://www.cpdl.org", "https://www.cpdl.org/A_Composition", "https://www.upf.edu", "This is a musical composition", "Composition", "en")
        query_output = submit_query(created_composition)
        self.assertEqual(query_output['data']['CreateMusicComposition']['name'], "A Musical Composition")
        created_update = mutation_update_composition(query_output['data']['CreateMusicComposition']['identifier'], publisher="Https://www.cpdl.org")
        query_output_update = submit_query(created_update)
        self.assertEqual(query_output_update['data']['UpdateMusicComposition']['identifier'], query_output['data']['CreateMusicComposition']['identifier'])
        created_delete = mutation_delete_composition(query_output['data']['CreateMusicComposition']['identifier'])
        query_output_delete = submit_query(created_delete)
        self.assertEqual(query_output_delete['data']['DeleteMusicComposition']['identifier'], query_output['data']['CreateMusicComposition']['identifier'])


if __name__ == '__main__':
    unittest.main()