import os

from freezegun import freeze_time

from trompace.mutations import rating
from tests import CeTestCase


class TestRating(CeTestCase):

    def setUp(self) -> None:
        super()
        self.data_dir = os.path.join(self.test_directory, "data", "rating")

    @freeze_time("2020-04-09T10:57:55")
    def test_create_rating_basic(self):
        expected = self.read_file("create_rating_basic.txt")

        create_rating = rating.create_rating("https://trompamusic.eu/user/mozart", 5, 5)
        self.assertEqual(create_rating, expected)

    @freeze_time("2020-04-09T11:03:20")
    def test_create_rating_complete(self):
        expected = self.read_file("create_rating_complete.txt")

        create_rating = rating.create_rating("https://trompamusic.eu/user/beethoven", 4, 5, worstrating=1,
                                             additionaltype="https://vocab.trompamusic.eu/vocab#PerformanceFeedback")
        self.assertEqual(create_rating, expected)

    @freeze_time("2020-04-09T12:20:39")
    def test_update_rating_single(self):
        expected = self.read_file("update_rating_basic.txt")
        update_rating = rating.update_rating("60ab3727-5972-4785-867f-2d050b0acde0", ratingvalue=4)
        self.assertEqual(update_rating, expected)

    @freeze_time("2020-04-09T12:21:27")
    def test_update_rating_complete(self):
        expected = self.read_file("update_rating_complete.txt")
        update_rating = rating.update_rating("60ab3727-5972-4785-867f-2d050b0acde0",
                                             creator="https://trompamusic.eu/user/mahler",
                                             ratingvalue=7, bestrating=10, worstrating=1,
                                             additionaltype="https://vocab.trompamusic.eu/vocab#PerformanceFeedback")
        self.assertEqual(update_rating, expected)

    def test_delete_rating(self):
        expected = self.read_file("delete_rating.txt")
        delete_rating = rating.delete_rating("c9e0b0d0-d3b8-47c6-a4a4-4b9aa11969d1")

        self.assertEqual(delete_rating, expected)
