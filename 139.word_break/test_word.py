import unittest
from word import Solution


class TestWordBreak(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_single_character_true(self):
        s = "a"
        wordDict = ["a"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_single_character_false(self):
        s = "a"
        wordDict = ["b"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_reuse_word_multiple_times(self):
        s = "aaaaaaa"
        wordDict = ["a", "aa", "aaa"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_prefix_but_no_full_match(self):
        s = "aaaaab"
        wordDict = ["a", "aa", "aaa", "aaaa"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_long_word_exact_match(self):
        s = "longword"
        wordDict = ["longword"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_overlapping_choices(self):
        s = "catsanddog"
        wordDict = ["cats", "cat", "and", "sand", "dog"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))


if __name__ == "__main__":
    unittest.main()
