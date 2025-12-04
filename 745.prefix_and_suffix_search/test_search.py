import unittest
from typing import List
from search import WordFilter

# --- Test Cases ---

class TestWordFilter(unittest.TestCase):

    def test_example_case(self):
        """Test the example provided in the problem description."""
        wf = WordFilter(["apple"])
        # "apple" starts with "a" and ends with "e" -> index 0
        self.assertEqual(wf.f("a", "e"), 0)

    def test_basic_functionality(self):
        """Test simple matches with distinct words."""
        words = ["apple", "banana", "orange"]
        wf = WordFilter(words)
        
        # 'banana': prefix 'b', suffix 'a' -> index 1
        self.assertEqual(wf.f("b", "a"), 1)
        # 'orange': prefix 'or', suffix 'ge' -> index 2
        self.assertEqual(wf.f("or", "ge"), 2)

    def test_return_largest_index(self):
        """If multiple words match, it should return the largest index."""
        # 'bat' appears at 0 and 2. 
        words = ["bat", "bar", "bat"]
        wf = WordFilter(words)
        
        # query matches both "bat" at 0 and "bat" at 2
        self.assertEqual(wf.f("b", "t"), 2) 

    def test_overlapping_words(self):
        """Test when distinct words match the same criteria."""
        # 'test' (0) and 'toast' (1).
        # Both start with 't' and end with 'st'.
        words = ["test", "toast"]
        wf = WordFilter(words)
        
        self.assertEqual(wf.f("t", "st"), 1)

    def test_no_match_cases(self):
        """Test cases where no word matches criteria."""
        words = ["apple", "banana"]
        wf = WordFilter(words)
        
        # Prefix matches, Suffix does not
        self.assertEqual(wf.f("app", "z"), -1)
        
        # Suffix matches, Prefix does not
        self.assertEqual(wf.f("z", "le"), -1)
        
        # Both exist independently in DIFFERENT words, but not the SAME word
        # "apple" has "a", "banana" has "a". 
        # But looking for prefix "b" (banana) and suffix "e" (apple)
        self.assertEqual(wf.f("b", "e"), -1)

    def test_full_word_match(self):
        """Test providing the full word as prefix and suffix."""
        wf = WordFilter(["cycle"])
        self.assertEqual(wf.f("cycle", "cycle"), 0)

    def test_single_character_words(self):
        """Test edge cases with single letter words."""
        words = ["a", "b", "a"]
        wf = WordFilter(words)
        
        self.assertEqual(wf.f("a", "a"), 2) # Last 'a' is at index 2
        self.assertEqual(wf.f("b", "b"), 1)
        self.assertEqual(wf.f("c", "c"), -1)

    def test_prefix_suffix_overlap(self):
        """Test when prefix and suffix overlap in the middle of the word."""
        # "ababa" -> starts with "aba", ends with "aba"
        wf = WordFilter(["ababa"])
        self.assertEqual(wf.f("aba", "aba"), 0)

    def test_queries_longer_than_words(self):
        """Test when prefix or suffix is longer than the word itself."""
        wf = WordFilter(["cat"])
        # Prefix "cats" is impossible for word "cat"
        self.assertEqual(wf.f("cats", "t"), -1)
        # Suffix "cats" is impossible for word "cat"
        self.assertEqual(wf.f("c", "cats"), -1)

if __name__ == '__main__':
    unittest.main()