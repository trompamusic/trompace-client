# Tests for mutations pertaining to music composition objects.
import os

import pytest

from trompace.mutations import musiccomposition
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from tests import CeTestCase


class TestMusicComposition(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "musiccomposition")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_musiccomposition.txt"))

        created_musiccomposition = musiccomposition.mutation_create_music_composition(
            title="Das Lied von der Erde", contributor="https://www.cpdl.org", creator="https://www.upf.edu",
            source="https://www.cpdl.org/Das_Lied_von_der_Erde", format_="text/html", subject="Music Composition",
            language="en", inlanguage="de", name="The Song of the Earth"
        )
        self.assert_queries_equal(created_musiccomposition, expected)

    def test_create_no_language(self):
        """A musiccomposition can be missing a language value, and this should generate a valid mutation"""
        musiccomposition.mutation_create_music_composition(
            title="Das Lied von der Erde", contributor="https://www.cpdl.org", creator="https://www.upf.edu",
            source="https://www.cpdl.org/Das_Lied_von_der_Erde", format_="text/html", subject="Music Composition",
            inlanguage="de", name="The Song of the Earth"
        )

    def test_create_all_arguments(self):
        created_musiccomposition = musiccomposition.mutation_create_music_composition(
            title="Das Lied von der Erde: I. Das Trinklied vom Jammer der Erde", contributor="https://musicbrainz.org",
            creator="https://www.upf.edu", source="https://musicbrainz.org/work/ff15c2ab-0775-3757-975a-331357299635",
            format_="text/html", subject="Music Composition",
            language="de", inlanguage="de", name="Das Lied von der Erde: I. Das Trinklied vom Jammer der Erde",
            description="First composition of a song-cycle by Mahler", position=1
        )

        expected = self.read_file(os.path.join(self.data_dir, "create_musiccomposition_complete.txt"))
        self.assert_queries_equal(created_musiccomposition, expected)

    def test_update_name(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_composition_name.txt"))

        created_update = musiccomposition.mutation_update_music_composition(
            identifier='2eeca6dd-c62c-490e-beb0-2e3899fca74f',
            name="The Song Of The Earth")
        self.assert_queries_equal(created_update, expected)

    def test_update_all(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_composition_all.txt"))

        created_update = musiccomposition.mutation_update_music_composition(
            identifier='2eeca6dd-c62c-490e-beb0-2e3899fca74f', title="Das Lied von der Erde",
            contributor="https://www.cpdl.org", creator="https://www.upf.edu",
            source="https://www.cpdl.org/Das_Lied_von_der_Erde", subject="Music Composition",
            language="en", inlanguage="en", name="The Song of the Earth", position=2)
        self.assert_queries_equal(created_update, expected)

    def test_invalid_language(self):
        with pytest.raises(UnsupportedLanguageException):
            musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f', language="ja")

    def test_invalid_format(self):
        with pytest.raises(NotAMimeTypeException):
            musiccomposition.mutation_update_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                               format_="test,html")

    def test_delete(self):
        expected = self.read_file(os.path.join(self.data_dir, "delete_musiccomposition.txt"))

        created_delete = musiccomposition.mutation_delete_music_composition('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assert_queries_equal(created_delete, expected)

    def test_merge_exampleOf(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_music_composition_work_example.txt"))

        created_match = musiccomposition.mutation_merge_music_composition_work_example(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assert_queries_equal(created_match, expected)

    def test_remove_exampleOf(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_music_composition_work_example.txt"))

        created_match = musiccomposition.mutation_remove_music_composition_work_example(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assert_queries_equal(created_match, expected)

    def test_merge_music_composition_included_composition(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_music_composition_included_composition.txt"))
        created = musiccomposition.mutation_merge_music_composition_included_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396"
        )
        self.assert_queries_equal(created, expected)

    def test_remove_music_composition_included_composition(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_music_composition_included_composition.txt"))
        created = musiccomposition.mutation_remove_music_composition_included_composition(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396"
        )
        self.assert_queries_equal(created, expected)

    def test_merge_music_composition_has_part(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_music_composition_has_part.txt"))
        created = musiccomposition.mutation_merge_music_composition_has_part(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396"
        )
        self.assert_queries_equal(created, expected)

    def test_remove_music_composition_has_part(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_music_composition_has_part.txt"))
        created = musiccomposition.mutation_remove_music_composition_has_part(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396"
        )
        self.assert_queries_equal(created, expected)

    def test_merge_music_composition_composer(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_music_composition_composer.txt"))
        created = musiccomposition.mutation_merge_music_composition_composer(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "cd79f87e-39f3-44bc-ae2f-b9854ab6df3b"
        )
        self.assert_queries_equal(created, expected)

    def test_remove_music_composition_composer(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_music_composition_composer.txt"))
        created = musiccomposition.mutation_remove_music_composition_composer(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "cd79f87e-39f3-44bc-ae2f-b9854ab6df3b"
        )
        self.assert_queries_equal(created, expected)

    def test_merge_music_composition_exact_match(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_music_composition_exact_match.txt"))
        created = musiccomposition.mutation_merge_music_composition_exact_match(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "ccd75459-db61-425f-b587-2dc96bf169df"
        )
        self.assert_queries_equal(created, expected)

    def test_remove_music_composition_exact_match(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_music_composition_exact_match.txt"))
        created = musiccomposition.mutation_remove_music_composition_exact_match(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "ccd75459-db61-425f-b587-2dc96bf169df"
        )
        self.assert_queries_equal(created, expected)
