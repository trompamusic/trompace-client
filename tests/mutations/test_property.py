# Tests for mutations pertaining to properties.
import os

from tests import CeTestCase
from trompace import StringConstant
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, \
    mutation_add_controlaction_propertyvaluespecification


class TestProperty(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "property")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_propery.txt"))

        created_property = mutation_create_property("MusicXML file", "targetFile",
                                                    "Select a MusicXML file to be converted.",
                                                    [StringConstant("DigitalDocument")])
        assert created_property == expected

    def test_create_propertyvaluespecification(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_propertyvaluespecification.txt"))

        created_propertyvaluespecification = mutation_create_propertyvaluespecification("Result name",
                                                                                        "What name would you like to give.",
                                                                                        "", 100, 4, False, "resultName",
                                                                                        "String", True)
        assert created_propertyvaluespecification == expected

    def test_add_controlaction_propertyvaluespecification(self):
        expected = self.read_file(os.path.join(self.data_dir, "add_controlaction_propertyvaluespecification.txt"))

        created_match = mutation_add_controlaction_propertyvaluespecification("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                                              "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        assert created_match == expected
