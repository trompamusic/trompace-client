# Tests for mutations pertaining to music recording objects.
import os

import pytest

from trompace.mutations import musicrecording
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from tests import CeTestCase


class TestMusicRecording(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "musicrecording")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_musicrecording.txt"))

        created_musiccomposition = musicrecording.mutation_create_musicrecording(
            name="Best of you",
            title="Muziekweb - de muziekbibliotheek van Nederland",
            description="Description of the MusicRecording",
            contributor="https://www.muziekweb.nl",
            creator="https://github.com/trompamusic/ce-data-import",
            source="https://www.muziekweb.nl/Embed/JK157518-0002",
            format_="text/html",
            encodingformat="text/html",
            subject="Best of you",
            language="en"
        )
        self.assert_queries_equal(created_musiccomposition, expected)

    def test_update(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_musicrecording.txt"))

        created_update = musicrecording.mutation_update_musicrecording(identifier='2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                                       title="Best of you - 2006 version")
        self.assert_queries_equal(created_update, expected)

    def test_delete(self):
        expected = self.read_file(os.path.join(self.data_dir, "delete_musicrecording.txt"))

        created_delete = musicrecording.mutation_delete_musicrecording('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assert_queries_equal(created_delete, expected)

    def test_merge_music_recording_audio(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_music_recording_audio.txt"))

        actual = musicrecording.mutation_merge_music_recording_audio("d3f968f4-90cd-4764-93bc-6fadcc2a35e6",
                                                                     "b10ac895-beb8-489e-8168-3e786d1aeb0e")

        self.assert_queries_equal(actual, expected)

    def test_remove_music_recording_audio(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_music_recording_audio.txt"))

        actual = musicrecording.mutation_remove_music_recording_audio("d3f968f4-90cd-4764-93bc-6fadcc2a35e6",
                                                                      "b10ac895-beb8-489e-8168-3e786d1aeb0e")

        self.assert_queries_equal(actual, expected)
