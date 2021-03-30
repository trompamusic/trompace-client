# Tests for mutations pertaining to software applications.
import os

from tests import CeTestCase
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application


class TestApplication(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "application")

    def test_create(self):
        expected = self.read_file(os.path.join(self.data_dir, "create_softwareapplication.txt"))

        created_application = mutation_create_application(name="Verovio MusicXML Converter",
                                                          contributor="https://www.verovio.org",
                                                          creator="Verovio",
                                                          source="https://github.com/rism-ch/verovio",
                                                          subject="Music notation engraving library for MEI with MusicXML,Humdrum support, toolkits, JavaScript, Python",
                                                          description="Verovio supports conversion from MusicXML to MEI. When converting from this web interface, the resulting MEI data will be displayed directly in the MEI-Viewer. The MEI file can be saved through the MEI  button that will be displayed on the top right.",
                                                          language="en")
        self.assert_queries_equal(created_application, expected)

    def test_add_entrypoint_application(self):
        expected = self.read_file(os.path.join(self.data_dir, "add_endtrypoint_application.txt"))

        created_add_entrypoint = mutation_add_entrypoint_application('2eeca6dd-c62c-490e-beb0-2e3899fca74f',
                                                                     '59ce8093-5e0e-4d59-bfa6-805edb11e396')
        self.assert_queries_equal(created_add_entrypoint, expected)
