# Tests for mutations pertaining to music composition objects.
import os

from tests import CeTestCase
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations import mediaobject


class TestDocument(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "mediaobject")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_mediaobject.txt"))

        created_mediaobject = mediaobject.mutation_create_media_object(name="Rossinyol", description="Traditional choir piece", date="1972", creator="trompamusic.eu", \
                                                                       contributor="www.upf.edu", format_="text/html", encodingformat="text/html", source="https://www.cpdl.org/wiki/index.php/Rossinyol", subject="Catalan choir piece", \
                                                                       contenturl="https://www.cpdl.org/wiki/index.php/Rossinyol", language="en", inlanguage="ca")
        self.assertEqual(created_mediaobject, expected)

    def test_update_name(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_mediaobject_name.txt"))

        created_update = mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                  name="Rossinyol")
        self.assertEqual(created_update, expected)

    def test_update_all(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_mediaobject_all.txt"))

        created_update = mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f', name="Rossinyol", description="Traditional choir piece", \
                                                                  date="1972", creator="trompamusic.eu", contributor="www.upf.edu", format_="text/html", encodingformat="text/html", \
                                                                  source="https://www.cpdl.org/wiki/index.php/Rossinyol", subject="Catalan choir piece", contenturl="https://www.cpdl.org/wiki/index.php/Rossinyol", language="en")
        print(created_update)
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = self.read_file(os.path.join(self.data_dir, "delete_mediaobject.txt"))

        created_delete = mediaobject.mutation_delete_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        print(created_delete)
        self.assertEqual(created_delete, expected)

    def test_add_broad_match(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_work_example.txt"))

        created_match = mediaobject.mutation_merge_media_object_work_example("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                          "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_broad_match(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_work_example.txt"))

        created_match = mediaobject.mutation_remove_media_object_work_example(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_invalid_language(self):
        with self.assertRaises(UnsupportedLanguageException):
            mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f',language="ja")
        with self.assertRaises(UnsupportedLanguageException):
            mediaobject.mutation_create_media_object(name="Rossinyol", description="Traditional choir piece", date="1972", creator="trompamusic.eu", \
                                                     contributor="www.upf.edu", format_="text/html", encodingformat="text/html", source="https://www.cpdl.org/wiki/index.php/Rossinyol", subject="Catalan choir piece", \
                                                     contenturl="https://www.cpdl.org/wiki/index.php/Rossinyol", language="ja", inlanguage="ca")


    def test_invalid_format(self):
        with self.assertRaises(NotAMimeTypeException):
            mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f',format_="test,html")
        with self.assertRaises(NotAMimeTypeException):
            mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f', encodingformat="test,html")
        with self.assertRaises(NotAMimeTypeException):
            mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f', name="Rossinyol", description="Traditional choir piece", \
                                                     date="1972", creator="trompamusic.eu", contributor="www.upf.edu", format_="text,html", encodingformat="text/html", \
                                                     source="https://www.cpdl.org/wiki/index.php/Rossinyol", subject="Catalan choir piece", contenturl="https://www.cpdl.org/wiki/index.php/Rossinyol", \
                                                     language="en", inlanguage="ca")
        with self.assertRaises(NotAMimeTypeException):
            mediaobject.mutation_update_media_object('2eeca6dd-c62c-490e-beb0-2e3899fca74f', name="Rossinyol", description="Traditional choir piece", \
                                                     date="1972", creator="trompamusic.eu", contributor="www.upf.edu", format_="text/html", encodingformat="text,html", \
                                                     source="https://www.cpdl.org/wiki/index.php/Rossinyol", subject="Catalan choir piece", contenturl="https://www.cpdl.org/wiki/index.php/Rossinyol", language="en", \
                                                     inlanguage="ca")

    def test_merge_exampleOf(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_object_encoding.txt"))

        created_match = mediaobject.mutation_merge_media_object_encoding(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)

    def test_remove_exampleOf(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_object_encoding.txt"))

        created_match = mediaobject.mutation_remove_media_object_encoding(
            "ff562d2e-2265-4f61-b340-561c92e797e9",
            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
