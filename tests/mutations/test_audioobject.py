import os

import pytest

from tests import CeTestCase
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations import audioobject


class TestAudioObject(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "audioobject")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_audioobject.txt"))

        created_audioobject = audioobject.mutation_create_audioobject(
            title="Rossinyol - webpage", name="Rossinyol", description="Traditional choir piece",
            date="1972", creator="trompamusic.eu",
            contributor="www.upf.edu", format_="text/html", encodingformat="audio/mpeg",
            source="https://www.cpdl.org/wiki/index.php/Rossinyol",
            contenturl="https://example.com/audio/rossinyol.mp3",
            embedurl="https://example.com/embed/rossinyol",
            language="en", inlanguage="ca"
        )
        self.assert_queries_equal(created_audioobject, expected)
