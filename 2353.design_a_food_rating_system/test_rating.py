import unittest
from rating import FoodRatings


class TestFoodRatings(unittest.TestCase):

    def setUp(self):
        self.foodRatings = FoodRatings(
            foods=["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
            cuisines=["korean", "japanese", "japanese", "greek", "japanese", "korean"],
            rats=[9, 12, 8, 15, 14, 7]
        )

    def test_initial_highest_rated(self):
        self.assertEqual(self.foodRatings.highestRated("korean"), "kimchi")
        self.assertEqual(self.foodRatings.highestRated("japanese"), "ramen")
        self.assertEqual(self.foodRatings.highestRated("greek"), "moussaka")

    def test_change_rating_simple(self):
        self.foodRatings.changeRating("sushi", 16)
        self.assertEqual(self.foodRatings.highestRated("japanese"), "sushi")

    def test_lexicographical_tie_break(self):
        self.foodRatings.changeRating("sushi", 16)
        self.foodRatings.changeRating("ramen", 16)
        # ramen < sushi lexicographically
        self.assertEqual(self.foodRatings.highestRated("japanese"), "ramen")

    def test_multiple_updates_same_food(self):
        self.foodRatings.changeRating("ramen", 5)
        self.assertEqual(self.foodRatings.highestRated("japanese"), "miso")

        self.foodRatings.changeRating("ramen", 20)
        self.assertEqual(self.foodRatings.highestRated("japanese"), "ramen")

    def test_multiple_cuisines_independent(self):
        self.foodRatings.changeRating("bulgogi", 20)
        self.assertEqual(self.foodRatings.highestRated("korean"), "bulgogi")
        self.assertEqual(self.foodRatings.highestRated("japanese"), "ramen")

    def test_stale_entries_cleanup(self):
        # Many updates to same food to create stale heap entries
        for r in range(1, 10):
            self.foodRatings.changeRating("sushi", r)

        self.foodRatings.changeRating("ramen", 15)
        self.assertEqual(self.foodRatings.highestRated("japanese"), "ramen")


if __name__ == "__main__":
    unittest.main()
