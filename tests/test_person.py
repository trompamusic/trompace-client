# Tests for mutations pertaining to person/artists objects.
import os
import unittest

from connection import submit_query
from mutations.person import mutation_create_artist, mutation_update_artist, mutation_delete_artist
from tests import util


class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "person")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ARTIST.txt")

        created_artist = mutation_create_artist("A. J. Fynn", "https://www.cpdl.org", "https://www.cpdl.org",
                                                "https://www.upf.edu", "https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                                                "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \u201cWhere The Columbines Grow\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn.",
                                                "en")
        self.assertEqual(created_artist, expected)

    def test_create_additional(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ARTIST_ADDITIONAL.txt")

        created_artist = mutation_create_artist("A. J. Fynn", "https://www.cpdl.org", "https://www.cpdl.org",
                                                "https://www.upf.edu", "https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                                                "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \u201cWhere The Columbines Grow\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn.",
                                                "en", birthDate="1860", deathDate="1920",
                                                url="https://en.wikipedia.org/wiki/A._J._Fynn")
        self.assertEqual(created_artist, expected)

    def test_update(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ARTIST_UPDATE.txt")

        created_update = mutation_update_artist('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                publisher="Https://www.cpdl.org")
        self.assertEqual(created_update, expected)

    def test_delete(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ARTIST_DELETE.txt")

        created_delete = mutation_delete_artist('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        self.assertEqual(created_delete, expected)

    def test_query(self):
        created_artist = mutation_create_artist("A. J. Fynn", "https://www.cpdl.org", "https://www.cpdl.org",
                                                "https://www.upf.edu", "https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                                                "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \u201cWhere The Columbines Grow\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn.",
                                                "en")
        query_output = submit_query(created_artist)
        self.assertEqual(query_output['data']['CreatePerson']['name'], "A. J. Fynn")
        created_update = mutation_update_artist(query_output['data']['CreatePerson']['identifier'],
                                                publisher="Https://www.cpdl.org")
        query_output_update = submit_query(created_update)
        self.assertEqual(query_output_update['data']['UpdatePerson']['identifier'],
                         query_output['data']['CreatePerson']['identifier'])
        created_delete = mutation_delete_artist(query_output['data']['CreatePerson']['identifier'])
        query_output_delete = submit_query(created_delete)
        self.assertEqual(query_output_delete['data']['DeletePerson']['identifier'],
                         query_output['data']['CreatePerson']['identifier'])
