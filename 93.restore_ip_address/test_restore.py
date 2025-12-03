import unittest
from typing import List
from restore import Solution

class TestRestoreIPAddresses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # --- Standard Examples ---
    
    def test_example_1_standard(self):
        s = "25525511135"
        expected = ["255.255.11.135", "255.255.111.35"]
        # Use assertCountEqual for lists where order doesn't matter
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)

    def test_example_2_zeros(self):
        s = "0000"
        expected = ["0.0.0.0"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)

    def test_example_3_leading_zeros_invalid_segments(self):
        s = "101023"
        expected = ["1.0.10.23", "1.0.102.3", "10.10.2.3", "10.102.3", "101.0.2.3"] # Wait, based on your logic "10.102.3" is not 4 segments.
        # Let's verify the correct set for "101023"
        correct_expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), correct_expected)
        
    # --- Edge Cases ---

    def test_minimum_length_valid(self):
        # "1.1.1.1" -> 4 characters
        s = "1111"
        expected = ["1.1.1.1"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)

    def test_maximum_length_valid(self):
        # "255.255.255.255" -> 12 characters
        s = "255255255255"
        expected = ["255.255.255.255"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)

    def test_too_short(self):
        # Length 3: Impossible to form 4 segments.
        s = "123"
        expected = []
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)

    def test_too_long(self):
        # Length 13: Impossible to form 4 segments (max length is 12).
        s = "1234567890123"
        expected = []
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)
        
    def test_contains_large_number_invalid(self):
        # Contains a segment that is > 255.
        s = "256256256256"
        expected = []
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)
        
    def test_valid_but_mixed_large_and_small(self):
        # Checks if it correctly skips "300" but finds "30.0.0.0"
        s = "3000000" 
        # Only valid segment is 3.0.0.0? No, 30.0.0.0 is not 7 chars.
        # 3.0.0.00 -> invalid segment 00
        # 30.0.0.0 -> invalid, 8 chars needed
        # 3.0.0.0.0... -> too many segments
        # Let's use a simpler case: "12345678"
        s = "12345678"
        expected = ["12.34.56.78", "1.234.56.78", "123.45.67.8"]
        # The correct set for "12345678" is:
        # 1.2.345.678 (Invalid >255)
        # 1.23.45.678 (Invalid >255)
        # 1.234.56.78 (Valid)
        # 12.3.456.78 (Invalid >255)
        # 12.34.56.78 (Valid)
        # 123.4.56.78 (Valid)
        # 123.45.6.78 (Valid)
        # 123.45.67.8 (Valid)
        correct_expected = ["1.234.56.78", "12.34.56.78", "123.4.56.78", "123.45.6.78", "123.45.67.8"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), correct_expected)

    # --- Leading Zero Cases ---

    def test_leading_zero_invalid_segment(self):
        # Checks if it correctly rejects "1.01.1.1" or "1.1.01.1" etc.
        s = "101010" # 6 chars
        # 1.0.1.010 (Invalid: 010)
        # 1.0.10.10 (Valid)
        # 1.01.0.10 (Invalid: 01)
        # 10.1.0.10 (Valid)
        # 10.10.1.0 (Valid)
        # 101.0.10 (Invalid length)
        expected = ["1.0.10.10", "10.1.0.10", "10.10.1.0", "1.0.101.0", "101.0.1.0"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)

    def test_all_zeros_with_invalid_segments(self):
        # Ensures "0.00.0.0" is rejected due to "00"
        s = "00000" # 5 chars
        # Only "0.0.0.0" is 4 chars, so must be 4*1 = 4 chars.
        # Length 5 can't be partitioned into 4 valid single-digit segments.
        self.assertCountEqual(self.solution.restoreIpAddresses(s), [])
        
    def test_leading_zero_at_start(self):
        s = "00100"
        # 0.0.1.00 (Invalid: 00)
        # 0.0.10.0 (Valid)
        # 0.01.0.0 (Invalid: 01)
        # 0.010.0 (Invalid: 010)
        # 0.0.100 (Invalid length)
        expected = ["0.0.10.0"]
        self.assertCountEqual(self.solution.restoreIpAddresses(s), expected)


if __name__ == '__main__':
    # This setup allows running the tests directly from the script
    unittest.main(argv=['first-arg-is-ignored'], exit=False)