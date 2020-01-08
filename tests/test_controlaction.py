# Tests for mutations pertaining to control action objects.
import os
import unittest

from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from tests import util


class TestControlAction(unittest.TestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(os.path.dirname(__file__), "data", "controlaction")

    def test_create(self):
        expected = util.read_file(self.data_dir, "EXPECTED_CONTROLACTION.txt")

        created_control_action = mutation_create_controlaction("Verovio MusicXML Converter",
                                                               "MusicXML to MEI conversion", "accepted")
        self.assertEqual(created_control_action, expected)

    def test_add_entrypoint_controlaction(self):
        expected = util.read_file(self.data_dir, "EXPECTED_ADD_CONTROLACTION_ENTRYPOINT.txt")

        created_match = mutation_add_entrypoint_controlaction("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                              "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        print(created_match)
        self.assertEqual(created_match, expected)
