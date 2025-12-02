from compression import Solution
import unittest
from typing import List

class TestStringCompression(unittest.TestCase):
    """
    Test suite for the Solution.compress method.
    """

    def setUp(self):
        """Set up the Solution instance before each test method."""
        # Note: 'compression' is assumed to be the module where the Solution class is defined
        self.solution = Solution()

    # --- Standard Test Cases (Examples) ---

    def test_example_one(self):
        """Test case: ["a","a","b","b","c","c","c"] -> ["a","2","b","2","c","3"]"""
        chars: List[str] = ["a","a","b","b","c","c","c"]
        expected_len = 6
        expected_chars = ["a","2","b","2","c","3"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Example 1")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Example 1")

    def test_example_two_single_char(self):
        """Test case: ["a"] -> ["a"] (No compression)"""
        chars: List[str] = ["a"]
        expected_len = 1
        expected_chars = ["a"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Example 2")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Example 2")

    def test_example_three_large_group(self):
        """Test case: Group length 12 -> ["b","1","2"] (Split count)"""
        chars: List[str] = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected_len = 4
        expected_chars = ["a","b","1","2"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Example 3")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Example 3")

    # --- Edge Cases and Boundary Tests ---

    def test_no_compression_needed(self):
        """Test case: ["a","b","c","d"] (All unique characters)"""
        chars: List[str] = ["a","b","c","d"]
        expected_len = 4
        expected_chars = ["a","b","c","d"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for No Compression")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for No Compression")

    def test_single_group_length_ten(self):
        """Test case: Group length 10 -> ["o","1","0"] (Boundary test for 2 digits)"""
        chars: List[str] = ["o"] * 10
        expected_len = 3
        expected_chars = ["o","1","0"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Length 10")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Length 10")

    def test_maximum_length_100(self):
        """Test case: Group length 100 -> ["x","1","0","0"] (Boundary test for 3 digits)"""
        chars: List[str] = ["x"] * 100
        expected_len = 4
        expected_chars = ["x","1","0","0"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Length 100")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Length 100")

    def test_mixed_case_and_symbols(self):
        """Test case: Mixed cases and symbols -> ["A","2","a","2","!","3"]"""
        chars: List[str] = ["A","A","a","a","!","!","!"]
        expected_len = 6
        expected_chars = ["A","2","a","2","!","3"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Mixed Case/Symbol")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Mixed Case/Symbol")

    def test_empty_array(self):
        """Test case: [] -> [] (Empty input)"""
        chars: List[str] = []
        expected_len = 0
        expected_chars = []
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Empty Array")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Empty Array")

    def test_array_of_length_two(self):
        """Test case: ["h", "h"] -> ["h", "2"]"""
        chars: List[str] = ["h", "h"]
        expected_len = 2
        expected_chars = ["h", "2"]
        
        result_len = self.solution.compress(chars)
        
        self.assertEqual(result_len, expected_len, "Return length mismatch for Length 2")
        self.assertEqual(chars[:result_len], expected_chars, "Compressed array content mismatch for Length 2")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)