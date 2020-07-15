# Tests for queries pertaining to music composition objects.
import os
import unittest
from trompace.queries import musiccomposition
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from tests import util


class TestDocument(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "musiccomposition")

    def test_query(self):
        expected = util.read_file(self.data_dir, "query_musiccomposition_parameter.txt")
        created_musiccomposition = musiccomposition.query_musiccomposition(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        self.assertEqual(created_musiccomposition, expected)

    def test_query_all(self):
        expected = util.read_file(self.data_dir, "query_musiccomposition.txt")

        created_musiccomposition = musiccomposition.query_musiccomposition()
        self.assertEqual(created_musiccomposition, expected)
