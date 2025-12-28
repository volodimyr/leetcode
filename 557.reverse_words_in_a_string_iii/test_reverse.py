import unittest
from reverse import Solution


class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_sentence(self):
        self.assertEqual(
            self.solution.reverseWords("Let's take LeetCode contest"),
            "s'teL ekat edoCteeL tsetnoc"
        )

    def test_single_word(self):
        self.assertEqual(
            self.solution.reverseWords("hello"),
            "olleh"
        )

    def test_multiple_spaces(self):
        self.assertEqual(
            self.solution.reverseWords("hello   world"),
            "olleh dlrow"
        )

    def test_leading_trailing_spaces(self):
        self.assertEqual(
            self.solution.reverseWords("  hello world  "),
            "olleh dlrow"
        )

    def test_empty_string(self):
        self.assertEqual(
            self.solution.reverseWords(""),
            ""
        )

    def test_only_spaces(self):
        self.assertEqual(
            self.solution.reverseWords("     "),
            ""
        )

    def test_numbers_and_symbols(self):
        self.assertEqual(
            self.solution.reverseWords("abc123 !@#"),
            "321cba #@!"
        )


if __name__ == "__main__":
    unittest.main()
