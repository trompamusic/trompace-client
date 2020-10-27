# Tests for mutations pertaining to person objects.
import os

import pytest

from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException

from trompace.mutations import person
from tests import CeTestCase


class TestPerson(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "person")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_person.txt"))

        created_person = person.mutation_create_person(
            title="A. J. Fynn", contributor="https://www.cpdl.org",
            creator="https://www.upf.edu", source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
            language="en", format_="text/html", gender="male",
            description="Born circa 1860Died circa 1920A. J. Fynn was an early 20th Century scholar\
 in literature and anthropology")
        assert created_person == expected

    def test_create_invalid_values(self):
        """Passing invalid values to language, format_, or gender cause exceptions"""
        with pytest.raises(ValueError):
            person.mutation_create_person(
                title="A. J. Fynn", contributor="https://www.cpdl.org",
                creator="https://www.upf.edu",
                source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                format_="text/html",
                gender="test"
            )

        with pytest.raises(UnsupportedLanguageException):
            person.mutation_create_person(
                title="A. J. Fynn", contributor="https://www.cpdl.org",
                creator="https://www.upf.edu",
                source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                format_="text/html",
                language="pt"
            )

        with pytest.raises(NotAMimeTypeException):
            person.mutation_create_person(
                title="A. J. Fynn", contributor="https://www.cpdl.org",
                creator="https://www.upf.edu",
                source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                format_="html"
            )

    def test_update(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_person.txt"))

        created_update = person.mutation_update_person('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                       title="A. J. Fynn")
        assert created_update == expected

    def test_delete(self):
        expected = self.read_file(os.path.join(self.data_dir, "delete_person.txt"))

        created_delete = person.mutation_delete_person('2eeca6dd-c62c-490e-beb0-2e3899fca74f')

        assert created_delete == expected

    def test_invalid_language(self):
        with pytest.raises(UnsupportedLanguageException):
            person.mutation_update_person('2eeca6dd-c62c-490e-beb0-2e3899fca74f', language="ja")
        with pytest.raises(UnsupportedLanguageException):
            person.mutation_create_person(title="A. J. Fynn", contributor="https://www.cpdl.org",
                                        creator="https://www.upf.edu",
                                        source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                                        language="ja", format_="text/html",
                                        description="Born circa 1860Died circa 1920A. J. Fynn was\
                                        an early 20th Century scholar in literature and anthropology")

    def test_invalid_format(self):
        with pytest.raises(NotAMimeTypeException):
            person.mutation_update_person('2eeca6dd-c62c-490e-beb0-2e3899fca74f', format_="test,html")
        with pytest.raises(NotAMimeTypeException):
            person.mutation_create_person(title="A. J. Fynn", contributor="https://www.cpdl.org",
                                        creator="https://www.upf.edu",
                                        source="https://www.cpdl.org/wiki/index.php/A._J._Fynn",
                                        language="en", format_="text,html",
                                        description="Born circa 1860Died circa 1920A. J. Fynn was\
                                        an early 20th Century scholar in literature and anthropology")

    def test_person_add_exact_match_person(self):
        expected = self.read_file(os.path.join(self.data_dir, "merge_person_exactmatch.txt"))

        actual = person.mutation_person_add_exact_match_person("d3f968f4-90cd-4764-93bc-6fadcc2a35e6",
                                                               "b10ac895-beb8-489e-8168-3e786d1aeb0e")

        assert actual == expected

    def test_person_remove_exact_match_person(self):
        expected = self.read_file(os.path.join(self.data_dir, "remove_person_exactmatch.txt"))

        actual = person.mutation_person_remove_exact_match_person("d3f968f4-90cd-4764-93bc-6fadcc2a35e6",
                                                                  "b10ac895-beb8-489e-8168-3e786d1aeb0e")

        assert actual == expected
