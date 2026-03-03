import unittest
from row import Solution


class TestSingleRowKeyboard(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        keyboard = "abcdefghijklmnopqrstuvwxyz"
        word = "cba"
        self.assertEqual(self.solution.calculateTime(keyboard, word), 4)

    def test_example_2(self):
        keyboard = "pqrstuvwxyzabcdefghijklmno"
        word = "neetcode"
        self.assertEqual(self.solution.calculateTime(keyboard, word), 77)

    def test_single_character(self):
        keyboard = "abcdefghijklmnopqrstuvwxyz"
        word = "a"
        self.assertEqual(self.solution.calculateTime(keyboard, word), 0)

    def test_repeated_character(self):
        keyboard = "abcdefghijklmnopqrstuvwxyz"
        word = "aaaaa"
        self.assertEqual(self.solution.calculateTime(keyboard, word), 0)

    def test_reverse_keyboard(self):
        keyboard = "zyxwvutsrqponmlkjihgfedcba"
        word = "abc"
        # moves: 0 -> 25 -> 24 -> 23
        expected = 25 + 1 + 1
        self.assertEqual(self.solution.calculateTime(keyboard, word), expected)

    def test_random_layout(self):
        keyboard = "qwertyuiopasdfghjklzxcvbnm"
        word = "leetcode"
        result = self.solution.calculateTime(keyboard, word)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()