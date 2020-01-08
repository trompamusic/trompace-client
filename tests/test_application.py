# Tests for mutations pertaining to software applications.
import os
import unittest

from tests import util
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application


class TestApplication(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "application")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_APPLICATION.txt")

        created_application = mutation_create_application("Verovio MusicXML Converter",
                                                          contributor="https://www.verovio.org",
                                                          creator="Verovio",
                                                          source="https://github.com/rism-ch/verovio",
                                                          subject="Music notation engraving library for MEI with MusicXML,Humdrum support, toolkits, JavaScript, Python",
                                                          description="Verovio supports conversion from MusicXML to MEI. When converting from this web interface, the resulting MEI data will be displayed directly in the MEI-Viewer. The MEI file can be saved through the MEI  button that will be displayed on the top right.",
                                                          language="en")
        self.assertEqual(created_application, expected)

    def test_add_entrypoint_application(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ADD_ENTRYPOINT_APPLICATION.txt")

        created_add_entrypoint = mutation_add_entrypoint_application('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                                     '59ce8093-5e0e-4d59-bfa6-805edb11e396')
        self.assertEqual(created_add_entrypoint, expected)
