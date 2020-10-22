# Tests for queries pertaining to music composition objects.
import os
import unittest

from tests import CeTestCase
from trompace.queries import musiccomposition


class TestDocument(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "musiccomposition")

    def test_query(self):
        expected = self.read_file(os.path.join(self.data_dir, "query_musiccomposition_parameter.txt"))
        created_musiccomposition = musiccomposition.query_musiccomposition(identifier="ff59650b-1d47-4ea5-b356-31fddeb48315")
        assert created_musiccomposition == expected

    def test_query_all(self):
        expected = self.read_file(os.path.join(self.data_dir, "query_musiccomposition.txt"))

        created_musiccomposition = musiccomposition.query_musiccomposition()
        assert created_musiccomposition == expected
