# Tests for queries pertaining to music composition objects.
import os
import unittest
from trompace.queries import mediaobject
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from tests import util


class TestDocument(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "mediaobject")

    def test_query(self):
        expected = util.read_file(self.data_dir, "query_mediaobject_parameter.txt")
        created_mediaobject = mediaobject.query_mediaobject(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        self.assertEqual(created_mediaobject, expected)

    def test_query_all(self):
        expected = util.read_file(self.data_dir, "query_mediaobject.txt")

        created_mediaobject = mediaobject.query_mediaobject()
        self.assertEqual(created_mediaobject, expected)
