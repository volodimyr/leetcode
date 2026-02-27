import unittest
from reverse import Solution


class TestReverseWords(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        expected = ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
        self.solution.reverseWords(s)
        self.assertEqual(s, expected)

    def test_example_2(self):
        s = ["a"]
        expected = ["a"]
        self.solution.reverseWords(s)
        self.assertEqual(s, expected)

    def test_two_words(self):
        s = ["h","i"," ","t","h","e","r","e"]
        expected = ["t","h","e","r","e"," ","h","i"]
        self.solution.reverseWords(s)
        self.assertEqual(s, expected)

    def test_multiple_short_words(self):
        s = ["a"," ","b"," ","c"]
        expected = ["c"," ","b"," ","a"]
        self.solution.reverseWords(s)
        self.assertEqual(s, expected)

    def test_numbers_and_letters(self):
        s = ["1","2","3"," ","a","b","c"]
        expected = ["a","b","c"," ","1","2","3"]
        self.solution.reverseWords(s)
        self.assertEqual(s, expected)

    def test_long_single_word(self):
        s = list("helloworld")
        expected = list("helloworld")
        self.solution.reverseWords(s)
        self.assertEqual(s, expected)


if __name__ == "__main__":
    unittest.main()