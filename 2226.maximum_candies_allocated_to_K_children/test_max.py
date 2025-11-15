import unittest
from typing import List
from max import Solution

class TestMaximumCandies(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Example 1: Basic case with 3 children"""
        candies = [5, 8, 6]
        k = 3
        self.assertEqual(self.solution.maximumCandies(candies, k), 5)

    def test_example_2(self):
        """Example 2: Not enough candies"""
        candies = [2, 5]
        k = 11
        self.assertEqual(self.solution.maximumCandies(candies, k), 0)

    def test_single_pile_single_child(self):
        """Single pile, single child gets all"""
        candies = [10]
        k = 1
        self.assertEqual(self.solution.maximumCandies(candies, k), 10)

    def test_single_pile_multiple_children(self):
        """Single pile divided among multiple children"""
        candies = [20]
        k = 4
        self.assertEqual(self.solution.maximumCandies(candies, k), 5)

    def test_equal_distribution(self):
        """All piles same size, perfect division"""
        candies = [10, 10, 10, 10]
        k = 4
        self.assertEqual(self.solution.maximumCandies(candies, k), 10)

    def test_one_child(self):
        """Only one child, gets max pile"""
        candies = [1, 2, 3, 4, 5]
        k = 1
        self.assertEqual(self.solution.maximumCandies(candies, k), 5)

    def test_exact_division(self):
        """Piles divide exactly into k portions"""
        candies = [9, 12, 15]
        k = 12
        self.assertEqual(self.solution.maximumCandies(candies, k), 3)

    def test_large_k(self):
        """Very large k value (edge case from constraints)"""
        candies = [1, 2, 3]
        k = 1000000000000  # 10^12
        self.assertEqual(self.solution.maximumCandies(candies, k), 0)

    def test_all_ones(self):
        """All piles have size 1"""
        candies = [1, 1, 1, 1, 1]
        k = 5
        self.assertEqual(self.solution.maximumCandies(candies, k), 1)

    def test_all_ones_too_many_children(self):
        """All piles have size 1, but k is larger"""
        candies = [1, 1, 1]
        k = 5
        self.assertEqual(self.solution.maximumCandies(candies, k), 0)

    def test_large_piles(self):
        """Large pile values"""
        candies = [10000000, 10000000]
        k = 2
        self.assertEqual(self.solution.maximumCandies(candies, k), 10000000)

    def test_cannot_divide_evenly(self):
        """Candies cannot be divided evenly"""
        candies = [7, 11]
        k = 5
        self.assertEqual(self.solution.maximumCandies(candies, k), 3)

    def test_single_large_pile(self):
        """Single very large pile"""
        candies = [1000000]
        k = 100
        self.assertEqual(self.solution.maximumCandies(candies, k), 10000)

    def test_zero_children_edge_case(self):
        """Edge case: k = 1 (minimum from constraints)"""
        candies = [100]
        k = 1
        self.assertEqual(self.solution.maximumCandies(candies, k), 100)


def run_tests():
    """Run all tests and display results"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaximumCandies)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()