import unittest
from numbers import Solution   # adjust if your file name differs

class TestLargestNumber(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(Solution().largestNumber([10, 2]), "210")

    def test_example_2(self):
        self.assertEqual(Solution().largestNumber([3, 30, 34, 5, 9]), "9534330")

    def test_single_element(self):
        self.assertEqual(Solution().largestNumber([1]), "1")

    def test_zero(self):
        self.assertEqual(Solution().largestNumber([0]), "0")

    def test_all_zeros(self):
        self.assertEqual(Solution().largestNumber([0, 0]), "0")

    def test_prefix_case(self):
        # tricky: 121 vs 12
        self.assertEqual(Solution().largestNumber([121, 12]), "12121")

    def test_duplicates(self):
        self.assertEqual(
            Solution().largestNumber([8308, 8308, 830]),
            "83088308830"
        )

    def test_large_numbers(self):
        self.assertEqual(
            Solution().largestNumber([999999998, 999999997]),
            "999999998999999997"
        )

    def test_compare_edge_conflict(self):
        # 343 + 34 = 34334
        # 34 + 343 = 34343 → larger
        self.assertEqual(
            Solution().largestNumber([343, 34]),
            "34343"
        )

    def test_many_zeros_with_nonzero(self):
        self.assertEqual(
            Solution().largestNumber([0, 0, 1, 0]),
            "1000"
        )

    def test_max_input_size(self):
        nums = [10**9] * 100
        expected = "1000000000" * 100
        self.assertEqual(Solution().largestNumber(nums), expected)


if __name__ == "__main__":
    unittest.main()
