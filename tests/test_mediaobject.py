# Tests for mutations pertaining to music composition objects.
import os
import unittest

from trompace.mutations import mediaobject
from tests import util


class TestDocument(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "mediaobject")

    def test_create(self):
        expected = util.read_file(self.data_dir, "create_mediaobject.txt")

        created_mediaobject = mediaobject.mutation_create_media_object(name="Rossinyol", description="Traditional choir piece", date="1972", creator="trompamusic.eu",\
        contributor="www.upf.edu", format_="text/html", encodingFormat="text/html", source="https://www.cpdl.org/wiki/index.php/Rossinyol", subject="Catalan choir piece", \
        contentUrl="https://www.cpdl.org/wiki/index.php/Rossinyol", language="en")
        self.assertEqual(created_mediaobject, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "update_mediaobject.txt")

        created_update = musiccomposition.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                  name="No Document")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "delete_mediaobject.txt")

        created_delete = musiccomposition.mutation_delete_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_add_broad_match(self):
        expected = util.read_file(self.data_dir, "merge_work_example.txt")

        created_match = musiccomposition.mutation_merge_media_object_work_example("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                          "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_broad_match(self):
        expected = util.read_file(self.data_dir, "remove_work_example.txt")

        created_match = musiccomposition.mutation_remove_media_object_work_example(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396") 
        self.assertEqual(created_match, expected)


    def test_merge_exampleOf(self):
        expected = util.read_file(self.data_dir, "merge_object_encoding.txt")

        created_match = musiccomposition.mutation_merge_media_object_encoding(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_exampleOf(self):
        expected = util.read_file(self.data_dir, "remove_object_encoding.txt")

        created_match = musiccomposition.mutation_remove_media_object_encoding(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
