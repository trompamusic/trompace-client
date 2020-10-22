# Tests for mutations pertaining to control action objects.
import os

from trompace.constants import ActionStatusType
from trompace.mutations import controlaction
import trompace.exceptions
from tests import CeTestCase


class TestControlAction(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "controlaction")

    def test_create_controlaction(self):
        expected = self.read_file(os.path.join(self.data_dir, "controlaction.txt"))

        created_control_action = controlaction.mutation_create_controlaction("Verovio MusicXML Converter",
                                                               "MusicXML to MEI conversion")
        self.assertEqual(created_control_action, expected)

        expected = self.read_file(os.path.join(self.data_dir, "controlaction_active.txt"))
        created_control_action = controlaction.mutation_create_controlaction("Verovio MusicXML Converter",
                                                               "MusicXML to MEI conversion", ActionStatusType.ActiveActionStatus)
        self.assertEqual(created_control_action, expected)

    def test_create_controlaction_invalid_status(self):
        """An invalid status for the ControlAction raises an Exception"""
        with self.assertRaises(trompace.exceptions.InvalidActionStatusException):
            controlaction.mutation_create_controlaction("Verovio MusicXML Converter",
                                                        "MusicXML to MEI conversion", "NotAStatus")

    def test_update_controlaction(self):
        """Update a ControlAction to have a different actionStatus or error message"""

        expected = self.read_file(os.path.join(self.data_dir, "update_controlaction.txt"))
        ca = controlaction.mutation_modify_controlaction("93982f65-005d-4d69-9731-6079d2489598",
                                                         ActionStatusType.CompletedActionStatus)
        self.assertEqual(ca, expected)

        # Add an Error message
        expected = self.read_file(os.path.join(self.data_dir, "update_controlaction_error.txt"))
        ca = controlaction.mutation_modify_controlaction("93982f65-005d-4d69-9731-6079d2489598",
                                                         ActionStatusType.FailedActionStatus,
                                                         error="Failed to do a thing")
        self.assertEqual(ca, expected)

    def test_update_controlaction_invalid_status(self):
        """An invalid status for the ControlAction raises an Exception"""
        with self.assertRaises(trompace.exceptions.InvalidActionStatusException):
            controlaction.mutation_modify_controlaction("93982f65-005d-4d69-9731-6079d2489598",
                                                        "NotAStatus",
                                                        error="Failed to do a thing")

    def test_add_entrypoint_controlaction(self):
        expected = self.read_file(os.path.join(self.data_dir, "add_entrypoint_controlaction.txt"))

        created_match = controlaction.mutation_add_entrypoint_controlaction("ff562d2e-2265-4f61-b340-561c92e797e9",
                                                                            "59ce8093-5e0e-4d59-bfa6-805edb11e396")
        self.assertEqual(created_match, expected)
