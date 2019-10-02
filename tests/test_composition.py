# Tests for mutations pertaining to musical compositions and works related objects.
import os
import unittest

from trompace.mutations.work import mutation_create_composition, mutation_update_composition, mutation_delete_composition, \
    mutation_add_composition_author, mutation_remove_composition_author
from tests import util


class TestComposition(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "composition")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_COMPOSITION.txt")

        created_composition = mutation_create_composition("A Musical Composition", "https://www.cpdl.org",
                                                          "https://www.cpdl.org", "https://www.cpdl.org/A_Composition",
                                                          "https://www.upf.edu", "This is a musical composition",
                                                          "Composition", "en")
        self.assertEqual(created_composition, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "EXPECTED_COMPOSITION_UPDATE.txt")

        created_update = mutation_update_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                     publisher="Https://www.cpdl.org")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "EXPECTED_COMPOSITION_DELETE.txt")

        created_delete = mutation_delete_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_add_composer(self):
        expected = util.read_file(self.data_dir, "EXPECTED_WORK_ADD_COMPOSER.txt")

        created_add_composer = mutation_add_composition_author('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                               '59ce8093-5e0e-4d59-bfa6-805edb11e396')
        self.assertEqual(created_add_composer, expected)

    def test_remove_composer(self):
        expected = util.read_file(self.data_dir, "EXPECTED_WORK_REMOVE_COMPOSER.txt")

        created_remove_composer = mutation_remove_composition_author('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                                     '59ce8093-5e0e-4d59-bfa6-805edb11e396')
        self.assertEqual(created_remove_composer, expected)
