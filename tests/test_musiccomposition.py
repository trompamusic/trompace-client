# Tests for mutations pertaining to music composition objects.
import os
import unittest

from trompace.mutations import musiccomposition
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from tests import util


class TestMusicComposition(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "musiccomposition")

    def test_create(self):
        expected = util.read_file(self.data_dir, "create_musiccomposition.txt")

        created_musiccomposition = musiccomposition.mutation_create_music_composition(title="Das Lied von der Erde", contributor="https://www.cpdl.org", creator="https://www.upf.edu",
                                                    source= "https://www.cpdl.org/Das_Lied_von_der_Erde", subject="Music Composition",
                                                    language="en", inLanguage="en", name="The Song of the Earth")
        self.assertEqual(created_musiccomposition, expected)

    def test_update_name(self):
        expected = util.read_file(self.data_dir, "update_composition_name.txt")

        created_update = musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                  name="The Song Of The Earth")
        self.assertEqual(created_update, expected)

    def test_update_all(self):
        expected = util.read_file(self.data_dir, "update_composition_all.txt")

        created_update = musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',title="Das Lied von der Erde", contributor="https://www.cpdl.org", creator="https://www.upf.edu",
                                                    source= "https://www.cpdl.org/Das_Lied_von_der_Erde", subject="Music Composition",
                                                    language="en", inLanguage="en", name="The Song of the Earth")
        print(created_update)
        self.assertEqual(created_update, expected)

    def test_invalid_language(self):
        with self.assertRaises(UnsupportedLanguageException):
            musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',language="ja")

    def test_invalid_format(self):
        with self.assertRaises(NotAMimeTypeException):
            musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',format_="test,html")

    def test_delete(self):
        expected = util.read_file(self.data_dir, "delete_musiccomposition.txt")

        created_delete = musiccomposition.mutation_delete_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_add_broad_match(self):
        expected = util.read_file(self.data_dir, "add_broad_match.txt")

        created_match = musiccomposition.mutation_add_broad_match_music_composition("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                          "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_broad_match(self):
        expected = util.read_file(self.data_dir, "remove_broad_match.txt")

        created_match = musiccomposition.mutation_remove_broad_match_music_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)


    def test_merge_exampleOf(self):
        expected = util.read_file(self.data_dir, "merge_example_of_work.txt")

        created_match = musiccomposition.mutation_merge_music_composition_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_exampleOf(self):
        expected = util.read_file(self.data_dir, "remove_example_of_work.txt")

        created_match = musiccomposition.mutation_remove_music_composition_work_example_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
