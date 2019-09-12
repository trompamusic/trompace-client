import mutations
from mutations.person import mutation_create_artist, mutation_update_artist
from connection import submit_query

import unittest

class TestPerson(unittest.TestCase):

    def test_create(self):
        created_artist = mutation_create_artist("A. J. Fynn", "https://www.cpdl.org", "https://www.cpdl.org", "https://www.upf.edu", "https://www.cpdl.org/wiki/index.php/A._J._Fynn", "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \u201cWhere The Columbines Grow\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn.", "en")
        expected_artist = '\nmutation {\n  \nCreatePerson(\ntitle: "A. J. Fynn"\nname: "A. J. Fynn"\npublisher: "https://www.cpdl.org"\ncontributor: "https://www.cpdl.org"\ncreator: "https://www.upf.edu"\nsource: "https://www.cpdl.org/wiki/index.php/A._J._Fynn"\nsubject: "artist"\ndescription: "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \\u201cWhere The Columbines Grow\\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn."\nformat: "text/html"\nlanguage: en\n) {\n  identifier\n  name\n}\n\n}\n'
        self.assertEqual(created_artist, expected_artist)

    def test_update(self):
        created_update = mutation_update_artist('2eeca6dd-c62c-490e-beb0-2e3899fca74f',description = "Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar in literature and anthropology, specializing in the American West and Native American culture. His most notable musical composition was \u201cWhere The Columbines Grow\u201d, which was adopted as the official state song of the US State of Colorado in 1915.View the Wikipedia article on A. J. Fynn.")
        expected_update = '\nmutation {\n  \nUpdatePerson(\n  identifier: "2eeca6dd-c62c-490e-beb0-2e3899fca74f"\n) {\n  identifier\n  relation\n}\n\n}\n'
        self.assertEqual(created_update, expected_update)

if __name__ == '__main__':
    unittest.main()