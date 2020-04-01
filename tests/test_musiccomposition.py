# Tests for mutations pertaining to music composition objects.
import os
import unittest

from trompace.mutations import musiccomposition
from tests import util


class TestDocument(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "musiccomposition")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION.txt")

        created_musiccomposition = musiccomposition.mutation_create_music_composition(title="A Document", contributor="https://www.cpdl.org", creator="https://www.cpdl.org/A_Document",
                                                    source= "https://www.cpdl.org/wiki/index.php/A._J._Fynn""https://www.cpdl.org/A_Document", subject="subject",
                                                    language="en", inLanguage="en", name="A Document")
        self.assertEqual(created_musiccomposition, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION_UPDATE.txt")

        created_update = musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                  name="No Document")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION_DELETE.txt")

        created_delete = musiccomposition.mutation_delete_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_add_broad_match(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION_BROAD_MATCH.txt")

        created_match = musiccomposition.mutation_add_broad_match_music_composition("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                          "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_broad_match(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION_REMOVE_BROAD_MATCH.txt")

        created_match = musiccomposition.mutation_remove_broad_match_music_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396") 
        self.assertEqual(created_match, expected)


    def test_merge_exampleOf(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION_MERGE_EXAMPLEOF_COMPOSITION.txt")

        created_match = musiccomposition.mutation_merge_music_composition_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_exampleOf(self):
        expected = util.read_file(self.data_dir, "EXPECTED_MUSICCOMPOSITION_REMOVE_EXAMPLEOF_COMPOSITION.txt")

        created_match = musiccomposition.mutation_remove_music_composition_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
