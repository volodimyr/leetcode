import unittest
from median import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1, 3], [2]),
            2.0
        )

    def test_example_2(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1, 2], [3, 4]),
            2.5
        )

    def test_one_empty_array(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([], [1]),
            1.0
        )

    def test_other_empty_array(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([2], []),
            2.0
        )

    def test_both_single_element(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1], [2]),
            1.5
        )

    def test_even_total_length(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1, 3], [2, 4]),
            2.5
        )

    def test_odd_total_length(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1, 2, 3], [4, 5]),
            3.0
        )

    def test_negative_numbers(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([-5, -3, -1], [-2, 0]),
            -2.0
        )

    def test_duplicates(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1, 1, 1], [1, 1]),
            1.0
        )

    def test_large_gap(self):
        self.assertEqual(
            self.sol.findMedianSortedArrays([1, 2], [100, 101, 102]),
            100.0
        )


if __name__ == "__main__":
    unittest.main()
