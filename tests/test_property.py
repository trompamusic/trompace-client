# Tests for mutations pertaining to properties.
import os
import unittest

from tests import util
from trompace.mutations import StringConstant
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, \
    mutation_add_controlaction_propertyvaluespecification


class TestProperty(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "property")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_PROPERTY.txt")

        created_property = mutation_create_property("MusicXML file", "targetFile",
                                                    "Select a MusicXML file to be converted.",
                                                    [StringConstant("DigitalDocument")])
        self.assertEqual(created_property, expected)

    def test_create_propertyvaluespecification(self):
        expected = util.read_file(self.data_dir, "EXPECTED_PROPERTYVALUESPECIFICATION.txt")

        created_propertyvaluespecification = mutation_create_propertyvaluespecification("Result name",
                                                                                        "What name would you like to give.",
                                                                                        "", 100, 4, False, "resultName",
                                                                                        "String", True)
        self.assertEqual(created_propertyvaluespecification, expected)

    def test_add_controlaction_propertyvaluespecification(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION.txt")

        created_match = mutation_add_controlaction_propertyvaluespecification("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                                              "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
