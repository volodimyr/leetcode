import unittest
from typing import List, Set, Tuple # Used for type hinting
from search import Solution

class TestFindWords(unittest.TestCase):
    
    def setUp(self):
        # Create a new instance of the solution before each test
        self.solution = Solution()

    ## Test Case 1: Basic functionality and dictionary example
    def test_basic_example(self):
        board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ]
        words = ["oath","pea","eat","rain"]
        expected = set(["oath", "eat"])
        
        result = set(self.solution.findWords(board, words))
        self.assertEqual(result, expected)

    ## Test Case 2: Words with shared prefixes (Trie pruning test)
    def test_shared_prefixes(self):
        board = [
            ["a","b","c"],
            ["a","e","d"],
            ["a","f","g"]
        ]
        words = ["a", "ab", "abc", "abcd", "abe"]
        expected = set(["a", "ab", "abc", "abe", "abcd"])
        
        result = set(self.solution.findWords(board, words))
        self.assertEqual(result, expected)

    ## Test Case 3: No words found
    def test_no_words_found(self):
        board = [
            ["x","y"],
            ["z","w"]
        ]
        words = ["hello", "world", "test"]
        expected = set()
        
        result = set(self.solution.findWords(board, words))
        self.assertEqual(result, expected)

    ## Test Case 4: Backtracking and non-linear paths
    def test_backtracking_required(self):
        board = [
            ["a", "b"],
            ["c", "d"]
        ]
        words = ["ac", "ab", "acb", "abd"] # "acb" requires backtracking from 'c' to 'b'
        expected = set(["ac", "ab", "abd"])
        
        result = set(self.solution.findWords(board, words))
        self.assertEqual(result, expected)

    ## Test Case 5: Single-cell board
    def test_single_cell(self):
        board = [["a"]]
        words = ["a", "b"]
        expected = set(["a"])
        
        result = set(self.solution.findWords(board, words))
        self.assertEqual(result, expected)

    ## Test Case 6: Larger grid with various words
    def test_larger_grid(self):
        board = [
            ["a","b","c","d"],
            ["s","a","a","t"],
            ["a","c","k","e"],
            ["a","c","d","n"]
        ]
        # From your original example: "bat","cat","back","backend","stack" -> ["cat","back","backend"]
        # bat: not found
        # cat: found
        # back: found
        # backend: found
        # stack: found (s->t->a->c->k) or (s->a->a->c->k)
        words = ["bat", "cat", "back", "backend", "stack", "sad", "sac"]
        expected = set(["cat", "back", "backend", "sac"])
        
        result = set(self.solution.findWords(board, words))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    # You would typically run this file directly in a terminal
    # python your_file_name.py
    unittest.main(argv=['first-arg-is-ignored'], exit=False)