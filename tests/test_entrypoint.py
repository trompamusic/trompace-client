# Tests for mutations pertaining to entry points.
import os
import unittest

from trompace.mutations.entrypoint import mutation_create_entry_point
from tests import util


class TestEntryPoint(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "entrypoint")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ENTRYPOINT.txt")

        created_entrypoint = mutation_create_entry_point("Verovio MusicXML Converter", "https://www.verovio.org", "Music notation engraving library for MEI with MusicXML,Humdrum support, toolkits, JavaScript, Python",
                                                "Verovio supports conversion from MusicXML to MEI. When converting from this web interface, the resulting MEI data will be displayed directly in the MEI-Viewer. The MEI file can be saved through the MEI  button that will be displayed on the top right.","Verovio", "https://github.com/rism-ch/verovio","en", "TROMPA algorithm proof of concept.", ["json"],["text"], identifier="ffb473fe-b345-4f10-8fee-424ef13f6686")
        self.assertEqual(created_entrypoint, expected)


