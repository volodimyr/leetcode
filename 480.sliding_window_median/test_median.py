from typing import List
import unittest
from median import Solution

class TestSlidingWindowMedian(unittest.TestCase):
    
    # Utility to compare float arrays with a tolerance
    def assertFloatArraysClose(self, result: List[float], expected: List[float], tolerance: float = 1e-5):
        self.assertEqual(len(result), len(expected), "Output array length mismatch.")
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], delta=tolerance, 
                                   msg=f"Median mismatch at index {i}: {result[i]} vs {expected[i]}")

    ## 🧪 Test Case 1: Example from problem (Odd k)
    def test_example_one(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 2: Example from problem (Odd k, different numbers)
    def test_example_two(self):
        nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        k = 3
        expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 3: Even Window Size (k=4)
    def test_even_window_size(self):
        nums = [1, 2, 3, 4, 5, 6]
        k = 4
        # Windows: [1, 2, 3, 4] -> (2+3)/2=2.5 | [2, 3, 4, 5] -> (3+4)/2=3.5 | [3, 4, 5, 6] -> (4+5)/2=4.5
        expected = [2.5, 3.5, 4.5]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 4: Duplicates
    def test_with_duplicates(self):
        nums = [4, 1, 3, 4, 5, 2, 4]
        k = 4
        # [4, 1, 3, 4] -> sorted [1, 3, 4, 4] -> 3.5
        # [1, 3, 4, 5] -> sorted [1, 3, 4, 5] -> 3.5
        # [3, 4, 5, 2] -> sorted [2, 3, 4, 5] -> 3.5
        # [4, 5, 2, 4] -> sorted [2, 4, 4, 5] -> 4.0
        expected = [3.5, 3.5, 3.5, 4.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 5: Single Window (k == N)
    def test_k_equals_n(self):
        nums = [9, 8, 7, 6, 5]
        k = 5
        expected = [7.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 6: Edge Case (k = 1)
    def test_k_equals_one(self):
        nums = [10, 5, 15, 0]
        k = 1
        expected = [10.0, 5.0, 15.0, 0.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 7: Negative and Zero Values
    def test_negatives_and_zero(self):
        nums = [10, -5, 20, -10, 30, 0]
        k = 4
        # [10, -5, 20, -10] -> [-10, -5, 10, 20] -> 2.5
        # [-5, 20, -10, 30] -> [-10, -5, 20, 30] -> 7.5
        # [20, -10, 30, 0]  -> [-10, 0, 20, 30] -> 10.0
        expected = [2.5, 7.5, 10.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

    ## 🧪 Test Case 8: Only Negative Numbers
    def test_only_negatives(self):
        nums = [-10, -5, -20, -1]
        k = 3
        # [-10, -5, -20] -> [-20, -10, -5] -> -10.0
        # [-5, -20, -1] -> [-20, -5, -1] -> -5.0
        expected = [-10.0, -5.0]
        self.assertFloatArraysClose(Solution().medianSlidingWindow(nums, k), expected)

if __name__ == '__main__':
    # Running the tests might be helpful to see the result, 
    # but the custom Median class must be fixed for true passing.
    print("Running unit tests using a mocked, slow Median implementation.")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)