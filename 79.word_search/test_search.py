import unittest
from typing import List
from search import Solution
# --- Unit Tests ---

class TestWordSearch(unittest.TestCase):
    """
    Unit tests for the Solution.exist method (Word Search).
    """

    def setUp(self):
        # Initialize the Solution class before each test
        self.solver = Solution()

    def test_example_1_found(self):
        """Test the standard example case where the word exists."""
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCCED"
        self.assertTrue(self.solver.exist(board, word), 
                        f"Expected True for '{word}'")

    def test_example_2_found(self):
        """Test the case where 'SEE' is found."""
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "SEE"
        self.assertTrue(self.solver.exist(board, word),
                        f"Expected True for '{word}'")

    def test_example_3_not_found_revisit(self):
        """Test the case where a cell must be revisited, which is not allowed."""
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCB"
        self.assertFalse(self.solver.exist(board, word),
                         f"Expected False for '{word}'")

    def test_simple_vertical_path(self):
        """Test a simple vertical path."""
        board = [["A", "B"], ["C", "D"]]
        word = "AC"
        self.assertTrue(self.solver.exist(board, word))
    
    def test_no_match(self):
        """Test a word that does not exist in the board."""
        board = [["A", "B"], ["C", "D"]]
        word = "EFG"
        self.assertFalse(self.solver.exist(board, word))

    def test_word_longer_than_board(self):
        """Test a word that is physically too long for the board."""
        board = [["A", "B"], ["C", "D"]]
        word = "ABCDA"
        self.assertFalse(self.solver.exist(board, word))

    def test_single_cell_board(self):
        """Test case for a 1x1 board."""
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solver.exist(board, word))
        word_2 = "B"
        self.assertFalse(self.solver.exist(board, word_2))

    def test_full_backtracking_required(self):
        """Test case requiring extensive backtracking across the board."""
        board = [
            ["a", "a"],
            ["a", "a"]
        ]
        word = "aaaa"
        self.assertTrue(self.solver.exist(board, word))


if __name__ == '__main__':
    # Run the tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)