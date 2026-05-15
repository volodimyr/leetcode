import unittest
from shortest import WordDistance


class TestWordDistance(unittest.TestCase):

    def setUp(self):
        self.wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])

    def test_example_coding_practice(self):
        self.assertEqual(self.wd.shortest("coding", "practice"), 3)

    def test_example_makes_coding(self):
        self.assertEqual(self.wd.shortest("makes", "coding"), 1)

    def test_adjacent_words(self):
        wd = WordDistance(["a", "b"])
        self.assertEqual(wd.shortest("a", "b"), 1)

    def test_word_appears_multiple_times_picks_closest(self):
        # "makes" at indices 1 and 4; "perfect" at index 2 — closest pair is (1,2) = 1
        self.assertEqual(self.wd.shortest("makes", "perfect"), 1)

    def test_same_word_multiple_occurrences(self):
        # "makes" at 1 and 4; "practice" at 0 — closest is (1,0) = 1
        self.assertEqual(self.wd.shortest("makes", "practice"), 1)

    def test_two_element_array(self):
        wd = WordDistance(["hello", "world"])
        self.assertEqual(wd.shortest("hello", "world"), 1)

    def test_words_far_apart(self):
        wd = WordDistance(["x", "a", "a", "a", "y"])
        self.assertEqual(wd.shortest("x", "y"), 4)

    def test_multiple_queries_same_instance(self):
        wd = WordDistance(["a", "c", "b", "c", "a"])
        self.assertEqual(wd.shortest("a", "c"), 1)
        self.assertEqual(wd.shortest("a", "b"), 2)
        self.assertEqual(wd.shortest("b", "c"), 1)


if __name__ == "__main__":
    unittest.main()
