import unittest
from palindrome import Solution     # adjust import to your file name


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        s = "a"
        expected = [["a"]]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)

    def test_no_multi_char_palindromes(self):
        s = "abc"
        expected = [["a", "b", "c"]]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)

    def test_all_same_char(self):
        s = "aaa"
        expected = [
            ["a", "a", "a"],
            ["a", "aa"],
            ["aa", "a"],
            ["aaa"]
        ]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)

    def test_even_length_palindromes(self):
        s = "abba"
        expected = [
            ["a", "b", "b", "a"],
            ["a", "bb", "a"],
            ["abba"]
        ]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)

    def test_complex_case(self):
        s = "racecar"
        expected = [
            ["r","a","c","e","c","a","r"],
            ["r","a","cec","a","r"],
            ["r","aceca","r"],
            ["racecar"]
        ]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)

    def test_large_non_palindromic(self):
        s = "abcdefg"
        expected = [["a","b","c","d","e","f","g"]]
        result = self.sol.partition(s)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
