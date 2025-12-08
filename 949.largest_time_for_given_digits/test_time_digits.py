import unittest
from time_digits import Solution

class TestLargestTimeFromDigits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.largestTimeFromDigits([1,2,3,4]), "23:41")

    def test_example_2(self):
        self.assertEqual(self.sol.largestTimeFromDigits([5,5,5,5]), "")

    def test_all_zero(self):
        self.assertEqual(self.sol.largestTimeFromDigits([0,0,0,0]), "00:00")

    def test_no_valid_hour(self):
        # No arrangement can form hour < 24
        self.assertEqual(self.sol.largestTimeFromDigits([7,7,7,1]), "")

    def test_multiple_valid_same_prefix(self):
        self.assertEqual(self.sol.largestTimeFromDigits([2,3,5,9]), "23:59")

    def test_repeated_digits_valid(self):
        self.assertEqual(self.sol.largestTimeFromDigits([2, 2, 1, 1]), "22:11")

    def test_low_digits(self):
        self.assertEqual(self.sol.largestTimeFromDigits([0,1,2,3]), "23:10")

    def test_unsorted_input(self):
        self.assertEqual(self.sol.largestTimeFromDigits([4,3,2,1]), "23:41")

    def test_edge_case_2359(self):
        self.assertEqual(self.sol.largestTimeFromDigits([2,3,5,9]), "23:59")

    def test_no_valid_minute(self):
        self.assertEqual(self.sol.largestTimeFromDigits([2,4,6,0]), "20:46")

if __name__ == "__main__":
    unittest.main()
