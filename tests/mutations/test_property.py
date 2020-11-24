# Tests for mutations pertaining to properties.
import os

from tests import CeTestCase
from trompace import StringConstant
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification


class TestProperty(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "property")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_propery.txt"))

        created_property = mutation_create_property("MusicXML file", "targetFile",
                                                    "Select a MusicXML file to be converted.",
                                                    [StringConstant("DigitalDocument")])

        assert self.compare_queries(created_property, expected)

    def test_create_propertyvaluespecification(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_propertyvaluespecification.txt"))

        created_propertyvaluespecification = mutation_create_propertyvaluespecification("Result name",
                                                                                        "What name would you like to give.",
                                                                                        "", 100, 4, False, "resultName",
                                                                                        "String", True)

        assert self.compare_queries(created_propertyvaluespecification, expected)


