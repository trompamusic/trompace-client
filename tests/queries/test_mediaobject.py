# Tests for queries pertaining to music composition objects.
import os
from trompace.queries import mediaobject
from tests import CeTestCase


class TestDocument(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "mediaobject")

    def test_query(self):
        expected = self.read_file(os.path.join(self.data_dir, "query_mediaobject_parameter.txt"))
        created_mediaobject = mediaobject.query_mediaobject(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        self.assertEqual(created_mediaobject, expected)

    def test_query_all(self):
        expected = self.read_file(os.path.join(self.data_dir, "query_mediaobject.txt"))

        created_mediaobject = mediaobject.query_mediaobject()
        self.assertEqual(created_mediaobject, expected)
