import os

from tests import CeTestCase
from trompace.mutations import musicgroup


class TestMusicGroup(CeTestCase):
    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "musicgroup")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_musicgroup.txt"))

        create_musicgroup = musicgroup.mutation_create_musicgroup(
            title="Queen - MusicBrainz",
            contributor="https://musicbrainz.org",
            creator="https://github.com/trompamusic/trompa-ce-client/tree/v0.1/demo",
            source="https://musicbrainz.org/artist/0383dadf-2a4e-4d10-a46a-e9e041da8eb3",
            format_="text/html",
            language="en",
            name="Queen",
            founding_date="1970-06-27"
        )
        self.assert_queries_equal(create_musicgroup, expected)

    def test_update(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_musicgroup.txt"))

        update_musicgroup = musicgroup.mutation_update_musicgroup(
            identifier="457c6b78-3c58-44d0-b789-3373ea22304a",
            title="Not Queen - MusicBrainz",
        )
        self.assert_queries_equal(update_musicgroup, expected)

    def test_delete(self):
        expected = self.read_file(os.path.join(self.data_dir, "delete_musicgroup.txt"))
        delete_musicgroup = musicgroup.mutation_delete_musicgroup(identifier="457c6b78-3c58-44d0-b789-3373ea22304a")
        self.assert_queries_equal(delete_musicgroup, expected)

    def test_add_exact_match_musicgroup(self):
        expected = self.read_file(os.path.join(self.data_dir, "add_exact_match_musicgroup.txt"))
        exactmatch = musicgroup.mutation_musicgroup_add_exact_match_musicgroup(
            identifier_from="457c6b78-3c58-44d0-b789-3373ea22304a",
            identifier_to="fdf1e9e8-4f5b-40ab-81e7-521ea66d0aa6"
        )
        self.assert_queries_equal(exactmatch, expected)

    def test_remove_exact_match_musicgroup(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_exact_match_musicgroup.txt"))
        exactmatch = musicgroup.mutation_musicgroup_remove_exact_match_musicgroup(
            identifier_from="457c6b78-3c58-44d0-b789-3373ea22304a",
            identifier_to="fdf1e9e8-4f5b-40ab-81e7-521ea66d0aa6"
        )
        self.assert_queries_equal(exactmatch, expected)