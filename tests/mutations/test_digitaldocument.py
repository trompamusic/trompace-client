# Tests for mutations pertaining to digital document objects.
import os

from trompace.mutations import digitaldocument
from tests import CeTestCase


class TestDigitalDocument(CeTestCase):

    def setUp(self) -> None:
        self.maxDiff = None
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "document")

    def test_create(self):
        """
         title: str = None, contributor: str = None,
                                    creator: str = None, source: str = None, format_: str = None,
                                    subject: str = None, language: str = None, description: str = None
        """
        expected = self.read_file(os.path.join(self.data_dir, "create_digitaldocument.txt"))

        created_document = digitaldocument.mutation_create_digitaldocument(
            title="A Document", contributor="https://www.cpdl.org", creator="https://www.upf.edu",
            source="https://www.cpdl.org/A_Document", format_="text/html", subject="A document about a topic",
            language="en", description="This is a document")
        assert created_document == expected

    def test_update(self):
        expected = self.read_file(os.path.join(self.data_dir, "update_digitaldocument.txt"))

        created_update = digitaldocument.mutation_update_digitaldocument(
            '2eeca6dd-c62c-490e-beb0-2e3899fca74f',
            source="https://www.cpdl.org/A_Different_Document")
        assert created_update == expected

    def test_delete(self):
        expected = self.read_file(os.path.join(self.data_dir, "delete_digitaldocument.txt"))

        created_delete = digitaldocument.mutation_delete_digitaldocument('2eeca6dd-c62c-490e-beb0-2e3899fca74f')
        assert created_delete == expected
